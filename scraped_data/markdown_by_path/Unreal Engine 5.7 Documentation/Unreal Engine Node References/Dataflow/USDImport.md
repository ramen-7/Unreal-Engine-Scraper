<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport?application_version=5.7 -->

# USDImport

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
7. USDImport

# USDImport

USDImport (v2) Import a USD file from a third party garment construction software.

On this page

### Description

USDImport (v2)

Import a USD file from a third party garment construction software.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth USD Import |
| Type | [FChaosClothAssetUSDImportNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetUSDImportNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bImportSimMesh | Only import the simulation mesh data from the USD file. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportRenderMesh | Only import the render mesh data from the USD file. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportWithOpacity | Importing the render mesh with opacity requires transluscency to be enable in the project settings. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UsdFile | Path of the USD file to import. | [FChaosClothAssetImportFilePath](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportFilePath) | (FilePath="",bForceReimport=False) |
| ReimportUsdFile | Click on this button to reimport the specified USD file and regenerate the intermediary assets. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ReloadSimStaticMesh | The USD import process generates an intermediary simulation static mesh. Click on this button to reimport it without reimporting the USD file. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ReloadRenderStaticMesh | The USD import process generates an intermediary render static mesh. Click on this button to reimport it without reimporting the USD file. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| PackagePath | Content folder where all the USD assets are imported. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| ImportedSimStaticMesh | The static mesh created from the USD import process used as simulation mesh. Note that this property can still be empty after successfully importing a simulation mesh depending on whether the simulation mesh is imported from an older version of USD cloth schema. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| ImportedUVScale | The UV scale used to import the patterns from the imported static mesh UV coordinates. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| ImportedRenderStaticMesh | The static mesh created from the USD import process used as render mesh. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| ImportedSimAssets | List of all the simulation static mesh's dependent assets. This does not include any Engine, or Engine plugin content. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| ImportedRenderAssets | List of all the render static mesh's dependent assets. This does not include any Engine, or Engine plugin content. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport?application_version=5.7#parameters)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport?application_version=5.7#outputs)
