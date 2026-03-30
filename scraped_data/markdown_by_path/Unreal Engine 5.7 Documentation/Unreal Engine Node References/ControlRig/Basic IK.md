<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK?application_version=5.7 -->

# Basic IK

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
7. Basic IK

# Basic IK

Solves the two bone IK given two bones. Note: This node operates in world space!

On this page

### Description

Solves the two bone IK given two bones.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwoBone,IK |
| Type | [FRigUnit\_TwoBoneIKSimplePerItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimplePerItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ItemA | The name of first item | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| ItemB | The name of second item | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| EffectorItem | The name of the effector item (if exists) | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Effector | The transform of the effector | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| PrimaryAxis | The major axis being aligned - along the item | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the polevector | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| SecondaryAxisWeight | Determines how much the secondary axis roll is being applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| PoleVector | The polevector to use for the IK solver This can be a location or direction. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| PoleVectorKind | The kind of pole vector this is representing - can be a direction or a location | [Control Rig Vector Kind](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigVectorKind) | Direction |
| PoleVectorSpace | The space in which the pole vector is expressed | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bEnableStretch | If set to true the stretch feature of the solver will be enabled | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchStartRatio | The ratio where the stretch starts | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| StretchMaximumRatio | The maximum allowed stretch ratio | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.250000 |
| Weight | The weight of the solver - how much the IK should be applied. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| ItemALength | The length of the first item. If set to 0.0 it will be determined by the hierarchy | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ItemBLength | The length of the second item. If set to 0.0 it will be determined by the hierarchy | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The settings for debug drawing | [Rig Unit Two Bone IKSimple Debug Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimple_DebugSe-) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIK?application_version=5.7#inputs)
