<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding?application_version=5.7 -->

# SetFleshBonePositionTargetBinding

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
6. [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow "Dataflow")
7. SetFleshBonePositionTargetBinding

# SetFleshBonePositionTargetBinding

SetFleshBonePositionTargetBinding (v2)

On this page

### Description

SetFleshBonePositionTargetBinding (v2)

Binds vertices from Collection to bone skeletal mesh surface via kinematic or weak constraints.

Input(s) :
VertexSelection - (optional) only create kinematic/weak constraints on vertices in the VertexSelection

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetFleshBonePositionTargetBindingDataflowNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetFleshBonePositionTargetBindi-_1) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalBindingMode |  | [ESkeletalBindingMode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/ESkeletalBindingMode) | Dataflow\_SkeletalBinding\_PositionTarget |
| PositionTargetStiffness |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10000.000000 |
| SearchRadius | Collection vertices are bound to their closest skeletal mesh vertices within the search radius | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMeshIn |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| VertexSelection | (optional) only create kinematic/weak constraints on vertices in the VertexSelection | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding?application_version=5.7#outputs)
