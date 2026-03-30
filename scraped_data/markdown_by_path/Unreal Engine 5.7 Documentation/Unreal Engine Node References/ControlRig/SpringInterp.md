<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp?application_version=5.7 -->

# SpringInterp

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
7. SpringInterp

# SpringInterp

Uses a simple spring model to interpolate a float from Current to Target.

On this page

### Description

Uses a simple spring model to interpolate a float from Current to Target.
Uses a simple spring model to interpolate a vector from Current to Target.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation|Springs |
| Tags | SpringInterp,Spring Interpolate,Alpha,SpringInterpolate,Verlet |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | Rest/target position of the spring. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Strength | The spring strength determines how hard it will pull towards the target. The value is the frequency at which it will oscillate when there is no damping. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| CriticalDamping | The amount of damping in the spring. Set it smaller than 1 to make the spring oscillate before stabilizing on the target. Set it equal to 1 to reach the target without overshooting. Set it higher than one to make the spring take longer to reach the target. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Force | Extra force to apply (since the mass is 1, this is also the acceleration). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| bUseCurrentInput | If true, then the Current input will be used to initialize the state, and is required to be a variable that holds the current state. If false then the Target value will be used to initialize the state and the Current input will be ignored/unnecessary as a state will be maintained by this node. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Current | Current position of the spring. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| TargetVelocityAmount | The amount that the velocity should be passed through to the spring. A value of 1 will result in more responsive output, but if the input is noisy or has step changes, these discontinuities will be passed through to the output much more than if a smaller value such as 0 is used. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bInitializeFromTarget | If true, then the initial value will be taken from the target value, and not from the current value. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | New position of the spring after delta time. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Velocity | The resulting velocity of this spring | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpringInterp?application_version=5.7#outputs)
