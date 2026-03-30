<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding?application_version=5.7 -->

# SetVertexTrianglePositionTargetBinding

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
7. SetVertexTrianglePositionTargetBinding

# SetVertexTrianglePositionTargetBinding

SetVertexTrianglePositionTargetBinding (v1)

On this page

### Description

SetVertexTrianglePositionTargetBinding (v1)

Create point-triangle weak constraints (springs) between surface meshes of different geometries based on search radius.

Input(s) :
VertexSelection - (optional) only create weak constraints from surface vertices in VertexSelection to triangles in other geometries

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetVertexTrianglePositionTargetBindingDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetVertexTrianglePositionTarget-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PositionTargetStiffness |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| SearchRadius | Search radius for point-triangle pairs between geometry surfaces. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bAllowSliding | if point-triangle weak constraints created are anisotropic and allow sliding along the triangle plane | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bZeroRestLengthEditable |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUseZeroRestLengthSprings | if point-triangle weak constraints created are zero rest-length. if true, this will cause point triangle pair to stick together, as opposed to separated by their rest state distance. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| VertexSelection | (optional) only create weak constraints from surface vertices in VertexSelection to triangles in other geometries | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding?application_version=5.7#outputs)
