---
id: xenoarchaeology
title: 异星考古
group: 异星考古
order: 10
source: ServerInfo/Guidebook/Science/Xenoarchaeology.xml
---

# 异星考古

异星考古是科研部的一个分支，主要研究外星**神器（Artifact）**。

解开神器的秘密可以获得研究点，并揭示奇怪、可能有用或危险的效果。

完整的节点、触发条件和实验操作见[神器完全指南](artifact-guide.html)。

回合开始时，科研部通常有一到两个神器。更多神器可以通过以下方式获得：

- 向**货运部**订购
- 由**打捞队**发现
- 使用**碎片**重新组装
- 在特定空间站事件中出现

## 神器

<entity id="ComplexXenoArtifact"></entity>
<entity id="ComplexXenoArtifactItem"></entity>

神器内部包含按**层阶（Class）**排列的**节点（Node）**。

- 解锁一个节点后，会继续开放其上层的相连节点。
- 每个节点都有**触发条件（Trigger）**，必须在神器附近完成对应动作才能解锁。
- 节点解锁后会触发其**效果（Effect）**，并在控制台中显示为**[激活]**。
- 每个节点都有**耐久度（Durability）**：解锁后可以手动激活的次数。
- 越高的节点越难到达，但会提供更多**研究点（Research Points）**。
- 解锁全部节点没有额外奖励，但每个节点都会提供研究点。

## 设备

<entity id="MachineArtifactAnalyzer" caption="神器分析器"></entity>
<entity id="ComputerAnalysisConsole" caption="分析控制台"></entity>
<entity id="NodeScanner" caption="节点扫描器"></entity>

- **神器分析器（Artifact Analyzer）：** 固定设备，用于扫描神器并将数据发送到分析控制台。
- **[分析控制台](analysis-console.html)：** 固定设备，用于显示节点树。必须使用多功能工具与神器分析器连接。
- **节点扫描器（Node Scanner）：** 手持设备，可以显示当前正在触发的节点 ID，以及神器是否已经准备好触发。科研人员可以直接在实验舱内或附近查看状态。

<entity id="CrateArtifactContainer" caption="神器运输箱"></entity>
<entity id="HandheldArtifactContainer" caption="手持神器收容器"></entity>

- **神器收容器：** 可以安全储存和运输神器，并阻止节点被触发。

<entity id="MachineArtifactCrusher" caption="神器粉碎机"></entity>

- **神器粉碎机（Artifact Crusher）：** 将神器粉碎成碎片。四个碎片可以重新组成一个新神器。

<entity id="ArtifactFragment" caption="神器碎片"></entity>

- **神器碎片：** 被摧毁神器的残片。收集四个碎片后，可以通过制造菜单重组为新的神器。
