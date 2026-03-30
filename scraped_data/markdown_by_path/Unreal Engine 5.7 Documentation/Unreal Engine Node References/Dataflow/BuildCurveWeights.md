<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights?application_version=5.7 -->

# BuildCurveWeights

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
7. BuildCurveWeights

# BuildCurveWeights

BuildCurveWeights (v1)

On this page

### Description

BuildCurveWeights (v1)
Experimental

Build a weight map that will be identical on every curves

Input(s) :
Collection - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the geometry transfer spatially
WeightsAttribute - Vertex kinematic weights key to be used in other nodes if necessary

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildCurveWeightsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildCurveWeightsDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CurveWeights | This curve determines the weight value from root to tip. The X axis range is [0,1], 0 mapping the root and 1 the tip | [FRuntimeFloatCurve](/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=,DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry transfer spatially | [FDataflowCurveSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| WeightsAttribute | Vertex kinematic weights key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights?application_version=5.7#outputs)
