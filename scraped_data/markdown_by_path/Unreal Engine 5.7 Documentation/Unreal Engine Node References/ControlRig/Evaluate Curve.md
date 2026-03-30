<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve?application_version=5.7 -->

# Evaluate Curve

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
7. Evaluate Curve

# Evaluate Curve

Evaluates the provided curve. Values are normalized between 0 and 1

On this page

### Description

Evaluates the provided curve. Values are normalized between 0 and 1

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Animation |
| Tags | Curve,Profile |
| Type | [FRigVMFunction\_AnimEvalRichCurve](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_AnimEvalRichCurve) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input value to evaluate the curve at | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Curve | The curve to evaluate | [Runtime Float Curve](/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| SourceMinimum | The minimum range of the input value (typically 0.0) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| SourceMaximum | The maximum range of the input value (typically 1.0) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| TargetMinimum | The minimum range of the output | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| TargetMaximum | The maximum range of the output | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The evaluated value of the curve at the input value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateCurve?application_version=5.7#outputs)
