<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints?application_version=5.7 -->

# ClusterScatterPoints

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
7. ClusterScatterPoints

# ClusterScatterPoints

ClusterScatterPoints (v1)

On this page

### Description

ClusterScatterPoints (v1)

Cluster Scatter Points Dataflow Node

Input(s) :
NumberClustersMin - Minimum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max
NumberClustersMax - Maximum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max
PointsPerClusterMin - Minimum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max
PointsPerClusterMax - Maximum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max
ClusterRadiusFractionMin - Minimum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this.
Each point will be placed at least this far (plus the Cluster Radius Offset) from its cluster center.
ClusterRadiusFractionMax - Maximum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this.
Each point will be placed at most this far (plus the Cluster Radius Offset) from its cluster center.
ClusterRadiusOffset - Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance
RandomSeed - Seed for random
BoundingBox - BoundingBox to generate points inside of

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FClusterScatterPointsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterScatterPointsDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| NumberClustersMin | Minimum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| NumberClustersMax | Maximum number of clusters of points to create. The amount of clusters created will be chosen at random between Min and Max | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| PointsPerClusterMin | Minimum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| PointsPerClusterMax | Maximum number of points per cluster. The amount of points in each cluster will be chosen at random between Min and Max | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 30 |
| ClusterRadiusFractionMin | Minimum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this. Each point will be placed at least this far (plus the Cluster Radius Offset) from its cluster center. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ClusterRadiusFractionMax | Maximum cluster radius (as fraction of the overall bounding box size). Cluster Radius Offset will be added to this. Each point will be placed at most this far (plus the Cluster Radius Offset) from its cluster center. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |
| ClusterRadiusOffset | Cluster radius offset (in cm). This offset will be added to the 'Min/Max Dist from Center' distance | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RandomSeed | Seed for random | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints?application_version=5.7#outputs)
