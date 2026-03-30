<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices?application_version=5.7 -->

# Get Parent Indices

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
7. Get Parent Indices

# Get Parent Indices

Returns an array of relative parent indices for each item.

On this page

### Description

Returns an array of relative parent indices for each item. Several options here
a) If an item has multiple parents the major parent (based on the weights) will be returned.
b) If an item has a parent that's not part of the collection INDEX\_NONE will be returned.
c) If an item has a parent that's not part of the collection, but a grand parent is we'll use that index instead.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Items |
| Tags | Collection,Array |
| Type | [FRigUnit\_CollectionGetParentIndicesItemArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_CollectionGetParentIndi-_1) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The input array of items to retrieve the parent indices for | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ParentIndices | The resulting array of parent indices | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetParentIndices?application_version=5.7#outputs)
