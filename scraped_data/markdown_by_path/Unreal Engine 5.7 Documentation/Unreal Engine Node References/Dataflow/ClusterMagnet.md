<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet?application_version=5.7 -->

# ClusterMagnet

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
7. ClusterMagnet

# ClusterMagnet

ClusterMagnet (v1)

On this page

### Description

ClusterMagnet (v1)

Cluster by grouping the selected bones with their adjacent, neighboring bones.

Input(s) :
Collection [Intrinsic] - Collection on which to merge bones into a cluster
TransformSelection - Bone selection
Iterations - How many layers of neighbors to include in the clusters -- i.e. if 1, only direct neighbors are clustered; if 2, neighbors of neighbors are included, etc.

Output(s):
Collection [Passthrough] - Collection on which to merge bones into a cluster

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Cluster |
| Type | [FClusterMagnetDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FClusterMagnetDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a cluster | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | Bone selection | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Iterations | How many layers of neighbors to include in the clusters -- i.e. if 1, only direct neighbors are clustered; if 2, neighbors of neighbors are included, etc. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection on which to merge bones into a cluster | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet?application_version=5.7#outputs)
