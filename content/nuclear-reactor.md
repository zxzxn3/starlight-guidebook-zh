---
id: nuclear-reactor
title: 核反应堆
group: 岗位
order: 39
source: ServerInfo/_FarHorizons/Guidebook/Engineering/NuclearReactor.xml
---

# 核反应堆

<entity id="NuclearReactorNormal" caption="核反应堆"></entity>

反应堆以网格形式容纳反应堆棒，通过燃料棒裂变产生热量，再由气体通道传给冷却气体。

## 反应堆棒

<entity id="NuclearFabricator"></entity>
<entity id="CerenkiteReactorFuelRod" caption="燃料棒"></entity>
<entity id="BohrumReactorControlRod" caption="控制棒"></entity>
<entity id="SteelReactorGasChannel" caption="气体通道"></entity>
<entity id="SteelReactorHeatExchanger" caption="热交换器"></entity>

反应堆棒会传递热量并与中子作用。温度达到 `CerenkiteReactorFuelRod.ReactorPart.MeltingPoint` K 后开始熔化，熔化后会释放更多热量，可能导致堆芯熔毁。

高温反应堆棒会导致严重烧伤。温度高于 `CerenkiteReactorFuelRod.ReactorPart.HotTemp`°C 时必须戴手套；达到 `CerenkiteReactorFuelRod.ReactorPart.BurnTemp`°C 后，手套也无法保护。

反应堆棒有四类：

- **燃料棒**：产生中子和热量。
- **控制棒**：限制中子通量，可调节插入深度。
- **气体通道**：把热量传给冷却气体，每根增加 `SteelReactorGasChannel.ReactorPart.GasVolume` L/s 流量。
- **热交换器**：传递热量且不与中子作用，适合把燃料棒热量导向气体通道。

## 燃料棒

燃料棒通过自发衰变或与现有中子作用产生热量。两个主要属性：

- 中子放射性：产生高能中子和大量热量，衰变为放射性。
- 放射性：产生中子和热量，衰变为乏燃料。

乏燃料不影响当前性能，但可提示何时更换。乏燃料可经核离心机处理成钚，用于制造钚燃料棒。

<entity id="NuclearCentrifuge"></entity>
<entity id="IngotPlutonium"></entity>

## 控制反应堆

反应堆界面包括 Targeting、Grid View 和 Status Panel。

- **Targeting**：用方向键选择坐标，查看并插入、取出反应堆棒；顶部显示名称、温度、中子放射性、放射性、乏燃料和库存部件。
- **Grid View**：切换温度、中子数量或燃料量视图。
- **Status Panel**：显示温度、辐射和热功率；温度达到 `NuclearReactorNormal.NuclearReactor.ReactorMeltdownTemp` K 时熔毁。辐射上限为 `NuclearReactorNormal.NuclearReactor.MaximumRadiation` rads，热功率上限为 `NuclearReactorNormal.NuclearReactor.MaximumThermalPower` Wt。

控制棒插入 100% 时效果最强，0% 时基本无效。

## 冷却

<entity id="PlasmaCanister"></entity>
<entity id="CarbonDioxideCanister"></entity>
<entity id="TritiumCanister"></entity>

- **等离子**：增加中子并衰变为氚，过量会导致失控。
- **二氧化碳**：吸收中子，可抑制等离子反应。
- **氚**：随机转化为氧、氮、氨、一氧化二氮或 Frezon；与氧接触并达到反应堆温度时会燃烧并释放大量热量。

## 辐射

<entity id="SignRadiation"></entity>
<entity id="ClosetRadiationSuit"></entity>
<entity id="ClothingOuterSuitRad"></entity>
<entity id="GeigerCounter"></entity>

逃逸中子越多，辐射越强。在反应堆附近工作应穿防护服并使用盖革计数器。
