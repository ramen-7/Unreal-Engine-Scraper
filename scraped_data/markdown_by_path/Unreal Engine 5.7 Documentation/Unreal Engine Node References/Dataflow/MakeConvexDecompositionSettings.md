<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings?application_version=5.7 -->

# MakeConvexDecompositionSettings

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
7. MakeConvexDecompositionSettings

# MakeConvexDecompositionSettings

MakeConvexDecompositionSettings (v1)

On this page

### Description

MakeConvexDecompositionSettings (v1)

Provide settings for running convex decomposition of geometry

Input(s) :
MinSizeToDecompose - If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition
MaxGeoToHullVolumeRatioToDecompose - If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition
ErrorTolerance - Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error).
Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1
MaxHullsPerGeometry - If greater than zero, maximum number of convex hulls to use in each convex decomposition.
Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1
MinThicknessTolerance - Optionally specify a minimum thickness (in cm) for convex parts; parts below this thickness will always be merged away. Overrides NumOutputHulls and ErrorTolerance when needed.
NumAdditionalSplits - Control the search effort spent per convex decomposition: larger values will require more computation but may find better convex decompositions
bProtectNegativeSpace - Whether to drive decomposition by finding a negative space that should not be covered by convex hulls. If enabled, ErrorTolerance and NumAdditionalSplits will not be used.
bOnlyConnectedToHull - When protecting negative space, only look for space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration.
NegativeSpaceTolerance - Amount of space to leave between convex hulls and protected negative space
NegativeSpaceMinRadius - Spheres smaller than this are not included in the negative space

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FMakeDataflowConvexDecompositionSettingsNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeDataflowConvexDecomposition-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MinSizeToDecompose | If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxGeoToHullVolumeRatioToDecompose | If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ErrorTolerance | Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error). Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxHullsPerGeometry | If greater than zero, maximum number of convex hulls to use in each convex decomposition. Note: Decomposition will only be performed if: bProtectNegativeSpace is true, ErrorTolerance is > 0, or MaxHullsPerGeometry > 1 | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| MinThicknessTolerance | Optionally specify a minimum thickness (in cm) for convex parts; parts below this thickness will always be merged away. Overrides NumOutputHulls and ErrorTolerance when needed. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| NumAdditionalSplits | Control the search effort spent per convex decomposition: larger values will require more computation but may find better convex decompositions | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| bProtectNegativeSpace | Whether to drive decomposition by finding a negative space that should not be covered by convex hulls. If enabled, ErrorTolerance and NumAdditionalSplits will not be used. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bOnlyConnectedToHull | When protecting negative space, only look for space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NegativeSpaceTolerance | Amount of space to leave between convex hulls and protected negative space | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| NegativeSpaceMinRadius | Spheres smaller than this are not included in the negative space | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DecompositionSettings |  | [FDataflowConvexDecompositionSettings](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FDataflowConvexDecompositionSett-) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings?application_version=5.7#outputs)
