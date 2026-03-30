<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms?application_version=5.7 -->

# Modify Transforms

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
7. Modify Transforms

# Modify Transforms

Modify Transforms is used to perform a change in the hierarchy by setting one or more bones' transforms

On this page

### Description

Modify Transforms is used to perform a change in the hierarchy by setting one or more bones' transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | ModifyBone |
| Type | [FRigUnit\_ModifyTransforms](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ModifyTransforms) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ItemToModify | The items to modify. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_ModifyTransforms\_PerItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ModifyTransforms_PerIte-)> | (()) |
| Weight | At 1 this sets the transform, between 0 and 1 the transform is blended with previous results. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| WeightMinimum | The minimum of the weight - defaults to 0.0 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WeightMaximum | The maximum of the weight - defaults to 1.0 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Mode | Defines if the bone's transform should be set in local or global space, additive or override. | [Control Rig Modify Bone Mode](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigModifyBoneMode) | AdditiveLocal |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ModifyTransforms?application_version=5.7#inputs)
