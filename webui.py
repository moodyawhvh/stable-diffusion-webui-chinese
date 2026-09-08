# 🌐 本文件注释由 moodyawhvh/stable-diffusion-webui-chinese 汉化,原项目见 AUTOMATIC1111/stable-diffusion-webui。
from __future__ import annotations

import os
import time

from modules import timer
from modules import initialize_util
from modules import initialize

# 启动计时器:记录各阶段耗时,启动完成后打印汇总
startup_timer = timer.startup_timer
startup_timer.record("launcher")

initialize.imports()  # 预注册/导入各模块声明的依赖,统一管理 import 时机

initialize.check_versions()  # 校验 python 与关键依赖的版本是否满足要求


def create_api(app):
    """在给定的 FastAPI 应用上挂载 webui 的 API。"""
    from modules.api.api import Api
    from modules.call_queue import queue_lock

    api = Api(app, queue_lock)
    return api


def api_only():
    """--nowebui 模式:不构建 UI,只启动 API 服务。"""
    from fastapi import FastAPI
    from modules.shared_cmd_options import cmd_opts

    initialize.initialize()  # 完成模型、设置、扩展等全局初始化

    app = FastAPI()
    initialize_util.setup_middleware(app)
    api = create_api(app)

    from modules import script_callbacks
    # 依次触发扩展的 before_ui 与 app_started 回调(无 UI 场景 demo 传 None)
    script_callbacks.before_ui_callback()
    script_callbacks.app_started_callback(None, app)

    print(f"Startup time: {startup_timer.summary()}.")
    api.launch(
        server_name=initialize_util.gradio_server_name(),
        port=cmd_opts.port if cmd_opts.port else 7861,
        root_path=f"/{cmd_opts.subpath}" if cmd_opts.subpath else ""
    )


def webui():
    """常规模式:构建 gradio UI 并循环处理 stop/restart 命令。"""
    from modules.shared_cmd_options import cmd_opts

    launch_api = cmd_opts.api  # 是否随 UI 一起启动 API
    initialize.initialize()

    from modules import shared, ui_tempdir, script_callbacks, ui, progress, ui_extra_networks

    while 1:
        # 外层循环支持 UI 热重载:restart 时销毁当前 demo 并重建
        if shared.opts.clean_temp_dir_at_start:
            ui_tempdir.cleanup_tmpdr()  # 启动时按设置清理临时输出目录
            startup_timer.record("cleanup temp dir")

        script_callbacks.before_ui_callback()  # 扩展在 UI 构建前的回调
        startup_timer.record("scripts before_ui_callback")

        shared.demo = ui.create_ui()  # 构建 gradio Blocks 界面
        startup_timer.record("create ui")

        if not cmd_opts.no_gradio_queue:
            shared.demo.queue(64)  # 启用 gradio 队列,默认并发 64

        gradio_auth_creds = list(initialize_util.get_gradio_auth_creds()) or None

        auto_launch_browser = False
        # SD_WEBUI_RESTARTING=1 表示这是热重载后的重启,不再自动开浏览器
        if os.getenv('SD_WEBUI_RESTARTING') != '1':
            if shared.opts.auto_launch_browser == "Remote" or cmd_opts.autolaunch:
                auto_launch_browser = True
            elif shared.opts.auto_launch_browser == "Local":
                auto_launch_browser = not cmd_opts.webui_is_non_local

        # 启动 gradio;prevent_thread_lock 让 launch 不阻塞,便于主循环监听服务器命令
        app, local_url, share_url = shared.demo.launch(
            share=cmd_opts.share,
            server_name=initialize_util.gradio_server_name(),
            server_port=cmd_opts.port,
            ssl_keyfile=cmd_opts.tls_keyfile,
            ssl_certfile=cmd_opts.tls_certfile,
            ssl_verify=cmd_opts.disable_tls_verify,
            debug=cmd_opts.gradio_debug,
            auth=gradio_auth_creds,
            inbrowser=auto_launch_browser,
            prevent_thread_lock=True,
            allowed_paths=cmd_opts.gradio_allowed_path,
            app_kwargs={
                "docs_url": "/docs",
                "redoc_url": "/redoc",
            },
            root_path=f"/{cmd_opts.subpath}" if cmd_opts.subpath else "",
        )

        startup_timer.record("gradio launch")

        # gradio 通过 app.user_middleware 默认使用非常宽松的 CORS 策略,这让攻击者可以诱导用户
        # 打开恶意 HTML 页面,向运行中的 webui 发起请求并执行任意操作(包括安装扩展并运行其代码)。
        # 这里移除 CORSMiddleware 以封堵该风险。方案来自 RyotaK。
        app.user_middleware = [x for x in app.user_middleware if x.cls.__name__ != 'CORSMiddleware']

        initialize_util.setup_middleware(app)

        progress.setup_progress_api(app)  # 进度查询 API
        ui.setup_ui_api(app)

        if launch_api:
            create_api(app)  # 按需在同一个 app 上挂载 API

        ui_extra_networks.add_pages_to_demo(app)

        startup_timer.record("add APIs")

        with startup_timer.subcategory("app_started_callback"):
            script_callbacks.app_started_callback(shared.demo, app)  # 通知扩展服务已启动

        timer.startup_record = startup_timer.dump()
        print(f"Startup time: {startup_timer.summary()}.")

        try:
            # 主循环:阻塞等待服务器命令(stop/restart),5 秒轮询一次
            while True:
                server_command = shared.state.wait_for_server_command(timeout=5)
                if server_command:
                    if server_command in ("stop", "restart"):
                        break
                    else:
                        print(f"Unknown server command: {server_command}")
        except KeyboardInterrupt:
            print('Caught KeyboardInterrupt, stopping...')
            server_command = "stop"

        if server_command == "stop":
            print("Stopping server...")
            # 捕获到键盘中断:关闭服务并退出进程。
            shared.demo.close()
            break

        # 热重载后续不再自动打开浏览器
        os.environ.setdefault('SD_WEBUI_RESTARTING', '1')

        print('Restarting UI...')
        shared.demo.close()
        time.sleep(0.5)
        startup_timer.reset()  # 重置计时器,重新统计本轮启动耗时
        script_callbacks.app_reload_callback()  # 通知扩展 UI 即将重载
        startup_timer.record("app reload callback")
        script_callbacks.script_unloaded_callback()  # 通知扩展脚本卸载,释放资源
        startup_timer.record("scripts unloaded callback")
        initialize.initialize_rest(reload_script_modules=True)  # 重新初始化并重载脚本模块,回到循环顶部重建 UI


if __name__ == "__main__":
    from modules.shared_cmd_options import cmd_opts

    # --nowebui:纯 API 模式;否则启动完整 webui
    if cmd_opts.nowebui:
        api_only()
    else:
        webui()
