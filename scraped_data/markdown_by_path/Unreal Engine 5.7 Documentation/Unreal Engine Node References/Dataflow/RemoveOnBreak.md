<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak?application_version=5.7 -->

# RemoveOnBreak

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
7. RemoveOnBreak

# RemoveOnBreak

RemoveOnBreak (v1)

On this page

### Description

RemoveOnBreak (v1)

Remove on Break Dataflow Node

Input(s) :
Collection [Intrinsic] - Collection to set theremoval data on
TransformSelection - selection to apply the data on ( if not specified the entire collection will be set )
bEnabledRemoval - Whether or not to enable the removal on the selection
PostBreakTimer - How long after the break the removal will start ( Min / Max )
RemovalTimer - How long removal will last ( Min / Max )
bClusterCrumbling - If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect

Output(s):
Collection [Passthrough] - Collection to set theremoval data on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FRemoveOnBreakDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRemoveOnBreakDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to set theremoval data on | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | selection to apply the data on ( if not specified the entire collection will be set ) | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bEnabledRemoval | Whether or not to enable the removal on the selection | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PostBreakTimer | How long after the break the removal will start ( Min / Max ) | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| RemovalTimer | How long removal will last ( Min / Max ) | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000) |
| bClusterCrumbling | If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to set theremoval data on | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak?application_version=5.7#outputs)
