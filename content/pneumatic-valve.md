---
id: pneumatic-valve
title: 气动阀
group: 岗位
order: 67
source: ServerInfo/Guidebook/Engineering/PneumaticValve.xml
---

# 气动阀

<entity id="PressureControlledValve"></entity>

气动阀由压力控制，具有输入/输出端和控制端，可双向工作。输出压力比控制压力低 `PressureControlledValve.PressureControlledValve.Threshold` kPa 以上时开启；输出压力接近控制压力时关闭。

控制压力可通过管网和泵实时调整。气动阀依靠输入侧压力被动输气，有时填充速度比泵更快，但压力控制精度不如泵。

可用于按控制压力快速填充，或自动排放燃烧室气体。
