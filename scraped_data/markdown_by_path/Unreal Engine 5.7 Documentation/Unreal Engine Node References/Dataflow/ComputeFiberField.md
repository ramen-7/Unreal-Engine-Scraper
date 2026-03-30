<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField?application_version=5.7 -->

# ComputeFiberField

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
7. ComputeFiberField

# ComputeFiberField

ComputeFiberField (v1)

On this page

### Description

ComputeFiberField (v1)

Computes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra,
vertices, and origin & insertion vertex fields. Fiber directions should smoothly follow the geometry
oriented from the origin vertices pointing to the insertion vertices.

Input(s) :
Collection - typedef FManagedArrayCollection DataType;

Output(s):
Collection [Passthrough] - typedef FManagedArrayCollection DataType;

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FComputeFiberFieldNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FComputeFiberFieldNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OriginInsertionGroupName |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OriginVertexFieldName |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Origin |
| InsertionVertexFieldName |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Insertion |
| MaxIterations |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| Tolerance |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bShowMuscleColor | If muscles are colored by the flow from origins (blue) to insertions (red). This becomes optional in 5.6 | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

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

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField?application_version=5.7#outputs)
