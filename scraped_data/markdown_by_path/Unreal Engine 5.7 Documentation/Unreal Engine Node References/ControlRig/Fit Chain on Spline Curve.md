<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve?application_version=5.7 -->

# Fit Chain on Spline Curve

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
7. Fit Chain on Spline Curve

# Fit Chain on Spline Curve

Fits a given chain to a spline curve.

On this page

### Description

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Fit,Resample,Spline |
| Type | [FRigUnit\_FitChainToSplineCurveItemArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_FitChainToSplineCurveIt-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to align | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Spline | The curve to align to | [Control Rig Spline](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Alignment | Specifies how to align the chain on the curve | [Control Rig Curve Alignment](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigCurveAlignment) | Stretched |
| Minimum | The minimum U value to use on the curve | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | The maximum U value to use on the curve | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SamplingPrecision | The number of samples to use on the curve. Clamped at 64. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |
| PrimaryAxis | The major axis being aligned - along the bone | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the pole vector. You can use (0.0, 0.0, 0.0) to disable it. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PoleVectorPosition | The position of the pole vector used for aligning the secondary axis. Only has an effect if the secondary axis is set. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotations | The list of rotations to be applied along the curve | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_FitChainToCurve\_Rotation](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FitChainToCurve_Rotatio-)> | () |
| RotationEaseType | The easing to use between to rotations. | [Rig VMAnim Easing Type](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| Weight | The weight of the solver - how much the rotation should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The debug settings to use | [Rig Unit Fit Chain to Curve Debug Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FitChainToCurve_DebugSe-) | (bEnabled=False,Scale=1.000000,CurveColor=(R=1.000000,G=1.000000,B=0.000000,A=1.000000),SegmentsColor=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/FitChainonSplineCurve?application_version=5.7#inputs)
