---
id: delta-pressure
title: 压力差
group: 岗位
order: 83
source: ServerInfo/Guidebook/Engineering/DeltaPressure.xml
---

# 压力差

ΔP 是两个区域之间的压力差。压力会推动中间物体，并对玻璃窗、风门和百叶窗等造成压力伤害。超过阈值时玻璃会破裂并泄漏气体。

窗户越薄、玻璃越弱，承受能力越低。墙、气闸和防火门不受 ΔP 影响。

## 标准玻璃

<entity id="Window"></entity>
<entity id="WindowDirectional"></entity>
<entity id="Windoor"></entity>
<entity id="ShuttersWindow"></entity>
<entity id="InflatableWall"></entity>

标准整格玻璃阈值为 `Window.DeltaPressure.MinPressureDelta` kPa；四分之一格玻璃为 `WindowDirectional.DeltaPressure.MinPressureDelta` kPa。

## 强化玻璃

<entity id="ReinforcedWindow"></entity>
<entity id="WindowReinforcedDirectional"></entity>
<entity id="WindoorSecure"></entity>
<entity id="ShuttleWindow"></entity>

强化整格为 `ReinforcedWindow.DeltaPressure.MinPressureDelta` kPa；四分之一格为 `WindowReinforcedDirectional.DeltaPressure.MinPressureDelta` kPa。

## 等离子与铀玻璃

<entity id="PlasmaWindow"></entity>
<entity id="PlasmaWindowDirectional"></entity>
<entity id="WindoorPlasma"></entity>
<entity id="UraniumWindow"></entity>
<entity id="UraniumWindowDirectional"></entity>
<entity id="WindoorUranium"></entity>

整格阈值 `PlasmaWindow.DeltaPressure.MinPressureDelta` kPa；四分之一格阈值 `PlasmaWindowDirectional.DeltaPressure.MinPressureDelta` kPa。

## 强化等离子与铀玻璃

<entity id="ReinforcedPlasmaWindow"></entity>
<entity id="PlasmaReinforcedWindowDirectional"></entity>
<entity id="WindoorSecurePlasma"></entity>
<entity id="ReinforcedUraniumWindow"></entity>
<entity id="UraniumReinforcedWindowDirectional"></entity>
<entity id="WindoorSecureUranium"></entity>

整格阈值 `ReinforcedPlasmaWindow.DeltaPressure.MinPressureDelta` kPa；四分之一格阈值 `PlasmaReinforcedWindowDirectional.DeltaPressure.MinPressureDelta` kPa。
