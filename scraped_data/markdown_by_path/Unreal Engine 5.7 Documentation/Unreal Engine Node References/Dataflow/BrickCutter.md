<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter?application_version=5.7 -->

# BrickCutter

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
7. BrickCutter

# BrickCutter

BrickCutter (v1)

On this page

### Description

BrickCutter (v1)

Editor Fracture Mode / Fracture / Brick tool
Fracture with a customizable brick pattern.
Note: Currently only supports fracturing with at least some (non-zero) Grout.

Input(s) :
Collection [Intrinsic] - Collection to cut
BoundingBox - Boundingbox to create the cutting planes in
TransformSelection - The selected pieces to cut
Transform - Transform to apply to cut planes
BrickLength - Brick length (in cm)
BrickHeight - Brick height (in cm)
BrickDepth - Brick depth (in cm)
RandomSeed - Seed for random
ChanceToFracture - Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture.
Grout - Amount of space to leave between cut pieces
Amplitude - Size of the Perlin noise displacement (in cm). If 0, no noise will be applied
Frequency - Period of the Perlin noise. Smaller values will create a smoother noise pattern
Persistence - Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor
Lacunarity - Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor
OctaveNumber - Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity
Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains
PointSpacing - Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise
CollisionSampleSpacing - The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions
Only used if Add Samples For Collision is enabled

Output(s):
Collection [Passthrough] - Collection to cut
TransformSelection [Passthrough] - The selected pieces to cut
NewGeometryTransformSelection - Fractured Pieces

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Fracture |
| Type | [FBrickCutterDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBrickCutterDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Bond | The brick bond pattern defines how the bricks are arranged | [EFractureBrickBondEnum](/documentation/en-us/unreal-engine/API/Plugins/FractureEngine/EFractureBrickBondEnum) | Dataflow\_FractureBrickBond\_Stretcher |
| SplitIslands | Whether to split the fractured mesh pieces based on geometric connectivity after fracturing | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| AddSamplesForCollision | If enabled, add extra vertices (without triangles) to the geometry in regions where vertices are spaced too far apart (e.g. across large triangles) These extra vertices will be used as collision samples in particle-implicit collisions, and can help the physics system detect collisions more accurately Note this is *only* useful for simulations that use particle-implicit collisions | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| BoundingBox | Boundingbox to create the cutting planes in | [FBox](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Min=(X=0.000000,Y=0.000000,Z=0.000000),Max=(X=0.000000,Y=0.000000,Z=0.000000),IsValid=False) |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |
| Transform | Transform to apply to cut planes | [FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| BrickLength | Brick length (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 194.000000 |
| BrickHeight | Brick height (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 57.000000 |
| BrickDepth | Brick depth (in cm) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 92.000000 |
| RandomSeed | Seed for random | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |
| ChanceToFracture | Chance to fracture each selected bone. If 0, no bones will fracture; if 1, all bones will fracture. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Grout | Amount of space to leave between cut pieces | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Amplitude | Size of the Perlin noise displacement (in cm). If 0, no noise will be applied | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Frequency | Period of the Perlin noise. Smaller values will create a smoother noise pattern | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.100000 |
| Persistence | Persistence of the layers of Perlin noise. At each layer (octave) after the first, the amplitude of the Perlin noise is scaled by this factor | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| Lacunarity | Lacunarity of the layers of Perlin noise. At each layer (octave) after the first, the frequency of the Perlin noise is scaled by this factor | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 2.000000 |
| OctaveNumber | Number of fractal layers of Perlin noise to apply. Each layer is additive, with Amplitude and Frequency parameters scaled by Persistence and Lacunarity Smaller values (1 or 2) will create noise that looks like gentle rolling hills, while larger values (> 4) will tend to look more like craggy mountains | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 4 |
| PointSpacing | Distance (in cm) between vertices on cut surfaces where noise is added. Larger spacing between vertices will create more efficient meshes with fewer triangles, but less resolution to see the shape of the added noise | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 10.000000 |
| CollisionSampleSpacing | The number of centimeters to allow between vertices on the mesh surface: If there are gaps larger than this, add additional vertices (without triangles) to help support particle-implicit collisions Only used if Add Samples For Collision is enabled | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 50.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection to cut | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| TransformSelection | The selected pieces to cut | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| NewGeometryTransformSelection | Fractured Pieces | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter?application_version=5.7#outputs)
