<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl?application_version=5.7 -->

# Spawn Physics Control

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
7. Spawn Physics Control

# Spawn Physics Control

Adds a new physics control as a component on the owner element.

On this page

### Description

Adds a new physics control as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Control |
| Type | [FRigUnit\_AddPhysicsControl](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsControl) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| ParentBodyComponentKey | The optional body that "does" the controlling - though if it is dynamic then it can move too | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| bUseParentBodyAsDefault | Whether or not to use the parent body (if one exists) as the Physics Control parent | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ChildBodyComponentKey | The body that is controlled | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| ControlData | Describes the initial strength etc of the new control | [Physics Control Data](/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlData) | (bEnabled=True,LinearStrength=0.000000,LinearDampingRatio=1.000000,LinearExtraDamping=0.000000,MaxForce=0.000000,AngularStrength=0.000000,AngularDampingRatio=1.000000,AngularExtraDamping=0.000000,MaxTorque=0.000000,LinearTargetVelocityMultiplier=1.000000,AngularTargetVelocityMultiplier=1.000000,CustomControlPoint=(X=0.000000,Y=0.000000,Z=0.000000),bUseCustomControlPoint=False,bUseSkeletalAnimation=True,bDisableCollision=False,bOnlyControlChildObject=False) |
| ControlMultiplier | Fine control over the control strengths etc | [Physics Control Multiplier](/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlMultiplier) | (LinearStrengthMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearDampingRatioMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),LinearExtraDampingMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),MaxForceMultiplier=(X=1.000000,Y=1.000000,Z=1.000000),AngularStrengthMultiplier=1.000000,AngularDampingRatioMultiplier=1.000000,AngularExtraDampingMultiplier=1.000000,MaxTorqueMultiplier=1.000000) |
| ControlTarget | The initial target for the new control | [Physics Control Target](/documentation/en-us/unreal-engine/API/Plugins/PhysicsControl/FPhysicsControlTarget) | (TargetPosition=(X=0.000000,Y=0.000000,Z=0.000000),TargetVelocity=(X=0.000000,Y=0.000000,Z=0.000000),TargetOrientation=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),TargetAngularVelocity=(X=0.000000,Y=0.000000,Z=0.000000),bApplyControlPointToTarget=False) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ControlComponentKey | The Physics Control component key that was created | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsControl?application_version=5.7#outputs)
