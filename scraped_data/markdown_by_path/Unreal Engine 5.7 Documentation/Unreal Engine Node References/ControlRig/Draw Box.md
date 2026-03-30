<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox?application_version=5.7 -->

# Draw Box

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
7. Draw Box

# Draw Box

Draws a box in the viewport

On this page

### Description

Draws a box in the viewport

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | BoundingBox,Bbox |
| Type | [FRigVMFunction\_DebugBoxNoSpace](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_DebugBoxNoSpace) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The input bounding box to draw | [Box](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Color | The color to use for the debug draw | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use for the debug draw | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the positions with | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawBox?application_version=5.7#inputs)
