---
id: singularity-tesla-engine
title: 单数与 Tesla 引擎
group: 岗位
order: 35
source: ServerInfo/Guidebook/Engineering/SingularityTeslaEngine.xml
---

# 单数与 Tesla 引擎

这两种引擎能为整个班次提供近乎无限的电力，也能同样轻易地毁掉空间站。必须认真准备并持续监控，防止脱困。

两种引擎的基础流程类似，但子系统不同。

## 约束场

约束场是多格光束构成的屏障，用于阻止单数或 Tesla 逃离。发射器和约束场本身都可能伤害人员，或把人击飞到深空。

<entity id="Emitter"></entity>
<entity id="ContainmentFieldGenerator"></entity>
<entity id="ContainmentField"></entity>

约束场在开启并受发射器供能的约束场发生器之间形成。发生器必须开启、8 格内存在另一台发生器，并位于同一水平或垂直轴上。因此单段约束场最长 7 格。

用 <kbd>Use</kbd> 开启发生器。未开启时，即使被发射器击中也不会工作。

发射器为发生器充能，能量会自然衰减；能量不足后约束场消失。约束场存在时不能关闭或拆下发生器，必须等场消散。

## 发射器

<entity id="Emitter"></entity>

发射器连接 MV 电缆，供电且开启时会持续发射激光。建议用 <kbd>AltActivateItemInWorld</kbd> 锁定发射器，防止入侵者关闭约束场。

## 粒子加速器

粒子加速器（PA）由多个部件组成，会从发射端射出加速粒子。

<entity id="ParticleAcceleratorEndCap" caption="PA 端盖"></entity>
<entity id="ParticleAcceleratorControlBox" caption="PA 控制箱"></entity>
<entity id="ParticleAcceleratorFuelChamber" caption="PA 燃料室"></entity>
<entity id="ParticleAcceleratorPowerBox" caption="PA 电源箱"></entity>
<entity id="ParticleAcceleratorEmitterStarboard" caption="右舷发射端"></entity>
<entity id="ParticleAcceleratorEmitterFore" caption="前发射端"></entity>
<entity id="ParticleAcceleratorEmitterPort" caption="左舷发射端"></entity>

若空间站已有未完成的 PA，确认电源箱下有 MV 线，固定全部部件，再给每个部件接上 LV 线，用螺丝刀关闭面板。最后在 PA 控制电脑上扫描全部部件；未扫描时 PA 不会工作。若显示不完整，检查缺少的部件。

<entity id="ParticleAcceleratorControlBox"></entity>
