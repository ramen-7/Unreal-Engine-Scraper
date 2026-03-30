<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7 -->

# Data Visualization Flags

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
8. [Getting Started with Chaos Visual Debugger](/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger "Getting Started with Chaos Visual Debugger")
9. Data Visualization Flags

# Data Visualization Flags

Understand data visualization flags in Chaos Visual Debugger.

![Data Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/f0aa4f18-8e27-45d0-822f-33f4bb154676?resizing_type=fill&width=1920&height=335)

 On this page

To help you identify unusual physics behavior, **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) provides debug draw tools to visualize aspects of your application that are not normally visible during runtime.

You can control which debug draw tools are visualized in the viewport by toggling data flags. Data flags are organized into the following categories:

* [Collision Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#collisions)
* [Scene Queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#scene-queries)
* [Particle Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#particle-data)
* [Joint Constraints](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#joint-constraints)
* [Character Ground Constraints](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#character-ground-constraints)
* [Generic Debug Draw Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#generic-debug-draw-data)
* [Acceleration Structures](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#acceleration-structures-data)
* [Common Show Flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger#common-show-flags)

Certain flags, such as **Center of Mass**, can have a performance impact on CVD. If the debug draw limit is reached, a warning appears in the viewport reading:

`Max Debug Draw lines limit reached! Try selecting fewer debug draw categories or focus the camera in a narrower area.`

## Collision Data

Visualized collision data can help you identify areas where collisions are behaving unexpectedly. For example, when two objects intersect one another, instead of colliding as expected.  
  
To enable collision data, follow these steps:

1. In the Viewport Toolbar, click **Show > Collision Data Flags > Enable Draw**. This option opens a list of data flags.

   [![Collision Data Flags](https://dev.epicgames.com/community/api/documentation/image/9ea5a13b-382c-4b4e-af5b-7731444b1291?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9ea5a13b-382c-4b4e-af5b-7731444b1291?resizing_type=fit)
2. Choose from the list of data flags to toggle on or off.

   [![Collision Data Flags](https://dev.epicgames.com/community/api/documentation/image/e2a0bb1c-c473-4241-b65a-40b08a7ed42a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2a0bb1c-c473-4241-b65a-40b08a7ed42a?resizing_type=fit)
3. Click **Collision Data Visualization Settings** to customize how the data is drawn in the viewport.

   [![Collision Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/db5da910-e6b2-46d0-955d-256c8976c93e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db5da910-e6b2-46d0-955d-256c8976c93e?resizing_type=fit)

The visualization settings include the following options:

* **Show Debug Text:** Toggles viewport debug text (if any) on and off.
* **Depth Priority:** Draws data in **worldspace** or in the **foreground** (always on top of any other scene components).
* **Options for Scale and Radius:** Control the size of debug draw elements, making them easier to see in the viewport.

Most data flags include visualization settings that contain similar toggleable features.

## Scene Queries

Visualized [scene queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview) (line traces, sweeps, and overlaps) can help you debug cases where you performed a query during runtime but the query didn't find an expected object.

To enable scene query data, follow these steps:

1. In the Viewport Toolbar, click **Show > Scene Query Data Flags > Enable Draw**. This option opens a list of data flags.

   [![Scene Query Data Flags](https://dev.epicgames.com/community/api/documentation/image/79d126a2-4bce-442c-8a33-3817116c4e60?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79d126a2-4bce-442c-8a33-3817116c4e60?resizing_type=fit)
2. Choose from the list of data flags to toggle on or off.

   [![Scene Query Flags](https://dev.epicgames.com/community/api/documentation/image/99c5e2ee-8b97-45e3-98bc-12d9fe59b999?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99c5e2ee-8b97-45e3-98bc-12d9fe59b999?resizing_type=fit)
3. Click **Scene Query Visualization Settings** to customize how the data is drawn in the viewport.

   [![Scene Query Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/51680a59-f24b-4cb5-9b9c-515ac3054ecd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51680a59-f24b-4cb5-9b9c-515ac3054ecd?resizing_type=fit)

## Particle Data

Visualized particle data can help you identify irregular particle behavior, such as a particle moving faster than expected after applying a force.

To enable particle data, follow these steps:

1. In the Viewport Toolbar, click **Show > Particle Data Flags > Enable Draw**. This option opens a list of data flags.

   [![Particle Data Flags](https://dev.epicgames.com/community/api/documentation/image/0ada1c65-ed71-4e60-923c-408f6226caed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ada1c65-ed71-4e60-923c-408f6226caed?resizing_type=fit)
2. Choose from the list of data flags to toggle on or off.

   [![Particle Data Flags](https://dev.epicgames.com/community/api/documentation/image/8d48d5b9-6dd0-47ed-958e-fb3db934b5c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d48d5b9-6dd0-47ed-958e-fb3db934b5c3?resizing_type=fit)
3. Click **Particle Data Visualization Settings** to customize how the data is drawn in the viewport.

   [![Particle Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/53b5db12-2911-44cc-98fd-6b483b13bf02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/53b5db12-2911-44cc-98fd-6b483b13bf02?resizing_type=fit)

CVD only records and visualizes **physics thread** particle data, not **game thread** particle data. Game thread particle data is not visualized.

### Geometry

Most particles have both [simple and complex collision geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine), but only one is used for collision detection.

Options for toggling between simple and complex geometry, and other geometry visualization flags, are located in the Viewport Toolbar under **Show > Geometry Flags** menu.

[![Geometry Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/827f8506-06a4-4562-9ab1-15f250a3e89b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/827f8506-06a4-4562-9ab1-15f250a3e89b?resizing_type=fit)

**Query Only** geometry is visualized with translucent material. You can click through translucent materials by pressing **T** (or click **Allow Translucent Selection** in the Hamburger Menu) to enable or disable translucent selects.

### Particle Colorization

To increase draw visibility, you can choose to colorize particles using the following modes:

* **None:** Draws particles in default gray.
* **State:** Colorizes based on a [physics body’s state](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-bodies-reference-for-unreal-engine) in a simulation (dynamic, sleeping, kinematic, or static).
* **Shape Type:** Colorizes based on [collision geometry type](https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine) (simple shapes, convex, heightfield, or trimesh).
* **Client Server:** Colorizes based on client or server-spawned particles.

![State and Default Gray](https://dev.epicgames.com/community/api/documentation/image/e27a71d1-eff0-4a3f-9cd8-44e7e4152095?resizing_type=fit&width=1920&height=1080)![State and Default Gray](https://dev.epicgames.com/community/api/documentation/image/d1e27353-843d-400a-bf20-3f6e08ab3cd0?resizing_type=fit&width=1920&height=1080)

**State and Default Gray**

To change the mode and customize the colors, follow these steps:

1. In the Viewport Toolbar, click **Show > Particle Colorization**.

   [![Particle Colorization](https://dev.epicgames.com/community/api/documentation/image/f231e948-63ac-4011-a816-e6edac6e724e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f231e948-63ac-4011-a816-e6edac6e724e?resizing_type=fit)
2. In the **Colors Mode** dropdown, click the **Particle Color Mode** dropdown, and select the mode to use.

   [![Particle Color Mode](https://dev.epicgames.com/community/api/documentation/image/89512faf-0314-463a-9918-2790c7792f37?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89512faf-0314-463a-9918-2790c7792f37?resizing_type=fit)
3. Click the **Colors by [mode]** dropdown menu to customize colors. Then, click a color tile to open a contextual color picker.

   [![Color Picker](https://dev.epicgames.com/community/api/documentation/image/48f45e74-eebb-49ea-994c-54dd66ccd0fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48f45e74-eebb-49ea-994c-54dd66ccd0fe?resizing_type=fit)

The table below describes the contextual color picker user interface (UI).

| Number | Description |
| --- | --- |
| 1 | Color wheel (or color spectrum if toggled). |
| 2 | Displays current and previously selected colors. |
| 3 | Toggles sRGB preview. |
| 4 | Toggles between the color wheel and color spectrum. |
| 5 | Toggles visibility of **Color Schemes**. |
| 6 | Eyedropper tool. |
| 7 | RBG/HSV sliders. |
| 8 | Alpha slider. |
| 9 | Displays the current color’s hex code. |
| 10 | **Color Schemes**: Functions similarly to swatches in Adobe Photoshop and other design programs. |

## Joint Constraints

Visualized joint constraints can help you debug unwanted ragdoll behavior, such as twisting joints. CVD records joint constraint data as an individual piece of data for every frame. Due to this, maintaining a selection across gameplay frames is not currently possible.

To enable joint constraint data, follow these steps:

1. In the Viewport Toolbar, click **Show > Joint Constraint Data Flags > Enable Draw**. This option opens a list of data flags.

   [![Enable Joint Constraint Flags](https://dev.epicgames.com/community/api/documentation/image/ac26e55b-0a10-4f63-9b6d-39e7f6cf757d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac26e55b-0a10-4f63-9b6d-39e7f6cf757d?resizing_type=fit)
2. Choose from the list of data flags to toggle on or off.

   [![Joint Constraint Flags](https://dev.epicgames.com/community/api/documentation/image/0ba4e021-5d82-48c7-ae94-795dfe8ba02e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ba4e021-5d82-48c7-ae94-795dfe8ba02e?resizing_type=fit)
3. Click **Joint Constraint Visualization Settings** to customize how the data is drawn in the viewport.

   [![Joint Constraint Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/415f01aa-cb92-4bcd-8d97-3ff38b6ee6b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/415f01aa-cb92-4bcd-8d97-3ff38b6ee6b7?resizing_type=fit)

CVD doesn’t record joint constraints by default. To enable it, click the **Data Channel** dropdown menu in the main toolbar, and check **JointConstraints**.

[![Enable Join Constraints](https://dev.epicgames.com/community/api/documentation/image/386e084f-8088-449f-88d7-bc52f9d1cd8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/386e084f-8088-449f-88d7-bc52f9d1cd8e?resizing_type=fit)

## Character Ground Constraints

CVD can record the state of character ground constraints used by Unreal Engine’s Character Movement System, called [Mover 2.0](https://dev.epicgames.com/documentation/en-us/unreal-engine/mover-in-unreal-engine). Using this flag, you can identify and debug unusual behavior such as characters floating above or clipping through a ground plane.

To enable character ground constraint data, follow these steps:

1. In the Viewport Toolbar, click **Show > Character Ground Constraints Data Flags > Enable Draw**. This option opens a list of data flags.

   [![Enable Ground Constraints](https://dev.epicgames.com/community/api/documentation/image/1e369991-f8fd-4159-8f06-dad4a8659a46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e369991-f8fd-4159-8f06-dad4a8659a46?resizing_type=fit)
2. Choose from the list of data flags to toggle on or off.

   [![Ground Constraint Flags](https://dev.epicgames.com/community/api/documentation/image/5e2ba581-b962-4d0f-85fc-225c00161e1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e2ba581-b962-4d0f-85fc-225c00161e1e?resizing_type=fit)
3. Click **Character Ground Constraints Visualization Settings**, to customize how the data is drawn in the viewport.

   [![Ground Constraint Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/ae67fadb-923f-4623-a516-a169629f5514?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae67fadb-923f-4623-a516-a169629f5514?resizing_type=fit)

CVD doesn’t record character ground constraints by default. To enable it, click the **Data Channel** dropdown menu in the main toolbar, and check **Character Ground Constraints**.

[![Data Channels Ground Constraints](https://dev.epicgames.com/community/api/documentation/image/dde73ca5-6cf5-4e78-bda8-81bfa8031f82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dde73ca5-6cf5-4e78-bda8-81bfa8031f82?resizing_type=fit)

## Generic Debug Draw Data

The following C++ macros and Blueprint [nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/nodes-in-unreal-engine) record debug draw shapes directly in CVD. Debug draw shapes can offer context when debugging physics calculations.

For example, if you use two points in space to calculate a force applied to a physics body, CVD only shows the body before and after the force is applied. If something looks off, you can use generic debug draw macros (or Blueprint nodes) to visualize the two points, and the force, frame-by-frame. This workflow can provide context on how the force was calculated and help you to correct it.

### C++ Macros

Depending on the shape you need to draw, each macro has its own set of parameters — except for the following optional parameters, which each macro uses:

| Macro | Parameter | Description |
| --- | --- | --- |
| **TraceDebugDrawBox** | **InBox** | The shape you want to record. |
| All macros | **Tag** | The FName that is used as a tag for filtering, search, and debug draw as a text tag in CVD’s viewport. |
| All macros | **Color** | The color to apply to this shape when it’s debug drawn in CVD. |
| All macros | **SolverID** | The ID of the solver this shape should be associated with. If no ID is provided, this shape is added as part of the current game from data bucket. |
| **TraceDebugDrawLine**, **TraceDebugDrawVector** | **InStartLocation** | The start point of the line. |
| **TraceDebugDrawLine** | **InEndLocation** | The end point of the line. |
| **TraceDebugDrawVector** | **InVector** | The vector you want to record. |
| **TraceDebugDrawSphere** | **Center** | The origin point of the sphere. |
| **TraceDebugDrawSphere** | **Radius** | The radius of the sphere. |
| All macros | **Owner** | Any UObject this debug draw shape is related to. This is used internally to know if a shape is recorded from a server solver or a client solver. |

### Blueprint Nodes

The following generic debug draw macros can also be implemented as function nodes in a Blueprint’s **Event Graph:**

* CVD Record Debug Draw Sphere
* CVD Record Debug Draw Box
* CVD Record Debug Draw Line

[![Event Graph](https://dev.epicgames.com/community/api/documentation/image/62a34414-91df-4c83-8ff8-5961173e1297?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/62a34414-91df-4c83-8ff8-5961173e1297?resizing_type=fit)

For more information about each node, see the Chaos Visual Debugger section of [Unreal Engine Blueprint API Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI?application_version=5.6).

#### Enable Generic Debug Draw Data

To enable generic debug draw data, follow these steps:

1. In the Viewport Toolbar, click **Show > Generic Debug Draw Data Flags > Enable Draw**. This option opens a list of data flags.

   [![Generic Debug Draw Data Flags](https://dev.epicgames.com/community/api/documentation/image/a6018ff5-47f1-4a97-a18c-624fc2fbeda8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a6018ff5-47f1-4a97-a18c-624fc2fbeda8?resizing_type=fit)
2. Choose from the list of data flags to toggle on or off.

   [![Generic Debug Draw Options](https://dev.epicgames.com/community/api/documentation/image/756db150-83e0-45c0-9977-92190fd2b199?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/756db150-83e0-45c0-9977-92190fd2b199?resizing_type=fit)
3. Click **Generic Debug Draw Data Visualization Settings** to customize how the data is drawn in the viewport.

   [![Generic Debug Draw Data Enabled](https://dev.epicgames.com/community/api/documentation/image/77786f4c-c0f3-4c2d-9b37-41862865dba5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/77786f4c-c0f3-4c2d-9b37-41862865dba5?resizing_type=fit)

## Acceleration Structures

CVD can record and visualize acceleration structures used by the scene query system, which is currently an AABB (Axis-Aligned Bounding Box) Tree. An AABB Tree is a bounding volume hierarchy you can use to determine potential overlaps between objects.

In CVD, you can use AABB Tree visualization to see the composition of the tree and the bounds of each object as they were added to the tree.

This visualization is useful when an object that a scene query should have hit wasn’t hit, or wasn’t even evaluated by the physics engine. You can use AABB Tree visualization in CVD to inspect the bounds of the object and determine whether the error was caused by, for example, the bounds failing to encompass the object visually or incorrect bounds within the tree.

To customize which acceleration structure data flags are drawn, follow these steps:

1. In the **Viewport, click Show > Acceleration Structure Data Flags**, and select your desired data flags.

   [![Acceleration Structure Data Flags](https://dev.epicgames.com/community/api/documentation/image/9a13ca39-2994-4867-b21f-ae3065f639aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a13ca39-2994-4867-b21f-ae3065f639aa?resizing_type=fit)
2. Click **Acceleration Structure Visualization Settings** to customize how the data is drawn in the viewport.

   [![Acceleration Structure Visualization Settings](https://dev.epicgames.com/community/api/documentation/image/5494ebf5-786f-4931-b178-5fbe4aa850a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5494ebf5-786f-4931-b178-5fbe4aa850a5?resizing_type=fit)

CVD doesn’t record acceleration structures by default. To enable it, click the **Data Channel** dropdown menu in the Main Toolbar, and check **Acceleration Structures Data**.

[![Enable Acceleration Structure Data Channel](https://dev.epicgames.com/community/api/documentation/image/6cc18ae6-9aa9-4c9f-87f0-ed81380d628c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cc18ae6-9aa9-4c9f-87f0-ed81380d628c?resizing_type=fit)

## Common Show Flags

The **Common Show Flags** menu contains flags derived from the engine itself that can assist with visibility in CVD.

To customize which flags are enabled, in the Viewport Toolbar, click the **Show > Common Show Flags**.

[![Common Show Flags](https://dev.epicgames.com/community/api/documentation/image/aed15348-2a74-4177-a503-f08b51f32c6a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aed15348-2a74-4177-a503-f08b51f32c6a?resizing_type=fit)

## Next Up

* [![Data Inspectors](https://dev.epicgames.com/community/api/documentation/image/e41606f4-f2e2-4f65-bf67-295486d1ef4f?resizing_type=fit&width=640&height=640)

  Data Inspectors

  Understand data inspectors in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger)

* [![Capturing Data with Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/e4f0e2ed-45af-4558-8dbd-04be6afe4bd7?resizing_type=fit&width=640&height=640)

  Capturing Data with Chaos Visual Debugger

  Capture and play back recordings with Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger)

* [chaos visual debugger](https://dev.epicgames.com/community/search?query=chaos%20visual%20debugger)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Collision Data](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#collisions)
* [Scene Queries](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#scene-queries)
* [Particle Data](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#particle-data)
* [Geometry](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#geometry-visualization-flags)
* [Particle Colorization](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#particle-colorization)
* [Joint Constraints](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#joint-constraints)
* [Character Ground Constraints](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#character-ground-constraints)
* [Generic Debug Draw Data](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#generic-debug-draw-data)
* [C++ Macros](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#c++macros)
* [Blueprint Nodes](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#blueprint-nodes)
* [Enable Generic Debug Draw Data](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#enabling-generic-debug-draw-data)
* [Acceleration Structures](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#acceleration-structures-data)
* [Common Show Flags](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#common-show-flags)
* [Next Up](/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger?application_version=5.7#nextup)
