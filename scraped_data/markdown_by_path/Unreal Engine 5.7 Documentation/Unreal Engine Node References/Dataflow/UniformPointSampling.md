<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling?application_version=5.7 -->

# UniformPointSampling

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
7. UniformPointSampling

# UniformPointSampling

UniformPointSampling (v1)

On this page

### Description

UniformPointSampling (v1)

Uniform Sampling on a DynamicMesh

Input(s) :
TargetMesh [Intrinsic] - Mesh to sample points on
SamplingRadius - Desired "radius" of sample points. Spacing between samples is at least 2x this value.
MaxNumSamples - Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled
SubSampleDensity - Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results.
RandomSeed - Random Seed used to initialize sampling strategies

Output(s):
SamplePoints - Sampled positions on the mesh
SampleTriangleIDs - Sampled triangleID
SampleBarycentricCoords - Barycentric Coordinates of each Sample Point in it's respective Triangle.
NumSamplePoints - Number of Sampled positions on the mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | PointSampling |
| Type | [FUniformPointSamplingDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FUniformPointSamplingDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMesh | Mesh to sample points on | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SamplingRadius | Desired "radius" of sample points. Spacing between samples is at least 2x this value. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| MaxNumSamples | Maximum number of samples requested. If 0 or default value, mesh will be maximally sampled | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SubSampleDensity | Density of subsampling used in Poisson strategy. Larger numbers mean "more accurate" (but slower) results. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| RandomSeed | Random Seed used to initialize sampling strategies | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SamplePoints | Sampled positions on the mesh | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleTriangleIDs | Sampled triangleID | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| SampleBarycentricCoords | Barycentric Coordinates of each Sample Point in it's respective Triangle. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePoints | Number of Sampled positions on the mesh | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling?application_version=5.7#outputs)
