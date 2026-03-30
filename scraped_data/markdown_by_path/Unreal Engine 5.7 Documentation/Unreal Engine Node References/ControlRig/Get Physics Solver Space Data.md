<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData?application_version=5.7 -->

# Get Physics Solver Space Data

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
7. Get Physics Solver Space Data

# Get Physics Solver Space Data

Retrieves the simulation space data that were generated during the simulation step, so the values

On this page

### Description

Retrieves the simulation space data that were generated during the simulation step, so the values
returned will relate to the previous update if the solver has not yet been stepped.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Debug |
| Type | [FRigUnit\_GetPhysicsSolverSpaceData](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_GetPhysicsSolverSpaceDa-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver to relate this new physics element to | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| LinearVelocity | The velocity of the simulation space (in world space) | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularVelocity | The angular velocity of the simulation space (in world space) | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| LinearAcceleration | The linear acceleration of the simulation space (in world space) | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| AngularAcceleration | The angular acceleration of the simulation space (in world space) | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Gravity | The gravitational acceleration that will be applied (in simulation space) | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetPhysicsSolverSpaceData?application_version=5.7#outputs)
