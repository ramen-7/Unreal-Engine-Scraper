<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron?application_version=5.7 -->

# CreateTetrahedron

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
7. CreateTetrahedron

# CreateTetrahedron

CreateTetrahedron (v1)

On this page

### Description

CreateTetrahedron (v1)

Create Tetrahedron Dataflow Node

Input(s) :
Collection - Input pass-through collection. When connected, the generated tetrahedron will be nested into
its associated parents transform.
SourceCollection - Source collection used to generate the tetrahedron from. Closed geometry within the collections geometry group will be used to
generate tetrahedron.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FCreateTetrahedronDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCreateTetrahedronDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Method | Tetrahedral meshing method (TetWild or ISO-stuffing) | [TEnumAsByte](/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[TetMeshingMethod](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/TetMeshingMethod)> | IsoStuffing |
| Selection | Name of the mesh in the collection. This is defined from the name of the mesh's parent transform. CollectionKey("BoneName","Vertices") | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| NumCells | General control for density for the tetrahedron. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 32 |
| OffsetPercent | Surface offset percentage to increase or decrease the surface alignment. | double | 0.050000 |
| IdealEdgeLengthRel | ! Desired relative edge length, as a fraction of bounding box size | double | 0.050000 |
| MaxIterations | ! Maximum number of optimization iterations. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 80 |
| StopEnergy | ! Energy at which to stop optimizing tet quality and accept the result. | double | 10.000000 |
| EpsRel | ! Relative tolerance, controlling how closely the mesh must follow the input surface. | double | 0.001000 |
| bCoarsen | ! Coarsen the tet mesh result. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bExtractManifoldBoundarySurface | ! Enforce that the output boundary surface should be manifold. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bSkipSimplification | ! Skip the initial simplification step. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bInvertOutputTets | ! Invert tetrahedra. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDiscardInteriorTriangles | Common | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input pass-through collection. When connected, the generated tetrahedron will be nested into its associated parents transform. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SourceCollection | Source collection used to generate the tetrahedron from. Closed geometry within the collections geometry group will be used to generate tetrahedron. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input pass-through collection. When connected, the generated tetrahedron will be nested into its associated parents transform. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron?application_version=5.7#outputs)
