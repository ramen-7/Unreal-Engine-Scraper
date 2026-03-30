<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics?application_version=5.7 -->

# Instantiate physics

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
7. Instantiate physics

# Instantiate physics

Instantiates all the objects in the physics world.

On this page

### Description

Instantiates all the objects in the physics world. Some properties can't be modified after this happens.
Note that it will happen automatically during the first simulation step if it hasn't been explicitly
requested. Explicit instantiation allows the timing to be controlled, as allocations etc may cause some
delays.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Physics |
| Type | [FRigUnit\_InstantiatePhysics](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_InstantiatePhysics) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | The solver that should be instantiated | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Instantiatephysics?application_version=5.7#inputs)
