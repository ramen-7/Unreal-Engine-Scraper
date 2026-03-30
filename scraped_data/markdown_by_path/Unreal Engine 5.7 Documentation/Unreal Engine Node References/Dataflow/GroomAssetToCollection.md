<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection?application_version=5.7 -->

# GroomAssetToCollection

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
7. GroomAssetToCollection

# GroomAssetToCollection

GroomAssetToCollection (v1)

On this page

### Description

GroomAssetToCollection (v1)
Experimental

Transform a groom asset to a collection

Input(s) :
GroomAsset - Input asset to read the guides from
CurvesType - Type of curves to use to fill the groom collection (guides/strands)
CurvesThickness - Curves thickness for geometry generation

Output(s):
Collection - Managed array collection used to store the curves

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGroomAssetToCollectionDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGroomAssetToCollectionDataflowN-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroomAsset | Input asset to read the guides from | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGroomAsset](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsCore/UGroomAsset)> | None |
| CurvesThickness | Curves thickness for geometry generation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| CurvesType | Type of curves to use to fill the groom collection (guides/strands) | [EGroomCollectionType](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/EGroomCollectionType) | Guides |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection used to store the curves | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection?application_version=5.7#outputs)
