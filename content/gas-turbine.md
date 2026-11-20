---
id: gas-turbine
title: 燃气涡轮
group: 岗位
order: 40
source: ServerInfo/_FarHorizons/Guidebook/Engineering/GasTurbine.xml
---

# 燃气涡轮

<entity id="GasTurbineNormal" caption="燃气涡轮"></entity>

涡轮接收反应堆的高温气体，输出电力并把冷却后的气体送回反应堆。输出受 RPM 影响，而 RPM 由 Flow Rate 和 Stator Load 控制。

## Flow Rate

决定每秒通过涡轮的气体量。越高，RPM 越高。通常设置为反应堆核心最大流量：`SteelReactorGasChannel.ReactorPart.GasVolume` × 气体通道数 + `NuclearReactorNormal.NuclearReactor.ReactorVesselGasVolume` L/s。

## Stator Load

决定每转产生多少功率。越高，RPM 越低。应调整以维持最佳 RPM。

## RPM

涡轮有最佳转速，过快或过慢都会降低效率。

## 状态警告

- **Overspeed**：转速过高，会损伤涡轮，长时间或严重超速会解体。焊接器可修复，但通常需多次。
- **Overtemp**：入口气体高于 `GasTurbineNormal.GasTurbine.MaxTemp` K 时会紧急排入房间，可能烧伤人员或引发火灾。
- **Stalling**：气体温度不足以推动设定的 Stator Load。
- **Undertemp**：气体温度等于或低于 `GasTurbineNormal.GasTurbine.MinTemp` K，无法提取能量。

## 涡轮部件

<entity id="NuclearFabricator"></entity>
<entity id="SteelGasTurbineBlade" caption="涡轮叶片"></entity>
<entity id="SteelGasTurbineStator" caption="定子"></entity>

叶片决定完整性和惯性。完整性越高越耐久；惯性越高，转速变化越平稳。定子决定效率和输出。部件由核制造机使用[材料](NuclearMaterials)生产。
