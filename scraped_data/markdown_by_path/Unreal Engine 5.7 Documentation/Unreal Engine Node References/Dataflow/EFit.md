<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit?application_version=5.7 -->

# EFit

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
6. [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow "Dataflow")
7. EFit

# EFit

EFit (v1)

On this page

### Description

EFit (v1)

Fits a value from one range to another

Takes the value num from the range (oldmin, oldmax) and shifts it to the corresponding value in the new range (newmin, newmax). Unlike fit, this function does not clamp values in the given range.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FEFitDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FEFitDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Float |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| OldMin |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| OldMax |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| NewMin |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| NewMax |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit?application_version=5.7#outputs)
