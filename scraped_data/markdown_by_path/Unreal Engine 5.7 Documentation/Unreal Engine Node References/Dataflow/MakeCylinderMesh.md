<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh?application_version=5.7 -->

# MakeCylinderMesh

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
7. MakeCylinderMesh

# MakeCylinderMesh

MakeCylinderMesh (v1) Make a cylinder mesh Output(s): Mesh - Output mesh

On this page

### Description

MakeCylinderMesh (v1)

Make a cylinder mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeCylinderMeshDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeCylinderMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius1 | Radius1 of cylinder | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Radius2 | Radius2 of cylinder | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Height | Height of cylinder | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| LengthSamples | LengthSamples of cylinder | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| AngleSamples | AngleSamples of cylinder | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 12 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh?application_version=5.7#parameters)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh?application_version=5.7#outputs)
