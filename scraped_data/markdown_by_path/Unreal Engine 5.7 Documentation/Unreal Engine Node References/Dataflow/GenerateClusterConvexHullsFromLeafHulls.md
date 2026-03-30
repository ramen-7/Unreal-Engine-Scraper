<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls?application_version=5.7 -->

# GenerateClusterConvexHullsFromLeafHulls

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
7. GenerateClusterConvexHullsFromLeafHulls

# GenerateClusterConvexHullsFromLeafHulls

GenerateClusterConvexHullsFromLeafHulls (v1)

On this page

### Description

GenerateClusterConvexHullsFromLeafHulls (v1)

Generates cluster convex hulls for leafs hulls

Input(s) :
ConvexCount - Maximum number of convex to generate for a specific cluster. Will be ignored if error tolerance is used instead
ErrorTolerance - Error tolerance to use to decide to merge leaf convex together.
This is in centimeters and represents the side of a cube, the volume of which will be used as threshold
to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex
OptionalSelectionFilter - Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed.
bAllowMergingLeafHulls - Also allow the same hull merging process to run on leaf hulls (merging hulls on leaves in the selection)
bProtectNegativeSpace - Whether to use a sphere cover to define negative space that should not be covered by convex hulls
TargetNumSamples - Approximate number of spheres to consider when covering negative space. Only applicable with the Uniform Sample Method or if Require Search Sample Coverage is disabled.
MinSampleSpacing - Minimum desired spacing between spheres; if > 0, will attempt not to place sphere centers closer than this
NegativeSpaceTolerance - Amount of space to leave between convex hulls and protected negative space
MinRadius - Spheres smaller than this are not included in the negative space

Output(s):
SphereCovering - A representation of the negative space protected by the 'protect negative space' option. If negative space is not protected, this will contain zero spheres.

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGenerateClusterConvexHullsFromLeafHullsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGenerateCluster-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bPreferExternalCollisionShapes | Whether to prefer available External (imported) collision shapes instead of the computed convex hulls on the Collection | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AllowMerges | Method to determine if the convex hulls from two separate bones can potentially be merged | [EAllowConvexMergeMethod](/documentation/en-us/unreal-engine/API/Runtime/Chaos/EAllowConvexMergeMethod) | ByProximity |
| MergeProximityFilter | Filter to optionally only consider spatially close convex hulls for merges | [EConvexHullProximityFilter](/documentation/en-us/unreal-engine/API/Runtime/Chaos/EConvexHullProximityFilter) | None |
| MergeProximityDistanceThreshold | If applying a convex hull proximity filter, the distance threshold to use for determining that two convex hulls are close enough to merge | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| SampleMethod | Method to use to find and sample negative space | [ENegativeSpaceSampleMethodDataflowEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ENegativeSpaceSampleMethodDatafl-) | Uniform |
| bRequireSearchSampleCoverage | Whether to require that all candidate locations identified by Voxel Search are covered by negative space samples, up to the specified Min Sample Spacing. Only applies to Voxel Search. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlyConnectedToHull | When performing Voxel Search, only look for negative space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. Only applies to Voxel Search. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SphereCoveringDebugDrawRenderSettings |  | [FDataflowNodeSphereCoveringDebugDrawSettings](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeSphereCoveringDebug-) | (bDisplaySphereCovering=False,RenderType=Wireframe,bTranslucent=True,LineWidthMultiplier=0.250000,ColorMethod=Single,Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorRandomSeed=0,ColorA=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),ColorB=(R=0.000000,G=0.000000,B=1.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| ConvexCount | Maximum number of convex to generate for a specific cluster. Will be ignored if error tolerance is used instead | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 2 |
| ErrorTolerance | Error tolerance to use to decide to merge leaf convex together. This is in centimeters and represents the side of a cube, the volume of which will be used as threshold to know if the volume of the generated convex is too large compared to the sum of the volume of the leaf convex | double | 0.000000 |
| OptionalSelectionFilter | Optional transform selection to compute cluster hulls on -- if not provided, all cluster hulls will be computed. | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| bAllowMergingLeafHulls | Also allow the same hull merging process to run on leaf hulls (merging hulls on leaves in the selection) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bProtectNegativeSpace | Whether to use a sphere cover to define negative space that should not be covered by convex hulls | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| TargetNumSamples | Approximate number of spheres to consider when covering negative space. Only applicable with the Uniform Sample Method or if Require Search Sample Coverage is disabled. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 50 |
| MinSampleSpacing | Minimum desired spacing between spheres; if > 0, will attempt not to place sphere centers closer than this | double | 1.000000 |
| NegativeSpaceTolerance | Amount of space to leave between convex hulls and protected negative space | double | 2.000000 |
| MinRadius | Spheres smaller than this are not included in the negative space | double | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| SphereCovering | A representation of the negative space protected by the 'protect negative space' option. If negative space is not protected, this will contain zero spheres. | [FDataflowSphereCovering](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowSphereCovering) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls?application_version=5.7#outputs)
