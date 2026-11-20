---
id: air-vent
title: 通风口
group: 岗位
order: 57
source: ServerInfo/Guidebook/Engineering/AirVent.xml
---

# 通风口

<entity id="GasVentPump"></entity>

通风口用于向房间输入气体，直到达到设定压力。需要附近 LV 电缆供电，可用焊接器封死。

## 默认运行

默认向环境输出气体，外部压力上限为 `GasVentPump.GasVentPump.DefaultExternalBound` kPa。速度与“两倍管网压力减去环境压力”成正比。

## 压力锁定

环境压力低于 `GasVentPump.GasVentPump.UnderPressureLockoutThreshold` kPa 时进入锁定，避免向破洞房间浪费气体，指示灯变黄。可右键选择解除锁定，或在空气警报上设为 Fill。锁定状态下仍会极慢漏气。

## 设置

连接空气警报后可选择：

- **Releasing**：从管网向环境放气。
- **Siphoning**：从环境抽气到管网，指示灯变红。

PressureBound 决定限制方式：

- **ExternalBound**：遵守环境压力上下限。
- **InternalBound**：遵守管网压力上下限。
- **Both**：同时遵守两者。
- **NoBound**：不限制。

External bound 可视为环境上限，Internal bound 可视为管网下限。
