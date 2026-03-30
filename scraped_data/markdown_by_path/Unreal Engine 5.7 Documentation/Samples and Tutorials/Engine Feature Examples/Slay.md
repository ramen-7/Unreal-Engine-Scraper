<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7 -->

# Slay

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Engine Feature Examples](/documentation/en-us/unreal-engine/engine-feature-examples-for-unreal-engine "Engine Feature Examples")
7. Slay

# Slay

Fully realize your virtual production workflows in Unreal Engine by learning about Slay and its cinematic techniques.

![Slay](https://dev.epicgames.com/community/api/documentation/image/0e5eb53f-ce86-4e3e-b246-aae44fa14506?resizing_type=fill&width=1920&height=335)

 On this page

Virtual production is supported in Unreal Engine through the use of various cinematic tools, rendering features, and workflows. The Slay sample, built by **[Mold3D Studio](https://www.mold3dstudio.com/)**, was created to demonstrate techniques, rendering features, and workflows that can be achieved when considering virtual production in Unreal Engine.

This document provides an overview of how to view the Slay sample, as well as the workflows and production techniques that were used to create it.

#### Prerequisites

* The Slay sample content is a graphically intensive scene. It requires at least an **Intel Core i9 Series** processor and **GeForce RTX 2080 Ti,** or similar.
* When opening the project or Level for the first time, there may be a long initial load time as numerous assets are loaded and compiled for the first time.

## Setup

To set up a project with the Slay sample, follow these steps:

1. Access the [Slay sample](https://fab.com/s/6066e5de148a) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.
4. Open your new project in the Unreal Editor.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Viewing the Slay Sequence

To view the Slay sequence, click the **Cinematics** button in the main toolbar and select **TF\_Edit**.

[![open slay cinematic](https://dev.epicgames.com/community/api/documentation/image/7845ad8f-997e-49d1-96af-a9cddf7a0a3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7845ad8f-997e-49d1-96af-a9cddf7a0a3a?resizing_type=fit)

This will open the **[Master Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine)** for the Slay cinematic. You can see the multiple shots used to assemble the full sequence in this view.

[![slay master sequence](https://dev.epicgames.com/community/api/documentation/image/80186d3f-b41a-4793-aca2-66778a584ed1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80186d3f-b41a-4793-aca2-66778a584ed1?resizing_type=fit)

Select the **Camera** button on the Shot Track to look through the **[Cameras](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)** for each shot, and click the **Play** button to play the sequence.

[![play slay sequence](https://dev.epicgames.com/community/api/documentation/image/290c3309-145f-416b-9de5-7d622c0109d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/290c3309-145f-416b-9de5-7d622c0109d2?resizing_type=fit)

## Quixel Megascan Assets

The Temple Level was built using a combination of unique assets and **[Quixel Megascan](https://quixel.com/megascans/home)** assets. These assets were used in Slay to provide background details, props, and foliage. Using Quixel Megascan assets in your project can save time and resources when creating large environments.

[![slay quixel megascan](https://dev.epicgames.com/community/api/documentation/image/2138ddbd-73d9-4c69-a679-a8f4e5cba42f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2138ddbd-73d9-4c69-a679-a8f4e5cba42f?resizing_type=fit)

You can view some of the Quixel Megascan assets used in the Slay sample by navigating to the **[Quixel Megascan](https://quixel.com/megascans/home)** website. Some notable examples include:

* **[Gravestones](https://quixel.com/megascans/home?category=3D%20asset&category=historical&category=feudal%20japan&category=gravestone&search=gravestone)** in the Temple courtyard.

  [![quixel megascan grave](https://dev.epicgames.com/community/api/documentation/image/213fbecf-fd11-42b0-be07-c5faa53376f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/213fbecf-fd11-42b0-be07-c5faa53376f4?resizing_type=fit)
* **[Location or era-specific props](https://quixel.com/megascans/home?category=3D%20asset&search=japan)** placed around the Level.

  [![quixel megascan japan props](https://dev.epicgames.com/community/api/documentation/image/761c6757-1241-4a0e-baa2-77367edff6f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/761c6757-1241-4a0e-baa2-77367edff6f5?resizing_type=fit)
* **[Grass](https://quixel.com/megascans/home?category=3D%20plant&category=grass)** and other foliage placed in the gardens and other areas.

  [![quixel megascan grass](https://dev.epicgames.com/community/api/documentation/image/ee0b331a-6771-4c26-811b-5c61c65f0b84?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee0b331a-6771-4c26-811b-5c61c65f0b84?resizing_type=fit)

## Shot-Based Workflow

The Slay sequence was created using **[Sequencer](animating-characters-and-objects/Sequencer/)** and its **[Shot-Based](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine)** workflow. This was done so that each shot contains all necessary content for that shot only, rather than a larger single sequence. This setup allows for quick modifications to the sequence as a whole, as shots can be **[edited, trimmed, and re-arranged](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine)**, just like in any non-linear editing software.

In the Master Sequence **TF\_Edit**, you can see all the shots arranged in the **Shot Track**. Additionally there are **[Audio Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-audio-track-in-unreal-engine)** for playing audio that has been timed to the sequence edit, and a **[Fade Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine)** for controlling the fade to and from black.

[![slay master sequence](https://dev.epicgames.com/community/api/documentation/image/ebe9ec78-f18e-4315-91dc-5600d893c34a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ebe9ec78-f18e-4315-91dc-5600d893c34a?resizing_type=fit)

Double-click any shot to open and view its contents.

### Level Visibility

The first shot of Slay is an exterior view of the Temple. Because of this unique angle, it was necessary to create a custom **[Landscape](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine)** and assets for a Level that only is visible for the duration of **Shot TF0010\_02**. The Level's visibility is controlled by the **[Level Visibility Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-level-visibility-track-in-unreal-engine)**, and can be seen in shot **TF0010\_02** (Shot 1)

With the Level Visibility Track placed inside the shot, it will evaluate only for the duration of the shot. In this case, the Level containing the lower-resolution Landscape for use when inside the Temple is hidden, and the Level containing higher-resolution Landscape and other assets is displayed instead.

[![slay level visibility terrain](https://dev.epicgames.com/community/api/documentation/image/308cad99-5859-4105-9c19-1c17309e8d72?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/308cad99-5859-4105-9c19-1c17309e8d72?resizing_type=fit)

You can manually preview the higher-resolution Landscape Level by navigating to the **[Levels](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine)** panel, enabling **Terrain\_TF0010,** and disabling **Terrain**.

### Using Spawnables

**[Spawnables](https://dev.epicgames.com/documentation/en-us/unreal-engine/spawn-temporary-actors-in-unreal-engine-cinematics?application_version=5.5)** are Actors that are spawned and typically exist only for the duration of a single sequence. These are used extensively in several shots throughout the Slay sequence in order to address problems unique to each shot. Since each shot is its own sequence, spawnables will only exist for the duration of a shot, making it easier to manage these Actors.

An example of a spawnable Actor can be seen in **Shot TF0020\_01** (Shot 2). In this example, the original static mesh door is hidden and replaced with a spawnable **Skeletal Mesh** door, containing animation to match the character's movement as she opens it. When the shot ends, the door is unspawned automatically.

[![slay spawnable door actor](https://dev.epicgames.com/community/api/documentation/image/9d19c35b-1ef8-45cd-8be3-05825a99269f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d19c35b-1ef8-45cd-8be3-05825a99269f?resizing_type=fit)

### Artist Collaboration

In the Slay sample, each shot is its own sequence, and therefore its own asset. Shots also contain **[Subscene Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-subscequences-track-in-unreal-engine)** which are their own sequence assets as well. Because of this division of assets, it is much simpler to enable multiple artists to work on a single sequence or shot at the same time, without file conflicts occurring. Subscenes can also be duplicated, enabling the same contents to be reused and shared across multiple instances.

In several shots, you can see Subscene Tracks for both **Lighting** and **FX**, which enable artists from these disciplines to work within these sequences instead of the main shot sequence. In this way, subscenes are not only useful for limiting file conflicts, but also for Sequencer organization.

[![slay multi user subscene](https://dev.epicgames.com/community/api/documentation/image/48a8b53a-9c09-4e4c-adb4-64b1e2812d15?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48a8b53a-9c09-4e4c-adb4-64b1e2812d15?resizing_type=fit)

You can double-click a Subscene section to open it and view its contents.

[![subscene contents](https://dev.epicgames.com/community/api/documentation/image/290a164d-de5a-40e3-aa44-ce8c25fe1ef2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/290a164d-de5a-40e3-aa44-ce8c25fe1ef2?resizing_type=fit)

When a shot or subscene is opened from a parent sequence, it will be displayed within the context of the Master Sequence. This means that even though you are viewing only a single subscene, all tracks from the Master Sequence and current shot also remain visible. You can edit lights, add visual effects, and perform other actions with full visual context of the scene.

This context view can be enabled or disabled by toggling **Evaluate Sub Sequences In Isolation** from Sequencer's [Playback Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine).

### Camera Animation

The Camera animation for Slay was **[created](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine)** entirely in Sequencer. In some cases, additive camera animation is also used to enhance the camera movement. This is done using **[Camera Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/template-sequences-in-unreal-engine)**, which are a form of **[Template Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/template-sequences-in-unreal-engine)**.

[![additive camera animation](https://dev.epicgames.com/community/api/documentation/image/1a66ab02-3b4c-49cf-8d97-04a5874ccf7f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a66ab02-3b4c-49cf-8d97-04a5874ccf7f?resizing_type=fit)

Double-clicking one of these **Template Animations** will open the corresponding template sequence, where you can view the animation that is being used.

[![camera animation sequence](https://dev.epicgames.com/community/api/documentation/image/9a9f3f99-e36a-4aa0-9790-0d521e8eb10c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a9f3f99-e36a-4aa0-9790-0d521e8eb10c?resizing_type=fit)

## Lighting and Materials

Lighting, Materials, and Effect usage plays a critical role in the Slay sample. Proper utilization of the Master Sequence and Shot ecosystem enables artists to more effectively light and apply material adjustments for each shot.

### Lighting Workflows

As mentioned [previously](https://dev.epicgames.com/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine), lighting and other workflows can occur within Subscenes. Here, a typical lighting workflow would be to add your necessary **Light Actors** to the sequence as **[Spawnables](https://dev.epicgames.com/documentation/en-us/unreal-engine/spawn-temporary-actors-in-unreal-engine-cinematics?application_version=5.5)**. This is done so that the lights will only remain visible for the duration of the shot, and do not need to be manually turned on or off.

[![spawnable light](https://dev.epicgames.com/community/api/documentation/image/188e0cef-c8ea-4c67-a5b8-605e23b29ac7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/188e0cef-c8ea-4c67-a5b8-605e23b29ac7?resizing_type=fit)

Other lighting techniques can be used to enhance your shots, such as using **Light Blockers** to block out certain areas of a scene from the main Level's light. Afterward you can more directly control the lighting of a shot using your spawnable lights.

For example, in **Shot TF0020\_01** (Shot 2), if you disable the **Camera** button to stop piloting it, then navigate in the viewport to view the Temple entrance area, you should see a large **Light Blocker** being used. This is used so that a more controlled lighting environment can be created for the shot.

[![light blocker](https://dev.epicgames.com/community/api/documentation/image/47bd4985-1b39-41e9-bb2e-e0ebaa7671d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47bd4985-1b39-41e9-bb2e-e0ebaa7671d5?resizing_type=fit)

With the light blocker in place, other lights can be spawned to better enhance the lighting in this shot, such as the spotlight shining through the nearby lattice, which casts soft shadows on the door.

[![slay lighting](https://dev.epicgames.com/community/api/documentation/image/97aeb11e-5f11-49e0-b42b-36eb3681810d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97aeb11e-5f11-49e0-b42b-36eb3681810d?resizing_type=fit)

In some other cases, it may be necessary to hide certain meshes to let light pass through and shine on your Actors. In **Shot TF0080\_01**, part of the Temple structure is hidden in order to let the sunlight cast on the Oni character.

[![hide level for lights](https://dev.epicgames.com/community/api/documentation/image/9e7d3cd3-0050-4d7b-80f2-8944081a6179?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e7d3cd3-0050-4d7b-80f2-8944081a6179?resizing_type=fit)

**[Lighting Channels](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine)** are also used in Slay to control how lights affect the environment and characters. In this case, spawnable lights are only affecting **Channel 2**. This same channel is then enabled on all Characters, causing them to be lit by these lights. The environment is not lit by these lights because those meshes only have **Channel 0** enabled.

[![lighting channels](https://dev.epicgames.com/community/api/documentation/image/074fa2ca-054b-47c6-8a46-d319216884c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/074fa2ca-054b-47c6-8a46-d319216884c8?resizing_type=fit)

### Material Workflows

If a **[Material](designing-visuals-rendering-and-graphics/materials/)** is set up with **parameters**, you can reference these parameters in Sequencer to make overriding material parameter adjustments. In Slay, this was done to make minor adjustments to materials for specific shots. Similar to the previous lighting and shot-based workflows, these edits can be made on a per-shot basis without persisting to the next shot.

In Shot's **TF00110\_01 Lighting Subsequence**, you can see the **Roughness** and other parameters on Oni's armor material are adjusted using **Material Element Tracks**. The Material Element number corresponds to the same Material Element ID on the mesh.

[![material parameter track](https://dev.epicgames.com/community/api/documentation/image/043862c0-4a68-4d86-bcab-0ad2ad514428?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/043862c0-4a68-4d86-bcab-0ad2ad514428?resizing_type=fit)

Clicking **Add Parameter (+)** will reveal a list of the available material parameters for that element. Select a parameter to add it as a track.

[![add material](https://dev.epicgames.com/community/api/documentation/image/0b972c73-966b-4f83-91fe-092dd2c55e59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b972c73-966b-4f83-91fe-092dd2c55e59?resizing_type=fit)

## Render Settings

The Slay sample was created to be rendered as **Final Pixel** out, showcasing the high quality images that can be rendered with Unreal Engine. Because of this, there are several important parameters that are being set that increase the fidelity of the scene in both the viewport and when rendered using .

### Post Process Volume

**[Post Processing](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine)** is used in the scene to control **Ray Tracing** effects such as **Global Illumination, Reflections,** and **Shadows**. Color correction is also applied using **[Color Grading and the Filmic Tonemapper](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-grading-and-the-filmic-tonemapper-in-unreal-engine)** properties.

To view the post process properties being used in Slay, select the **Post Process Volume** in the Level. It can be found by searching for it in the .

[![post process volume](https://dev.epicgames.com/community/api/documentation/image/27370579-8d33-41a9-8172-1dbed2e4e7ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27370579-8d33-41a9-8172-1dbed2e4e7ce?resizing_type=fit)

You can preview the effects of the Post Process Volume by enabling or disabling the **Enabled** property in its details. Using post processing can help you in making your scenes appear more vibrant.

![Post Processing Off](https://dev.epicgames.com/community/api/documentation/image/8a3a285f-8e81-4713-8368-40174900179e?resizing_type=fit&width=1920&height=1080)

![Post Processing On](https://dev.epicgames.com/community/api/documentation/image/dcdd9cd5-6458-4500-9b94-601cb563314a?resizing_type=fit&width=1920&height=1080)

Post Processing Off

Post Processing On

### Viewport Optimization

As Slay is a graphically intense project, it became necessary to optimize the editor viewport experience to ensure smooth, reliable performance when working in Unreal Engine. This was done by setting certain [Console Variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) within the **DefaultEngine.ini** **[Configuration File](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine)**.

Some examples of the variables being set are:

C++

```
|  |  |
| --- | --- |
|  | r.HairStrands.Enable 1.0 |
|  | r.HairStrands.DeepShadow.Resolution 512.0 |
|  | r.RayTracing.Shadows.AcceptFirstHit 1.0 |
|  | r.RayTracing.SkyLight.ScreenPercentage 55.0 |
```

r.HairStrands.Enable 1.0
r.HairStrands.DeepShadow.Resolution 512.0
r.RayTracing.Shadows.AcceptFirstHit 1.0
r.RayTracing.SkyLight.ScreenPercentage 55.0

Copy full snippet(4 lines long)

To view the other console variables in use, you can navigate to the **Config** folder located in the install location of the Slay project and open **DefaultEngine.ini** in a text editor.

### Movie Render Queue Settings

The final picture for Slay is rendered using Unreal Engine's **[Movie Render Queue tool](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue)**. Movie Render Queue supports several features for producing high-quality renders, such as its temporal subsampling feature which is used to apply a high-quality radial motion blur effect. Additionally, Console Variables are used in Slay to increase graphical fidelity during the rendering process.

To open the Movie Render Queue window, click the **Render** button in Sequencer's Toolbar.

[![open movie render queue](https://dev.epicgames.com/community/api/documentation/image/fae96b02-2720-4e0f-a112-8a65e1ab71f1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fae96b02-2720-4e0f-a112-8a65e1ab71f1?resizing_type=fit)

The specific render settings used for Slay are saved as a **Movie Pipeline Master Config Asset**. To apply this preset to the render, click the **Settings** dropdown menu and select **Slay\_MovieRenderQueue\_Preset**.

[![render settings preset](https://dev.epicgames.com/community/api/documentation/image/795ff0a6-73da-46d1-9975-e9ec2f2a0f2d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/795ff0a6-73da-46d1-9975-e9ec2f2a0f2d?resizing_type=fit)

To see the settings being used, click the **Slay\_MovieRenderQueue\_Preset** settings text. This will open the **[Render Settings](animating-characters-and-objects/Sequencer/movie-render-pipeline/RenderSettings)** window which contains the various output, quality, and other settings applied during the rendering process.

[![render settings](https://dev.epicgames.com/community/api/documentation/image/a8aa1dde-8524-4542-8886-5d64f7c51ec9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8aa1dde-8524-4542-8886-5d64f7c51ec9?resizing_type=fit)

#### Anti-Aliasing

In order to reduce image noise, as well as to produce smoother edges and motion blur, [Anti-Aliasing](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) is used with **Temporal Sample Count** set to **19**.

[![slay anti aliasing render settings](https://dev.epicgames.com/community/api/documentation/image/25b6d5ce-bfae-4a0c-98b5-55e1a9ea4863?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25b6d5ce-bfae-4a0c-98b5-55e1a9ea4863?resizing_type=fit)

#### Console Variables

To increase graphical fidelity in several areas including **Motion Blur**, **Subsurface Scattering**, and **Raytracing**, the following [Console Variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) are used:

[![slay console variable render settings](https://dev.epicgames.com/community/api/documentation/image/14484424-51df-4bbe-9f54-4ac593b30872?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14484424-51df-4bbe-9f54-4ac593b30872?resizing_type=fit)

C++

```
r.MotionBlurQuality 4.0
	r.MotionBlurSeparable 1.0
	r.DepthOfFieldQuality 4.0
	r.ScreenPercentage 125.0
	r.ViewDistanceScale 50.0
	r.SSS.Quality 1.0
	r.SSR.Quality 4.0
	r.Shadow.DistanceScale 10.0
	r.ShadowQuality 5.0
	r.Shadow.RadiusThreshold 0.001
```

Expand code  Copy full snippet(22 lines long)

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#prerequisites)
* [Setup](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#setup)
* [Viewing the Slay Sequence](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#viewing-the-slay-sequence)
* [Quixel Megascan Assets](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#quixel-megascan-assets)
* [Shot-Based Workflow](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#shot-based-workflow)
* [Level Visibility](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#level-visibility)
* [Using Spawnables](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#using-spawnables)
* [Artist Collaboration](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#artist-collaboration)
* [Camera Animation](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#camera-animation)
* [Lighting and Materials](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#lighting-and-materials)
* [Lighting Workflows](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#lighting-workflows)
* [Material Workflows](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#material-workflows)
* [Render Settings](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#render-settings)
* [Post Process Volume](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#post-process-volume)
* [Viewport Optimization](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#viewport-optimization)
* [Movie Render Queue Settings](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#movie-render-queue-settings)
* [Anti-Aliasing](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#anti-aliasing)
* [Console Variables](/documentation/en-us/unreal-engine/slay-sample-project-for-unreal-engine?application_version=5.7#console-variables)
