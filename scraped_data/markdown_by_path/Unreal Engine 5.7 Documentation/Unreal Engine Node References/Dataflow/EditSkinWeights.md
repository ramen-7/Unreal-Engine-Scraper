<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights?application_version=5.7 -->

# EditSkinWeights

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
7. EditSkinWeights

# EditSkinWeights

EditSkinWeights (v1)

On this page

### Description

EditSkinWeights (v1)
Experimental

Edit skin weights vertex properties.

Input(s) :
BoneIndicesKey - Bone indices key to be used in other nodes if necessary
BoneWeightsKey - Bone weights key to be used in other nodes if necessary
SkeletalMesh - Skeletal mesh to extract the skeleton from for the skinning

Output(s):
BoneIndicesKey [Passthrough] - Bone indices key to be used in other nodes if necessary
BoneWeightsKey [Passthrough] - Bone weights key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Edit skin weights and save it to collection |
| Type | [FDataflowCollectionEditSkinWeightsNode](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionEditSkinWeigh-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneIndicesName | The name to be set as a weight map attribute. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| BoneWeightsName | The name to be set as a weight map attribute. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |
| bCompressSkinWeights | Boolean to use a compressed format (FVector4f, FIntVector) to store the skin weights | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoneIndicesKey | Bone indices key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoneWeightsKey | Bone weights key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| SkeletalMesh | Skeletal mesh to extract the skeleton from for the skinning | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights?application_version=5.7#outputs)
