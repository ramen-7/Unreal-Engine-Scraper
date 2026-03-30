<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig?application_version=5.7 -->

# SimulationSolverConfig

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
7. SimulationSolverConfig

# SimulationSolverConfig

SimulationSolverConfig (v1) Solver properties configuration node.

On this page

### Description

SimulationSolverConfig (v1)

Solver properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Solver Config |
| Type | [FChaosClothAssetSimulationSolverConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_31) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| NumIterations | The number of time step dependent solver iterations. This sets iterations at 60fps. NumIterations can never be bigger than MaxNumIterations. At lower fps up to MaxNumIterations may be used instead. At higher fps as low as one single iteration might be used. Higher number of iterations will increase the stiffness of all constraints and improve convergence, but will also increase the CPU cost of the simulation. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| MaxNumIterations | The maximum number of solver iterations. This is the upper limit of the number of iterations set in solver, when the frame rate is lower than 60fps. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 6 |
| NumSubstepsImported | The number of solver substeps. This will increase the precision of the collision inputs and help with constraint resolutions but will increase the CPU cost. | [FChaosClothAssetImportedIntValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedIntValue) | (ImportedValue=1,bUseImportedValue=False) |
| bEnableDynamicSubstepping | Enable dynamic substepping. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DynamicSubstepDeltaTime | Choose the number of substeps based on a target substep delta time in milliseconds. Substeps are clamped to [1, NumSubsteps]. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 16.670000 |
| bEnableNumSelfCollisionSubsteps | Enable setting separate SelfCollisionSubsteps. Otherwise, self collisions will be detected every substep. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| NumSelfCollisionSubsteps | Set a separate number of self collision substeps. Lower this number to increase speed at the expense of lower self collision accuracy. Actual value always clamped between [1, NumSubsteps]. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig?application_version=5.7#outputs)
