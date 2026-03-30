<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies?application_version=5.7 -->

# FilterSimulationProxies

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
7. FilterSimulationProxies

# FilterSimulationProxies

FilterSimulationProxies (v1)

On this page

### Description

FilterSimulationProxies (v1)

Filter simulation proxies from context

Input(s) :
SimulationProxies - Simulation proxies coming from the context and filtered with the groups

Output(s):
FilteredProxies - Simulation proxies coming from the context and filtered with the groups

### Information

|  |  |
| --- | --- |
| Module | [DataflowSimulation](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation) |
| Category | Physics|Proxy |
| Tags | DataflowSimulationTag |
| Type | [FFilterSimulationProxiesDataflowNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FFilterSimulationProxiesDataflow-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationGroups | Simulation groups to filter the output solvers properties | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationProxies | Simulation proxies coming from the context and filtered with the groups | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FilteredProxies | Simulation proxies coming from the context and filtered with the groups | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies?application_version=5.7#outputs)
