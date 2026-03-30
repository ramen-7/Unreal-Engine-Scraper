<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing?application_version=5.7 -->

# ApplyRBFResizing

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
7. ApplyRBFResizing

# ApplyRBFResizing

ApplyRBFResizing (v1)

On this page

### Description

ApplyRBFResizing (v1)
Experimental

Apply the interpolation data calculated by GenerateRBFResizingWeights to resize a mesh.

Input(s) :
MeshToResize - The mesh being resized
TargetSkeletalMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
TargetMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
InterpolationData - The pre-calculated base RBF interpolation data.

Output(s):
ResizedMesh - The resulting resized mesh

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Apply RBF Resizing |
| Type | FApplyRBFResizingNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseSkeletalMeshTarget | Use a skeletal mesh for the target mesh (instead of a dynamic mesh) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bInterpolateNormals | Whether or not to interpolate the normals as well as the positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshToResize | The mesh being resized | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| TargetSkeletalMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| TargetSkeletalMeshLODIndex |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| TargetMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| InterpolationData | The pre-calculated base RBF interpolation data. | [FMeshResizingRBFInterpolationData](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) | (SampleIndices=,SampleRestPositions=,InterpolationWeights=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizedMesh | The resulting resized mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing?application_version=5.7#outputs)
