<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath?application_version=5.7 -->

# Parent Constraint Math

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
7. Parent Constraint Math

# Parent Constraint Math

Computes the output transform by constraining the input transform to multiple parents

On this page

### Description

Computes the output transform by constraining the input transform to multiple parents

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orient,Scale |
| Type | [FRigUnit\_ParentConstraintMath](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraintMath) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Input | Input is used to calculate offsets from parents' initial transform | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Parents | The array of parents to compute the constrained transform for | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings to use for the constraint compute | [Rig Unit Parent Constraint Math Advanced Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraintMath_Ad-) | (InterpolationType=Average) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Output | The resulting constrained transform | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraintMath?application_version=5.7#outputs)
