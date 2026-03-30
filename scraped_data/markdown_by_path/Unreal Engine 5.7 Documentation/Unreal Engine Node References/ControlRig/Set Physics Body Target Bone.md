<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone?application_version=5.7 -->

# Set Physics Body Target Bone

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
7. Set Physics Body Target Bone

# Set Physics Body Target Bone

Sets what bone is targeted by the simulation - i.e. where the simulation output is written to.

On this page

### Description

Sets what bone is targeted by the simulation - i.e. where the simulation output is written to.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyTargetBone](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_9) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| TargetBone | The bone to use as a target for the Physics Body - i.e. where its transforms should be written to. | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyTargetBone?application_version=5.7#inputs)
