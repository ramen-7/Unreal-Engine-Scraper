<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal?application_version=5.7 -->

# CurveSamplingAnimationAssetTerminal

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
7. CurveSamplingAnimationAssetTerminal

# CurveSamplingAnimationAssetTerminal

CurveSamplingAnimationAssetTerminal (v1)

On this page

### Description

CurveSamplingAnimationAssetTerminal (v1)

* terminal node to create an animation asset for muscle activation MLD training.
* The animation remains in the rest pose with the curves spiking from 0 to 1 to 0 in each block of frames (Number of frames per muscle)
* Curves will stay at value 0 most of the time. Only one curve is active at a time.
* Total animation frames = Frame Rate \* Number of frames per muscle

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Terminal |
| Type | [FCurveSamplingAnimationAssetTerminalNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FCurveSamplingAnimationAssetTerm-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FrameRate | Frame rate of the animation | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 30 |
| NumFramesPerMuscle | Number of frames created for each curve. Within this window of frames, curve value will go from 0 to 1 to 0. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMeshAsset |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| AnimationAsset |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UAnimSequence](/documentation/en-us/unreal-engine/API/Runtime/Engine/UAnimSequence)> | None |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal?application_version=5.7#inputs)
