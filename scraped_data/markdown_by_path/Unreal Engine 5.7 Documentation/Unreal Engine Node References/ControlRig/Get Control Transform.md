<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform?application_version=5.7 -->

# Get Control Transform

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
7. Get Control Transform

# Get Control Transform

GetControlTransform is used to retrieve a single transform from a hierarchy.

On this page

### Description

GetControlTransform is used to retrieve a single transform from a hierarchy.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Controls |
| Tags | GetControlTransform |
| Type | [FRigUnit\_GetControlTransform](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_GetControlTransform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The name of the Control to retrieve the transform for. | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Space | Defines if the Control's transform should be retrieved in local or global space. | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The current value of the control. | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Minimum | The minimum value of the control. | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Maximum | The maximum value of the control. | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetControlTransform?application_version=5.7#outputs)
