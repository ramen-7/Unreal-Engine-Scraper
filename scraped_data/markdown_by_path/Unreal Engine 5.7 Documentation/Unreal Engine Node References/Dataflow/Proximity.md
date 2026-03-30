<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity?application_version=5.7 -->

# Proximity

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
7. Proximity

# Proximity

Proximity (v1)

On this page

### Description

Proximity (v1)

Update the proximity (contact) graph for the bones in a Collection

Input(s) :
DistanceThreshold - If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors
ContactThreshold - If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity
Collection [Intrinsic] - GeometryCollection to update the proximity graph on

Output(s):
Collection [Passthrough] - GeometryCollection to update the proximity graph on

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FProximityDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FProximityDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ProximityMethod | Which method to use to decide whether a given piece of geometry is in proximity with another | [EProximityMethodEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EProximityMethodEnum) | Dataflow\_ProximityMethod\_Precise |
| FilterContactMethod | How to use the Contact Threshold (if > 0) to filter out unwanted small or corner contacts from the proximity graph. If contact threshold is zero, no filtering is applied. | [EProximityContactFilteringMethodEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EProximityContactFilteringMethod-) | Dataflow\_ProximityContactFilteringMethod\_ProjectedBoundsOverlap |
| bUseAsConnectionGraph | Whether to automatically transform the proximity graph into a connection graph to be used for simulation | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ContactAreaMethod | The method used to compute contact areas for simulation purposes (only when 'Use As Connection Graph' is enabled) | [EConnectionContactAreaMethodEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EConnectionContactAreaMethodEnum) | Dataflow\_ConnectionContactAreaMethod\_None |
| bRecomputeConvexHulls | Whether to compute new convex hulls for proximity, or use the pre-existing hulls on the Collection, when using convex hulls to determine proximity | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color |  | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=0.000000,A=1.000000) |
| LineWidthMultiplier |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| CenterColor |  | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| CenterSize |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12.000000 |
| bRandomizeColor | Randomize color per connection | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ColorRandomSeed | Random seed | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to update the proximity graph on | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| DistanceThreshold | If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ContactThreshold | If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection to update the proximity graph on | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity?application_version=5.7#outputs)
