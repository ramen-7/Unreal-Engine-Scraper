<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions?application_version=5.7 -->

# TransformPositions

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
7. TransformPositions

# TransformPositions

TransformPositions (v1) Chaos Cloth Asset Transform Positions Node

On this page

### Description

TransformPositions (v1)

Chaos Cloth Asset Transform Positions Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Transform Positions |
| Type | [FChaosClothAssetTransformPositionsNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAssetTransformPositio-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bTransform2DSimPositions | Enable Transforming 2D Sim Mesh Positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Sim2DScale | 2D Sim Transform scale. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000) |
| Sim2DRotation | 2D Sim Transform rotation angle in degrees. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Sim2DTranslation | 2D Sim Transform translation. | [FVector2f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000) |
| Sim2DPattern | Sim Pattern to transform. All patterns will be used when set to -1. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |
| bTransform3DSimPositions | Enable Transforming 3D Sim Mesh Positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| Sim3DScale | 3D Sim Transform scale. | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Sim3DRotation | 3D Sim Transform rotation angle in degrees (Euler Angles) | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Sim3DTranslation | 3D Sim Transform translation. | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| bTransformRenderPositions | Enable Transforming Render Positions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| RenderScale | Render Transform scale. | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| RenderRotation | Render Transform rotation angle in degrees (Euler Angles) | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RenderTranslation | Render Transform translation. | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| RenderPattern | Render Pattern to transform. All patterns will be used when set to -1. | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | -1 |

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

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions?application_version=5.7#outputs)
