---
id: cargo-bounties
title: 货运赏金
group: 岗位
order: 17
source: ServerInfo/Guidebook/Cargo/CargoBounties.xml
---

# 货运赏金

[货运部](cargo.html)几乎可以通过出售任何物品赚钱，但完成货运赏金电脑上的订单收益更高。

## 开始赏金

<entity id="ComputerCargoBounty"></entity>
<entity id="PaperCargoBountyManifest"></entity>

操作货运赏金电脑打开界面。电脑会显示当前赏金，可以打印标签或跳过。

- 打印标签会生成赏金清单，列出所需物品。清单可以无限打印，但要避免与其他货运技术员重复工作。
- 同时最多存在六项赏金。跳过会用新赏金替换当前项，冷却 15 分钟，并作废原赏金，可能影响正在处理它的其他技术员。

## 完成赏金

<entity id="PaperCargoBountyManifest"></entity>
<entity id="CrateGenericSteel"></entity>
<entity id="AppraisalTool"></entity>

拿着赏金清单收集货物。多数部门在看到清单后愿意提供所需物品。

把货物放入空箱，关闭箱子，再将赏金清单贴到箱子上。使用估价工具检查，界面应显示赏金已完成。

## 出售赏金

<entity id="PaperCargoBountyManifest"></entity>
<entity id="CrateGenericSteel"></entity>
<entity id="CargoPalletSell"></entity>

确认完成后，按普通货物流程运到贸易站出售。返回空间站后，原赏金会被新赏金替换。
