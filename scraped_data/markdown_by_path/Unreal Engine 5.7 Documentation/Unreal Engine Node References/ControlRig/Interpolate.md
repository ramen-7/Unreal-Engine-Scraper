<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate?application_version=5.7 -->

# Interpolate

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
7. Interpolate

# Interpolate

Linearly interpolates between A and B using the ratio T

On this page

### Description

Linearly interpolates between A and B using the ratio T
Performs a spherical interpolation of the quaternions A and B based on the blend value T.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Interpolate,Lerp,Mix,Blend,Slerp,SphericalInterpolate |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first color to interpolate from | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| B | The second color to interpolate to | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |
| T | The blend value for the interpolation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting interpolated color | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Interpolate?application_version=5.7#outputs)
