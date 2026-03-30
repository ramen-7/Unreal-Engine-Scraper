<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData?application_version=5.7 -->

# Set Shape Library from User Data

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
7. Set Shape Library from User Data

# Set Shape Library from User Data

Allows to set / add a shape library on the running control rig from user data

On this page

### Description

Allows to set / add a shape library on the running control rig from user data

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Tags | Shape,Gizmo,Library |
| Type | [FRigUnit\_SetupShapeLibraryFromUserData](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SetupShapeLibraryFromUs-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NameSpace | The name space of the user data to look the shape library up within | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Path | The path within the user data for the shape library | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| LibraryName | Optionally provide the namespace of the shape library to use.  *This is only useful if you have multiple shape libraries and you*  want to override a specific one. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| LogShapeLibraries | If this is checked we'll output the resulting shape libraries to the log for debugging. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SetShapeLibraryfromUserData?application_version=5.7#inputs)
