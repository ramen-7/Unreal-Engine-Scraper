<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection?application_version=5.7 -->

# BlueprintToCollection

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
7. BlueprintToCollection

# BlueprintToCollection

BlueprintToCollection (v2)

On this page

### Description

BlueprintToCollection (v2)

Create a geometry collection from an asset

Output(s):
Collection - Geometry collection newly created
Materials - Material instances array from the static mesh
InstancedMeshes - Array of instanced meshes
RootProxyMeshes - corresponding source proxies

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FBlueprintToCollectionDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBlueprintToCollectionDataflowNo-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Blueprint | Asset input | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UBlueprint](/documentation/en-us/unreal-engine/API/Runtime/Engine/UBlueprint)> | None |
| bSplitComponents | Split components | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Geometry collection newly created | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Materials | Material instances array from the static mesh | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| InstancedMeshes | Array of instanced meshes | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionAutoInstanceMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionAutoInstanceM-)> |  |
| RootProxyMeshes | corresponding source proxies | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection?application_version=5.7#parameters)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection?application_version=5.7#outputs)
