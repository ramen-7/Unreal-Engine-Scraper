<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch?application_version=5.7 -->

# Item Name Search

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
7. Item Name Search

# Item Name Search

Creates an item array based on a name search. The name search is case sensitive.

On this page

### Description

Creates an item array based on a name search.
The name search is case sensitive.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Tags | Bone,Joint,Collection,Filter |
| Type | [FRigUnit\_CollectionNameSearchArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionNameSearchArr-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PartialName | The partial name to look for | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| TypeToSearch | The type of elements to look for | [Rig Element Type](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting array of elements matching the filters | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ItemNameSearch?application_version=5.7#outputs)
