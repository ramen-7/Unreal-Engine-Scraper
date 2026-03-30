<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform?application_version=5.7 -->

# Evaluate Live Link Frame (Transform)

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
7. Evaluate Live Link Frame (Transform)

# Evaluate Live Link Frame (Transform)

Evaluate current Live Link Transform associated with supplied subject

On this page

### Description

Evaluate current Live Link Transform associated with supplied subject

### Information

|  |  |
| --- | --- |
| Plugin | [LiveLinkControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/LiveLinkControlRig) |
| Category | Live Link |
| Type | [FRigUnit\_LiveLinkEvaluteFrameTransform](/documentation/en-us/unreal-engine/API/Plugins/LiveLinkControlRig/FRigUnit_LiveLinkEvaluteFrameTra-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SubjectName | The name of the subject to evaluate | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bDrawDebug | If True debug data will be drawn | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug drawing | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugDrawOffset | The world offset to use for the debug drawing | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting transform of the subject | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/EvaluateLiveLinkFrameTransform?application_version=5.7#outputs)
