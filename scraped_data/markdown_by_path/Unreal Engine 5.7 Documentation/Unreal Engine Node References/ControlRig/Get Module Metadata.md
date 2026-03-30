<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata?application_version=5.7 -->

# Get Module Metadata

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
7. Get Module Metadata

# Get Module Metadata

Returns some metadata on a given module

On this page

### Description

Returns some metadata on a given module

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Type | [FRigDispatch\_GetModuleMetadata](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigDispatch_GetModuleMetadata) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Name | The name of the metadata | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |
| Default | The default value used as a fallback if the metadata does not exist | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The value to get / set | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |
| Found | Returns true if the metadata exists with the specific type | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/GetModuleMetadata?application_version=5.7#outputs)
