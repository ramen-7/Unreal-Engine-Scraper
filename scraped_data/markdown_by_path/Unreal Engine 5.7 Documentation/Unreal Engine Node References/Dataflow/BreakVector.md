<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7 -->

# BreakVector

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
7. BreakVector

# BreakVector

2 nodes with name BreakVector

On this page

## BreakVector (FDataflowVectorBreakNode)

BreakVector (v1)

Break a vector in 4 components
if the input vector is of a lower dimension than 4, the remaining components will be set to zero

Input(s) :
V - Vector to break into components

Output(s):
X - X component
Y - Y component
Z - Z component
W - W component

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | Expand Split X Y Z W Components |
| Type | [FDataflowVectorBreakNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorBreakNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Vector to break into components | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X | X component | [FDataflowNumericTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
| Y | Y component | [FDataflowNumericTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
| Z | Z component | [FDataflowNumericTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |
| W | W component | [FDataflowNumericTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowNumericTypes) |  |

## BreakVector (FExpandVectorDataflowNode)

BreakVector (v1)

Expands a Vector into X, Y, Z components

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Utilities|Vector |
| Tags | Expand X Y Z |
| Type | [FExpandVectorDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FExpandVectorDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Vector |  | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| X |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Y |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Z |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [BreakVector (FDataflowVectorBreakNode)](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#breakvector(fdataflowvectorbreaknode))
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#outputs)
* [BreakVector (FExpandVectorDataflowNode)](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#breakvector(fexpandvectordataflownode))
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#information-2)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector?application_version=5.7#outputs-2)
