<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp?application_version=5.7 -->

# AlphaInterp

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
7. AlphaInterp

# AlphaInterp

Takes in a float value and outputs an accumulated value with a customized scale and clamp

On this page

### Description

Takes in a float value and outputs an accumulated value with a customized scale and clamp
Takes in a vector value and outputs an accumulated value with a customized scale and clamp
Takes in a quaternion value and outputs an accumulated value with a customized scale and clamp

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Simulation|Time |
| Tags | AlphaInterp,Alpha Interpolate,Alpha,Lerp,LinearInterpolate |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to interpolate | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Scale | The scale to apply to the interpolation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Bias | The bias to use for the interpolation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| bMapRange | If True the input value will be mapped using the min and max range | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| InRange | The minimum and maximum for the input range | [Input Range](/documentation/en-us/unreal-engine/API/Runtime/Engine/FInputRange) | (Min=0.000000,Max=1.000000) |
| OutRange | The minimum and maximum for the output range | [Input Range](/documentation/en-us/unreal-engine/API/Runtime/Engine/FInputRange) | (Min=0.000000,Max=1.000000) |
| bClampResult | If True the output value will be clamped by the min and max | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| ClampMin | The minimum for the output's clamp range | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| ClampMax | The maximum for the output's clamp range | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bInterpResult | If True to the output result will be further intepolated | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| InterpSpeedIncreasing | The output interpolation increasing speed | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| InterpSpeedDecreasing | The output interpolation decreasing speed | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting interpolated value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AlphaInterp?application_version=5.7#outputs)
