<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig?application_version=5.7 -->

# SimulationSelfCollisionConfig

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
7. SimulationSelfCollisionConfig

# SimulationSelfCollisionConfig

SimulationSelfCollisionConfig (v2)

On this page

### Description

SimulationSelfCollisionConfig (v2)

Self-collision repulsion forces (point-face) properties configuration node.
Note that the kinematic collider has been deprecated in favor of SkinnedTriangleMesh Physics Asset bodies

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Self Collision Config |
| Type | [FChaosClothAssetSimulationSelfCollisionConfigNode\_v2](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_29) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bUseSelfCollisions | Activating this node will enable self collisions. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| SelfCollisionThickness | The self collision offset per side. Total thickness of cloth is 2x this value. | [FChaosClothAssetWeightedValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetWeightedValue) | (bIsAnimatable=True,Low=0.500000,High=0.500000,WeightMap="SelfCollisionThickness",bImportFabricBounds=False,bBuildFabricMaps=False) |
| SelfCollisionStiffness | The stiffness of the springs used to control self collision. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| SelfCollisionFriction | Friction coefficient for cloth - cloth interaction. | [FChaosClothAssetImportedFloatValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetImportedFloatVal-) | (ImportedValue=0.000000,bUseImportedValue=False) |
| SelfCollisionDisableNeighborDistance | Disabled neighbor collision ring. Collisions are disabled between vertices within this N-ring connectivity distance. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 5 |
| SelfCollisionLayers | Self collision layers face int map. Generate this map using the SelectionsToIntMap node with SimFace Selections. Faces labeled with -1 will collide normally without any layering behavior. Faces labeled with any other number will keep higher layer numbers outside lower layer numbers (outside = front facing normal direction). | [FChaosClothAssetConnectableIStringValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="SelfCollisionLayers",bBuildFabricMaps=False) |
| SelfCollisionDisabledFaces | Sim face selection set of faces which should not self collide | [FChaosClothAssetConnectableIStringValue](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetConnectableIStri-) | (StringValue="SelfCollisionDisabledFaces",bBuildFabricMaps=False) |
| bUseSelfIntersections | Enable self intersection resolution. This will try to fix any cloth intersections that are not handled by collision repulsions. Can be expensive. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseGlobalIntersectionAnalysis | Do global intersection analysis to determine the correct normals for the collision springs | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bUseContourMinimization | Do a step of contour minimization at the beginning of the timestep. Contour minimization will attempt to resolve intersections by shortening the intersection edge. Helpful with open intersections that global intersection analysis can't fix. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NumContourMinimizationPostSteps | Number of post timestep contour minimization steps to do. (Very Expensive!) Contour minimization will attempt to resolve intersections by shortening the intersection edge.Helpful with open intersections that global intersection analysis can't fix. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| bUseGlobalPostStepContours | Use global contour gradients when doing post timestep contour minimization | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig?application_version=5.7#outputs)
