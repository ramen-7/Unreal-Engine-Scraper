<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK?application_version=5.7 -->

# Basic FABRIK

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
7. Basic FABRIK

# Basic FABRIK

The FABRIK solver can solve N-Bone chains using

On this page

### Description

The FABRIK solver can solve N-Bone chains using
the Forward and Backward Reaching Inverse Kinematics algorithm.
For now this node supports single effector chains only.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | N-Bone,IK |
| Type | [FRigUnit\_FABRIKItemArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_FABRIKItemArray) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The chain to use | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| EffectorTransform | The transform of the effector in global space | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Precision | The precision to use for the fabrik solver | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Weight | The weight of the solver - how much the IK should be applied. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| MaxIterations | The maximum number of iterations. Values between 4 and 16 are common. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| bSetEffectorTransform | The option to set the effector transform | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicFABRIK?application_version=5.7#inputs)
