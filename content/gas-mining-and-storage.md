---
id: gas-mining-and-storage
title: 气体开采与储存
group: 岗位
order: 86
source: ServerInfo/Guidebook/Engineering/GasMiningAndStorage.xml
---

# 气体开采与储存

气体不断被消耗或泄漏，空间站必须持续开采并储存。

## 气体采矿机

<entity id="GasMinerOxygenStation"></entity>
<entity id="GasMinerNitrogenStation"></entity>

采矿机无需电力，持续向所在环境输出常温气体，达到截止压力后停止。用 <kbd>ExamineEntity</kbd> 检查可查看信息。

<entity id="GasMinerNitrogen" caption="300 kPa"></entity>
<entity id="GasMinerNitrogenStation" caption="1000 kPa"></entity>
<entity id="GasMinerNitrogenStationLarge" caption="4500 kPa"></entity>

更大型号截止压力更高。脱离后可用扳手重新固定。

## 储气

储气罐接收采矿机气体并供其他系统使用。回收管网会把回收气体送回储气罐；配气网络和燃烧室会消耗气体。

出气端为被动通风口时，可用[气体分析仪](atmos-tools.html)测量泵入口，从而判断储罐气体。
