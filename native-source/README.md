# PhotoCraft 原生集成源码

基线：`storytold/photocraft`，版本 0.18.0，提交
`422ca7beda90d927643bcd074646ebbd37706d75`。

修改涉及 `crates/ui-egui` 和 `crates/engine`：选区下方的 egui 工具栏、可序列化的提示词状态、
后台本地请求、图层右键羽化控制，以及 `layer.layerMask.edit` 的居中圆形/正方形蒙版参数。
`ui.inspect.codexAI.maskFeatherMenu` 提供菜单与控件坐标，供界面测试使用。
图像导出、选区、图层和撤销仍通过已有引擎命令完成。

开发版 0.2.10 新增 **文件 → 导出 → 导出到剪贴板**（`file.export.clipboard`）。
引擎将整张可见画布合成为内存中的图片；桌面层通过现有系统剪贴板服务写入 RGBA8，
无需临时导出文件。保留透明度，忽略选区，不改变文档和撤销记录；剪贴板写入失败时保留原有内部复制内容。
实现位于 `crates/engine/src/cmd/clipboard_export_cmds.rs` 和 `crates/ui-egui/src/app/clipboard.rs`，
相关菜单、简繁中文翻译和回归测试包含在同一补丁中。

Development preview 0.2.10 adds **File → Export → Export to Clipboard** (`file.export.clipboard`).
The engine composites the entire visible canvas in memory; the desktop uses the existing system
clipboard service to write RGBA8 without an intermediate export file. It preserves transparency,
ignores the selection, and leaves the document and undo history unchanged. A failed OS write
preserves the previous internal clipboard. The patch includes the command, menu, Chinese translations,
and regression tests. Canvases are limited to 64 million pixels.

在项目根目录准备源码（本机已经完成）：

```powershell
git clone https://github.com/storytold/photocraft.git research/photocraft
git -C research/photocraft checkout 422ca7beda90d927643bcd074646ebbd37706d75
git -C research/photocraft apply ../../native-source/photocraft-codex.patch
python build_native.py
```

依赖 Rust/MSVC 构建工具及网络下载 Cargo 依赖。构建输出 `native/photocraft.exe`，
不修改已安装的原版编辑器。`native-build.toml` 是便于本机迭代的开发配置。

原生界面只在启动脚本设置 `PHOTOCRAFT_CODEX_PORT` 和 `PHOTOCRAFT_CODEX_TOKEN_FILE`
时启用。生成后台是 `photocraft_ai/native.py`，只接收经认证的 localhost 请求。
在 WebAssembly 中禁用本机后台能力，保持原有网页版本构建兼容。

上游许可证和通知随二进制保存于 `native/`。源码补丁遵循上游 MIT OR Apache-2.0。
