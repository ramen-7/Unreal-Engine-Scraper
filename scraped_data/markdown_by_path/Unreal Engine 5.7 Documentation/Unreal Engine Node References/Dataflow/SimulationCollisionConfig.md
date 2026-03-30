<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig?application_version=5.7 -->

# SimulationCollisionConfig

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
7. SimulationCollisionConfig

# SimulationCollisionConfig

SimulationCollisionConfig (v1) Chaos Cloth Asset Simulation Collision Config Node

On this page

### Description

SimulationCollisionConfig (v1)

Chaos Cloth Asset Simulation Collision Config Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Collision Config |
| Type | [FChaosClothAssetSimulationCollisionConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_15) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| CollisionThicknessImported | The added thickness of collision shapes. | [FChaosClothAssetImportedFloatValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedFloatVal-) | (ImportedValue=1.000000,bUseImportedValue=False) |
| FrictionCoefficientWeighted | Friction coefficient for cloth - collider interaction. Currently only Skinned Triangle Meshes use the weighted value. All other collisions only use the Low value. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.800000,High=0.800000,WeightMap="FrictionCoefficient",bImportFabricBounds=False,bBuildFabricMaps=False) |
| bEnableSimpleColliders | Enable colliding against any simple (e.g., capsules, convexes, spheres, boxes) colliders.. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUsePlanarConstraintForSimpleColliders | Use Planar Constraints for simple (e.g., capsules, convexes, spheres, boxes) colliders when doing multiple iterations. Planar constraints are cheaper than full collision detection, but less accurate. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| bEnableComplexColliders | Enable colliding against any complex (e.g., SkinnedLevelSet, MLLevelSet) colliders. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUsePlanarConstraintForComplexColliders | Use Planar Constraints for complex (e.g., SkinnedLevelSet, MLLevelSet) colliders when doing multiple iterations. Planar constraints are cheaper than full collision detection, but less accurate. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bEnableSkinnedTriangleMeshCollisions | Enable colliding against any Skinned Triangle Mesh colliders. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseSelfCollisionSubstepsForSkinnedTriangleMeshes | Use 'NumSelfCollisionSubsteps' (Located on SimulationSolverConfig) to also control Skinned Triangle Mesh collision updates | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ClothCollisionThicknessImported | Thickness added to the cloth when colliding against collision shapes. Currently only Skinned Triangle Meshes use the weighted value. All other collisions only use the Low value. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.000000,High=0.000000,WeightMap="ClothCollisionThickness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| ProximityStiffness | Stiffness for proximity repulsion forces (Force-based solver only). Units = kg cm/ s^2 (same as XPBD springs) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| bUseCCD | Use continuous collision detection (CCD) to prevent any missed collisions between fast moving particles and colliders. This has a negative effect on performance compared to when resolving collision without using CCD. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig?application_version=5.7#outputs)
