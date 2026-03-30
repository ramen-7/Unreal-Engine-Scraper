<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights?application_version=5.7 -->

# BuildSplineSkinWeights

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
7. BuildSplineSkinWeights

# BuildSplineSkinWeights

BuildSplineSkinWeights (v1)

On this page

### Description

BuildSplineSkinWeights (v1)
Experimental

Build spline skinning data from skeletal mesh

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to focus the geometry transfer spatially
SkeletalMesh - SkeletalMesh used to compute spline skinning weights. Will be stored onto the groom asset
LODIndex - LOD used to build skinning weights
RootBones - Root bones to be used for spline skinning. Uses all bones if empty. Note that branches in the skeleton is currently not supported.
SamplesPerSegment - Number of spline samples per bone segment.

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
SplineParamKey - Spline Skinning Parameter key
SplineBonesKey - Spline Bones key containing root and end spline bone. To be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildSplineSkinWeightsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildSplineSkinWeightsDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to focus the geometry transfer spatially | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| SkeletalMesh | SkeletalMesh used to compute spline skinning weights. Will be stored onto the groom asset | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| LODIndex | LOD used to build skinning weights | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| RootBones | Root bones to be used for spline skinning. Uses all bones if empty. Note that branches in the skeleton is currently not supported. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| SamplesPerSegment | Number of spline samples per bone segment. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 64 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SplineParamKey | Spline Skinning Parameter key | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| SplineBonesKey | Spline Bones key containing root and end spline bone. To be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights?application_version=5.7#outputs)
