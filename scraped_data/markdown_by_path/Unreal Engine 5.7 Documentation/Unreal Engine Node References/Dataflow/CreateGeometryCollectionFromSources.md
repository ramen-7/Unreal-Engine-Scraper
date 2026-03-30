<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources?application_version=5.7 -->

# CreateGeometryCollectionFromSources

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
7. CreateGeometryCollectionFromSources

# CreateGeometryCollectionFromSources

CreateGeometryCollectionFromSources (v2)

On this page

### Description

CreateGeometryCollectionFromSources (v2)

create a geometry collection from a set of geometry sources
if the source array is not connected, the source array from the current asset is going to be used

Input(s) :
Sources - array of geometry sources

Output(s):
Collection - Geometry collection newly created
Materials - Materials array to use for this asset
InstancedMeshes - array of instanced meshes
RootProxyMeshes - corresponding source proxies

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FCreateGeometryCollectionFromSourcesDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateGeometryC-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sources | array of geometry sources | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionSource](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionSource)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Geometry collection newly created | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Materials array to use for this asset | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | array of instanced meshes | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes | corresponding source proxies | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources?application_version=5.7#outputs)
