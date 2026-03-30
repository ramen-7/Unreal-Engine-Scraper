<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls?application_version=5.7 -->

# CreateNonOverlappingConvexHulls

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
7. CreateNonOverlappingConvexHulls

# CreateNonOverlappingConvexHulls

CreateNonOverlappingConvexHulls (v1)

On this page

### Description

CreateNonOverlappingConvexHulls (v1)

Generates convex hull representation for the bones for simulation

Input(s) :
CanExceedFraction - Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children. 0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume.
SimplificationDistanceThreshold - Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume)
OverlapRemovalShrinkPercent - Overlap removal will be computed as if convex hulls were this percentage smaller (in range 0-100)
CanRemoveFraction - Fraction of the convex hulls for a cluster that we can remove before using the hulls of the children

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCreateNonOverlappingConvexHullsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateNonOverlappingConvexHulls-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OverlapRemovalMethod | Whether and in what cases to automatically cut away overlapping parts of the convex hulls, to avoid the simulation 'popping' to fix the overlaps | [EConvexOverlapRemovalMethodEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EConvexOverlapRemovalMethodEnum) | Dataflow\_EConvexOverlapRemovalMethod\_All |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CanRemoveFraction | Fraction of the convex hulls for a cluster that we can remove before using the hulls of the children | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.300000 |
| SimplificationDistanceThreshold | Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CanExceedFraction | Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children. 0 means the convex volume cannot exceed the geometry volume; 1 means the convex volume is allowed to be 100% larger (2x) the geometry volume. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| OverlapRemovalShrinkPercent | Overlap removal will be computed as if convex hulls were this percentage smaller (in range 0-100) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls?application_version=5.7#outputs)
