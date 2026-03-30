<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim?application_version=5.7 -->

# Aim

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
7. Aim

# Aim

Aligns the rotation of a primary and secondary axis of an item to a global target.

On this page

### Description

Aligns the rotation of a primary and secondary axis of an item to a global target.
Note: This node operates in global space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | Lookat |
| Type | [FRigUnit\_AimItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The name of the item to align | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Primary | The primary target for the aim | [Rig Unit Aim Item Target](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=1.000000,Y=0.000000,Z=0.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Secondary | The secondary target for the aim - also referred to as PoleVector / UpVector | [Rig Unit Aim Item Target](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimItem_Target) | (Weight=1.000000,Axis=(X=0.000000,Y=0.000000,Z=1.000000),Target=(X=1.000000,Y=0.000000,Z=0.000000),Kind=Location,Space=(Type=Bone,Name="")) |
| Weight | The weight of the change - how much the change should be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| DebugSettings | The debug setting for the node | [Rig Unit Aim Bone Debug Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimBone_DebugSettings) | (bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Aim?application_version=5.7#inputs)
