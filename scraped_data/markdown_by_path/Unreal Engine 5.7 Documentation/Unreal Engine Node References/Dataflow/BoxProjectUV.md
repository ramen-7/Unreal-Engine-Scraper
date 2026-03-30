<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV?application_version=5.7 -->

# BoxProjectUV

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
7. BoxProjectUV

# BoxProjectUV

BoxProjectUV (v1)

On this page

### Description

BoxProjectUV (v1)

Generates UVs using a box projection

Input(s) :
Collection [Intrinsic] - Target Collection
UVChannel - UV channel to unwrap into ( 0 by default )
GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture

Output(s):
Collection [Passthrough] - Target Collection
UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default )

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|UV |
| Type | [FBoxProjectUVDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBoxProjectUVDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ProjectionScale |  | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000,Z=100.000000) |
| UVOffset |  | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.500000,Y=0.500000) |
| bAutoFitToBounds |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bCenterBoxAtPivot |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bUniformProjectionScale |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GutterSize | Approximate space to leave between UV islands, measured in texels for 512x512 texture | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV?application_version=5.7#outputs)
