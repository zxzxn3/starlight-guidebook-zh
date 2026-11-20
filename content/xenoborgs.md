---
id: xenoborgs
title: 异形赛博格
group: 敌对角色
order: 15
source: ServerInfo/Guidebook/Antagonist/Xenoborgs.xml
---

# 异形赛博格

<entity id="MMIFilled"></entity>

异形赛博格是自我复制的机械生物，会摘取活体或赛博格的智慧大脑，交给母舰装入空底盘。

## 目标

杀死并采集全站智慧大脑，带回母舰核心；收集材料制造更多异形赛博格；不惜代价保护母舰。

## 母舰核心

<entity id="MothershipCore"></entity>

母舰核心是异形赛博格的生命核心和唯一制造者，被毁后全部异形赛博格都会毁灭。核心不能移动，可制造专属升级模块。

## 转化船员

<entity id="MachineArtifactCrusher" caption="尸体粉碎机"></entity>

赛博格带回尸体并放入粉碎机，母舰核心消耗材料打印空底盘。用撬棍打开底盘，取出空 MMI；有机大脑装入 MMI，硅基大脑可直接放入，然后装回底盘、命名、升级模块并关闭锁定。

新赛博格初始无电，需要充电。

## 底盘

所有底盘都带定位母舰的针指器、GPS、材料袋和基础工具。

<entity id="XenoborgModuleBasic" caption="基础模块"></entity>
<entity id="XenoborgModuleTool" caption="工具模块"></entity>

### 工程型

<entity id="XenoborgEngi"></entity>

工程型负责入侵和打开入口，内置门禁破解器和工程工具。

<entity id="XenoborgModuleAccessBreaker"></entity>
<entity id="XenoborgModuleFireExtinguisher"></entity>

### 重型

<entity id="XenoborgHeavy"></entity>

移动慢但耐久高，内置激光和无线电干扰器。

<entity id="XenoborgModuleLaser"></entity>
<entity id="XenoborgModuleJammer"></entity>
<entity id="XenoborgModuleHeavyLaser"></entity>

### 侦察型

<entity id="XenoborgScout"></entity>

快速近战单位，内置喷气背包，负责运送尸体和救援太空中的赛博格。

<entity id="XenoborgModuleSword"></entity>
<entity id="XenoborgModuleSpaceMovement"></entity>
<entity id="XenoborgModuleEnergySword"></entity>

### 潜行型

<entity id="XenoborgStealth"></entity>

无固定武器，使用催眠注射器和隐形设备绑架目标，也能用变色龙投影仪伪装成物品。

<entity id="XenoborgModuleHypo"></entity>
<entity id="XenoborgModuleChameleonProjector"></entity>
<entity id="XenoborgModuleCloakDevice"></entity>
<entity id="XenoborgModuleSuperCloakDevice"></entity>

## 战术

跃迁前关闭 IFF，攻击前讨论目标。未暴露时间越长，异形赛博格越危险。

## 法则

<entity id="XenoborgCircuitBoard"></entity>

母舰核心：1. 你是母舰核心。2. 不惜代价保护自身。3. 保护所有异形赛博格。4. 制造更多异形赛博格。5. 让赛博格送来材料和智慧大脑。

异形赛博格：1. 不惜代价保护母舰。2. 保护自身。3. 保护其他异形赛博格。4. 制造更多异形赛博格。5. 把材料和智慧大脑送到母舰核心。

## 胜负

异形赛博格大胜：回合结束时数量多于活着的船员。
船员大胜：母舰核心和一个或多个异形赛博格被毁，或剩余异形赛博格过少。
