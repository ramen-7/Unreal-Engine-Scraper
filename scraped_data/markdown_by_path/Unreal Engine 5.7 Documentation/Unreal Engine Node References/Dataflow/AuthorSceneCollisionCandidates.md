<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates?application_version=5.7 -->

# AuthorSceneCollisionCandidates

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
7. AuthorSceneCollisionCandidates

# AuthorSceneCollisionCandidates

AuthorSceneCollisionCandidates (v1)

On this page

### Description

AuthorSceneCollisionCandidates (v1)

Marks mesh vertices as candidates for scene collision raycasts. Each vertex has an associated
bone index to use as the origin of the raycast. The runtime distance between the vertex and the
bone designates the range of the scene query depth.

Input(s) :
VertexIndices - ! Indices to use with environment collisions. If this input is not connected, then all
! indicies are used.
OriginBoneIndex - ! Bone index to use as the world raycast origin. -1 denotes the component transform.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAuthorSceneCollisionCandidates](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAuthorSceneCollisionCandidates) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSurfaceVerticesOnly | ! Restricts vertices to only ones on the surface. All vertices otherwise. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexIndices | ! Indices to use with environment collisions. If this input is not connected, then all ! indicies are used. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| OriginBoneIndex | ! Bone index to use as the world raycast origin. -1 denotes the component transform. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates?application_version=5.7#outputs)
