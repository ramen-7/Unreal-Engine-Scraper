<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints?application_version=5.7 -->

# Spline From Points

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
7. Spline From Points

# Spline From Points

Creates a Spline curve from an array of positions

On this page

### Description

Creates a Spline curve from an array of positions

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Tags | Spline From Positions |
| Type | [FRigUnit\_ControlRigSplineFromPoints](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_ControlRigSplineFromPoi-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | The input points to form the spline | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> | () |
| SplineMode | The mode to use for the spline | [Spline Type](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/ESplineType) | Hermite |
| bClosed | If True the spline will be closed | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SamplesPerSegment | Specifies the detail per segment of the spline | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| Compression | The amount of compression to apply | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Stretch | The amount of stretch to allow for the spline | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The resulting spline | [Control Rig Spline](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SplineFromPoints?application_version=5.7#outputs)
