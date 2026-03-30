<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions?application_version=5.7 -->

# Basic IK Positions

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
7. Basic IK Positions

# Basic IK Positions

Solves the two bone IK given positions Note: This node operates in world space!

On this page

### Description

Solves the two bone IK given positions
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | TwoBone,IK |
| Type | [FRigUnit\_TwoBoneIKSimpleVectors](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_TwoBoneIKSimpleVectors) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Effector | The position of the effector | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Root | The position of the root of the triangle | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PoleVector | The position of the pole of the triangle | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bEnableStretch | If set to true the stretch feature of the solver will be enabled | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| StretchStartRatio | The ratio where the stretch starts | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| StretchMaximumRatio | The maximum allowed stretch ratio | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.250000 |
| BoneALength | The length of the first bone. If set to 0.0 it will be determined by the hierarchy | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| BoneBLength | The length of the second bone. If set to 0.0 it will be determined by the hierarchy | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Elbow | The resulting elbow position | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/BasicIKPositions?application_version=5.7#outputs)
