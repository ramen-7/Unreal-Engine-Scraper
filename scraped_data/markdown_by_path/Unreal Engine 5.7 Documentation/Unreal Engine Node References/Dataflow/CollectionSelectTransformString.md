<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString?application_version=5.7 -->

# CollectionSelectTransformString

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
7. CollectionSelectTransformString

# CollectionSelectTransformString

CollectionSelectTransformString (v1)

On this page

### Description

CollectionSelectTransformString (v1)

Selects transforms by name using a the BoneName attributeor other Transform group string typed attributes

Input(s) :
Collection [Intrinsic] - Collection for the selection
Attribute - Text to serach in the name
SearchText - Text to serach in the name

Output(s):
Collection [Passthrough] - Collection for the selection
TransformSelection - output selection of the matching transforms

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Tags | Name, Bone, Attribute |
| Type | [FCollectionSelectTransformStringDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectTransformString-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method | Method to use to match the name | [EDataflowCollectionSelectionByNameMethod](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowCollectionSelectionByNa-) | Contains |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SearchText | Text to serach in the name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Attribute | Text to serach in the name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | BoneName |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | output selection of the matching transforms | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString?application_version=5.7#outputs)
