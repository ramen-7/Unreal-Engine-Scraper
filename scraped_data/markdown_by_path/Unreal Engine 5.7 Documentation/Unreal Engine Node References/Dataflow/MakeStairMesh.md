<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh?application_version=5.7 -->

# MakeStairMesh

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
7. MakeStairMesh

# MakeStairMesh

MakeStairMesh (v1) Make a stair mesh Output(s): Mesh - Output mesh

On this page

### Description

MakeStairMesh (v1)

Make a stair mesh

Output(s):
Mesh - Output mesh

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Mesh |
| Type | [FMakeStairMeshDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeStairMeshDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StairType | Type of staircase | [EDataflowStairTypeEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EDataflowStairTypeEnum) | Linear |
| NumSteps | The number of steps in this staircase. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 8 |
| StepWidth | The width of each step. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |
| StepHeight | The height of each step. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 20.000000 |
| StepDepth | The height of each step. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 30.000000 |
| CurveAngle | Inner radius of the curved staircase | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 90.000000 |
| InnerRadius | Curve angle of the staircase (in degrees) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 150.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh | Output mesh | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh?application_version=5.7#parameters)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh?application_version=5.7#outputs)
