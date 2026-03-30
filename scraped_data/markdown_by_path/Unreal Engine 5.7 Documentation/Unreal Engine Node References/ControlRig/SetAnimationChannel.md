<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel?application_version=5.7 -->

# SetAnimationChannel

1. ![Epic Games](https://edc-cdn.net/assets/images/logo-epic.svg)[Developer](/)
2. [Documentation](/documentation/ "Documentation")
3. Unreal Engine
   * [Unreal Engine](/documentation/en-us/unreal-engine)
   * [Fortnite](/documentation/en-us/fortnite)
   * [Twinmotion](/documentation/en-us/twinmotion)
   * [MetaHuman](/documentation/en-us/metahuman)
   * [RealityScan](/documentation/en-us/realityscan)
   * [RealityScan Mobile](/documentation/en-us/realityscan-mobile)
   * [Fab](/documentation/en-us/fab)
4. [Unreal Engine 5.7 Documentation](/documentation/en-us/unreal-engine/unreal-engine-5-7-documentation "Unreal Engine 5.7 Documentation")
5. [Unreal Engine Node References](/documentation/en-us/unreal-engine/node-reference "Unreal Engine Node References")
6. [ControlRig](/documentation/en-us/unreal-engine/node-reference/ControlRig "ControlRig")
7. SetAnimationChannel

# SetAnimationChannel

Set Bool Channel is used to set a control's animation channel value

On this page

### Description

Set Bool Channel is used to set a control's animation channel value
Set Float Channel is used to set a control's animation channel value
Set Int Channel is used to set a control's animation channel value
Set Vector2D Channel is used to set a control's animation channel value
Set Vector Channel is used to set a control's animation channel value
Set Rotator Channel is used to set a control's animation channel value
Set Transform Channel is used to set a control's animation channel value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetAnimationChannel,Set Bool Channel,Animation,Channel,Set Float Channel,Set Int Channel,Set Vector2D Channel,Set Vector Channel,Set Rotator Channel,Set Transform Channel |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The new value of the animation channel | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Control | The name of the Control to retrieve the value for. | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Channel | The name of the animation channel to retrieve the value for. | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bInitial | If set to true the initial value will be returned | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationChannel?application_version=5.7#inputs)
