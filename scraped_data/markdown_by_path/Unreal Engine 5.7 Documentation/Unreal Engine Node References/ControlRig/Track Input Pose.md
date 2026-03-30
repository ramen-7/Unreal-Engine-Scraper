<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose?application_version=5.7 -->

# Track Input Pose

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
7. Track Input Pose

# Track Input Pose

Forces tracking of the input animation (on all physics bodies) for the next N frames

On this page

### Description

Forces tracking of the input animation (on all physics bodies) for the next N frames

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Reset,Simulate |
| Type | [FRigUnit\_TrackInputPose](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_TrackInputPose) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver to relate this new physics element to | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| NumberOfFrames | The number of frames to track the input pose for | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| bForceNumberOfFrames | If true, then the number will be forced, potentially reducing the number. If false, then the NumberOfFrames will only be used to increase the number of frames remaining. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TrackInputPose?application_version=5.7#inputs)
