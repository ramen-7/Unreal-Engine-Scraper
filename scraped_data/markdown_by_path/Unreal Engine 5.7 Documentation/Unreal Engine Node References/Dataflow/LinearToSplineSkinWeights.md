<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights?application_version=5.7 -->

# LinearToSplineSkinWeights

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
7. LinearToSplineSkinWeights

# LinearToSplineSkinWeights

LinearToSplineSkinWeights (v1)

On this page

### Description

LinearToSplineSkinWeights (v1)
Experimental

Convert linear skinning data to spline skinning data

Input(s) :
Collection - Managed array collection to be used to store datas
VertexSelection - Vertex selection to process vertices subset

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas
SplineParamKey - Spline skinning parameter key
SplineBonesKey - Spline bones key. Used for storing root and end spline bone for each vertex.

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FLinearToSplineSkinWeightsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FLinearToSplineSkinWeightsDatafl-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | Vertex selection to process vertices subset | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SplineParamKey | Spline skinning parameter key | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| SplineBonesKey | Spline bones key. Used for storing root and end spline bone for each vertex. | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights?application_version=5.7#outputs)
