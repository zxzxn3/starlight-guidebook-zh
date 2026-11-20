---
id: expanding-and-repairing-stations
title: 扩建与维修空间站
group: 岗位
order: 29
source: ServerInfo/Guidebook/Engineering/ExpandingRepairingStation.xml
---

# 扩建与维修空间站

玩家经常需要扩建空间站，或修复陨石和破坏造成的洞口。

## 格栅

格栅是铺在太空中的金属杆结构，用作建造和固定物体的基础。

<entity id="SheetSteel"></entity>
<entity id="PartRodMetal"></entity>

在太空用 <kbd>Use</kbd> 放置金属杆即可建造格栅。钢板可以在建造菜单中制成金属杆。

格栅不能维持压力，气体都会漏入太空。用剪线钳对格栅按 <kbd>Use</kbd> 可拆除。

如果无法放置格栅，通常是附近存在另一块距离过近的独立网格。可以用剪线钳移除冲突格栅。

## 船体地板

船体地板是空间站的实体基础。

<entity id="SheetSteel"></entity>
<entity id="FloorTileItemSteel"></entity>
<entity id="FloorTileItemDark"></entity>
<entity id="FloorTileItemWhite"></entity>

在格栅上使用钢板或几乎任何地砖即可铺成能维持气压的船体地板。

建议使用地砖：一块钢板能制作四块地砖。RCD 可以把船体地板拆回格栅。
