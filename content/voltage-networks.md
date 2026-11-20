---
id: voltage-networks
title: 电压网络
group: 岗位
order: 45
source: ServerInfo/Guidebook/Engineering/VoltageNetworks.xml
---

# 电压网络

空间站配电分为低压、中压和高压三类。

<entity id="CableHVStack"></entity>
<entity id="CableMVStack"></entity>
<entity id="CableApcStack"></entity>

## 低压网络

低压为灯具、电脑和多数小型设备供电，由 APC 从 MV 网络转换得到。

<entity id="APCBasic"></entity>
<entity id="PoweredSmallLight"></entity>
<entity id="ComputerShuttleCargo"></entity>
<entity id="ComputerComms"></entity>
<entity id="Autolathe"></entity>
<entity id="VendingMachineEngivend"></entity>
<entity id="VendingMachineMedical"></entity>
<entity id="AlwaysPoweredWallLight"></entity>

LV 线无需连到每台设备，只要线距离设备足够近。径向 2 格、轴向 3 格内均可供电。

## 中压网络

中压网络为 APC 和需要 MV 的设备供电，例如粒子加速器。MV 由变电站从 HV 转换得到。

<entity id="SubstationBasic"></entity>
<entity id="SubstationWallBasic"></entity>

## 高压网络

高压网络在空间站内传输大量电力，为 SMES、变电站等高功率设备供电。多数高输出发电机直接接入 HV。

<entity id="SMESBasic"></entity>
<entity id="RadiationCollector"></entity>
<entity id="TeslaCoil"></entity>

## 电击伤害

被带电电缆电击时，电压越高伤害越大。接触带电 MV 和 HV 电缆应佩戴绝缘手套。
