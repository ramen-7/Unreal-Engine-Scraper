<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath?application_version=5.7 -->

# Aim Math

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
7. Aim Math

# Aim Math

Outputs an aligned transform of a primary and secondary axis of an input transform to a world target.

On this page

### Description

Outputs an aligned transform of a primary and secondary axis of an input transform to a world target.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Lookat |
| Type | [FRigUnit\_AimBoneMath](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBoneMath) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InputTransform | The transform (in global space) before the aim was applied (optional) | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Primary | The primary target for the aim | [Rig Unit Aim Item Target](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=1.000000,Y=0.000000,Z=0.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Secondary | The secondary target for the aim - also referred to as PoleVector / UpVector | [Rig Unit Aim Item Target](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=0.000000,Y=0.000000,Z=1.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Weight | The weight of the change - how much the change should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugSettings | The debug setting for the node | [Rig Unit Aim Bone Debug Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBone_DebugSettings) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transform | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimMath?application_version=5.7#outputs)
