<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector?application_version=5.7 -->

# RBF Vector

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
7. RBF Vector

# RBF Vector

A RBF interpolator from vector to float

On this page

### Description

A RBF interpolator from vector to float
A RBF interpolator from vector to vector
A RBF interpolator from vector to color
A RBF interpolator from vector to quaternion
A RBF interpolator from vector to transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|RBF Interpolation |
| Tags | RBF Vector,RBF Vector to Float,RBF,Interpolate,Vector,RBF Vector to Vector,RBF Vector to Color,RBF Vector to Quat,RBF Vector to Transform |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The array of targets to interpolate within | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorFloat\_Target](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorFloat_T-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorVector\_Target](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorVector_-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorColor\_Target](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorColor_T-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorQuat\_Target](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorQuat_Ta-)>   [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMathRBFInterpolateVectorXform\_Target](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FMathRBFInterpolateVectorXform_T-)> | () |
| Input | The input vector | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| DistanceFunction | The distance function to use | [RBFVector Distance Type](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFVectorDistanceType) | Euclidean |
| SmoothingFunction | The smoothing function to use | [RBFKernel Type](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERBFKernelType) | Gaussian |
| SmoothingRadius | The radius to apply for the smoothing function | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| bNormalizeOutput | If true the resulting output will be normalized | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The interpolated result | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/RBFVector?application_version=5.7#outputs)
