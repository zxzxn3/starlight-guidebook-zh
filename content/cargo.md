---
id: cargo
title: 货运部
group: 岗位
order: 16
source: ServerInfo/Guidebook/Cargo/Cargo.xml
---

# 货运部

补给部门也就是货运部，为空间站供应燃料、原材料等必要资源，也提供彩票、玩偶等改善生活的物品。

货运通过赏金、出售杂物和打捞等方式赚取 spesos，也就是空间站货币，再用它购买船员需要的各种站外设备。满足其他部门需求是货运的职责。

## 人员

货运部由货运技术员和打捞专家组成，由货运主管领导。

<entity id="ToyFigurineCargoTech" caption="货运技术员"></entity>
<entity id="ToyFigurineSalvage" caption="打捞专家"></entity>
<entity id="ToyFigurineQuartermaster" caption="货运主管"></entity>

## 赚钱

货运最常见的困难是资金不足。主要收入来自在贸易站出售物品。空间站上几乎所有东西都有经济价值，可用估价工具查看；作为[赏金](cargo-bounties.html)出售时价值更高。

<entity id="AppraisalTool"></entity>
<entity id="CargoPallet"></entity>
<entity id="CrateGenericSteel"></entity>

发现贵重物品后带回货运舱。能装箱的物品应装入空箱。货运穿梭机不在时，把待售物品放到货运托盘。穿梭机停靠后，再把箱子和其他货物装船。

<entity id="ComputerPalletConsole"></entity>
<entity id="CargoPalletSell"></entity>
<entity id="ComputerCargoOrders"></entity>

装船后飞往贸易站，把货物放到绿色销售托盘，再在货运销售电脑上点击 **Sell**。带着 spesos 回站，并存入货运请求电脑。

完成[赏金](cargo-bounties.html)或出售[打捞](salvage.html)获得的贵重物品还能赚得更多。

## 下单

<entity id="ComputerCargoOrders"></entity>

所有订单都从货运请求电脑开始。首先货运必须有足够 spesos。资金不足时，应先赚钱。

是否满足请求由货运自行决定。资金紧张时，可以拒绝并非立即必要的订单。

点击需求物品名称，填写收件人、理由，然后点击 **Approve**。有些空间站有公共请求电脑，此时只需批准玩家自行提交的订单。

<entity id="CargoPalletBuy"></entity>
<entity id="PaperCargoInvoice"></entity>

订单会被送到贸易站的采购托盘。把对应箱子装回穿梭机并返回空间站，阅读箱子上的货运发票标签，将货物交给收件人。

## 驾驶

订单通过轨道贸易站送入，再由货运穿梭机运回主站。穿梭机不会自动驾驶，需要在机上或远程驾驶。

<entity id="ComputerShuttleCargo"></entity>

货运舱和穿梭机内各有一台货运穿梭机控制台。操作后进入穿梭机导航视图：

- 切换到 **DOCK** 界面，解除穿梭机与空间站之间的气闸连接。
- 穿梭机脱离后即可驾驶。太空中动量守恒，注意制动。
- 使用 <kbd>ShuttleStrafeUp</kbd>、<kbd>ShuttleStrafeDown</kbd>、<kbd>ShuttleStrafeLeft</kbd>、<kbd>ShuttleStrafeRight</kbd> 平移，使用 <kbd>ShuttleRotateLeft</kbd>、<kbd>ShuttleRotateRight</kbd> 转向，按 <kbd>ShuttleBrake</kbd> 制动。
- 驾驶到贸易站后与气闸对接。

[了解如何通过赏金提高收益](cargo-bounties.html)。
