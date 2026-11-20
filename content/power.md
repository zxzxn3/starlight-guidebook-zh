---
id: power
title: 电力
group: 岗位
order: 31
source: ServerInfo/Guidebook/Engineering/Power.xml
---

# 电力

电力是空间站的生命线。断电后空间站会迅速陷入混乱。工程师负责维持发电、配电并满足各部门需求。

<entity id="SingularityGenerator"></entity>
<entity id="TeslaGenerator"></entity>
<entity id="AmeController"></entity>
<entity id="SMESBasic"></entity>
<entity id="SubstationBasic"></entity>
<entity id="APCBasic"></entity>

- 空间站[发电机](Generators)有等级层次。低级设备容易搭建但持续性较差；高级设备更持久但更复杂。
- [电压网络](VoltageNetworks)负责分配电力，并通过设备逐级降压。
- 发电机存在[爬坡](Ramping)，需要时间匹配电网需求。

## 开局供电

班次开始时，空间站完全依靠[电池](PowerStorage)，通常只能维持 5–10 分钟。

应启动[反物质引擎](ame.html)延长电池时间，并搭建[太阳能板](SolarPanels)提供免费电力。之后可以开始搭建[单数引擎](SingularityEngine)或[Tesla 引擎](TeslaEngine)等高级发电机，维持剩余班次。
