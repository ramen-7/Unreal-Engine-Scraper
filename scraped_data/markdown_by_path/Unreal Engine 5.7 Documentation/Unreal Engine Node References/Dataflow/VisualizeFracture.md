<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture?application_version=5.7 -->

# VisualizeFracture

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
7. VisualizeFracture

# VisualizeFracture

VisualizeFracture (v1)

On this page

### Description

VisualizeFracture (v1)

Visualizing fracture/cluster info in fractured collection

Input(s) :
Collection [Intrinsic] - Collection to visualize
RandomSeed - Seed for random
ExplodeAmount - Scale amount to expand the pieces uniformly in all directions
Scale - Scale amounts to expand the pieces in all 3 directions
Offset - Translate collection for exploded view

Output(s):
Collection [Passthrough] - Collection to visualize

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FVisualizeFractureDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FVisualizeFractureDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bApplyExplodedView | Use cluster level for coloring and explode | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bApplyColor |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColoringType |  | [EDataflowVisualizeFractureColoringType](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowVisualizeFractureColori-) | ColorByLevel |
| RandomColorRangeMin |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 40 |
| RandomColorRangeMax |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 190 |
| Attribute |  | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Min |  | [FMinSettings](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMinSettings) | (MinAttrValue=0.000000,MinColor=(R=0.000000,G=1.000000,B=0.000000,A=1.000000)) |
| Max |  | [FMaxSettings](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMaxSettings) | (MaxAttrValue=1.000000,MaxColor=(R=1.000000,G=0.000000,B=0.000000,A=1.000000)) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to visualize | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| RandomSeed | Seed for random | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Level |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ExplodeAmount | Scale amount to expand the pieces uniformly in all directions | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Scale | Scale amounts to expand the pieces in all 3 directions | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Offset | Translate collection for exploded view | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to visualize | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture?application_version=5.7#outputs)
