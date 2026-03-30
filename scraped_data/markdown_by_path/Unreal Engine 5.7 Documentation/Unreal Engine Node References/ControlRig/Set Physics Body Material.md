<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial?application_version=5.7 -->

# Set Physics Body Material

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
7. Set Physics Body Material

# Set Physics Body Material

Applies the material settings to all the collision shapes

On this page

### Description

Applies the material settings to all the collision shapes

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_HierarchySetPhysicsBodyMaterial](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchySetPhysicsBody-_4) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsBodyComponentKey | The Physics Body to be updated | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsBody") |
| Material | The physics material to be used for collision on the Physics Body | [Rig Physics Material](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsMaterial) | (Friction=1.000000,Restitution=0.000000,FrictionCombineMode=Multiply,RestitutionCombineMode=Multiply) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetPhysicsBodyMaterial?application_version=5.7#inputs)
