<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter?application_version=5.7 -->

# SetMuscleActivationParameter

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
6. [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow "Dataflow")
7. SetMuscleActivationParameter

# SetMuscleActivationParameter

SetMuscleActivationParameter (v1)

On this page

### Description

SetMuscleActivationParameter (v1)

Sets per-muscle parameters for custom muscle contraction.

Input(s) :
AnimationAsset - Use minimum muscle lengths across this animation asset to infer MuscleLengthRatioThresholdForMaxActivation
SkeletalMesh - Skeletal mesh used to linear blend skin kinematic origins and insertions.
This must be the same as the one used to create TransformSource group.
Check geometry spreadsheet for more info.

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetMuscleActivationParameterNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetMuscleActivationParameterNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ParameterMethod |  | [TEnumAsByte](/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EParameterMethod](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/EParameterMethod)> | Global |
| ApplyGlobalParameters | Click on this button to apply global parameters. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ContractionVolumeScale | Muscles gain volume during contraction if > 1. Volume-preserving if 1. Default: 1 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| GlobalFiberLengthRatioAtMaxActivation | How much muscle fibers shorten at max activation 1. A smaller value means more contraction in the fiber direction. Default: 0.5 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| GlobalMuscleLengthRatioThresholdForMaxActivation | Muscle length ratio (defined by origin-insertion distance) below this threshold is considered to reach max activation 1. Default: 0.75 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| GlobalInflationVolumeScale | Inflates muscle rest volume if > 1 and deflates muscle rest volume if < 1. Default: 1 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bUseLengthActivationCurve |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| GlobalLengthActivationCurve | Curve editor for muscle length-activation curve. Default: linear X-axis: normalized muscle length level from 0 (rest state) to 1 (muscle length ratio = Muscle Length Ratio Threshold For Max Activation) Y-axis: muscle activation from 0 to 1 | [FRuntimeFloatCurve](/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| ThresholdScalingPercent | This percentage (usually between 0 and 100%) globally scales minimum muscle lengths computed from the animation asset. For example, if minimum muscle length = 0.5 and ThresholdScalingPercent = 80%, the final MuscleLengthRatioThresholdForMaxActivation for this muscle is 1 - (1 - 0.5) \* 80% = 0.6 | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| ImportLowestMuscleLengthRatio | Click on this button to import the minimum muscle lengths across the animation asset as MuscleLengthRatioThresholdForMaxActivation | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ImportAllMuscleNames | Click on this button to import muscle bone names (in the Transform group) from the collection. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ResetToGlobalParameters | Click on this button to reset per-muscle parameters to global parameters. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ApplyCustomParameters | Click on this button to apply custom muscle parameters. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ParameterArray |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AnimationAsset | Use minimum muscle lengths across this animation asset to infer MuscleLengthRatioThresholdForMaxActivation | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UAnimSequence](/documentation/en-us/unreal-engine/API/Runtime/Engine/UAnimSequence)> | None |
| SkeletalMesh | Skeletal mesh used to linear blend skin kinematic origins and insertions. This must be the same as the one used to create TransformSource group. Check geometry spreadsheet for more info. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter?application_version=5.7#outputs)
