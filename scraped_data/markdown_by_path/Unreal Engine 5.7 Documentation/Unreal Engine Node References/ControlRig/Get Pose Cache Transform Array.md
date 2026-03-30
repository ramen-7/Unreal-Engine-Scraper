<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray?application_version=5.7 -->

# Get Pose Cache Transform Array

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
4. Get Pose Cache Transform Array

# Get Pose Cache Transform Array

Returns an array of transforms from a given hierarchy pose

On this page

### Description

Returns an array of transforms from a given hierarchy pose

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetTransformArray](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetTransformArray) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the transform from | [Rig Pose](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| Space | Defines if the transform should be retrieved in local or global space | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | GlobalSpace |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | True if the transforms has been retrieved successfully | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Transforms | The resulting array of transforms | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheTransformArray?application_version=5.7#outputs)
