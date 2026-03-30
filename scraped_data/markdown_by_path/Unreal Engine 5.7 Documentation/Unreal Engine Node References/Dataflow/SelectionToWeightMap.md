<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap?application_version=5.7 -->

# SelectionToWeightMap

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
7. SelectionToWeightMap

# SelectionToWeightMap

SelectionToWeightMap (v1)

On this page

### Description

SelectionToWeightMap (v1)

Convert an integer index selection to a vertex weight map where different map values can be set for selected and unselected vertices.

Input(s) :
SelectionName - The name of the selection to convert.

Output(s):
WeightMapName - The name of the weight map attribute that will be added to the collection.
If left empty the same name as the selection name will be used instead.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection To Weight Map |
| Type | [FChaosClothAssetSelectionToWeightMapNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionToWeigh-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| UnselectedValue | The value unselected vertices receive. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SelectedValue | The value selected vertices receive. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SelectionName | The name of the selection to convert. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| WeightMapName | The name of the weight map attribute that will be added to the collection. If left empty the same name as the selection name will be used instead. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap?application_version=5.7#outputs)
