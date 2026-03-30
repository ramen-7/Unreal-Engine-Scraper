<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation?application_version=5.7 -->

# CollectionSelectionSetOperation

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
7. CollectionSelectionSetOperation

# CollectionSelectionSetOperation

CollectionSelectionSetOperation (v1)

On this page

### Description

CollectionSelectionSetOperation (v1)

Runs boolean operation on selection ( support all selection types )

Input(s) :
SelectionA [Intrinsic] - First Selection object
SelectionB [Intrinsic] - Second Selection object

Output(s):
Selection - Array of the selected bone indices after operation

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection |
| Type | [FCollectionSelectionSetOperationDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionSetOperation-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Operation | Boolean operation | [ESetOperationEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESetOperationEnum) | Dataflow\_SetOperation\_AND |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SelectionA | First Selection object | [FDataflowSelectionTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |
| SelectionB | Second Selection object | [FDataflowSelectionTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Selection | Array of the selected bone indices after operation | [FDataflowSelectionTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation?application_version=5.7#outputs)
