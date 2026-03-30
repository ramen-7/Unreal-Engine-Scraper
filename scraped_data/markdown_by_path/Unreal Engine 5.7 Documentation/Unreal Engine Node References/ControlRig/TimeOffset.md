<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset?application_version=5.7 -->

# TimeOffset

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
7. TimeOffset

# TimeOffset

Records a value over time and can access the value from the past

On this page

### Description

Records a value over time and can access the value from the past

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | TimeOffset,Value Over Time (Float),Buffer,Delta,History,Previous,Delay,Value Over Time (Vector),Value Over Time (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to record | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SecondsAgo | Seconds of time in the past you want to query the value for | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| BufferSize | The sampling precision of the buffer. The higher the more precise - the more memory usage. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| TimeRange | The maximum time required for offsetting in seconds. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting offset value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TimeOffset?application_version=5.7#outputs)
