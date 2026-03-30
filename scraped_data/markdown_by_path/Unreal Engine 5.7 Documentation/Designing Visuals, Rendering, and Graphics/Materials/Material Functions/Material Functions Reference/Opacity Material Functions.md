<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/opacity-material-functions-in-unreal-engine?application_version=5.7 -->

# Opacity Material Functions

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
9. Opacity Material Functions

# Opacity Material Functions

Functions to handle opacity values within a Material network.

![Opacity Material Functions](https://dev.epicgames.com/community/api/documentation/image/0da16947-e237-415b-9a9a-370f1cd24614?resizing_type=fill&width=1920&height=335)

 On this page

Opacity Material Functions exist to speed up the handling of complex opacity calculations.

## SoftOpacity

The **SoftOpacity** function takes in an Opacity value and then runs a variety of calculations on it to give it a softer feel. It applies a Fresnel effect, depth-based alpha, and pixel depth. The end result causes the object to fade away as the camera approaches it.

| Item | Description |
| --- | --- |
| Inputs |  |
| **DepthFadeDistance (Scalar)** | The depth at which objects have completely faded away. Only viable if using the *OutputUsesDepthBias* output. |
| **OpacityIn (Scalar)** | This is the incoming opacity value. |
| **FadeDistance (Scalar)** | How close you should get to the surface before it starts fading out. |
| Outputs |  |
| **OutputUsesDepthBias** | This output causes the object to fade completely away to complete transparency by the time it reaches the distance set in the *DepthFadeDistance* input. |
| **OutputNoDepthBias** | This output causes the object to fade completely away as it reaches the camera, meaning there is no offset. This output is 12 instructions less expensive than *OutputUsesDepthBias*. |

![Soft Opacity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f12cc3b-5b1a-45ce-b283-f0e3e8930eb3/soft-opacity.png)

In this example, the cylinder appears more transparent along the edges, where the mesh curves away from the camera. This is due to the Fresnel effect in the Material Function.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [SoftOpacity](/documentation/en-us/unreal-engine/opacity-material-functions-in-unreal-engine?application_version=5.7#softopacity)
