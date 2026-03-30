<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags?application_version=5.7 -->

# Filter Items by Tags

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
6. [ControlRig](/documentation/en-us/unreal-engine/node-reference/ControlRig "ControlRig")
7. Filter Items by Tags

# Filter Items by Tags

Filters an item array by a list of tags

On this page

### Description

Filters an item array by a list of tags

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata |
| Type | [FRigUnit\_FilterItemsByMetadataTags](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FilterItemsByMetadataTa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The items to filter | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Tags | The tags to find | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Inclusive | If set to true only items with ALL of tags will be returned, if set to false items with ANY of the tags will be removed | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The results of the filter | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/FilterItemsbyTags?application_version=5.7#outputs)
