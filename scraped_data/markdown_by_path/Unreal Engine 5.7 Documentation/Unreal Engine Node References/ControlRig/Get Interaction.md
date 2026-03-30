<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction?application_version=5.7 -->

# Get Interaction

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
7. Get Interaction

# Get Interaction

Returns true if the Control Rig is being interacted

On this page

### Description

Returns true if the Control Rig is being interacted

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Execution |
| Tags | IsInteracting,Gizmo,Manipulation,Interaction,Tracking |
| Type | [FRigUnit\_IsInteracting](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_IsInteracting) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bIsInteracting | True if there is currently an interaction happening | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsTranslating | True if the current interaction is a translation | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsRotating | True if the current interaction is a rotation | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| bIsScaling | True if the current interaction is scaling | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Items | The items being interacted on | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction?application_version=5.7#information)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetInteraction?application_version=5.7#outputs)
