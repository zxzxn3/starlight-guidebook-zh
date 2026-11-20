---
id: science
title: 科研部总览
group: 科学总览
order: 10
source: ServerInfo/Guidebook/Science/Science.xml
---

# 科研部总览

**科研部（Science）**通常也被称为研发部（R&D）。这个部门通过产生研究点来解锁新科技，再使用这些科技在车床上制造新物品，以支援整座空间站。

## 人员构成

科研部由**研究助理**和**科学家**组成，并由**研究主任**负责管理。

<entity id="ToyFigurineScientist" caption="科学家"></entity>
<entity id="ToyFigurineResearchDirector" caption="研究主任"></entity>

## 研究与科技

<entity id="ComputerResearchAndDevelopment"></entity>
<entity id="ResearchAndDevelopmentServer"></entity>

部门里最重要的设施是**研发服务器**和**研发控制台**。服务器保存已经解锁的科技；控制台用于消耗研究点解锁新科技。

每项科技都需要消耗**研究点**，解锁后会在各处的车床上增加对应配方。有些科技还有前置科技，必须先完成前置研究。

[查看完整科技列表](technologies.html)。

## 学科

科技分为五个研究学科：

<entity id="Wrench" caption="工业"></entity>
<entity id="WeaponTetherGun" caption="实验"></entity>
<entity id="ComputerTelevision" caption="民用服务"></entity>
<entity id="WeaponXrayCannon" caption="军备"></entity>
<entity id="ExosuitFabricator" caption="生物化学相关制造设备"></entity>

靠近研发控制台，可以看到每个学科树中锁定了哪些科技。

## 科技等级

每个学科通常包含多个科技等级。初始只会开放一级科技。

要进入下一等级，需要完成当前等级约 **75%** 的科技。例如，想解锁二级研究，就需要先完成一级研究的 75%。

当研究进入**三级科技**后，就需要特别谨慎：完成某个学科的三级科技，会**锁死其他学科的三级科技**。除非你找到了其他规避方式，否则最好先询问研究主任。

## 车床

<entity id="Protolathe"></entity>
<entity id="CircuitImprinter"></entity>
<entity id="ExosuitFabricator"></entity>
<entity id="MedicalTechFab"></entity>
<entity id="SecurityTechFab"></entity>

在车床上选择一台研发服务器后，就可以制造服务器里已经解锁的配方。制造通常需要钢铁、玻璃、塑料、金和等离子等材料，这些材料可以向货运部或打捞队获取。
