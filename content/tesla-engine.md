---
id: tesla-engine
title: Tesla 引擎
group: 岗位
order: 37
source: ServerInfo/Guidebook/Engineering/TeslaEngine.xml
---

# Tesla 引擎

Tesla 引擎利用受约束的闪电球发电，通过 Tesla Coil 收集雷击能量。

<entity id="TeslaGenerator"></entity>
<entity id="TeslaEnergyBall"></entity>

## 约束场

应使用最小尺寸约束场。更大的场会让闪电球接近敏感设备，绕过接地杆和 Tesla Coil。

<entity id="ContainmentFieldGenerator"></entity>
<entity id="ContainmentField"></entity>
<entity id="TeslaGenerator"></entity>

## 雷击

闪电球会周期攻击周围物体，优先攻击 Tesla Coil 和接地杆。找不到这些目标时，会攻击变电站、APC 和机械等设备，也会电击生物和船员。

## Tesla Coil

<entity id="TeslaCoil"></entity>

Coil 应围在闪电球周围，拾取雷击并保护更远处设备。每次雷击都会损伤 Coil，需要定期修理。Coil 会把能量充入内部电池并快速送入电网；附近配置 SMES 可以平滑储存输出。

## 接地杆

<entity id="TeslaGroundingRod"></entity>

接地杆不会被雷击损坏，适合构成安全网。应用于保护发射器和约束场发生器等敏感设备。

## Tesla 脱困

闪电球逃出后会随机移动，被 APC、变电站和机械吸引，也会电击船员。绝缘手套能防止电击，但不能阻止闪电球攻击。

<entity id="ClothingHandsGlovesColorYellow"></entity>

可用便携粒子减速器发射反粒子摧毁，但 Tesla 比单数更强，需要大量反粒子，建议多人协作。

<entity id="WeaponParticleDecelerator"></entity>
