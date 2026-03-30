<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection?application_version=5.7 -->

# BakeTextureFromCollection

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
7. BakeTextureFromCollection

# BakeTextureFromCollection

BakeTextureFromCollection (v1)

On this page

### Description

BakeTextureFromCollection (v1)

* Bake a texture from a geometry collection
* Output to a 4 channels Image object ( RGBA )

Input(s) :
Collection [Intrinsic] - Target Collection
FaceSelection - selection of faces to bake : if not connected, all faces will be used
Resolution - resolution of the image to bake
GutterSize - Approximate space to leave between UV islands, measured in texels
UVChannel - Index of the added UV channel
MaxDistance - Max distance to search for the outer mesh surface
OcclusionRays - Number of occlusion rays
OcclusionBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur)
CurvatureBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur)
VoxelResolution - Voxel resolution of smoothed shape representation
SmoothingIterations - Amount of smoothing iterations to apply before computing curvature
ThicknessFactor - Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size
MaxCurvature - Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. Values outside that range will be clamped

Output(s):
Collection [Passthrough] - Target Collection
Image - Output image with the bake attributes
UVChannel [Passthrough] - Index of the added UV channel

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Texture |
| Type | [FBakeTextureFromCollectionDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBakeTextureFromCollectionDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RedChannel | Attribute to bake in the red channel | [ECollectionBakeTextureAttribute](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | DistanceToExternal |
| GreenChannel | Attribute to bake in the green channel | [ECollectionBakeTextureAttribute](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | AmbientOcclusion |
| BlueChannel | Attribute to bake in the blue channel | [ECollectionBakeTextureAttribute](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | Curvature |
| AlphaChannel | Attribute to bake in the alpha channel | [ECollectionBakeTextureAttribute](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ECollectionBakeTextureAttribute) | None |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| FaceSelection | selection of faces to bake : if not connected, all faces will be used | [FDataflowFaceSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) | () |
| UVChannel | Index of the added UV channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| GutterSize | Approximate space to leave between UV islands, measured in texels | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 1 |
| Resolution | resolution of the image to bake | [EDataflowImageResolution](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution512 |
| MaxDistance | Max distance to search for the outer mesh surface | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| OcclusionRays | Number of occlusion rays | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |
| OcclusionBlurRadius | Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.250000 |
| CurvatureBlurRadius | Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.250000 |
| VoxelResolution | Voxel resolution of smoothed shape representation | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 128 |
| SmoothingIterations | Amount of smoothing iterations to apply before computing curvature | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 10 |
| ThicknessFactor | Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 4.000000 |
| MaxCurvature | Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. Values outside that range will be clamped | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Target Collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| Image | Output image with the bake attributes | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |
| UVChannel | Index of the added UV channel | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection?application_version=5.7#outputs)
