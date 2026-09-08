# 启动入口脚本:负责转发参数并调用 modules/launch_utils 完成环境准备与启动流程。
# 🌐 本文件注释由 moodyawhvh/stable-diffusion-webui-chinese 汉化,原项目见 AUTOMATIC1111/stable-diffusion-webui。
from modules import launch_utils

# 从 launch_utils 暴露常用对象:命令行参数、python/git 可执行路径、仓库索引地址、本地仓库目录
args = launch_utils.args
python = launch_utils.python
git = launch_utils.git
index_url = launch_utils.index_url
dir_repos = launch_utils.dir_repos

# 当前提交哈希与 git 标签(用于版本展示与一致性检查)
commit_hash = launch_utils.commit_hash
git_tag = launch_utils.git_tag

# 环境准备与启动相关的工具函数:命令执行、依赖检查、pip 安装、仓库克隆/拉取、扩展管理等
run = launch_utils.run
is_installed = launch_utils.is_installed
repo_dir = launch_utils.repo_dir

run_pip = launch_utils.run_pip
check_run_python = launch_utils.check_run_python
git_clone = launch_utils.git_clone
git_pull_recursive = launch_utils.git_pull_recursive
list_extensions = launch_utils.list_extensions
run_extension_installer = launch_utils.run_extension_installer
prepare_environment = launch_utils.prepare_environment
configure_for_tests = launch_utils.configure_for_tests
start = launch_utils.start


def main():
    # --dump_sysinfo:收集系统信息并保存后直接退出(用于问题排查)
    if args.dump_sysinfo:
        filename = launch_utils.dump_sysinfo()

        print(f"Sysinfo saved as {filename}. Exiting...")

        exit(0)

    launch_utils.startup_timer.record("initial startup")

    # 准备运行环境:校验 python/git 版本、安装依赖、克隆所需仓库(可用 --skip-prepare-environment 跳过)
    with launch_utils.startup_timer.subcategory("prepare environment"):
        if not args.skip_prepare_environment:
            prepare_environment()

    # --test-server:按测试服务器模式初始化(供自动化测试使用)
    if args.test_server:
        configure_for_tests()

    # 启动 webui(或 --nowebui 模式下的 API 服务)
    start()


if __name__ == "__main__":
    main()
