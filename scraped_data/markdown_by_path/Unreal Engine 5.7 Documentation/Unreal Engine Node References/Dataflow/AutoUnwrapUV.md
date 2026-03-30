<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV?application_version=5.7 -->

# AutoUnwrapUV

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
7. AutoUnwrapUV

# AutoUnwrapUV

AutoUnwrapUV (v1)

On this page

### Description

AutoUnwrapUV (v1)

Auto unwrap UVs for a specific UV channel

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - Faces to auto unwrap, no selection means all faces
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
| Type | [FAutoUnwrapUVDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FAutoUnwrapUVDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | Faces to auto unwrap, no selection means all faces | [FDataflowFaceSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | UV channel to unwrap into ( 0 by default ) | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV?application_version=5.7#outputs)
