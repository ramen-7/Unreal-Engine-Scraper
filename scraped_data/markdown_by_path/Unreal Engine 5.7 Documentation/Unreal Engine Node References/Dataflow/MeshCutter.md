<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter?application_version=5.7 -->

# MeshCutter

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
7. MeshCutter

# MeshCutter

MeshCutter (v1)

On this page

### Description

MeshCutter (v1)

Editor Fracture Mode / Fracture / Mesh tool
Fracture using the shape of a chosen static mesh and/or array of dynamic meshes

Input(s) :
Collection [Intrinsic] - Collection to cut
BoundingBox - Boundingbox to create the cutting planes in
TransformSelection - The selected pieces to cut
Transform - Transform to apply to cut planes
CuttingDynamicMeshes - Dynamic Meshes to cut with
CuttingStaticMesh - Static Mesh to cut with
NumberToScatter - Number of meshes to random scatter
GridX - Number of meshes to add to grid in X
GridY - Number of meshes to add to grid in Y
GridZ - Number of meshes to add to grid in Z
Variability - Magnitude of random displacement to cutting meshes
MinScaleFactor - Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max
MaxScaleFactor - Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max
RollRange - Roll will be chosen between -Range and +Range
PitchRange - Pitch will be chosen between -Range and +Range
YawRange - Yaw will be chosen between -Range and +Range
RandomSeed - Seed for random
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to cut
TransformSelection [Passthrough] - The selected pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FMeshCutterDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshCutterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseHiRes | If using a Static Mesh to cut, attempt to use the Nanite HiRes source mesh, if available and non-empty. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| LODLevel | If using a Static Mesh to cut, and not using the Nanite HiRes source mesh, use this LOD level's mesh | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| CutDistribution | How to arrange the mesh cuts in space | [EMeshCutterCutDistribution](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EMeshCutterCutDistribution) | SingleCut |
| PerCutMeshSelection | When there are multiple cutting meshes, how to choose the cut mesh to apply at each location | [EMeshCutterPerCutMeshSelection](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EMeshCutterPerCutMeshSelection) | All |
| bRandomOrientation | Whether to randomly vary the orientation of the cutting meshes | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox | Boundingbox to create the cutting planes in | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply to cut planes | [FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| CuttingStaticMesh | Static Mesh to cut with | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UStaticMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/UStaticMesh)> | None |
| CuttingDynamicMeshes | Dynamic Meshes to cut with | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)>> |  |
| NumberToScatter | Number of meshes to random scatter | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| GridX | Number of meshes to add to grid in X | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| GridY | Number of meshes to add to grid in Y | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| GridZ | Number of meshes to add to grid in Z | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| Variability | Magnitude of random displacement to cutting meshes | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MinScaleFactor | Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| MaxScaleFactor | Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.500000 |
| RollRange | Roll will be chosen between -Range and +Range | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| PitchRange | Pitch will be chosen between -Range and +Range | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| YawRange | Yaw will be chosen between -Range and +Range | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 180.000000 |
| RandomSeed | Seed for random | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter?application_version=5.7#outputs)
