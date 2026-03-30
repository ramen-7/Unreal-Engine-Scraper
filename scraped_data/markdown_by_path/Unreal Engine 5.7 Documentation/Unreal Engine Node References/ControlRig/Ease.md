<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease?application_version=5.7 -->

# Ease

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
7. Ease

# Ease

Returns the eased version of the input value

On this page

### Description

Returns the eased version of the input value

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Easing,Profile,Smooth,Cubic |
| Type | [FRigVMFunction\_AnimEasing](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_AnimEasing) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to ease using the easing functions | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Type | The type of easing to apply | [Rig VMAnim Easing Type](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | CubicEaseInOut |
| SourceMinimum | The minimum value of the input | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SourceMaximum | The maximum value of the input | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| TargetMinimum | The minimum value of the output | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| TargetMaximum | The maximum value of the output | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting eased output value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Ease?application_version=5.7#outputs)
