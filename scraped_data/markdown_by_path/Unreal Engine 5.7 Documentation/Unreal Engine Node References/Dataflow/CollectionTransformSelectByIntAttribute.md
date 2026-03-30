<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute?application_version=5.7 -->

# CollectionTransformSelectByIntAttribute

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
7. CollectionTransformSelectByIntAttribute

# CollectionTransformSelectByIntAttribute

CollectionTransformSelectByIntAttribute (v1)

On this page

### Description

CollectionTransformSelectByIntAttribute (v1)

Selects bones by an int attribute

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
TransformSelection - Transform selection including the new indices

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|Transform |
| Type | [FCollectionTransformSelectionByIntAttrDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionTrans-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Group name for the attr | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Transform |
| AttrName | Attribute name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min | Minimum value for the selection | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Max | Maximum value for the selection | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1000 |
| RangeSetting | Values for the selection has to be inside or outside [Min, Max] range | [ERangeSettingEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ERangeSettingEnum) | Dataflow\_RangeSetting\_InsideRange |
| bInclusive | If true then range includes Min and Max values | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Min | Minimum value for the selection | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Max | Maximum value for the selection | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | Transform selection including the new indices | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute?application_version=5.7#outputs)
