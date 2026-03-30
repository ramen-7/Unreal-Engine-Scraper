<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap?application_version=5.7 -->

# MeshWrap

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
7. MeshWrap

# MeshWrap

MeshWrap (v1)

On this page

### Description

MeshWrap (v1)
Experimental

Dataflow node for wrapping one mesh's topology to another mesh's shape. Uses point landmarks defined by the Mesh Wrap Landmarks node to match corresponding points between the two meshes.

Input(s) :
SourceTopologyMesh - Input mesh with the desired wrapped mesh topology.
TargetShapeMesh - Input mesh with the desired wrapped mesh shape.
SourceTopologyLandmarks - Landmarks defined on SourceTopologyMesh. TargetShapeLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap.
TargetShapeLandmarks - Landmarks defined on TargetShapeMesh. SourceTopologyLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap.

Output(s):
WrappedMesh - Output wrapped mesh.
MatchedLandmarks - Landmarks matched by Identifier from SourceTopologyLandmarks and TargetShapeLandmarks.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Wrap |
| Type | [FMeshWrapNode](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MaxNumOuterIterations | Mesh Wrap is calculated with an inner and outer loop. This is the maximum number of outer loops. Each outer loop increases the Projection Stiffness by ProjectionStiffnessMultiplier. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| NumInnerIterations | Mesh Wrap is calculated with an inner and outer loop. This is the number of inner loops run before increasing the Projection Stiffness in the outer loop. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| ProjectionTolerance | Mesh Wrap will terminate early if the Projection tolerance is within this threshold. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000100 |
| LaplacianStiffness | Weight of mesh wrap to retain Source Topology mesh features. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| InitialProjectionStiffness | Initial weight of mesh wrap to match projected Target Shape. Each outer loop will multiply this stiffness by ProjectionStiffnessMultiplier. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| ProjectionStiffnessMuliplier | Each outer loop will multiply InitialProjectionStiffness by this to improve Target Shape match. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CorrespondenceStiffness | Weight of mesh wrap to match Landmark correspondences. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DefaultDisplayMaterial | Display material for Source or Target when none is supplied. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterial](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterial)> | None |
| bDisplayLandmarks | Display landmarks. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bDisplaySource | Draw source mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SourceDisplayOffset | Offset of source mesh display for side-by-side drawing. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -150.000000 |
| bDisplayTarget | Draw target mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TargetDisplayOffset | Offset of target mesh display for side-by-side drawing. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceTopologyMesh | Input mesh with the desired wrapped mesh topology. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetShapeMesh | Input mesh with the desired wrapped mesh shape. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| SourceTopologyLandmarks | Landmarks defined on SourceTopologyMesh. TargetShapeLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |
| TargetShapeLandmarks | Landmarks defined on TargetShapeMesh. SourceTopologyLandmarks with matching Identifiers will be used to find correspondences that help improve the wrap. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapLandmark](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapLandmark)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| WrappedMesh | Output wrapped mesh. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| MatchedLandmarks | Landmarks matched by Identifier from SourceTopologyLandmarks and TargetShapeLandmarks. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FMeshWrapCorrespondence](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes/FMeshWrapCorrespondence)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap?application_version=5.7#outputs)
