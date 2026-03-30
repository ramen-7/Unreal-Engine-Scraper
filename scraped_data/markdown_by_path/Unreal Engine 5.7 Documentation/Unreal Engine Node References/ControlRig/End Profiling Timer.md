<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer?application_version=5.7 -->

# End Profiling Timer

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
7. End Profiling Timer

# End Profiling Timer

Ends an existing profiling timer for debugging, used in conjunction with Start Profiling Timer

On this page

### Description

Ends an existing profiling timer for debugging, used in conjunction with Start Profiling Timer

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Debug |
| Tags | Measure,StopProfiling,Meter,Profile |
| Type | [FRigUnit\_EndProfilingTimer](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_EndProfilingTimer) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumberOfMeasurements | The number of measurements to take for profiling | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| Prefix | The prefix to use when printing to the log | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Timer |
| DebugDrawSettings | The debug draw settings for this node | [Rig VMDebug Draw Settings](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDebugDrawSettings) | (DepthPriority=SDPG\_Foreground,Lifetime=-1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/EndProfilingTimer?application_version=5.7#inputs)
