<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7 -->

# Add

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
7. Add

# Add

2 nodes with name Add

On this page

## Add ()

Returns the sum of the two values

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Add,Sum,+ |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first color for the operation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| B | The second color for the operation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting color | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) |  |

## Add (FRigVMDispatch\_ArrayAdd)

Adds an element to an array and returns the new element's index.
Modifies the input array.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Array |
| Tags | List,Collection |
| Type | [FRigVMDispatch\_ArrayAdd](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_ArrayAdd) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecuteContext | This pin is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |
| Array | The array to add an element to. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigVMUnknownType](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType)> |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Element | The element to add to the array. | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the newly added element. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Add ()](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#add())
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#outputs)
* [Add (FRigVMDispatch\_ArrayAdd)](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#add(frigvmdispatch-arrayadd))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#information-2)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Add?application_version=5.7#outputs-2)
