<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster?application_version=5.7 -->

# AutoCluster

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
7. AutoCluster

# AutoCluster

AutoCluster (v1)

On this page

### Description

AutoCluster (v1)

Automatically group pieces of a fractured Collection into a specified number of clusters

Input(s) :
ClusterSites - Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries
ClusterFraction - Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process
SiteSize - Choose the Edge-Size of the cube used to groups bones under a cluster (in cm).
ClusterGridWidth - Choose the number of cluster sites to distribute along the X axis
ClusterGridDepth - Choose the number of cluster sites to distribute along the Y axis
ClusterGridHeight - Choose the number of cluster sites to distribute along the Z axis
MinimumSize - If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster.
Collection [Intrinsic] - Fractured GeometryCollection to cluster
TransformSelection [Intrinsic] - Bone selection for the clustering

Output(s):
Collection [Passthrough] - Fractured GeometryCollection to cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FAutoClusterDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAutoClusterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ClusterSizeMethod | How to choose the size of the clusters to create | [EClusterSizeMethodEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EClusterSizeMethodEnum) | Dataflow\_ClusterSizeMethod\_ByNumber |
| DriftIterations | For a grid distribution, optionally iteratively recenter the grid points to the center of the cluster geometry (technically: applying K-Means iterations) to balance the shape and distribution of the clusters | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bPreferConvexity | Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConcavityTolerance | If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AutoCluster | If true, bones will only be added to the same cluster if they are physically connected (either directly, or via other bones in the same cluster) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| EnforceSiteParameters | If true, make sure the site parameters are matched as close as possible ( bEnforceConnectivity can make the number of site larger than the requested input may produce without it ) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AvoidIsolated | If true, prevent the creation of clusters with only a single child. Either by merging into a neighboring cluster, or not creating the cluster. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color |  | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |
| LineWidthMultiplier |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| CenterColor |  | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| CenterSize |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12.000000 |
| bRandomizeColor | Randomize color per connection | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ColorRandomSeed | Random seed | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to cluster | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection for the clustering | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| ClusterSites | Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| ClusterFraction | Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.250000 |
| SiteSize | Choose the Edge-Size of the cube used to groups bones under a cluster (in cm). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ClusterGridWidth | Choose the number of cluster sites to distribute along the X axis | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ClusterGridDepth | Choose the number of cluster sites to distribute along the Y axis | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ClusterGridHeight | Choose the number of cluster sites to distribute along the Z axis | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| MinimumSize | If a cluster has volume less than this value (in cm) cubed, then the auto-cluster process will attempt to merge it into a neighboring cluster. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bPreferConvexity | Whether to favor clusters that have a convex shape. (Note: Does not support ByGrid clustering.) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ConcavityTolerance | If > 0, cube root of maximum concave volume to add per cluster (ignoring concavity of individual parts) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Fractured GeometryCollection to cluster | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster?application_version=5.7#outputs)
