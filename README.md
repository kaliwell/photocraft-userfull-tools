# PhotoCraft Userfull Tools

**统一版入口**：最新合并源码在 [photocraft-codex-ai](https://github.com/kaliwell/photocraft-codex-ai)。Codex AI、参考图、长图切割与复制画布现在可在同一个 PhotoCraft 0.20.1 中使用，不需要分开运行。本次未发布新整合包，下方 v0.3.8 为此前的独立版本。

**Unified build:** the latest merged source lives in [photocraft-codex-ai](https://github.com/kaliwell/photocraft-codex-ai). One PhotoCraft 0.20.1 hosts Codex AI, references, the cutter and clipboard export. No new package is published for this merge; v0.3.8 below is the earlier standalone release.

[中文功能使用图](https://github.com/kaliwell/photocraft-codex-ai/blob/main/docs/usage-zh.md) · [English illustrated guide](https://github.com/kaliwell/photocraft-codex-ai/blob/main/docs/usage-en.md)

> Screenshots in these guides show the unified development build; they do not describe every feature in the standalone v0.3.8 ZIP.

> 使用图展示的是统一开发版，不代表独立 v0.3.8 ZIP 包含其中全部功能。

**Native PhotoCraft tools with Codex AI, long-image slicing, and clipboard export.**

**PhotoCraft 原生增强工具：Codex AI、长图切割和剪贴板导出。**

[中文](#中文说明) · [English](#english) · [Download v0.3.8 / 下载](https://github.com/kaliwell/photocraft-userfull-tools/releases/tag/v0.3.8)

Based on PhotoCraft **0.19.0** and the upstream Codex AI integration **v0.3.1**. Current toolkit: **v0.3.8**, Windows x64 portable development build.

## 中文说明

**语言切换（0.3.8）**：编辑 → 首选项 → 界面 → 语言，选择 English 或中文并应用。AI 工具栏、切图窗口及常用任务提示随编辑器设置切换，无需单独重启插件。用户提示词和文件名保留原文。

参考图功能已从 Userfull Tools 移除，改由[原 Codex AI 插件](https://github.com/kaliwell/photocraft-codex-ai)提供。

### 功能

- **选区 AI 编辑**：在选区下方局部修改、移除物体或生成图片，结果导入新图层，可撤销。
- **长图切割**：单栏大图、最大化/还原、切割线编辑和撤销、PNG ZIP 导出、方案自动恢复及 LongPicCutter JSON 互通。
- **复制完整画布**：顶部“复制图片”或“文件 → 导出 → 导出到剪贴板”，保留透明度，无需先保存到文件夹。
- **尺寸适配与羽化**：默认方图生成；局部编辑使用方形补边参考图和原画布反向映射，仅应用选区。支持可编辑向内羽化、蒙版形状和 0–1000 px 调整。

### 下载与安装

1. 打开 [v0.3.8 发布页](https://github.com/kaliwell/photocraft-userfull-tools/releases/tag/v0.3.8)，下载 **`photocraft-codex-ai-0.3.8-windows-x64-local-node.zip`** 和对应的 `.sha256` 文件。
2. 完整解压到可写的新目录，运行 **`start.cmd`**。
3. 使用本机 Node.js 和 Codex CLI；如需安装 CLI，运行 `npm.cmd install -g @openai/codex`。首次启动按提示登录自己的账号；也可用 `login.cmd` 重新登录。
4. 打开图片、创建选区，即可使用 AI 工具栏。长图切割与复制图片位于顶部标题栏。

包内包含 PhotoCraft 0.19.0、Python 3.13.5、Pillow 11.3.0 和源码补丁；**不包含 Node.js、Codex CLI 或账号凭据**。AI 需要网络及支持相应生图能力的账号。

需要 HTTP/混合代理时，在解压目录创建 `runtime/codex-proxy.json`，将端口改为自己的配置：

```json
{"url":"http://127.0.0.1:7888"}
```

更新前保存文档并关闭旧版，再解压本仓库的新整合包；可复制自己的代理配置、偏好设置和切图方案。请通过本仓库整合包更新定制工具。

### 说明与验证

[长图切割与尺寸适配](docs/long-image-cutter.md) · [发布说明](RELEASE_NOTES.md) · [验证记录](VALIDATION.md)


## English

**Language switching (0.3.8):** choose **Edit → Preferences → Interface → Language**, then apply your selection. The AI composer, cutter and standard job messages follow the editor language without a separate plugin restart. User prompts and filenames are preserved. Untranslated languages fall back to English; third-party messages retain their original wording.

PhotoCraft Userfull Tools extends the native PhotoCraft editor with selection-based Codex AI workflows and practical image utilities. It uses your locally installed Codex CLI and your own sign-in.

Reference images have moved to the [original Codex AI plugin](https://github.com/kaliwell/photocraft-codex-ai).

### Features

- **Selection AI editing:** fill, remove objects, or generate artwork from the floating selection toolbar. Results become new layers with undo support.
- **Long-image cutter:** a large, resizable single-source window with Maximize/Restore, editable cut lines, undo, lossless PNG ZIP export, local plan recovery, and LongPicCutter-compatible JSON import/export.
- **Full-canvas clipboard export:** use **Copy image** in the title bar or **File → Export → Export to Clipboard**. Copies the visible composite with transparency without creating an export file.
- **Image-size adaptation and feathering:** square generation by default, letterboxed editing references with inverse canvas mapping, selection-only application, and editable inward-feathered layer masks with shape and 0–1000 px controls.

### Download and run

1. Open the [v0.3.8 release](https://github.com/kaliwell/photocraft-userfull-tools/releases/tag/v0.3.8). Download **`photocraft-codex-ai-0.3.8-windows-x64-local-node.zip`** and its `.sha256` checksum.
2. Extract the complete archive into a new writable directory and run **`start.cmd`**.
3. Use your existing Node.js and Codex CLI. If needed, install the CLI with `npm.cmd install -g @openai/codex`. Sign in with your own account when prompted, or run `login.cmd` to sign in again.
4. Open an image and make a selection to display the AI composer. The cutter and clipboard buttons are in the title bar.

Includes PhotoCraft 0.19.0, Python 3.13.5, Pillow 11.3.0, and the native source patch. **Node.js, Codex CLI, and account credentials are not bundled.** AI features require network access and an account with the relevant image-generation capability.

For an HTTP/mixed proxy, create `runtime/codex-proxy.json` with `{"url":"http://127.0.0.1:7888"}` and substitute your own port. Before upgrading, save documents and close the old version, then extract the new toolkit into a separate directory. Copy your own proxy configuration, preferences, and cutting plans as needed. Update customized tools through this repository’s portable releases.

### Limits and validation

The plugin imposes no fixed reference-image count; actual Codex/model/tool errors are surfaced. Local resource guards still apply. Unexpected model framing or aspect ratios may introduce adaptation errors; original generated files are retained. Clipboard and slice exports use RGBA8.

See [cutter instructions](docs/long-image-cutter.md), [release notes](RELEASE_NOTES.md), and [validation records](VALIDATION.md). Focused tests, local GUI checks, Clippy and wasm checks are documented there. Live multi-image generation was not requested during reference-image QA; the full historical regression suite is not entirely green. This remains a development preview.

### Source and attribution

- [PhotoCraft](https://github.com/storytold/photocraft), baseline `2df9f807702a935184041355a86405380bda8274` (0.19.0), MIT OR Apache-2.0.
- [Upstream Codex AI integration](https://github.com/kaliwell/photocraft-codex-ai), v0.3.1.
- The cutter workflow was inspired by [LongPicCutter](https://github.com/kaliwell/LongPicCutter) and independently implemented in Rust/egui; no source or assets from that project are included.

Build instructions: [native-source/README.md](native-source/README.md). Licenses and notices: [THIRD_PARTY.md](THIRD_PARTY.md), with upstream notices included alongside the editor binary.
