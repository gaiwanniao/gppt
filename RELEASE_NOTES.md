# Release Notes — v1.0.0

把"文件夹里的需求 + 资料 + 你的模板"一键变成可编辑 PPT 的首个正式版本。
The first stable release: turn a folder's brief + materials + your template into
an editable deck in one shot.

## ✨ 功能 / Features
- 按你自己的 `.pptx` 模板生成**原生可编辑**幻灯片（保留母版、主题色、字体）。
  Build native, editable slides on your own `.pptx` template.
- 需求文件驱动：自动生成大纲（`content.md`），无需手写。
  Brief-driven: the slide outline is generated for you.
- 8 种制作角色：简约 / 商务 / 汇报者 / 咨询顾问 / 创意 / 数据派 / 路演者 / 教学者。
  8 maker roles for different styles.
- 联网搜索：Claude Code 内置 WebSearch/WebFetch，MCP 兜底，来源写入备注。
  Web research via built-in WebSearch/WebFetch (MCP fallback), with citations.
- 在 Claude Code 中用 `/gppt` 调用，或自然描述自动触发。
  Invoke with `/gppt`, or trigger by describing the task.

## 📦 安装 / Install
- **Claude Code**：`git clone https://github.com/<your-username>/gppt.git ~/.claude/skills/gppt`，重启 `claude` 后输入 `/gppt`。
- **claude.ai / 桌面端**：下载本 Release 附带的 `gppt.skill`，在 Settings → Capabilities/Skills 上传。

## ⚠️ 注意 / Notes
- Claude Code 需要**解压后的 `SKILL.md`**，不要直接丢 `.skill` 压缩包。
  Claude Code needs the extracted `SKILL.md`, not the `.skill` archive.
- 建议 Claude Code 版本 ≥ 2.1（技能可作为斜杠命令调用）。
  Claude Code ≥ 2.1 recommended (skills usable as slash commands).
