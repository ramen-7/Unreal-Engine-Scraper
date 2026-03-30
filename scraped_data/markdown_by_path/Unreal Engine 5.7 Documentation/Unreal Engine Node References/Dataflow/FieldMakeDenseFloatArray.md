<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray?application_version=5.7 -->

# FieldMakeDenseFloatArray

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
7. FieldMakeDenseFloatArray

# FieldMakeDenseFloatArray

FieldMakeDenseFloatArray (v1)

On this page

### Description

FieldMakeDenseFloatArray (v1)

Converts a sparse FloatArray (a selected subset of the whole incoming array) into a dense FloatArray
(same number of elements as the incoming array using NumSamplePositions) using the Remap input
NumSamplePositions controls the size of the output array, only indices smaller than l to than NumSamplePositions
will be processed

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Fields |
| Type | [FFieldMakeDenseFloatArrayDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFieldMakeDenseFloatArrayDataflo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Default |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatInput |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| FieldRemap |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| NumSamplePositions |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FieldFloatResult |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray?application_version=5.7#outputs)
