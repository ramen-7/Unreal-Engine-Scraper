<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint?application_version=5.7 -->

# Parent Constraint

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
7. Parent Constraint

# Parent Constraint

Constrains an item's transform to multiple items' transforms

On this page

### Description

Constrains an item's transform to multiple items' transforms

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Constraints |
| Tags | Parent,Orient,Scale |
| Type | [FRigUnit\_ParentConstraint](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraint) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to constrain | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| bMaintainOffset | If True the offset will be computed based on the current delta between each child and parent | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Filter | The filter to apply on the transform | [Transform Filter](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FTransformFilter) | (TranslationFilter=(bX=True,bY=True,bZ=True),RotationFilter=(bX=True,bY=True,bZ=True),ScaleFilter=(bX=True,bY=True,bZ=True)) |
| Parents | The array of parents to constrain the child to | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FConstraintParent](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FConstraintParent)> | (()) |
| AdvancedSettings | The advanced settings of the constraint operation | [Rig Unit Parent Constraint Advanced Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ParentConstraint_Advanc-) | (InterpolationType=Average,RotationOrderForFilter=XZY) |
| Weight | The weight to use when applying the resulting transform to the child | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ParentConstraint?application_version=5.7#inputs)
