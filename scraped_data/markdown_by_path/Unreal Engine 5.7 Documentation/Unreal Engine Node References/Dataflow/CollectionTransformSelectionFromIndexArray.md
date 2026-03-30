<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray?application_version=5.7 -->

# CollectionTransformSelectionFromIndexArray

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
7. CollectionTransformSelectionFromIndexArray

# CollectionTransformSelectionFromIndexArray

CollectionTransformSelectionFromIndexArray (v1)

On this page

### Description

CollectionTransformSelectionFromIndexArray (v1)

Convert index array to a transform selection

Input(s) :
Collection [Intrinsic] - Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection.
BoneIndices - Array of bone indices to convert to a trannsform selection

Output(s):
Collection [Passthrough] - Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection.
TransformSelection - Array of the selected bone indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Array |
| Type | [FCollectionTransformSelectionFromIndexArrayDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_11) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndices | Array of bone indices to convert to a trannsform selection | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use for the selection. Note only valid bone indices for the collection will be included in the output selection. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Array of the selected bone indices | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray?application_version=5.7#outputs)
