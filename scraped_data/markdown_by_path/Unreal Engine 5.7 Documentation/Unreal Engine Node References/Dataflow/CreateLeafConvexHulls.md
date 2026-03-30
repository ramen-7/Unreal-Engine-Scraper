<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls?application_version=5.7 -->

# CreateLeafConvexHulls

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
7. CreateLeafConvexHulls

# CreateLeafConvexHulls

CreateLeafConvexHulls (v1)

On this page

### Description

CreateLeafConvexHulls (v1)

Create Leaf Convex Hulls Dataflow Node

Input(s) :
OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed.
SimplificationDistanceThreshold - Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume).

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FCreateLeafConvexHullsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateLeafConvexHullsDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GenerateMethod | How convex hulls are generated -- computed from geometry, imported from external collision shapes, or an intersection of both options. | [EGenerateConvexMethod](/documentation/en-us/unreal-engine/API/Runtime/Chaos/EGenerateConvexMethod) | ComputedFromGeometry |
| IntersectIfComputedIsSmallerByFactor | If GenerateMethod is Intersect, only actually intersect when the volume of the Computed Hull is less than this fraction of the volume of the External Hull(s). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| MinExternalVolumeToIntersect | If GenerateMethod is Intersect, only actually intersect if the volume of the External Hull(s) exceed this threshold. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bComputeIntersectionsBeforeHull | Whether to compute the intersection before computing convex hulls. Typically should be enabled. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SphereCoveringDebugDrawRenderSettings |  | [FDataflowNodeSphereCoveringDebugDrawSettings](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeSphereCoveringDebug-) | (bDisplaySphereCovering=False,RenderType=Wireframe,bTranslucent=True,LineWidthMultiplier=0.250000,ColorMethod=Single,Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorRandomSeed=0,ColorA=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorB=(R=0.000000,G=0.000000,B=1.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| OptionalSelectionFilter | Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| SimplificationDistanceThreshold | Computed convex hulls are simplified to keep points spaced at least this far apart (except where needed to keep the hull from collapsing to zero volume). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| ConvexDecompositionSettings |  | [FDataflowConvexDecompositionSettings](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowConvexDecompositionSett-) | (MinSizeToDecompose=0.000000,MaxGeoToHullVolumeRatioToDecompose=1.000000,ErrorTolerance=0.000000,MaxHullsPerGeometry=-1,MinThicknessTolerance=0.000000,NumAdditionalSplits=4,bProtectNegativeSpace=False,bOnlyConnectedToHull=True,NegativeSpaceTolerance=2.000000,NegativeSpaceMinRadius=10.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SphereCovering |  | [FDataflowSphereCovering](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls?application_version=5.7#outputs)
