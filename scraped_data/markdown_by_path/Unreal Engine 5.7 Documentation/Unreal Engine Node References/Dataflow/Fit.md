<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit?application_version=5.7 -->

# Fit

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
7. Fit

# Fit

Fit (v1)

On this page

### Description

Fit (v1)

Fits a value from one range to another
Returns a number between newmin and newmax that is relative to num in the range between oldmin and oldmax.
If the value is outside the old range, it will be clamped to the new range.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FFitDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFitDataflowNode) |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit?application_version=5.7#outputs)
