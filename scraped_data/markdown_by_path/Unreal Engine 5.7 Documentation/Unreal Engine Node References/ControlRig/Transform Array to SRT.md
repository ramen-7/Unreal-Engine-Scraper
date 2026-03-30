<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT?application_version=5.7 -->

# Transform Array to SRT

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
7. Transform Array to SRT

# Transform Array to SRT

Decomposes a Transform Array to its components.

On this page

### Description

Decomposes a Transform Array to its components.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | EulerTransform,Scale,Rotation,Orientation,Translation,Location |
| Type | [FRigVMFunction\_MathTransformArrayToSRT](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformArra-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The input transform array to decompose | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Translations | The array of translations - one for each input transform | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Rotations | The array of rotation - one for each input transform | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FQuat](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Scales | The array of scale values - one for each input transform | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformArraytoSRT?application_version=5.7#outputs)
