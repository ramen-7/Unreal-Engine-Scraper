<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh?application_version=5.7 -->

# UpdateClothFromDynamicMesh

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
7. UpdateClothFromDynamicMesh

# UpdateClothFromDynamicMesh

UpdateClothFromDynamicMesh (v1)

On this page

### Description

UpdateClothFromDynamicMesh (v1)
Experimental

Update cloth collection attributes from a DynamicMesh

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Update Cloth Collection Dynamic Mesh Cloth |
| Type | [FChaosClothAssetUpdateClothFromDynamicMeshNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_43) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCopyToRenderPositions | Copy DynamicMesh Vertex Positions to Render Positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToRendeNormalsAndTangents | Copy DynamicMesh Vertex Normals and Tangents to Render Normals and Tangents | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyUVsToRenderUVs | Copy DynamicMesh UVs to Render UVs | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToRenderMaterials | Copy input materials to Render Materials (order and number must match otherwise only the minimum common number of materials are updated) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToSim3DPositions | Copy DynamicMesh Vertex Positions to Sim3D Positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyToSimNormals | Copy DynamicMesh Vertex Normals to Sim Normals | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCopyUVsToSim2DPositions | Copy DynamicMesh UVs to Sim2D Positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UVChannelIndex | Which UV Channel to use at Sim2D Positions or Render UVs. Use -1 to copy all Render UVs. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DynamicMesh |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| Materials |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh?application_version=5.7#outputs)
