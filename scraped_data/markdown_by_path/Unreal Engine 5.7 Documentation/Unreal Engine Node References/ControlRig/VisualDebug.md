<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug?application_version=5.7 -->

# VisualDebug

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
7. VisualDebug

# VisualDebug

Debug draw parameters for an Axis given a quaternion

On this page

### Description

Debug draw parameters for an Axis given a quaternion
Debug draw parameters for an Axis given a transform

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | VisualDebug,Visual Debug Quat,Draw,Rotation,Visual Debug Transform,Axes |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The pass through rotation to draw | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnabled | If set to False the debug drawing will be skipped | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Thickness | The line thickness to use for the drawing | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Scale | The scale to apply to the axes drawn | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualDebug?application_version=5.7#inputs)
