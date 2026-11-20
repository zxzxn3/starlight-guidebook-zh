---
id: thermomachines
title: 温控机
group: 岗位
order: 78
source: ServerInfo/Guidebook/Engineering/Thermomachines.xml
---

# 温控机

温控机用电加热或冷却管网和环境中的气体。耗电越多，功率越大。接近目标温度时会降低输出，但待机仍消耗全功率。温度容差为 `GasThermoMachineFreezer.GasThermoMachine.TemperatureTolerance` K。

<entity id="SpaceHeater"></entity>
<entity id="GasThermoMachineHeater"></entity>
<entity id="GasThermoMachineFreezer"></entity>

## 空间加热器

便携式环境温控设备，温度范围 `SpaceHeater.SpaceHeater.MinTemperature`–`SpaceHeater.SpaceHeater.MaxTemperature` K，有三档功率。常用于植物学或科研。

## 管网温控机

固定式加热器或冷冻机，消耗 `GasThermoMachineFreezer.GasThermoMachine.HeatCapacity` W，温度范围 `GasThermoMachineFreezer.GasThermoMachine.MinTemperature`–`GasThermoMachineFreezer.GasThermoMachine.MaxTemperature` K。

拆解后用螺丝刀切换电路板可改变加热/冷却模式。电路板可在科研部的电路印刷机打印。

## Hellfire 温控机

<entity id="GasThermoMachineHellfireHeater"></entity>
<entity id="GasThermoMachineHellfireFreezer"></entity>

更强但更耗电，且会把 `GasThermoMachineHellfireFreezer.GasThermoMachine.EnergyLeakPercentage` 的能量泄漏到周围环境。
