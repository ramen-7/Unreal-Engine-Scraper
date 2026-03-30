<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh?application_version=5.7 -->

# FilterPointsWithMesh

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
7. FilterPointsWithMesh

# FilterPointsWithMesh

FilterPointsWithMesh (v1)

On this page

### Description

FilterPointsWithMesh (v1)

Filter a point set to only the points inside or outside of a given mesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to use to filter point set
bKeepInside - Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number.
WindingThreshold - The winding number threshold to use for determining whether a point is inside or outside of the mesh, if corresponding Filter Method is set
MinDistance - The min distance to surface to keep, if corresponding Filter Method is set
MaxDistance - The max distance to surface to keep, if corresponding Filter Method is set
bUseSignedDistance - Whether to use signed distances for the Min and Max Distance thresholds. Otherwise, unsigned distance is used.
Note: Signs are computed via the Winding Number. The sign is negative if the point's Winding Number is below the Winding Threshold.
SamplePoints - Points to filter

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | FFilterPointSetWithMeshDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FilterMethod |  | [uint8](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to use to filter point set | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplePoints | Points to filter | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| bKeepInside | Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| WindingThreshold | The winding number threshold to use for determining whether a point is inside or outside of the mesh, if corresponding Filter Method is set | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| MinDistance | The min distance to surface to keep, if corresponding Filter Method is set | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxDistance | The max distance to surface to keep, if corresponding Filter Method is set | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000.000000 |
| bUseSignedDistance | Whether to use signed distances for the Min and Max Distance thresholds. Otherwise, unsigned distance is used. Note: Signs are computed via the Winding Number. The sign is negative if the point's Winding Number is below the Winding Threshold. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Points to filter | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh?application_version=5.7#outputs)
