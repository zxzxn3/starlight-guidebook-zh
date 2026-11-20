---
id: solar-panels
title: 太阳能板
group: 岗位
order: 46
source: ServerInfo/Guidebook/Engineering/SolarPanels.xml
---

# 太阳能板

太阳能板是低维护被动电源，通过阳光发电，可补充电网，且无需燃料。

<entity id="SolarPanel"></entity>

## 发电

输出取决于电池板与太阳的相对角度及遮挡情况。正对太阳且无遮挡时，标准太阳能板输出 `SolarPanel.SolarPanel.MaxSupply` W。太阳能板产生 HV 电力，下方必须有 HV 电缆接入电网。

## 电力桥接

太阳能适合与 [AME](ame.html) 同时启动，可延长电池续航并降低其他发电机负载，为高级引擎争取时间。

## 调整面板

太阳在太空中持续移动，太阳能板必须追踪太阳。连接太阳能控制电脑可调整朝向和追踪速率。

<entity id="ComputerSolarControl"></entity>

太阳移动速度每班次不同，应观察后调好速率。电脑也会报告总发电量。

## 建造

在太阳能组件上使用两块玻璃即可制作。

<entity id="SolarAssembly"></entity>
<entity id="SheetGlass10"></entity>
<entity id="SolarPanel"></entity>

太阳能组件可向货运购买。

## 维修

<entity id="SolarPanelBroken"></entity>
<entity id="Crowbar"></entity>
<entity id="ShardGlass"></entity>
<entity id="Welder"></entity>

用撬棍取出破碎玻璃，将碎片焊回玻璃板，再重新安装到组件上。

## 搭建阵列

开局太阳能板通常未对准且未接电网。需要从机房铺设 HV 线，并用控制电脑对准。机房通常有控制电脑和 [SMES](PowerStorage)。

<entity id="SignDirectionalSolar"></entity>
<entity id="AirlockEngineering"></entity>

## 升级

把普通玻璃替换为等离子玻璃或铀玻璃。

<entity id="SolarPanelPlasma"></entity>
<entity id="SolarPanelUranium"></entity>

分别最多输出 `SolarPanelPlasma.SolarPanel.MaxSupply` W 和 `SolarPanelUranium.SolarPanel.MaxSupply` W，耐久也更高。
