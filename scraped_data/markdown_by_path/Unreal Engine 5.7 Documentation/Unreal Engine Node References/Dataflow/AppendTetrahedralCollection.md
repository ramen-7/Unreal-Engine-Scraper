<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection?application_version=5.7 -->

# AppendTetrahedralCollection

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
7. AppendTetrahedralCollection

# AppendTetrahedralCollection

AppendTetrahedralCollection (v2)

On this page

### Description

AppendTetrahedralCollection (v2)

Append another Tetrahedral Collection to this collection. All attributes will be appended to the end.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FAppendTetrahedralCollectionDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FAppendTetrahedralCollectionData-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeTransform | If checked, non-geometry transforms from CollectionToAppend are merged into Collection by matching transform names. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CollectionToAppend |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| CollectionGeometrySelection |  | [FDataflowGeometrySelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| CollectionToAppendGeometrySelection |  | [FDataflowGeometrySelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| CollectionGeometryGroupGuids |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| CollectionToAppendGeometryGroupGuids |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection?application_version=5.7#outputs)
