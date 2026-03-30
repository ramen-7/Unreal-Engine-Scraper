<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes?application_version=5.7 -->

# ConvertSelectionTypes

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
7. ConvertSelectionTypes

# ConvertSelectionTypes

ConvertSelectionTypes (v1)

On this page

### Description

ConvertSelectionTypes (v1)

Convert Selection types

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
In [Intrinsic] - Input value

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
Out - Output value

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Convert |
| Type | [FConvertSelectionTypesDataflowNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FConvertSelectionTypesDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAllElementsMustBeSelected | If true then for converting vertex/face selection to transform/geometry selection all vertex/face must be selected for selecting the associated transform/geometry or going from vertex to face selection all vertices must be selected to select the face | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| In | Input value | [FDataflowSelectionTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) | (Value=()) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Out | Output value | [FDataflowSelectionTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowSelectionTypes) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes?application_version=5.7#outputs)
