<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig?application_version=5.7 -->

# SimulationStretchOverrideConfig

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
7. SimulationStretchOverrideConfig

# SimulationStretchOverrideConfig

SimulationStretchOverrideConfig (v1)

On this page

### Description

SimulationStretchOverrideConfig (v1)
Experimental

Stretching constraint property override configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Stretching Override Config |
| Type | [FChaosClothAssetSimulationStretchOverrideConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_33) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bOverrideStretchUse3dRestLengths | Enable overriding Stretch Use 3d Rest Lengths | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bStretchUse3dRestLengths | Whether to use the 3D draped space as rest lengths, or use the 2D pattern space instead. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OverrideStretchStiffness | Stretch stiffness override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffness | Stretch stiffness override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| bApplyUniformStretchStiffnessOverride | Whether or not to apply the Stretch Stiffness Override to warp, weft, and bias stiffnesses of anisotropic springs. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| OverrideStretchStiffnessWarp | Warp stiffness override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffnessWarp | Stretch stiffness warp override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideStretchStiffnessWeft | Weft stiffness override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffnessWeft | Stretch stiffness weft override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideStretchStiffnessBias | Bias stiffness override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchStiffnessBias | Stretch stiffness bias override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideStretchDamping | Damping override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| StretchDamping | Stretch damping override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideWarpScale | Warp scale override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| WarpScale | Stretch damping override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |
| OverrideWeftScale | Weft scale override type. | [EChaosClothAssetConstraintOverrideType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetConstraintOverri-) | None |
| WeftScale | Stretch damping override value. | [FChaosClothAssetWeightedValueOverride](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValueOve-) | (Low=1.000000,High=1.000000) |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig?application_version=5.7#outputs)
