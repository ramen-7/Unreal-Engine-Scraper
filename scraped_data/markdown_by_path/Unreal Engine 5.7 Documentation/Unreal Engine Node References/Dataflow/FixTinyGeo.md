<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo?application_version=5.7 -->

# FixTinyGeo

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
7. FixTinyGeo

# FixTinyGeo

FixTinyGeo (v1)

On this page

### Description

FixTinyGeo (v1)

Editor Fracture Mode / Utilities / TinyGeo tool
Merge pieces of geometry onto their neighbors -- use it to, for example, clean up too small pieces of geometry.

Input(s) :
Collection [Intrinsic] - Collection to use
TransformSelection - The selected pieces to use
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to use

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FFixTinyGeoDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FFixTinyGeoDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MergeType | Whether to merge small geometry, or small clusters | [EFixTinyGeoMergeType](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoMergeType) | MergeGeometry |
| bOnFractureLevel | Only consider bones at the current Fracture Level | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bOnlyClusters | Only auto-consider clusters for merging. Note that leaf nodes can still be consider if manually selected. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlySameParent | Only merge clusters to neighbors with the same parent in the hierarchy | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bGeometryOnlySameParent | Only merge geometry to neighbors with the same parent in the hierarchy | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| NeighborSelection |  | [EFixTinyGeoNeighborSelectionMethod](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoNeighborSelectionMeth-) | LargestNeighbor |
| bOnlyToConnected | Only merge pieces that are connected in the proximity graph.If unchecked, connected pieces will still be favored, but if none are available the closest disconnected piece can be merged. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseCollectionProximityForConnections | Whether to use the Proximity (as computed by the Proximity node) to determine which bones are connected, and thus can be considered for merging. Otherwise will compute and use a reasonable default connectivity. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| UseBoneSelection | Options for using the current bone selection | [EFixTinyGeoUseBoneSelection](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoUseBoneSelection) | NoEffect |
| SelectionMethod |  | [EFixTinyGeoGeometrySelectionMethod](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFixTinyGeoGeometrySelectionMeth-) | RelativeVolume |
| MinVolumeCubeRoot | If size (cube root of volume) is less than this value, geometry should be merged into neighbors -- i.e. a value of 2 merges geometry smaller than a 2x2x2 cube | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RelativeVolume | If cube root of volume relative to the overall shape's cube root of volume is less than this, the geometry should be merged into its neighbors. (Note: This is a bit different from the histogram viewer's "Relative Size," which instead shows values relative to the largest rigid bone.) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The selected pieces to use | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to use | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo?application_version=5.7#outputs)
