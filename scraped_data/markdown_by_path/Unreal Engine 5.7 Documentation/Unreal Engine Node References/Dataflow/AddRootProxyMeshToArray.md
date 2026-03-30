<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray?application_version=5.7 -->

# AddRootProxyMeshToArray

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
7. AddRootProxyMeshToArray

# AddRootProxyMeshToArray

AddRootProxyMeshToArray (v1)

On this page

### Description

AddRootProxyMeshToArray (v1)

* Add a root proxy object to an array of root proxy mesh
* + (used by geometry collection assets)

Input(s) :
RootProxyMeshes - Root proxy array to add the mesh to

Output(s):
RootProxyMeshes [Passthrough] - Root proxy array to add the mesh to

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Type | [FAddRootProxyMeshToArrayDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAddRootProxyMeshToArrayDataflow-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | Root proxy array to add the mesh to | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |
| RootProxyMesh |  | [FDataflowRootProxyMesh](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh) | (Mesh=None,Transform=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),OverrideMaterials=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RootProxyMeshes | Root proxy array to add the mesh to | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowRootProxyMesh](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowRootProxyMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray?application_version=5.7#outputs)
