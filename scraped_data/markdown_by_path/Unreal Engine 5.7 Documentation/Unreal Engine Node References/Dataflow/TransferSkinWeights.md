<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights?application_version=5.7 -->

# TransferSkinWeights

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
7. TransferSkinWeights

# TransferSkinWeights

TransferSkinWeights (v1)

On this page

### Description

TransferSkinWeights (v1)

Transfer the skinning weights set on a skeletal mesh to the simulation and/or render mesh stored in the cloth collection.

Input(s) :
SkeletalMesh - The skeletal mesh to transfer the skin weights from.
SimCollection - The collection containing the sim mesh to use when the Render Mesh Transfer Source is set to Collection/Sim Collection. When this input isn't connected, the Collection input is used instead.
LodIndex - The skeletal mesh LOD to transfer the skin weights from.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Transfer Skin Weights |
| Type | [FChaosClothAssetTransferSkinWeightsNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTransferSkinWeig-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| TargetMeshType | The type of cloth mesh the skeletal mesh transfer will be applied to, simulation, render mesh, or both. | [EChaosClothAssetTransferTargetMeshType](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetTransferTargetMe-) | All |
| SimMeshSourceTypeHint | For the sim mesh, simulation mesh transfers always use the specified skeletal mesh. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Skeletal Mesh |
| RenderMeshSourceType | For the render mesh, choose which source to use, either the default or specified simulation mesh or the specified skeletal mesh. | [EChaosClothAssetTransferRenderMeshSource](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetTransferRenderMe-) | SimulationMesh |
| Transform | The relative transform between the skeletal mesh and the cloth asset. | [FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| TransferMethodHint | Algorithm used for the transfer method. When the Render Mesh Transfer Source is set to use the sim mesh from the Collection/Sim Collection input, only the ClosestPointOnSurface method is available. | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Closest Point On Surface |
| TransferMethod | Algorithm used for the transfer method. Use the simple ClosestPointOnSurface method or the more complex InpaintWeights method for better results. Note: When using the simulation mesh as source for the render mesh transfer, the algorithm will always be the ClosestPointOnSurface method, whatever this setting is. | [EChaosClothAssetTransferSkinWeightsMethod](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAsset-_4) | InpaintWeights |
| RadiusPercentage | Percentage of the bounding box diagonal of the simulation mesh to use as search radius for the InpaintWeights method. All points outside of the search radius will be ignored. When set to a negative value (e.g. -1), all points will be considered. | double | 0.050000 |
| NormalThreshold | Maximum angle difference (in degrees) between the target and source point normals to be considered a match for the InpaintWeights method. If set to a negative value (e.g. -1), normals will be ignored. | double | 30.000000 |
| LayeredMeshSupport | If true, when the closest point doesn't pass the normal threshold test, will try again with a flipped normal. This helps with layered meshes where the "inner" and "outer" layers are close to each other but whose normals are pointing in the opposite directions. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| NumSmoothingIterations | The number of smoothing iterations applied to the vertices whose weights were automatically computed. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| SmoothingStrength | The smoothing strength of each smoothing iteration. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| InpaintMask | Optional mask where a non-zero value indicates that we want the skinning weights for the vertex to be computed automatically instead of it being copied over from the source mesh. | [FChaosClothAssetWeightedValueNonAnimatableNoLowHighRange](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_45) | (WeightMap="InpaintMask") |
| MaxNumInfluences | The maximum number of bones that will influence each vertex. | [EChaosClothAssetMaxNumInfluences](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/EChaosClothAssetMaxNumInfluences) | Eight |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SkeletalMesh | The skeletal mesh to transfer the skin weights from. | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[USkeletalMesh](/documentation/en-us/unreal-engine/API/Runtime/Engine/USkeletalMesh)> | None |
| LodIndex | The skeletal mesh LOD to transfer the skin weights from. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| SimCollection | The collection containing the sim mesh to use when the Render Mesh Transfer Source is set to Collection/Sim Collection. When this input isn't connected, the Collection input is used instead. | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights?application_version=5.7#outputs)
