<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK?application_version=5.7 -->

# Spring IK

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
7. Spring IK

# Spring IK

The Spring IK solver uses a verlet integrator to perform an IK solve.

On this page

### Description

The Spring IK solver uses a verlet integrator to perform an IK solve.
It support custom constraints including distance, length etc.
Note: This node operates in world space!

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | IK |
| Type | [FRigUnit\_SpringIK](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SpringIK) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StartBone | The name of the first bone to solve | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| EndBone | The name of the second bone to solve | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| HierarchyStrength | Sets the coefficient of the springs along the hierarchy. Values between 1 and 2048 are common. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 256.000000 |
| EffectorStrength | Sets the coefficient of the springs towards the effector. Values between 1 and 2048 are common. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| EffectorRatio | Defines the equilibrium of the effector springs. This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| RootStrength | Sets the coefficient of the springs towards the root. Values between 1 and 2048 are common. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| RootRatio | Defines the equilibrium of the root springs. This value ranges from 0.0 (zero distance) to 1.0 (distance in initial pose) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Damping | The higher the value to more quickly the simulation calms down. Values between 0.0001 and 0.75 are common. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.400000 |
| PoleVector | The polevector to use for the IK solver This can be a location or direction. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| bFlipPolePlane | If set to true the pole plane will be flipped | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| PoleVectorKind | The kind of pole vector this is representing - can be a direction or a location | [Control Rig Vector Kind](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/EControlRigVectorKind) | Direction |
| PoleVectorSpace | The space in which the pole vector is expressed | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| PrimaryAxis | The major axis being aligned - along the bone | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.000000,Z=0.000000) |
| SecondaryAxis | The minor axis being aligned - towards the pole vector | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=0.000000) |
| bLiveSimulation | If set to true simulation will continue for all intermediate bones over time. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Iterations | Drives how precise the solver operates. Values between 4 and 24 are common. This is only used if the simulation is not live (bLiveSimulation setting). | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| bLimitLocalPosition | If set to true bones are placed within the original distance of the previous local transform. This can be used to avoid stretch. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bPropagateToChildren | If set to true all of the global transforms of the children of this bone will be recalculated based on their local transforms. Note: This is computationally more expensive than turning it off. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DebugSettings | The debug setting for the node | [Rig Unit Spring IK Debug Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SpringIK_DebugSettings) | (bEnabled=False,Scale=1.000000,Color=(R=0.000000,G=0.000000,B=1.000000,A=1.000000),WorldOffset=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringIK?application_version=5.7#inputs)
