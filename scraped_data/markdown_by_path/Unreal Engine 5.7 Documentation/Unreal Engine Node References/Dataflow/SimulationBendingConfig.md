<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig?application_version=5.7 -->

# SimulationBendingConfig

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
7. SimulationBendingConfig

# SimulationBendingConfig

SimulationBendingConfig (v1) Bending constraint property configuration node.

On this page

### Description

SimulationBendingConfig (v1)

Bending constraint property configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Bending Config |
| Type | [FChaosClothAssetSimulationBendingConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_9) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RestAngleType | Method for calculating the rest angles of the constraints. | [EChaosClothAssetRestAngleConstructionType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_2) | Use3DRestAngles |
| FlatnessRatio | Calculate rest angles as a ratio between completely flat and whatever is the 3D rest angle. When FlatnessRatio = 0, this is equivalent to "Use3DRestAngles". When FlatnessRatio = 1, the rest angle will be 0 (completely flat). If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValueNonAnimatable](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.000000,High=0.000000,WeightMap="FlatnessRatio",bImportFabricBounds=False,bBuildFabricMaps=False) |
| RestAngle | Set rest angles to be the explicit value set here (in degrees). 0 = Flat, Positive values fold away from the edge normal, Negative values fold toward the edge normal. When converting vertex weight values to edge values, the value with the smallest absolute value is selected. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValueNonAnimatable](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_44) | (Low=0.000000,High=0.000000,WeightMap="RestAngle",bImportFabricBounds=False,bBuildFabricMaps=False) |
| SolverType | Constraint solver type | [EChaosClothAssetConstraintSolverType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintSolver-) | PBD |
| DistributionType | Constraint distribution type | [EChaosClothAssetConstraintDistributionType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_3) | Isotropic |
| ConstraintType | Constraint method type | [EChaosClothAssetBendingConstraintType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetBendingConstrain-) | HingeAngles |
| BendingStiffnessWarp | The stiffness of the bending constraints in the warp (vertical) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="BendingStiffnessWarp",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingStiffnessWeft | The stiffness of the bending constraints in the weft (horizontal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="BendingStiffnessWeft",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingStiffnessBias | The stiffness of the bending constraints in the bias (diagonal) direction. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=100.000000,High=100.000000,WeightMap="BendingStiffnessBias",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingAnisoDamping | The damping of the bending anisotropic constraints, relative to critical damping. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="BendingAnisoDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |
| AnisoBucklingRatio | Once the element has bent such that it's folded more than this ratio from its rest angle ("buckled"), switch to using Buckling Stiffness instead of BendingElement Stiffness. When Buckling Ratio = 0, the Buckling Stiffness will never be used. When BucklingRatio = 1, the Buckling Stiffness will be used as soon as it's bent past its rest configuration. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.500000,High=0.500000,WeightMap="BucklingRatio",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffnessWarp | The stiffness after buckling in the warp (vertical) direction. The constraint will use this stiffness instead of element Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than BendingElement Stiffness. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=50.000000,High=50.000000,WeightMap="BucklingStiffnessWarp",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffnessWeft | The stiffness after buckling in the weft (horizontal) direction. The constraint will use this stiffness instead of element Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than BendingElement Stiffness. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=50.000000,High=50.000000,WeightMap="BucklingStiffnessWeft",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffnessBias | The stiffness after buckling in the bias (diagonal) direction. The constraint will use this stiffness instead of element Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than BendingElement Stiffness. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=50.000000,High=50.000000,WeightMap="BucklingStiffnessBias",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingStiffness | The Stiffness of the bending constraints. Increase the iteration count for stiffer materials. Note that PBD stiffnesses will be internally clamped to [0,1]. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="BendingStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BendingDamping | The damping of the bending constraints, relative to critical damping. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=1.000000,High=1.000000,WeightMap="BendingDamping",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingStiffness | The stiffness after buckling. The constraint will use this stiffness instead of bending Stiffness once the cloth has buckled, i.e., bent beyond a certain angle. Typically, Buckling Stiffness is set to be less than Bending Stiffness. Note that PBD stiffnesses will be internally clamped to [0,1]. Buckling Ratio determines the switch point between using BendingElement Stiffness and Buckling Stiffness. If a valid weight map is found with the given Weight Map name, then both Low and High values are interpolated with the per particle weight to make the final value used for the simulation. Otherwise all particles are considered to have a zero weight, and only the Low value is meaningful. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.900000,High=0.900000,WeightMap="BucklingStiffness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| BucklingRatioWeighted | Once the element has bent such that it's folded more than this ratio from its rest angle ("buckled"), switch to using Buckling Stiffness instead of BendingElement Stiffness. When Buckling Ratio = 0, the Buckling Stiffness will never be used. When BucklingRatio = 1, the Buckling Stiffness will be used as soon as it's bent past its rest configuration. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.500000,High=0.500000,WeightMap="BucklingRatio",bImportFabricBounds=False,bBuildFabricMaps=False) |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig?application_version=5.7#outputs)
