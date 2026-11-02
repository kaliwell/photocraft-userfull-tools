# PhotoCraft Codex AI v0.2.11 · 顶部复制图片 / Title-bar Copy image

顶部标题栏月亮图标左侧新增“复制图片”按钮，直接调用现有的完整画布剪贴板导出功能。无文档或系统图片剪贴板不可用时禁用；窗口过窄时隐藏按钮，仍可从文件导出菜单使用。

Adds a Copy image button immediately before the appearance icon in the title bar. It uses the existing full-canvas clipboard export, is disabled without an open document or image clipboard service, and hides on narrow windows while remaining available in the File export menu.

## 中文

新增 **文件 → 导出 → 导出到剪贴板**。将当前画布的可见图层合成结果直接复制为系统剪贴板图片，在其他软件按 **Ctrl+V** 粘贴，无需选择文件夹或创建导出文件。

- 复制完整画布尺寸，保留透明度，不受当前选区或活动图层影响。
- 不改变文档、选区、图层和撤销记录，也不调用 AI 或消耗生成额度。
- 即使关闭了自动复制到系统剪贴板的偏好设置，手动导出仍然可用。
- 剪贴板不可用或被其他程序占用时显示错误，并保留原有内部复制内容。
- 系统图片格式为 8-bit RGBA，支持最多 6400 万像素；接收软件可能自行丢弃透明度。
- 保留已有的原生选区 AI 工具栏及可编辑蒙版功能。

此包为 Windows x64 开发预览版，包含配套 PhotoCraft、Python 与 Pillow，使用本机 Node.js 和已安装的 Codex CLI。保存文档并关闭旧版后，从新版 `start.cmd` 启动。

## English

Adds **File → Export → Export to Clipboard**. Copy the composite of the current canvas's visible layers directly as a system clipboard image, then press **Ctrl+V** in another app. No folder picker or export file is required.

- Copies the full canvas with transparency, regardless of the current selection or active layer.
- Leaves the document, selection, layers, and undo history unchanged. No AI call or generation quota is needed.
- Explicit export works even when automatic Copy mirroring to the system clipboard is disabled.
- Reports an unavailable or busy clipboard and preserves the previous internal clipboard contents on failure.
- Uses 8-bit RGBA with a 64-million-pixel limit. The receiving app may discard transparency.
- Retains the native selection AI toolbar and editable masks.

This Windows x64 development preview includes the matching PhotoCraft editor, Python, and Pillow. It uses local Node.js and an installed Codex CLI. Save documents and close the old version before launching the new `start.cmd`.
