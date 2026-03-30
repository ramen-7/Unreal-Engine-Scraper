<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7 -->

# Color Management with OpenColorIO

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Managing Color](/documentation/en-us/unreal-engine/managing-color-in-unreal-engine "Managing Color")
7. Color Management with OpenColorIO

# Color Management with OpenColorIO

Ensure color consistency across projects with OpenColorIO.

![Color Management with OpenColorIO](https://dev.epicgames.com/community/api/documentation/image/e02f3a8d-5a38-4a79-8941-106645f8ac2e?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine 5 supports OCIO v2. For more information about the features included in OCIO v2, refer to the [OCIO documentation](https://opencolorio.readthedocs.io/en/latest/upgrading_v2/how_to.html).

[OpenColorIO](http://opencolorio.org/) (**OCIO**) is a color management system used primarily in film and virtual production. OCIO guarantees the colors of captured video remain consistent through the entire film pipeline. This pipeline includes initial camera capture, all the compositing applications that need to work with the captured media, and the final render.

**Unreal Engine** (UE) offers support for using OCIO to convert the colors of linear media in several ways:

* When you use media sources like captured clips or live feeds in your project, you can apply color conversion to make those media sources match your computer-generated elements in UE.
* You can use OCIO to apply color conversions to your Viewport and Play in Editor (PIE) windows. This means your reference frames in the editor will be consistent with your chosen color space.
* You can re-apply another color conversion to the composited feed you output from [Composure](/documentation/404). This helps make your CG elements and live frames blend more convincingly, while preserving the colors of the original shots faithfully.
* You can use Displays and Views to apply color conversions to multiple physical or virtual display devices from the same OCIO configuration.
* You can apply color space transformations to [nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine) renders on monitors and LED walls.
* When you export a video through [Movie Render Queue](/documentation/404), you can apply a color space transformation to your output video or image sequence.

All OCIO features in the engine rely on an **OpenColorIO Configuration Asset**, which you use to manage the color profiles that you want to work with.

The OpenColorIO Configuration Asset references an OCIO configuration (`.ocio`) file, which contains detailed specifications about multiple color profiles and how to transform between them. UE currently supports OCIO v2. For more details on OCIO configuration files, refer to the [OpenColorIO v2 documentation](https://opencolorio.readthedocs.io/en/latest/index.html).

This page contains links to documentation about creating an OpenColorIO Configuration Asset and applying color transformations in the engine.

## Quick Start

This page guides you through creating an OpenColorIO Configuration Asset.

[![OpenColorIO Quick Start](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/031e2255-6539-439e-a665-755b7948af3d/placeholder_topic.png)

OpenColorIO Quick Start

Create OpenColorIO Configuration Assets from OpenColorIO configuration files.](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine)

## Converting Colors in the Viewport

The Editor supports applying OCIO color conversions to the Level Viewport through **Viewport View Modes** and to Play in Editor mode through Blueprints. This page shows how to apply color transformations to the Level Viewport and Play in Editor mode.

[![Convert Colors in the Viewport and Play in Editor mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f098823-b637-4b6a-8b9e-c7aebe7b4df0/placeholder_topic.png)

Convert Colors in the Viewport and Play in Editor mode

Apply color conversion to the Level Viewport and Play in Editor with OpenColorIO in Unreal Engine](/documentation/en-us/unreal-engine/apply-color-conversion-to-the-level-viewport-and-play-in-editor-with-opencolorio-in-unreal-engine)

## Converting Colors in Blueprints

This page describes how to use **Blueprints** to apply color transformations.

[![Converting Colors in Blueprints](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1b38a96-de20-4e42-bb13-3ab1cad47b63/placeholder_topic.png)

Converting Colors in Blueprints

Apply color transformation using Blueprints with OpenColorIO in Unreal Engine](/documentation/en-us/unreal-engine/converting-colors-in-unreal-engine-blueprints)

## Converting Colors in nDisplay

[nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine) supports applying OCIO color conversions to nDisplay renders for the entire cluster, the inner frustum, or individual cluster nodes. This can be useful for managing the color spaces of specific displays. This page explains how to use OCIO with nDisplay.

[![Color Management in nDisplay](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e5e92f3-b6a0-4e40-8911-d3b18d8a232d/placeholder_topic.png)

Color Management in nDisplay

Using nDisplay color management tools.](/documentation/en-us/unreal-engine/color-management-in-ndisplay-in-unreal-engine)

## Converting Colors in Movie Render Queue

[Movie Render Queue](/documentation/404) supports applying OCIO color conversions to media exports. This page shows how to set the color conversion in Movie Render Queue.

[![Image Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f27b8fe7-b921-468a-8aa1-fcd50d69a507/placeholder_topic.png)

Image Settings

Adjust the picture quality of your render with Movie Render Queue's Image Settings](/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine)

## Converting Colors in Composure

[Composure](/documentation/404) supports applying OCIO color conversions to input and output media. This page explains how to apply color transformations in Composure.

[![Converting Colors in Composure with OpenColorIO](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8fe5435f-1eba-42dc-99a2-324e61015ff4/placeholder_topic.png)

Converting Colors in Composure with OpenColorIO

Apply color transformation to a Composure Element and to the composited output with OpenColorIO in Unreal Engine.](/documentation/en-us/unreal-engine/converting-colors-in-composure-with-opencolorio-in-unreal-engine)

* [vfx](https://dev.epicgames.com/community/search?query=vfx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Quick Start](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7#quickstart)
* [Converting Colors in the Viewport](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7#convertingcolorsintheviewport)
* [Converting Colors in Blueprints](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7#convertingcolorsinblueprints)
* [Converting Colors in nDisplay](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7#convertingcolorsinndisplay)
* [Converting Colors in Movie Render Queue](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7#convertingcolorsinmovierenderqueue)
* [Converting Colors in Composure](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine?application_version=5.7#convertingcolorsincomposure)
