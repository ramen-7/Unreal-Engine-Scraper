<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals?application_version=5.7 -->

# ReverseNormals

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
7. ReverseNormals

# ReverseNormals

ReverseNormals (v1)

On this page

### Description

ReverseNormals (v1)

Reverse the geometry's normals or/and winding order of the simulation or/and render meshes stored in the cloth collection.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Reverse Simulation Render Mesh Normals |
| Type | [FChaosClothAssetReverseNormalsNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetReverseNormalsNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimPatterns | List of sim patterns to apply the operation on. All patterns will be used if left empty. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bReverseSimMeshNormals | Whether to reverse the simulation mesh normals. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverseSimMeshWindingOrder | Whether to reverse the simulation mesh triangles' winding order. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderPatterns | List of render patterns to apply the operation on. All patterns will be used if left empty. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bReverseRenderMeshNormals | Whether to reverse the render mesh normals. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bReverseRenderMeshWindingOrder | Whether to reverse the render mesh triangles' winding order. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals?application_version=5.7#outputs)
