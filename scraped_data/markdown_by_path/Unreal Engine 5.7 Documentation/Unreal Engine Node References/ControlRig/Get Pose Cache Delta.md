<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta?application_version=5.7 -->

# Get Pose Cache Delta

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
7. Get Pose Cache Delta

# Get Pose Cache Delta

Compares two pose caches and compares their values.

On this page

### Description

Compares two pose caches and compares their values.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetDelta](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetDelta) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PoseA | The first pose to compare | [Rig Pose](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| PoseB | The second pose to compare | [Rig Pose](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| PositionThreshold | The delta threshold for a translation / position difference. 0.0 disables position differences. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| RotationThreshold | The delta threshold for a rotation difference (in degrees). 0.0 disables rotation differences. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ScaleThreshold | The delta threshold for a scale difference. 0.0 disables scale differences. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| CurveThreshold | The delta threshold for curve value difference. 0.0 disables curve differences. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ElementType | The type of elements to compare | [Rig Element Type](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigElementType) | All |
| Space | Defines in which space transform deltas should be computed | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| ItemsToCompare | An optional list of items to compare | [Rig Element Key Collection](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) | (Keys=) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PosesAreEqual | True if the poses A and B are equal | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| ItemsWithDelta | An array of items with a difference in them between poses A and B | [Rig Element Key Collection](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheDelta?application_version=5.7#outputs)
