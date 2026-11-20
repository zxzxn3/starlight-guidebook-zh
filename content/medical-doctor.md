---
id: medical-doctor
title: 医生
group: 岗位
order: 20
source: ServerInfo/Guidebook/Medical/MedicalDoctor.xml
---

# 医生

医生负责治疗空间站船员的各类伤痛，从擦伤到严重烧伤。本页介绍治疗选择、分诊和后续照护。

## 基础

判断伤情有两种方法：用健康分析仪或医疗 PDA 扫描，或 Shift + 点击检查并点击心脏图标。

分析仪能发现检查看不到的毒素和辐射伤害，但会发出声音并消耗电池。

<entity id="SignExamroom" caption="检查病人"></entity>
<entity id="MedicalPDA"></entity>
<entity id="MedicalInternPDA" caption="实习生 PDA"></entity>
<entity id="HandheldHealthAnalyzer"></entity>

## 药物与治疗

多数药物有过量阈值，过量会伤害病人。药丸需要时间代谢；需要快速起效时使用注射器。

- 钝击伤害：Bicaridine 或 Bruise Pack。
- 烧伤：Dermaline 或 Ointment。
- 毒素（中毒）：Dylovene。
- 毒素（辐射）：Hyronalin 或 Arithrazine。
- 缺氧：Resomi/Avali 用 Amoxla，其他种族用 Dexaline；所有种族都可用 Inaprovaline。
- 失血：Resomi/Avali 用 Amoxla，其他种族用 Dexaline Plus。检查病人，皮肤苍白就说明仍需补血或补铁。
- 出血：Tranexamic Acid 和纱布；烧伤也可烧灼止血。

<entity id="MedkitFilled"></entity>
<entity id="MedkitBruteFilled" caption="钝伤包"></entity>
<entity id="MedkitRadiationFilled" caption="辐射包"></entity>
<entity id="MedkitBurnFilled" caption="烧伤包"></entity>
<entity id="MedkitToxinFilled" caption="毒素包"></entity>
<entity id="Brutepack"></entity>
<entity id="Ointment"></entity>
<entity id="EmergencyMedipen"></entity>
<entity id="Bloodpack"></entity>
<entity id="Gauze"></entity>

## 基础治疗与分诊

检查病人是否活着、是否出血、受到何种伤害。100 点伤害进入濒死，200 点伤害死亡。紧急注射器和 Epinephrine 常用于稳定病人。

条件允许时把病人固定到医疗床。需要时间治疗时，可固定到停滞床；但停滞状态下代谢和药物几乎停止，需要恢复代谢后药物才有效。血袋、药膏和钝伤包仍正常工作。

<entity id="MedicalBed"></entity>
<entity id="StasisBed"></entity>

## 判断尸体

1. 检查时若显示“Their soul has departed.”，说明灵魂已离开，玩家无法复活；没有这句话则可以尝试复苏。
2. 尸体是否腐烂？腐烂尸体只能用克隆，除颤器无效。
3. 有灵魂且未腐烂时可以复苏。暂时没时间时，应把尸体放入停尸柜，避免腐烂。

## 复苏

除缺氧外，除颤器可以复苏总伤害低于 200 的病人。死者体内药物不代谢，但仍可用钝伤包和药膏降低伤害，使数值达到复苏条件。

<entity id="Brutepack"></entity>
<entity id="Defibrillator"></entity>
<entity id="Ointment"></entity>
