<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer?application_version=5.7 -->

# AddSolverDeformer

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
7. AddSolverDeformer

# AddSolverDeformer

AddSolverDeformer (v1)

On this page

### Description

AddSolverDeformer (v1)

Add a graph deformer to the groom simulation

Input(s) :
PhysicsSolvers - Physics solvers to advance in time
SimulationTime - Delta time to use to advance the solver

Output(s):
PhysicsSolvers [Passthrough] - Physics solvers to advance in time

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsSolver](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsSolver) |
| Category | Physics|Solver |
| Tags | DataflowSimulationTag |
| Type | [FAddSolverDeformerDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsSolver/FAddSolverDeformerDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| MeshDeformer | Graph deformer solver the component is using | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UOptimusDeformer](/documentation/en-us/unreal-engine/API/Plugins/OptimusCore/UOptimusDeformer)> | None |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| SimulationTime | Delta time to use to advance the solver | [FDataflowSimulationTime](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationTime) | () |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolvers | Physics solvers to advance in time | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FDataflowSimulationProperty](/documentation/en-us/unreal-engine/API/Runtime/DataflowSimulation/FDataflowSimulationProperty)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer?application_version=5.7#outputs)
