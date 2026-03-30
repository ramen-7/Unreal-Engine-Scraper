<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit?application_version=5.7 -->

# FilterSizedOutfit

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
7. FilterSizedOutfit

# FilterSizedOutfit

FilterSizedOutfit (v1)

On this page

### Description

FilterSizedOutfit (v1)
Experimental

Select a single size for the passed Outfit and filter out all non matching sizes.

Input(s) :
Outfit - The outfit to filter.
SizeName - The name of the body size to use to filter.
If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements.
TargetBody - The target body skeletal mesh containing the measurements to select the required size to use to filter.
The target body is unused if Size Name is a valid name.

Output(s):
Outfit [Passthrough] - The outfit to filter.
OutfitCollection - The outfit collection output, provided for convenience as a view into the outfit object metadata.
SizeName [Passthrough] - The name of the body size to use to filter.
If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements.

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Filter Sized Outfit |
| Type | FChaosOutfitAssetFilterSizedOutfitNode |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to filter. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |
| SizeName | The name of the body size to use to filter. If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| TargetBody | The target body skeletal mesh containing the measurements to select the required size to use to filter. The target body is unused if Size Name is a valid name. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | The outfit to filter. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| SizeName | The name of the body size to use to filter. If the input Size Name is empty, the output will be set to a name set from the Target Body's measurements. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| OutfitCollection | The outfit collection output, provided for convenience as a view into the outfit object metadata. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit?application_version=5.7#outputs)
