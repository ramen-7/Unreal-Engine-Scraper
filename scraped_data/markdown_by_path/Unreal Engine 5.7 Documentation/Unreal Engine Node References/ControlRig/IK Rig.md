<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig?application_version=5.7 -->

# IK Rig

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
7. IK Rig

# IK Rig

Supply an IK Rig asset and provide goal transforms to run IK on the skeleton.

On this page

### Description

Supply an IK Rig asset and provide goal transforms to run IK on the skeleton.

### Information

|  |  |
| --- | --- |
| Plugin | [IKRig](/documentation/en-us/unreal-engine/API/PluginIndex/IKRig) |
| Category | Hierarchy |
| Tags | IK Rig, IK |
| Type | [FRigUnit\_IKRig](/documentation/en-us/unreal-engine/API/Plugins/IKRig/FRigUnit_IKRig) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IKRigAsset | An IK Rig asset to be evaluated. | IKRig Definition | None |
| Goals | A list of Goals to solve. These must match what is in the IK Rig, any missing Goals will have their alphas set to zero. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FIKRigGoalInput](/documentation/en-us/unreal-engine/API/Plugins/IKRig/FIKRigGoalInput)> | () |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IKRig?application_version=5.7#inputs)
