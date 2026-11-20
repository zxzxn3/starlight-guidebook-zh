---
id: inspecting-power
title: 检查电力
group: 岗位
order: 48
source: ServerInfo/Guidebook/Engineering/InspectingPower.xml
---

# 检查电力

工程师可以用电力监控电脑查看全部电网。

<entity id="ComputerPowerMonitoring"></entity>

地图会显示 LV/MV/HV 电网、APC、SMES、变电站和所有发电机；统计区显示发电机总输出、电池总使用量和全网负载。

理想状态下，发电机输出应接近总负载，电池使用量应较低：

- 发电机输出低于负载：电力赤字。
- 电池使用量高：电池正在补足缺口。
- 电池使用量为零且发电机输出仍低于负载：电池耗尽，空间站正在压降供电。
- 发电机输出高于总负载：SMES 正在充电。

## 设备标签

点击发电机可查看其供电目标和输出；点击 SMES、变电站或 APC 可查看两端电网、输入、输出和设备连接。

## 多用工具

<entity id="Multitool"></entity>

对电缆使用多用工具可查看当前供电、电池供电、理论最大供电、实际需求、正在充电容量和正在放电容量。结果只代表该电缆所属电压网络，局部 LV 与全站 HV 的统计不同。
