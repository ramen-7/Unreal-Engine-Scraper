<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7 -->

# Getting Started with Chaos Visual Debugger

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Chaos Visual Debugger](/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine "Chaos Visual Debugger")
8. Getting Started with Chaos Visual Debugger

# Getting Started with Chaos Visual Debugger

Navigate Chaos Visual Debugger’s user interface.

![Getting Started with Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/74ded45c-9f64-4ecc-a662-8e8beef1d420?resizing_type=fill&width=1920&height=335)

 On this page

**[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) is a tool that you can use to record physics simulations. With CVD, you can record games and applications running on your machine, as well as from a remote machine, or a platform that’s connected to your machine.

[![](https://dev.epicgames.com/community/api/documentation/image/af6324d6-5713-470d-bd20-c64224b35cd6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af6324d6-5713-470d-bd20-c64224b35cd6?resizing_type=fit)

By playing back recordings in CVD, you can inspect data for debugging. These recordings are project independent, meaning they can be loaded even without access to Unreal Engine (UE) project files, enabling cross-team collaboration or remote debugging.

The data that CVD records includes:

* **Particles** (including velocities, accelerations, mass properties, and object states)
* **Collision geometry** (including collision channels)
* **Collision constraints** (contact pairs with their state)
* **Joint constraints** (state and joint settings)
* **Character ground constraints** (physics-based character movement)
* **Scene queries** (including line traces, sweeps, and overlaps)
* **Rigid body animation nodes** (RBAN)

In the context of CVD, **particles** usually refer to rigid bodies.

## Launch Chaos Visual Debugger

There are two ways to launch CVD; [from the Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#inside-the-unreal-editor) or [as a standalone program](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#as-a-standalone-program).

### Inside the Unreal Editor

To open the Chaos Visual Debugger from the Unreal Editor, in the menu bar, click **Tools > Debug > Chaos Visual Debugger**. After selecting CVD, the tool will open in a new window.

[![Launch From The Editor](https://dev.epicgames.com/community/api/documentation/image/81ea3fed-2bd6-4f3b-b294-b1e7e10d4d52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81ea3fed-2bd6-4f3b-b294-b1e7e10d4d52?resizing_type=fit)

### As a Standalone Program

To run CVD as a standalone program, you must use a source-code build of Unreal Engine. You can download a source-code build from [GitHub](https://www.unrealengine.com/en-US/ue-on-github). To learn more, see [Building Unreal Engine from Source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).

You can build and run the CVD as a standalone program from either an executable (not portable) or batch file (portable). The table below describes the file location and build steps for each option.

| Build Flow | Description |
| --- | --- |
| **CVD Executable** | The executable is located in the following file path: `Engine\Binaries\Win64\ChaosVisualDebugger.exe`  To build and run CVD, follow these steps:   1. From your IDE of choice (such as Visual Studio), open the CVD executable. 2. Build and run the executable.   Once built, you can create a shortcut to the executable and run the tool with a single click. |
| **CVD Batch File** | The batch file located at the following path:  `Engine\Programs\ChaosVisualDebugger\BuildAndCook.bat`  To build and run CVD, follow these steps:   1. Build the Editor. 2. Run the batch file to build, cook, and package CVD. 3. Access the output build from `Engine\Programs\ChaosVisualDebugger\PackagedBuild` and run it. |

## Explore the CVD User Interface

This section describes the most common buttons, panels, and toolbars you will interact with in the Chaos Visual Debugger. While some of these elements are similar to the Unreal Editor interface, you should familiarize yourself with CVD due to visual differences between CVD and some Unreal Editor versions.

The sections below describe where to find each user interface (UI) element and offer simple use cases. For a deeper dive, follow the links provided throughout this page.

[![CVD Interface](https://dev.epicgames.com/community/api/documentation/image/1ae159a8-20f8-4710-bcd9-43a2c79f5dda?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ae159a8-20f8-4710-bcd9-43a2c79f5dda?resizing_type=fit)

| Number | Name | Overview |
| --- | --- | --- |
| 1 | **Menu Bar** | Options to load recent recordings and modify the CVD layout. |
| 2 | **Main Toolbar** | Options to start or stop recordings, load recordings, and customize which data to record. |
| 3 | **Viewport Toolbar** | Options to modify which data is displayed in the viewport and how it's visually differentiated. |
| 4 | **Scene Outliner** | Displays a list of scene components within a recording. |
| 5 | **Viewport** | Displays a loaded or live recording, like the Unreal Editor viewport. This can include:   * A level open in the Unreal Editor. * A Play-In-Editor (PIE) session. * Packaged builds running on your machine. * An application running on a platform connected to your machine, such as a console. |
| 6 | **Playback Controls** | Displays a collection of playback timelines and logs including:   * [The Game Frames Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#game-frames-timeline) * [The Solver Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#solver-timeline) * [The Solver Stage Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#solver-stage-timeline) * [The Recorded Output Log](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#recorded-output-log) * [The Output Log](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#output-log) |
| 7 | **Details Panel** | Displays information for a selection made in the viewport that doesn't have a dedicated Data Inspector, such as particles. |
| 8 | **Data Inspectors** | Provides additional details for:   * [Collision data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#collision-data-inspector) * [Scene queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#scene-query-inspector) * [Joint constraint data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#joint-constraint-data-inspector) * [Particle data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#particle-data-details-panel) |

### Menu Bar

| Name | Description | Image |
| --- | --- | --- |
| **File** | Quick access to open recent recordings. | [Menu Bar File](https://dev.epicgames.com/community/api/documentation/image/05640caa-0c0f-499d-9d2f-a49dca24096b?resizing_type=fit) |
| **Window** | Show or hide parts of the CVD UI. | [Menu Bar Window](https://dev.epicgames.com/community/api/documentation/image/eddafbd0-0758-474f-b701-be80d7c5d85d?resizing_type=fit) |

### Main Toolbar

[![Main Toolbar](https://dev.epicgames.com/community/api/documentation/image/4842107f-d4c1-430e-ae6d-ffea856c4aec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4842107f-d4c1-430e-ae6d-ffea856c4aec?resizing_type=fit)

| Number | Name | Description |
| --- | --- | --- |
| 1 | **Open File** | Loads existing `.utrace` recordings. |
| 2 | **Connect to Session** | (Legacy) Connects to a remote machine for remote debugging.  This is now only used when recording a remote session via the command line. See [(Legacy) Record a Live Session with the Command Line Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger#legacy-record-a-live-session-with-the-command-line-interface) for more information. |
| 3 | **Combine** | Combines multiple recordings that are open in CVD into one `.cvdmulti` file. |
| 4 | **Scene Query Browser** | Inspects all scene queries made for a single frame. For more information on this, see [Data Inspectors](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger). |
| 5 | **Session Targets** | Selects the target(s) to record. |
| 6 | **Loading Mode** | Loads single or multiple recordings (which merges data). |
| 7 | **Record to File** | Begins a recording and saves to file. |
| 8 | **Record Live Session** | Begins a recording and renders the visualization in real time. |
| 9 | **Data Channels** | Customizes the data captured during recording, such as:   * [Data flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger) * [Simulation stages](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#solver-stage-timeline) |
| 10 | **Settings** | Customizes CVD’s UI and performance. |

### Viewport Toolbar

[![Viewport Toolbar](https://dev.epicgames.com/community/api/documentation/image/b9f5e930-9f35-4ba2-80de-bd2d347f74fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9f5e930-9f35-4ba2-80de-bd2d347f74fe?resizing_type=fit)

1. [Hamburger Menu](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#hamburger-menu)
2. [View Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#view-mode)
3. [Lighting Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#lighting-mode)
4. [Show Button](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#show-button)
5. [Transform and Snapping Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#transform-and-snapping-toolbar)

#### Hamburger Menu

| Name | Description | Image |
| --- | --- | --- |
| **Play at Recorded Framerate** | Overrides the recorded frame rate to a fixed one. | [Play At Recorded Framerate](https://dev.epicgames.com/community/api/documentation/image/94710bbe-f892-42e7-9236-94d9810c5651?resizing_type=fit) |
| **Object Tracking (F8)** | Locks the camera to an object in the viewport. | [Object Tracking](https://dev.epicgames.com/community/api/documentation/image/332730c6-919c-4aef-8595-aaf769e3920d?resizing_type=fit) |
| **FOV Options** | Adjusts the viewport’s FOV (field of view) and furthest render distance. | [FOV Options](https://dev.epicgames.com/community/api/documentation/image/a37d5186-1379-4a07-a37d-b4d0a87feac4?resizing_type=fit) |
| **Allow Translucent Selection (T)** | Toggles the ability to click through translucent objects. | [Allow Translucent Selection](https://dev.epicgames.com/community/api/documentation/image/63d399ac-9881-4f02-9c35-dd8562b4a137?resizing_type=fit) |
| **Go to Location** | Teleports the camera to a location entered into this field, using an XYZ format. | [Go To Location](https://dev.epicgames.com/community/api/documentation/image/0b7dabf8-f29e-4f7f-bca7-fb1554c36b28?resizing_type=fit) |

#### View Mode

View mode switches between **Perspective**, **Top**, **Bottom**, **Left**, **Right**, **Front**, and **Back** views in the viewport.

| Perspective | Top | Left |
| --- | --- | --- |
| [Perspective](https://dev.epicgames.com/community/api/documentation/image/e20328e0-fdff-4d28-b93e-ea4aaf49369c?resizing_type=fit) | [Top](https://dev.epicgames.com/community/api/documentation/image/2ab85134-6a5f-4ed9-9987-010c751d4e96?resizing_type=fit) | [Left](https://dev.epicgames.com/community/api/documentation/image/c3c47c0b-c1e5-49f4-a089-b100046ab6a4?resizing_type=fit) |

#### Lighting Mode

Lighting mode switches between **Lit**, **Unlit**, **Lit** **Wireframe**, and **Wireframe** view modes in the viewport.

![Lighting Modes](https://dev.epicgames.com/community/api/documentation/image/389d07f6-8083-4dbd-82eb-baa8de412163?resizing_type=fit&width=1920&height=1080)![Lighting Modes](https://dev.epicgames.com/community/api/documentation/image/78bb80f5-b4d7-4a26-99ac-2b6460a2cf00?resizing_type=fit&width=1920&height=1080)![Lighting Modes](https://dev.epicgames.com/community/api/documentation/image/db7d7894-0b97-4a0d-be51-0982078970f6?resizing_type=fit&width=1920&height=1080)![Lighting Modes](https://dev.epicgames.com/community/api/documentation/image/17bf8af8-b661-405c-87b4-927abc9fdb2d?resizing_type=fit&width=1920&height=1080)

**Lighting Modes**

For better visibility when using Unlit mode, enable **Mesh Edges**.

[![Mesh Edges](https://dev.epicgames.com/community/api/documentation/image/209f074f-5a5c-4fda-be6f-8af100778536?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/209f074f-5a5c-4fda-be6f-8af100778536?resizing_type=fit)

#### Show Button

The **Show** button modifies which visualization flags and debug text are visible in the viewport for an existing recording. For more information about data flags, see [Data Visualization Flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger).

[![Show Button](https://dev.epicgames.com/community/api/documentation/image/576635ca-fe9e-4c28-92bc-50d2e2a2351a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/576635ca-fe9e-4c28-92bc-50d2e2a2351a?resizing_type=fit)

Settings in this menu persist between CVD sessions unless reset to default.

#### Transform and Snapping Toolbar

The transform and snapping toolbar is similar to the legacy viewport toolbar in previous versions of the Unreal Editor. Most often, you’ll use these tools to manipulate light actors.

| Icon | Name | Description |
| --- | --- | --- |
| [Icon Select](https://dev.epicgames.com/community/api/documentation/image/1a59c3c9-128c-45d6-ad60-cfb05f89086c?resizing_type=fit) | **Select Objects** | Selects objects within the viewport. |
| [Translate Object](https://dev.epicgames.com/community/api/documentation/image/ea14cd04-6cde-457f-b08a-2208433f7fcf?resizing_type=fit) | **Select and Translate Objects** | Moves light actors around the world along individual axes, dual axes, or on all three axes. |
| [Rotate Object](https://dev.epicgames.com/community/api/documentation/image/6f17c4d9-7eed-49ff-be60-95b29667ca27?resizing_type=fit) | **Select and Rotate Objects** | Rotates light actors along individual axes. |
| [Scale Object](https://dev.epicgames.com/community/api/documentation/image/1c688e3c-43f7-4ddc-9970-bb6562a1484f?resizing_type=fit) | **Select and Scale Objects** | Scales light actors using the scale gizmo. Use the gizmo to scale objects along individual axes, dual axes, or uniformly on all three axes. |
| [Coordinate System](https://dev.epicgames.com/community/api/documentation/image/9b78b1ec-6a8c-4257-88fe-e962b14395e4?resizing_type=fit) | **Coordinate System** | Cycles the coordinate system between **World** and **Local**. |
| [Snap To Surface](https://dev.epicgames.com/community/api/documentation/image/cc7cb5fc-842c-4aa7-af6d-cee17bb74930?resizing_type=fit) | **Snap to Surface** | Sets the snapping behavior of light actors when you drag them along another object’s surface. |
| [Snap To Grid](https://dev.epicgames.com/community/api/documentation/image/27ef1988-e41f-448d-80fd-c3676b21a767?resizing_type=fit) | **Snap to Grid** | Toggles whether light actors snap to the grid and sets the increment. |
| [Rotation Increments](https://dev.epicgames.com/community/api/documentation/image/1d4fda57-1f38-410b-81b8-57b80ea2e894?resizing_type=fit) | **Rotation Increments** | Toggles whether light actors rotate in increments and sets the degree. |
| [Scaling Increments](https://dev.epicgames.com/community/api/documentation/image/0cf8a82e-eb16-43e4-8199-5b4a4daa7f94?resizing_type=fit) | **Scaling Increments** | Toggles whether light actors scale in increments and sets the increment. |
| [Camera Speed](https://dev.epicgames.com/community/api/documentation/image/4f813627-bc75-4a1e-896e-79334fa70a5e?resizing_type=fit) | **Camera Speed** | Affects the speed at which the camera can move around the world. |

### Scene Outliner

The **Scene Outliner** displays a list of scene components within a recording. Since each recording can contain multiple solvers, each solver's particles are put under a folder with the name and ID of the solver they belong to. Within that folder, each particle is labeled with its Chaos-side debug name.

[![Scene Outliner](https://dev.epicgames.com/community/api/documentation/image/60b8a755-553a-4289-bc69-23850e1dd93a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60b8a755-553a-4289-bc69-23850e1dd93a?resizing_type=fit)

In CVD, a **physics solver** is an instance of a physics simulation (usually from a game world), handled by the [Chaos Physics Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine).

### Playback Controls

The Chaos Visual Debugger includes controls to play and rewind existing recordings based on [game-thread](https://dev.epicgames.com/documentation/en-us/unreal-engine/threaded-rendering-in-unreal-engine) frames, physics-solver frames, or stages of a simulation. This maximizes the degree to which you can inspect situations that use [networked physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/networked-physics-overview), asynchronous physics, or multiple game worlds (such as multiplayer games).

#### Game Frames Timeline

The **Game Frames Timeline** represents each game-thread frame for a recording.

[![Game Frames Timeline](https://dev.epicgames.com/community/api/documentation/image/ddee7ff6-5026-4413-85ba-92c8dd140cb5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ddee7ff6-5026-4413-85ba-92c8dd140cb5?resizing_type=fit)

When you playback a recording using this timeline, you’ll notice that the Solver Timeline also plays. This is because for each **game-thread** frame that plays, CVD searches for the closest **physics-solver** frame available at that timestamp.

The frame numbers of the Game Frames Timeline may not always match the Solver Timeline. This is because game-thread frames can correspond to multiple physics-solver frames. Access to both timelines means you can inspect situations where this occurs, such as when using Async Physics.

[![Game Frame and Solver Timelines](https://dev.epicgames.com/community/api/documentation/image/341d2b5d-3e0b-47eb-820a-94b48108ce83?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/341d2b5d-3e0b-47eb-820a-94b48108ce83?resizing_type=fit)

(1) Solver Timeline (2) Game Frames Timeline

For an in-depth explanation of how CVD visualizes Sync and Async Physics, data from multiple game worlds, and resimulated frames, see [Debugging Chaos Physics in Unreal Engine at the 16:05](https://youtu.be/_DKKztvMd2o?t=1007) minute mark.

#### Solver Timeline

The **Solver Timeline** represents each physics-solver frame for a recording. Each solver gets a dedicated track. Using this timeline, you can playback data for any solver track and see which solver frame corresponds to a specific game-thread frame.

[![Solver Timeline](https://dev.epicgames.com/community/api/documentation/image/4b04d15d-e462-4ab1-ae8e-fd49a63d8188?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b04d15d-e462-4ab1-ae8e-fd49a63d8188?resizing_type=fit)

| Setting | Description | Image |
| --- | --- | --- |
| **Timeline Sync Mode** | Controls how each solver track is synced.   * **Recorded Timestamp (Default):** Syncs all solver tracks based on which time they were recorded, regardless of networked physics time offsets. * **Network Tick:** Visualizes each solver track as if the client-side prediction logic works correctly. This can help you pinpoint any divergences that indicate a client and server desync. * **Manual:** Fully disables automatic track syncs. | [Network Tick](https://dev.epicgames.com/community/api/documentation/image/4cb6503a-273b-4e5e-ae39-b3b02549738d?resizing_type=fit) |
| **Re-Simulation Badge** | Appears on any solver track that includes frames that are part of a re-simulation done during the network desync correction process. | [ReSim Badge](https://dev.epicgames.com/community/api/documentation/image/4ac59488-8b0a-427f-9a0c-3b3152129bf9?resizing_type=fit) |
| **Visibility Control** | Shows or hides visualized data from a particular solver track. | [Visibility Control](https://dev.epicgames.com/community/api/documentation/image/e0db75a7-0008-482d-9662-c741347bbd4d?resizing_type=fit) |

#### Solver Stage Timeline

With the **Solver Stage Timeline**, you can jump to a specific **stage** of a physics simulation. **Stages** are snapshots of a simulation taken at different points within a single physics frame.

[![Solver Stage Timeline](https://dev.epicgames.com/community/api/documentation/image/6618e055-0423-4c5f-a064-952fd4690d7b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6618e055-0423-4c5f-a064-952fd4690d7b?resizing_type=fit)

You can visualize the following stages, using a particle simulation as an example:

| Stage | Description |
| --- | --- |
| **Evolution Start** | Takes a snapshot of all particles at the beginning of the solver step. |
| **Post-Integrate** | Takes a snapshot of all particles after performing the `Integrate` calculation on them. |
| **Collision Detection Broad Phase** | Takes a snapshot of all mid phases (an object is created for every particle pair whose bounds overlap) after running the Broad Phase of the collision detection process. |
| **Collision Detection Narrow Phase** | Takes a snapshot of all mid phases after running the Narrow Phase of the collision detection process. |
| **Pre Constraint Solve** | Takes a snapshot of all particles before solving the available constraints. |
| **Post Constraint Solve** | Takes a snapshot of all particles after solving the constraints. |
| **Evolution End** | Takes a snapshot of all particles at the end of the solver step. |

The Solver Stage Timeline is useful for inspecting unusual behavior within singular frames, such as when an object appears in the correct location at the beginning of a frame but in an unexpected location at the end of a frame.

#### Recorded Output Log

Located next to the Solver Timeline Tracks tab, the **Recorded Output Log** tab is where CVD records the log stream of your application for retroactive inspection.

[![Recorded Output Log](https://dev.epicgames.com/community/api/documentation/image/115f02ea-7c13-407d-a2c8-8f59f547a339?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/115f02ea-7c13-407d-a2c8-8f59f547a339?resizing_type=fit)

#### Output Log

The **Output Log** is a real-time log to monitor activity. This tab shows the active log for the current CVD instance and displays errors or warnings for CVD itself.

[![Output Log](https://dev.epicgames.com/community/api/documentation/image/bf1ab71b-21fc-4286-9a9c-9544a9743552?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf1ab71b-21fc-4286-9a9c-9544a9743552?resizing_type=fit)

## Details Panel

The **Details** panel displays information for a selection made in the viewport.

[![Details Panel](https://dev.epicgames.com/community/api/documentation/image/20ccfa17-2c80-45c4-87b7-e2d20b113d34?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20ccfa17-2c80-45c4-87b7-e2d20b113d34?resizing_type=fit)

The Details panel also acts as the Data Inspector for particle data. For more information, see [Particle Data (Details Panel)](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger#particle-data-details-panel).

## Next Up

* [![Data Inspectors](https://dev.epicgames.com/community/api/documentation/image/e41606f4-f2e2-4f65-bf67-295486d1ef4f?resizing_type=fit&width=640&height=640)

  Data Inspectors

  Understand data inspectors in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger)

* [![Data Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/30c4b8fb-085b-461f-9543-fe2b6e998a80?resizing_type=fit&width=640&height=640)

  Data Visualization Flags

  Understand data visualization flags in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger)

* [![Capturing Data with Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/e4f0e2ed-45af-4558-8dbd-04be6afe4bd7?resizing_type=fit&width=640&height=640)

  Capturing Data with Chaos Visual Debugger

  Capture and play back recordings with Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger)

* [chaos visual debugger](https://dev.epicgames.com/community/search?query=chaos%20visual%20debugger)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Launch Chaos Visual Debugger](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#launchchaosvisualdebugger)
* [Inside the Unreal Editor](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#inside-the-unreal-editor)
* [As a Standalone Program](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#as-a-standalone-program)
* [Explore the CVD User Interface](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#explorethecvduserinterface)
* [Menu Bar](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#nbsp-nbsp-menu-bar)
* [Main Toolbar](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#nbsp-nbsp-main-toolbar)
* [Viewport Toolbar](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#viewport-toolbar)
* [Hamburger Menu](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#hamburger-menu)
* [View Mode](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#view-mode)
* [Lighting Mode](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#lighting-mode)
* [Show Button](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#show-button)
* [Transform and Snapping Toolbar](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#transform-and-snapping-toolbar)
* [Scene Outliner](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#scene-outliner)
* [Playback Controls](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#playback-controls)
* [Game Frames Timeline](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#game-frames-timeline)
* [Solver Timeline](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#solver-timeline)
* [Solver Stage Timeline](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#solver-stage-timeline)
* [Recorded Output Log](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#recorded-output-log)
* [Output Log](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#output-log)
* [Details Panel](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#details-panel)
* [Next Up](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger?application_version=5.7#nextup)
