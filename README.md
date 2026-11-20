# Starlight Guidebook 中文

Starlight 服务器 Space Station 14 Guidebook 的非官方中文翻译项目。

在线浏览：<https://zxzxn3.github.io/starlight-guidebook-zh/>

## 当前进度

目录保留 Starlight Guidebook 的完整树状结构，当前可见条目已全部翻译，共 397 个中文页面。

如果后续上游新增条目，未翻译页面会显示原文词数，并可点击进入本地生成的英文原文页。英文页会保留 Guidebook 内部链接、实体提示、表格和可见的规则标记。

法则组、试剂、反应配方、微波炉菜谱和油炸锅菜谱会在构建时从客户端内容缓存生成，名称与正文保留英文原文。

已覆盖：

- 全部 `How To Play SS14` 子树
- 翻译约定与中英术语对照
- 服务器规则、Metashield 与跨回合记忆
- 化学品、饮品、食物配方和书写格式参考表
- 通用 SOP、警报等级、指挥、安保、工程、货运、打捞、服务与医疗 SOP
- 公司法、犯罪清单、量刑、审判与特殊实体条款
- 科研总览、科技树和研发流程
- 异常研究、A.P.E. 和扫描设备
- 异星考古、神器节点和实验操作
- 机器人学与赛博格
- Starlight 科研 SOP

目录中的当前可见条目均已翻译；后续主要工作是跟随上游 Guidebook 更新并维护译名。

### 术语标注

游戏内 UI、物品、设备、岗位和机制名称通常在正文首次出现时标注英文原文。已经显示英文实体 ID 的实体卡、重复出现的名词和普通中文表达不会逐个附加英文。

## 本地查看

克隆仓库后可直接打开 `site/index.html`。

## 重新构建

构建需要：

- Python 3.11 或更高版本
- `zstd`
- Starlight 客户端及其内容缓存

创建环境并安装依赖：

```fish
python -m venv .venv
source .venv/bin/activate.fish
python -m pip install -r requirements.txt
```

生成站点和 EPUB：

```fish
python build_site.py
```

默认读取：

```text
~/.local/share/Space Station 14/launcher/content.db
```

使用其他路径时设置 `STARLIGHT_CONTENT_DB`：

```fish
set -x STARLIGHT_CONTENT_DB /path/to/content.db
```

验证生成结果：

```fish
python verify.py
```

从客户端内容缓存重新提取英文来源：

```fish
python guidebook_source.py
```

## 目录结构

- `content/`：中文 Markdown 正文
- `data/`：实体中文标签
- `templates/`：HTML、CSS 和 EPUB 模板
- `guidebook_source.py`：读取客户端内容、FTL 和科技数据
- `build_site.py`：生成静态站点、搜索索引和 EPUB
- `verify.py`：验证链接、搜索数据与 EPUB 结构
- `site/`：已生成并发布的静态站点

## 许可证与署名

- 构建脚本和站点代码使用 MIT 许可证，见 [LICENSE](LICENSE)。
- 中文译文及依据上游 Guidebook 改编的文本使用 CC BY-SA 3.0，见 [LICENSE-CONTENT.md](LICENSE-CONTENT.md)。
- 上游项目、版权和许可证说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

本项目与 Space Wizards Federation 或 Starlight 官方无隶属关系。
