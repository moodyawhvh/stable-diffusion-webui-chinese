<div align="center">

# stable-diffusion-webui 中文翻译版

**[中文版] stable-diffusion-webui — 功能最全的 Stable Diffusion Web 图形界面,文生图/图生图一站式上手**

[![原项目](https://img.shields.io/badge/原项目-AUTOMATIC1111--stable-diffusion-webui-blue?style=flat-square&logo=github)](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/AUTOMATIC1111/stable-diffusion-webui?style=flat-square&label=原项目Stars)](https://github.com/AUTOMATIC1111/stable-diffusion-webui/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/AUTOMATIC1111/stable-diffusion-webui

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

stable-diffusion-webui 是目前最流行的 Stable Diffusion Web 界面,基于 Gradio 实现,把文生图(txt2img)、图生图(img2img)、图像放大、面部修复、模型训练等功能全部集成在一个浏览器页面里。它一键安装脚本开箱即用,支持 NVIDIA / AMD / Intel 以及 Apple Silicon 等多种硬件,配合海量社区扩展,是本地 AI 绘图的事实标准。

## ✨ 主要特性

- 原生 txt2img 文生图与 img2img 图生图模式
- 一键安装与运行脚本(仍需自行安装 Python 和 Git)
- 局部重绘(Inpainting)与向外扩展绘制(Outpainting)
- 提示词注意力权重控制,如 `((tuxedo))`、`(tuxedo:1.21)`,选中文字按 `Ctrl+Up/Down` 微调
- 提示词矩阵、X/Y/Z 参数对比图、循环回推、变化生成等批量实验工具
- Textual Inversion 嵌入训练,8GB 显存即可训练 embeddings
- Extras 选项卡:GFPGAN / CodeFormer 面部修复,RealESRGAN / ESRGAN / SwinIR / LDSR 超分辨率放大
- 生成参数随图片保存(PNG 信息块 / EXIF),拖入图片即可还原全部参数
- 负面提示词、样式预设、CLIP 反推提示词、提示词中途编辑
- Highres Fix 一键高分辨率修复、检查点合并器、模型热切换加载
- 4GB 显卡可用(有 2GB 成功案例),xformers 加速,进度条与实时预览
- LoRA / Hypernetwork / 嵌入选择器界面,训练选项卡含图像预处理
- 支持 Stable Diffusion 2.0、Alt-Diffusion、Segmind SSD-1B、safetensors 格式
- 内置 API,支持社区自定义脚本与扩展生态

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

Windows(NVIDIA 显卡,推荐):

1. 确保已安装 [Python 3.10.6](https://www.python.org/downloads/release/python-3106/)(勾选 Add Python to PATH)和 [git](https://git-scm.com/download/win)。
2. 克隆仓库:
   ```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
   ```
3. 双击运行 `webui-user.bat`(普通用户身份,不要用管理员)。
4. 浏览器打开 `http://127.0.0.1:7860` 开始生图。

Linux:

1. 安装依赖:
   ```bash
   # Debian 系:
   sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
   # Red Hat 系:
   sudo dnf install wget git python3 gperftools-libs libglvnd-glx
   ```
2. 在目标目录执行:
   ```bash
   wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
   ```
3. 运行 `./webui.sh`,参数配置见 `webui-user.sh`。

AMD GPU、Intel 核显/独显、Apple Silicon 及 Ascend NPU 的安装说明见原项目 Wiki;也可使用 Google Colab 等在线服务运行。

完整源代码与最新版本请访问原项目:https://github.com/AUTOMATIC1111/stable-diffusion-webui

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。

**如果觉得有用,请给原项目点个 Star!** ⭐
