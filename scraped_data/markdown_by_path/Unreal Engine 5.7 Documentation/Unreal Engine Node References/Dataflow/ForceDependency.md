<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency?application_version=5.7 -->

# ForceDependency

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
7. ForceDependency

# ForceDependency

ForceDependency (v1)

On this page

### Description

ForceDependency (v1)

Force an evaluation dependency between two values

Input(s) :
Value - Evaluating Value will force an evaluation of DependentValue
DependentValue - Evaluating Value will force an evaluation of DependentValue

Output(s):
Value [Passthrough] - Evaluating Value will force an evaluation of DependentValue

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | FlowControl |
| Type | [FDataflowForceDependencyNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowForceDependencyNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| DependentValue | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |
| Value | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | Evaluating Value will force an evaluation of DependentValue | [FDataflowAnyType](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowAnyType) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency?application_version=5.7#outputs)
