<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo?application_version=5.7 -->

# Chain Info

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
7. Chain Info

# Chain Info

Retrieves various pieces of info about an interpolated transform hierarchy from an rig element item list

On this page

### Description

Retrieves various pieces of info about an interpolated transform hierarchy from an rig element item list

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Chain |
| Type | [FRigUnit\_ChainInfo](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainInfo) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to use to interpret the chain | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Param | The parameter value down the chain of items from 0 to 1 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bCalculateStretch | If True calculate stretch factors of chain and current segment | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bInitial | If True use initial transform values for chain | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDebug | Enable debug draw for node | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugScale | Debug draw scale | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InterpolatedTransform | The interpolated transform at the chain's input parameter | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| ChainLength | The length of the interpolated chain | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| ParamLength | The parametric length of the interpolated chain | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| ChainStretchFactor | Stretch factor of chain | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| SegmentInfo | Segment Info | [Rig Unit Chain Info Segment Info](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainInfo_SegmentInfo) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainInfo?application_version=5.7#outputs)
