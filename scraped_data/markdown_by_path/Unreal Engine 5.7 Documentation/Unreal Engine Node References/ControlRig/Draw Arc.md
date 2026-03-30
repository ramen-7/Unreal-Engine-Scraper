<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc?application_version=5.7 -->

# Draw Arc

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
7. Draw Arc

# Draw Arc

Draws an arc in the viewport, can take in different min and max degrees

On this page

### Description

Draws an arc in the viewport, can take in different min and max degrees

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw Ellipse, Draw Circle |
| Type | [FRigVMFunction\_DebugArcNoSpace](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugArcNoSpace) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The transform of the arc to draw | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Color | The color to use for the debug draw | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Radius | The radius of the arc to draw | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MinimumDegrees | The minimum angle in degrees of the arc | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaximumDegrees | The maximum angle in degrees of the arc | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 360.000000 |
| Thickness | The line thickness to use for the debug draw | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Detail | The detail to use when drawing the arc | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawArc?application_version=5.7#inputs)
