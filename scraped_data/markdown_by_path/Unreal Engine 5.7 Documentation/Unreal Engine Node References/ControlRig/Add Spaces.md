<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces?application_version=5.7 -->

# Add Spaces

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
7. Add Spaces

# Add Spaces

Adds available spaces for a given control. This is used for the space switching widget.

On this page

### Description

Adds available spaces for a given control. This is used for the space switching widget.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,AddParent,Constraint,Space |
| Type | [FRigUnit\_AddAvailableSpaces](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AddAvailableSpaces) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Control | The available spaces to add for a given control | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Spaces | The spaces to add | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKeyWithLabel](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKeyWithLabel)> | ((Key=(Type=Control))) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/AddSpaces?application_version=5.7#inputs)
