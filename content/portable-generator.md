---
id: portable-generator
title: 便携式发电机
group: 岗位
order: 33
source: ServerInfo/Guidebook/Engineering/PortableGenerator.xml
---

# 便携式发电机

P.A.C.M.A.N. 系列用于为关键房间、区域或部门提供应急电力，易于搭建和维护。

<entity id="PortableGeneratorJrPacman" caption="J.R.P.A.C.M.A.N."></entity>
<entity id="PortableGeneratorPacman" caption="P.A.C.M.A.N."></entity>
<entity id="PortableGeneratorSuperPacman" caption="S.U.P.E.R.P.A.C.M.A.N."></entity>

## Junior 型

<entity id="WeldingFuelTank"></entity>

J.R.P.A.C.M.A.N. 常见于维修通道，适合船员自行处理局部断电。最多输出 `PortableGeneratorJrPacman.FuelGenerator.MaxTargetPower` W，足以供应一两个房间，对医疗部或化学室很有价值。

用扳手固定在 LV 电缆上，加入焊接燃料并启动。它只能使用焊接燃料。

## 大型型号

<entity id="SheetPlasma"></entity>
<entity id="SheetUranium"></entity>

P.A.C.M.A.N. 和 S.U.P.E.R.P.A.C.M.A.N. 由工程部用于大型断电、补充电力或启动大型引擎。它们连接 MV 或 HV 电缆并可切换。

S.U.P.E.R.P.A.C.M.A.N. 输出最高 `PortableGeneratorSuperPacman.FuelGenerator.MaxTargetPower` W，满载续航更长，但低负载时效率较低。分别以铀板和等离子板为燃料。
