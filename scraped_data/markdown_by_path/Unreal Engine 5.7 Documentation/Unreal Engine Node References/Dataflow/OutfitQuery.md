<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery?application_version=5.7 -->

# OutfitQuery

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
7. OutfitQuery

# OutfitQuery

OutfitQuery (v1)

On this page

### Description

OutfitQuery (v1)

Query an Outfit about its properties.

Input(s) :
Outfit - Input/output collection (Output is always a passthrough)

Output(s):
Outfit [Passthrough] - Input/output collection (Output is always a passthrough)
bHasAnyValidPieces - Has this outfit any valid pieces?
bHasAnyValidBodySizes - Has this outfit any valid body sizes?

### Information

|  |  |
| --- | --- |
| Package | ChaosOutfitAssetDataflowNodes |
| Category | Outfit |
| Tags | Outfit Query |
| Type | FChaosOutfitAssetOutfitQueryNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bBodyPartMustExist | Check that body parts are present in the asset registry when checking for valid body sizes. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bMeasurementsMustExist | Check that measurements are valid when checking for valid body sizes. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bInterpolationDataMustExist | Check that some interpolation data exists when checking for valid body sizes. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input/output collection (Output is always a passthrough) | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Outfit | Input/output collection (Output is always a passthrough) | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UChaosOutfit](/documentation/en-us/unreal-engine/API/Plugins/ChaosOutfitAssetEngine/UChaosOutfit)> |  |
| bHasAnyValidPieces | Has this outfit any valid pieces? | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bHasAnyValidBodySizes | Has this outfit any valid body sizes? | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery?application_version=5.7#outputs)
