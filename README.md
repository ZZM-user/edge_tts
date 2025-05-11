# 🎧 Dify Edge-TTS 插件

> ⚡️ 为你的 Dify 智能体赋予真实、生动、多语种的语音合成功能 —— 基于微软 Edge TTS 引擎。

## 🚀 插件简介

**Dify Edge-TTS 插件** 通过集成微软的 Edge TTS 引擎，让文本转化为自然流畅的语音。无论是小说播讲、短视频配音，还是为无障碍应用提供语音支持，它都能胜任。

### 🔊 插件特性

- 支持 **100+ 神经网络语音模型**
- 覆盖 **45+ 种语言和地区**
- 支持设置语速、语调、音频格式（如 `wav`）等参数

## 🧩 适用场景

- 小说 / 剧情类短视频自动配音
- 聊天 / 问答智能体语音输出
- 教育、语言学习、阅读辅助
- 无障碍设备语音提示
- 内容创作流程自动化

## 🛠 安装与配置

### 📦 安装方式

你可以通过以下两种方式安装本插件：

1. **通过 Dify Marketplace 安装**（推荐）
2. **手动安装**：
    - 克隆本仓库或下载 `.difypkg` 文件
    - 上传到你的 Dify 实例中进行本地安装

### 🔐 前置准备：获取 API 密钥

前往 Microsoft Azure 语音服务平台申请免费 TTS 服务，并获取以下信息：

- `speech_key`（你的 Azure TTS API Key）
- `service_region`（如：`eastasia`、`westeurope` 等）

👉 [Azure TTS 控制台](https://speech.azure.cn/portal/voicegallery)

> ⚠️ 需使用中国区语音服务请切换至 Azure 中国站点。
