<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint?application_version=5.7 -->

# Aim Constraint

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
7. Aim Constraint

# Aim Constraint

Orients an item such that its aim axis points towards a global target.

On this page

### Description

Orients an item such that its aim axis points towards a global target.
Note: This node operates in global space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Lookat, Aim |
| Type | [FRigUnit\_AimConstraintLocalSpaceOffset](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraintLocalSpace-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The name of the item to apply aim | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |
| bMaintainOffset | Maintains the offset between child and weighted average of parents based on initial transforms | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | Filters the final rotation by axes based on the euler rotation order defined in the node's advanced settings If flipping is observed, try adjusting the rotation order | [Filter Option Per Axis](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FFilterOptionPerAxis) | (bX=True,bY=True,bZ=True) |
| AimAxis | Child is rotated so that its AimAxis points to the parents | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| UpAxis | Child is rotated around the AimAxis so that its UpAxis points to/Aligns with the WorldUp target | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| WorldUp | Defines how Child should rotate around the AimAxis. This is the aim target for the UpAxis | [Rig Unit Aim Constraint World Up](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraint_WorldUp) | (Target=(X=0.000000,Y=0.000000,Z=1.000000),Kind=Direction,Space=(Type=None,Name="")) |
| Parents | The array of parents to constaint this aim to | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings to use for the constraint | [Rig Unit Aim Constraint Advanced Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AimConstraint_AdvancedS-) | (DebugSettings=(bEnabled=False,Scale=10.000000,WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))),RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AimConstraint?application_version=5.7#inputs)
