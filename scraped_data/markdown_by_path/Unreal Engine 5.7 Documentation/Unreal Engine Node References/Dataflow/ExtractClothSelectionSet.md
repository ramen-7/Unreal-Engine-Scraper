<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet?application_version=5.7 -->

# ExtractClothSelectionSet

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
7. ExtractClothSelectionSet

# ExtractClothSelectionSet

ExtractClothSelectionSet (v1)

On this page

### Description

ExtractClothSelectionSet (v1)
Experimental

Extract a selection set from a Cloth Collection.

Input(s) :
Selection - Name of the selection set to be extracted. Currently only SimVertices3D and RenderVertices sets are supported.
DynamicMesh - Dynamic mesh used to reorder indices.

Output(s):
ExtractedSelectionSet - Extracted Selection Set as a Set
ExtractedSelectionArray - Extracted Selection Set as an array

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Extract Cloth Selection Set |
| Type | [FChaosClothAssetExtractSelectionSetNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetExtractSelection-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bReorderForDynamicMesh | Reorder extracted indices to match the order of a DynamicMesh that was created via ClothCollectionToDynamicMesh | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh | Dynamic mesh used to reorder indices. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExtractedSelectionSet | Extracted Selection Set as a Set | [TSet](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| ExtractedSelectionArray | Extracted Selection Set as an array | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet?application_version=5.7#outputs)
