---
id: air-injector
title: 空气注入器
group: 岗位
order: 59
source: ServerInfo/Guidebook/Engineering/AirInjector.xml
---

# 空气注入器

<entity id="GasOutletInjector"></entity>

空气注入器强制把气体压入环境，主要用于储气室和燃烧室等高压房间。无需电力。

它会把环境加压到 `GasOutletInjector.GasOutletInjector.MaxPressure` kPa，速度与内部气体量成正比。
