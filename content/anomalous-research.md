---
id: anomalous-research
title: 异常研究
group: 异常研究
order: 10
source: ServerInfo/Guidebook/Science/AnomalousResearch.xml
---

# 异常研究

异常研究是科研部的分支，主要工作是收容、观测和操控各种独特的空间异常（Anomaly）。

## 设备

<entity id="AnomalyScanner"></entity>
<entity id="MachineAnomalyVessel"></entity>
<entity id="MachineAPE"></entity>

异常扫描器（Anomaly Scanner）、收容容器（Anomaly Vessel）和异常粒子发射器（A.P.E.）共同用于异常的观测与收容。

<entity id="MachineAnomalyGenerator"></entity>

异常发生器（Anomaly Generator）会消耗等离子，在空间站某处生成一个随机异常。

## 异常

异常是出现在空间站上的固定对象。它们不能移动，因此无论出现在哪里，都必须围绕其位置建立安全措施。

<entity id="AnomalyPyroclastic" caption="热火山异常"></entity>

每个异常有三项主要属性，其中两项可以通过扫描看到：

- **严重度（Severity）：** 表示异常危险程度的数值。
- **稳定性（Stability）：** 分为衰减、稳定或增长，决定异常效果的频率和影响范围。
- **生命值（Health）：** 隐藏属性。对异常发射**收容粒子（Containment Particle）**会降低生命值；使用过多会使异常消失。

## 脉冲与超临界事件

异常最危险的效果通常发生在**脉冲（Pulse）**和**超临界事件（Supercritical）**期间。

脉冲是半规律出现的异常效果爆发，危险程度中等，并会随严重度和稳定性提高而增强。

当异常的严重度达到 100% 时，会进入**超临界事件**。异常会先膨胀，随后消失并引发灾难性后果。应尽一切可能避免超临界。
