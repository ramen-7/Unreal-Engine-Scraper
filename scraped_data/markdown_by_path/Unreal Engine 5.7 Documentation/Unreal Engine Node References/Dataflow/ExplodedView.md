<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView?application_version=5.7 -->

# ExplodedView

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
7. ExplodedView

# ExplodedView

ExplodedView (v1)

On this page

### Description

ExplodedView (v1)

"Explodes" the pieces from the Collection for better visualization

Input(s) :
Collection [Intrinsic] - Collection to explode
UniformScale - Scale amount to expand the pieces uniformly in all directions
Scale - Scale amounts to expand the pieces in all 3 directions
Offset - Translate collection for exploded view

Output(s):
Collection [Passthrough] - Collection to explode

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture|Utilities |
| Type | [FExplodedViewDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExplodedViewDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to explode | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| UniformScale | Scale amount to expand the pieces uniformly in all directions | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Scale | Scale amounts to expand the pieces in all 3 directions | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Offset | Translate collection for exploded view | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to explode | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView?application_version=5.7#outputs)
