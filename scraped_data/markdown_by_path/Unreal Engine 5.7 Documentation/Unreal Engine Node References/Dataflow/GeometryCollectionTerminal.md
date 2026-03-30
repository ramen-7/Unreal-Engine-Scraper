<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal?application_version=5.7 -->

# GeometryCollectionTerminal

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
7. GeometryCollectionTerminal

# GeometryCollectionTerminal

GeometryCollectionTerminal (v2)

On this page

### Description

GeometryCollectionTerminal (v2)

* Geometry Collection asset terminal node

Input(s) :
Materials - Materials to set on this asset
InstancedMeshes - array of instanced meshes

Output(s):
Materials [Passthrough] - Materials to set on this asset
InstancedMeshes [Passthrough] - array of instanced meshes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Terminal |
| Type | [FGeometryCollectionTerminalDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollectionTerminalDataf-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Materials | Materials to set on this asset | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | array of instanced meshes | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Materials to set on this asset | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | array of instanced meshes | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal?application_version=5.7#outputs)
