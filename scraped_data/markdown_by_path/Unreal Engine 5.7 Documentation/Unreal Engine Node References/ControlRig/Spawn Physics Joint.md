<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint?application_version=5.7 -->

# Spawn Physics Joint

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
7. Spawn Physics Joint

# Spawn Physics Joint

Adds a new Physics Joint as a component on the owner element.

On this page

### Description

Adds a new Physics Joint as a component on the owner element.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Add,Construction,Create,New,Joint,Articulation,Constraint,Skeleton |
| Type | [FRigUnit\_AddPhysicsJoint](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_AddPhysicsJoint) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Owner | The owner of the newly created component (must be set/valid) | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| ParentBodyComponentKey | The parent body of the joint. If unset, then the system will try to find a suitable body by looking for a parent that contains a body that is in the same solver as the child body. | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| ChildBodyComponentKey | The child body of the joint. If unset, then the system will try to find a suitable body | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| JointData | The properties of the joint | [Rig Physics Joint Data](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) | (bEnabled=True,bAutoCalculateParentOffset=True,ExtraParentOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),bAutoCalculateChildOffset=True,ExtraChildOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),LinearConstraint=(Limit=0.000000,XMotion=LCM\_Locked,YMotion=LCM\_Locked,ZMotion=LCM\_Locked,Stiffness=0.000000,Damping=0.000000,Restitution=0.000000,ContactDistance=5.000000,bSoftConstraint=False),ConeConstraint=(Swing1LimitDegrees=45.000000,Swing2LimitDegrees=45.000000,Swing1Motion=ACM\_Free,Swing2Motion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),TwistConstraint=(TwistLimitDegrees=45.000000,TwistMotion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),bDisableCollision=True,LinearProjectionAmount=0.500000,AngularProjectionAmount=0.000000,ParentInverseMassScale=1.000000) |
| DriveData | Optional motor/drive associated with the physics joint | [Rig Physics Drive Data](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsDriveData) | (LinearDriveConstraint=(PositionTarget=(X=0.000000,Y=0.000000,Z=0.000000),VelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),XDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),YDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),ZDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),bAccelerationMode=True),AngularDriveConstraint=(TwistDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SwingDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),SlerpDrive=(Stiffness=50.000000,Damping=1.000000,MaxForce=0.000000,bEnablePositionDrive=False,bEnableVelocityDrive=False),OrientationTarget=(Pitch=0.000000,Yaw=0.000000,Roll=0.000000),AngularVelocityTarget=(X=0.000000,Y=0.000000,Z=0.000000),AngularDriveMode=SLERP,bAccelerationMode=True),bUseSkeletalAnimation=True,SkeletalAnimationVelocityMultiplier=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint component key that was created | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnPhysicsJoint?application_version=5.7#outputs)
