<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray?application_version=5.7 -->

# MakeManagedArrayCollectionArray

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
7. MakeManagedArrayCollectionArray

# MakeManagedArrayCollectionArray

MakeManagedArrayCollectionArray (v1)

On this page

### Description

MakeManagedArrayCollectionArray (v1)

Append an element to an array of ManagedArrayCollections.

Input(s) :
Array [Intrinsic] - Array to append to. If no input connection, a new array will be created
Element - The element to append.

Output(s):
Array [Passthrough] - Array to append to. If no input connection, a new array will be created

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Array |
| Tags | Make Managed Array Collection |
| Type | [FDataflowMakeManagedArrayCollectionArrayNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowMakeManagedArrayCollect-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to append to. If no input connection, a new array will be created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
| Element | The element to append. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | Array to append to. If no input connection, a new array will be created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray?application_version=5.7#outputs)
