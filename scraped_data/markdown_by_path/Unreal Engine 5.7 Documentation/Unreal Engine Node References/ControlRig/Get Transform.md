<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform?application_version=5.7 -->

# Get Transform

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
7. Get Transform

# Get Transform

GetTransform is used to retrieve a single transform from a hierarchy.

On this page

### Description

GetTransform is used to retrieve a single transform from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | GetBoneTransform,GetControlTransform,GetInitialTransform,GetSpaceTransform,GetTransform |
| Type | [FRigUnit\_GetTransform](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to retrieve the transform for | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |
| bInitial | Defines if the transform should be retrieved as current (false) or initial (true). Initial transforms for bones and other elements in the hierarchy represent the reference pose's value. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The current transform of the given item - or identity in case it wasn't found. | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetTransform?application_version=5.7#outputs)
