<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings?application_version=5.7 -->

# GenerateSurfaceBindings

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
7. GenerateSurfaceBindings

# GenerateSurfaceBindings

GenerateSurfaceBindings (v1)

On this page

### Description

GenerateSurfaceBindings (v1)

Generate barycentric bindings (used by the FleshDeformer deformer graph and Geometry Cache generation) of a render surface to a tetrahedral mesh and its surface.

* If a point is outside of the tetrahedral mesh, find surface embedding within SurfaceProjectionSearchRadius.
  Embeddings of LOD 0 are color coded in the render view:
  green: embedded on in a tetrahedron
  blue: embedded on a surface triangle
  red: orphan (cannot be embedded)
  yellow: orphan reparented to a tetrahedron from a node neighbor

Input(s) :
Collection - Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
StaticMeshIn - The input mesh, whose render surface is used to generate bindings.
SkeletalMeshIn - The input mesh, whose render surface is used to generate bindings.
TransformSelection - Render mesh will only bind to geometries whose transforms are in TransformSelection.
GeometryGroupGuidsIn - Render mesh will only bind to geometries whose GeometryGroupGuids match here.

Output(s):
Collection [Passthrough] - Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's.
SKMDynamicMesh - Converted from embedded skeletal/static mesh

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FGenerateSurfaceBindings](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FGenerateSurfaceBindings) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshLODList | Select skeletal mesh LODs to embed. Default empty list selects all LODs. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| bDoSurfaceProjection | Enable binding to the exterior hull of the tetrahedron mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SurfaceProjectionSearchRadius | The search radius when looking for surface triangles to bind to. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bDoOrphanReparenting | When nodes aren't contained in tetrahedra and surface projection fails, try to find suitable bindings by looking to neighboring parents. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| StaticMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| SkeletalMeshIn | The input mesh, whose render surface is used to generate bindings. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| TransformSelection | Render mesh will only bind to geometries whose transforms are in TransformSelection. | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| GeometryGroupGuidsIn | Render mesh will only bind to geometries whose GeometryGroupGuids match here. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection containing tetrahedral mesh and surface mesh. Bindings are stored as standalone groups in the \p Collection, keyed by the name of the input render mesh and all available LOD's. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SKMDynamicMesh | Converted from embedded skeletal/static mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings?application_version=5.7#outputs)
