<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve?application_version=5.7 -->

# Get Pose Cache Curve

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
7. Get Pose Cache Curve

# Get Pose Cache Curve

Returns the hierarchy's pose curve value

On this page

### Description

Returns the hierarchy's pose curve value

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Pose Cache |
| Tags | Hierarchy,Pose,State |
| Type | [FRigUnit\_PoseGetCurve](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_PoseGetCurve) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pose | The pose to retrieve the curve value from | [Rig Pose](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigPose) | (Elements=,HierarchyTopologyVersion=-1,PoseHash=-1) |
| Curve | The name of the curve to retrieve | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Valid | True if the curve value has been retrieved successfully | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| CurveValue | The resulting curve value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPoseCacheCurve?application_version=5.7#outputs)
