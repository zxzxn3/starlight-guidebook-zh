---
id: salvage
title: 打捞
group: 岗位
order: 18
source: ServerInfo/Guidebook/Cargo/Salvage.xml
---

# 打捞

打捞是货运的重要收入来源，也是最危险的来源之一。打捞队从太空残骸和神秘采矿小行星获取财富。

太空充满危险，但准备充分并保持协作，任何打捞队都能为货运赚取大量资金。

## 准备

离站前必须准备所需装备，否则很可能还没见到收益就死亡。

<entity id="SuitStorageSalv"></entity>
<entity id="LockerSalvageSpecialist"></entity>
<entity id="VendingMachineSalvage"></entity>

打捞部起始房间提供离站所需物品。科研部能研发更好的武器和设备，但初始装备也比空手好。

<entity id="ClothingOuterHardsuitSpatio"></entity>
<entity id="ClothingShoesBootsMag"></entity>
<entity id="VendingMachineTankDispenserEVA"></entity>

- **Spationaut Hardsuit**：太空生存基础。记得打开头盔以便呼吸，并开启内置照明。
- **Magboots**：在残骸上提供抓地力，也能防止滑倒。
- **氧气/氮气**：Laspi 和 Vox 需要氮气，其他种族通常需要氧气。气体罐售货机可补充。

<entity id="WeaponProtoKineticAccelerator"></entity>

所有打捞专家都必须武装，以应对敌对生物。

- **Proto-Kinetic Accelerator（PKA）**：无限弹药，可缓慢采矿并在太空中推进。科研部可升级伤害、射程和射速。

<entity id="Pickaxe"></entity>
<entity id="OreBag"></entity>

- **Pickaxe**：以合理速度采矿所需，也可作为近战武器。
- **Ore Bag**：放在腰带槽后，会吸附并自动拾取附近矿石。

<entity id="FireExtinguisher"></entity>
<entity id="WeaponGrapplingGun"></entity>
<entity id="SalvagePDA"></entity>
<entity id="ComputerRadar"></entity>

- **Fire Extinguisher**：简易喷气背包。在太空中喷射会产生反作用力，可用任何液体补充。
- **Grappling Gun**：用普通枪械方式发射，装填可收回钩索。钩住物体后按 <kbd>UseSecondary</kbd> 拉近自己。
- **Salvage PDA**：内置 AstroNav GPS 程序，手持时可当 GPS 使用。离站前记录空间站坐标。
- **Mass Scanner Computer**：俯视显示空间站和附近物体，可用于确认残骸或小行星的位置和方向。

<entity id="RadioHandheld"></entity>
<entity id="HandheldGPSBasic"></entity>
<entity id="ClothingBeltUtilityFilled"></entity>

- **Handheld Radio**：普通无线电不可用时仍可与打捞队通讯。
- **GPS**：备用定位器，也适合新加入的打捞员。
- **Utility Belt**：拆解残骸机械时携带工具。不采矿时可一直佩戴。

## 打捞磁铁

<entity id="SalvageMagnet"></entity>

打捞磁铁会把太空残骸拉到附近。它提供五个随机选项，包括小行星、打捞残骸和太空碎片。选择后，目标会被拉来并保留 **6 分钟**；时间结束后，网格上剩余的战利品会消失。未选择的选项每 **3 分钟**刷新。

在六分钟内飞往目标，尽可能取得收益，然后返回空间站。

### 小行星

<entity id="Pickaxe"></entity>
<entity id="OreBag"></entity>
<entity id="OreProcessor"></entity>

磁铁会显示小行星资源类型，可据此决定优先级。小行星没有敌对生物，相对安全，但仍有其他威胁。

用镐和矿石袋采矿，再用矿石处理机把矿石精炼成材料。小心普通岩石中的 Gibtonite，受到扰动会爆炸。

### 太空碎片

<entity id="Wrench"></entity>
<entity id="FireExtinguisher"></entity>
<entity id="Recycler"></entity>

太空碎片能补充班次初期短缺的钢铁、玻璃等基础材料。散落的物品和废料需要逐件收集，可以拖来箱子或储物柜存放。

碎片中常有太空鲤鱼和 Sharkminnow 等危险生物，也可能埋有地雷。

返回后，把废料放入部门回收机，转化为材料交给货运。硬币、戒指和手表等贵重物品也应交给货运，在贸易站出售。

### 打捞残骸

<entity id="SurvivalKnife"></entity>
<entity id="Fulton"></entity>
<entity id="WeaponProtoKineticAccelerator"></entity>

磁铁会显示残骸规模。残骸的危险和价值差异很大，威胁通常比普通碎片更多样。与敌人保持距离，用 PKA 射击；留意贵重战利品和机械，并用估价工具判断价值。

## 进阶与升级

初始装备足以完成基础工作，但进阶装备能提高效率，并让打捞员挑战危险的采矿小行星。

### 打捞任务板

<entity id="ComputerSalvageJobBoard"></entity>

打捞任务板位于打捞舱，是打捞版的赏金电脑。完成指定材料任务可赚取 spesos，并解锁高级打捞装备。

收集完成后打印打捞任务运输标签，贴到装有货物的箱子或储物柜上，用估价工具确认后送往贸易站出售。完成后，货运请求电脑会解锁新的打捞专属箱子。

<entity id="Fulton1"></entity>
<entity id="WeaponCrusher"></entity>
<entity id="SeismicCharge"></entity>

- **Fulton**：与信标连接后，可附着在未固定的箱子或机械上，短暂等待后传送到信标，适合运输物品和人员。
- **Crusher 武器**：升级近战装备。Crusher Dagger 比生存刀挥动更快且自动攻击；Crusher 和 Crusher Glaive 是可发射特殊弹体的长柄武器。弹体本身无伤害，但快速近战被标记的敌人可吸血治疗。所有 Crusher 都带内置照明。
- **Seismic Charge**：采矿炸药，可破碎小行星或炸开危险残骸。可连接远程引爆器，或贴在墙上延时起爆。

### 与科研部合作

<entity id="ToyFigurineScientist"></entity>
<entity id="ResearchDisk"></entity>

科研部依赖打捞提供钢、塑料、玻璃，以及银、金、等离子和铀。打捞则依赖科研升级装备，双方应尽量优先处理对方需求。

<entity id="MiningDrill"></entity>
<entity id="HandHeldMassScanner"></entity>
<entity id="PKAUpgradeRange"></entity>

科研部可以提供：

- 采矿钻和矿物扫描仪，以及高产工业矿石处理机。
- 手持质量扫描仪，可在太空中查看自身位置。
- PKA 升级，最多安装两个，可从伤害、射速和射程中选择。

## 采矿小行星

熟悉打捞磁铁后，可以前往采矿小行星。通常需要穿梭机或喷气背包，内部极其危险，不建议独自探索。

<entity id="MobGoliath"></entity>
<entity id="MobHivelord"></entity>
<entity id="MobBasilisk"></entity>

小行星分为随机生成、充满敌人和材料的 Dungeon，以及分布大量矿脉、战利品和怪物的小行星区。

- **Goliath**：巨型生物，会用触手控制目标，再用巨爪和利齿攻击。可屠宰获得 Goliath Hide Plating，用于打捞任务和升级 Spationaut 太空服。
- **Hivelord**：快速而行动不规则的异常生物，会保持距离并生成小型 Brood 围攻。可屠宰获得快速腐烂的 Hivelord Core，用于任务，也可生吃快速治疗。
- **Basilisk**：冰壳怪物，会发射冷冻能量束造成伤害和减速。击败后可屠宰获得珍贵钻石矿。
