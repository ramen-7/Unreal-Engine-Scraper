<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray?application_version=5.7 -->

# FloatArrayToIntArray

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
7. FloatArrayToIntArray

# FloatArrayToIntArray

FloatArrayToIntArray (v1)

On this page

### Description

FloatArrayToIntArray (v1)

Converts a Float array to Int array using the specified method.

Input(s) :
FloatArray - Float array value to convert

Output(s):
IntArray - Int array output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Conversions |
| Type | [FFloatArrayToIntArrayDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayToIntArrayDataflowNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Function | Conversion method: Floor takes the floor of each input float value - 1.1 turns into 1. Ceil takes the ceil - 1.1 turns into 2. Round rounds to the nearest integer - 1.1 turns into 1. Tuncate trucates like a type cast - 1.1 turns into 1. Non-zero to Index appends the index of all non-zero values to the output array. Zero to Index appends the index of all zero values to the output array. | [EFloatArrayToIntArrayFunctionEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EFloatArrayToIntArrayFunctionEnu-) | Dataflow\_FloatToInt\_NonZeroToIndex |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Float array value to convert | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| IntArray | Int array output | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray?application_version=5.7#outputs)
