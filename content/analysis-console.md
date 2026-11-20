---
id: analysis-console
title: 分析控制台
group: 异星考古
order: 30
source: ServerInfo/Guidebook/Science/AnalysisConsole.xml
---

# 分析控制台

分析控制台（Analysis Console）用于和神器交互。它可以查看节点、触发条件（Triggers）和效果，也可以提取研究点（Research Points）。

<entity id="ComputerAnalysisConsole" caption="分析控制台"></entity>

控制台会显示神器节点树的详细信息，包括：

- **ID：** 与节点扫描器配合使用的唯一标识。
- **层阶（Class）：** 节点所在的层级名称；同一层节点共享该层阶。
- **状态：**
  - **锁定（Locked）：** 默认状态。
  - **激活（Active）：** 第一次触发后的状态。
  - **已解锁（Unlocked）：** 到达更深节点后，较浅节点会显示此状态，并禁止手动激活。
- **耐久度（Durability）：** 剩余可手动激活次数。
- **效果（Effect）：** 节点激活或手动触发时会发生什么。
- **触发条件（Triggers）：** 解锁节点需要完成的动作。
- **服务器（Server）：** 选择接收提取研究点的研发服务器。
- **提取点数（Extract Points）：** 提取自上次提取以来新解锁节点所产生的研究点。
