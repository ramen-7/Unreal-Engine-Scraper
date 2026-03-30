<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation?application_version=5.7 -->

# Set Physics Body Update Kinematic From Simulation

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
7. Set Physics Body Update Kinematic From Simulation

# Set Physics Body Update Kinematic From Simulation

If true, then kinematic objects will be written back from simulation to the bones.

On this page

### Description

If true, then kinematic objects will be written back from simulation to the bones. This only
necessary when either kinematic targets are being used, or when the target bone differs from the source bone.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyUpdateKinematicFromSimulation](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_Hierarc-_2) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| bUpdateKinematicFromSimulation | When bodies are written back from simulation, if this is set to false, there is a small performance benefit to skipping bodies that are known to be kinematic, and when they are set to just track the input animation. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyUpdateKinematicFromSimulation?application_version=5.7#inputs)
