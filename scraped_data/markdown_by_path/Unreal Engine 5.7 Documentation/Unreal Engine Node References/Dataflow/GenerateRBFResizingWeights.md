<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights?application_version=5.7 -->

# GenerateRBFResizingWeights

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
7. GenerateRBFResizingWeights

# GenerateRBFResizingWeights

GenerateRBFResizingWeights (v1)

On this page

### Description

GenerateRBFResizingWeights (v1)
Experimental

Sample points and generate RBF Interpolation data for a given Source mesh.

Input(s) :
MeshToResize - The mesh to resize. This is currently unused but may be used to improve point sampling in the future.
SourceMesh - The source mesh to be sampled.
NumInterpolationPoints - The number of interpolation points to be sampled.

Output(s):
InterpolationData - The calculated interpolation points and RBF weights

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Generate RBF Resizing Weights |
| Type | FGenerateRBFResizingWeightsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMesh | The source mesh to be sampled. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| NumInterpolationPoints | The number of interpolation points to be sampled. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1500 |
| MeshToResize | The mesh to resize. This is currently unused but may be used to improve point sampling in the future. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InterpolationData | The calculated interpolation points and RBF weights | [FMeshResizingRBFInterpolationData](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights?application_version=5.7#outputs)
