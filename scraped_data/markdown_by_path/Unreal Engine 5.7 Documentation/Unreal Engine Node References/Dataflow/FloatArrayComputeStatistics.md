<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics?application_version=5.7 -->

# FloatArrayComputeStatistics

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
7. FloatArrayComputeStatistics

# FloatArrayComputeStatistics

FloatArrayComputeStatistics (v1)

On this page

### Description

FloatArrayComputeStatistics (v1)

Computes statistics of a float array

Input(s) :
FloatArray [Intrinsic] - Array to compute values from
TransformSelection - TransformSelection describes which values to use, if not connected all the elements will be used

Output(s):
Value - Computed value
Indices - Indices of elements with the computed value

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Type | [FFloatArrayComputeStatisticsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayComputeStatisticsData-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OperationName | Statistics Operation | [EStatisticsOperationEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStatisticsOperationEnum) | Dataflow\_EStatisticsOperationEnum\_Min |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Array to compute values from | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| TransformSelection | TransformSelection describes which values to use, if not connected all the elements will be used | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | Computed value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Indices | Indices of elements with the computed value | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics?application_version=5.7#outputs)
