<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation?application_version=5.7 -->

# Distribute Rotation

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
7. Distribute Rotation

# Distribute Rotation

Distributes rotations provided across a array of items.

On this page

### Description

Distributes rotations provided across a array of items.
Each rotation is expressed by a quaternion and a ratio, where the ratio is between 0.0 and 1.0
Note: This node adds rotation in local space of each item!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwistBones |
| Type | [FRigUnit\_DistributeRotationForItemArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DistributeRotationForIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to use to distribute the rotation | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Rotations | The list of rotations to be applied | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_DistributeRotation\_Rotation](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DistributeRotation_Rota-)> | () |
| RotationEaseType | The easing to use between to rotations. | [Rig VMAnim Easing Type](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| Weight | The weight of the solver - how much the rotation should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/DistributeRotation?application_version=5.7#inputs)
