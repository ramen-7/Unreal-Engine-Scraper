<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform?application_version=5.7 -->

# Offset Transform

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
7. Offset Transform

# Offset Transform

Offset Transform is used to add an offset to an existing transform in the hierarchy.

On this page

### Description

Offset Transform is used to add an offset to an existing transform in the hierarchy. The offset is post multiplied.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Transforms |
| Tags | Offset,Relative,AddBoneTransform |
| Type | [FRigUnit\_OffsetTransformForItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_OffsetTransformForItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to offset the transform for | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| OffsetTransform | The transform of the item relative to its previous transform | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Weight | Defines how much the change will be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bPropagateToChildren | If set to true children of affected items in the hierarchy will follow the transform change - otherwise only the parent will move. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/OffsetTransform?application_version=5.7#inputs)
