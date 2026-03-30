<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices?application_version=5.7 -->

# BlendVertices

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
7. BlendVertices

# BlendVertices

BlendVertices (v1)

On this page

### Description

BlendVertices (v1)

Blend vertex values from another cloth collection. The topology of the Collection will remain the same.

Input(s) :
Collection - Input/output collection
BlendCollection - Collection to blend in.

Output(s):
Collection [Passthrough] - Input/output collection

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Blend Vertices |
| Type | [FChaosClothAssetBlendVerticesNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetBlendVerticesNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bRequireSameVertexCounts | Require same vertex counts between Collection and BlendCollection in order to blend a vertex type. Otherwise the shared subset will be blended. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BlendingWeight | Blending Weight. 0 = Keep existing values in Collection. 1 = Set values from BlendCollection. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bBlendSimMesh | Blend Sim Mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlend2DSimPositions | Blend 2D Sim Positions. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlend3DSimPositions | Blend 3D Sim Positions. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendSimNormals | Blend 3D Sim Normals. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderMesh | Blend Render Mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderPositions | Blend Render Positions. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderNormalsAndTangents | Blend Render Normals and Tangents. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderUVs | Blend Render UVs. Only existing UV sets on Collection will be updated. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bBlendRenderColors | Blend Render Colors. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BlendCollection | Collection to blend in. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input/output collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices?application_version=5.7#outputs)
