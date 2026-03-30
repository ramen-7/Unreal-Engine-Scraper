<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh?application_version=5.7 -->

# BoxToMesh

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
7. BoxToMesh

# BoxToMesh

BoxToMesh (v1)

On this page

### Description

BoxToMesh (v1)

Converts a BoundingBox into a DynamicMesh

Input(s) :
Box [Intrinsic] - BoundingBox input

Output(s):
Mesh - Mesh output
TriangleCount - Mesh triangle count

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Mesh|Utilities |
| Type | [FBoxToMeshDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoxToMeshDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Box | BoundingBox input | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Mesh output | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| TriangleCount | Mesh triangle count | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh?application_version=5.7#outputs)
