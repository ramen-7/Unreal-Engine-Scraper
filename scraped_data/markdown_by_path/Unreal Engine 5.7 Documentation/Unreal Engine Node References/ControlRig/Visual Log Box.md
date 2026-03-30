<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox?application_version=5.7 -->

# Visual Log Box

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
7. Visual Log Box

# Visual Log Box

Logs box shape - recording for Visual Logs has to be enabled to record this data

On this page

### Description

Logs box shape - recording for Visual Logs has to be enabled to record this data

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Debug |
| Tags | Draw,String |
| Type | [FRigVMFunction\_VisualLogBox](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VisualLogBox) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | The box to draw | [Box](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| bWireframe | Whether to display as wireframe | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ObjectColor | The color of the logged object | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| Text | The text to log | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Category | The category of the logged text | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | VisLogRigVM |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/VisualLogBox?application_version=5.7#inputs)
