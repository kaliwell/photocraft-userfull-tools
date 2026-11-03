# PhotoCraft Userfull Tools v0.3.6

Windows x64 portable development preview · PhotoCraft 0.19.0

## 中文

本次发布整合多图参考及此前工具版的长图切割、剪贴板导出和尺寸适配功能。

- **多图参考**：拖入或多选图片，显示编号缩略图，支持单张移除和横向滚动。参考图按顺序作为真实附件发送给 Codex，“图1/图2”按参考图编号解释。
- 不固定图片张数，显示 Codex 实际输入错误；保留本地资源保护。参考图保留像素尺寸，支持 EXIF 转正。
- **长图切割**：单栏大图、最大化/还原、切割线编辑和撤销、PNG ZIP、自动恢复及 LongPicCutter JSON 互通。
- **复制图片**：顶部按钮或文件导出菜单复制完整可见画布，保留透明度，无需导出到文件夹。
- **尺寸适配**：默认 1:1 生图；局部编辑使用方形补边参考图和反向映射，按原选区导入，保留可编辑向内羽化。

### 下载与启动

下载 **`photocraft-codex-ai-0.3.6-windows-x64-local-node.zip`**，完整解压到新目录，运行 **`start.cmd`**。使用同名 `.zip.sha256` 文件核对下载。

包含 PhotoCraft 0.19.0、Python 3.13.5 和 Pillow 11.3.0；沿用本机 Node.js、Codex CLI 和自己的登录，不含账号凭据。AI 需要网络及相应生图能力。更新前保存文档并关闭旧版；需要代理时复制自己的 `runtime/codex-proxy.json`。

### 验证与限制

52 项 Python 测试、8 项原生 AI 工具栏测试，以及 UI Clippy、wasm 和源码补丁反向校验通过。5 张测试图验证显示、移除及请求附件字节与顺序；真实多选窗口支持添加到 6 张。测试未额外请求真实 AI 生图。拖放路由通过原生 dropped-file handle 测试；自动化环境中的 OS 级拖动模拟未完成。

仍为开发预览，全量历史回归并非全绿。异常模型构图/比例可能导致适配误差；原始生成文件保留。完整记录见 `VALIDATION.md`。

## English

This release combines multi-image references with the toolkit’s long-image cutter, clipboard export, and image-size adaptation.

- **Multiple image references:** drag pictures onto the AI composer or select several. Numbered thumbnails support removal and horizontal scrolling. Actual image attachments are sent to Codex in order; numbered pictures in prompts refer to user references.
- No fixed image-count cap. Actual Codex input errors are surfaced, with local resource guards. References retain their pixel dimensions and are corrected for EXIF orientation.
- **Long-image cutter:** large single-source window, Maximize/Restore, editable cut lines, undo, PNG ZIP export, local plan recovery, and LongPicCutter JSON interchange.
- **Copy image:** title-bar and File/Export commands copy the full visible canvas with transparency, without an export file.
- **Size adaptation:** square generation by default; Fill/Remove use letterboxed references and inverse canvas mapping for selection-only import. Editable inward feathering remains available.

### Download and run

Download **`photocraft-codex-ai-0.3.6-windows-x64-local-node.zip`**, extract it completely into a new directory, and run **`start.cmd`**. Verify the archive with the accompanying `.zip.sha256` file.

Includes PhotoCraft 0.19.0, Python 3.13.5, and Pillow 11.3.0. Uses your local Node.js, Codex CLI, and sign-in; no account credentials are bundled. AI features require network access and the relevant image-generation capability. Save documents and close the old version before upgrading. Copy your own `runtime/codex-proxy.json` if required.

### Validation and limitations

52 Python tests, eight native AI-toolbar tests, UI Clippy, wasm, and reverse-patch checks passed. Five pictures verified gallery/removal and exact outgoing attachment bytes/order. The native multi-select dialog added pictures to a six-image batch. No extra live AI generation was requested. Native dropped-file handles exercised drag routing; OS-level drag simulation did not complete in the automation environment.

This remains a development preview; the historical full regression suite is not entirely green. Unexpected model framing/aspect ratios may introduce adaptation errors. Original generated files are retained. See `VALIDATION.md` for details.

## Earlier toolkit changes / 此前工具版改动

| Version | Changes / 改动 |
| --- | --- |
| 0.3.5 | Larger single-source cutter; removed preview / 放大单栏切图窗口，移除预览 |
| 0.3.4 | Square edit references and canvas mapping / 方形编辑参考图及画布映射 |
| 0.3.3 | Native cutter and square generation / 原生切图与默认方图生成 |
| 0.3.2 | Upstream v0.3.1 integration on PhotoCraft 0.19.0 / 合并上游 v0.3.1 |
| 0.2.11 | Title-bar Copy image / 顶部复制图片按钮 |
| 0.2.10 | Full-canvas clipboard export / 完整画布剪贴板导出 |
