<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh?application_version=5.7 -->

# BranchMesh

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
7. BranchMesh

# BranchMesh

BranchMesh (v1)

On this page

### Description

BranchMesh (v1)

Branch between two mesh inputs based on boolean condition

Input(s) :
MeshA - Mesh input
MeshB - Mesh input

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|FlowControl |
| Type | [FBranchMeshDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBranchMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bCondition | If true, Output = MeshA, otherwise Output = MeshB | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshA | Mesh input | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| MeshB | Mesh input | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bCondition | If true, Output = MeshA, otherwise Output = MeshB | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh?application_version=5.7#outputs)
