<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport?application_version=5.7 -->

# SkeletalMeshImport

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
7. SkeletalMeshImport

# SkeletalMeshImport

SkeletalMeshImport (v2)

On this page

### Description

SkeletalMeshImport (v2)

Import a skeletal mesh asset into the cloth collection simulation and/or render mesh containers.

Input(s) :
SkeletalMesh - The skeletal mesh to import.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Skeletal Mesh Import |
| Type | [FChaosClothAssetSkeletalMeshImportNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_42) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Reimport | Reimport the imported skeletal mesh asset. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| LODIndex | The skeletal mesh LOD to import. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSingleSection | Enable single import section mode. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| SectionIndex | The skeletal mesh LOD section to import. If not enabled, then all sections will be imported. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bImportSimMesh | Whether to import the simulation mesh from the specified skeletal mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bImportRenderMesh | Whether to import the render mesh from the specified skeletal mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| UVChannel | UV channel of the skeletal mesh to import the 2D simulation mesh patterns from. If set to -1, or the specified UVChannel doesn't exist then the import will unwrap the 3D simulation mesh into 2D simulation mesh patterns. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| UVScale | Apply this scale to the UVs when populating Sim Mesh positions. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| bSetPhysicsAsset | Set the same physics asset as the one used by the imported skeletal mesh. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bImportSimMorphTargets | Import morph targets as Sim Mesh Morph Targets | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SkeletalMesh | The skeletal mesh to import. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport?application_version=5.7#outputs)
