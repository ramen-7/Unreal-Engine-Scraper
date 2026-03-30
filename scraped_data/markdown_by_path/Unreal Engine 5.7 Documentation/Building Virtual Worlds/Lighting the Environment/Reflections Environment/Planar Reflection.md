<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7 -->

# Planar Reflection

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Reflections Environment](/documentation/en-us/unreal-engine/reflections-environment-in-unreal-engine "Reflections Environment")
8. Planar Reflection

# Planar Reflection

An overview of the planar reflections actor that can be used to create mirror-like reflections.

![Planar Reflection](https://dev.epicgames.com/community/api/documentation/image/8042a523-32e2-4a84-90c7-c0eab403663e?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** (UE) supports real-time **Planar Reflection** that can give more accurate looking reflections than **Screen Space Reflections** (SSR) provide but come with a higher rendering cost. This higher rendering cost is due to how Planar Reflection works, as Planar Reflection actually renders the level again from the direction of the reflection.

![Banner image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13b7c7f2-b8e0-4c55-a206-0985532480ca/plan-refl-banner.png)

### Screen Space Reflections VS Planar Reflections

Screen Space Reflections (SSR) are much more efficient than Planar Reflections when it comes to rendering, but are also much less reliable.The image comparison below shows the limits of SSR versus Planar Reflections.

![Screen Space Reflections](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1483378f-72b1-4ac0-b469-2d11ba58222b/01-plan-refl-scene-disabled.png)

![Planar Reflections](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/824cea89-a2cc-4de9-a8c7-08706da486bb/02-plan-refl-scene-enabled.png)

Screen Space Reflections

Planar Reflections

* **Screen Space Reflections:** The image on the left shows the limitation of Screen Space Reflections. Notice the significant amount of 'leaking' that happens at the edges of the image or the part of the pool towards the camera view where reflections start to fade out. This happens because SSR can not reflect objects that are off-screen.
* **Planar Reflections:** The image on the right shows the same level, however, this time, Planar Reflections have been enabled. Notice how there is no leaking in the image, even at the sides and edges of the pool, the reflection is consistent and accurate. This is because Planar Reflections can reflect objects that are off-screen regardless of camera view.

### Enabling Planar Reflections

To use enable and use Planar Reflections in your project you will need to do the following:

1. Click the **Edit** in the **Main** menu panel, select **Project Settings**.

   ![Open Project Setting menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ac3cf9f-8e41-41b4-8ddc-89735b968182/03-plan-refl-project-settings.png)
2. In the **Project Settings** menu, navigate to the **Rendering > Reflections** section.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f8ab8a1-d5ea-4ed2-b1f1-0808c204f013/04-plan-refl-rendering-reflection-section.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f8ab8a1-d5ea-4ed2-b1f1-0808c204f013/04-plan-refl-rendering-reflection-section.png)

   Click image for full size.
3. Click on the check box next to **Support global clip plane for Planar Reflections**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84457667-cfd7-40b8-b3c4-6b3420123188/05-plan-refl-enable-support-planar-reflection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84457667-cfd7-40b8-b3c4-6b3420123188/05-plan-refl-enable-support-planar-reflection.png)

   Click image for full size.

   Failing to re-start the UE Editor after Planar Reflections are enabled will result in Planar Reflections not working.
4. Restart the UE Editor when prompted.

   ![Restart UE Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fce86c80-bfe7-41c9-8077-287a17a7ecdd/06-plan-refl-restart-ue-editor.png)
5. Once the UE Editor has restarted, go to the **Place Actors** panel and in the **Visual Effects** tab, select and drag a **Planar Reflection Actor** to the Level.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a222f9c1-b516-4693-acbc-8d4263d0bdea/07-plan-refl-add-planar-reflection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a222f9c1-b516-4693-acbc-8d4263d0bdea/07-plan-refl-add-planar-reflection.png)

   Click image for full size.
6. With the Planar Reflection Actor now placed in the level, you can now use the **G** key to hide and unhide the Actor. You can also use the **Move**, **Rotate**, and **Scale** tools to better position and size the Planar Reflection Actor to meet your levels needs.

Any nearby reflective Materials will automatically be affected by the Planar Reflection Actor as soon as it is added to the level. Static Meshes that are placed in the level will also have their normals used to distort the reflection, allowing for the simulation of waves.

### Planar Reflection Actor Properties

The Planar Reflection Actor has a number of properties that when adjusted can significantly affect the look of the reflection. The following table outlines these properties and how they will change the look of the Planar Reflection.

![Planar Reflection properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7bff69a7-1197-467a-93fe-ef9016d12f12/08-plan-refl-planar-refl-properties.png)

| Properties | Description |
| --- | --- |
| **Normal Distortion Strength** | Controls the strength of normals when distorting the planar reflection. |
| **Prefilter Roughness** | The roughness value to prefilter the planar reflection texture with. This is useful for hiding low resolutions. Larger values have a larger GPU cost. |
| **Distance from Plane Fadeout Start** | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| **Distance from Plane Fadeout End** | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| **Angle from Plane Fade Start** | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |
| **Angle from Plane Fade End** | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |
| **Show Preview Plane** | Toggles the visibility of the reflection plane while working in the Editor. This does not affect the planar reflection. |
| Advanced Properties |  |
| **Prefilter Roughness Distance** | The distance at which the prefilter roughness value will be achieved. |
| **Screen Percentage** | Downsample percent can be used to reduce GPU time rendering the planar reflection. This directly affects the quality of the reflection produced by the planar reflection. |
| **Extra FOV** | Addtional Field of View (FOV) used when rendering to the reflection tetxure. This is useful when normal distortion is causing reads outside the reflection texture. Larger values increase rendering thread and GPU cost, as more objects and triangles have to be rendered into the planar reflection. |
| **Render Scene Two-Sided** | Whether to render the scene as two-sided, which can be useful to hide artifacts where normal distortion would read "under" an object that has been clipped by the reflection plane. With this setting enabled, the backfaces of a mesh woul dbe displayed in the clipped region instead of the background which is potentially a bright sky. Be sure to add the water plane to the **Hidden Actors** if enabling this, as water plane will not block the reflection. |
| **LOD Distance Factor** | Scales the distance used by Level of Detail (LOD). Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass. |

### Planar Reflections Actor Scene Capture Properties

The Planar Reflection Actor also has a number of properties that enable you to control the performance cost of the realtime reflection that is captured.

![Scene Capture properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f80f705-a63a-4e04-9e93-64d043dc4c38/09-plan-refl-scene-capture-properties.png)

| Property | Description |
| --- | --- |
| **Primitive Render Mode** | Controls what primitives get rendered into the scene capture.   * **Render Scene Primtive (Legacy)** - Renders all primitives in the scene; * **Render Scene Primtives** - Renderes all primitives in the scene except any added to the **Hidden Actors** list; * **Use ShowOnly List** - Renders only Actors listed in the **Show Only Actors** list. |
| **Capture Source** | Controls capture source type.   * **Scene Color (HDR) in RGB, Inv Opacity in A**; * **Scene Color (HDR) in RGB, 0 in A**; * **Final Color (LDR) in RGB** * **Scene Color (HDR) in RGB, Scene Depth in A**; * **Scene Depth in R**; * **Device Depth in RGB**; * **Normal in RGB (Deferred Renderer only)**; * **Base Color in RGB (Deferred Renderer only)**; * **Final Color (HDR) in Linear sRGB gamut**; * **Final Color (with tone curve) in Linear sRGB gamut**. |
| **Capture Every Frame** | Whether to update the capture's contents every frame. If disabled, the component will render once on load and then only when moved. |
| **Capture on Movement** | Whether to update the capture's contents on movement. It is disabled if you are going to capture manually from Blueprint. |
| **Always Persist Rendering State** | Whether to persist the rendering state even if **Capture Every Frame** is disabled. This enables velocities for Motion Blur and Temporal Anti-Aliasing (TAA) to be computed. |
| **Hidden Actors** | A list of selected Actors available in the level to hide in the scene capture. |
| **Show Only Actors** | A list of Actors available in the level that will be rendered by this scene capture when using the **Primitive Render Mode** for **Use ShowOnly List**. |
| **Max View Distance Override** | Sets the maximum render distance (in centimeters) for primtives rendered in the scene capture when values are greater than 0. This can be used to cull distance objects from a reflection if the reflecting plane is in an enclosed areas like a hallway or room. |
| **Capture Sort Priority** | Sets the capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. The highest value will come first. |
| **Use Ray Tracing if Enabled** | Whether to use ray tracing for this capture. Ray Tracing must be enabled in the project. |
| **Profiling Event Name** | Sets a name for the profiling event when profiling the GPU. This is useful to know which planar reflection is being used when using multiple ones in your levels. |
| Advanced Properties |  |
| **General Show Flags** | Common feature show flags that toggles some features and Actors from being rendered to the scene capture. For example, Anti-aliasing, Fog, Static and Skeletal Meshes, and more. |
| **Advanced Show Flags** | Common advanced feature show flags that toggles some features and Actors from being rendered to the scene capture. For example, Foliage, Instanced Static Meshes, Paper 2D Sprties, and more. |
| **Post Processing Show Flags** | Toggles show flags for Bloom, Eye Adaptation, and Motion Blur from being rendered to the scene capture. |
| **Light Types Show Flags** | Toggles show flag for Sky Lighting from being rendered to the scene capture. |
| **Lighting Components Show Flags** | Toggles show flags for Ambient Occlusion and Dynamic Shadows from being rendered to the scene capture. |
| **Lighting Features Show Flags** | Toggles common show flags for Lighting features from being rendered to the scene capture. For example, Distance Field Ambient Occlusion (DFAO), Light Functions, Screen Space Reflections, and more. |
| **Hidden Show Flags** | Toggles show flags for Lighting and Post Processing from being rendered to the scene capture. |

## Planar Reflection Limitations

While Planar Reflections offer some very realistic reflections, this features does have a number of limitations which are listed below.

* Planar Reflections cause your entire scene to be rendered twice, so you'll want to budget half your frame time for it on the Rendering thread and GPU!
* Limit the number of Planar Reflections placed in the world. Often times, one will still be too much.
* Size it appropriately, which enables it to be culled when not visible.
* The cost to render the Planar Reflection Actor comes directly from what is currently being rendered in the level. Scenes that are triangle and draw call heavy will suffer the most performance issues when this feature is enabled because those costs don't scale with Screen Percentage.

## Planar Reflection Performance

While enabling and using Planar Reflections in your project will give you crisp and reasonably accurate reflections, this option will have a direct impact on the project's performance. In the following section, we will take a look at the performance impact enabling Planar Reflections will have in a high-end PC project as well as a project that is geared towards mobile devices.

Examples below use the **Kite & Infinity Blade Grass Lands** project for demonstrating the performance impact of the Planar Reflections. You can find this project in the **Marketplace** of the **Epic Games Laincher**.

### Planar Reflection Performance & Kite Demo

Due to the size and varying height of the Kite demos Landscape terrain, adding and then scaling a single Planar Reflection Actor to encompass the entire level would not work and could lead to very poor performance. Instead, Planar Reflection Actors were strategically placed and scaled to fit areas of the level that needed them. In the following image, we can see what the visual impact Planar Reflections have on water used the Kite demo.

![Planar Reflections Off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb919fe3-a3db-4a68-83c2-95b258765d42/10-plan-refl-ssr-reflections.png)

![Planar Reflections On](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f50f584a-ca5b-49d7-8204-691c0788dd40/11-plan-refl-pr-reflections.png)

Planar Reflections Off

Planar Reflections On

While the visual impact Planar Reflections have on the level is quite dramatic, so is the impact they have on performance. If you take a look at the left hand image below, **Planar Reflection Off**, you will see that the entire level is taking 31 ms to render. If you take a look at the right hand image, **Planar Reflections On**, you will see that the entire level is taking 29.19 ms to render. On top of that, Planar Reflection are adding an additional 23.07 ms of rendering time bring the total time to render the scene with Planar Reflections enabled to around 52 ms.

|  |  |
| --- | --- |
| GPU Visualizer for Level with Planar Reflection Off | GPU Visualizer for Level with Planar Reflection On |
| Planar Reflection Off | Planar Reflection On |
| *Click for full image* | *Click for full image* |

The reason why Planar Reflections are taking around 31 ms to render is due to the fully dynamic lighting and shadowing used in Kite. Levels that make use of Stationary / Precomputed lighting and shadowing will be much more efficient when rendered again for the Planar Reflection.

### Planar Reflection Performance & Infinity Blade Dungeons

Due to the size and layout of the Infinity Blade Elven Ruins map, only one Planar Reflection was needed and it was scaled to match the already existing water Static Mesh that was placed in the level. In the following images, we can see the visual impact adding a Planar Reflection has on the look of the water in the Elven Ruins map.

![Planar Reflections Off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c22b665-9512-4c15-88c1-2cced29b6a8c/14-plan-refl-ssr-reflections-1.png)

![Planar Reflections On](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a7a5508-778a-45ed-ae9b-8d5ab422efc1/15-plan-refl-pr-reflections-1.png)

Planar Reflections Off

Planar Reflections On

While adding a Planar Reflection makes the water look more lifelike, the impact it has on performance is quite small when compared to the Kite Demo. If you take a look at the image on the left hand side below, Planar Reflections Off, you can see that without Planar Reflections the scene is costing around 11 ms to render. If you take a look at the image on the right hand side, Planar Reflections On, you can see that with Planar Reflections cost around 1.67 ms to rendering bring the total time to render the level to around 13 ms.

|  |  |
| --- | --- |
| GPU Visualizer for Level with Planar Reflection Off | GPU Visualizer for Level with Planar Reflection On |
| Planar Reflection Off | Planar Reflection On |
| *Click for full image* | *Click for full image* |

The reason that Planar Reflections only cost 1.67 ms to render in the Elven Ruins map versus the 23.07 ms that it takes to render the Planar Reflections in the Kite Demo is due to how the Static Meshes and Materials that are used in the Elven Ruins were built. Since the Elven Ruins map and its content was designed for mobile devices, close attention was paid to the amount of triangles and Material instructions each asset used. Because of this, when Planar Reflections are enabled in the Elven Ruins map, they will cost less as the assets that are used in the map are greatly reduced in complexity and size when compared to the Kite Demo assets.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [reflections](https://dev.epicgames.com/community/search?query=reflections)
* [planar reflections](https://dev.epicgames.com/community/search?query=planar%20reflections)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Screen Space Reflections VS Planar Reflections](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#screenspacereflectionsvsplanarreflections)
* [Enabling Planar Reflections](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#enablingplanarreflections)
* [Planar Reflection Actor Properties](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#planarreflectionactorproperties)
* [Planar Reflections Actor Scene Capture Properties](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#planarreflectionsactorscenecaptureproperties)
* [Planar Reflection Limitations](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#planarreflectionlimitations)
* [Planar Reflection Performance](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#planarreflectionperformance)
* [Planar Reflection Performance & Kite Demo](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#planarreflectionperformance&kitedemo)
* [Planar Reflection Performance & Infinity Blade Dungeons](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine?application_version=5.7#planarreflectionperformance&infinitybladedungeons)
