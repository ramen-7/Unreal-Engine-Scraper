<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport?application_version=5.7 -->

# StaticMeshImport

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
7. StaticMeshImport

# StaticMeshImport

StaticMeshImport (v2)

On this page

### Description

StaticMeshImport (v2)

Import a static mesh asset into the cloth collection simulation and/or render mesh containers.

Input(s) :
StaticMesh - The Static Mesh to import from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Static Mesh Import |
| Type | [FChaosClothAssetStaticMeshImportNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetStaticMeshImport-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported static mesh asset. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| LODIndex | Which static mesh Lod to import. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSimMesh | Import static mesh data as a simulation mesh data. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SimMeshSection | Material section to import as sim mesh data. Use -1 to import all sections. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| UVChannel | UV channel of the static mesh to import the 2D simulation mesh patterns from. If set to -1, or the specified UVChannel doesn't exist then the import will unwrap the 3D simulation mesh into 2D simulation mesh patterns. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| UVScale | Apply this scale to the UVs when populating Sim Mesh positions. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| bImportRenderMesh | Import static mesh data as render mesh data. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| RenderMeshSection | Material section to import as render mesh data. Use -1 to import all sections. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StaticMesh | The Static Mesh to import from. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport?application_version=5.7#outputs)
