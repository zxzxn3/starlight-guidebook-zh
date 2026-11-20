---
id: pressure-regulator
title: 入口压力调节器
group: 岗位
order: 77
source: ServerInfo/Guidebook/Engineering/PressureRegulator.xml
---

# 入口压力调节器

<entity id="GasPressureRegulator"></entity>

管网压力超过阈值时自动开启，把气体排到输出管；低于阈值后关闭。最大流量 `GasPressureRegulator.GasPressureRegulator.MaxTransferRate` L/s。

常用于防止 TEG 冷却回路和管道超压，也可从燃烧室排出多余高温气体，同时将压力维持在能继续燃烧的范围内。
