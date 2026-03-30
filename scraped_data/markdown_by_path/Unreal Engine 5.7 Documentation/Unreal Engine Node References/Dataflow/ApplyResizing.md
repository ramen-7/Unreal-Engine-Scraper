<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing?application_version=5.7 -->

# ApplyResizing

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
7. ApplyResizing

# ApplyResizing

ApplyResizing (v1)

On this page

### Description

ApplyResizing (v1)
Experimental

Apply resizing for a given Target Mesh.

Input(s) :
TargetSkeletalMesh - The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh
SkeletalMeshLODIndex - Source and Target mesh LOD.
InterpolationData - The pre-calculated base RBF interpolation data.
bForceApplyToRenderMesh - Force apply to the render mesh. Otherwise, the sim mesh will be resized if it exists, only resizing the render mesh if no sim mesh data exists.
SourceSkeletalMesh - The source mesh. Used for CustomResizingRegions. Must have matching vertices with TargetMesh
bSkipCustomRegionResizing - Skip applying Custom Region Resizing data.
bSavePreResizedSimPosition3D - Save pre-resized sim 3d vertices for scaling 2D rest length in XPBD anisotropic stretch constraints.
IMPORTANT: Using Save Pre-Resized Sim Position 3D requires the following settings in SimulationStretchConfig node:
Stretch Use 3d Rest Lengths: false
Solver Type: XPBD
Distribution Type: Anisotropic

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Apply Cloth Outfit Resizing |
| Type | [FChaosClothAssetApplyResizingNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetApplyResizingNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TargetSkeletalMesh | The target mesh that corresponds with the SourceMesh used to generate the InterpolationData. Must have matching vertices with SourceMesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| InterpolationData | The pre-calculated base RBF interpolation data. | [FMeshResizingRBFInterpolationData](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) | (SampleIndices=,SampleRestPositions=,InterpolationWeights=) |
| SkeletalMeshLODIndex | Source and Target mesh LOD. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bForceApplyToRenderMesh | Force apply to the render mesh. Otherwise, the sim mesh will be resized if it exists, only resizing the render mesh if no sim mesh data exists. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SourceSkeletalMesh | The source mesh. Used for CustomResizingRegions. Must have matching vertices with TargetMesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| bSkipCustomRegionResizing | Skip applying Custom Region Resizing data. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bSavePreResizedSimPosition3D | Save pre-resized sim 3d vertices for scaling 2D rest length in XPBD anisotropic stretch constraints. IMPORTANT: Using Save Pre-Resized Sim Position 3D requires the following settings in SimulationStretchConfig node: Stretch Use 3d Rest Lengths: false Solver Type: XPBD Distribution Type: Anisotropic | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing?application_version=5.7#outputs)
