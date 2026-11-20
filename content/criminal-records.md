---
id: criminal-records
title: 犯罪记录
group: 岗位
order: 104
source: ServerInfo/Guidebook/Security/CriminalRecords.xml
---

# 犯罪记录

<entity id="ComputerCriminalRecords"></entity>

犯罪记录电脑用于管理船员名单中每个人的犯罪历史和状态。所有人都能查看，只有安保权限可以修改。

界面包含姓名、指纹或 DNA 搜索、船员列表和犯罪记录详情。底部过滤器可只显示通缉、拘留或假释人员。

在记录中可查看身份信息，并在 None、Wanted、Detained 之间切换状态。设为 Wanted 时必须填写原因；逮捕后应改为 Detained，释放后改回 None。

## 犯罪历史

将状态设为逮捕后，电脑会自动添加一条以 `ARRESTED:` 开头的记录。也可以点击 **Add** 手动填写罪行和刑期，班次时间会自动加入。

选择不需要的记录并点击 **Delete** 可删除。
