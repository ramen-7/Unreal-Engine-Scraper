<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D?application_version=5.7 -->

# Set Control Vector2D

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
7. Set Control Vector2D

# Set Control Vector2D

SetControlVector2D is used to perform a change in the hierarchy by setting a single control's Vector2D value.

On this page

### Description

SetControlVector2D is used to perform a change in the hierarchy by setting a single control's Vector2D value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetControlVector2D,SetGizmoVector2D |
| Type | [FRigUnit\_SetControlVector2D](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetControlVector2D) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector | The 2d vector value to get / set for the given Control. | [Vector 2D](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to set the value for. | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Weight | The weight of the change - how much the change should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetControlVector2D?application_version=5.7#inputs)
