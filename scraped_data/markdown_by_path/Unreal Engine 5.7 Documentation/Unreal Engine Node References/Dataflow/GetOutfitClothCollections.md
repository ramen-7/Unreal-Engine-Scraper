<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections?application_version=5.7 -->

# GetOutfitClothCollections

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
7. GetOutfitClothCollections

# GetOutfitClothCollections

GetOutfitClothCollections (v1)

On this page

### Description

GetOutfitClothCollections (v1)
Experimental

Extract the cloth collections contained into the specified source outfit.

Input(s) :
Outfit - The source outfit.
LodIndex - The LOD to output in the cloth collections array. Set to -1 to output all LODs

Output(s):
Outfit [Passthrough] - The source outfit.
ClothCollections - The outfit cloth collections array in group of consecutives LODs for each of the outfit pieces.
NumLods - The number of LODs output in the cloth collections array.
NumPieces - The number of cloth pieces output in the cloth collections array.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Cloth Collections |
| Type | FChaosGetOutfitClothCollectionsNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| LodIndex | The LOD to output in the cloth collections array. Set to -1 to output all LODs | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The source outfit. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| ClothCollections | The outfit cloth collections array in group of consecutives LODs for each of the outfit pieces. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection)> |  |
| NumLods | The number of LODs output in the cloth collections array. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| NumPieces | The number of cloth pieces output in the cloth collections array. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections?application_version=5.7#outputs)
