<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground?application_version=5.7 -->

# MeshConstrainedDeformationTestPlayground

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
7. MeshConstrainedDeformationTestPlayground

# MeshConstrainedDeformationTestPlayground

MeshConstrainedDeformationTestPlayground (v1) Experimental Mesh Constrained Deformation Node

On this page

### Description

MeshConstrainedDeformationTestPlayground (v1)
Experimental

Mesh Constrained Deformation Node

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Tags | Mesh Constrained Deformation |
| Type | FMeshConstrainedDeformationNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Iterations |  | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 100 |
| bEnableShearConstraint | Remove shear deformation | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ShearConstraintStrength |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableBendingConstraint |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| BendingConstraintStrength |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| bEnableEdgeConstraint |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| EdgeConstraintStrength |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Gravity |  | [FVector3d](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| BaseMesh |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> | None |
| InvMass |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| EdgeConstraintWeights |  | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResizingMesh |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDataflowMesh](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/UDataflowMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground?application_version=5.7#outputs)
