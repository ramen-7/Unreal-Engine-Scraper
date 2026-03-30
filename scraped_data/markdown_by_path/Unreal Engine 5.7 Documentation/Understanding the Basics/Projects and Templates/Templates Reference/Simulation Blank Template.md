<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/simulation-blank-template-in-unreal-engine?application_version=5.7 -->

# Simulation Blank Template

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Projects and Templates](/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine "Projects and Templates")
7. [Templates Reference](/documentation/en-us/unreal-engine/unreal-engine-templates-reference "Templates Reference")
8. Simulation Blank Template

# Simulation Blank Template

Introduction to the Simulation Blank template in Unreal Engine

![Simulation Blank Template](https://dev.epicgames.com/community/api/documentation/image/61725ea1-b9fe-43c8-a776-64bd6600c5cf?resizing_type=fill&width=1920&height=335)

 On this page

The **Simulation Blank** template is an **Empty World** Level template enriched with simulation-specific settings and functionality. It consists of an empty environment with the following features and characteristics:

* A flat Static Mesh as the ground/floor.
* A [SunSky](/documentation/en-us/unreal-engine/geographically-accurate-sun-positioning-tool-in-unreal-engine) system with Earth-specific settings:

  + North offset compatible with the GeoReferencing plugin conventions.
  + A directional light with realistic Sun properties (**Intensity**, **Source Angle**), casting far shadows that leverage the [Virtual Shadow Maps](/documentation/404) system (requires enabling the **DirectX 12 (SM6. Experimental)** option under **Project Settings > Platforms - Windows** and a compatible graphics card).
* [Volumetric clouds](/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine), with a natural-looking material.
* [Exponential Height Fog](/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine).
* Stars (note that these are for cosmetic purposes only, and do not accurately represent realistic star positioning for any given real-world location).
* A global Post-Process Volume with **Exposure** settings corresponding to human vision.
* A [Georeferencing](/documentation/en-us/unreal-engine/georeferencing-a-level-in-unreal-engine) Actor to locate the environment on Earth.

The Geographic location of the UE origin in the SunSky and Georeferencing Actors has been set to 73W, 45N. You'll have to adapt it to your actual environment location if needed.

This template also comes with a custom `BP_SimGameMode` Blueprint that defines a specific `BP_SimPlayerController` and `BP_SimfloatingPawn`. These Blueprints are provided as an example of how to enhance the default features of the base Controller and Pawn classes and are explained below.

## The Simulation Player Controller (BP\_SimPlayerController)

This controller comes with some key shortcuts to allow the following player actions at runtime:

* Navigate freely with a floating Pawn spawned on play (`BP_SimfloatingPawn`).
* Alternate between this floating Pawn and a Pawn that already exists in the Level.
* Control the time of day.
* Display a profiling and stats widget.
* Display the Geospatial location status bar.

The following keyboard shortcuts are available:

| **Key** | **Action** |
| --- | --- |
| Pawn controls |  |
| **Enter** | Alternate between the Floating Pawn and a pre-existing Level Pawn. |
| **Tab** | When controlling a Level Pawn, switch to the next controllable Pawn. |
| **Shift + Tab** | When controlling a Level Pawn, switch to the previous controllable Pawn. |
| **1 - 6** | Direct shortcut to control a specific Level Pawn. If there are more than 6, use the **Tab** key. |
| Time of Day controls |  |
| **End** | Decrease the current Time of Day. |
| **Page Down** | Increase the current Time of Day. |
| **Insert** | Smoothly transition the Time of Day to a Dawn value. |
| **Home** | Smoothly transition the Time of Day to a Noon value. |
| **Page Up** | Smoothly transition the Time of Day to a Dusk value. |
| Widget controls |  |
| **P** | Show / Hide the Profiling Widget. |
| **G** | Show / Hide the Geospatial Widget. |

### Geospatial Widget

[![Geospatial Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e68aed4c-f682-4dc4-8042-43300b280bab/geospatial-widget.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e68aed4c-f682-4dc4-8042-43300b280bab/geospatial-widget.png)

Click image for full size.

The **Geospatial Widget** is a status bar displaying your current location on Earth in different coordinate systems:

* Projected CRS.
* Geographic CRS (Lat/Long).
* Geocentric (ECEF).

To learn more, refer to the [Georeferencing a Level](/documentation/en-us/unreal-engine/georeferencing-a-level-in-unreal-engine) page.

### Profiling Widget

[![Profiling Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e22708a-fd1c-45ec-a52d-ce4cbeedc83b/profiling-widget.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e22708a-fd1c-45ec-a52d-ce4cbeedc83b/profiling-widget.png)

Click image for full size.

The **Profiling Widget** is a debug utility to profile the performance of your application.

The left button stack will show or hide different performance counters, which you can also access by their associated `stat counterName` console command. The widget displays the most common and useful ones:

* FPS
* Unit
* Engine
* SceneRendering
* Game
* GPU

Since profiling is heavily linked to the number of frames per second (FPS), the second column of buttons is where you can enable or disable vertical sync (VSync) or cap FPS to 30 or 60 FPS if desired.

## The Simulation Floating Pawn (BP\_SimfloatingPawn)

The Simulation Floating Pawn is an improved version of the Unreal Engine default Pawn, with the added capability to control the maximum navigation speed using the **mouse wheel**. This helps when dealing with large environments.

**Clicking** the mouse wheel will reset to the default speed.

* [templates](https://dev.epicgames.com/community/search?query=templates)
* [simulation](https://dev.epicgames.com/community/search?query=simulation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [The Simulation Player Controller (BP\_SimPlayerController)](/documentation/en-us/unreal-engine/simulation-blank-template-in-unreal-engine?application_version=5.7#thesimulationplayercontroller(bp-simplayercontroller))
* [Geospatial Widget](/documentation/en-us/unreal-engine/simulation-blank-template-in-unreal-engine?application_version=5.7#geospatialwidget)
* [Profiling Widget](/documentation/en-us/unreal-engine/simulation-blank-template-in-unreal-engine?application_version=5.7#profilingwidget)
* [The Simulation Floating Pawn (BP\_SimfloatingPawn)](/documentation/en-us/unreal-engine/simulation-blank-template-in-unreal-engine?application_version=5.7#thesimulationfloatingpawn(bp-simfloatingpawn))

Related documents

[Playing and Simulating

![Playing and Simulating](https://dev.epicgames.com/community/api/documentation/image/c789be9b-7c2a-40ef-ae47-9ea6b248ca9b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine)
