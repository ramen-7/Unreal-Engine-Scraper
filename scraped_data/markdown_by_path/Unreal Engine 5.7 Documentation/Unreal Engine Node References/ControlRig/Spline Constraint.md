<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint?application_version=5.7 -->

# Spline Constraint

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
7. Spline Constraint

# Spline Constraint

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
| Type | [FRigUnit\_SplineConstraint](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_SplineConstraint) |

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
| PrimaryAxis | The primary axis to use when building transforms | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The secondary axis to use when building transforms | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineConstraint?application_version=5.7#inputs)
