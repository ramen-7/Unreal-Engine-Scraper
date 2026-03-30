<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection?application_version=5.7 -->

# AssignMaterialToCollection

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
7. AssignMaterialToCollection

# AssignMaterialToCollection

AssignMaterialToCollection (v1)

On this page

### Description

AssignMaterialToCollection (v1)

Assign material to a set of face in a geometry collection

Input(s) :
Collection [Intrinsic] - Collection to assign material to
FaceSelection - Faces that will be set with this material index, if no selection is connected , all faces will be set
MaterialArray [Intrinsic] - Array holding the materials objects
Material - Material to assign to the selection

Output(s):
Collection [Passthrough] - Collection to assign material to
MaterialArray [Passthrough] - Array holding the materials objects
MaterialIndex - Index where the material was set in the array

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Materials |
| Type | [FAssignMaterialInterfaceToCollectionDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAssignMaterialI-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeDuplicateMaterials | If true, detect duplicate in the material array and only add the material in the array if it does not yet exists | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to assign material to | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces that will be set with this material index, if no selection is connected , all faces will be set | [FDataflowFaceSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| MaterialArray | Array holding the materials objects | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| Material | Material to assign to the selection | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to assign material to | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| MaterialArray | Array holding the materials objects | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| MaterialIndex | Index where the material was set in the array | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection?application_version=5.7#outputs)
