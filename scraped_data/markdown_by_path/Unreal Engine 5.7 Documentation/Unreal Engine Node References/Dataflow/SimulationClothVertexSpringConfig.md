<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig?application_version=5.7 -->

# SimulationClothVertexSpringConfig

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
7. SimulationClothVertexSpringConfig

# SimulationClothVertexSpringConfig

SimulationClothVertexSpringConfig (v1)

On this page

### Description

SimulationClothVertexSpringConfig (v1)
Experimental

Node for creating vertex-vertex constraints and setting their simulation properties.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Vertex Spring |
| Type | [FChaosClothAssetSimulationClothVertexSpringConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_13) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bAppendToExisting | Append to existing set of constraints. Stiffnesses inherited from existing constraints. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| VertexSpringExtensionStiffness | Extension Stiffness is the spring stiffness applied when the spring is currently longer than its rest length. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000) |
| VertexSpringCompressionStiffness | Compression Stiffness is the spring stiffness applied when the spring is currently shorter than its rest length. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=100.000000,Y=100.000000) |
| VertexSpringDamping | This damping is the relative to critical damping. This is a low-high range, but there are currently no ways to author per-spring stiffnesses, so only Low is used in practice. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| ConstructionSets | Construction data for procedurally generating constraints. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) | (()) |
| RestLengthScale | Scale applied to the rest lengths of the springs. A value of 1 will preserve the distance in the rest collection. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| GenerateConstraints | Click on this button to generate constraints from the construction data. | [FDataflowFunctionProperty](/documentation/en-us/unreal-engine/API/Plugins/DataflowNodes/FDataflowFunctionProperty) | () |
| ConstraintVertices | Raw constraint end point data. Modify at your own risk. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| RestLengths | Raw constraint rest length data. Modify at your own risk. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig?application_version=5.7#outputs)
