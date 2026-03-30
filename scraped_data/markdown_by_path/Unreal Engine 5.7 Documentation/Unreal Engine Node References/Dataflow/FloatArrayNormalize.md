<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize?application_version=5.7 -->

# FloatArrayNormalize

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
7. FloatArrayNormalize

# FloatArrayNormalize

FloatArrayNormalize (v1)

On this page

### Description

FloatArrayNormalize (v1)

Normalize the selected float data in a FloatArray

Input(s) :
InFloatArray [Intrinsic] - Input VectorArray
Selection - Selection for the operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Float |
| Type | [FFloatArrayNormalizeDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFloatArrayNormalizeDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InFloatArray | Input VectorArray | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| Selection | Selection for the operation | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| MinRange |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRange |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutFloatArray |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize?application_version=5.7#outputs)
