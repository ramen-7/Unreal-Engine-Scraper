<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData?application_version=5.7 -->

# Make Drive Data

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
7. Make Drive Data

# Make Drive Data

Helper to simplify creation of drive data

On this page

### Description

Helper to simplify creation of drive data

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeDriveData](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeDriveData) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bEnableLinearDrive | Whether to enable the linear drive (not normally used for character joints) | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| LinearStrength | The strength used to drive linear motion | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| LinearDampingRatio | The amount of damping associated with the linear strength. A value of 1 Results in critically damped motion where the control drives as quickly as possible to the target without overshooting. Values > 1 result in more damped motion, and values below 1 result in faster, but more "wobbly" motion. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| LinearExtraDamping | The amount of additional linear damping. This is added to the damping that comes from LinearDampingRatio and can be useful when you want damping even when LinearStrength is zero. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bEnableAngularDrive | Whether to enable the angular drive | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AngularDriveMode | The type of drive. Note that SLERP drives don't work if any axis is locked | [Angular Drive Mode](/documentation/en-us/unreal-engine/API/Runtime/Engine/EAngularDriveMode__Type) | SLERP |
| AngularStrength | The strength used to drive angular motion | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| AngularDampingRatio | The amount of damping associated with the angular strength. A value of 1 Results in critically damped motion where the control drives as quickly as possible to the target without overshooting. Values > 1 result in more damped motion, and values below 1 result in faster, but more "wobbly" motion. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| AngularExtraDamping | The amount of additional angular damping. This is added to the damping that comes from AngularDampingRatio and can be useful when you want damping even when AngularStrength is zero. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SkeletalAnimationVelocityMultiplier | The amount of skeletal animation velocity to use in the targets | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DriveData | The drive data, representing the properties specified here, that can be set on a Physics Joint | [Rig Physics Drive Data](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeDriveData?application_version=5.7#outputs)
