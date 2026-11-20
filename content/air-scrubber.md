---
id: air-scrubber
title: 空气洗涤器
group: 岗位
order: 60
source: ServerInfo/Guidebook/Engineering/AirScrubber.xml
---

# 空气洗涤器

<entity id="GasVentScrubber"></entity>

洗涤器负责移除呼吸和大气事故产生的废气，需要附近 LV 电缆供电。默认过滤除氮气和氧气外的全部气体。

可用焊接器封死。

## 设置

连接空气警报后，可在 Gas filters 中选择目标气体。切换警报模式会重置过滤设置。

- **Scrubbing**：按过滤列表清除气体。
- **Siphoning**：忽略过滤，抽取全部气体。

Rate 决定抽取速度。WideNet 会让洗涤器同时处理自身及周围四格，共五格气体，大幅提高处理速度。

当环境中不需要的气体浓度很高时，自动模式会启用 WideNet，适合快速清除燃烧室中的氚。
