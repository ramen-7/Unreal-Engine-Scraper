<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Init?application_version=5.7 -->

# Init

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
4. Init

# Init

Sets the size of the array, initializing all elements to the given value. Modifies the input array.

On this page

### Description

Sets the size of the array, initializing all elements to the given value.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayInit](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayInit) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to initialize. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Num | The new size of the array. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| Element | The value that is set to all elements. | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Init?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Init?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/Init?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Init?application_version=5.7#inputs)
