<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData?application_version=5.7 -->

# Make Articulation Joint Data

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
7. Make Articulation Joint Data

# Make Articulation Joint Data

Helper to simplify creation of joint data for a typical articulation (i.e. locked linear motion, but with an angular limit)

On this page

### Description

Helper to simplify creation of joint data for a typical articulation (i.e. locked linear motion,
but with an angular limit)

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_MakeArticulationJointData](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_MakeArticulationJointDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AngularLimit | The angular limit in Degrees (twist, swing1, swing2) -ve indicates the limit range is free | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=-1.000000,Y=-1.000000,Z=-1.000000) |
| SoftStrength | If limited, then this will be used to control the softness of the limit -ve indicates the limit is hard A value of 1 is reasonably soft | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=-1.000000,Y=-1.000000,Z=-1.000000) |
| SoftDampingRatio | If limited, then this will be used to control the damping ratio of the limit | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| JointData | Joint data that can be used in a Physics Joint, calculated according to the values set here, and configured to act as a "normal" articulation joint. | [Rig Physics Joint Data](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeArticulationJointData?application_version=5.7#outputs)
