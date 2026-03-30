<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp?application_version=5.7 -->

# Critical Spring Damp

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
7. Critical Spring Damp

# Critical Spring Damp

Damps a float using a spring damper

On this page

### Description

Damps a float using a spring damper
Damps a vector using a spring damper
Damps a quaternion using a spring damper

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Damp|Experimental |
| Tags | Critical Spring Damp,Critical Spring Damp (Float),Critical Spring Damp (Vector),Critical Spring Damp (Quat) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to damp | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| ValueVelocity | The velocity of the value | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| ExecutePin | This property is used to chain multiple mutable nodes together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Target | The target to damp towards | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| SmoothingTime | The time to apply smoothing for | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.200000 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/CriticalSpringDamp?application_version=5.7#inputs)
