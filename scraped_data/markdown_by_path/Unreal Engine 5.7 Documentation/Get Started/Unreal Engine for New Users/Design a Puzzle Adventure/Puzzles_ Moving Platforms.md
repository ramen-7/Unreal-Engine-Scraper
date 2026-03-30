<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7 -->

# Puzzles: Moving Platforms

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Design a Puzzle Adventure](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine "Design a Puzzle Adventure")
8. Puzzles: Moving Platforms

# Puzzles: Moving Platforms

In the second part of the platformer puzzle, create the moving platforms with blueprints and learn how to debug your script.

![Puzzles: Moving Platforms](https://dev.epicgames.com/community/api/documentation/image/8c84da04-714f-4651-ad6e-cac4f3fcf149?resizing_type=fill&width=1920&height=335)

 On this page

In this tutorial, you’ll create logic to power a moving platform, and activate it with the gameplay objects you built in [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine). You’ll also incorporate the game mechanic time into your puzzle.

By using a modular workflow, you’ll be able to modify the platform's scale, movement, destination, and speed from the viewport. You’ll also be able to choose which platform any switch activates in a single click.

With this flexibility, you can make changes to your level and test its functionality on the fly as you design. Efficient and flexible design choices improve the speed and resilience of your development pipeline.

## Before You Begin

This tutorial assumes you already have an understanding of the following topics, which are covered in the previous sections of [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

* Materials
* Blueprints
* Variables
* Blueprint Interfaces
* Play-In-Editor mode

You’ll need the following assets created in [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine) and [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine):

* `BP_Switch`
* `BP_Cube`
* `BP_Key`
* `BPI_Interaction`
* `M_BasicColor`
* `M_EmissiveColor`
* `M_BasicColor_Blue`

## Create a Moving Platform

By learning how to create a moving platform and activate it with a switch, you can design simple functionality such as transporting a player across a level. The switch, cube, and platform can be combined to create complex functionality such as an entire platforming puzzle — like the one we provide at the end of this tutorial.

To keep your workflow modular, you’ll begin by creating a material instance and a Blueprint class for the platform.

### Create a Material Instance

To create a material instance for the platform, follow these steps:

1. In the **Content Browser**, in **AdventureGame > Designer > Materials**, right-click **M\_BasicColor** and select **Create Material Instanc**e.
2. Name the instance `M_BasicColor_Orange`. Double-click the instance to open it in the **Material Editor**.
3. Expand **Global Vector Parameter Values**, and enable **Color** to override it.
4. Set the **Color** parameter to **Hex sRGB** value `F76E00FF`.

   [![Image-of-a-material-with-color-picker-open](https://dev.epicgames.com/community/api/documentation/image/79a3434c-8a07-4c16-b267-02a4dabd9781?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79a3434c-8a07-4c16-b267-02a4dabd9781?resizing_type=fit)
5. **Save** the instance and close it.

Your Materials folder should now look like this:

[![Image-of-materials-folder-content-assets](https://dev.epicgames.com/community/api/documentation/image/e24144f3-ebab-43f5-b758-c2a5d812e3ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e24144f3-ebab-43f5-b758-c2a5d812e3ac?resizing_type=fit)

### Set Up a Blueprint Class

To create a Blueprint class for the platform, follow these steps:

1. In the **Content Browser**, navigate to **AdventureGame > Designer > Blueprints** and create a new folder called **`Platforms`**.
2. Inside the **Platforms** folder, right-click and create a new **Blueprint Class**.
3. In the **Pick Parent Class** dialog, select **Actor** and name the new Blueprint `BP_Platform`.
4. Double-click it to open `BP_Platform` in the Blueprint Editor.
5. In the **Components** tab, create a static mesh by clicking **Add**, search for `cube`, and select it.
6. Name the mesh `Platform`.

   [![New-blueprint-actor-named-bp-platform](https://dev.epicgames.com/community/api/documentation/image/f5f71829-b886-44c5-9889-70631b5fd22e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5f71829-b886-44c5-9889-70631b5fd22e?resizing_type=fit)
7. In the **Details** panel, under the **Materials** heading, set **Element 0** to `M_BasicColor_Orange`.

   [![Details-panel-with-base-color-orange-being-set](https://dev.epicgames.com/community/api/documentation/image/3e9e8e6b-2d45-4223-aed0-60ac08cad873?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e9e8e6b-2d45-4223-aed0-60ac08cad873?resizing_type=fit)

To make your platform’s scale quickly customizable from within the Level Editor and make platforms of different sizes, you can use an editable variable:

1. In the **My Blueprint** tab, navigate to the **Variables** heading. Click the **+** button to create a variable and name it `PlatformScale`.
2. Set its pin type to **Vector** and click the **eye icon** so the eye is open.

   [![Menu-of-platform-scale-with-vector-option-and-open-eye](https://dev.epicgames.com/community/api/documentation/image/ffb83028-0e79-4a8e-b786-066b47dc592f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ffb83028-0e79-4a8e-b786-066b47dc592f?resizing_type=fit)
3. In the **Details** panel, next to **Category**, add it to the `Setup` category.
4. **Compile** your Blueprint, then set the **Default Value** of **PlatformScale** to `2`, `2`, `0.1`.

   [![Setting-the-platform-scale-values](https://dev.epicgames.com/community/api/documentation/image/5e079b04-f957-45e2-9070-d493d219ad9f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e079b04-f957-45e2-9070-d493d219ad9f?resizing_type=fit)
5. In the **Construction Script** graph, drag off the **Construction Script** node’s **Exec** pin and create **Set World Scale 3D (Platform)**.

   [![Blueprint-of-construction-script-node](https://dev.epicgames.com/community/api/documentation/image/c844669e-3f8c-47c9-8631-5ded4e327174?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c844669e-3f8c-47c9-8631-5ded4e327174?resizing_type=fit)
6. Drag off the **New Scale** pin on the **Set World Scale 3D** node and create a **Get PlatformScale** node. This applies new Scale values to the Platform mesh component.

   [![In-blueprints-connect-platform-scale-to-world-scale](https://dev.epicgames.com/community/api/documentation/image/945d0d47-9853-4323-b11a-824633b5a02e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/945d0d47-9853-4323-b11a-824633b5a02e?resizing_type=fit)
7. **Save** and **Compile**.

Your **Construction Script** graph should now look like this:

If copying this snippet into your graph, you’ll need to connect the **Construction Script** entry node to **Set World Scale 3D**.

Blueprint

Construction Script Snippet

Copy full snippet(35 lines long)

If you go back to the blueprint’s **Viewport** tab, you’ll see the construction script applied to the platform’s new scale values.

From the **Content Browser**, drag an instance of your platform into your level, or into **Room 1** if you’re following along with our provided level. For this tutorial, make sure you also have an instance of `BP_Switch` and `BP_Cube` in the level:

[![Image-of-level-with-platforms-and-a-cube](https://dev.epicgames.com/community/api/documentation/image/16baf45e-2c6c-43c8-b536-1e6756711221?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16baf45e-2c6c-43c8-b536-1e6756711221?resizing_type=fit)

## Build with Logic

When an object overlaps the switch, the platform should move back and forth between two locations. Before you begin building, let’s draft the logic that powers this interaction by answering the questions: *what* needs to happen to *who* — and *when*?

Here is a breakdown of the platform's logic:

If `BP_Platform` is **active**, then:

* If `BP_Platform` is at its **start location**, **move forward** to its **end location**, and **wait** for 2 seconds.
* If `BP_Platform` is at its **end location**, **move backward** to its **start location**, and **wait** for 2 seconds.

If `BP_Platform` is not **active**, then `BP_Platform` **stops**.

The reason for designating wait time is to allow the player time to get onto (or push something onto) the platform. You can scale the wait time depending on how difficult you want this gameplay task to be. Later on in this tutorial, you’ll use **time** to set the platform’s speed, which can also affect difficulty.

Since you’ve already created `BP_Platform`, you need a boolean to determine if it’s active or inactive.

To create a boolean, follow these steps:

1. In the **My Blueprint** tab of `BP_Platform`, click the **+** button to create a new variable and name it `Active`.
2. Set its pin type to **Boolean** and click the **eye icon** so it’s open.

   [![Image-of-the-menu-with-the-new-active-variable](https://dev.epicgames.com/community/api/documentation/image/de88d4d9-7078-4cee-8d99-4a32f3992d28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de88d4d9-7078-4cee-8d99-4a32f3992d28?resizing_type=fit)
3. In the **Details** panel, change the **Category** to `Setup`.
4. **Compile** your Blueprint and verify that the **Default Value** of **Active** has a checkmark (true).

   [![Details-tab-with-active-variable-selected](https://dev.epicgames.com/community/api/documentation/image/b2692e84-446c-40d4-ac71-bf2c3f54d7f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2692e84-446c-40d4-ac71-bf2c3f54d7f9?resizing_type=fit)

Next, you’ll define locations for the platform to move between.

### Define Locations

Your drafted logic states that the platform requires two locations:

* Start location
* End location

To keep your work modular, you’ll define the start location by referencing the platform's instance. You’ll define the end location by referencing a **target point actor**.

A **target point** is a non-rendering actor that has coordinate data. You can use target points as spawn points, to set animation paths, to guide AI movement, or to control the orientation of joints in IK rigs.

You’ll also need vectors to store the coordinate data from the platform instance and the target point actor, and implement it within `BP_Platform`:

|  |  |  |
| --- | --- | --- |
| Variable Name | Type | Explanation |
| **StartLocation** | Vector | Stores BP\_Platform’s coordinates. |
| **EndLocation** | Vector | Stores the Target Point actor’s coordinates. |
| **TargetPoint** | TargetPoint | The Target Point actor that designates your EndLocation in the level. |

To set up your variables, follow these steps:

1. In the **My Blueprint** tab, click the **+** button twice to create two new variables.
2. Name the variables  `StartLocation` and `EndLocation`.
3. Set the pin types to **Vector**.
4. Create a variable called `TargetPoint` and set the pin type to **Target Point (Object Reference)**. This variable type is used to reference target point actors within Blueprints.
5. With the `TargetPoint` variable selected, navigate to the **Details** panel. Change the **Category** to `Setup` and add a check to the checkbox for **Instance Editable**.

Your variable list should now look like this:

[![Image-with-all-the-settings-for-variables](https://dev.epicgames.com/community/api/documentation/image/b1b6e727-530e-4f95-a3c5-3392b6527898?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1b6e727-530e-4f95-a3c5-3392b6527898?resizing_type=fit)

With your variables created, you can add logic:

1. Navigate to the **EventGraph** and delete the **Event ActorBeginOverlap** and **Event Tick** nodes. You won't need them. Keep **Event BeginPlay**.
2. From the **Exec** pin of the **Event BeginPlay** node, drag out and create **Set StartLocation**.

   [![Blueprint-with-event-begin-play-node](https://dev.epicgames.com/community/api/documentation/image/14c24ac5-e300-49f2-a757-19a489a1fb20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14c24ac5-e300-49f2-a757-19a489a1fb20?resizing_type=fit)
3. From the **Start Location** pin, drag out and create **Get Actor Location**. Verify that the **Target** field is set to **Self**.

   [![Blueprint-with-get-actor-location-node](https://dev.epicgames.com/community/api/documentation/image/caeb314d-20fe-488a-ab6f-afd75b0c3548?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/caeb314d-20fe-488a-ab6f-afd75b0c3548?resizing_type=fit)
4. From the **Exec** pin of **Set StartLocation**, drag out and create **Set EndLocation**.

   [![Blueprint-showing-set-end-location-node](https://dev.epicgames.com/community/api/documentation/image/c262e9d9-238b-494f-89c4-17caa262a130?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c262e9d9-238b-494f-89c4-17caa262a130?resizing_type=fit)
5. From the **End Location Vector** pin, drag out and create **Get Actor Location**.
6. From the **Target** pin of **Get Actor Locatio**n, drag out and create **Get TargetPoint**.

   [![Blueprint-showing-get-actor-location-to-target-point](https://dev.epicgames.com/community/api/documentation/image/dd6971cf-496f-4163-a538-a8046ebdf94f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd6971cf-496f-4163-a538-a8046ebdf94f?resizing_type=fit)
7. **Save** and **Compile**.

  Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(56 lines long)

Now you can create a target point actor in your level for the Blueprint to reference:

1. From the editor’s main toolbar, click the **Add** button.
2. Search for **target point** and select it to create one in your level.

   [![Adding-a-target-point](https://dev.epicgames.com/community/api/documentation/image/e489bc7b-6a0d-4a32-b498-c205b15b39fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e489bc7b-6a0d-4a32-b498-c205b15b39fd?resizing_type=fit)
3. Move the target point to where you want the platform to end up. To follow along in the sample level, set the target point’s **Location** to `-6200`, `570`, `-5.5` (at the bottom of Room 1).
4. In the viewport, select the instance of `BP_Platform` and move it where you want the platform to start from.
5. With `BP_Platform` selected, in the **Setup** section of the **Details** panel next to **Target Point**, search for the instance of Target Point in your level (or use the eyedropper to select it in the viewport).

   [![Details-panel-settings-for-target-point](https://dev.epicgames.com/community/api/documentation/image/4e144fa9-84fa-4eb1-b1a7-df0e894dd6d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e144fa9-84fa-4eb1-b1a7-df0e894dd6d8?resizing_type=fit)

[![Image-of-level-with-crosshair-icon-for-target-point](https://dev.epicgames.com/community/api/documentation/image/0936c33d-a7b0-4e97-b7bc-c7b792443689?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0936c33d-a7b0-4e97-b7bc-c7b792443689?resizing_type=fit)

Next, you’ll build the platform's movement.

## Build Movement

Your drafted logic requires the platform to move in four ways:

* Move forward
* Wait
* Move backward
* Stop

To signal the events **forward**, **backward**, and **stop**, you’ll create custom events. The **wait** event can be created using a variable, later on.

To create custom events, follow these steps:

1. In `BP_Platform`’s **EventGraph**, right-click and create **Add Custom Event**.
2. Name the new node `evMoveForward`. You should see the event appear under the **EventGraph** heading in the **My Blueprint** tab.
3. Create two more custom events. Name them `evMoveBackward` and `evStop`.

   [![Ev-move-backward-and-ev-stop-nodes](https://dev.epicgames.com/community/api/documentation/image/43e9bbfa-7f0d-48df-8762-4037ef2d56a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43e9bbfa-7f0d-48df-8762-4037ef2d56a9?resizing_type=fit)
4. Since you only want the platform to move if the `Active` boolean is true, drag out from the **Exec** pin on the **Set End Location** node and create a **Branch** node.

   [![Exec-pin-to-set-location-node](https://dev.epicgames.com/community/api/documentation/image/08410cd5-2c84-4a46-8fb6-c426669027b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08410cd5-2c84-4a46-8fb6-c426669027b2?resizing_type=fit)
5. On the **Branch** node, drag out from the **Condition** pin and create **Get Active**.

   [![Condition-pin-to-get-active-node](https://dev.epicgames.com/community/api/documentation/image/4412b9d7-9520-47e0-8592-6423e119c984?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4412b9d7-9520-47e0-8592-6423e119c984?resizing_type=fit)
6. From the **True** pin of the **Branch** node, drag out and create **EvMoveForward** to trigger that event.

   [![Create-the-ev-move-forward-trigger](https://dev.epicgames.com/community/api/documentation/image/dada728e-b721-457b-8202-2606863cea59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dada728e-b721-457b-8202-2606863cea59?resizing_type=fit)
7. **Save** and **Compile**.

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(102 lines long)

If you test your platform in PIE mode, the platform won't do anything. This is because custom events only signal an event; they need further logic to describe the platform’s movement.

### Create Forward Movement

To power your custom events, you’ll use a **Timeline** node. Within a timeline, you can create two keyframes that represent the platform’s start and end locations.

To create a timeline, follow these steps:

1. Right-click in the **EventGraph**, search for and create **Add Timeline**.

   Make sure you don’t select Add Timeline Component.
2. Name the timeline node `TM_MovePlatform`.

   When you created the timeline node, a **TM\_MovePlatform** reference appears in the **Components** list of the **My Blueprint** panel. Similar to other components, you can use this reference in the graph to get or set its properties.
3. Connect the **Exec** pin from **evMoveForward** to the **Play** pin of **TM\_MovePlatform**.
4. Connect the **Exec** pin from **evStop** to the **Stop** pin of **TM\_MovePlatform**.
5. Connect the **Exec** pin from **evMoveBackward** to the **Reverse** pin.

   [![TM-move-platform-node-connected-to-custom-event-nodes](https://dev.epicgames.com/community/api/documentation/image/12f124c7-fb9e-485a-8fb0-967e44fb503f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12f124c7-fb9e-485a-8fb0-967e44fb503f?resizing_type=fit)
6. Double-click on **TM\_MovePlatform** to open the **Timeline Editor**. Your timeline is currently blank, so press the **Track** button and select **Float Track** as the track type.

   [![Add-float-track-menu-option](https://dev.epicgames.com/community/api/documentation/image/ff63cbe6-8d7e-4f21-8048-6aa772d20178?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff63cbe6-8d7e-4f21-8048-6aa772d20178?resizing_type=fit)
7. Name this new track `Alpha`.
8. Set the **Length** of the track to `1.00`. This is how many seconds the timeline plays from start to finish.

   [![Image-of-the-float-track-timeline](https://dev.epicgames.com/community/api/documentation/image/59e0a98c-a74a-4d99-ac81-45ab8fef6925?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/59e0a98c-a74a-4d99-ac81-45ab8fef6925?resizing_type=fit)
9. To add a keyframe, right-click in the timeline and select **Add key to CurveFloat\_0**.

   [![Menu-option-for-add-a-key](https://dev.epicgames.com/community/api/documentation/image/85cbbc3e-09b2-4282-b382-0a9158a7eeb6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/85cbbc3e-09b2-4282-b382-0a9158a7eeb6?resizing_type=fit)
10. Set the keyframe’s **Time** and **Value** to `0.0`.
11. Right-click the key and change the **Key Interpolation to Auto**. This adds easing to the graph curves; making your platform move slower at the beginning and end of its movement.

    [![Key-interpolation-menu-option-for-auto](https://dev.epicgames.com/community/api/documentation/image/ac15ec70-7cd3-451a-a495-ddf2ed23d738?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac15ec70-7cd3-451a-a495-ddf2ed23d738?resizing_type=fit)
12. Add a second keyframe, but set the **Time** and **Value** to `1.0`, and set the **Key Interpolation** to **Auto**.
13. **Save** and **Compile**.

Your Timeline should now look like this:

[![Image-of-graph-with-wave-line-over-time](https://dev.epicgames.com/community/api/documentation/image/19a503c9-b1bb-4e1f-96bd-0705c2b1b7fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19a503c9-b1bb-4e1f-96bd-0705c2b1b7fd?resizing_type=fit)

To create movement, you’ll instruct the platform to incrementally set itself a new location per each game frame, along a linear path, between the start and end locations. If you’re familiar with animation software, you can think of this as tweening. To do this, you’ll use a **Lerp** (linear interpolation) node.

Lerp nodes use an alpha, like the one you created in `TM_MovePlatform`, to incrementally blend between two values. You can use lerps to interpolate colors, materials, or in this case, locations.

To create a lerp and connect it to your existing logic, follow these steps:

1. Go back to the **EventGraph** tab. Drag from the **Update** pin of **TM\_MovePlatform** and create **Set World Location (Platform)**.

   [![Use-the-update-pin-and-set-world-location](https://dev.epicgames.com/community/api/documentation/image/25253e48-1e05-449d-902e-f0f4c7a3a7b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25253e48-1e05-449d-902e-f0f4c7a3a7b5?resizing_type=fit)
2. From the **New Location** pin of **Set World Location**, drag out and create **Lerp (Vector)**.

   [![Drag-out-and-create-a-lerp-vector](https://dev.epicgames.com/community/api/documentation/image/a77760d9-b854-4a28-9544-7dbd334cd8e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a77760d9-b854-4a28-9544-7dbd334cd8e1?resizing_type=fit)
3. From the **A** pin of the **Lerp** node, drag out and create **Get StartLocation**.
4. From the **B** pin of the **Lerp** node, drag out and create **Get EndLocation**.

   [![Drag-out-and-create-get-end-location](https://dev.epicgames.com/community/api/documentation/image/c8ef473d-2a13-46c0-9891-30423f894d0f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c8ef473d-2a13-46c0-9891-30423f894d0f?resizing_type=fit)
5. To utilize the alpha you created in **TM\_MovePlatform**, connect the **Alpha** pin of **TM\_MovePlatform** to the **Alpha** pin of the **Lerp**.

   [![Connect-the-tm-move-platform-to-the-lerp](https://dev.epicgames.com/community/api/documentation/image/c9f4b6be-1e46-467e-b126-36a288db527d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9f4b6be-1e46-467e-b126-36a288db527d?resizing_type=fit)
6. **Save**, **Compile**, and close the Blueprint Editor.

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(177 lines long)

Now you have enough logic to test your platform. In the editor’s main toolbar, click the **Play** button to enter PIE mode. At runtime, your platform should move to the end location. The platform moves fast right now so it might be hard to observe. Next, you’ll add backwards movement so the platform moves continuously when active. Later, you’ll add a variable to slow it down.

You can experiment with moving the target point around your level to see the effect.

The timeline you made is one second long, so the platform always takes one second to move from its starting location to the Target Point. The further you place the platform from the Target Point, the faster it needs to move to cover that distance.

![Gif-clip-of-yellow-platform-traveling-up-a-level](https://dev.epicgames.com/community/api/documentation/image/d5c054c0-fbdf-41e2-9af3-a9029cbe824c?resizing_type=fit)

So far, the platform only moves in one direction. Next, you’ll build its backwards movement.

### Create Backward Movement

To reverse the platform’s movement, you’ll need logic that checks which direction its timeline is moving. If it’s moving forward, the logic should call `evMoveBackwards`. If it’s not moving forward, the logic should call `evMoveForward`. You can use a branch node to handle this check.

To create a branch node and connect it to your existing logic, follow these steps:

1. From the **Finished** pin of the **TM\_MovePlatform**, drag out and create a **Branch** node.

   [![Dragging-out-a-pin-to-make-a-new-branch-node](https://dev.epicgames.com/community/api/documentation/image/cec7b984-b6c7-4a6d-9872-f8191144f87c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cec7b984-b6c7-4a6d-9872-f8191144f87c?resizing_type=fit)
2. From the branch’s **Condition** pin, drag out and create **Equal (Enum)**.

   [![Condition-pin-to-equal-node](https://dev.epicgames.com/community/api/documentation/image/439957e0-1b0e-4f48-8188-4c9b736d72a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/439957e0-1b0e-4f48-8188-4c9b736d72a9?resizing_type=fit)
3. Connect the **Direction** pin of **TM\_MovePlatform** to the **A** pin of **Equal**.

   [![Direction-pin-to-equal-node](https://dev.epicgames.com/community/api/documentation/image/f7fc65bd-2d32-4704-bc79-368c5d51e449?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7fc65bd-2d32-4704-bc79-368c5d51e449?resizing_type=fit)
4. Verify that the condition is set to **Forward**.
5. From the **True** pin of the branch, drag out and create **evMoveBackward****s**.
6. From the **False** pin of the branch, drag out and create **evMoveForward**.

   [![BP-image-with-e-move-forward-and-e-move-backward](https://dev.epicgames.com/community/api/documentation/image/0d70d0c2-3c39-4d59-bced-26409e6943a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d70d0c2-3c39-4d59-bced-26409e6943a6?resizing_type=fit)
7. Since you only want movement to occur if the `Active` boolean is true, check this first with another branch:

   1. To add a new node between **TM\_MovePlatfor****m** and the **Branch** node, drag from the **Finished** pin and add a new **Branch** node. This keeps the existing connections and adds the second Branch node in between.

      [![Condition-pin-to-get-active](https://dev.epicgames.com/community/api/documentation/image/68f68f11-ac5a-4287-b3d9-0d9dd39e2427?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68f68f11-ac5a-4287-b3d9-0d9dd39e2427?resizing_type=fit)
   2. From the **Condition** pin on the new **Branch** node, drag out and create **Get Active**.

      [![Use-the-finish-pin-to-a-new-branch-node](https://dev.epicgames.com/community/api/documentation/image/ffd1d232-a88c-48b5-93cf-061c9b060205?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ffd1d232-a88c-48b5-93cf-061c9b060205?resizing_type=fit)
8. **Save** and **Compile**.

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(243 lines long)

![Yellow-platform-raising-up-to-meet-top-of-wall](https://dev.epicgames.com/community/api/documentation/image/36865abc-58e4-4f0e-9ee3-78b213c43d0e?resizing_type=fit)

However, your draft logic states that the platform must wait for a duration of time before changing direction. Next, you’ll build this delay.

### Create a Delay

You can use a delay node to instruct the platform to wait, and a float-type variable to define the amount of time you want it to wait for.

To create a delay node and a float, follow these steps:

1. In the **My Blueprint** tab of `BP_Platform`, click the **+** button to to create a new variable and name it `WaitDuration`.
2. Set its pin type to **Float**.
3. In the **Details** panel, add it to the **Setup** category and enable **Instance Editable**.
4. **Compile** to access the variable’s **Default Value** and set it to `2` seconds. This is the time we’re using in the sample level.

   [![Details-tab-wait-duration-field](https://dev.epicgames.com/community/api/documentation/image/2968bd8e-3e28-4ec5-bc9b-46b4b6c4c8b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2968bd8e-3e28-4ec5-bc9b-46b4b6c4c8b3?resizing_type=fit)
5. To add the delay before the platform changes directions, drag from the **Finished** pin on **TM\_MovePlatform**, and create a **Delay** node.

   [![Create-a-delay-node](https://dev.epicgames.com/community/api/documentation/image/9b5d5221-a64d-44ef-84e2-2e40164d0f0c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b5d5221-a64d-44ef-84e2-2e40164d0f0c?resizing_type=fit)
6. From the **Duration** pin of the **Delay**, drag out and create **Get Wait Duration**.

   [![Create-get-wait-duration-node](https://dev.epicgames.com/community/api/documentation/image/c17504c0-6884-44a4-b11c-560ce9372be4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c17504c0-6884-44a4-b11c-560ce9372be4?resizing_type=fit)
7. **Save** and **Compile**.

Your variable list should now look like this:

[![Various-variable-options-in-the-my-blueprint-tab](https://dev.epicgames.com/community/api/documentation/image/b6efffa4-ff0f-4fb4-9b4d-49973fa00765?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b6efffa4-ff0f-4fb4-9b4d-49973fa00765?resizing_type=fit)

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(263 lines long)

Test your platform in PIE mode. It should move forwards, wait, then move backwards, wait, and repeat indefinitely.

![GIF-clip-of-player-getting-onto-a-platform-that-moves-up-and-back-down](https://dev.epicgames.com/community/api/documentation/image/fb61a378-857f-4773-9439-4dc7bd2db8d0?resizing_type=fit)

Finally, you need to activate your platform through `BP_Switch`.

## Connect the Switch to the Platform

The platform should only move when `BP_Switch` is activated by a player or other object. You’ll use the Blueprint interface functions you created in [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine), and your `Active` boolean, to signal when the platform should move forward and stop.

To make the switch’s `BPI_Interaction` messages start and stop the platform’s movement, follow these steps:

1. In `BP_Platform`, in the Blueprint Editor’s menu bar, click **Class Settings**.

   [![Blueprint-editor-menu-bar](https://dev.epicgames.com/community/api/documentation/image/93de5f1c-b065-406d-9943-b5b4428c201c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93de5f1c-b065-406d-9943-b5b4428c201c?resizing_type=fit)
2. In the **Details** panel, under the **Interfaces** headings, click the dropdown menu next to **Implemented Interfaces**. Search for and add **BPI\_Interaction**.

   [![Details-panel-implemented-interfaces](https://dev.epicgames.com/community/api/documentation/image/e89464c7-8720-4caf-9f91-8165f3179653?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e89464c7-8720-4caf-9f91-8165f3179653?resizing_type=fit)
3. This creates a new **Interfaces** heading in the My Blueprint tab.

   [![New-interfaces-section-in-details-tab](https://dev.epicgames.com/community/api/documentation/image/c71a1d1a-9c93-4073-8d3a-f9dc8eaebeef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c71a1d1a-9c93-4073-8d3a-f9dc8eaebeef?resizing_type=fit)
4. In the **Interfaces** heading, right-click **fnBPISwitchOn** and select **Implement Event** to populate it to the **EventGraph** as an event.

   [![In-implement-event-choose-fn-bpi-switch-on](https://dev.epicgames.com/community/api/documentation/image/2259212c-8ec0-48c1-86a5-7b60c565d093?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2259212c-8ec0-48c1-86a5-7b60c565d093?resizing_type=fit)
5. Do the same for **fnBPISwitchOff**.
6. From the **Exec** pin of **fnBPISwitchOn**, search for and create **Set Active**. Select the checkbox next to **Active** to set its value to true.
7. From the **Exec** pin of the **Set** node, search for and create **EvMoveForward**.

   [![Create-an-ev-move-forward-node](https://dev.epicgames.com/community/api/documentation/image/56b2f88f-0820-4287-885e-c794a3df9d4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56b2f88f-0820-4287-885e-c794a3df9d4e?resizing_type=fit)
8. From the **Exec** pin of **fnBPISwitchOff**, search for and create **Set Active**.

   [![Create-a-set-active-node](https://dev.epicgames.com/community/api/documentation/image/c79f40b8-181a-414b-996b-b02946e3e177?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c79f40b8-181a-414b-996b-b02946e3e177?resizing_type=fit)
9. From the **Exec** pin of the **Set** node, search for and create **EvStop**.
10. **Save** and **Compile**.

All of the logic that powers `BP_platform` is complete. Now that you’ve done the heavy lifting, you can modify which platform(s) a switch activates, where the platform travels to and from, and the platforms scale — all from the viewport. With these settings readily available from the viewport, you can design and test your level without continuously needing to edit the Blueprints.

Next, you’ll populate the switch’s array that you created in [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine).

### Populate the Interact Object List

You can populate the switch’s Interact Object List array with any object in your level that you want the switch to activate, so long as it has logic to power it. In this case, you’ll select the instance of `BP_Platform` in your level.

To populate the array, follow these steps:

1. Select your platform in the viewport. In the **Details** panels, set **Active** to false (unchecked). This will stop it from activating at runtime and wait for the switch’s signal.
2. Select your switch in the viewport. In the **Details** panel, under **Setup**, next to **Interact Object List**, click the **Add Element (+)** button to create a new index in the array.
3. In the dropdown, search for `BP_Platform` or use the eyedropper tool to select it in the viewport.

   [![Create-a-new-index-to-interact-with](https://dev.epicgames.com/community/api/documentation/image/e087d5c4-8c64-407b-8306-594b6fc51608?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e087d5c4-8c64-407b-8306-594b6fc51608?resizing_type=fit)

Enter PIE mode to test out your final gameplay object. When you, or a physics cube, overlap the switch, the platform should move back and forth (and stop when you or the cube moves away).

![Image-of-platform-leaving-without-player](https://dev.epicgames.com/community/api/documentation/image/2a06cfbc-2e60-46f9-b36e-9f31a52f7997?resizing_type=fit)

Try enabling `ActivateOnce` on the `BP_Switch`. You’ll notice that because the switch stays active, the platform continues to move even if you step away from the switch.

Depending on where you’ve placed the target point in your level, you might notice a problem. If you place the physics cube on the platform and step on the switch, the platform moves so quickly that the cube falls off. Impractical physics can frustrate players and stop them from completing your puzzle.

![Image-of-cube-falling-off-the-platform](https://dev.epicgames.com/community/api/documentation/image/85a7dfd4-10c4-4a7b-8b3f-6c1cb739fc31?resizing_type=fit)

In the next section, you’ll debug this problem.

## Debugging

In this section, you’ll make adjustments and add additional functionality to your physics cube and platform to mitigate issues which might cause frustration for your players while solving your puzzle.

### Adjusting Damping

As you push the cube, you might notice that it feels very light and easy to push. This sensitivity to force can pose problems when players maneuver the cube through a puzzle or as it travels on a platform.

To increase the [damping](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-damping-in-unreal-engine) on the cube, follow these steps:

1. Open `BP_Cube` in the **Blueprint Editor** and select the **Cube** static mesh.
2. In the **Details** panel, under **Physics**, set the **Linear Damping** `0.7` and **Angular Damping** to `0.8`. This is a suggested amount and might vary depending on your project’s needs.
3. **Save** and **Compile**.

Test the cube again. If it’s still falling off the platform, move on to adjusting the platform's speed.

### Adjusting Velocity

Since the velocity of the platform affects the physics cube, slowing down the platform’s speed can help the cube stay onboard.

To adjust the platform’s speed, follow these steps.

1. In `BP_Platform`’s **EventGraph**, create a new variable named `TimeToTarget`.
2. Set its **pin** type to **Float**.
3. **Compile** your Blueprint.
4. In the **Details** panel, enable **Instance Editable**, add it to the **Setup** category, and set the **Default Value** to `2.0`. This is a suggested amount that will vary depending on your level.
5. Go to the group of nodes near the top of your graph that starts with **Event BeginPlay**.
6. Drag out from the **Exec** pin of the **Set End Location** node. Search for and create **Set Play Rate (Timeline)**.

   You may need to uncheck **Context Sensitive** to find this node.

   ![Create-a-set-play-rate-timeline](https://dev.epicgames.com/community/api/documentation/image/582c8b50-f213-4844-a1d0-486e30d4a4db?resizing_type=fit)
7. From the **Target** pin of the **Set Play Rate** node, search for and create a **Get TM Move Platform** node.

   [![Create-a-get-tm-move-platform-node](https://dev.epicgames.com/community/api/documentation/image/089fd9cd-7dcd-47ba-9e4e-7824ad7081db?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/089fd9cd-7dcd-47ba-9e4e-7824ad7081db?resizing_type=fit)
8. From the **New Rate** pin of **Set Play Rate**, drag out and create a **Divide** operator node. Set its **A** value to `1.0`.

   [![Create-a-divide-operator-node](https://dev.epicgames.com/community/api/documentation/image/cbb85907-0188-4b05-9dc0-efd459af1a44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cbb85907-0188-4b05-9dc0-efd459af1a44?resizing_type=fit)
9. From the **B** pin of the **Divide** node, drag out and create **Get TimeToTarget**.

   [![Create-a-get-time-to-target](https://dev.epicgames.com/community/api/documentation/image/df9f0aba-5f38-4f35-a673-ebfc869b1380?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df9f0aba-5f38-4f35-a673-ebfc869b1380?resizing_type=fit)
10. **Save** and **Compile**.

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(356 lines long)

Test your level in PIE mode and see how that changes the interaction between the platform and the cube. The cube should now stay on the platform when it moves.

Because you included the `TimeToTarget` variable in the Setup category, you can easily adjust the platform’s speed and test it from the viewport as you design your level.

![Gif-clip-of-cube-floating-away-with-platform](https://dev.epicgames.com/community/api/documentation/image/6dafb7ca-6765-4b7d-b8d4-b188483570ef?resizing_type=fit)

## Example Puzzle

We created a puzzle for Room 1 using the switch, cube, platform, and key assets described in this tutorial. If you’d like to copy our puzzle instead of creating your own, the sections below describe how to place assets exactly where we put them. Each section highlights an insight that we uncovered during playtesting that influenced our design choices.

To copy our puzzle, your Blueprints must be named as follows:

* BP\_Switch
* BP\_Cube
* BP\_Platform
* BP\_Key

If you haven't made your assets according to this tutorial, the snippet may not copy as expected.

### The Obstacles, Cubes, and Key

During playtesting, we discovered that players were struggling to control the physics cube’s movement. We added walls to guide the cube as the player pushes it around the room, and damping to reduce the cube’s reactivity. This mitigates frustration and avoids unfairly punishing the player for unusual physics behavior.

We also discovered that we needed a way to reset our puzzle if the player failed. Since players are likely to knock cubes off of platforms while they play, we populated key locations with more cubes to reduce the amount of backtracking needed to reset the puzzle and replace destroyed cubes.

![Room 1 Development Sequence](https://dev.epicgames.com/community/api/documentation/image/76fd615e-74de-413f-8b00-1071491d6de5?resizing_type=fit&width=1920&height=1080)![Room 1 Development Sequence](https://dev.epicgames.com/community/api/documentation/image/a6c50357-5dfd-41b7-9c4d-59253bb07c4b?resizing_type=fit&width=1920&height=1080)![Room 1 Development Sequence](https://dev.epicgames.com/community/api/documentation/image/51edccd6-cf28-4346-a1d2-f7ca94dd01df?resizing_type=fit&width=1920&height=1080)![Room 1 Development Sequence](https://dev.epicgames.com/community/api/documentation/image/a849011d-4346-4b51-99b0-c52835a8b91c?resizing_type=fit&width=1920&height=1080)

**Room 1 Development Sequence**

To copy the obstacles into your level follow these steps:

1. Copy the snippet below by clicking **Copy Full Snippet**.

   Command Line

   Command Line Snippet

   ```
   Begin Map
      Begin Level
         Begin Actor Class=/Script/Engine.StaticMeshActor Name=StaticMeshActor_32 Archetype="/Script/Engine.StaticMeshActor'/Script/Engine.Default__StaticMeshActor'" ExportPath="/Script/Engine.StaticMeshActor'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.StaticMeshActor_32'"
            Begin Object Class=/Script/Engine.StaticMeshComponent Name="StaticMeshComponent0" Archetype="/Script/Engine.StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.StaticMeshActor_32.StaticMeshComponent0'"
            End Object
            Begin Object Name="StaticMeshComponent0" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.StaticMeshActor_32.StaticMeshComponent0'"
               StaticMesh="/Script/Engine.StaticMesh'/Game/LevelPrototyping/Meshes/SM_Cube.SM_Cube'"
               StaticMeshImportVersion=1
               StaticMeshDerivedDataKey="STATICMESH_FD1BFC73B5510AD60DFC65F62C1E933E_228332BAE0224DD294E232B87D83948FQuadricMeshReduction_V2$2e1_6D3AF6A2$2d5FD0$2d469B$2dB0D8$2dB6D9979EE5D2_CONSTRAINED0_100100000000000000000000000100000000000080FFFFFFFFFFFFFFFFFFFFFFFF000000000000803F00000000000000803F0000803F00000000000000003D19FC1626C9B248DECA64C7201D34D790CF7B09D3C0873700000000010000000100000000000000010000000100000000000000000000000100000001000000400000000000000001000000000000000000F03F000000000000F03F000000000000F03F0000803F00000000050000004E6F6E65000C00000030000000803FFFFFFFFF0000803FFFFFFFFF0000000000000041000000000000A0420303030000000000000000_RT00_0"
               RelativeLocation=(X=-5940.000136,Y=1669.999995,Z=-400.499900)
   ```

   Expand code  Copy full snippet(573 lines long)
2. In the Unreal Editor, click **Edit > Paste** or **Ctrl + V** in the viewport.

### The Platforms

In the same way that adding more physics cubes acted as a puzzle reset, we added a platform that lifts the player back up to the room’s starting position. By using the **Active** variable, this reset platform activates at runtime.

To copy the obstacles into your level follow these steps:

1. Copy the snippet below by clicking **Copy Full Snippet**.

   Command Line

   Command Line Snippet

   ```
   Begin Map
      Begin Level
         Begin Actor Class=/Game/AdventureGame/Designer/Blueprints/Platforms/BP_Platform.BP_Platform_C Name=BP_MovingPlatform_C_16 Archetype="/Game/AdventureGame/Designer/Blueprints/Platforms/BP_Platform.BP_Platform_C'/Game/AdventureGame/Designer/Blueprints/Platforms/BP_Platform.Default__BP_Platform_C'" ExportPath="/Game/AdventureGame/Designer/Blueprints/Platforms/BP_Platform.BP_Platform_C'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_MovingPlatform_C_16'"
            Begin Object Class=/Script/Engine.SceneComponent Name="DefaultSceneRoot" Archetype="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Blueprints/Platforms/BP_Platform.BP_Platform_C:DefaultSceneRoot_GEN_VARIABLE'" ExportPath="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_MovingPlatform_C_16.DefaultSceneRoot'"
            End Object
            Begin Object Class=/Script/Engine.StaticMeshComponent Name="Platform" Archetype="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Blueprints/Platforms/BP_Platform.BP_Platform_C:Platform_GEN_VARIABLE'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_MovingPlatform_C_16.Platform'"
            End Object
            Begin Object Class=/Script/Engine.TimelineComponent Name="TM_MovePlatform" ExportPath="/Script/Engine.TimelineComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_MovingPlatform_C_16.TM_MovePlatform'"
            End Object
            Begin Object Name="DefaultSceneRoot" ExportPath="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_MovingPlatform_C_16.DefaultSceneRoot'"
   ```

   Expand code  Copy full snippet(280 lines long)
2. In the Unreal Editor, click **Edit > Paste** or **Ctrl + V** in the viewport.
3. Connect the platforms to the corresponding target point:

   * `BP_Platform1` references **TargetPoint1**
   * `BP_Platform2` references **TargetPoint2**
   * `BP_Platform3` references **TargetPoint3**
   * `BP_Platform4` references **TargetPoint4**
   * `BP_Platform5` references **TargetPoint5**

### The Switches

We used the InteractObjectList array to connect some switches to multiple platforms. This way, we kept the puzzle concise and challenging, avoiding extra steps that might bore or frustrate the player.

To copy the obstacles into your level follow these steps:

1. Copy the snippet below by clicking **Copy Full Snippet**.

   Command Line

   Command Line Snippet

   ```
   Begin Map
      Begin Level
         Begin Actor Class=/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.BP_Switch_C Name=BP_ActivationPlate_C_9 Archetype="/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.BP_Switch_C'/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.Default__BP_Switch_C'" ExportPath="/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.BP_Switch_C'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_ActivationPlate_C_9'"
            Begin Object Class=/Script/Engine.SceneComponent Name="DefaultSceneRoot" Archetype="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.BP_Switch_C:DefaultSceneRoot_GEN_VARIABLE'" ExportPath="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_ActivationPlate_C_9.DefaultSceneRoot'"
            End Object
            Begin Object Class=/Script/Engine.StaticMeshComponent Name="Switch" Archetype="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.BP_Switch_C:Switch_GEN_VARIABLE'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_ActivationPlate_C_9.Switch'"
            End Object
            Begin Object Class=/Script/Engine.BoxComponent Name="Trigger" Archetype="/Script/Engine.BoxComponent'/Game/AdventureGame/Designer/Blueprints/Activation/BP_Switch.BP_Switch_C:Trigger_GEN_VARIABLE'" ExportPath="/Script/Engine.BoxComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_ActivationPlate_C_9.Trigger'"
            End Object
            Begin Object Name="DefaultSceneRoot" ExportPath="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_ActivationPlate_C_9.DefaultSceneRoot'"
   ```

   Expand code  Copy full snippet(115 lines long)
2. In the Unreal Editor, click **Edit > Paste** or **Ctrl + V** in the viewport.
3. Connect each switch to the correct platform:

   * `BP_Switch1` references `BP_Platform1`.
   * `BP_Switch2` references `BP_Platform2` and `BP_Platform 3`.
   * `BP_Switch3` references `BP_Platform5`.

Now, test your level to make sure it’s working properly and see if you can beat the puzzle. You can check your work against the complete level we provide at the end of this tutorial series.

## Next Up

[Create a Trap and Apply Damage](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Create a Moving Platform](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#createamovingplatform)
* [Create a Material Instance](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#createamaterialinstance)
* [Set Up a Blueprint Class](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#setupablueprintclass)
* [Build with Logic](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#buildwithlogic)
* [Define Locations](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#definelocations)
* [Build Movement](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#buildmovement)
* [Create Forward Movement](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#createforwardmovement)
* [Create Backward Movement](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#createbackwardmovement)
* [Create a Delay](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#createadelay)
* [Connect the Switch to the Platform](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#connecttheswitchtotheplatform)
* [Populate the Interact Object List](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#populatetheinteractobjectlist)
* [Debugging](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#debugging)
* [Adjusting Damping](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#adjustingdamping)
* [Adjusting Velocity](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#adjustingvelocity)
* [Example Puzzle](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#examplepuzzle)
* [The Obstacles, Cubes, and Key](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#theobstacles,cubes,andkey)
* [The Platforms](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#theplatforms)
* [The Switches](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#theswitches)
* [Next Up](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Traps and Damage

![Traps and Damage](https://dev.epicgames.com/community/api/documentation/image/87f77dd2-9774-4a28-9a73-a178e0642500?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine)
