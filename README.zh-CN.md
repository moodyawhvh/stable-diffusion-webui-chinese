<div align="center">

# stable-diffusion-webui 中文文档

[![原项目](https://img.shields.io/badge/原项目-AUTOMATIC1111--stable-diffusion-webui-blue?style=flat-square&logo=github)](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
[![GitHub Stars](https://img.shields.io/github/stars/AUTOMATIC1111/stable-diffusion-webui?style=flat-square&label=原项目Stars)](https://github.com/AUTOMATIC1111/stable-diffusion-webui/stargazers)
[![License](https://img.shields.io/badge/License-AGPL--3.0-lightgrey?style=flat-square)](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/LICENSE.txt)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

</div>

---

> 本文档是 [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 官方 README 的中文翻译,内容以原项目为准。

## 简介

Stable Diffusion Web UI:一个基于 Gradio 库实现的 Stable Diffusion 网页操作界面。

## 主要功能

[图文版功能展示(英文)](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features),以下为代表性条目:

- **文生图 / 图生图**:原生支持 txt2img 与 img2img 两种模式。
- **一键安装运行**:提供一键安装与运行脚本(仍需自备 Python 和 Git)。
- **局部重绘与扩图**:支持 Inpainting(局部重绘)、Outpainting(向外扩展)、Color Sketch 色彩素描。
- **提示词注意力控制**:
  - `a man in a ((tuxedo))` —— 让模型更关注"燕尾服";
  - `a man in a (tuxedo:1.21)` —— 等价的权重语法;
  - 选中文字后按 `Ctrl+Up` / `Ctrl+Down`(macOS 为 `Command+Up/Down`)可自动微调权重。
- **提示词矩阵 / X/Y/Z 图**:批量对比不同参数组合出图,绘制三维参数对比图。
- **Textual Inversion**:自定义 embeddings 数量不限、命名随意,支持每 token 多向量与半精度,8GB 显存即可训练(也有 6GB 成功案例)。
- **Extras 附加处理**:GFPGAN、CodeFormer 面部修复;RealESRGAN、ESRGAN、SwinIR、Swin2SR、LDSR 等神经网络超分放大。
- **采样器选择**:可选多种采样方法,支持调整 eta(噪声乘数)与更进阶的噪声参数。
- **生成参数还原**:出图参数随图保存(PNG 写入信息块,JPEG 写入 EXIF);把图片拖到 PNG Info 页即可还原并自动填回 UI;也可直接拖图/参数文本到提示词框。
- **负面提示词**:额外文本框,列出不想在图中出现的元素。
- **样式与变化**:Styles 可保存部分提示词并从下拉框快速套用;Variations 可生成仅有微小差异的同图。
- **CLIP 反推提示词**:一键根据图片猜测提示词。
- **提示词中途编辑**:生成过程中切换提示词,比如先画西瓜、中途切成动漫少女。
- **Highres Fix**:一键生成高分辨率图片而不出现常规畸变。
- **检查点合并器**:最多合并 3 个 checkpoint 为一个;支持模型运行中热加载。
- **任意提示词长度**:突破原版 75 token 上限;支持大写 `AND` 组合多提示词并可带权重,如 `a cat :1.2 AND a dog`。
- **批量处理**:img2img 批量处理一组文件。
- **训练选项卡**:训练 hypernetworks 与 embeddings,支持图像预处理(裁剪、镜像、BLIP / DeepDanbooru 自动打标)。
- **LoRA / Hypernetwork 选择器**:独立界面带预览地选择要加入提示词的 embeddings、hypernetworks 或 LoRA。
- **4GB 显卡可用**(也有 2GB 成功案例);[xformers](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers) 可为特定显卡带来大幅提速(命令行加 `--xformers`)。
- **进度条与实时预览**:可用独立神经网络生成近乎零显存开销的预览图;显示预计完成时间。
- **其他**:种子批量正确性、token 长度实时校验、可平铺纹理(Tiling)、中断生成、随时重读模型、UI 默认值/范围可经文本配置修改、UI 元素可排序、设置页、悬浮提示、内置 API 等。
- **模型支持**:Stable Diffusion 2.0、[Alt-Diffusion](https://arxiv.org/abs/2211.06679)、Segmind SSD-1B、RunwayML 专用 inpainting 模型、safetensors 格式;分辨率只需为 8 的倍数(原为 64)。
- **扩展生态**:社区自定义脚本;经扩展可实现历史图片浏览、[美学梯度](https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients)等。

## 安装与运行

请先确认满足[依赖要求](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies),再按你的硬件阅读对应指南:

- [NVIDIA 显卡(推荐)](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs)
- [AMD 显卡](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs)
- [Intel CPU / Intel GPU(核显与独显)](https://github.com/openvinotoolkit/stable-diffusion-webui/wiki/Installation-on-Intel-Silicon)(外部 Wiki)
- [Ascend NPU](https://github.com/wangshuai09/stable-diffusion-webui/wiki/Install-and-run-on-Ascend-NPUs)(外部 Wiki)

也可以使用 Google Colab 等在线服务,在线服务列表见 [Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services)。

### Windows 10/11 + NVIDIA 显卡(发行包方式)

1. 从 [v1.0.0-pre](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.0.0-pre) 下载 `sd.webui.zip` 并解压。
2. 运行 `update.bat`。
3. 运行 `run.bat`。

> 更多细节参见 [Install-and-Run-on-NVidia-GPUs](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs)。

### Windows 自动安装

1. 安装 [Python 3.10.6](https://www.python.org/downloads/release/python-3106/)(更新的 Python 版本不受 torch 支持),安装时勾选 "Add Python to PATH"。
2. 安装 [git](https://git-scm.com/download/win)。
3. 下载本仓库,例如:
   ```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
   ```
4. 在资源管理器中双击运行 `webui-user.bat`(请使用普通非管理员账户)。

### Linux 自动安装

1. 安装依赖:

   ```bash
   # Debian 系:
   sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
   # Red Hat 系:
   sudo dnf install wget git python3 gperftools-libs libglvnd-glx
   # openSUSE 系:
   sudo zypper install wget git python3 libtcmalloc4 libglvnd
   # Arch 系:
   sudo pacman -S wget git python3
   ```

   如果系统非常新,需要另装 python3.10 或 python3.11:

   ```bash
   # Ubuntu 24.04
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.11

   # Manjaro / Arch
   sudo pacman -S yay
   yay -S python311 # 注意不要与 python3.11 包搞混

   # 仅 3.11 需要:在启动脚本中设置环境变量
   export python_cmd="python3.11"
   # 或在 webui-user.sh 中:
   python_cmd="python3.11"
   ```

2. 进入想要安装的目录并执行:

   ```bash
   wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
   ```

   或者直接把仓库克隆到任意位置:

   ```bash
   git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
   ```

3. 运行 `./webui.sh`。
4. 启动选项见 `webui-user.sh`。

### Apple Silicon

安装说明见 [Installation-on-Apple-Silicon](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon)。

## 参与贡献

向本仓库提交代码的方法见 [Contributing](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Contributing)。

## 文档

项目文档已从 README 迁移至项目 [Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki)。

## 致谢(节选)

借用代码的许可证可在 `Settings -> Licenses` 页面及 `html/licenses.html` 文件中查看。部分致谢对象:

- Stable Diffusion:https://github.com/Stability-AI/stablediffusion 、https://github.com/CompVis/taming-transformers
- k-diffusion:https://github.com/crowsonkb/k-diffusion.git
- GFPGAN / CodeFormer / ESRGAN / SwinIR / Swin2SR / LDSR / MiDaS 等面部修复与超分模型作者
- Textual Inversion:Rinon Gal — https://github.com/rinongal/textual_inversion
- CLIP interrogator:https://github.com/pharmapsychotic/clip-interrogator
- xformers:https://github.com/facebookresearch/xformers
- DeepDanbooru:https://github.com/KichangKim/DeepDanbooru
- UniPC sampler、TAESD、LyCORIS、Hypertile 等算法作者
- 最初的 Gradio 脚本由一位匿名用户发布于 4chan,感谢这位匿名用户。

完整致谢列表以原项目 README 为准。

---

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的中文翻译版本,仅用于学习交流,所有代码版权归原项目作者 AUTOMATIC1111 所有,遵循其原始许可证(AGPL-3.0)。

**如果觉得有用,请给原项目点个 Star!** ⭐
