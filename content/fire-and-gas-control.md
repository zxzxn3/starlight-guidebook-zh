---
id: fire-and-gas-control
title: 火灾与气体控制
group: 岗位
order: 87
source: ServerInfo/Guidebook/Engineering/FireAndGasControl.xml
---

# 火灾与气体控制

<entity id="Firelock"></entity>
<entity id="FirelockGlass"></entity>
<entity id="FirelockEdge"></entity>
<entity id="FireAlarm"></entity>

## 防火门

防火门根据自身传感器或空气警报、火灾警报指令关闭，隔离危险区域。

空间站通过关键位置的防火门划分区域，防止危险沿走廊和开放空间扩散。

未连接警报时，两侧温差达到 `Firelock.Firelock.TemperatureThreshold` K，或压差达到 `Firelock.Firelock.PressureThreshold` kPa 时关闭。

持续异常会进入锁定，亮红灯，不能手动撬开，只能由有工程权限者或撬棍打开。断电锁定门只能用撬棍打开。

两侧环境恢复到容差范围后解除锁定。注意，两侧相同不代表两侧安全，例如两侧都已失压。

## 连接警报

防火门通过 List 系统连接到空气或火灾警报。每扇门有独立地址。

空气警报进入 Danger 时防火门关闭，回到 Green 时打开；锁定状态需警报重新发送绿色状态后才恢复。火灾警报触发时防火门关闭，重置后打开。

## 火灾警报

<entity id="FireAlarm"></entity>

传感器可连接到火灾警报。传感器进入危险温度阈值时触发警报，使所有连接防火门关闭。恢复正常温度后自动清除。也可手动触发和重置。
