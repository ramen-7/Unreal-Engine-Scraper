<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton?application_version=5.7 -->

# Import Skeleton

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
7. Import Skeleton

# Import Skeleton

Imports all bones (and curves) from the currently assigned skeleton.

On this page

### Description

Imports all bones (and curves) from the currently assigned skeleton.
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Skeleton,Mesh,AddBone,AddCurve,Spawn |
| Type | [FRigUnit\_HierarchyImportFromSkeleton](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyImportFromSkel-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NameSpace | The namespace to use when importing bones and curves | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| bIncludeCurves | If True the curves will be imported | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIncludeMeshSockets | If true the mesh sockets will be imported | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bIncludeVirtualBones | If true virtual bones will be imported | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Items | The resulting imported items | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportSkeleton?application_version=5.7#outputs)
