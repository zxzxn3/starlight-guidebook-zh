---
id: shadekin
title: Shadekin
group: 种族
order: 28
source: ServerInfo/_Starlight/Guidebook/Mobs/Shadekin.xml
---

# Shadekin

<entity id="MobShadekin"></entity>

Shadekin 原本来自名为“The Dark”的另一个维度。受雇或与 NT 签约的 Shadekin 大多患有称为“Black-eye”的病症，Shadekin 自己则称其为“被灼烧”。这种状况使他们无法返回“The Dark”。

他们适应没有光的故乡，视觉对光照高度敏感。昏暗光线会持续造成不适，强光则会造成明显疼痛和伤害。

## 种族特征

- 受到热伤害高 20%，冷伤害低 25%，细胞伤害低 75%。
- 失血伤害高 170%，失血恢复速度慢 75%；辐射伤害高 30%，电击伤害高 25%。
- 不需要呼吸或空气。
- 闪光弹击晕时间翻倍。
- 爪击造成 5 点斩击伤害。

## Marish

Shadekin 共用一种只有单词“Mar”的语言。这个短词可以通过延长发音中的 A 或 R 改变长度和构成，表达复杂思想与深层情感。对 Shadekin 而言，它简单却无穷深。

## 年龄与姓名

Shadekin 的生理衰老极慢。18 岁即成熟并具备受雇资格，但通常到约 100 岁仍被视为年轻；100–200 岁为中年，200–300 岁开始进入老年。

姓名对 Shadekin 意义重大。这些姓名更接近头衔，在离开“The Dark”进入物质世界时获得，通常来自其表现出的属性或品质，也可能取自热爱的物品、热情或理念。部分 Shadekin 已适应并自行更换头衔。

这不是轻率决定；更换头衔相当于抛弃过去的自我。

## 夜视

Shadekin 适应故乡环境，拥有先天夜视，能在深渊般的黑暗中看清事物，不需要光源。

穿戴闪光免疫装备时，夜视会变为普通视野。可以使用 HUD 变体保留夜视功能和 HUD，但失去闪光免疫。

<entity id="ClothingEyesGlassesSecurity" caption="安保眼镜：没有夜视，具有闪光免疫"></entity>
<entity id="ClothingEyesHudSecurity" caption="安保 HUD：具有夜视，没有闪光免疫"></entity>

## 光敏感

- **黑暗**：被动恢复增强，具有夜视。
- **低光**：没有增益或减益。
- **烦人光照**：被动恢复失效。
- **强光**：严重减速。
- **极强光照**：每秒受到 1 点热伤害。
