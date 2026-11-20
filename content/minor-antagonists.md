---
id: minor-antagonists
title: 次要敌对角色
group: 敌对角色
order: 16
source: ServerInfo/Guidebook/Antagonist/MinorAntagonists.xml
---

# 次要敌对角色

次要敌对角色由幽灵控制，给死亡玩家再次互动的机会，通常由随机事件产生。

## 悖论克隆体

<entity id="ParadoxCloneDummy"></entity>

随机船员被时空异常抛入本宇宙后形成的完美副本。为了修复悖论，必须找到并杀死原体。双方都认为自己是原体，船员记忆也会同时支持两人的历史，因此不能只凭记忆判断。

悖论克隆体没有特殊能力，但外观、DNA、指纹、服装、装备和 ID 完全相同。

## 亡魂

<entity id="MobRevenant"></entity>

亡魂是吸食生命精华的虚体。可以摧毁燃烧室或使空间站失压来取得灵魂。

- 精华既是生命值，也是能力资源。
- 用 <kbd>Use</kbd> 检查灵魂价值，再在目标濒死、死亡或睡眠时吸取。
- 吸取或使用能力时会出现 Corporeal 状态，此时可被攻击。

## 鼠王

<entity id="MobRatKing"></entity>

鼠王是巨型鼠类，目标是建立鼠群并大量进食。它们可以与船员交易，但船员阻挡取食时可视为紧急食物。

- 能力消耗饥饿度。
- **Raise Army** 可召唤鼠仆，并命令其停留、跟随或攻击。
- **Rat King's Domain** 制造对人有毒、对鼠类治疗的氨气。
- **Rummage** 可翻找垃圾处理设施获得食物。

鼠王和鼠仆能说话，可钻过气闸和桌子，但鼠仆仍很脆弱。

## 太空龙

<entity id="MobDragon"></entity>
<entity id="CarpRift"></entity>

太空龙是能吞食船员并制造鲤鱼裂隙的巨型跨维度鱼类，属于优先威胁，指挥人员不应与其交易。

- **Devour** 可吞食门窗墙壁，也可吞食昏迷或死亡船员治疗自身。
- **Dragon's Breath** 发射直线火焰弹，沿途多次爆炸并点燃物体。
- **Summon Carp Rift** 制造裂隙，每 5 分钟充能期间会生成太空鲤鱼；充能期间可被摧毁。

裂隙未充能就被毁会对龙造成暂时严重反噬。若五分钟后仍无裂隙充能，龙会消失；拥有三个充满裂隙后不会消失，但仍可被杀死。

## 史莱姆与蜘蛛

<entity id="MobAdultSlimesBlueAngry"></entity>
<entity id="MobGiantSpiderAngry"></entity>

敌对史莱姆和蜘蛛受饥饿和领地攻击性驱使。史莱姆可能依颜色造成额外细胞或毒素伤害，怕水；蜘蛛有毒牙、蛛网和开门能力。

## Scrapper

<entity id="DroneRogue"></entity>

Scrapper 是偷取资源并复制自身的失控无人机，会破坏空间站运作。它们通常依赖 Scrapper 外骨骼制造机生产工具和更多单位，能爬通风管偷取物资，但一般以生产为核心。
