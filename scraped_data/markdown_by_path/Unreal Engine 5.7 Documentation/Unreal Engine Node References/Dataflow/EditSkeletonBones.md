<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones?application_version=5.7 -->

# EditSkeletonBones

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
7. EditSkeletonBones

# EditSkeletonBones

EditSkeletonBones (v1)

On this page

### Description

EditSkeletonBones (v1)
Experimental

Edit skeleton bones properties.

Input(s) :
Skeleton - Skeleton to be edited

Output(s):
Skeleton [Passthrough] - Skeleton to be edited

### Information

|  |  |
| --- | --- |
| Module | [DataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes) |
| Category | Collection |
| Tags | Edit skeleton bones |
| Type | [FDataflowCollectionEditSkeletonBonesNode](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowCollectionEditSkeletonB-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VertexGroup | Target group in which the attributes are stored | [FScalarVertexPropertyGroup](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FScalarVertexPropertyGroup) | (Name="Vertices") |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| Skeleton | Skeleton to be edited | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Skeleton | Skeleton to be edited | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeleton](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeleton)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones?application_version=5.7#outputs)
