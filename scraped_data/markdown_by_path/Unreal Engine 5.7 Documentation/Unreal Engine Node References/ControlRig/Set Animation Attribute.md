<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute?application_version=5.7 -->

# Set Animation Attribute

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
7. Set Animation Attribute

# Set Animation Attribute

Modify an animation attribute if one is found, otherwise add a new animation attribute

On this page

### Description

Modify an animation attribute if one is found, otherwise add a new animation attribute

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Animation Attribute |
| Type | [FRigDispatch\_SetAnimAttribute](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetAnimAttribute) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the animation attribute | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BoneName | The name of the bone that stores the attribute, default to root bone if set to none | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Value | The value to get / set | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore),[int32](/documentation/en-us/unreal-engine/API/Runtime/Core),[FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString),[FQuat](/documentation/en-us/unreal-engine/API/Runtime/Core),[FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core),[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core),User Defined Structs,[FPoseHistoryAnimationAttribute](/documentation/en-us/unreal-engine/API/Plugins/PoseSearch/FPoseHistoryAnimationAttribute) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the animation attribute was successfully stored | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetAnimationAttribute?application_version=5.7#outputs)
