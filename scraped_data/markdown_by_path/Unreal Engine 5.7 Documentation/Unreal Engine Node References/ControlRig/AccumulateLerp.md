<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp?application_version=5.7 -->

# AccumulateLerp

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
7. AccumulateLerp

# AccumulateLerp

Interpolates two values over time over and over again

On this page

### Description

Interpolates two values over time over and over again
Interpolates two vectors over time over and over again
Interpolates two quaternions over time over and over again
Interpolates two transforms over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateLerp,Accumulate Lerp (Float),Simulate,Ramp,Accumulate Lerp (Vector),Accumulate Lerp (Quaternion),Accumulate Lerp (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetValue | The target value to interpolate towards | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| InitialValue | The initial value to start at | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Blend | The blend to use for the interpolation. This value may be scaled down based on the Integrate Delta Time setting | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateLerp?application_version=5.7#outputs)
