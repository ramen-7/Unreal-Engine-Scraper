<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/reflections-material-functions-in-unreal-engine?application_version=5.7 -->

# Reflections Material Functions

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
9. Reflections Material Functions

# Reflections Material Functions

Functions for aiding in the calculation of values for a variety of reflection types.

![Reflections Material Functions](https://dev.epicgames.com/community/api/documentation/image/576c25bc-f229-4272-8e3b-bf262e2bda2f?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/022bd7bd-1a75-406a-a892-b35c650e97db/reflectionheader.png)

This example shows off the real-time reflection capabilities of Unreal Engine. The scene shows a subway terminal with a lot of water leaks, grimy ceramic tiles, dilapidated pipe work, and other worn-out environment details. In this document, we will give an overview of some of the Functions that you can use to manipulate reflections like these.

## ViewAlignedReflection

This function takes in a spherical reflection texture and aligns it to the view. The calculation can be offset by inputting a custom reflection vector.

| Inputs | Description |
| --- | --- |
| **ReflectionVector (Vector 3)** | Takes in an existing reflection vector that needs to be aligned to the view. |
| **ReflectionTexture (TextureObject)** | Takes in an existing reflection texture, which needs to be spherical. |
| Outputs |  |
| **Texture** | Outputs the resulting view-based reflection texture. |
| **UVs** | Outputs the UV coordinates of the reflection texture so they can be reapplied elsewhere. |

![View Aligned Reflection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40ec5e7b-e08e-4314-abc7-e9070c7a374a/view-aligned-reflection.png)

## WorldAlignedReflection

This function takes in an incoming sphere-based reflection texture and aligns it to the world coordinates. The calculation can be offset by inputting a custom reflection vector.

| Inputs | Description |
| --- | --- |
| **ReflectionVector (Vector 3)** | Takes in an existing reflection vector that needs to be aligned to the view. |
| **ReflectionTexture (TextureObject)** | Takes in an existing reflection texture, which needs to be spherical. |
| Outputs |  |
| **WorldReflection** | Outputs the world-based reflection texture. |
| **WorldReflectionShadowed** | Outputs a more highly contrasted version of the texture that can be applied in shadowed areas. |

![WorldAlignedReflection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab711a03-ac75-453c-bca0-27ccf578b853/worldalignedreflection_demo.png)

## CustomReflectionVector

This function uses a normal map to generate a reflection vector independent of the default reflection vector and the normal's input on the base shader.

| Inputs | Description |
| --- | --- |
| **Normal (Vector3)** | Takes in a normal map to be used as the basis for the custom reflection vector. |

![Custom Reflection Vector](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11a35821-32d4-46be-84ba-a0e66bc0c258/custom-reflection-vector.png)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [ViewAlignedReflection](/documentation/en-us/unreal-engine/reflections-material-functions-in-unreal-engine?application_version=5.7#viewalignedreflection)
* [WorldAlignedReflection](/documentation/en-us/unreal-engine/reflections-material-functions-in-unreal-engine?application_version=5.7#worldalignedreflection)
* [CustomReflectionVector](/documentation/en-us/unreal-engine/reflections-material-functions-in-unreal-engine?application_version=5.7#customreflectionvector)
