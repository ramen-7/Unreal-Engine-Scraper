<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel?application_version=5.7 -->

# Line Trace By Trace Channel

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
7. Line Trace By Trace Channel

# Line Trace By Trace Channel

Performs a line trace against the world and return the first blocking hit using a specific channel.

On this page

### Description

Performs a line trace against the world and return the first blocking hit using a specific channel. Target objects can have different object types, but they need to have the same trace channel set to "block" in their collision response settings.
You can create custom trace channels in Project Setting - Collision.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Line,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_LineTraceByTraceChannel](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_LineTraceByTraceChannel) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| TraceChannel | The 'channel' that this trace is in, used to determine which components to hit | [Trace Type Query](/documentation/en-us/unreal-engine/API/Runtime/Engine/ETraceTypeQuery) | TraceTypeQuery1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/LineTraceByTraceChannel?application_version=5.7#outputs)
