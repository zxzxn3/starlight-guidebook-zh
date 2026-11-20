# Starlight Guidebook 中文

Starlight 服务器 Space Station 14 Guidebook 的非官方中文翻译项目。

在线浏览：<https://zxzxn3.github.io/starlight-guidebook-zh/>

## 当前进度

目录保留 Starlight Guidebook 的完整树状结构。已翻译页面可以直接打开；尚未翻译的页面会显示原文词数，方便判断下一批翻译范围。

目前优先完成科研部相关内容，包括：

- 科研总览、科技树和研发流程
- 异常研究、A.P.E. 和扫描设备
- 异星考古、神器节点和实验操作
- 机器人学与赛博格
- Starlight 科研 SOP

项目仍在持续翻译，尚未覆盖工程、安全、医疗、货运、服务、指挥等其他部门。

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
