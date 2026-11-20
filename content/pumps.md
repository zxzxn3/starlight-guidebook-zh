---
id: pumps
title: 泵
group: 岗位
order: 63
source: ServerInfo/Guidebook/Engineering/Pumps.xml
---

# 泵

泵主动移动气体。需要附近 LV 电力；红条一侧为输出；气体不能反向通过。压力或容量超过上限时会阻塞。工作时显示动画，无气或阻塞时红灯闪烁，断电或未固定时无动画。

<entity id="GasPressurePump" caption="压力泵"></entity>
<entity id="GasVolumePump" caption="体积泵"></entity>

## 压力泵

按压力移动气体，适合精确控压或抽真空。目标压力必须高于泵设定值；最高 `GasPressurePump.GasPressurePump.MaxTargetPressure` kPa。

## 体积泵

按体积快速移动大量气体，通常能达到更高压力；目标超过 `GasVolumePump.GasVolumePump.HigherThreshold` kPa 时阻塞。
