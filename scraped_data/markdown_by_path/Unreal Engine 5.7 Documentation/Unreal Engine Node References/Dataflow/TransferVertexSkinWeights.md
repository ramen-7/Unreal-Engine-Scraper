<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights?application_version=5.7 -->

# TransferVertexSkinWeights

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
7. TransferVertexSkinWeights

# TransferVertexSkinWeights

TransferVertexSkinWeights (v1)

On this page

### Description

TransferVertexSkinWeights (v1)

Transfer skin weights from a source collection to a target collection.
Component Transfer is used when all geometries from the source collection have matched names with the target collection.
Otherwise, Global Transfer is used.
Geometries are matched when the geometry's BoneName can be found as the start of the BoneName of a geometry in the target collection.
Use TransformNameSuffix to add extra string to the source geometry's BoneName to avoid multiple matched names.
For example, source geometry has name SK\_10 and target geometry has name SK\_10\_tet1
For all names, Check BoneName attribute in Transform group in the collection.

Input(s) :
Collection - Target collection to transfer vertex attribute to.
FromCollection - Source collection to transfer vertex attribute from.

Output(s):
Collection [Passthrough] - Target collection to transfer vertex attribute to.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection |
| Tags | Transfer vertex skin weights from the Source Collection to the Target Collection |
| Type | [FGeometryCollectionTransferVertexSkinWeightsNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGeometryCollect-_3) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TransferMethod | Transfer method [default: Paired Geometry Transfer] | [EDataflowTransferVertexAttributeNodeTransferMethod](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_2) | Global |
| BoundingVolumeType | Bounding volume type for source assets[default: Triangle] | [EDataflowTransferVertexAttributeNodeBoundingVolume](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-_1) | Triangle |
| SourceScale | Bounding volume hierarchy cell size for neighboring vertices to transfer into[default: Asset] | [EDataflowTransferVertexAttributeNodeSourceScale](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransfe-) | Asset\_Bound |
| Falloff | Falloff of source value based on distance from source triangle[default: Squared] | [EDataflowTransferVertexAttributeNodeFalloff](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowTransferVertexAttribute-) | None |
| FalloffThreshold | Threshold based on distance from source triangle.Values past the threshold will falloff.[Defaults to 1 percent of triangle size(0.01)] | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| EdgeMultiplier | Edge multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| BoundMultiplier | Max bound multiplier for the Bounding Volume Hierarchy(BVH) target's particle search radius. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| TransformNameSuffix | Suffix of transform names for geometry matching during transfer[default: \_Tet]. In CreateTetrahedron node we add \_Tet to tetrahedral geometries. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | \_Tet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FromCollection | Source collection to transfer vertex attribute from. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target collection to transfer vertex attribute to. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights?application_version=5.7#outputs)
