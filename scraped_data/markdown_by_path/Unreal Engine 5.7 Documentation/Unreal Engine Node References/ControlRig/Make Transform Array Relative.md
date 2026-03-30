<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative?application_version=5.7 -->

# Make Transform Array Relative

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
7. Make Transform Array Relative

# Make Transform Array Relative

Treats the provided transforms as a chain with global / local transforms, and

On this page

### Description

Treats the provided transforms as a chain with global / local transforms, and
projects each transform into the target space. Optionally you can provide
a custom parent indices array, with which you can represent more than just chains.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | Local,Global,Absolute,Array,Accumulate |
| Type | [FRigVMFunction\_MathTransformAccumulateArray](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformAccu-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transforms | The input transform array to accumulate | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetSpace | Defines the space to project to | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| Root | Provides the parent transform for the root | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ParentIndices | If this array is the same size as the transforms array the indices will be used to look up each transform's parent. They are expected to be in order. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeTransformArrayRelative?application_version=5.7#inputs)
