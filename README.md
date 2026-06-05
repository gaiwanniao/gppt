# gwn's ppt（`/gppt`）

一个 Claude 技能（Skill）：把一个文件夹里的**需求说明 + 资料 + 你自己的模板**，一键变成**可二次编辑**的 PowerPoint。你只管丢资料、写一句需求，剩下的（搭大纲、套模板、按需联网、出片）交给它。

---

## 一、它能做什么（功能特性）

- **按你的模板生成 PPT**：用你自己的 `.pptx` 作底稿，保留母版、主题色和字体，产物是**原生可编辑**的 PowerPoint 对象，不是图片。
- **需求文件驱动**：你在文件夹里写一个简单的需求说明，它据此自动生成幻灯片大纲（`content.md`），你不用手写大纲。
- **8 种制作角色（风格）**：在需求文件里指定角色，输出风格随之改变——
  `简约`、`商务`、`汇报者`、`咨询顾问`、`创意`、`数据派`、`路演者`、`教学者`。
- **联网搜索**：需求里要"补充最新数据"时，自动用 Claude Code 内置的 WebSearch / WebFetch 联网取证（Bedrock/Vertex 网关下可用搜索类 MCP 兜底），并把来源标注到讲者备注里。
- **一键调用**：在 Claude Code 里输入 `/gppt` 即可触发，也会在你自然描述需求时被自动识别。
- **可反复迭代**：改需求文件或 `content.md` 再跑一次，即可重塑整份 PPT。

---

## 二、目录结构

```
gppt/
├── SKILL.md                       # 技能主文件（Claude 据此工作）
├── README.md                      # 本说明
├── references/
│   ├── brief-guide.md             # 需求文件能写哪些内容、如何解读
│   ├── roles.md                   # 8 种制作角色的定义
│   ├── research.md                # 联网搜索方案
│   └── content-md-format.md       # content.md 大纲格式规范
└── scripts/
    └── scan_folder.py             # 扫描文件夹、自动分类资料
```

---

## 三、怎么安装

### 方式 A：装进 Claude Code（命令行，推荐）

Claude Code 通过读取 `~/.claude/skills/<名字>/SKILL.md` 来发现技能。**关键：放进去的必须是解压后的文件夹，而不是 `.skill` 压缩包。**

**用 git 安装（最简单）：**

```bash
git clone https://github.com/<你的用户名>/gppt.git ~/.claude/skills/gppt
```

**或手动放置**：把本仓库内容复制到 `~/.claude/skills/gppt/`，确保存在 `~/.claude/skills/gppt/SKILL.md`。

**如果你手上是 `gppt.skill` 压缩包**（它本质是 zip）：

```bash
cd ~/.claude/skills
unzip -o gppt.skill -d .     # 解压后得到 gppt/SKILL.md
```

**验证：**

```bash
ls ~/.claude/skills/gppt/SKILL.md   # 能列出就成功了
```

回到 Claude Code，输入 `/gp`，应能看到 `/gppt`。若没出现，退出重进 `claude` 一次再试。

> 想给整个团队共享，也可以放到某个项目的 `<项目>/.claude/skills/gppt/` 下并提交到仓库。

### 方式 B：装进 claude.ai / 桌面端（网页上传）

网页端是「上传安装」，要的是 `.skill` 压缩包：

1. 从本仓库下载 `gppt.skill`（或 `git clone` 后用下方命令自行打包）。
2. 打开 Claude → Settings → Capabilities / Skills → 上传 `gppt.skill`。

> 自行打包命令（在仓库上一级目录执行）：把 `gppt` 整个文件夹压缩成 zip，并改名为 `gppt.skill` 即可。

---

## 四、怎么使用

### 1. 准备一个文件夹，放进这些东西

| 放什么 | 作用 | 说明 |
|--------|------|------|
| 一个需求文件（如 `需求.md`） | **指挥棒** | 文件名含「需求 / 要求 / 说明 / 大纲 / brief / requirements」会被自动识别 |
| 一个 `.pptx` 模板 | 品牌底稿 | 文件名含「template / 模板 / brand / 母版」会被优先认作模板；不放则按角色从零设计 |
| `.docx / .pdf / .md / .txt` | 正文素材 | 实际内容来源 |
| `.csv / .xlsx` | 图表数据 | 会被画成可编辑图表 |
| 图片（png/jpg…） | 配图、Logo | 按需求放到对应页 |

### 2. 写需求文件（自由发挥，无需固定格式）

需求文件里可以写：受众、目标、页数、重点、要跳过什么、顺序、语气、**角色**、**是否联网**、**用哪个模板**。示例：

```
给管理层的季度复盘，8 页，角色：汇报者，模板用 brand.pptx，
重点讲增长来源和下半年预算建议，方法论部分跳过，
补充一下行业最新增速数据，结尾要一页明确的预算请求。
```

### 3. 在 Claude 里调用

- Claude Code：输入 `/gppt`，并告诉它文件夹路径（例如"用 ~/Desktop/testppt 文件夹做 PPT"）。
- 或自然描述："按这个文件夹里的需求和模板生成 PPT"。

它会按这个流程跑：扫描文件夹 → 读需求和资料 → 定角色 → 按需联网补料 → 生成 `content.md` 大纲（给你确认）→ 套你的模板渲染 → 自检 → 交付可编辑的 `.pptx`。

---

## 五、制作角色一览

| 角色 | 风格关键词 |
|------|-----------|
| `简约` | 大量留白、一页一观点、克制配色 |
| `商务` | 专业均衡（默认） |
| `汇报者` | 结论先行，每页回答"so what" |
| `咨询顾问` | 行动式标题、MECE / 金字塔结构 |
| `创意` | 大胆编辑风、强视觉冲击 |
| `数据派` | 图表主导、标注来源与单位 |
| `路演者` | 问题→方案→进展→诉求的叙事 |
| `教学者` | 循序渐进、友好、配示例 |

模板与角色同时存在时：**模板定品牌（色/字/母版），角色定版式、密度、标题风格与视觉母题。**

---

## 六、联网搜索说明

- **主方案**：Claude Code 内置 `WebSearch` + `WebFetch`，无需额外配置。若被要求授权，或加入 `~/.claude/settings.json`：
  ```json
  { "permissions": { "allow": ["WebSearch", "WebFetch"] } }
  ```
- **兜底方案**：走 Bedrock / Vertex 网关时内置 WebSearch 不可用，可接入搜索类 MCP（如 Brave Search、Exa），并把 `WebSearch` 加入 `disabledBuiltinTools`。
- 查到的事实会在大纲里标注来源；查不到不会编造。

---

## 七、常见问题

**输入 `/gppt` 搜不到？**
多半是把 `gppt.skill` 压缩包直接丢进了 `~/.claude/skills/gppt/`。Claude Code 需要的是解压后的 `SKILL.md`。按"方式 A"重新解压，确保 `~/.claude/skills/gppt/SKILL.md` 存在，再退出重进 `claude`。

**没有模板可以用吗？**
可以。不放模板时，它会按所选角色的配色和字体从零设计一套。

**生成的 PPT 能改吗？**
能。全部是原生 PowerPoint 对象（文字、形状、图表），可在 PowerPoint / WPS / Keynote 里直接编辑。

---
