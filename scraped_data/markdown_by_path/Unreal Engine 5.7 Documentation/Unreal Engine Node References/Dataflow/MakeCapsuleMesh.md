<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh?application_version=5.7 -->

# MakeCapsuleMesh

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
7. MakeCapsuleMesh

# MakeCapsuleMesh

MakeCapsuleMesh (v1) Make a capsule mesh Output(s): Mesh - Output mesh

On this page

### Description

MakeCapsuleMesh (v1)

Make a capsule mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeCapsuleMeshDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeCapsuleMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Radius | Radius of capsule | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SegmentLength | Length of capsule line segment, so total height is SegmentLength + 2\*Radius | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| NumHemisphereArcSteps | Number of vertices along the 90-degree arc from the pole to edge of spherical cap. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| NumCircleSteps | Number of vertices along each circle | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 6 |
| NumSegmentSteps | Number of subdivisions lengthwise along the cylindrical section | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh?application_version=5.7#parameters)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh?application_version=5.7#outputs)
