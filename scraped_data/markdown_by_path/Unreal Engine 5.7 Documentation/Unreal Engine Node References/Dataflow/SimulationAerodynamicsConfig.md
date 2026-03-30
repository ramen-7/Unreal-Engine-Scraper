<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig?application_version=5.7 -->

# SimulationAerodynamicsConfig

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
7. SimulationAerodynamicsConfig

# SimulationAerodynamicsConfig

SimulationAerodynamicsConfig (v1) Aerodynamics properties configuration node.

On this page

### Description

SimulationAerodynamicsConfig (v1)

Aerodynamics properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Aerodynamics Config |
| Type | [FChaosClothAssetSimulationAerodynamicsConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_6) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FluidDensity | The density of the medium in which the aerodynamic forces take place, usually air. The fluid density is given in kg/m^3. Air density is considered to be around 1.225 kg/m^3 in average atmospheric conditions. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.225000 |
| WindVelocitySpace | Wind velocity is specified in this space. | [EChaosSoftsSimulationSpace](/documentation/en-us/unreal-engine/API/Runtime/Chaos/EChaosSoftsSimulationSpace) | WorldSpace |
| WindVelocity | The fixed wind velocity [m/s] for this asset. For reference a wind gust is above 8m/s (18mph). | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Drag | The aerodynamic coefficient of drag applying on each particle. When "Outer Drag" is enabled, this acts as the "Inner Drag", i.e., drag applied when the air velocity is moving in the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="Drag",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableOuterDrag |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| OuterDrag | The aerodynamic coefficient of drag applying on each particle when the air velocity is moving against the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="OuterDrag",bImportFabricBounds=False,bBuildFabricMaps=False) |
| Lift | The aerodynamic coefficient of lift applying on each particle. When "Outer Lift" is enabled, this acts as the "Inner Lift", i.e., lift applied when the air velocity is moving in the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="Lift",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableOuterLift |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| OuterLift | The aerodynamic coefficient of lift applying on each particle when the air velocity is moving against the mesh normal direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.035000,High=1.000000,WeightMap="OuterLift",bImportFabricBounds=False,bBuildFabricMaps=False) |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig?application_version=5.7#outputs)
