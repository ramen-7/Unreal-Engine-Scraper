<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy?application_version=5.7 -->

# Draw Hierarchy

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
7. Draw Hierarchy

# Draw Hierarchy

Draws vectors on each bone in the viewport across the entire hierarchy

On this page

### Description

Draws vectors on each bone in the viewport across the entire hierarchy

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Type | [FRigUnit\_DebugHierarchy](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_DebugHierarchy) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | the items to draw the pose for. if this is empty we'll draw the whole hierarchy | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Scale | The scale to apply to the drawn transform | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| Color | The color to use when drawing | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| Thickness | The line thickness to use when drawing | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| WorldOffset | The world offset to pre-multiply the drawn transform with | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bEnabled | If set to False the debug drawing will be skipped | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawHierarchy?application_version=5.7#inputs)
