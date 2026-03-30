<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints?application_version=5.7 -->

# GridScatterPoints

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
7. GridScatterPoints

# GridScatterPoints

GridScatterPoints (v1)

On this page

### Description

GridScatterPoints (v1)

Grid Scatter Points Dataflow Node

Input(s) :
NumberOfPointsInX - Number of points in X direction
NumberOfPointsInY - Number of points in Y direction
NumberOfPointsInZ - Number of points in Z direction
RandomSeed - Seed for random
MaxRandomDisplacementX - Random displacement in X direction will be in the range (-MaxRandomDisplacementX, MaxRandomDisplacementX)
MaxRandomDisplacementY - Random displacement in Y direction will be in the range (-MaxRandomDisplacementY, MaxRandomDisplacementY)
MaxRandomDisplacementZ - Random displacement in Z direction will be in the range (-MaxRandomDisplacementZ, MaxRandomDisplacementZ)
BoundingBox - BoundingBox to generate points inside of

Output(s):
Points - Generated points

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Point |
| Type | [FGridScatterPointsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGridScatterPointsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoundingBox | BoundingBox to generate points inside of | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| NumberOfPointsInX | Number of points in X direction | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| NumberOfPointsInY | Number of points in Y direction | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| NumberOfPointsInZ | Number of points in Z direction | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| RandomSeed | Seed for random | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaxRandomDisplacementX | Random displacement in X direction will be in the range (-MaxRandomDisplacementX, MaxRandomDisplacementX) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRandomDisplacementY | Random displacement in Y direction will be in the range (-MaxRandomDisplacementY, MaxRandomDisplacementY) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| MaxRandomDisplacementZ | Random displacement in Z direction will be in the range (-MaxRandomDisplacementZ, MaxRandomDisplacementZ) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Points | Generated points | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints?application_version=5.7#outputs)
