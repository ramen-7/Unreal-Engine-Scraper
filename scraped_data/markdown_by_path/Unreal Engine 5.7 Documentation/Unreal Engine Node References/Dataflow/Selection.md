<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection?application_version=5.7 -->

# Selection

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
7. Selection

# Selection

Selection (v2)

On this page

### Description

Selection (v2)

Chaos Cloth Asset Selection Node V 2

Input(s) :
TransferCollection - The collection used to transfer sets from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Selection |
| Type | [FChaosClothAssetSelectionNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetSelectionNode_v2) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| OutputName | The name to be use as a selection. | [FChaosClothAssetConnectableOStringValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableOStri-) | (StringValue="") |
| InputName | The name to populate this set from and override based on Selection Override Type. Output Name will be used if Input Name is empty. | [FChaosClothAssetConnectableIStringValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="",bBuildFabricMaps=False) |
| SelectionOverrideType | How to apply this node's Indices onto existing sets. Changing this value will change the output set. To change how the node's stored indices are calculated, change the equivalent value on the Selection Tool context. | [EChaosClothAssetSelectionOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetSelectionOverrid-) | ReplaceAll |
| Group | The type of element the selection refers to | [FChaosClothAssetNodeSelectionGroup](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetNodeSelectionGro-) | (Name="") |
| Indices | Selected element indices | [TSet](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | () |
| RemoveIndices | Indices to remove from the Input selection | [TSet](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | () |
| Import | Import (replace) the current selection from the input Collection's selection with the given Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportSecondary | Import (replace) the current selection from the input Collection's secondary selection with the given Input Name (or Output Name if Input Name is empty). Secondary selections are only supported in v1 of this node. This function is provided as a migration tool to this current version. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| SimTransferType | The type of transfer used to transfer the sim mesh sets when a TransferCollection is connected. This property is disabled when no TransferCollection input has been connected. | [EChaosClothAssetWeightMapTransferType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetWeightMapTransfe-) | Use2DSimMesh |
| TransferSelectionThreshold | Selections are internally converted to maps in order to do the transfer and then converted back. This value is used to do the conversion back. Decrease this value to (possibly) expand the converted selection. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.950000 |
| Transfer | Transfer the selection from the connected Transfer Collection containing a selection with Input Name (or Output Name if Input Name is empty). | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransferCollection | The collection used to transfer sets from. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| OutputName.StringValue | The value for this property. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection?application_version=5.7#outputs)
