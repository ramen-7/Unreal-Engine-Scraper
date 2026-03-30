<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts?application_version=5.7 -->

# GetOutfitBodyParts

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
7. GetOutfitBodyParts

# GetOutfitBodyParts

GetOutfitBodyParts (v1)

On this page

### Description

GetOutfitBodyParts (v1)
Experimental

Extract the Body Part Skeletal Meshes from an Outfit.

Input(s) :
Outfit - The source outfit.

Output(s):
Outfit [Passthrough] - The source outfit.
BodySizeParts - The outfit body parts grouped by BodySize.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Body Parts Skeletal Mesh |
| Type | FChaosGetOutfitBodyPartsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| BodySizeParts | The outfit body parts grouped by BodySize. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts?application_version=5.7#outputs)
