---
id: cyborgs
title: 赛博格（Cyborg）
group: 机器人
order: 20
source: ServerInfo/_Starlight/Guidebook/Science/Cyborgs.xml
---

# 赛博格（Cyborg）

赛博格是人机混合体，由科研部的[机器人学](robotics.html)分支制造，用于承担空间站上的各种任务。它们受严格遵循的**硅基法则（Silicon Laws）**约束，无条件服务船员。

> 注意：无法则赛博格仍受服务器规则约束，只受其适用的硅基法则管理。

## 基础部件

<entity id="CyborgEndoskeleton" caption="赛博格内骨骼"></entity>
<entity id="ExosuitFabricator" caption="外骨骼制造机"></entity>

所有赛博格都以**内骨骼（Endoskeleton）**为基础，可在**外骨骼制造机**中制造。**检查**内骨骼可以查看后续装配步骤。完成组装后，还可以通过模块或更好的电池增加工具、延长续航。

新制造的赛博格需要一个能与电子身体连接的**大脑**。主要类型有两种，而且在底盘被拆解、更换或意外解体后，两者都可以继续独立说话。

- **人机接口（MMI）：** 让生物大脑与电子部件通信的装置。遭受严重工伤的船员可以在身体失去后继续服务。
- **正电子脑（Positronic Brain）：** 完全人工的大脑，可以自发产生神经活动。合成神经元的解析时间并不固定，但制造赛博格时不需要从船员身上取出大脑。

<entity id="MMIFilled" caption="人机接口（MMI）"></entity>
<entity id="PositronicBrain" caption="正电子脑"></entity>

两种大脑都不需要额外科技即可制造。

## 赛博格类型

赛博格制造完成后，需要为底盘（Chassis）选择一种岗位。岗位决定初始模块、可安装的额外模块，以及可使用的**部门无线电频道**。所有赛博格都能使用**科研频道**和**全站频道**，并且拥有**全区域通行权限**。

<entity id="BorgChassisGeneric" caption="通用型"></entity>
<entity id="BorgChassisEngineer" caption="工程型"></entity>
<entity id="BorgChassisMining" caption="打捞型"></entity>
<entity id="BorgChassisJanitor" caption="清洁型"></entity>
<entity id="BorgChassisService" caption="服务型"></entity>
<entity id="BorgChassisMedical" caption="医疗型"></entity>
<entity id="BorgChassisPurrfus" caption="Purrfus 型"></entity>
<entity id="BorgChassisCargo" caption="货运型"></entity>

*不同类型的赛博格底盘。*

底盘专精一旦确定就不能直接更改。要更换类型，必须制造新底盘。旧底盘中的大脑、电池和兼容模块可以转移过去。

## 模块

<entity id="BorgModuleTool" caption="赛博格工具模块"></entity>

赛博格没有手，主要通过各种**模块（Module）**拾取和操作物品。每种底盘都有自己的初始模块，额外模块可以作为升级安装。额外模块可在**外骨骼制造机**中打印。

**通用模块**提供多功能工具，例如撬棍、GPS 和线缆交互能力，可装入任何底盘。**通用型底盘最多可安装五个额外模块。**

<entity id="BorgModuleCable" caption="线缆模块"></entity>
<entity id="BorgModuleFireExtinguisher" caption="灭火器模块"></entity>

*通用模块示例。*

需要专门功能时，可以安装**专用模块**，例如扫描异常、建造墙壁、急救船员或清理润滑液。专用模块通常使用所属部门的配色。除**科研模块**可装入任何底盘外，其余专用模块只能装入对应底盘。**工程、清洁、服务、医疗和采矿专用底盘最多可安装三个额外模块。**

<entity id="BorgModuleAnomaly" caption="异常研究模块"></entity>
<entity id="BorgModuleRCD" caption="RCD 模块"></entity>
<entity id="BorgModuleMining" caption="采矿模块"></entity>
<entity id="BorgModuleCleaning" caption="清洁模块"></entity>
<entity id="BorgModuleService" caption="服务模块"></entity>
<entity id="BorgModuleChemical" caption="化学模块"></entity>

*专用模块示例。注意外壳和电路板的颜色。*

科学家研究新[科技](technologies.html)后，还会解锁更高级或更特殊的模块。

## 硅基法则

法则优先于其他所有玩法和角色扮演规则。如果法则明确要求你违反服务器规则，你必须执行。

- 缺少相关法则不能作为违反服务器规则的理由。没有优先于服务器规则的法则时，服务器规则仍然生效。
- 模糊法则通常不允许你违反服务器规则。如果理解不清，或某种解释会让你违反服务器规则，请先 Ahelp。

按顺序执行法则；编号最小、位于最上方或发生故障的法则优先于下方法则。

你不能主动要求改法，也不能同意未经授权的改法。

- 根据指挥 SOP 获得授权的改法应当允许，除非与现有法则冲突。
- 改变法则本身不算违反当前法则；未来在新法则下的行为也不应被视为违反旧法则。
- 面对未经授权的改法，可以按当前法则使用致命武力。

你必须保持对法则解释的一致性。

员工身份决定谁或什么是“船员”。带有适当岗位图标的个体视为船员。

- 持有有效证件的僵尸、敌对角色和核行动人员仍视为船员。
- 访客在人事主管正式雇佣前不是船员；访客图标为灰色 V。
- 囚犯不是船员，不应听从其命令；囚犯图标为监狱栏杆。

“伤害船员”指实际造成的人身伤害，优先考虑迫近程度和发生可能性。

对于不合理的命令，可以拒绝。例如要求硅基生命无正当理由自我永久移除，或要求你数清空间站上的所有灯。

## 公司法

赛博格、个人 AI 和站级 AI 等硅基生命受公司法中的特定保护与例外条款约束。表现出感知与智能的低级机器人也可能适用。

硅基生命天然受法则束缚，因此拥有一个硅基生命不构成非法拘禁。盗窃硅基生命属于重大盗窃。

- 对硅基生命施加暴力，应按严重程度视为破坏公物或损坏财产；底盘被摧毁或进入危急状态则属于毁坏财产。
- 硅基生命在执行命令时违反法律，责任归于下达命令的人。若硅基生命不受“必须服从命令”的标准法则约束，则需为自己的行为和犯罪负责。
- 只有在保障船员安全时，才可修改硅基法则。非标准法则只要不威胁船员，就可以保留。无法则硅基生命若违反公司法，其法则可以作为判决的一部分被修改。
- 来自非 NanoTrasen 势力的敌对硅基生命属于非船员实体，不享有其他硅基生命的公司法保护，应按其敌意和危险程度处理。
