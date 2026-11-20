---
id: air-alarms
title: 空气警报
group: 岗位
order: 92
source: ServerInfo/Guidebook/Engineering/AirAlarms.xml
---

# 空气警报

<entity id="AirAlarm"></entity>

空气警报集中监控和控制连接的大气设备。界面顶部显示压力、温度与状态；中部列出通风口、洗涤器和传感器；底部设置模式与自动切换。

## 状态

- **Normal**：空气可安全呼吸。
- **Warning**：环境开始偏离，逐渐危险。
- **Danger**：不再安全，需要内部供气或太空服。

Danger 时自动关闭防火门，恢复正常后打开。三种状态都能输出信号。

## 传感器

通风口和洗涤器内置传感器。可在 **Sensors** 页调整阈值。传感器检测到压力、温度或气体组成超限时改变警报状态。

也可另建空气传感器并连接警报，用于没有通风口或洗涤器的区域。

<entity id="AirSensor"></entity>

## 模式

- **None**：禁用全部连接设备。
- **Filtering**：通风口按标准压力送气，洗涤器清除废气。
- **Filtering (Wide)**：同上，但全部洗涤器启用 WideNet。
- **Fill**：通风口以 `GasVentPump.GasVentPump.MaxPressure` kPa 送气，洗涤器关闭。
- **Panic**：通风口关闭，洗涤器全部抽气。

Danger 以上自动切换 Wide，Normal 或 Warning 自动恢复普通 Filtering。可用 **Auto** 关闭自动切换。
