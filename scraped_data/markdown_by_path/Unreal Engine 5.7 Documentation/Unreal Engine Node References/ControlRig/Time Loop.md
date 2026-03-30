<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop?application_version=5.7 -->

# Time Loop

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
7. Time Loop

# Time Loop

Simulates a time value - and outputs loop information

On this page

### Description

Simulates a time value - and outputs loop information

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | Playback,Pause,Timeline |
| Type | [FRigVMFunction\_TimeLoop](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_TimeLoop) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Speed | The speed to play-back the time at | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Duration | the duration of a single loop in seconds | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Normalize | if set to true the output relative and flipflop will be normalized over the duration. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Absolute | the overall time in seconds | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Relative | the relative time in seconds (within the loop) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| FlipFlop | the relative time in seconds (within the loop), going from 0 to duration and then back from duration to 0, or 0 to 1 and 1 to 0 if Normalize is turned on | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Even | true if the iteration of the loop is even | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeLoop?application_version=5.7#outputs)
