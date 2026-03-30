<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector?application_version=5.7 -->

# DivideVector

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
7. DivideVector

# DivideVector

DivideVector (v1)

On this page

### Description

DivideVector (v1)

Multiply two vectors component wise: V = (A / B)
When a component of B is zero, use the falback value as a return value for the specific component

Input(s) :
A - A Vector operand
B - B Vector operand
Fallback - Fallback Vector used when components of B are zero

Output(s):
V - Add result V=A\*B

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Math|Vectors |
| Tags | / Division Over |
| Type | [FDataflowVectorDivideNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorDivideNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | A Vector operand | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| B | B Vector operand | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |
| Fallback | Fallback Vector used when components of B are zero | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) | (Value=(X=0.000000,Y=0.000000,Z=0.000000,W=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| V | Add result V=A\*B | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector?application_version=5.7#outputs)
