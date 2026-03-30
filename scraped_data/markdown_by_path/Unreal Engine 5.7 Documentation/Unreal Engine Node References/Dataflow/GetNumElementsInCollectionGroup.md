<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup?application_version=5.7 -->

# GetNumElementsInCollectionGroup

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
7. GetNumElementsInCollectionGroup

# GetNumElementsInCollectionGroup

GetNumElementsInCollectionGroup (v1)

On this page

### Description

GetNumElementsInCollectionGroup (v1)

Returns number of elements in a group in a Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute

Output(s):
NumElements - Number of elements for the attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetNumElementsInCollectionGroupDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetNumElementsInCollectionGroup-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Standard group names | [EStandardGroupNameEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStandardGroupNameEnum) | Dataflow\_EStandardGroupNameEnum\_Transform |
| CustomGroupName | User specified group name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumElements | Number of elements for the attribute | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup?application_version=5.7#outputs)
