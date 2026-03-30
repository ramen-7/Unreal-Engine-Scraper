<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors?application_version=5.7 -->

# ClusterMergeToNeighbors

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
7. ClusterMergeToNeighbors

# ClusterMergeToNeighbors

ClusterMergeToNeighbors (v1)

On this page

### Description

ClusterMergeToNeighbors (v1)

Merge selected bones to their neighbors

Input(s) :
Collection [Intrinsic] - Collection on which to merge bones into a neighboring cluster
TransformSelection - Bone selection
MinVolumeCubeRoot - Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value
bOnlyToConnected - Whether to only allow clusters to merge if their bones are connected in the proximity graph
bOnlySameParent - Whether to only allow clusters to merge if they have the same parent bone

Output(s):
Collection [Passthrough] - Collection on which to merge bones into a neighboring cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterMergeToNeighborsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterMergeToNeighborsDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NeighborSelectionMethod | Method to choose which neighbor to merge | [EClusterNeighborSelectionMethodEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EClusterNeighborSelectionMethodE-) | Dataflow\_ClusterNeighborSelectionMethod\_LargestNeighbor |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a neighboring cluster | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| MinVolumeCubeRoot | Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bOnlyToConnected | Whether to only allow clusters to merge if their bones are connected in the proximity graph | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlySameParent | Whether to only allow clusters to merge if they have the same parent bone | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a neighboring cluster | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors?application_version=5.7#outputs)
