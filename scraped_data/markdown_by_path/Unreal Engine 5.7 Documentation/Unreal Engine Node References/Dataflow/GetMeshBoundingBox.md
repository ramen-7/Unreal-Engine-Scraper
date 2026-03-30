<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox?application_version=5.7 -->

# GetMeshBoundingBox

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
7. GetMeshBoundingBox

# GetMeshBoundingBox

GetMeshBoundingBox (v1)

On this page

### Description

GetMeshBoundingBox (v1)

Get the local geometric bounding box a dynamic mesh

Input(s) :
Mesh - dynamic mesh to compute the bouning box from

Output(s):
BoundingBox - Geometric bounding box of the input dynamic mesh
Center - Center of the resulting bounding box
Dimensions - Dimensions of the resulting bounding box in centimers

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh |
| Tags | Bounds Size Dimensions Extents Center |
| Type | [FGetMeshBoundingBoxDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetMeshBoundingBoxDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | dynamic mesh to compute the bouning box from | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | Geometric bounding box of the input dynamic mesh | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Center | Center of the resulting bounding box | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Dimensions | Dimensions of the resulting bounding box in centimers | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox?application_version=5.7#outputs)
