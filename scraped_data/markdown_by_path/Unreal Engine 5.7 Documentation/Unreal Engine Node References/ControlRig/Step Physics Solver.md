<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver?application_version=5.7 -->

# Step Physics Solver

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
7. Step Physics Solver

# Step Physics Solver

Steps the specified physics solver

On this page

### Description

Steps the specified physics solver

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Simulate |
| Type | [FRigUnit\_StepPhysicsSolver](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_StepPhysicsSolver) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The physics solver that should be stepped | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| DeltaTimeOverride | If this is zero, then the execute context time will be used. If this is positive then it will override the delta time. A negative value will prevent the solver from stepping, but there will still be update costs associated with the node. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SimulationSpaceDeltaTimeOverride | If this is zero, then the simulation delta time will be used for evaluating movement of the simulation space. If this is positive then it will override. This may be needed if the component movement is being done in parallel, in which case you might need to pass in the previous time delta here. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Alpha | How much of the simulation is combined with the input bone. This currently happens in component space. Note that the simulation will continue to run, even if alpha = 0 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| VisualizationSettings | Settings that specify how the solver state should be visualized during/after the step | [Rig Physics Visualization Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsVisualizationSettings) | (bEnableVisualization=True,LineThickness=1.000000,ShapeSize=1,ShapeDetail=16,bShowBodies=True,bShowCentreOfMass=False,bShowJoints=True,bShowControls=False,bShowWorldObjects=True,bShowWorldOverlapBox=False,bShowActiveContacts=True,bShowInactiveContacts=False) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/StepPhysicsSolver?application_version=5.7#inputs)
