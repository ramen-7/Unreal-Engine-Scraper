<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport?application_version=5.7 -->

# ClothAssetImport

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
7. ClothAssetImport

# ClothAssetImport

ClothAssetImport (v1)

On this page

### Description

ClothAssetImport (v1)

For Reimport

Input(s) :
ClothAsset - The Cloth Asset to import into a collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Asset Import |
| Type | [FChaosClothAssetImportNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported cloth asset. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportLod | The LOD to import into the collection. Only one LOD can be imported at a time. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClothAsset | The Cloth Asset to import into a collection. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosClothAsset](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetEngine/UChaosClothAsset)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport?application_version=5.7#outputs)
