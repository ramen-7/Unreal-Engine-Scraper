<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7 -->

# Find

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
7. Find

# Find

2 nodes with name Find

On this page

## Find (FRigVMFunction\_StringFind)

Finds a string within another string

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Core|String |
| Tags | IndexOf |
| Type | [FRigVMFunction\_StringFind](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_StringFind) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input string to search within | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| Search | The string to search for | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Found | True if the search string was found in the input string | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Index | The index of the search string within the input string (or INDEX\_NONE) | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Find (FRigVMDispatch\_ArrayFind)

Searchs a potential element in an array and returns its index.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayFind](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayFind) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to search within. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |
| Element | The element to look for. | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the found element (or -1). | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Success | True if the element has been found. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Find (FRigVMFunction\_StringFind)](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#find(frigvmfunction-stringfind))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#outputs)
* [Find (FRigVMDispatch\_ArrayFind)](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#find(frigvmdispatch-arrayfind))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#information-2)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Find?application_version=5.7#outputs-2)
