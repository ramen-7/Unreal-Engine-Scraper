<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop?application_version=5.7 -->

# For Loop

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
7. For Loop

# For Loop

Given a count, execute iteratively until the count is up

On this page

### Description

Given a count, execute iteratively until the count is up

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Execution |
| Tags | Iterate |
| Type | [FRigVMFunction\_ForLoopCount](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_ForLoopCount) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Count | The number of iterations for this loop | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Index | The index of the current iteration | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Ratio | The ratio of the current iteration (from 0.0 for the first to 1.0 for the last) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Completed | The completed branch to run once the loop has finished all iterations | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ForLoop?application_version=5.7#outputs)
