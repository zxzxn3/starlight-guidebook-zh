---
id: plumbing-machines
title: 管道设备
group: 岗位
order: 95
source: ServerInfo/_Starlight/Guidebook/Engineering/PlumbingMachines.xml
---

# 管道设备

全部设备由 RPLD 放置。需要电力的设备必须位于 APC 供电范围。

<entity id="PlumbingInput"></entity>
<entity id="PlumbingOutput"></entity>

**Input**：手动倒入试剂的小罐，供网络其他设备拉取。
**Output**：可用容器从中取出试剂，主动从网络拉取。

<entity id="PlumbingSink"></entity>
<entity id="PlumbingDrain"></entity>

**Sink**：输入输出合一，可通过水龙头装容器，也可把试剂排入网络。
**Drain**：吸收地面液体并送入网络。

<entity id="PlumbingTank"></entity>

**Tank**：储存 2400u，一输入三输出，适合生产阶段间缓冲。

<entity id="PlumbingBuffer"></entity>

**Buffer**：可走过的小型储罐，储存 240u，一输入三输出。

<entity id="PlumbingFilter"></entity>

**Filter**：最多分离 4 种指定试剂，分别从过滤和直通输出送出。

<entity id="PlumbingInlineFilter"></entity>

**Inline Filter**：单线取走最多 10 种试剂，每种 10u，不改变其余流向。

<entity id="PlumbingReactor"></entity>

**Reactor**：按目标试剂和数量拉取、加热并触发化学反应。需要电力。

<entity id="PlumbingPillPress"></entity>

**Pill Press**：按剂量自动制作药片或贴片，可混合两个独立网络的指定比例。需要电力。

<entity id="PlumbingSynthesizer"></entity>

**Synthesizer**：消耗电量生成铁、碳、铜、氢、氧、糖、硅或磷。

<entity id="PlumbingSmartDispenser"></entity>

**Smart Dispenser**：存每种试剂最多 240u，每轮拉取 40u。用贴标签的容器可取对应试剂。需要电力。

<entity id="PlumbingDisposal"></entity>

**Disposal**：把拉入的试剂逐渐销毁，用于清理废液。
