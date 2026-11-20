---
id: singularity-engine
title: 单数引擎
group: 岗位
order: 36
source: ServerInfo/Guidebook/Engineering/SingularityEngine.xml
---

# 单数引擎

单数引擎利用受约束的单数体发电，通过辐射收集器和等离子气体收集单数体释放的辐射。

<entity id="SingularityGenerator"></entity>
<entity id="Singularity"></entity>

## 启动

- 把单数发生器放在约束场中央。
- 开启四台约束场发生器。
- 开启并锁定发射器。
- 确认约束场已形成。
- 开启辐射收集器并装入等离子。
- 建造粒子加速器。
- 在 PA 控制电脑开启并设置功率。

运行后持续监控单数体和约束场，并定期补充收集器中的等离子。

## 约束场

单数引擎应使用最大尺寸约束场。发生器应组成正方形，各发生器之间间隔 7 格。

<entity id="ContainmentFieldGenerator"></entity>

## 功率与衰减

单数会随时间衰减。PA 发射粒子撞击单数体，为其补充能量。功率越高，单数体越大、辐射越强，发电也越多。

## 发电

<entity id="RadiationCollector"></entity>
<entity id="PlasmaTank"></entity>

收集器需要装有等离子。用 <kbd>Use</kbd> 开启，用 <kbd>AltActivateItemInWorld</kbd> 取出气罐。辐射量和等离子量共同决定最大输出。

## 辐射防护

单数会产生足以杀死无防护船员的辐射。应穿防辐射服或工程太空服，并携带盖革计数器。

<entity id="ClothingOuterHardsuitEngineering"></entity>
<entity id="ClosetRadiationSuit"></entity>
<entity id="ClothingOuterSuitRad"></entity>
<entity id="GeigerCounter"></entity>

## 单数体特性

- 强引力会吸引物体和船员。
- 事件视界会永久摧毁接触到的任何东西。
- 持续释放辐射。
- 会随时间衰减。

## 单数脱困

单数逃出约束场后会吞食空间站，并因吞噬而变得更大。可以用便携粒子减速器发射反粒子摧毁，但通常需要多人同时射击。科研部可研发，货运部也可购买。

<entity id="WeaponParticleDecelerator"></entity>
