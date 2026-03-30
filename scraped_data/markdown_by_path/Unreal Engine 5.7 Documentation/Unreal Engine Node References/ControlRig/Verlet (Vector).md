<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector?application_version=5.7 -->

# Verlet (Vector)

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
7. Verlet (Vector)

# Verlet (Vector)

Simulates a single position over time using Verlet integration.

On this page

### Description

Simulates a single position over time using Verlet integration. It is recommended to use SpringInterp instead as it
is more accurate and stable, and has more meaningful parameters.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Springs |
| Tags | Simulate,Integrate |
| Type | [FRigVMFunction\_VerletIntegrateVector](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_VerletIntegrateVe-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | The target value to interpolate / integrate towards | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Strength | The strength of the verlet spring | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 64.000000 |
| Damp | The amount of damping to apply ( 0.0 to 1.0, but usually really low like 0.005 ) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.010000 |
| Blend | The amount of blending to apply per second | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |
| Force | The force feeding into the solver. Can be used for gravity. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Position | The resulting simulated position | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Velocity | The resulting simulated velocity | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Acceleration | The resulting simulated acceleration | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/VerletVector?application_version=5.7#outputs)
