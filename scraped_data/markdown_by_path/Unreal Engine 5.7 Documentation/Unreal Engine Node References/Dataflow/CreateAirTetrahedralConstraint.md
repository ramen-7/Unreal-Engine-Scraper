<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint?application_version=5.7 -->

# CreateAirTetrahedralConstraint

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
7. CreateAirTetrahedralConstraint

# CreateAirTetrahedralConstraint

CreateAirTetrahedralConstraint (v1)

On this page

### Description

CreateAirTetrahedralConstraint (v1)

Create air tetrahedral constraint between point-triangle pair from surface meshes of different geometries based on search radius.
The added tetrahedra help to maintain distance between geometries.
This node renders the boundary of the added tetrahedral mesh.

Input(s) :
VertexSelection - (optional) only create tetrahedral constraints from surface vertices in VertexSelection to triangles in other geometries.
For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries.
No constraints will be created between two geometries that are not in the VertexSelection.

Output(s):
DynamicMesh - Render dynamic mesh of the boundary mesh of added tetrahedra

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateAirTetrahedralConstraintDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateAirTetrahedralConstraintD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SearchRadius | tetrahedral constraint search radius | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create tetrahedral constraints from surface vertices in VertexSelection to triangles in other geometries. For example, if the VertexSelection contains only one geometry, only this geometry will bind to other geometries. No constraints will be created between two geometries that are not in the VertexSelection. | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| DynamicMesh | Render dynamic mesh of the boundary mesh of added tetrahedra | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint?application_version=5.7#outputs)
