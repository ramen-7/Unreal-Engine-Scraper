<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine?application_version=5.7 -->

# Depth of Field

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
6. [Post Process Effects](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine "Post Process Effects")
7. Depth of Field

# Depth of Field

Using in-editor tools to simulate the distance between near and far objects to blur parts, not in focus.

![Depth of Field](https://dev.epicgames.com/community/api/documentation/image/6ecddb88-e487-4eea-85a9-de4d3e4820cf?resizing_type=fill&width=1920&height=335)

 On this page

Similar to what happens with real-world cameras, **Depth of Field** (DOF) applies a blur to a scene based on the distance in front of, or behind, a focal point. The effect can be used to draw the viewer's attention to a specific subject of the shot based on depth and adds an aesthetic to make the rendering appear more like a photograph, or film.

## Depth of Field Types

There are several methods of performing depth of field effects in Unreal Engine that you can use. These have been broken into two categories:

* **Cinematic:** This method provides a cinematic and filmic look to a depth of field effects. Adjustments for this method align more with common camera options available in photography and cinematography. This option works for Desktop and Console platforms.
* **Mobile:** This method provides optimized and lower-cost DOF options that work for Mobile platforms.

Select from the methods below to learn more about their features:

[![Cinematic Depth of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76c79b1b-2724-4b49-878a-b7a5aaa0f07d/dof_cine_topic.png)

Cinematic Depth of Field

Setting up and using depth of field on desktop and console platforms.](/documentation/en-us/unreal-engine/cinematic-depth-of-field-in-unreal-engine)
[![Mobile Depth of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c1998b8-ab46-42a7-8ff2-5db39f6079f2/placeholder_topic.png)

Mobile Depth of Field

Setting up and using depth of field on mobile platforms.](/documentation/en-us/unreal-engine/mobile-depth-of-field-in-unreal-engine)

## Implementation

Depth of Field is broken up into three layers (or region); Near, Far, and Focal Region. Each of these is processed separately and then later composited together to achieve the final image effect. Objects in the Near and Far layers are always fully blurred. They are blended with the non-blurred scene to achieve the final result.

![Depth Of Field Implementation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2b042c1-353a-4220-88d2-91b8f6128302/ue5_1-depth-of-field-layer-implementation-1.png)

* Objects within the **Focal Region** (Black) use the non-blurred scene layer. This layer can be very narrow—like here, where it is only focused on the character— or very wide, encompassing more of the scene's foreground and background.
* Objects in the **Near** (Green) or **Far** (Blue) that are outside any transition areas between the Focal Region and the Near or Far regions are fully blended to the blurred layer meaning they are out-of-focus.
* Objects within the transition area—like the area to the left of the car—are blended linearly between the non-blurred scene layer (for Near and Far) and their blurred layer based on their position within the transition of the Focal Region.

### Visualizing Depth of Field

These layers, including transition regions, can be visualized using the **Depth of Field Layers** show flag in the Level Viewport under **Show** \> **Visualize**.

![Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcd844d8-b9e7-4a3d-8648-c2d895834f03/ue5_1-1-depth-of-field-visualization-scene-view.png)

![Layer Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/446c6d48-fca3-4680-a98c-b5f33da9e212/ue5_1-1-depth-of-field-visualization.png)

Scene

Layer Visualization

Visualizing the **Depth of Field Layers** also includes useful information relevant to the DOF method being used, such as values that are currently set or when moving the mouse around the scene, the distance from the camera to the Actor is displayed next to the mouse cursor.

![Visualizing Depth Of Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e416314e-5ac2-4ed5-a3a6-e7206bfc257d/ue5_1-depth-of-field-visualization-stats.png)

### Using Depth of Field in the Editor

Using Depth of Field in Unreal Editor can be done in a few different ways; by placing a [Post Process Volume](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine), using a [Camera Actor](/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine). Each of these has access to DOF properties via the [Post Process Volume and Camera](/documentation/en-us/unreal-engine/cinematic-depth-of-field-in-unreal-engine#postprocessvolumeandcameraactor). For [Cine Camera](/documentation/en-us/unreal-engine/cinematic-depth-of-field-in-unreal-engine#cinematiccamera), there are some additional industry-standard settings for cameras and lenses.

The majority of settings used can be accessed under the **Lens** tab in the **Camera** and **Depth of Field** sections.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be75b9c0-9c40-4998-bc56-965b6ac51e9f/ue5_1-depth-of-field-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be75b9c0-9c40-4998-bc56-965b6ac51e9f/ue5_1-depth-of-field-properties.png)

Click the image for full size.

When using a [Cine Camera Actor](/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine), replacing properties that affect depth of field can be found under the **Current Camera Settings** in the **Lens Settings** section.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d908030-bf06-4f8e-857e-1422accb7403/ue5_1-depth-of-field-properties-cine-camera-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d908030-bf06-4f8e-857e-1422accb7403/ue5_1-depth-of-field-properties-cine-camera-actor.png)

Click the image for full size.

If you're using a Camera or Cine Camera Actor, you can inhabit them using Actor Piloting in the Level Viewport by selecting the **Perspective** and choosing from one of the placed **Cameras** in the scene.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdbb8d92-f8cb-481a-a141-33bf0a74fb9f/ue5_1-depth-of-field-pilot-camera.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdbb8d92-f8cb-481a-a141-33bf0a74fb9f/ue5_1-depth-of-field-pilot-camera.png)

Click the image for full size.

The Level Viewport will snap to the camera's view and indicate that you are piloting and viewing what that camera sees.

![Level Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a18fcb65-4cc9-451c-b0b2-e50e896052c8/ue5_1-depth-of-field-pilot-camera-status.png)

Any properties that are changed in the Camera or Post Process Volume (if the Camera is within it) will immediately take effect in the viewport.

To achieve similar results as the shot above, the key is to use a low **Aperture (F-stop**) to get a large Bokeh shape, move the camera or viewport position closer to an object and change the **Field of View** (FOV) to be lower. Then, adjust the **Focus Distance** to get some scene content to be out of focus in front and behind the focus plane.

### Using Cinematic Camera's Debug Focus Plane

While using the [Cine Camera Actor](/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine), enable **Draw Debug Focus Plane** to see where the focus is placed in your level.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1536b5f2-0215-479f-9b55-ce203fd2ede8/ue5_1-properties-cine-camera-actor-draw-focus-plane.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1536b5f2-0215-479f-9b55-ce203fd2ede8/ue5_1-properties-cine-camera-actor-draw-focus-plane.png)

Click the image for full size.

When enabled, the focus plane will be drawn at the currently set **Manual Focus Distance** from the camera. In this case, the character is the focal point where everything is sharp and in focus. Anything in front or behind the focus plane will be out of focus.

![Draw Debug Focus Plane: Disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16ffedc3-f989-49fc-825b-5db4693ab3ca/ue5_1-debug-focus-plane-disabled.png)

![Draw Debug Focus Plane: Enabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d82d1f5f-d4ac-479b-9168-8205d98ca975/ue5_1-debug-focus-plane-enabled.png)

Draw Debug Focus Plane: Disabled

Draw Debug Focus Plane: Enabled



Use **Debug Focus Plane Color** to customize the RGBA color values for the focus plane being drawn. This is helpful in scenes where it may be hard to see the focus plane being drawn.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [post process](https://dev.epicgames.com/community/search?query=post%20process)
* [depth of field](https://dev.epicgames.com/community/search?query=depth%20of%20field)
* [dof](https://dev.epicgames.com/community/search?query=dof)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Depth of Field Types](/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine?application_version=5.7#depthoffieldtypes)
* [Implementation](/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine?application_version=5.7#implementation)
* [Visualizing Depth of Field](/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine?application_version=5.7#visualizingdepthoffield)
* [Using Depth of Field in the Editor](/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine?application_version=5.7#usingdepthoffieldintheeditor)
* [Using Cinematic Camera's Debug Focus Plane](/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine?application_version=5.7#usingcinematiccamera'sdebugfocusplane)
