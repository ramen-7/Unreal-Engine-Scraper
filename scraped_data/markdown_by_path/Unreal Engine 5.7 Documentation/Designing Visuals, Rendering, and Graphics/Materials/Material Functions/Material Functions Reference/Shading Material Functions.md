<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/shading-material-functions-in-unreal-engine?application_version=5.7 -->

# Shading Material Functions

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine "Material Functions")
8. [Material Functions Reference](/documentation/en-us/unreal-engine/unreal-engine-material-functions-reference "Material Functions Reference")
9. Shading Material Functions

# Shading Material Functions

Functions for handling special shading types, such as Fuzzy Shading networks.

![Shading Material Functions](https://dev.epicgames.com/community/api/documentation/image/1514517b-deaa-48c0-a057-051460139ce7?resizing_type=fill&width=1920&height=335)

 On this page

The Shading Material functions provide for specialized shading operations, such as fuzzy shading and adjusting the shape of a specular highlight.

## FuzzyShading

This function emulates a surface similar to velvet or moss, and is similar to a Fresnel calculation. Incidentally, it is also useful for shader effects such as a scanning electron microscope.

| Inputs | Description |
| --- | --- |
| **Diffuse (Vector3)** | Takes in a texture to be used as the diffuse color. |
| **Normal (Vector3)** | Takes in a normal map used to perturb the surface of the fuzzy result. |
| **CoreDarkness (Scalar)** | Value used to darken the object wherever its normals become parallel to the camera, generally toward the center. The higher the number, the darker the core. Default is 0.8. |
| **Power (Scalar)** | Controls the rate of falloff from the core to the edge. Default is 6.0. |
| **EdgeBrightness (Scalar)** | Controls how bright the surface becomes as its normals become perpendicular to the camera, generally toward the edges. |

![Fuzzy Shading](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b14c472-92fe-48fc-8690-20155df38007/fuzzy-shading.png)

## FuzzyShadingGrass

This function is designed to provide the diffuse portion of grass shading. Similar to FuzzyShading, this function allows you to blend in a new color at the edges by first desaturating by a given percentage and then applying a custom color to the desaturated area.

| Inputs | Description |
| --- | --- |
| **EdgeDesat (Scalar)** | 0-1 number controlling how much the edges of the object should be desaturated to make way for the edge color. |
| **EdgeColor (Vector3)** | This color will be applied to the edge area. Use *EdgeDesat* to desaturate that area if too much color mixing is taking place. |
| **Diffuse (Vector3)** | Takes in a texture to be used as the diffuse color. |
| **Normal (Vector3)** | Takes in a normal map used to perturb the surface of the fuzzy result. |
| **CoreDarkness (Scalar)** | Value used to darken the object wherever its normals become parallel to the camera, generally toward the center. The higher the number, the darker the core. Default is 0.8. |
| **Power (Scalar)** | Controls the rate of falloff from the core to the edge. Default is 6.0. |
| **EdgeBrightness (Scalar)** | Controls how bright the surface becomes as its normals become perpendicular to the camera, generally toward the edges. |

![Fuzzy Shading Grass](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/71f0c059-9f3d-49a1-abdf-2560e6e27b77/fuzzy-shading-grass.png)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [FuzzyShading](/documentation/en-us/unreal-engine/shading-material-functions-in-unreal-engine?application_version=5.7#fuzzyshading)
* [FuzzyShadingGrass](/documentation/en-us/unreal-engine/shading-material-functions-in-unreal-engine?application_version=5.7#fuzzyshadinggrass)
