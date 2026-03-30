<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue?application_version=5.7 -->

# SetMultiControlValue

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
7. SetMultiControlValue

# SetMultiControlValue

SetMultiControlFloat is used to perform a change in the hierarchy by setting multiple controls' float value.

On this page

### Description

SetMultiControlFloat is used to perform a change in the hierarchy by setting multiple controls' float value.
SetMultiControlInteger is used to perform a change in the hierarchy by setting multiple controls' integer value.
SetMultiControlVector2D is used to perform a change in the hierarchy by setting multiple controls' vector2D value.
SetMultiControlRotator is used to perform a change in the hierarchy by setting multiple controls' rotator value.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | SetMultiControlValue,Set Multiple Controls Float,SetMultipleControlsFloat,SetControlFloat,SetGizmoFloat,Set Multiple Controls Integer,SetMultipleControlsInteger,SetControlInteger,SetGizmoInteger,Set Multiple Controls Vector2D,SetMultipleControlsVector2D,SetControlVector2D,SetGizmoVector2D,Set Multiple Controls Rotator,SetMultipleControlsRotator,SetControlRotator,SetGizmoRotator |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Entries | The array of control-float pairs to be processed | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlFloat\_Entry](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlFloat_En-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlInteger\_Entry](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlInteger_-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlVector2D\_Entry](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlVector2D-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_SetMultiControlRotator\_Entry](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetMultiControlRotator_-)> | (()) |
| Weight | The weight of the change - how much the change should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetMultiControlValue?application_version=5.7#inputs)
