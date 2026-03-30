<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights?application_version=5.7 -->

# CorrectSkinWeights

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
7. CorrectSkinWeights

# CorrectSkinWeights

CorrectSkinWeights (v1)

On this page

### Description

CorrectSkinWeights (v1)
Experimental

Correct skin weights vertex properties.

Input(s) :
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary
SelectionMapKey - Selection map key to be used in other nodes if necessary
SmoothingIterations - Number of iteration required for the smoothing
SmoothingFactor - Lerp value in between the current and the average weight values
bUseSelectionAsPerVertexFactor - When true, use the decimal values of the selection as a per vertex factor for the selected operation - Currently available for Relax operation only - false by default
PruningThreshold - All weights below this threshold will be pruned
ClampingNumber - Max number of bones to consider for the skin weights
SelectionThreshold - Selection threshold to consider a neighbor skin weight

Output(s):
BoneIndicesKey [Passthrough] - Bone indices key to be used in other nodes if necessary
BoneWeightsKey [Passthrough] - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowEditor](/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor) |
| Category | Collection |
| Tags | Correct skin weights and save it to collection |
| Type | [FDataflowCorrectSkinWeightsNode](/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/FDataflowCorrectSkinWeightsNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndicesName | The name to be set for the bone indices. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| BoneWeightsName | The name to be set for the bone weights. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| SelectionMapName | Map name to be used to select vertices to correct | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| CorrectionType | Selection map key to be used in other nodes if necessary | [ESkinWeightsCorrectionType](/documentation/en-us/unreal-engine/API/Plugins/DataflowEditor/ESkinWeightsCorrectionType) | Relax |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SelectionMapKey | Selection map key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SmoothingIterations | Number of iteration required for the smoothing | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| SmoothingFactor | Lerp value in between the current and the average weight values | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| bUseSelectionAsPerVertexFactor | When true, use the decimal values of the selection as a per vertex factor for the selected operation - Currently available for Relax operation only - false by default | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| PruningThreshold | All weights below this threshold will be pruned | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| ClampingNumber | Max number of bones to consider for the skin weights | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| SelectionThreshold | Selection threshold to consider a neighbor skin weight | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights?application_version=5.7#outputs)
