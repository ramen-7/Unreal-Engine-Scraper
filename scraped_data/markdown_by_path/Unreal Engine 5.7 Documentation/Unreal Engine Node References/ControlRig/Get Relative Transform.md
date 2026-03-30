<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform?application_version=5.7 -->

# Get Relative Transform

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
4. Get Relative Transform

# Get Relative Transform

GetRelativeTransform is used to retrieve a single transform from a hierarchy in the space of another transform

On this page

### Description

GetRelativeTransform is used to retrieve a single transform from a hierarchy in the space of another transform

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | Offset,Local |
| Type | [FRigUnit\_GetRelativeTransformForItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetRelativeTransformFor-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child item to retrieve the transform for | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bChildInitial | Defines if the child's transform should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Parent | The parent item to use. The child transform will be retrieve in the space of the parent. | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bParentInitial | Defines if the parent's transform should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RelativeTransform | The transform of the given child item relative to the provided parent | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetRelativeTransform?application_version=5.7#outputs)
