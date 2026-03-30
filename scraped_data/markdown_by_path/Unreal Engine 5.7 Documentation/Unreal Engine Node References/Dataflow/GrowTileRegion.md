<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion?application_version=5.7 -->

# GrowTileRegion

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
7. GrowTileRegion

# GrowTileRegion

GrowTileRegion (v1)

On this page

### Description

GrowTileRegion (v1)
Experimental

Finds a square tile within a specified image region and duplicates it over the whole image.
The image region to search is determined by the UV coordinates in ValidRegionMesh -- only texels inside a 2D UV mesh triangle are considered when searching for a tile.
Note this node does not try to detect any repeating patterns, it just grabs the first square tile of the specified size that is entirely inside the UV mesh.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Grow Tile |
| Type | FMeshResizingGrowTileRegionNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshUVLayer |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| TileWidth |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| ValidRegionMesh |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image |  | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| MeshMask |  | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion?application_version=5.7#outputs)
