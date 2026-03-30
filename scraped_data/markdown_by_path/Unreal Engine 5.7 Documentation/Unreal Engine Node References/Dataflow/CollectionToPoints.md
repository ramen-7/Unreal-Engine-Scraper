<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints?application_version=5.7 -->

# CollectionToPoints

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
7. CollectionToPoints

# CollectionToPoints

CollectionToPoints (v1)

On this page

### Description

CollectionToPoints (v1)

Get vertices from a collection as a point cloud

Input(s) :
Collection [Intrinsic] - Collection storing the points

Output(s):
Collection [Passthrough] - Collection storing the points
Points - Points from the collection

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCollectionToPointsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionToPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection storing the points | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection storing the points | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Points | Points from the collection | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints?application_version=5.7#outputs)
