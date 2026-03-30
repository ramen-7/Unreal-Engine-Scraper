<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone?application_version=5.7 -->

# Spawn Bone

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
7. Spawn Bone

# Spawn Bone

Adds a new bone to the hierarchy Note: This node only runs as part of the construction event.

On this page

### Description

Adds a new bone to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Construction,Create,New,Joint,Skeleton |
| Type | [FRigUnit\_HierarchyAddBone](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddBone) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The initial transform of the new element | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Space | Defines if the transform should be interpreted in local or global space | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| Parent | The parent of the new element to add | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewBone |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnBone?application_version=5.7#outputs)
