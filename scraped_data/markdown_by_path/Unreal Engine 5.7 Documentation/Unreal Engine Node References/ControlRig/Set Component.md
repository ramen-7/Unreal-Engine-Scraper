<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent?application_version=5.7 -->

# Set Component

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
7. Set Component

# Set Component

Set the content of a component

On this page

### Description

Set the content of a component

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_SetComponentContent](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_SetComponentContent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Execute | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Key | The key of the component | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | () |
| Component | The actual component | [FRigPhysicsBodyComponent](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsBodyComponent),[FRigPhysicsControlComponent](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsControlComponent),[FRigPhysicsJointComponent](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsJointComponent),[FRigPhysicsSolverComponent](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigPhysicsSolverComponent) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Success | Returns true if the operation was successful. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetComponent?application_version=5.7#outputs)
