<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector?application_version=5.7 -->

# Set Control Vector

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
7. Set Control Vector

# Set Control Vector

SetControlVector is used to perform a change in the hierarchy by setting a single control's Vector value.

On this page

### Description

SetControlVector is used to perform a change in the hierarchy by setting a single control's Vector value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlVector,SetGizmoVector |
| Type | [FRigUnit\_SetControlVector](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlVector) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The vector value to get / set for the given Control. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Space | Defines if the bone's transform should be set in local or global space. | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector?application_version=5.7#inputs)
