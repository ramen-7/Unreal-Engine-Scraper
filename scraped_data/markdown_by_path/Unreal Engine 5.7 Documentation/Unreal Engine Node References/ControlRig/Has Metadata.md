<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata?application_version=5.7 -->

# Has Metadata

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
7. Has Metadata

# Has Metadata

Returns true if a given item in the hierarchy has a specific set of metadata

On this page

### Description

Returns true if a given item in the hierarchy has a specific set of metadata

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Hierarchy |
| Tags | MetadataExists,HasKey,SupportsMetadata,FindMetadata |
| Type | [FRigUnit\_HasMetadata](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HasMetadata) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The item to check the metadata for | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the metadata to check | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Type | The type of metadata to check for | [Rig Metadata Type](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetadataType) | Float |
| NameSpace | Defines in which namespace the metadata will be looked up | [Rig Meta Data Name Space](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/ERigMetaDataNameSpace) | Self |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Found | True if the item has the metadata | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/HasMetadata?application_version=5.7#outputs)
