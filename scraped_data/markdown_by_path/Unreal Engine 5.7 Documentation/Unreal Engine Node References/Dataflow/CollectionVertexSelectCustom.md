<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom?application_version=5.7 -->

# CollectionVertexSelectCustom

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
7. CollectionVertexSelectCustom

# CollectionVertexSelectCustom

CollectionVertexSelectCustom (v1)

On this page

### Description

CollectionVertexSelectCustom (v1)

Selects specified vertices in the GeometryCollection by using a
space separated list

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
VertexSelection - Vertex selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Vertex |
| Type | [FCollectionVertexSelectionCustomDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionVertexSelectionCustom-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexIndicies | Space separated list of vertex indices to specify the selection | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexIndicies | Space separated list of vertex indices to specify the selection | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VertexSelection | Vertex selection including the new indices | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom?application_version=5.7#outputs)
