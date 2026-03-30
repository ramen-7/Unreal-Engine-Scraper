<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget?application_version=5.7 -->

# GenerateSimMorphTarget

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
7. GenerateSimMorphTarget

# GenerateSimMorphTarget

GenerateSimMorphTarget (v1)

On this page

### Description

GenerateSimMorphTarget (v1)

Generate a Sim Morph target from a cloth collection sim mesh (with matching topology).

Input(s) :
Collection - Input/output collection
MorphTargetCollection - Collection to generate the morph target from.

Output(s):
Collection [Passthrough] - Input/output collection
MorphTargetName - Morph target name

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Generate Sim Morph Target |
| Type | [FChaosClothAssetGenerateSimMorphTargetNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_3) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bGenerateNormalDeltas | Whether or not to generate normal deltas | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| MorphTargetCollection | Collection to generate the morph target from. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| MorphTargetName | Morph target name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget?application_version=5.7#outputs)
