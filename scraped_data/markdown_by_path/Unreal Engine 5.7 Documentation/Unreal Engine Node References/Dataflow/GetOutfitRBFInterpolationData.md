<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData?application_version=5.7 -->

# GetOutfitRBFInterpolationData

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
7. GetOutfitRBFInterpolationData

# GetOutfitRBFInterpolationData

GetOutfitRBFInterpolationData (v1)

On this page

### Description

GetOutfitRBFInterpolationData (v1)
Experimental

Extract the Body Part RBF Interpolation Data from an outfit.

Input(s) :
Outfit - The source outfit.
BodySizeIndex - The body size index.
BodyPartIndex - The body part (sub) index.

Output(s):
Outfit [Passthrough] - The source outfit.
InterpolationData - The interpolation data.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit RBF Interpolation Data |
| Type | FChaosGetOutfitRBFInterpolationDataNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| BodySizeIndex | The body size index. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| BodyPartIndex | The body part (sub) index. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| InterpolationData | The interpolation data. | [FMeshResizingRBFInterpolationData](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingCore/FMeshResizingRBFInterpolationDat-) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData?application_version=5.7#outputs)
