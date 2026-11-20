---
id: defusal
title: 大型炸弹拆除
group: 岗位
order: 103
source: ServerInfo/Guidebook/Security/Defusal.xml
---

# 大型炸弹拆除

大型炸弹倒计时很长，但会在船体上炸出大洞。

## 装备

<entity id="Wirecutter"></entity>
<entity id="Screwdriver"></entity>
<entity id="Multitool"></entity>

剪线钳和螺丝刀是必要工具，多用工具可帮助识别线路。防爆服或其他防护装备能降低被炸碎的风险。

<entity id="ClothingHeadHelmetBombSuit"></entity>
<entity id="ClothingOuterSuitBomb"></entity>
<entity id="ClothingOuterHardsuitRd"></entity>
<entity id="ClothingOuterHardsuitAtmos"></entity>

## 炸弹类型

<entity id="SyndicateBomb"></entity>
<entity id="TrainingBomb"></entity>

训练炸弹只造成轻微船体损伤；辛迪加炸弹会炸出大洞，无防护人员会被直接绞碎。

## 启动与计时

右键选择开始倒计时，或 Alt + 点击炸弹即可启动。最短 `SyndicateBomb.TimerTrigger.ShortestDelayOption` 秒，最长 `SyndicateBomb.TimerTrigger.LongestDelayOption` 秒。剪断 PRCD 线后无法通过检查查看时间。

## 螺栓

启动后炸弹会固定在地面。剪断 BOLT 线即可解除固定，随后可用扳手拆下并丢入太空。

## 线路

用螺丝刀打开面板。标准辛迪加炸弹约有 10 根线：3 根假线、3 根爆炸线，其余功能如下。可以脉冲、剪断或修复。

- **LIVE**：脉冲延迟 30 秒；已启动时剪断可拆弹，未启动时会开始计时。
- **PRCD**：脉冲使时间前进 15 秒；剪断隐藏计时显示。
- **DLAY**：脉冲延迟 30 秒。
- **BOOM**：已启动时脉冲或剪断会立即爆炸；未启动时剪断会禁用炸弹，修复可重新启用。
- **BOLT**：脉冲转动螺栓；剪断解除固定；修复恢复。
- **Dummy**：任何操作都无效。
