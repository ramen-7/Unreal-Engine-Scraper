<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement?application_version=5.7 -->

# For Each Pose Cache Element

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
7. For Each Pose Cache Element

# For Each Pose Cache Element

Given a pose, execute iteratively across all items in the pose

On this page

### Description

Given a pose, execute iteratively across all items in the pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Collection,Loop,Iterate |
| Type | [FRigUnit\_PoseLoop](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseLoop) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to loop over | [Rig Pose](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item for the current pose entry | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |
| GlobalTransform | The global transform for the current pose entry | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| LocalTransform | The local transform for the current pose entry | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| CurveValue | The curve value for the current pose entry | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Index | The index of the current pose entry | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Count | The overall count of entries in the pose | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Ratio | Ranging from 0.0 (first item) and 1.0 (last item) This is useful to drive a consecutive node with a curve or an ease to distribute a value. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Completed | The branch to run when the loop has completed | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEachPoseCacheElement?application_version=5.7#outputs)
