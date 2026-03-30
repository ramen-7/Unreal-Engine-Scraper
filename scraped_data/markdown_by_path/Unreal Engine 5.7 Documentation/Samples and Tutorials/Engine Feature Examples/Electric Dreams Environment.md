<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7 -->

# Electric Dreams Environment

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
7. Electric Dreams Environment

# Electric Dreams Environment

Explore the Electric Dreams Environment featuring the Procedural Content Generation framework, Substrate, and the latest physics developments.

![Electric Dreams Environment](https://dev.epicgames.com/community/api/documentation/image/8fc2016b-4e4c-4ea9-a2f0-f19aeaf6fa9d?resizing_type=fill&width=1920&height=335)

 On this page

In the **Electric Dreams Environment** sample project, you can explore the environment demonstrated during the State of Unreal keynote at the 2023 Game Developers Conference. This demo offered a first look at several new, experimental features available in Unreal Engine 5.2, including:

* [Procedural Content Generation framework](building-virtual-worlds\procedural-generation) (PCG)
* [Substrate material authoring system](https://dev.epicgames.com/community/learning/courses/92D/unreal-engine-substrate-materials)
* Unreal Engine's latest physics developments

[![Electric Dreams Environment](https://dev.epicgames.com/community/api/documentation/image/4f49c67d-beb7-4735-b303-18f79b103ee5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f49c67d-beb7-4735-b303-18f79b103ee5?resizing_type=fit)

This demo also showcases several existing Unreal Engine 5 features, such as:

* [Lumen](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine)
* [Nanite](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5)
* [Soundscape](https://dev.epicgames.com/documentation/en-us/unreal-engine/soundscape-in-unreal-engine)

This environment sample is a learning resource to help you understand how the Electric Dreams world was built by incorporating both traditional and procedural workflows directly within Unreal Engine using the Procedural Content Generation framework. You can also explore other Unreal Engine features such as Substrate through the Opal Material example, Audio, Fluid Simulation Content, and more.

## Setup

To install the Electric Dreams Environment sample project, follow these steps:

1. Access the [Electric Dreams Environment sample](https://fab.com/s/7ee8c5704aaa) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Recommended System Specs

The Electric Dreams Environment sample is a graphically intensive project that requires a powerful video card to run at a stable framerate. We recommend that you install this project on a solid-state drive (SSD). [Nanite](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5) and [Virtual Textures](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-texturing-in-unreal-engine) depend on fast read speeds for the best possible performance.

The recommended hardware specifications are as follows:

| Recommended System Specs | Minimum System Specs |
| --- | --- |
| * 12-core CPU at 3.4 GHz * 64 GB of system RAM * GeForce RTX 3080 (equivalent or higher) * At least 10 GB VRAM | * 8-core CPU at 3.6 GHz * 32 GB of system RAM * GeForce RTX 2080 (equivalent or higher) * At least 8 GB VRAM |

The Electric Dreams Environment sample requires DirectX 12 support and up-to-date graphics drivers.

On lower spec systems, you can adjust the resolution and the viewport screen percentage setting to get better performance. On the minimum spec, we recommend a resolution of 1080p with 50% screen percentage for the larger environments. You can set this in the **Viewport Options Menu** located in the upper-left corner of your editor viewport using the **Screen Percentage** slider.

[![Change screen percentage in viewport options menu.](https://dev.epicgames.com/community/api/documentation/image/79b732c4-2325-4cb3-a35e-d84ea18291b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79b732c4-2325-4cb3-a35e-d84ea18291b6?resizing_type=fit)

Alternatively, you can use the console command `r.ScreenPercentage` to set this value at runtime. For example, `r.ScreenPercentage 50` sets the screen percentage to 50%.

## Navigating the Sample

When you open the Electric Dreams Environment sample, you are placed in the Startup level. The Startup level provides on-screen information for how to use this sample project as well as the sample's recommended system requirements.

The Electric Dreams Environment sample includes several levels. To open one of these levels, find the **Content Browser** and navigate to **Content > Levels**.

### Levels

The levels available in the Electric Dreams Environment sample are listed below in the following table:

| Level Name | Description |
| --- | --- |
| **ElectricDreams\_Env** | This level is the full Electric Dreams environment. This level includes both hand-crafted and procedural areas created with the PCG Framework. It also includes:   * Soundscape procedural ambient sounds * Fluid simulation puddle * Substrate shader ball * Demo Sequences   **Resource Needs**: This level is a resource intensive, 4 kilometer by 4 kilometer World Partition level with steaming disabled.  **Content File Path**: `/Game/Levels/ElectricDreams_Env` |
| **ElectricDreams\_PCG** | This level is a procedural-only version of the Electric Dreams environment.  **Resource Needs**: This level is a resource intensive, 4 kilometer by 4 kilometer World Partition level with streaming disabled.  **Content File Path**: `/Game/Levels/PCG/ElectricDreams_PCG` |
| **ElectricDreams\_PCGCloseRange** | This level is a smaller extract from the ElectricDreams\_PCG level. This level only contains the procedural river bed and creek area, as well as the large cliff structure.  **Resource Needs**: This level is resource friendly.  **Content File Path**: `/Game/Levels/PCG/ElectricDreams_PCGCloseRange` |
| **ElectricDreams\_PCGLargeAssembly** | This breakdown level contains the large cliff structure dropped into the world during the GDC demo with all Assemblies used to build it.  **Content File Path**: `/Game/Levels/PCG/Breakdown_Levels/ElectricDreams_PCGLargeAssembly` |
| **ElectricDreams\_PCGDitchAssembly** | This breakdown level contains the ditch embankment wall rule applied to an open spline with all Assemblies used to build it.  **Content File Path**: `/Game/Levels/PCG/Breakdown_Levels/ElectricDreams_PCGDitchAssembly` |
| **ElectricDreams\_PCGForest** | This breakdown level contains the parametrized PCG forest over a small landscape patch.  **Content File Path**: `/Game/Levels/PCG/Breakdown_Levels/ElectricDreams_PCGForest` |
| **ElectricDreams\_PCGSplineExample** | This example shows how to leverage a single Assembly onto a procedurally generated path by augmenting the original Assembly through PCG Graph logic.  **Content File Path**: `/Game/Levels/PCG/Breakdown_Levels/ElectricDreams_PCGSplineExample` |

You can interact with all of the PCG tools present in every level listed above in the following ways:

* Live in the **Unreal Editor**.
* During **Play-in-Editor** (PIE).
* Individually through the **Content Browser** in **Content > PCG > Graphs**.

Additional Text description actors are scattered throughout the main areas within the world as quick reference guides for things to look for.

[![Text description actor in the world.](https://dev.epicgames.com/community/api/documentation/image/46a4a04d-a7e1-4722-86e1-a36d9a15e21c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46a4a04d-a7e1-4722-86e1-a36d9a15e21c?resizing_type=fit)

## Electric Dreams In-Game Controls

### Drone Controls

Drone controls are available in PIE and cooked builds for every level within this sample. The following table provides an overview of the drone controls:

| Drone Action | Controller | Keyboard and Mouse |
| --- | --- | --- |
| **Move Forward** | Left Joystick | W |
| **Move Backward** | Left Joystick | S |
| **Move Left** | Left Joystick | A |
| **Move Right** | Left Joystick | D |
| **Look** | Right Joystick | Mouse Move |
| **Altitude Up (Ascend)** | Right Trigger | E |
| **Altitude Down (Descend)** | Left Trigger | Q |
| **Speed Up** | Right Bumper | F |
| **Slow Down** | Left Bumper | R |

### Sequence Shortcuts

The Electric Dreams GDC demo sequences are available when exploring the ElectricDreams\_Env level. These sequences can be triggered using the following keyboard shortcuts:

| Sequence Action | Keyboard |
| --- | --- |
| **Fly-Through** | Shift + C |
| **PCG Mid Range** | Shift + V |
| **PCG Long Range** | Shift + B |
| **Stop Playing Sequence** | Spacebar |

## Procedural Content Generation in Electric Dreams

Learn more about how the Electric Dreams Environment sample project incorporates traditional and procedural workflows together in Unreal Engine.

* [![Procedural Content Generation in Electric Dreams](https://dev.epicgames.com/community/api/documentation/image/209375c1-33e1-4d04-8f56-5fc87587a787?resizing_type=fit&width=640&height=640)

  Procedural Content Generation in Electric Dreams

  Learn how Electric Dreams incorporates traditional and procedural workflows in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-in-electric-dreams)

* [lumen](https://dev.epicgames.com/community/search?query=lumen)
* [soundscape](https://dev.epicgames.com/community/search?query=soundscape)
* [procedural content generation](https://dev.epicgames.com/community/search?query=procedural%20content%20generation)
* [pcg](https://dev.epicgames.com/community/search?query=pcg)
* [substrate](https://dev.epicgames.com/community/search?query=substrate)
* [electric dreams](https://dev.epicgames.com/community/search?query=electric%20dreams)
* [nanite](https://dev.epicgames.com/community/search?query=nanite)
* [fab](https://dev.epicgames.com/community/search?query=fab)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#setup)
* [Recommended System Specs](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#recommended-system-specs)
* [Navigating the Sample](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#navigating-the-sample)
* [Levels](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#levels)
* [Electric Dreams In-Game Controls](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#electric-dreams-in-game-controls)
* [Drone Controls](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#drone-controls)
* [Sequence Shortcuts](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#sequence-shortcuts)
* [Procedural Content Generation in Electric Dreams](/documentation/en-us/unreal-engine/electric-dreams-environment-in-unreal-engine?application_version=5.7#procedural-content-generation-in-electric-dreams)
