---
id: ame
title: 反物质引擎（AME）
group: 岗位
order: 34
source: ServerInfo/Guidebook/Engineering/AME.xml
---

# 反物质引擎（AME）

AME 是短期支援发电机，能在有限时间内提供大量电力，主要用于帮助工程师启动单数引擎或 Tesla 引擎。

## 建造

<entity id="AmeController"></entity>
<entity id="AmePartFlatpack"></entity>
<entity id="AmeJar"></entity>

控制器通过 HV 连接向电网输出电力，因此应放在 HV 电缆上。空间站通常已有裸露 HV 线或预留位置。

用多用工具把 AME 平板包转换为护盾结构。先铺设至少 3×3 的平板包；中心块越多，核心越多，安全输出越高。随后用多用工具逐个转换为护盾。

<entity id="AmeController"></entity>
<entity id="AmeShielding" caption="AME 护盾"></entity>

## 运行

把燃料罐装入控制器并设置安全注入速率。安全速率等于核心数的两倍：单核心为 2，双核心为 4。

超过该比例会过热，随后爆炸。控制器会报告当前输出和理论最大输出。
