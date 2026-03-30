<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7 -->

# AccumulateMul

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
7. AccumulateMul

# AccumulateMul

2 nodes with name AccumulateMul

On this page

## AccumulateMul ()

Multiplies a value over time over and over again
Multiplies a vector over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateMul,Accumulate Mul (Float),Simulate,\*\*,Accumulate Mul (Vector) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Multiplier | The multiplier to apply for every iteration | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| InitialValue | The initial value to start at | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1.000000 |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## AccumulateMul ()

Multiplies a quaternion over time over and over again
Multiplies a transform over time over and over again

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Accumulate |
| Tags | AccumulateMul,Accumulate Mul (Quaternion),Simulate,\*\*,Accumulate Mul (Transform) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Multiplier | The multiplier to apply for every iteration | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| InitialValue | The initial value to start at | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| bFlipOrder | If True the multiplier will be pre-multiplied, otherwise post-multiplied | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIntegrateDeltaTime | If True the integration will be relying on the delta time to create more deterministic results with varying framerates. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting accumulated value | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [AccumulateMul ()](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#accumulatemul())
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#outputs)
* [AccumulateMul ()](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#accumulatemul()-2)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#information-2)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AccumulateMul?application_version=5.7#outputs-2)
