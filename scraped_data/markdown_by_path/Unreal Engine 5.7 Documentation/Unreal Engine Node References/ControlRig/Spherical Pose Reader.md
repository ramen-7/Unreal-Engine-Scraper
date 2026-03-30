<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader?application_version=5.7 -->

# Spherical Pose Reader

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
7. Spherical Pose Reader

# Spherical Pose Reader

Outputs a float value between 0-1 based off of the driver item's rotation in a specified region.

On this page

### Description

Outputs a float value between 0-1 based off of the driver item's rotation in a specified region.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Pose Reader, SPR |
| Type | [FRigUnit\_SphericalPoseReader](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphericalPoseReader) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriverItem | The bone that will drive the output parameter when rotated into the active regions of this pose reader. | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| DriverAxis | The axis of the driver transform that is compared against the falloff regions. Typically the axis that is pointing at the child; usually X by convention. Default is X-axis (1,0,0). | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| RotationOffset | Rotate the entire falloff region to align with the desired area of effect. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=90.000000,Y=0.000000,Z=0.000000) |
| ActiveRegionSize | The size of the active region (green) that outputs the full value (1.0). Range is 0-1. Default is 0.1. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ActiveRegionScaleFactors | The directional scaling parameters for the active region (green). | [Region Scale Factors](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRegionScaleFactors) | (PositiveWidth=1.000000,NegativeWidth=1.000000,PositiveHeight=1.000000,NegativeHeight=1.000000) |
| FalloffSize | The size of the falloff region (yellow) that defines the start of the output range. A value of 1 wraps the entire sphere with falloff. Range is 0-1. Default is 0.2. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |
| FalloffRegionScaleFactors | The directional scaling parameters for the falloff region (yellow). | [Region Scale Factors](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRegionScaleFactors) | (PositiveWidth=1.000000,NegativeWidth=1.000000,PositiveHeight=1.000000,NegativeHeight=1.000000) |
| FlipWidthScaling | Flip the positive / negative directions of the width scale factors. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| FlipHeightScaling | Flip the positive / negative directions of the height scale factors. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| OptionalParentItem | An optional parent to use as a stable frame of reference for the active regions (defaults to DriverItem's parent if unset). | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Debug | The debug settings | [Spherical Pose Reader Debug Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FSphericalPoseReaderDebugSetting-) | (bDrawDebug=True,bDraw2D=False,bDrawLocalAxes=False,DebugScale=25.000000,DebugSegments=20,DebugThickness=0.250000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputParam | The normalized output parameter; ranges from 0 (when outside yellow region) to 1 (in the green region) and smoothly blends from 0-1 in the yellow region. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphericalPoseReader?application_version=5.7#outputs)
