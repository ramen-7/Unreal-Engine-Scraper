<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap?application_version=5.7 -->

# Remap

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
7. Remap

# Remap

Remaps the given value from a source range to a target range.

On this page

### Description

Remaps the given value from a source range to a target range.
Remaps the given value from a source range to a target range for each component

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Remap,Rescale,Scale |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to remap | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SourceMinimum | The minimum of the range of the input / source value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SourceMaximum | The maximum of the range of the input / source value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| TargetMinimum | The minimum of the range of the output / target value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| TargetMaximum | The maximum of the range of the output / target value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| bClamp | If set to true the result is clamped to the target range | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting remapped value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Remap?application_version=5.7#outputs)
