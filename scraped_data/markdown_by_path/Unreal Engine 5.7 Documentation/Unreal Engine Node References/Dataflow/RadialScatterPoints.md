<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints?application_version=5.7 -->

# RadialScatterPoints

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
7. RadialScatterPoints

# RadialScatterPoints

RadialScatterPoints (v2)

On this page

### Description

RadialScatterPoints (v2)

Radial Scatter Points Dataflow Node V 2

Input(s) :
BoundingBox - BoundingBox to generate points inside of
Center - Center of generated pattern
Normal - Normal to plane in which sites are generated
RandomSeed - Seed for random
AngularSteps - Number of angular steps
AngleOffset - Angle offset at each radial step (in degrees)
AngularNoise - Amount of global variation to apply to each angular step (in degrees)
Radius - Pattern radius (in cm)
RadialSteps - Number of radial steps
RadialStepExponent - Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent)
RadialMinStep - Minimum radial separation between any two voronoi points (in cm)
RadialNoise - Amount of global variation to apply to each radial step (in cm)
RadialVariability - Amount to randomly displace each Voronoi site radially (in cm)
AngularVariability - Amount to randomly displace each Voronoi site in angle (in degrees)
AxialVariability - Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm)

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FRadialScatterPointsDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRadialScatterPointsDataflowNode-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| Center | Center of generated pattern | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Normal | Normal to plane in which sites are generated | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| RandomSeed | Seed for random | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| AngularSteps | Number of angular steps | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| AngleOffset | Angle offset at each radial step (in degrees) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AngularNoise | Amount of global variation to apply to each angular step (in degrees) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Radius | Pattern radius (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |
| RadialSteps | Number of radial steps | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| RadialStepExponent | Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RadialMinStep | Minimum radial separation between any two voronoi points (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RadialNoise | Amount of global variation to apply to each radial step (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| RadialVariability | Amount to randomly displace each Voronoi site radially (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AngularVariability | Amount to randomly displace each Voronoi site in angle (in degrees) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| AxialVariability | Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints?application_version=5.7#outputs)
