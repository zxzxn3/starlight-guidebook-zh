---
id: airlocks
title: 气闸
group: 岗位
order: 27
source: ServerInfo/Guidebook/Engineering/Airlocks.xml
---

# 气闸

气闸用于控制空间站各区域通行。

<entity id="Airlock"></entity>
<entity id="AirlockGlass"></entity>

空手按 <kbd>Use</kbd>、双手占满时按 <kbd>ActivateItemInWorld</kbd>，或直接撞向气闸，都可以开门。门只会在携带正确权限 ID 时打开。ID 可以拿在手上或放在 ID 槽中；持有多个 ID 时会全部检查，PDA 中的 ID 也一样。

可以用门禁配置器修改权限，也可以用多用工具修改门电子元件，但需要先拆门。

<entity id="AccessConfigurator"></entity>
<entity id="Multitool"></entity>
<entity id="DoorElectronics"></entity>

气闸能阻挡气体流动，可用于封闭[破洞](Spacing)或[火灾](Fires)区域。即使关闭，门所在格仍可能储存气体；气体泄漏期间开门要小心。

## 锁定与紧急通行

气闸可以上锁，防止手动打开或撬开，顶部会亮红灯。

紧急通行模式允许任何人开门，不受权限限制，顶部会闪烁黄灯。

## 远程控制

气闸可由空间站 AI 或门遥控器远程控制。

<entity id="PlayerStationAiEmpty"></entity>
<entity id="DoorRemoteEngineering"></entity>
<entity id="DoorRemoteCommand"></entity>
<entity id="DoorRemoteMedical"></entity>
<entity id="DoorRemoteService"></entity>
<entity id="DoorRemoteSecurity"></entity>
<entity id="DoorRemoteResearch"></entity>

部门主管通常持有本部门门遥控器，可以开关门、上锁和启用紧急通行。

## 连接

气闸可以通过[网络连接](Networking)系统连接其他设备，例如连接通往太空的门，或将多扇气闸联动。

## 外观

不同部门有不同外观风格，颜色通常对应权限。

<entity id="AirlockCargo"></entity>
<entity id="AirlockCommand"></entity>
<entity id="AirlockNT"></entity>
<entity id="AirlockEngineering"></entity>
<entity id="AirlockMedical"></entity>
<entity id="AirlockScience"></entity>
<entity id="AirlockSecurity"></entity>
<entity id="AirlockCargoGlass"></entity>
<entity id="AirlockCommandGlass"></entity>
<entity id="AirlockNTGlass"></entity>
<entity id="AirlockEngineeringGlass"></entity>
<entity id="AirlockMedicalGlass"></entity>
<entity id="AirlockScienceGlass"></entity>
<entity id="AirlockSecurityGlass"></entity>

可以用喷漆器重新上色。

<entity id="SprayPainter"></entity>

## 线路

用螺丝刀打开维护面板后可接触内部线路。每根线控制一项功能；脉冲、剪切或修复会产生不同效果。

线路旁指示灯表示状态：

- 稳定亮起：系统正常。
- 闪烁：系统故障或行为异常。
- 不亮：没有供电。

线路功能：

- **BOLT**：脉冲切换锁定；剪断会锁定；修复无效。
- **POWR**：脉冲短暂断电；剪断一根会短路并电击无绝缘手套者，剪断两根才完全断电；修复可停止短路或恢复供电。
- **LOG**：脉冲暂时禁用记录；剪断永久禁用；修复恢复。
- **BLIT**：脉冲暂时关闭或开启锁定指示灯；剪断使灯不亮；修复恢复。
- **TIMR**：脉冲暂时缩短关门计时；剪断取消失效，安全后立即关门；修复恢复。
- **SAFE**：脉冲暂时关闭安全系统；剪断后即使有障碍也会关门；修复恢复。
- **AIA**：脉冲无效；剪断禁止 AI 控制；修复恢复。
