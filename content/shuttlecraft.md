---
id: shuttlecraft
title: 穿梭机建造
group: 岗位
order: 53
source: ServerInfo/Guidebook/Engineering/Shuttlecraft.xml
---

# 穿梭机建造

穿梭机建造流程直接，但昂贵且很难在一小时内完成。有充足空闲时间并想挑战时可以尝试。

## 所需部件

<entity id="Thruster"></entity>
<entity id="Gyroscope"></entity>
<entity id="ComputerShuttle"></entity>
<entity id="SubstationBasic"></entity>
<entity id="PortableGeneratorPacman" caption="P.A.C.M.A.N."></entity>
<entity id="CableHVStack"></entity>
<entity id="CableMVStack"></entity>
<entity id="CableApcStack"></entity>
<entity id="APCBasic"></entity>

可选：

<entity id="AirCanister"></entity>
<entity id="LightTube" caption="照明"></entity>
<entity id="AirlockGlassShuttle"></entity>
<entity id="SMESBasic"></entity>
<entity id="MobCorgiIan"></entity>
<entity id="NuclearBomb"></entity>

## 地基

带钢板和金属杆进入太空，在空间站边缘放置格栅。先留出 3–4 格间距，再铺设至少 3×3 的平台，并用一条格栅与空间站相连。

完成后用剪线钳切断连接空间站的格栅。新平台会成为独立网格，不受空间站锚定和重力影响。

<entity id="SheetSteel"></entity>
<entity id="PartRodMetal"></entity>
<entity id="FloorTileItemSteel"></entity>
<entity id="FloorTileItemDark"></entity>
<entity id="FloorTileItemWhite"></entity>

## 对接端口

穿梭机气闸可安全对接到空间站。朝向很重要，气闸底部的小凸起表示对接方向。

<entity id="AirlockShuttle"></entity>
<entity id="AirlockGlassShuttle"></entity>

## 方向控制

在平台四周安装推进器，建议每侧一个，以便任意方向移动。喷口必须朝向太空，前方有方块时不会点火。即使已固定，也可用 <kbd>RotateObjectClockwise</kbd> / <kbd>RotateObjectCounterclockwise</kbd> 旋转。

空手按 <kbd>Use</kbd> 或按 <kbd>ActivateItemInWorld</kbd> 可启停推进器。

## 旋转控制

<entity id="Gyroscope"></entity>

安装陀螺仪控制旋转。位置不如推进器关键，但应方便供电。质量很大时可能需要多个陀螺仪。

## 供电

小型穿梭机可用 J.R.P.A.C.M.A.N. 直接提供 LV。也可使用穿梭机 APU 或固定发电机，它们输出 HV，需要经壁挂变电站降至 MV 和 LV。

<entity id="PortableGeneratorJrPacman" caption="J.R.P.A.C.M.A.N."></entity>
<entity id="WeldingFuelTankFull"></entity>
<entity id="GeneratorWallmountAPU"></entity>
<entity id="GeneratorBasic15kW"></entity>
<entity id="SubstationWallBasic"></entity>

## 驾驶

安装穿梭机控制电脑，确认推进器和陀螺仪都接好 MV、LV 电力。完成后即可驾驶。
