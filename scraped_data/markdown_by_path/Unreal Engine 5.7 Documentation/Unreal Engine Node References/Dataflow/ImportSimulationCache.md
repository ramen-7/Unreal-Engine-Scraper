<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache?application_version=5.7 -->

# ImportSimulationCache

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
7. ImportSimulationCache

# ImportSimulationCache

ImportSimulationCache (v1)

On this page

### Description

ImportSimulationCache (v1)
Experimental

Set vertex values from a simulation cache. The topology of the Collection will remain the same.

Input(s) :
Collection - Input/output collection
ImportedCache - Cache to import in.

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Import Cache |
| Type | [FChaosClothAssetImportSimulationCacheNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_4) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CacheIndex | Cache index to read | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| CacheTime | Cache time to read | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Transform | Transform cache data. | [FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| ParticleOffset | Particle cache offset. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bUpdateSimulationMesh | Update simulation mesh from cache. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bRecalculateNormals | Recalculate simulation normals based on imported positions. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUpdateRenderMesh | Update render mesh from cache via proxy deformer data. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| ImportedCache | Cache to import in. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosCacheCollection](/documentation/en-us/unreal-engine/API/Plugins/ChaosCaching/UChaosCacheCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache?application_version=5.7#outputs)
