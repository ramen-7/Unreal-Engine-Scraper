<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel?application_version=5.7 -->

# Spawn Integer Animation Channel

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
7. Spawn Integer Animation Channel

# Spawn Integer Animation Channel

Adds a new animation channel to the hierarchy

On this page

### Description

Adds a new animation channel to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,AddAnimationChannel,NewAnimationChannel,CreateAnimationChannel,AddChannel,NewChannel,CreateChannel,SpawnChannel |
| Type | [FRigUnit\_HierarchyAddAnimationChannelInteger](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_4) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new animation channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MinimumValue | The minimum value of the new animation channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| MaximumValue | The maximum value for the animation channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| LimitsEnabled | The enable settings for the limits | [Rig Unit Hierarchy Add Animation Channel Single Limit Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddAnimationCh-_9) | (Enabled=(bMinimum=True,bMaximum=True)) |
| ControlEnum | The enum to use to find valid values | Enum | None |
| Parent | The parent of the new element to add | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewChannel |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnIntegerAnimationChannel?application_version=5.7#outputs)
