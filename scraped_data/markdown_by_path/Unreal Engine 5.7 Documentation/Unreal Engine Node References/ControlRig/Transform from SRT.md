<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT?application_version=5.7 -->

# Transform from SRT

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
7. Transform from SRT

# Transform from SRT

Composes a Transform (and Euler Transform) from its components.

On this page

### Description

Composes a Transform (and Euler Transform) from its components.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Transform |
| Tags | EulerTransform,Scale,Rotation,Orientation,Translation,Location |
| Type | [FRigVMFunction\_MathTransformFromSRT](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathTransformFrom-_2) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Location | The location for the desired transform | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Rotation | The euler angles in degrees for the desired transform | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RotationOrder | The rotation order to interpret the euler angles by | [Euler Rotation Order](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | XYZ |
| Scale | The scale for the desired transform | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The result as a transform | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| EulerTransform | The result as a euler transform | [Euler Transform](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformfromSRT?application_version=5.7#outputs)
