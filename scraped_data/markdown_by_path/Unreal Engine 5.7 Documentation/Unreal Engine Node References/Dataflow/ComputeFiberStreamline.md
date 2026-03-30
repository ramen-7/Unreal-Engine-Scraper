<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline?application_version=5.7 -->

# ComputeFiberStreamline

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
7. ComputeFiberStreamline

# ComputeFiberStreamline

ComputeFiberStreamline (v1)

On this page

### Description

ComputeFiberStreamline (v1)

Computes fiber streamlines (line segments) flowing from muscle origins to insertions in the muscle fiber field.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeFiberStreamlineNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeFiberStreamlineNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OriginInsertionGroupName |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OriginVertexFieldName |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Origin |
| InsertionVertexFieldName |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Insertion |
| MaxStreamlineIterations |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 500 |
| MaxPointsPerLine |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 20 |
| NumLinesMultiplier |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OriginIndices |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| InsertionIndices |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | typedef FManagedArrayCollection DataType; | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VectorField |  | [FFieldCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FFieldCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline?application_version=5.7#outputs)
