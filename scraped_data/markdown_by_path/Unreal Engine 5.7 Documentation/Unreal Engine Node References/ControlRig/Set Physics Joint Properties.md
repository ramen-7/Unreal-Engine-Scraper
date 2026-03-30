<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties?application_version=5.7 -->

# Set Physics Joint Properties

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
7. Set Physics Joint Properties

# Set Physics Joint Properties

Sets the joint data for a physics joint component

On this page

### Description

Sets the joint data for a physics joint component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetJointData](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetJointData) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsJointComponentKey | The Physics Joint to be updated | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsJoint") |
| JointData | The physics joint data (limit and drive properties) to be used | [Rig Physics Joint Data](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointData) | (bEnabled=True,bAutoCalculateParentOffset=True,ExtraParentOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),bAutoCalculateChildOffset=True,ExtraChildOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)),LinearConstraint=(Limit=0.000000,XMotion=LCM\_Locked,YMotion=LCM\_Locked,ZMotion=LCM\_Locked,Stiffness=0.000000,Damping=0.000000,Restitution=0.000000,ContactDistance=5.000000,bSoftConstraint=False),ConeConstraint=(Swing1LimitDegrees=45.000000,Swing2LimitDegrees=45.000000,Swing1Motion=ACM\_Free,Swing2Motion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),TwistConstraint=(TwistLimitDegrees=45.000000,TwistMotion=ACM\_Free,Stiffness=50.000000,Damping=5.000000,Restitution=0.000000,ContactDistance=1.000000,bSoftConstraint=True),bDisableCollision=True,LinearProjectionAmount=0.500000,AngularProjectionAmount=0.000000,ParentInverseMassScale=1.000000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsJointProperties?application_version=5.7#inputs)
