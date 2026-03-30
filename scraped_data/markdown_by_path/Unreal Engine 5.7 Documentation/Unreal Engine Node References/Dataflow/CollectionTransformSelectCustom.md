<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom?application_version=5.7 -->

# CollectionTransformSelectCustom

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
7. CollectionTransformSelectCustom

# CollectionTransformSelectCustom

CollectionTransformSelectCustom (v2)

On this page

### Description

CollectionTransformSelectCustom (v2)

Selects specified bones in the GeometryCollection by using a
comma separated list, e.g. "0, 2, 5-10, 12-15"

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionCustomDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_10) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndices | Comma separated list of single or a range of bone indices to specify the selection, e.g. "0, 2, 5-10, 12-15" | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndices | Comma separated list of single or a range of bone indices to specify the selection, e.g. "0, 2, 5-10, 12-15" | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom?application_version=5.7#outputs)
