<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy?application_version=5.7 -->

# GenerateInterpolatedProxy

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
7. GenerateInterpolatedProxy

# GenerateInterpolatedProxy

GenerateInterpolatedProxy (v1)

On this page

### Description

GenerateInterpolatedProxy (v1)
Experimental

Generate a pair of Dynamic Meshes with the same topology that can be interpolated.

Currently, this node relies on the vertex mapping data existing on the input source and target meshes,
and that the mapped vertices on both meshes match.

Input(s) :
SourceMesh - Source mesh
SourceMaterialArray - Source materials.
TargetMesh - Target mesh

Output(s):
ProxyMesh - Output proxy mesh
ProxyMaterialArray - Proxy materials.

### Information

|  |  |
| --- | --- |
| Module | [MeshResizingDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/MeshResizingDataflowNodes) |
| Category | MeshResizing |
| Type | FGenerateInterpolatedProxyDataflowNode |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BlendAlpha | Alpha between source (0) and target (1) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SourceMesh | Source mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| SourceMaterialArray | Source materials. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |
| TargetMesh | Target mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ProxyMesh | Output proxy mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |
| ProxyMaterialArray | Proxy materials. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UMaterialInterface](/documentation/en-us/unreal-engine/API/Runtime/Engine/UMaterialInterface)>> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy?application_version=5.7#outputs)
