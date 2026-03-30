<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute?application_version=5.7 -->

# Attribute

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
7. Attribute

# Attribute

Attribute (v2) Experimental Create a new attribute for the specified group.

On this page

### Description

Attribute (v2)
Experimental

Create a new attribute for the specified group.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Attribute |
| Type | [FChaosClothAssetAttributeNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetAttributeNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the attribute to create. | [FChaosClothAssetConnectableIOStringValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIOStr-) | (StringValue="") |
| Group | The attribute group. | [FChaosClothAssetNodeAttributeGroup](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeAttributeGro-) | (Name="") |
| Type | The attribute type. | [EChaosClothAssetNodeAttributeType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetNodeAttributeTyp-) | Integer |
| IntValue | Default integer value. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| FloatValue | Default float value. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| VectorValue | Default vector value. | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Name.StringValue | The value for this property. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute?application_version=5.7#outputs)
