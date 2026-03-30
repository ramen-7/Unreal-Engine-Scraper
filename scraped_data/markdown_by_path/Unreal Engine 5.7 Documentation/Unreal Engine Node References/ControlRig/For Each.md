<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach?application_version=5.7 -->

# For Each

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
7. For Each

# For Each

Loops over the elements in an array.

On this page

### Description

Loops over the elements in an array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayIterator](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayIterator) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Array | The array to iterate over | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Completed | The Completed execute argument. | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Element | The current element. | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Index | The index of the current element. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Count | The count of all elements in the array. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Ratio | A float ratio from 0.0 (first element) to 1.0 (last element). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForEach?application_version=5.7#outputs)
