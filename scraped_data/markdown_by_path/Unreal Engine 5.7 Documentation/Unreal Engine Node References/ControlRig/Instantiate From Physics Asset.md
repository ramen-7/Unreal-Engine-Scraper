<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset?application_version=5.7 -->

# Instantiate From Physics Asset

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
7. Instantiate From Physics Asset

# Instantiate From Physics Asset

Creates multiple physics components based on the supplied physics asset.

On this page

### Description

Creates multiple physics components based on the supplied physics asset.
Note that the resulting simulation bodies may not precisely match the physics asset.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New |
| Type | [FRigUnit\_HierarchyInstantiateFromPhysicsAsset](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyInstantiateFro-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | Note that setting the solver component, if known, has the benefit of avoiding the need to search for an automatic solver. | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| bUseAutomaticSolver | If true (and the physics solver is not explicitly set), then this component will be added to any physics solver that exists above it in the hierarchy, if that solver allows automatically adding physics components. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PhysicsAsset | The Physics Asset to instantiate from | Physics Asset | None |
| ConstraintProfileName | Name of the constraint profile to use. If empty (or invalid), the default profile will be used | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| BonesToUse | If this is empty, then all bodies in the physics asset that match a bone in the hierarchy will be created. Otherwise only bodies that relate to the specified bones will be created. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> | () |
| bEnableJoints | Whether to enable the joints authored in the physics asset. Note that you can't have drives without joints. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bEnableDrives | Whether to enable the drives authored in the physics asset. Note that if you are creating parent space controls, you may not want the drives | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bAddSimSpaceControl | Whether to create a simulation-space control for each body that was created | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bAddParentSpaceControl | Whether to create a parent-space control for each body that was created. Note that if this is set to true, then it will be created for the root-most body in the physics asset too. This is often not needed, so make sure it isn't enabled if you don't want it to be. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SimSpaceControlData | Data for the simulation space control | [Physics Control Data](/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |
| ParentSpaceControlData | Data for the parent space control | [Physics Control Data](/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKeys | The Physics Body component keys that were created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
| PhysicsJointComponentKeys | The Physics Joint component keys that were created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
| SimSpaceControlComponentKeys | The simulation-space Physics Control component keys that were created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |
| ParentSpaceControlComponentKeys | The parent-space Physics Control component keys that were created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/InstantiateFromPhysicsAsset?application_version=5.7#outputs)
