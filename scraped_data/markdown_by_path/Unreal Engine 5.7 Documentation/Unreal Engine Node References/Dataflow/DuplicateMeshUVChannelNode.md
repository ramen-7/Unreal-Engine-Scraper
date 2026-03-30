<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode?application_version=5.7 -->

# DuplicateMeshUVChannelNode

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
7. DuplicateMeshUVChannelNode

# DuplicateMeshUVChannelNode

DuplicateMeshUVChannelNode (v1)

On this page

### Description

DuplicateMeshUVChannelNode (v1)

Create a new UV layer/channel in a UDataflowMesh

Input(s) :
Mesh [Intrinsic] - DataflowMesh input/output

Output(s):
Mesh [Passthrough] - DataflowMesh input/output
NewUVChannel - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Tags | Mesh UV DataflowMesh |
| Type | [FDuplicateMeshUVChannelNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDuplicateMeshUVChannelNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceUVChannel | Index of the source UV channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh input/output | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | DataflowMesh input/output | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |
| NewUVChannel | Index of the added UV channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode?application_version=5.7#outputs)
