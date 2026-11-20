---
id: plumbing
title: 管道化学系统
group: 岗位
order: 93
source: ServerInfo/_Starlight/Guidebook/Engineering/Plumbing.xml
---

# 管道化学系统

<entity id="RPLD" caption="RPLD"></entity>

管道系统用液体管道自动运输试剂。RPLD 类似 RCD，可放置液体管道和多数管道设备。所有设备可旋转，连接口必须与相邻管道对齐。

## 液体管道

管道会自动连接相邻设备和管道，并隐藏在地板下。共有主、次、三级三层，可用 RPLD 切换。

<entity id="PlumbingDuctStraight" caption="直管"></entity>
<entity id="PlumbingDuctBend" caption="弯管"></entity>
<entity id="PlumbingDuctTJunction" caption="T 形管"></entity>
<entity id="PlumbingDuctFourway" caption="十字管"></entity>
<entity id="PlumbingDuctManifold" caption="多通桥"></entity>

Manifold 可跨越三层连接不同管道。

## 接口颜色

- 红色：输入，设备从网络拉取。
- 蓝色：输出，其他设备从此拉取。
- 绿色：混合输入，用于比例混合，例如压片机。

连接成功时为平滑接口，未连接时为锯齿接口。

## 柱塞

多数带缓冲的设备可用柱塞把内容物排到地面，清除堵塞试剂。

[试剂流动](plumbing-flow.html)；[设备列表](plumbing-machines.html)。

化学主机、化学分配器和工业研磨机也支持管道连接。
