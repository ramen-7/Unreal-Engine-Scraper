<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine?application_version=5.7 -->

# Depth Material Expressions

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
7. [Material Expressions Reference](/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference "Material Expressions Reference")
8. Depth Material Expressions

# Depth Material Expressions

Material expressions that deal with depth of the pixel being rendered.

![Depth Material Expressions](https://dev.epicgames.com/community/api/documentation/image/8fc86a1f-2320-494e-9a54-275c38ac5d02?resizing_type=fill&width=1920&height=335)

 On this page

## DepthFade

The **DepthFade** Material Expression is used to hide unsightly seams that occur when translucent objects intersect with opaque ones.

| Property | Description |
| --- | --- |
| **Fade Distance** | World space distance over which the fade should take place. This is used if the FadeDistance input is unconnected. |
| Inputs |  |
| **Opacity** | Takes in the existing opacity for the object prior to the depth fade. |
| **FadeDistance** | World space distance over which the fade should take place. |

In the comparison below, a translucent sphere intersects an opaque one (green). Note the smoother transition when DepthFade is used.

![Without Depth Fade](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d86702e3-c42f-445d-bf13-d9a9ce1de887/depth-fade-slider-01.png)

![With Depth Fade](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3b59de9-9780-4bac-9aef-75a3677dfa0e/depth-fade-slider-02.png)

Without Depth Fade

With Depth Fade

The Material network for this example is pictured below.

![Depth Fade Material Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6064fe2-1be1-497c-941e-4ee1877f5967/depth-fade-graph.png)

## PixelDepth

The **PixelDepth** Material Expression outputs the depth, or distance from the camera, of the pixel currently being rendered.

|  |  |
| --- | --- |
| Pixel Depth Example | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c8144c3-930d-4e7c-be4b-aceb0bdcdc66/pixel-depth-graph.png) |
| Result | Material Graph (Click to enlarge.) |

In this example, the Material network was applied to the floor. Notice how the linear interpolation blends between the two colors as the floor recedes beyond 2048 units. A Power expression was used to boost the contrast between the two colors and yield a more meaningful visual result.

## SceneDepth

The **SceneDepth** Material Expression outputs the existing scene depth. This is similar to [PixelDepth](/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine#pixeldepth), except that PixelDepth can sample the depth only at the pixel currently being drawn, whereas SceneDepth can sample depth at **any location**.

Only translucent materials may utilize SceneDepth.

| Inputs | Description |
| --- | --- |
| **UVs** | Takes in UV texture coordinates used to determine how the depth "texture" is sampled. |

|  |  |
| --- | --- |
| Scene Depth Example | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9e93741-3e9c-460e-8a84-f795460b1adf/scene-depth-graph.png) |
| Result | Material Graph (Click to enlarge.) |

In this example, we have applied the material network to a translucent sphere. Notice how the SceneDepth node is reading the pixels behind the sphere, rather than the ones on its surface.

The resulting normalized depth is linear in the 0.0 to 1.0 range.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [DepthFade](/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine?application_version=5.7#depthfade)
* [PixelDepth](/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine?application_version=5.7#pixeldepth)
* [SceneDepth](/documentation/en-us/unreal-engine/depth-material-expressions-in-unreal-engine?application_version=5.7#scenedepth)
