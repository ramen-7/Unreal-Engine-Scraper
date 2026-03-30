<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative?application_version=5.7 -->

# Make Relative

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
7. Make Relative

# Make Relative

Returns the relative local rotation within a parent's rotation

On this page

### Description

Returns the relative local rotation within a parent's rotation
Returns the relative local transform within a parent's transform
Returns the relative local vector within a parent's vector

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | Make Relative,Local,Global,Absolute |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Global | The global rotation quaternion to make relative | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |
| Parent | The parent global rotation to make the input relative to | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Local | The resulting relative rotation | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/MakeRelative?application_version=5.7#outputs)
