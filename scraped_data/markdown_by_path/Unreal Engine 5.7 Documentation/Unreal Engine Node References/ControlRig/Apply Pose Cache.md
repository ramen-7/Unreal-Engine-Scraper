<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache?application_version=5.7 -->

# Apply Pose Cache

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
7. Apply Pose Cache

# Apply Pose Cache

Sets the hierarchy's pose

On this page

### Description

Sets the hierarchy's pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_HierarchySetPoseItemArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchySetPoseItemArr-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to apply to the hierarchy | [Rig Pose](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| ElementType | The types of element to apply the pose for | [Rig Element Type](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| Space | The space to use to apply the pose in | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| ItemsToSet | An optional collection to filter against | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| Weight | The weight to use when applying the transforms | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ApplyPoseCache?application_version=5.7#inputs)
