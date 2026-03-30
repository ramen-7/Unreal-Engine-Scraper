<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7 -->

# DMX Previs

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
7. DMX Previs

# DMX Previs

How to set up the DMX Previs sample, view the light show previs, and explore the DMX-controlled fixtures and effects.

![DMX Previs](https://dev.epicgames.com/community/api/documentation/image/27dee8af-581e-40e3-a8fc-c24887d2feb5?resizing_type=fill&width=1920&height=335)

 On this page

The DMX Previs sample is a fully-animated digital light show using the [DMX](https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-overview) plugin in Unreal Engine. This sample was created in collaboration with [Moment Factory](https://momentfactory.com/home) to show an example of live event previsualization that is as close as possible to the real-life technical counterpart. To leverage Unreal Engine's rendering capabilities and to showcase the newly developed proxy fixture system, the sample features a complex lighting rig that fills the entire open space.

This video shows repeated, flashing lights at certain points that may cause discomfort or potentially trigger seizures for people with photosensitive epilepsy. Viewer discretion is advised.

Moment Factory’s DMX Sample Project For Live Event Previs | Unreal Engine

Exploring and modifying this sample will help you learn how you can:

* Use the DMX plugin Sequencer integration to record and play back an entire live event show programmed on an external lighting desk.
* Use the extensible fixture system to create your own DMX-enabled virtual twins to real hardware devices.
* Customize and tweak your fixture's rendering functions for both real-time previs and high-quality media export.

This project is both CPU-intensive for DMX Track playback in Sequencer and GPU-intensive for high-quality volumetric beam rendering. See the Fixtures and Hardware section for details on the hardware specifications used for this project.

## Getting Started

To create a project with the DMX Previs sample, follow these steps:

1. Access the [DMX Previs sample](https://fab.com/s/14fbd7034e1b) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

1. Press **Play** to view the previs sequence.

   [![Play the previs sequence](https://dev.epicgames.com/community/api/documentation/image/9fd9a10a-33bb-4ebd-8599-eb56e1dfb47c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9fd9a10a-33bb-4ebd-8599-eb56e1dfb47c?resizing_type=fit)

To view the show with optimal performance, build the project with the **Shipping** configuration.

Follow these steps to set the project's build configuration to **Shipping**:

1. In the Editor's main menu, choose **File > Package Project > Build Configuration**, and select **Shipping**.
2. Choose **File > Package Project > Windows** to package the project with the **Shipping** configuration.

[![Shipping build configuration option in the Unreal Editor menu](https://dev.epicgames.com/community/api/documentation/image/d1f6592b-b3b6-44b2-b204-eef764f4c42b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1f6592b-b3b6-44b2-b204-eef764f4c42b?resizing_type=fit)

## Viewing the Show from Multiple Perspectives

After opening the project and pressing **Play in the Editor**, the sequence begins with the cinematic camera view.

To view the show from other perspectives in the virtual auditorium, you can switch camera views with the playback controls defined in the project's [Level Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine) or disable the cinematic camera in **Sequencer**. Both methods are described below.

[![Viewing the show](https://dev.epicgames.com/community/api/documentation/image/082c966d-0b62-45df-afee-9bc2d4e12fd6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/082c966d-0b62-45df-afee-9bc2d4e12fd6?resizing_type=fit)

Image courtesy of Moment Factory.

### Show Playback Controls

Once the Unreal session has started, you can use the following playback controls:

| Key | Description |
| --- | --- |
| **F9** | Show the FPS counter, in both Standalone and Shipping builds. |
| **Space Bar** | Pause or resume the sequence and the DMX playback. |
| **T** | Toggle between cinematics and freecam. In freecam mode, you can move the camera to get a closer look at the light fixtures and view the show from other angles. |
| **V** | Cycle between predefined cinecamera views. |
| **R** | Restart the sequence and DMX playback. |
| **Escape** | Exit the session. |

### Disable Cinematic Camera

You can cycle through freecam and cinematics using the **T** toggle key. Press **V** to cycle between predefined camera locations. Follow the steps below to completely turn off the cinematic camera during the show.

1. In the **Content Browser**, open **DMXPrevis\_Animations** in **Content > Sequences**.

   [![DMX previs animations in the content browser](https://dev.epicgames.com/community/api/documentation/image/7f3e6417-15d9-4fbc-83aa-6873b7c73da8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7f3e6417-15d9-4fbc-83aa-6873b7c73da8?resizing_type=fit)
2. In the **Sequencer** window, right-click on the **Camera Cuts** track and select **Mute** from the options.

   [![Sequencer window camera cuts track mute option](https://dev.epicgames.com/community/api/documentation/image/579a6c9a-5720-4b05-b62f-c1badaef472e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/579a6c9a-5720-4b05-b62f-c1badaef472e?resizing_type=fit)
3. Press **Play**. You will be able to move the camera freely and view the show from different angles.

## Modifying the Show in Real-Time

During DMX track playback in Sequencer, it's useful to be able to modify the show as you are viewing it. This section describes how to change the look and feel of some of the light fixtures.

The project contains more assets than the ones described in this section. Explore all the light fixtures in the project; each type has its own Blueprint and functionality.

### Changing Spotlight Distance

Follow these steps to modify the light distance value of some of the lights. Decreasing this value can help to improve performance during playback; increasing the value creates more volumetric beam effects.

1. In the **World Outliner**, type **Spot** in the search bar and select all the filtered assets.

   [![Filtering assets by the word spot](https://dev.epicgames.com/community/api/documentation/image/775225c6-d954-4858-812d-3bfee8c030ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/775225c6-d954-4858-812d-3bfee8c030ba?resizing_type=fit)
2. In the **Details** panel, change the **Light Distance Max** property value from **5000.0** to a smaller value for better performance or a higher value for increased volumetric effect.

   ![Light distance max 5000](https://dev.epicgames.com/community/api/documentation/image/141b4892-843d-4663-a527-c9b18f385157?resizing_type=fit&width=1920&height=1080)

   ![Light distance max 1000](https://dev.epicgames.com/community/api/documentation/image/3d50fe28-45e3-41cd-9a2b-3a8b3ecd1fca?resizing_type=fit&width=1920&height=1080)

   Light distance max 5000

   Light distance max 1000

### Adjusting Beam Quality

All the fixtures used are specifically customised for the project and have adaptive quality logic for balancing speed and quality in real-time. The logic for adaptive quality is defined in the **M\_Beam\_Inhibitive\_Master** Material, located in **Content > DMX > FixtureMaterials**.

[![fixture materials in the content browser](https://dev.epicgames.com/community/api/documentation/image/adae7059-f4ae-4de7-9d9c-9c3283aa832e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/adae7059-f4ae-4de7-9d9c-9c3283aa832e?resizing_type=fit)

This Material dynamically adjusts the volumetric beam shader sample counts as a function of the live DMX Zoom angle.

* The wider the beam is, the lower the sample count to retain high performance with minimal visual impact.
* The narrower the beam is, the higher the sample count for increased beam sharpness.

You can adjust the quality settings in the **Material Editor** for the **M\_Beam\_inhibitive\_Master** Material. The settings are located in the **Parameter Defaults** panel.

[![Material parameter defaults panel](https://dev.epicgames.com/community/api/documentation/image/49b9f21e-6c34-4931-b147-518585535257?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49b9f21e-6c34-4931-b147-518585535257?resizing_type=fit)

* **Low Quality Level:** Defines the lowest possible multiple for the predefined sample count.
* **Max Quality Level:** Defines the highest possible multiple for the predefined sample count.
* **Use MRQ Override:** Forces a specific multiplier for all fixture material and material instances regardless of the low and max values set. This property is useful to set when exporting high quality videos or image sequences of the project.
* **Zoom Based Intensity:** When enabled, the light function can lower in intensity when the zoom is wider but be closer to the intended brightness when the zoom is narrower. This mimics the behaviour of real lights where the brightness on any given surface is lower when the beam is wider.

![Low Quality Level 0.3 Max Quality Level 1.0](https://dev.epicgames.com/community/api/documentation/image/712b4124-a167-4f23-9136-23b960735be0?resizing_type=fit&width=1920&height=1080)

![Low Quality Level 0.3 Max Quality Level 5.0](https://dev.epicgames.com/community/api/documentation/image/c0d537dc-febd-4169-9d4e-c26705fca25f?resizing_type=fit&width=1920&height=1080)

Low Quality Level 0.3 Max Quality Level 1.0

Low Quality Level 0.3 Max Quality Level 5.0

*In the left image, the Max Quality Level is set to 1 creating
grainier beams. In the right image, the Max Quality Level is set to 5 so
the beams appear sharper.*

**Quality Levels** set to values greater than **1** are meant for offline renderings using [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue). For this project, the **Quality Level** was typically set to **2** for both **Low and Max Quality Levels** to generate footage.

### Changing Catwalk Cell Count

Follow these steps to change the cell count for the DMX Fixture Matrix used in the Catwalk.

1. In the project's **Content Browser**, double-click the **DMXLib\_v4** asset to open the **DMX Library Editor**.

   [![DMX library asset in the content browser](https://dev.epicgames.com/community/api/documentation/image/53e4da1d-c2d9-41f4-868e-2e79957baf43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/53e4da1d-c2d9-41f4-868e-2e79957baf43?resizing_type=fit)
2. In the **Fixture Types** tab, select **CatwalkStrip** under **Matrix/Pixel Bar**. This example is going to modify its **Mode Properties**.

   [![catwalk strip mode properties](https://dev.epicgames.com/community/api/documentation/image/caae8e17-4531-4862-a16f-076781f675a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/caae8e17-4531-4862-a16f-076781f675a1?resizing_type=fit)
3. In the **Mode Properties** panel, change the **Y Cells** property value from **5** to **20**.

   [![changing the value of the y cells property](https://dev.epicgames.com/community/api/documentation/image/9a92c733-d90a-4634-a509-5033d325282e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a92c733-d90a-4634-a509-5033d325282e?resizing_type=fit)
4. In the **World Outliner**, select all the **CatwalkStrips** assets.
5. In the **Details** panel under the **DMX Matrix Fixture** section, click **Generate Preview Mesh** to update the mesh in the viewport with the changes you made in the DMX Library.

   [![Details panel DMX Matrix Fixture section Generate preview mesh button](https://dev.epicgames.com/community/api/documentation/image/9b8cbd87-f81c-4e0b-ab52-b0cc19c44de2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b8cbd87-f81c-4e0b-ab52-b0cc19c44de2?resizing_type=fit)
6. In the viewport, all the **CatwalkStrips** now have more cells.

   ![catwalk 5 Y cells](https://dev.epicgames.com/community/api/documentation/image/1386b4e8-f0ad-4578-9020-8aaa03578a93?resizing_type=fit&width=1920&height=1080)

   ![catwalk 20 Y cells](https://dev.epicgames.com/community/api/documentation/image/16d7f1ff-fdf7-463e-b3ec-5c4b59581035?resizing_type=fit&width=1920&height=1080)

   catwalk 5 Y cells

   catwalk 20 Y cells

## Exporting Media with Movie Render Queue

In a typical live event previs workflow, designers and artists will work at lower quality levels for quicker iterations. For review purposes, it's useful to render high-quality image sequences or Apple ProRes files.

This sample includes two presets for [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) to generate high-resolution media. The presets are located in **Content > Cinematics > MoviePipeline > Presets**. The two presets have different resolutions:

* **UHD**: Preset for Ultra High Definition (3840x2160) export to Apple ProRes 422 HQ.
* **FHD**: Preset for Full High Definition (1920x1080) export to Apple ProRes 422 HQ.

[![movie render queue presets](https://dev.epicgames.com/community/api/documentation/image/80dce019-b795-41d4-a422-1a2387aff3c9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80dce019-b795-41d4-a422-1a2387aff3c9?resizing_type=fit)

Follow these steps to export high quality media using Movie Render Queue.

1. In the project's **World Outliner**, select all the spotlights and set their **Light Distance Max** property to **12,000**.

   [![spotlight light distance max 12000](https://dev.epicgames.com/community/api/documentation/image/8df1d9fe-a711-445e-993b-c6bb7800bd57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8df1d9fe-a711-445e-993b-c6bb7800bd57?resizing_type=fit)
2. In the project's **Content Browser**, navigate to **DMX > FixtureMaterials**.
3. Open the **M\_Beam\_Inhibitive\_Master** Material in the Material Editor.
4. In the **Parameter Defaults** panel of the **Material Editor**:

   1. Set **Low Quality Level** to **2.0**.
   2. Set **Max Quality Level** to **2.0**.

   [![quality levels set to 2](https://dev.epicgames.com/community/api/documentation/image/f6f5fe16-2186-4be0-86c8-1cdb375bb764?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f6f5fe16-2186-4be0-86c8-1cdb375bb764?resizing_type=fit)
5. Close the Material Editor.
6. In the main Editor, choose **Window > Cinematics > Movie Render Queue** to open the **Movie Render Queue** window.

   [![open the movie render queue window](https://dev.epicgames.com/community/api/documentation/image/6d774ab0-09a0-4de5-90fe-a8038769c66c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d774ab0-09a0-4de5-90fe-a8038769c66c?resizing_type=fit)
7. Press the **Add Render** button and select the **DMXPrevis\_Animations** Level Sequence.

   [![select the DMX previs animations level sequence](https://dev.epicgames.com/community/api/documentation/image/55ae065a-3400-4b38-b741-8286e805ef01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55ae065a-3400-4b38-b741-8286e805ef01?resizing_type=fit)
8. Under the **Settings** column, click the dropdown arrow and select the desired preset, UHD or FHD.

   [![select the preset in the settings column](https://dev.epicgames.com/community/api/documentation/image/756a9555-1e29-44eb-8d7f-34c889c5be48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/756a9555-1e29-44eb-8d7f-34c889c5be48?resizing_type=fit)
9. Click **Render (Local)** to export the rendered frames locally.

   [![Click render local](https://dev.epicgames.com/community/api/documentation/image/8917dba6-215e-49a6-85e4-95edf4776e51?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8917dba6-215e-49a6-85e4-95edf4776e51?resizing_type=fit)

You can set the **MRQ Override** parameter in **M\_B\_Inhibitive\_Master** to **1.0** in order to override the **Low** and **Max Quality Levels**.

## Live Event Previs Project File Structure

This sample project includes a variety of assets to recreate an auditorium and full light show with DMX. To help you explore everything in the project, see the descriptions of all the folders below.

### Content Browser

[![DMX subfolders in the content browser hierarchy](https://dev.epicgames.com/community/api/documentation/image/5b2ed4a8-1106-4423-9f13-d6c3b4cd2e91?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b2ed4a8-1106-4423-9f13-d6c3b4cd2e91?resizing_type=fit)

The **Content** folder contains the following sub-folders:

* **Assets:** General project and level assets for the stage and auditorium.
* **Audio:** The show soundtrack.
* **Blueprints:** [GameMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine) override using Spectator Pawn.
* **Cinematics:** [Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine#movie-render-queue) settings for Ultra High Definition (UHD) and Full High Definition (FHD) offline renders.
* **DMX:** All DMX-related content.

  + **Disks:** Project-specific DMX fixture gobos, which control the shape and pattern of a light. A given light can have multiple gobos throughout the show and can be animated.
  + **EffectTables:** Defines the effects for the DMX-enabled light types used in the project.
  + **FixtureMaterials:** Project-specific and optimized DMX Fixture materials. This is an extension of what was shipped with the DMX plugin.
  + **FixturesBP:** Project-specific Lighting Fixture blueprints. This is an extension of what was shipped with the DMX plugin.
  + **GoboWheel:** Same as the contents of the **Disks** folder but as separate textures.
  + **Plugins:** Useful DMX tools and widgets.
  + **SpecialFXBP:** Project-specific pyro, laser, and fireworks fixture assets. It also contains the DMX-controlled sphere that is in the middle of the stage.
  + **DMXLib\_v4:** The project core [DMX library](https://dev.epicgames.com/documentation/en-us/unreal-engine/create-a-dmx-library-and-add-fixture-patches-in-unreal-engine), which contains all the Fixture definitions, Universes, and patching.
* **Effects:**

  + **Bloom:** Project-specific, high-quality, convoluted bloom **Texture** without streaks.
  + **Fireworks:** Project-specific fireworks **Blueprints** and [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) particle system.
  + **Flash:** Audience cell phone lights and **Niagara** particle system.
  + **RockLevitation:** Levitating rock **Niagara** particle system.
  + **WaterMaterials:** High-quality water materials for the project.
* **Maps:** Different parts of the level are contained in their own separate maps:

  + **Main**: The persistent level that contains the sequencer track, post-process volume, and soundtrack.
  + **DMXControlled**: This level contains all DMX-controlled elements, lighting fixtures, and effects.
  + **Terrain:** This level contains the terrain and rock formation.
  + **Venue:** This level contains the venue and structural-related actors, such as the arena, audience, and trusses.
* **MegaScans: Quixel MegaScan** assets used for terrain and environment.
* **Movies:** Contains [Media Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-in-unreal-engine) assets for movie playback.

  + **Clock\_LED**: Contains the image sequence for animating the Clock LED that surrounds the catwalk.
  + **Drapes**: Contains the image sequence for the drapes' video projection.
* **MSPresets**: MegaScan preset assets.
* **Sequences**: Contains the [Level Sequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview).
* **Showfile**: The showfile (`.zip`) from the [grandMA2](https://www.malighting.com/downloads/products/grandma2/) lighting console. You can uncompress the file and use it on your console.
* **Splash**: The project's splash image when it loads in the Unreal Editor.
* **Tropical\_Jungle\_Pack**: The asset pack used for the environment.

### World Outliner

Explore all the assets in the **World Outliner**, especially the following items and folders:

* **Cams:** The list of cameras used by Sequencer cinematics and predefined camera locations.
* **DMX\_FX** and **DMX\_LX**: DMX-controlled fixtures and effects.
* **DMXPrevis\_Animations:** The Level Sequence that drives the show, soundtrack, and DMX track.

## Fixtures and Hardware

This sample was designed to use the following fixtures and hardware.

### Fixtures

| Fixture Name | Fixture Type | Quantity |
| --- | --- | --- |
| Lighting Fixtures |  |  |
| **Audience Strip - No pixels** | Custom LED | 50 |
| **Audience Wash LED Par** | Elation SixPar 300 | 12 |
| **Catwalk Strip - 5 pixels** | Custom LED | 20 |
| **Matrix Strip - 5 pixels** | Custom LED | 32 |
| **Scenic Wash LED Par** | Elation SixPar 300 | 14 |
| **SpotMH1** | Elation Proteus Maximus | 64 |
| **SpotMH2** | Robe Megapointe | 94 |
| **Strobe RGB** | Elation Protron 3K LED Strobe | 122 |
| **Stage Strip - 5 pixels** | Custom LED | 24 |
| **Sun Strip - 5 pixels** | Custom LED | 90 |
| **Truss Toner** | Elation SixPar 300 | 220 |
| **WashMH1** | Ireos Space Canon | 8 |
| **WashMH2** | GLP X4 | 16 |
| **Vomitory LED Par** | Elation SixPar 300 | 2 |
| **Total Lighting Fixture Count** |  | 768 |
| SFX Fixtures |  |  |
| --- | --- | --- |
| **Fireworks** | N/A | 8 |
| **Laser RGB** | N/A | 6 |
| **Pyrotechnic Launcher** | N/A | 33 |
| **Total SFX Fixture Count** |  | 47 |

### Lighting Console

| Hardware | Quantity |
| --- | --- |
| **grandMA2 light** | 1 |
| **MA Lighting NPU** | 1 |

### DMX

| Specs | Description |
| --- | --- |
| **Channels** | 7368 |
| **DMX Universes** | 15 |
| **Protocol** | Art-Net |
| **Unique Cues** | 144 |
| **Timecode Sync** | MIDI |

## Plugins

The following plugins provide the core functionality shown in this sample:

* DMX Engine
* DMX Fixtures
* DMX Pixel Mapping
* DMX Protocol
* Level Sequence Editor
* Movie Render Queue

* [dmx](https://dev.epicgames.com/community/search?query=dmx)
* [live event](https://dev.epicgames.com/community/search?query=live%20event)
* [previs](https://dev.epicgames.com/community/search?query=previs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#getting-started)
* [Viewing the Show from Multiple Perspectives](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#viewing-the-show-from-multiple-perspectives)
* [Show Playback Controls](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#show-playback-controls)
* [Disable Cinematic Camera](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#disable-cinematic-camera)
* [Modifying the Show in Real-Time](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#modifying-the-show-in-real-time)
* [Changing Spotlight Distance](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#changing-spotlight-distance)
* [Adjusting Beam Quality](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#adjusting-beam-quality)
* [Changing Catwalk Cell Count](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#changing-catwalk-cell-count)
* [Exporting Media with Movie Render Queue](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#exporting-media-with-movie-render-queue)
* [Live Event Previs Project File Structure](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#live-event-previs-project-file-structure)
* [Content Browser](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#content-browser)
* [World Outliner](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#world-outliner)
* [Fixtures and Hardware](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#fixtures-and-hardware)
* [Fixtures](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#fixtures)
* [Lighting Console](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#lighting-console)
* [DMX](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#dmx)
* [Plugins](/documentation/en-us/unreal-engine/dmx-previs-sample-project-for-unreal-engine?application_version=5.7#plugins)
