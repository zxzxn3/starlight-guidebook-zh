---
id: combustion-turbine
title: 燃烧涡轮
group: 岗位
order: 96
source: ServerInfo/_Starlight/Guidebook/Engineering/CombustionTurbine.xml
---

# 燃烧涡轮

从燃烧室抽取高温高压气体，使其通过叶片膨胀并排入低压废气，气体越密、压降越大，转子越快，HV 输出越高。

<entity id="CombustionTurbineCompressor" caption="入口压缩机"></entity>
<entity id="CombustionTurbineRotor" caption="核心转子"></entity>
<entity id="CombustionTurbineOutlet" caption="涡轮出口"></entity>
<entity id="ComputerCombustionTurbine" caption="控制电脑"></entity>
<entity id="IgniterFloor" caption="点火器"></entity>

## 获取与组装

货运出售包含三段和电脑的箱装涡轮。更多设备需研究 Combustion turbines（Industrial）；用电路板制造的段不带部件，需要在工程制造台打印一级部件。

三段沿同一方向排列并形成气密墙：

- 入口压缩机从后方燃烧室吸气。
- 核心转子发电并经 HV 输出，启动电机需 APC 电力。
- 出口把废气排到前方，通向太空或排气管。

检查任一段确认组装完成，并用多用工具把控制电脑连到核心转子。

## 运行

1. 在燃烧室填入约 3–5 份氧配 1 份等离子，压力越高输出越大。
2. 确保排气侧通向太空。排入常压房间几乎没有压降，涡轮会失速。
3. 用点火器点燃。
4. 在电脑启动涡轮，启动电机会带动转子，之后由燃烧维持。

一级压缩机入口约为 800 L/s。1 MPa 时约耗 30 mol/s，2 MPa 约 60 mol/s，满级 3 MPa 可超过 100 mol/s。

冷气体几乎不能驱动转子。叶片只提取部分热量，尾气仍可能超过 1000 K；未燃烧燃料可通过尾气过滤器回收。混合气停留过久后会生成更热的氚。

## 调速器

转子达到额定速度后，调速器会自动关闭入口，避免超速和浪费燃料。电脑会显示调速器是否正在限速；长期限速说明应升级部件。

## 部件

| 等级 | 压缩机与转子 | 定子 |
| --- | --- | --- |
| 2 | 10 塑钢 | 15 塑钢 |
| 3 | 10 铀 | 15 铀 |
| 4 | 5 钻石 | 8 钻石 |

一级涡轮在 1.5–2 MPa 燃烧下约 300 kW，满级在 3 MPa 下可约 1.5 MW。

关闭并等待转子停止，用螺丝刀打开面板、撬棍取出部件并换上新品。面板内无部件时再次撬动会拆解设备。

## 损伤

入口气体超过部件额定温度会损失完整性，归零后转子爆炸，转速越高爆炸越大。降温、减少燃料、加入氮气缓冲或升级部件可避免过热。
