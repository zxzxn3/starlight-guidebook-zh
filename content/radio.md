---
id: radio
title: 无线电与语音
group: 新玩家与基础
order: 20
source: ServerInfo/Guidebook/NewPlayer/Controls/Radio.xml
---

# 语音与文字频道

交流是 Space Station 14 的重要部分。按 <kbd>FocusChatInputWindow</kbd> 可以跳到聊天输入框。

输入框旁的文字表示消息将发送到哪个频道，也决定角色会以什么方式说出输入内容。

Local 是正常音量的普通交谈。

Whisper 只有附近的人能听见。通过无线电发送消息时，角色会自动低声说话。

Emote 是角色做出的动作，任何没有失明的人都能接收。哑剧演员经常使用各种表情动作。

以 <kbd>FocusWhisperChatWindow</kbd> 开始输入可以发送低语；以 `(@)` 开始输入可以发送动作。

按 <kbd>CycleChatChannelForward</kbd> 可以依次切换所有文字频道。

站得离对方太远时，对方可能听不清全部内容，低语时尤其明显。

## 无线电

无线电可以与全站以及所属部门通讯。

<entity id="ClothingHeadsetAssistant"></entity>

在文字前输入分号 `;`，即可通过公共频道发送全站无线电消息。紧挨着你的玩家可能听到无线电消息的片段，即使他们没有对应频道权限。注意隔墙偷听者。

## 部门无线电

只要佩戴装有本部门加密钥匙的耳机，就可以输入冒号 `:` 和部门字母，通过部门无线电频道发送消息。

检查耳机可以查看可用频道。

<entity id="ClothingHeadsetEngineering"></entity>

检查未改装的工程耳机，可以看到公共频道和工程频道的前缀。

也可以使用 `:h`。这个快捷方式会自动选择所属部门频道。例如空间站工程师使用 `:h` 时，等同于 `:e`。

## 加密钥匙

加密钥匙授予对应频道权限。前面检查的工程耳机之所以显示公共和工程频道，是因为工程耳机自带这两种加密钥匙。

<entity id="EncryptionKeyCommon"></entity>
<entity id="EncryptionKeyEngineering"></entity>

用螺丝刀可以取出耳机中的加密钥匙。手上拿着加密钥匙并点击耳机，可以安装新钥匙。

所有指挥人员都带有自己所属频道的备用钥匙。更换岗位时也可以在人事主管办公室申请。

## OOC 频道

OOC（Out of Character）频道位于游戏世界之外，包括 LOOC、OOC 和死亡聊天。

LOOC 在回合中开放；OOC 通常在回合结束后开放；死亡聊天只有角色死亡后才能查看和发言。

不要通过 Discord 或在回合中开放的 OOC 讨论当前回合。
