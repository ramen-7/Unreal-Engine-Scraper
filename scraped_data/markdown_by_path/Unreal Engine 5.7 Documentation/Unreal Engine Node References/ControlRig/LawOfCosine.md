<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine?application_version=5.7 -->

# LawOfCosine

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
7. LawOfCosine

# LawOfCosine

Computes the angles alpha, beta and gamma (in radians) between the three sides A, B and C

On this page

### Description

Computes the angles alpha, beta and gamma (in radians) between the three sides A, B and C

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | LawOfCosine,Law Of Cosine |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The length of the first edge of the triangle | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |
| B | The length of the second edge of the triangle | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |
| C | The length of the third edge of the triangle | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| AlphaAngle | The angle between B and C | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| BetaAngle | The angle between A and C | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| GammaAngle | The angle between A and B | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double |  |
| bValid | True if the results are valid | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/LawOfCosine?application_version=5.7#outputs)
