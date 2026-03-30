<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody?application_version=5.7 -->

# Spawn Physics Body

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
7. Spawn Physics Body

# Spawn Physics Body

Adds a new physics body as a component on the owner element.

On this page

### Description

Adds a new physics body as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Body,Skeleton |
| Type | [FRigUnit\_AddPhysicsBody](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsBody) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Solver | The solver to relate this new physics body should be added to | [Rig Physics Body Solver Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodySolverSettings) | (PhysicsSolverComponentKey=(ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver"),bUseAutomaticSolver=True,SourceBone=(Type=None,Name=""),TargetBone=(Type=None,Name=""),bIncludeInChecksForReset=True) |
| Dynamics | The dynamics properties of the new physics element | [Rig Physics Dynamics](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDynamics) | (Density=1.000000,MassOverride=1.000000,bOverrideCentreOfMass=False,CentreOfMassOverride=(X=0.000000,Y=0.000000,Z=0.000000),CentreOfMassNudge=(X=0.000000,Y=0.000000,Z=0.000000),bOverrideMomentsOfInertia=False,MomentsOfInertiaOverride=(X=1.000000,Y=1.000000,Z=1.000000),LinearDamping=0.000000,AngularDamping=0.000000) |
| Collision | The collision properties of the new physics element | [Rig Physics Collision](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsCollision) | (Boxes=,Spheres=,Capsules=,Material=(Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply)) |
| BodyData | The runtime modifiable data | [Physics Control Modifier Data](/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlModifierData) | (MovementType=Simulated,CollisionType=QueryAndPhysics,KinematicTargetSpace=OffsetInBoneSpace,GravityMultiplier=1.000000,PhysicsBlendWeight=1.000000,bUpdateKinematicFromSimulation=True) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body component key that was created | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsBody?application_version=5.7#outputs)
