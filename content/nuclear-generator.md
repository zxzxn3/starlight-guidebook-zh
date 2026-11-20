---
id: nuclear-generator
title: 核能发电机
group: 岗位
order: 38
source: ServerInfo/_FarHorizons/Guidebook/Engineering/NuclearGenerator.xml
---

# 核能发电机

<entity id="NuclearReactorNormal" caption="核反应堆"></entity>
<entity id="GasTurbineNormal" caption="燃气涡轮"></entity>

核反应堆通过裂变加热冷却气体，再由[燃气涡轮](GasTurbine)发电。

## 启动

- 向冷却回路充入气体。
- 根据反应堆布局设置涡轮流量。
- 把燃料棒放入空槽，通常由控制棒控制，周围配置热交换器和气体通道。
- 抽出控制棒开始升温。
- 升温过程中调整 Stator Load，维持最佳 RPM。
- 输出足够后，将控制棒插回以维持反应堆温度。

燃料棒会逐渐失去放射性，需要继续抽出控制棒或更换燃料棒。
