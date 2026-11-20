---
id: teg
title: 热电发电机（TEG）
group: 岗位
order: 42
source: ServerInfo/Guidebook/Engineering/TEG.xml
---

# 热电发电机（TEG）

TEG 通过在冷热气体之间交换热量发电。热气体通常来自等离子燃烧，太空中的散热管阵列负责冷却循环气体。除核心和三通循环器外，其他部件都是普通大气设备。

## 发电机

<entity id="TegCirculator"></entity>
<entity id="TegCenter"></entity>

三通循环器有方向，只允许气体单向通过；检查设备可确认方向。输入输出之间需要压力差，因此泵必须开启。哪一侧热、哪一侧冷并不重要，只要有温差。两路气体不会混合，只交换热量。

## 热回路

热回路通过燃烧室加热气体。燃烧室通常与大气主区域用一格太空隔开，包含空气注入器或被动通风口、排太空口和洗涤器阵列。

<entity id="AirInjector"></entity>
<entity id="PassiveVent"></entity>
<entity id="AirScrubber"></entity>

空气注入器最多维持约 9 MPa，良好燃烧很容易达到上限；最好换成连接体积泵的被动通风口。排太空口用于控制压力。洗涤器应把燃烧气体送入 TEG，并通过空气警报设置清除除氧气和等离子外的一切，同时抽气。

## 冷回路

常见方案有水蒸气排放、散热器阵列和冷冻机回路。

### 水冷

让水蒸气经过 TEG 冷侧后排入太空。成本低，但浪费气体、效率差。

### 冷却剂阵列

<entity id="HeatExchanger"></entity>

热交换器应并联，不要串联。热交换器前使用体积泵，后方使用满压气泵。体积泵流量设为 `200 / 热交换器数量` L/s。散热器必须铺在格栅上，不能放在地板上。

### 冷冻机回路

以冷冻机代替太空散热器。虽然耗电，但远低于 TEG 输出。等离子或 Frezon 因比热高，是常用冷却剂。

<entity id="GasThermoMachineFreezerEnabled" caption="冷冻机"></entity>

## 提高效率

大气系统可以不断优化。确保冷暖两个管网不混合，只通过 TEG 交换热量。
