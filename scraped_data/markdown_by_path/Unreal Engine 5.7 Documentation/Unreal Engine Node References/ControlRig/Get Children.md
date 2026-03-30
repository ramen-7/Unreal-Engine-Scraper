<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren?application_version=5.7 -->

# Get Children

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
7. Get Children

# Get Children

Creates an item array based on the direct or recursive children

On this page

### Description

Creates an item array based on the direct or recursive children
of a provided parent item. Returns an empty array for an invalid parent item.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Bone,Joint,Collection,Filter,Parent |
| Type | [FRigUnit\_CollectionChildrenArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionChildrenArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Parent | The parent to search the children for | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bIncludeParent | If True the parent will be included in the list of results | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bRecursive | If True children of children will be included | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bDefaultChildren | When true, it will return all children, regardless of whether the parent is active or not. When false, will return only the children which are influenced by this parent | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| TypeToSearch | The type of children to look for | [Rig Element Type](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting array of children | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetChildren?application_version=5.7#outputs)
