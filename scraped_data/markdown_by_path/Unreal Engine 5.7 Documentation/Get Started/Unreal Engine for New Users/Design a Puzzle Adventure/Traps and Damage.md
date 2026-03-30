<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7 -->

# Traps and Damage

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
8. Traps and Damage

# Traps and Damage

Learn to build environmental blueprints that damage the player and build a game-over loop that triggers when the player is eliminated.

![Traps and Damage](https://dev.epicgames.com/community/api/documentation/image/c466ed11-8959-4b85-baf0-d892ca6311a0?resizing_type=fill&width=1920&height=335)

 On this page

Environmental hazards play a big role in shaping gameplay. By using hazards and traps, you add consequences for the player and escalate the difficulty and tension as they progress through a puzzle or level.

In this part of the tutorial series, you’ll create a spike trap and a fire trap that can damage the player. Then you’ll connect your fire trap and switch gameplay objects to create a new gameplay mechanic and puzzle.

Now that the player can take damage and lose all their health, you’ll also set up a fail condition that ends and restarts the game, giving players the chance to try again.

[![](https://dev.epicgames.com/community/api/documentation/image/b2f0d9e4-feff-4246-985f-750d7c09c7de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2f0d9e4-feff-4246-985f-750d7c09c7de?resizing_type=fit)

## Before You Begin

Make sure you understand these topics covered in previous sections of [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

* Blueprint basics like variables, functions, event graphs, and adding nodes.
* Using blueprint interface events to make a switch toggle another gameplay object.

You’ll need the following assets from [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine) and [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine):

* `M_BasicColor` Material and `M_BasicColor_Red` Material Instance
* `BPI_Interaction` Blueprint Interface
* `BP_Switch` Blueprint Class

## Build a Set of Related Blueprint Classes

Throughout this tutorial series, you’ve encountered Unreal Engine assets that use parent-child relationships and inheritance. **Inheritance** means creating a new child class that reuses and extends the features of an existing parent class. The child class can expand upon those features without altering the parent. Inheritance saves you time by reusing useful features across many assets instead of manually adding them to each new asset.

Your Material Instance assets inherit features from their parent Materials. In many of your blueprints, you created components that inherit transform data from a parent component.

Games use different types of hazards, but they often share the same core features. A parent trap blueprint can define those shared features, while each child trap blueprint extends those features, adding different visuals and behaviors.

Your base (parent) trap needs to detect player overlap and use the damage game mechanic to decrease player health over time. Then, you’ll create (or subclass) child traps to extend the base trap’s features and add additional visuals or behaviors. The spike trap adds additional static meshes to its appearance, and the fire trap adds a fire effect and behavior that makes it toggle on and off.

[![](https://dev.epicgames.com/community/api/documentation/image/655b2a76-d10c-471c-a1b3-02177bed7839?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/655b2a76-d10c-471c-a1b3-02177bed7839?resizing_type=fit)

Your level is still in the blockout stage, so focus on creating a simplified version of each trap that still informs the future visual design.

## Create the Base Trap Blueprint

First, create the base trap blueprint class as a parent of and foundation for your specialized traps.

To create a blueprint that defines common trap features, follow these steps:

1. In the **Content Browser**, go to the **Content > AdventureGame > Designer > Blueprints** folder, and create a new folder named `Traps`.
2. In the **Traps** folder, right-click or click **Add**, and create a new **Blueprint Class**.
3. In the `Pick Parent Class` window, click **Actor**.
4. Name this class `BP_TrapBase` and open it.

### Add Components

For the base trap, you’ll create a blockout-style static mesh to show the trap’s boundaries. All traps also need a collision volume to know when the player steps on them.

To create the physical components of the base trap, follow these steps:

1. In the **Components** tab, click **Add**, and search for and add a **Cube** static mesh shape.
2. Name the mesh component `TrapBase`.
3. In the **Details** panel under **Transform**, change the cube’s **Scale** to `2`, `2`, `0.1` to create a flat square base.

   [![](https://dev.epicgames.com/community/api/documentation/image/34632d9d-12cd-4dfb-b755-59ca68dc7224?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34632d9d-12cd-4dfb-b755-59ca68dc7224?resizing_type=fit)
4. In the **Components** tab, with **TrapBase** selected, click **Add**, and search for and select a **Box Collision** component.
5. Name the collision component `TrapTrigger`. This is the collision volume you’ll use to detect when the player is standing on the trap.

   Just like with `BP_Switch`, you’re attaching the collision component to the mesh, so if you want to change the size of the trap, the trigger area automatically adjusts.
6. In the **Details** panel under **Transform**, change the following properties to create a large collision box above the base mesh:

   1. Set **Location** to `0`, `0`, `400`.
   2. Set **Scale** to `1.5`, `1.5`, `12`.

   [![](https://dev.epicgames.com/community/api/documentation/image/42e71bbc-8a46-49b4-ab6f-28d253a8ed5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/42e71bbc-8a46-49b4-ab6f-28d253a8ed5e?resizing_type=fit)

### Add Variables

All traps also need editable properties that let you customize:

* If the hazard is active or inactive.
* The damage the trap does to the player.
* The damage interval, or time between hits.

And, the trap needs to know who collided with it.

To add common properties to the base trap, follow these steps:

1. In the **My Blueprint** tab, create the following variables:

   |  |  |  |  |
   | --- | --- | --- | --- |
   | **Variable Name** | **Type** | **Category** | **Default Value** |
   | Active | Boolean | Setup | True |
   | BaseDamage | Float | Setup | 5.0 |
   | DamageInterval | Float | Setup | 1.0 |

   After creating a variable, compile your blueprint to add a default value.
2. Click each variable’s eye icon so the eye is open, making all three variables editable and public.
3. Add a variable named `OtherActor` and change the type to **Actor (Object Reference)**.

   [![](https://dev.epicgames.com/community/api/documentation/image/2211002c-fab7-4a21-aea5-517c17718fa5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2211002c-fab7-4a21-aea5-517c17718fa5?resizing_type=fit)

### Create a Function to Apply Damage

Now that your trap has its base properties, you can start creating the trap’s behavior. All traps should lower the player’s hit points (HP) at a regular interval when the player overlaps the collision volume.

Unreal Engine has built-in solutions for many common gameplay mechanics, including applying and receiving damage.

For the trap, you’ll use the built-in **Apply Damage** function node. To organize the damage-handling logic, you’ll create your own function that calls **Apply Damage** on all characters touching the trap if the trap is active.

To create a function that applies trap damage to the player, follow these steps:

1. In the **Functions** section, click **Add**. Name this function `fnApplyDamageToTargets` and open its graph.
2. You only want to apply damage if the trap is turned on and active, so add a **Branch** node where the **Condition** is a reference (Get) to the **Active** variable.

   [![](https://dev.epicgames.com/community/api/documentation/image/6b3eb762-30d4-4003-903a-a00bc1f37524?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6b3eb762-30d4-4003-903a-a00bc1f37524?resizing_type=fit)
3. Later in this tutorial, you’ll add some NPC enemies, so it’s possible that many actors could be on the trap at once. So, when the trap is active, loop through an array of all actors touching the trap:

   1. Connect the **Branch** node’s **True** pin to a **For Each Loop** node.
   2. For the loop’s **Array** input, you need to create an array of all overlapping actors. Unreal Engine does this for you — add a **Get Overlapping Actors (TrapTrigger)** node. The node comes with a reference to **TrapTrigger** as its **Target**.
   3. In the **Get Overlapping Actors** node, change the **Class Filter** to **Character** so player and NPC characters can be added to the array.

      [![](https://dev.epicgames.com/community/api/documentation/image/bdb38b7d-2cd7-42c3-b264-f5160c27ab9d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bdb38b7d-2cd7-42c3-b264-f5160c27ab9d?resizing_type=fit)
4. For each array element, or each iteration of the loop, apply the amount of damage set in the **BaseDamage** variable to the actor in that array element. To do this, connect an **Apply Damage** node to the **Loop Body**.

   [![](https://dev.epicgames.com/community/api/documentation/image/0210b9ae-f9a7-4b42-b3e1-6bbe231964d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0210b9ae-f9a7-4b42-b3e1-6bbe231964d8?resizing_type=fit)

   The **Apply Damage** function comes from the Unreal Engine Game Statics library. The icon in the top-right corner means the function can be used in networked games and can run on the server.
5. Set up the **Apply Damage** node:

   1. For the **Damaged Actor** pin, connect the loop’s **Array Element**.
   2. For the **Base Damage** pin, connect a reference to the **BaseDamage** variable.

   [![](https://dev.epicgames.com/community/api/documentation/image/63b18bcf-298e-48fe-854d-f0d0172f7860?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/63b18bcf-298e-48fe-854d-f0d0172f7860?resizing_type=fit)

6. **Save** and **Compile** your blueprint.

Your complete **fnApplyDamageToTarget** function should look like the following:

Blueprint

Copy full snippet(99 lines long)

If you copy and paste this snippet into the corresponding graph in your project, connect the function entry node to the **Branch** node.

### Create a Timer That Applies Damage Over Time

Next, you need to make the trap call the apply-damage function at regular time intervals. To do this, you’ll use one of Unreal Engine’s timer functions to create a timer.

In this blueprint, you’ll use **Set Timer by Function Name**:

[![](https://dev.epicgames.com/community/api/documentation/image/b2cb6ab4-092c-4171-8a93-728ffa75261a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2cb6ab4-092c-4171-8a93-728ffa75261a?resizing_type=fit)

This node creates a timer and binds a function to that timer so that when the timer expires, the node calls the function, executing all the actions in that function.

To set up a timer when the game starts, follow these steps:

1. Go to `BP_TrapBase`’s **EventGraph** tab. Delete the provided **Event ActorBeginOverlap** and **Event Tick** nodes.
2. Before the trap performs any actions, you want to check if it’s active. From the **Event BeginPlay** node, add a **Branch** node where the **Condition** is a reference to the **Active** variable.
3. From the **Branch** node’s **True** pin, create a **Set Timer by Function Name** node.
4. Set up the timer node:

   1. For the **Time** pin, connect a reference to the **DamageInterval** variable.

      [![](https://dev.epicgames.com/community/api/documentation/image/c38f7aa1-6cdc-47d8-b6d4-2c9f72d294e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c38f7aa1-6cdc-47d8-b6d4-2c9f72d294e6?resizing_type=fit)
   2. Click the text box next to **Function Name**, and enter `fnApplyDamageToTarget`.

      Ensure you’ve spelled the function name correctly or the logic won’t execute properly.
   3. Enable **Looping**.
5. **Set Timer** nodes output a return value called a **Timer Handle** that acts like a tracking number or controller for the timer. To stop, pause, or resume the timer, you’ll reference this timer handle, so save it in a new variable:

   1. In the **My Blueprint** panel, create a new variable named `TimerHandler`. Change its type to **Timer Handle**.
   2. Add a **Set Timer Handler** node and connect it to **Set Timer by Event**’s return value and exec pins.

      [![](https://dev.epicgames.com/community/api/documentation/image/bfe7601b-961a-43bd-bd27-a280bf15d1b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bfe7601b-961a-43bd-bd27-a280bf15d1b5?resizing_type=fit)
6. When Unreal Engine creates a timer, it starts running immediately, so you need to pause the timer until a character steps on the trap. Connect a **Pause Timer by Handle** node and give it your **TimerHandler**.

   [![](https://dev.epicgames.com/community/api/documentation/image/64eab345-d930-40a4-9dfc-8865f8653b25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64eab345-d930-40a4-9dfc-8865f8653b25?resizing_type=fit)
7. **Save** and **Compile** your blueprint.

You can also create timers with a **Set Timer by Event** node. Here, you’d use the node actions list to **Add Custom Event** and use it as a **delegate** to bind actions to the timer.

Custom events are reusable, named blocks of logic similar to functions. Unlike functions, they can contain delays, timeline nodes, and other latent actions — so you may need to use this method as your game grows in complexity.

Connect an event’s square delegate pin to pass a reference of that event to the timer node. This isn’t triggering the event, but instead storing the event and its actions for later (when the time interval expires).

[![](https://dev.epicgames.com/community/api/documentation/image/16abb90a-44a6-42cf-a357-7d1d87f7cdbd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16abb90a-44a6-42cf-a357-7d1d87f7cdbd?resizing_type=fit)

### Start and Stop Damage

You’ve created and paused the damage timer so it’s ready and waiting. Now, make the damage resume when a character steps on the trap’s collision volume, and pause the damage when characters stop overlapping the volume.

To add logic that starts the damage, follow these steps:

1. In the **Components** panel, right-click the **TrapTrigger** component, go to **Add Event**, and select **Add OnComponentBeginOverlap**.
2. After the event, connect a **Set Other Actor** node to save the overlapping actor in the variable.
3. Connect the event and **Set** node’s **Other Actor** pins.
4. Connect an **fnApplyDamageToTarget** node so the character receives damage immediately when touching the trap.

   [![](https://dev.epicgames.com/community/api/documentation/image/f3557f9e-b114-4f6c-8832-fbabbe63500e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3557f9e-b114-4f6c-8832-fbabbe63500e?resizing_type=fit)
5. Connect an **Unpause Timer by Handle** node to resume the timer and damage intervals. For its **Handle input**, connect a reference to the **TimerHandler** variable.

   [![](https://dev.epicgames.com/community/api/documentation/image/38e38d8b-46bc-40a7-a89e-38305fc1687c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38e38d8b-46bc-40a7-a89e-38305fc1687c?resizing_type=fit)

To add logic that stops the damage over time, follow these steps:

1. Right-click the **TrapTrigger** component, go to **Add Event > On Component End Overlap**.
2. After the event, connect a **Pause Timer by Handle** node, again giving it a reference to **TimerHandler**.

   [![](https://dev.epicgames.com/community/api/documentation/image/f0c1ac90-d796-4ae0-9bba-6be0e06a5dd5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0c1ac90-d796-4ae0-9bba-6be0e06a5dd5?resizing_type=fit)
3. **Save** and **Compile** your blueprint.

The trap now creates, starts, and pauses a damage timer.

The finished `BP_TrapBase` event graph should look like the following:

Blueprint

Copy full snippet(240 lines long)

For more information about timers and timer management, see [Gameplay Timers](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-timers-in-unreal-engine).

### Test the Base Trap

To test the trap, add a Print String message that reports on-screen when the trap applies damage.

To print a message on screen that shows the trap is working as intended, follow these steps:

1. In `BP_TrapBase`, go to the **fnApplyDamageToTarget** tab.
2. In the function’s graph, connect a **Print String** node after the **Apply Damage** node.
3. Change the **In String** to `Player hit!`
4. Click the arrow at the bottom of the **Print String** node to show more options, and change the **Duration** to `5`. This makes it easier to see the damage hits over time.

   [![](https://dev.epicgames.com/community/api/documentation/image/08ef9ba0-ad60-4482-861e-3432b3146b4a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08ef9ba0-ad60-4482-861e-3432b3146b4a?resizing_type=fit)
5. **Compile** and **Save** the blueprint. In the **Content Browser**, drag an instance of `BP_TrapBase` into your level.
6. Play the level and step on the trap. A new “Player hit!” message should appear every second.

   [![](https://dev.epicgames.com/community/api/documentation/image/1026e7ed-fd30-47da-b96d-7956bde57369?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1026e7ed-fd30-47da-b96d-7956bde57369?resizing_type=fit)

## Subclass a Spike Trap

Now that you’ve completed your parent class, it’s time to start subclassing!

First, you’ll create a spike trap that modifies the base trap’s appearance, adding some shape language. A plain flat trap doesn’t look dangerous, but the player will interpret a spikey object as something that could hurt them.

To create a spike trap, follow these steps:

1. In the **Content Browser**, in the **Traps** folder, right-click `BP_TrapBase` and select **Create Child Blueprint Class**.
2. Name the blueprint class `BP_TrapSpikes` and open it.
3. In the **Components** tab, with **DefaultSceneRoot** selected, click **Add**, and search for and select **Cone**.

   You’ll resize and position the cones to fit four rows of four cones each (or 16 in total).
4. In the cone’s **Details** panel, in the **Transform** section, change the following properties:

   1. Change the **Location** to `-75`, `-75`, `25`.
   2. Change the **Scale** to `0.5`, `0.5`, `0.4`.

   Now there’s a smaller spike in the corner of the base mesh.

   [![](https://dev.epicgames.com/community/api/documentation/image/59cfee39-cb17-4e53-b8d6-5d94991644d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/59cfee39-cb17-4e53-b8d6-5d94991644d8?resizing_type=fit)
5. For some visual contrast, in the **Materials** section, use the dropdown menu to change the cone’s material to `M_BasicColor_Red`.
6. Select and duplicate (**Ctrl + D**) the cone three times, translating each cone over by 50 units so they line up in a row across one side of the base mesh.

   [![](https://dev.epicgames.com/community/api/documentation/image/0ae0490b-dea7-4a6d-81b8-5654220b2194?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ae0490b-dea7-4a6d-81b8-5654220b2194?resizing_type=fit)

   You can reposition cones in the Details panel or in the Viewport. For faster adjustments with the gizmo, change your translate snap settings to 50 units.

   [![](https://dev.epicgames.com/community/api/documentation/image/2ec8efb9-6244-4877-a64b-4aea20c8a383?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ec8efb9-6244-4877-a64b-4aea20c8a383?resizing_type=fit)
7. Hold **Ctrl** to select all four cones and duplicate them. In the **Components** panel, select the four new cones (they’ll have the largest number suffixes), and move them over 50 units. Repeat this two more times to create a 4x4 grid of cones.

   [![](https://dev.epicgames.com/community/api/documentation/image/a68c3ebd-ff1d-41fa-b1fa-028e5067c12e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a68c3ebd-ff1d-41fa-b1fa-028e5067c12e?resizing_type=fit)
8. The slopes and angles in the spikes could make it awkward for the player to move off the trap. To prevent the player from landing between the spikes, add an invisible floor at the top of the spikes:

   1. In the **Components** tab, duplicate the **TrapBase** mesh and name it `InvisFloor`.
   2. Move the floor up so only the tips of the spikes are visible above the floor.

      [![](https://dev.epicgames.com/community/api/documentation/image/2f413ce4-6ad8-4c16-a1f9-975b6873b3f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f413ce4-6ad8-4c16-a1f9-975b6873b3f3?resizing_type=fit)
   3. In the **Details** panel, in the **Collision** section, ensure **Collision Presets** is set to **BlockAllDynamic**. This blocks all actors from passing through the mesh.
   4. In the **Rendering** section, disable **Visible**. This hides the mesh in the viewports and during gameplay.

      [![](https://dev.epicgames.com/community/api/documentation/image/ed3d872a-7b6e-46b0-9d99-4c40d761ceb8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed3d872a-7b6e-46b0-9d99-4c40d761ceb8?resizing_type=fit)
9. In the **Components** tab, select the **TrapBase** mesh. In the **Details** panel, in the **Rendering** section, enable **Hidden in Game**. This keeps the mesh visible in viewports, but hides it during gameplay, so you’ll only see the spikes.
10. **Save** and **Compile** your blueprint.

The spike trap subclass has all the behavior of your base trap, so it also prints the “Player hit!” messages when the trap is working. Drag an instance of `BP_TrapSpikes` into your level and test it out!

[![](https://dev.epicgames.com/community/api/documentation/image/498f1c9c-d807-4248-b01c-92a06f9b79dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/498f1c9c-d807-4248-b01c-92a06f9b79dd?resizing_type=fit)

## Subclass a Fire Trap

Next, you’ll create a trap that extends the base trap’s behavior. A fire trap adds a hazard that the player can turn off with a switch, which is a gameplay mechanic you can turn into a new puzzle.

In [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine), you created the `BPI_Interaction` blueprint interface that a switch can use to turn other gameplay objects on and off. You can also use this interface in a trap blueprint so a switch can change the trap’s Active variable during gameplay.

First, you’ll need a new material to use when the trap is deactivated.

To create a black material for the fire trap, follow these steps:

1. In the **Content Browser**, go to the **AdventureGame > Designer > Materials** folder.
2. Right-click `M_BasicColor` and select **Create Material Instance**.
3. Name the material instance `M_BasicColor_Black` and open it.
4. Expand **Global Vector Parameter Values**, enable **Color**, and click the color swatch to change it to dark grey (Hex sRGB = `3D3B3BFF`). This looks better in-game than pure black.

   [![](https://dev.epicgames.com/community/api/documentation/image/13244046-f126-4793-9701-b0be246bad98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13244046-f126-4793-9701-b0be246bad98?resizing_type=fit)
5. Save and close the material instance.

To subclass a fire trap, follow these steps:

1. In the **Content Browser**, right-click `BP_TrapBase` and select **Create Child Blueprint Class**.
2. Name the blueprint `BP_TrapFire` and open it.

   [![](https://dev.epicgames.com/community/api/documentation/image/6977859b-5643-464a-810d-19feb890c3ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6977859b-5643-464a-810d-19feb890c3ee?resizing_type=fit)
3. Change the base mesh's color to make it represent a fire trap. Select the **TrapBase** component and, in the **Details** panel, in the **Materials** section, change the material to `M_BasicColor_Red`.

   [![](https://dev.epicgames.com/community/api/documentation/image/abc815d7-0551-4811-94e2-e3366cdb982b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abc815d7-0551-4811-94e2-e3366cdb982b?resizing_type=fit)
4. Above the viewport, click **Class Settings**.
5. In the **Details** panel, in the **Interfaces** section, next to **Implemented Interfaces**, click **Add**, and search for and select `BPI_Interaction`.

   [![](https://dev.epicgames.com/community/api/documentation/image/5c547234-4a1b-40ea-9477-1805db4860b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c547234-4a1b-40ea-9477-1805db4860b6?resizing_type=fit)

   In the **My Blueprint** panel, the **fnBPISwitchOff** and **fnBPISwitchOn** event functions appear in the Interfaces section.
6. Just like with `BP_Switch`, set up customizable materials for the fire trap:

   1. In the **Variables** section of the **My Blueprint** panel, create two variables named `OffMaterial` and `OnMaterial`.
   2. Change their type to **Material Interface (Object Reference)**.
   3. Click their eye icons to make them public and editable.
   4. Change their **Category** to **Setup**.

      [![](https://dev.epicgames.com/community/api/documentation/image/2d232297-bf6c-43e0-bc78-1cd13e7ddbb5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d232297-bf6c-43e0-bc78-1cd13e7ddbb5?resizing_type=fit)
   5. Compile and set the following default values:

      * **OffMaterial**: `M_BaseColor_Black`
      * **OnMaterial**: `M_BaseColor_Red`
7. **Save** and **Compile** the blueprint so you can use the interface events in the trap’s event graph.

### Extend the Trap's Behavior

Just like when you made the moving platform in [Puzzles: Moving Platforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine), you need to set up the trap’s event graph to take the following actions when a switch calls **fnBPISwitchOn** and **fnBPISwitchOff**:

* Activate or deactivate the trap.
* Change the trap’s material.

With the moving platform, you needed the platform to start moving when the player activates the switch. For the trap, you need the opposite — the trap is active when the level starts and should turn off when the player activates the switch.

To add logic that deactivates fire traps when the player presses a switch, follow these steps:

1. Go to the fire trap’s **EventGraph** tab. In the **My Blueprint** panel, in the **Interfaces** list, double-click **fnBPIButtonOn** to add an event node to the graph.
2. `BP_TrapBase` variables don’t appear in the **My Blueprint** panel, but you can access them with the node actions list. Drag off the **Event fnBPISwitchOn** node’s **exec** pin, search for `active variable`, and select **Set Active**. Keep **Active** disabled.

   [![](https://dev.epicgames.com/community/api/documentation/image/08380077-7ae9-4c40-b83f-86e9ef49ebf9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08380077-7ae9-4c40-b83f-86e9ef49ebf9?resizing_type=fit)
3. After the **Set** node, connect a **Set Material (TrapBase)** node (in the **Rendering > Material** section of the actions list).
4. In the **Set Material** node, connect a reference to the **OffMaterial** variable to the **Material** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/cccd3ba0-2b10-458f-becb-44e0ca6d54c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cccd3ba0-2b10-458f-becb-44e0ca6d54c7?resizing_type=fit)

To add logic that activates fire traps if a switch is deactivated, follow these steps:

1. In the **Interfaces** section, double-click **Event fnBPISwitchOff** to add that node.
2. After the event, connect a **Set Active** variable node, but this time enable **Active**.
3. After the **Set** node, connect a **Set Material (TrapBase)** node and connect a reference to **OnMaterial**.

   [![](https://dev.epicgames.com/community/api/documentation/image/0e949289-d65e-462a-b784-c5f84340fbc1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e949289-d65e-462a-b784-c5f84340fbc1?resizing_type=fit)
4. **Save** and **Compile** your blueprint.

Your complete fire trap event graph should look like the following:

Blueprint

Copy full snippet(128 lines long)

Add an instance of `BP_TrapFire` to your level and give it a try!

[![](https://dev.epicgames.com/community/api/documentation/image/fc517873-d521-49d6-8ea3-62c629064aae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc517873-d521-49d6-8ea3-62c629064aae?resizing_type=fit)

## Update the HUD With Player HP

Time to replace those Print String nodes with some real feedback for the player. You’ll change your HUD to report the player’s HP in real time.

### Add an HP Variable to the HUD

To add dynamic player health to your HUD, follow these steps:

1. In the **Content Browser**, open your `WBP_PlayerHUD` widget blueprint. Ensure you’re in **Designer** view.
2. In the **Hierarchy**, click the **txtHP** widget. In the **Details** panel, enable **Is Variable** and delete **100** from the **Text** property.

   [![](https://dev.epicgames.com/community/api/documentation/image/fa52674d-bed9-4e88-bbaa-815a63396a5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa52674d-bed9-4e88-bbaa-815a63396a5a?resizing_type=fit)
3. Go to the **Graph** view and set up a new function that sets the value of **txtHP**:

   1. In the **Functions** section, add a new function named **fnSetHP**.
   2. With the function selected, in the **Details** panel, click **+** next to **Inputs**.
   3. Name the input `NewHP` and change its type to **Float**.

      Later, you’ll change the player character to call this function when they take damage.
4. In the **fnSetHP** function’s graph, after the function entry node, connect a **SetText (Text)** node.

   [![500](https://dev.epicgames.com/community/api/documentation/image/d6f1186f-1064-4d8c-bb0b-240177dd3db7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6f1186f-1064-4d8c-bb0b-240177dd3db7?resizing_type=fit)

   If you can’t find a node in the node actions list, disable **Context Sensitive**.
5. Set up the **SetText (Text)** node:

   1. For the **Target**, connect a reference to the **txtHP** variable. This is the text widget that displays the player’s health.
   2. For the **In Text**, connect the function entry node’s **New HP** input pin. Unreal Engine automatically adds a **To Text (Float)** node to convert the value.

      [![](https://dev.epicgames.com/community/api/documentation/image/130af771-daa0-409b-bc26-fe1609c4641d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/130af771-daa0-409b-bc26-fe1609c4641d?resizing_type=fit)
   3. **Save** and **Compile** the widget blueprint.

The complete **fnSetHP** function’s graph looks like the following:

Blueprint

Copy full snippet(45 lines long)

If you copy this blueprint snippet into your graph, you need to connect the function entry node to the **SetText** and **To Text** nodes.

### Display the Player’s Starting HP

Set up any available HUD variables before displaying them. In this case, you know the player’s starting HP, so you can display that information when the game starts.

To update the player character blueprint to display their HP on the HUD, follow these steps:

1. In the **Content Browser**, open your `BP_AdventureCharacter` blueprint. In the event graph, find the **Event Possessed** logic.

   [![](https://dev.epicgames.com/community/api/documentation/image/fa61628b-49c9-429c-a357-de4628b71ee5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa61628b-49c9-429c-a357-de4628b71ee5?resizing_type=fit)

   In the **My Blueprint** panel, expand **Graphs** > **EventGraph** and double-click **Event Possessed** to focus on it in the graph.
2. In between the **Set** node and **Add to Viewport** node, connect a **fnSetHP** node:

   1. For the **Target**, use the **Set** node’s output pin to make the HUD the target.
   2. For **New HP**, connect a reference to the player’s **Health** variable.

      [![](https://dev.epicgames.com/community/api/documentation/image/d83717ac-b767-4377-8872-10ca2d9c4ff0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d83717ac-b767-4377-8872-10ca2d9c4ff0?resizing_type=fit)
3. Ensure the **Add to Viewport** node’s **Target** pin also connects to a **HUD** variable node.
4. In the **My Blueprint** panel, click the **Health** variable. In the **Details** panel, change (or keep) the default value. This tutorial uses **100** starting hit points.
5. **Save** and **Compile**.

The player’s new **Event Possessed** logic should look like the following:

Blueprint

Copy full snippet(90 lines long)

If copying this logic into your project, first delete the existing **Event Possessed** logic group.

Now, the HUD displays the player’s health when the game starts. The last piece of logic you need is to update the HUD when the player is damaged. To do this, you’ll modify the character’s existing damage-handling logic to work with your HUD.

### Update the Player’s HP After Taking Damage

To handle damage to the player, follow these steps:

1. In the bottom-left corner of `BP_AdventureCharacter`’s event graph, find the section of logic labelled “**Damage and death handling**” that starts with an **Event AnyDamage** node. You’re going to modify this section to execute your own logic instead.

   [![](https://dev.epicgames.com/community/api/documentation/image/0d7d4b72-05bd-4a91-802e-704ff79be9b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d7d4b72-05bd-4a91-802e-704ff79be9b3?resizing_type=fit)
2. Delete all nodes that come after the **Branch** node. Keep the **Branch** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/ef5e17a6-b187-48f9-9b47-b161cbf65a1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef5e17a6-b187-48f9-9b47-b161cbf65a1e?resizing_type=fit)

   This section of logic uses **operator nodes** to perform calculations. When the character receives damage, the **Event AnyDamage** node triggers, passing information about the damage dealt, the type of damage, and the controller and actor that instigated the damage. Next, the damage is subtracted from the character’s **Health** variable. Once the health is subtracted, the **Branch** node checks if the player’s health has reached 0.
3. For now, you want to build logic that updates the HUD when the player’s health is greater than 0. So, from the **False** pin, connect an **FnSetHP** node to send the new health value to the HUD.
4. Set up the **fnSetHP** node:

   1. For the **Target**, connect a reference to the character’s **HUD** variable.
   2. For the **New HP** input, connect a reference to the **Health** variable.

      [![](https://dev.epicgames.com/community/api/documentation/image/12ab9792-6787-4b1a-909c-a4225ddedb7f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12ab9792-6787-4b1a-909c-a4225ddedb7f?resizing_type=fit)
5. **Save** and **Compile** your blueprint.

Now the HUD displays the player’s current health and updates that health value when the player takes damage.

Go back to your `BP_TrapBase` blueprint and delete any **Print String** nodes you added to the base trap’s event graph.

Play your game again and test it out!

[![](https://dev.epicgames.com/community/api/documentation/image/cd89341a-fb9a-4066-83df-d7b110330714?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd89341a-fb9a-4066-83df-d7b110330714?resizing_type=fit)

## Create a Fail and Respawn Condition

When the player runs out of health and is eliminated, you’ll want to stop the game and give them a chance to try again. In this tutorial, you’ll disable the player’s controls, communicate to the player that they’ve lost the game, and load the level.

First, you’ll create a game-over widget blueprint that tells the player they have been eliminated.

### Add a Game-Over Screen

To create a widget blueprint for your game-over screen, follow these steps:

1. In the **Content Browser**, in the **AdventureGame > Designer > Blueprints > Widgets** folder, right-click, go to **User Interface**, and select **Widget Blueprint**.
2. In the **Pick Parent Class** window, click **User Widget**.
3. Name the widget blueprint `WBP_EliminatedScreen` and open it.

To set up the game-over UI, follow these steps:

1. In the **Palette** tab, search for canvas and drag a **Canvas Panel** onto **[WBP\_EliminatedScreen]** in the **Hierarchy**. Just like with your HUD, the canvas is your root widget.
2. The canvas will have a game-over message layered over a blur effect that makes the text easier to read. From the **Palette** tab, drag an **Overlay** to become a child of the canvas.
3. With the overlay selected, in the **Details** panel, in the Slot (Canvas Panel Slot) section, expand **Anchors**, and change both **Maximum** values (**X** and **Y**) to `1`.

   The other Slot properties (below **Anchors**) change to **Offset** settings.

   [![](https://dev.epicgames.com/community/api/documentation/image/1ef23e2c-4ec5-4e84-b79f-58dea1e51037?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ef23e2c-4ec5-4e84-b79f-58dea1e51037?resizing_type=fit)

   When you built the HUD, you kept all anchor points in one corner so if the screen size changed, those objects stay anchored to the anchor point. Now, the overlay is anchored to the entire canvas bounding box, so the overlay shrinks or stretches to match the screen size.
4. When you changed the anchor settings, the editor changed some offset values to maintain the overlay panel’s default shape. To remove this, change **Offset Right** and **Offset Bottom** to `0`. Now the overlay fills the screen.

   [![](https://dev.epicgames.com/community/api/documentation/image/4d3bb252-9963-4f70-abe8-6fd5e20f302b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d3bb252-9963-4f70-abe8-6fd5e20f302b?resizing_type=fit)
5. From the **Palette** tab, drag a **Background Blur** widget to become a child of the **Overlay** panel.
6. With the blur effect selected, in the **Details** panel, in the **Slot (Overlay Slot)** section, change:

   1. **Horizontal Alignment** to **Fill Horizontally**.
   2. **Vertical Alignment** to **Fill Vertically**.

      [![](https://dev.epicgames.com/community/api/documentation/image/3e589600-9716-4947-852b-980443badaa2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e589600-9716-4947-852b-980443badaa2?resizing_type=fit)
7. In the **Appearance** section, change **Blur** **Strength** to `5`.
8. From the **Palette** tab, add a **Text** widget as a child of the **Overlay**.
9. With the **Text** widget selected, in the **Details** panel, in the **Slot (Overlay Slot)** section, change:

   1. **Horizontal Alignment** to **Center Align Horizontally**.
   2. **Vertical Alignment** to **Center Align Vertically**.

      [![](https://dev.epicgames.com/community/api/documentation/image/1bae3c34-d4cf-417d-96f1-8480fc74cd34?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1bae3c34-d4cf-417d-96f1-8480fc74cd34?resizing_type=fit)
10. In the **Content** section, change the **Text** to `You are eliminated…restarting the level.`
11. In the **Appearance** section, make the text larger and easier to read by configuring the following properties:

    1. Click the color swatch next to **Color and Opacity**, and pick a color for your text. This tutorial uses pink (Color **Hex sRGB** = `FF4D7AFF`).
    2. Expand the **Font** header, and change **Size** to `60`.
    3. Expand **Font > Outline Settings**, and change **Outline** Size to `1`.

       [![](https://dev.epicgames.com/community/api/documentation/image/60eab9fb-9dc3-4d6e-812b-d03b97c4d8fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60eab9fb-9dc3-4d6e-812b-d03b97c4d8fc?resizing_type=fit)

12. **Save** and **Compile** your blueprint.

### Build Logic for a Fail Condition

Now that you have a game-over screen, you can modify the character class to display it when the player runs out of HP. When this happens, execution passes through the True result of that Branch node you were working with earlier.

To handle player defeat, you’ll need to:

* Disable player input so the player can’t move.
* Show the game-over screen.
* Restart the level after a set amount of time.

To stop and load the game when the player is eliminated, follow these steps:

1. In `BP_AdventurePlayer`, go back to the damage-handling logic (beginning with **Event AnyDamage**) in your character blueprint.
2. After the **Branch** node’s **True** execution pin, connect a **Do Once** node and **Disable Input** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/7a90f6e3-d9a0-4908-ba92-6dc209d7bc97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a90f6e3-d9a0-4908-ba92-6dc209d7bc97?resizing_type=fit)

   The player can continue to get hit after they run out of health, so the Do Once node ensures that the logic after it only executes once.
3. For the **Disable Input** node’s **Player Controller** pin, connect a **Get Player Controller** node (in the **Game > Player** section of the node actions list).

   [![](https://dev.epicgames.com/community/api/documentation/image/2e004064-6504-4610-99cb-fd3af59ede93?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e004064-6504-4610-99cb-fd3af59ede93?resizing_type=fit)

   There are a few nodes named **Get Player Controller**. Ensure the node has a **Player Index** input pin. An index of **0** is the default index for the first player character spawned into the level.
4. After disabling the player controller, create and display the game-over screen:

   1. Connect a **Create Widget** node. In the node, change the **Class** to `WBP_EliminatedScreen`.

      [![](https://dev.epicgames.com/community/api/documentation/image/740de1b6-72f6-4d83-8c0b-657983a2a70f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/740de1b6-72f6-4d83-8c0b-657983a2a70f?resizing_type=fit)
   2. Connect the widget node’s **exec** and **Return Value** pins to an **Add to Viewport** node.

      [![](https://dev.epicgames.com/community/api/documentation/image/584426ef-5a6e-4434-ad3f-b8e08c970ed3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/584426ef-5a6e-4434-ad3f-b8e08c970ed3?resizing_type=fit)
5. Add a time delay, get the current level name, and then load that level:

   1. After the **Add to Viewport** node, connect a **Delay** node and change the **Duration** to `5` seconds.
   2. After the **Delay**, connect a **Get Current Level Name** node.
   3. After **Get Current Level Name**, connect an **Open Level (by Name)** node.
   4. Connect the **Return Value** pin to the **Level Name** pin. The editor automatically adds a string-to-name conversion node.

      [![](https://dev.epicgames.com/community/api/documentation/image/e58c3427-771e-46f9-a989-982ea834b5b1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e58c3427-771e-46f9-a989-982ea834b5b1?resizing_type=fit)
6. **Save** and **Compile** your player blueprint.

This section of the `BP_AdventureCharacter` event graph should now look like the following:

Blueprint

Copy full snippet(311 lines long)

If copying this logic into your project, delete the existing **Damage handling** group of nodes (including **Event AnyDamage** and **Event Destroyed** logic) first.

Play your level to test it out. Step on a trap, let your character lose all their HP, and make sure the game resets as intended.

[![](https://dev.epicgames.com/community/api/documentation/image/622821cf-d30e-4e3b-ba9e-3cba3e4bdfc2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/622821cf-d30e-4e3b-ba9e-3cba3e4bdfc2?resizing_type=fit)

## Add Hazards to Your Puzzles

In [Puzzles: Switches and Cubes](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine), you learned about designing gameplay mechanics that add difficulty, tension, consequences, and risk-reward decisions. Environmental hazards that damage the player are one mechanic that introduces these consequences. You can use the spike traps to add danger and additional consequences to earlier puzzles and obstacles in the level, and switch-powered fire traps can create more dynamic puzzles that make the player interact with the environment to reveal safe paths.

When designing games, a key part of reducing overhead and improving development speed is finding multiple different ways to use and combine gameplay objects. In a previous section of this tutorial series, the switch powered platforms to create a path forward. Here, the same switch can disable fire traps to reveal a path for the player. This adds variety to the level without needing an endless number of unique systems.

Similar to the door-and-key game mechanic you created earlier in this tutorial series, your fire trap becomes another mechanic to manage the player's pacing and access to the environment.

### Create a Maze Puzzle with Fire Traps

In Room 2, you’ll combine switches and fire traps to build a maze puzzle where the player must carefully disable hazards to discover and collect the last key.

It often helps to sketch puzzles on paper first. Since the traps are 1m x 1m, our sample Room 2 can fit a 7 x 9 grid of traps. Start by drawing a path through the grid that ends at the key. Then, divide the path up into segments and place switches to control each segment.

To add difficulty and create more reveals and surprises, add architectural features that block sightlines. For example, place switches behind walls or pillars so the player has to discover them along the path.

[![](https://dev.epicgames.com/community/api/documentation/image/f236de2e-303b-4a0e-90c0-bc6c9957f451?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f236de2e-303b-4a0e-90c0-bc6c9957f451?resizing_type=fit)

This looping path gives the player a glance at the key so they discover the goal while traversing the first segment of the path.

With your plan complete, start blocking out the puzzle in the level editor.

[![](https://dev.epicgames.com/community/api/documentation/image/f40a2da6-f907-47be-8c05-f480f01cc505?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f40a2da6-f907-47be-8c05-f480f01cc505?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/5831c041-c131-4708-b709-97434c47c862?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5831c041-c131-4708-b709-97434c47c862?resizing_type=fit)

Once you create the path to the key and new blockout shapes, fill in the rest of the room with fire traps to obscure the correct route.

[![](https://dev.epicgames.com/community/api/documentation/image/917147d7-532e-4928-b05d-c6f09d9a2001?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/917147d7-532e-4928-b05d-c6f09d9a2001?resizing_type=fit)

Rename your level objects in the **Outliner** so it’s clear which fire traps each switch controls. For example, if `BP_Switch1` turns off three traps, name them `BP_FireTrap_S1_0`, `BP_FireTrap_S1_1`, and `BP_FireTrap_S1_2`. Rename the extra fire traps something like `BP_FireTrap_Extra` to show they aren’t part of the puzzle.

If desired, you can help the player exit when they complete the puzzle by adding a final switch under the key that disables some traps along the way out.

[![](https://dev.epicgames.com/community/api/documentation/image/976c5bb0-a409-43b9-8896-54cd97ba4b70?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/976c5bb0-a409-43b9-8896-54cd97ba4b70?resizing_type=fit)

Test your puzzle often, paying attention to sightlines, frustration points, and possible shortcuts. Recruit a friend to help; they may find loopholes you didn’t expect. During playtesting, you may realize you need to make adjustments to stop or deter the player from skipping parts of the puzzle.

If you do discover an exploit, you have a couple of options:

* Rearrange the path or puzzle.
* Add more architectural blockers.
* Increase the fire damage so straying off the path has harsher consequences.

Leaving an exploit but increasing the cost gives the player a choice and autonomy. They can choose between spending more time to reveal the safe path or sacrificing their HP to rush to the key.

In the sample level’s puzzle, we added some rubble under the archway to the key so the player can see the key, but can’t skip directly to it. We also hid the switches not only for some rewarding reveals, but also to prevent skipping that part of the path.

[![](https://dev.epicgames.com/community/api/documentation/image/d80f09cd-9f74-47df-9646-e3e2d48d2da0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d80f09cd-9f74-47df-9646-e3e2d48d2da0?resizing_type=fit)

### Add Spikes to Past Obstacles

Let’s add spikes to past puzzles to add consequences for falling

Start with Room 1’s puzzle. For the first moving platform, keep the stakes low so if the player falls, they just climb back up and try again. When you introduce a new mechanic, give the player room to learn in a safe space so they can focus on learning

Similarly, in the Start Room, you can add some spikes to the pit under the first key. The player can practice jumping on the first two platforms to prepare them for the final, riskier jump over to the key. Now, grabbing the first key unscathed becomes a bit more exciting.

[![](https://dev.epicgames.com/community/api/documentation/image/d844b60e-a957-448d-aea0-a840ed9ca7f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d844b60e-a957-448d-aea0-a840ed9ca7f7?resizing_type=fit)

Once the player understands the basics and has some practice moving blocks on platforms and switches, it’s time to add consequences. Under the second platform or third button, place some spike traps. Now you’ve raised the tension since the player takes damage if they fall, but they can quickly move off the trap to minimize that damage and continue.

[![](https://dev.epicgames.com/community/api/documentation/image/fbb67b5b-d06a-41a6-9080-f2539d9b846f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fbb67b5b-d06a-41a6-9080-f2539d9b846f?resizing_type=fit)

Finally, for the last platform and switch, keep raising the danger. Cover the area below with spikes so they have to run further to get out of the spikes and therefore take more damage. At this point, the player should be more competent with the mechanic, and the consequence for mistakes feels fairer because they’ve already practiced.

[![](https://dev.epicgames.com/community/api/documentation/image/94d529e8-e5e4-4939-a9c1-5d1346fc09fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94d529e8-e5e4-4939-a9c1-5d1346fc09fa?resizing_type=fit)

This design follows this popular structure for introducing gameplay mechanics to players:

1. **Introduce**: The first platform teaches the game mechanic safely.
2. **Develop**: The second platform and cube tests the player’s growing skill with moderate risk.
3. **Twist**: The final platform escalates the danger and adds a new direction of movement, turning the mechanic into a tense challenge.

Like you learned in the Gameplay Design lesson in [Puzzles: Moving Platforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine), by ramping up the consequences across the puzzle, you balance fairness and excitement.

### Change a Trap’s Damage

You may decide to change the difficulty level by increasing or decreasing the damage of one type of trap. You could do this in one of two ways:

* In the **Outliner**, search for “spike” or “fire”, and select all traps of that type. In the **Details** panel, change **Setup > Base Damage** as desired. With this method, you’d need to remember to also change the **Base Damage** of any new instances of that trap you add to your level. Or, add new trap instances to the level by duplicating existing traps to avoid having to edit each new instance.

  [![](https://dev.epicgames.com/community/api/documentation/image/0e6026c5-d2ec-407e-b458-113e8676c39f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e6026c5-d2ec-407e-b458-113e8676c39f?resizing_type=fit)

  **OR**
* Open one of your child trap blueprints and go to its **Construction Script** tab. You can’t edit inherited variables in the My Blueprint panel, but you can set variables in the graph. After the two **Construction Script** nodes, connect a **Set Base Damage** node. In the node, change the **Base Damage** value as desired.

  [![](https://dev.epicgames.com/community/api/documentation/image/56ce1da9-ee30-45d0-aef1-26d5eb1f8917?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56ce1da9-ee30-45d0-aef1-26d5eb1f8917?resizing_type=fit)

To ensure your gameplay objects are predictable for the player, ensure all traps of one type deal the same damage.

In the tutorial’s sample level, fire traps do 5 damage per second, and spike trap instances are modified to do 10 damage per second.

## Try the Sample Level

If you’d like to use pieces of the room designed in this part of the tutorial instead of creating your own, copy the snippets below.

### Room 2’s Blockout

This text snippet contains Room 2’s floor, walls, and the new blockout shapes added to create this room’s puzzle. In the **Outliner**, all shapes are in a folder named Room2.

Command Line

```
Begin Map
   Begin Level
      Begin Actor Class=/Script/Engine.TextRenderActor Name=TextRenderActor_19 Archetype="/Script/Engine.TextRenderActor'/Script/Engine.Default__TextRenderActor'" ExportPath="/Script/Engine.TextRenderActor'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.TextRenderActor_19'"
         Begin Object Class=/Script/Engine.TextRenderComponent Name="NewTextRenderComponent" Archetype="/Script/Engine.TextRenderComponent'/Script/Engine.Default__TextRenderActor:NewTextRenderComponent'" ExportPath="/Script/Engine.TextRenderComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.TextRenderActor_19.NewTextRenderComponent'"
         End Object
         Begin Object Class=/Script/Engine.BillboardComponent Name="Sprite" Archetype="/Script/Engine.BillboardComponent'/Script/Engine.Default__TextRenderActor:Sprite'" ExportPath="/Script/Engine.BillboardComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.TextRenderActor_19.Sprite'"
         End Object
         Begin Object Name="NewTextRenderComponent" ExportPath="/Script/Engine.TextRenderComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.TextRenderActor_19.NewTextRenderComponent'"
            Text=NSLOCTEXT("[3C535F7772EB3B3657484B5E2D5B925D]", "2347F80B407C68C27836E990A20143CF", "Room 2")
            HorizontalAlignment=EHTA_Center
```

Expand code  Copy full snippet(1009 lines long)

To copy all of Room 2’s blockout, follow these steps:

1. Remove anything already in Room 2 (or anything at the end of Hallway 2):

   * Use the **Outliner** to select the existing contents of Room 2: Right-click the `Room2` folder, and select **Select > Immediate Children**. Press **Delete**.
   * Or, switch the viewport to **Top** orthographic view to select and delete the existing room manually.
2. Click **Copy Full Snippet**.
3. In Unreal Editor, ensure the viewport is the active panel (click anywhere in the viewport or **Outliner** and press **Esc**), and then press **Ctrl + V**.

Your level and **Outliner** should look like the following:

[![](https://dev.epicgames.com/community/api/documentation/image/6ccac1ea-2953-4763-a200-60666173dfa3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6ccac1ea-2953-4763-a200-60666173dfa3?resizing_type=fit)

### Room 2’s Switches, Traps, and Key

This text snippet contains the puzzle’s switches, traps, and red key. In the Outliner, all objects are in a folder named Room2.

To copy blueprint instances between projects, the parent blueprint assets must be completely identical and have the same file names and locations. If you’ve changed the blueprint’s components, variable names, or properties in your project, the snippet may not copy as expected, and you’ll need to set up these level objects manually.

Command Line

```
Begin Map
   Begin Level
      Begin Actor Class=/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.BP_TrapFire_C Name=BP_FireTrap_C_261 Archetype="/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.BP_TrapFire_C'/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.Default__BP_TrapFire_C'" ExportPath="/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.BP_TrapFire_C'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_FireTrap_C_261'"
         Begin Object Class=/Script/Engine.SceneComponent Name="DefaultSceneRoot" Archetype="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.BP_TrapFire_C:ICH-DefaultSceneRoot_GEN_VARIABLE'" ExportPath="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_FireTrap_C_261.DefaultSceneRoot'"
         End Object
         Begin Object Class=/Script/Engine.StaticMeshComponent Name="TrapBase" Archetype="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.BP_TrapFire_C:TrapBase_GEN_VARIABLE'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_FireTrap_C_261.TrapBase'"
         End Object
         Begin Object Class=/Script/Engine.BoxComponent Name="TrapTrigger" Archetype="/Script/Engine.BoxComponent'/Game/AdventureGame/Designer/Blueprints/Traps/BP_TrapFire.BP_TrapFire_C:TrapTrigger_GEN_VARIABLE'" ExportPath="/Script/Engine.BoxComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_FireTrap_C_261.TrapTrigger'"
         End Object
         Begin Object Name="DefaultSceneRoot" ExportPath="/Script/Engine.SceneComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.BP_FireTrap_C_261.DefaultSceneRoot'"
```

Expand code  Copy full snippet(2012 lines long)

To set up the puzzle’s blueprint pieces, follow these steps:

1. Click **Copy Full Snippet**.
2. In Unreal Editor, ensure the viewport or **Outliner** is the active panel, and press **Ctrl + V**.
3. Check each switch's **Setup** properties and, if necessary, reconnect each switch to its fire traps:

   1. In the **Outliner**, in the `Room2` folder, click `BP_Switch4`.
   2. In the **Details** panel, in the **Setup** section, expand the **Interact Object List**.
   3. For each element in the list, click the dropdown, search for `S4`, and select one of the `S4`-labelled fire traps.

      [![](https://dev.epicgames.com/community/api/documentation/image/55c2a8b0-d05b-423c-8e06-97c1633af5dc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55c2a8b0-d05b-423c-8e06-97c1633af5dc?resizing_type=fit)
   4. Repeat these steps for each switch:

      * `BP_Switch5` triggers `BP_FireTrap_S5_0-7`

        [![](https://dev.epicgames.com/community/api/documentation/image/602d1d66-687a-4a52-8995-d5f7e54bbcf5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/602d1d66-687a-4a52-8995-d5f7e54bbcf5?resizing_type=fit)
      * `BP_Switch6` triggers `BP_FireTrap_S6_0-3`

        [![](https://dev.epicgames.com/community/api/documentation/image/791d7eed-209e-46c9-aa6e-217f74e24e42?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/791d7eed-209e-46c9-aa6e-217f74e24e42?resizing_type=fit)
      * `BP_Switch7` triggers `BP_FireTrap_S7_0-4`

        [![](https://dev.epicgames.com/community/api/documentation/image/2663f1de-0647-43b8-9140-4c50c29d1d44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2663f1de-0647-43b8-9140-4c50c29d1d44?resizing_type=fit)
      * `BP_Switch8` triggers `BP_FireTrap_S8_0-3`

        [![](https://dev.epicgames.com/community/api/documentation/image/25cf3056-25ff-4e5c-b81c-116d7066be37?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25cf3056-25ff-4e5c-b81c-116d7066be37?resizing_type=fit)
      * `BP_Switch9`, under the key, triggers `BP_FireTrap_S9_0-4`

        [![](https://dev.epicgames.com/community/api/documentation/image/be1f62ee-6079-4d90-81be-1320e5d82973?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be1f62ee-6079-4d90-81be-1320e5d82973?resizing_type=fit)

Your level and **Outliner** should look like the following:

[![](https://dev.epicgames.com/community/api/documentation/image/ada49dc9-f618-45e4-bcb2-8033a32ed563?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ada49dc9-f618-45e4-bcb2-8033a32ed563?resizing_type=fit)

## Next Up

Next, you’ll learn how to add another popular hazard to your game — enemy NPCs! Learn how to create an AI enemy character and add Navigation Mesh to your level so the enemies can find and damage the player.

* [![Create an Enemy](https://dev.epicgames.com/community/api/documentation/image/4fbadab0-8092-43bc-9cd7-af30b9660238?resizing_type=fit&width=640&height=640)

  Create an Enemy

  Build game logic to create Enemy Characters that deal and receive damage.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Build a Set of Related Blueprint Classes](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#buildasetofrelatedblueprintclasses)
* [Create the Base Trap Blueprint](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#createthebasetrapblueprint)
* [Add Components](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#addcomponents)
* [Add Variables](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#addvariables)
* [Create a Function to Apply Damage](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#createafunctiontoapplydamage)
* [Create a Timer That Applies Damage Over Time](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#createatimerthatappliesdamageovertime)
* [Start and Stop Damage](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#startandstopdamage)
* [Test the Base Trap](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#testthebasetrap)
* [Subclass a Spike Trap](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#subclassaspiketrap)
* [Subclass a Fire Trap](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#subclassafiretrap)
* [Extend the Trap's Behavior](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#extendthetrap'sbehavior)
* [Update the HUD With Player HP](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#updatethehudwithplayerhp)
* [Add an HP Variable to the HUD](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#addanhpvariabletothehud)
* [Display the Player’s Starting HP](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#displaytheplayer%E2%80%99sstartinghp)
* [Update the Player’s HP After Taking Damage](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#updatetheplayer%E2%80%99shpaftertakingdamage)
* [Create a Fail and Respawn Condition](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#createafailandrespawncondition)
* [Add a Game-Over Screen](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#addagame-overscreen)
* [Build Logic for a Fail Condition](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#buildlogicforafailcondition)
* [Add Hazards to Your Puzzles](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#addhazardstoyourpuzzles)
* [Create a Maze Puzzle with Fire Traps](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#createamazepuzzlewithfiretraps)
* [Add Spikes to Past Obstacles](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#addspikestopastobstacles)
* [Change a Trap’s Damage](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#changeatrap%E2%80%99sdamage)
* [Try the Sample Level](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#trythesamplelevel)
* [Room 2’s Blockout](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#room2%E2%80%99sblockout)
* [Room 2’s Switches, Traps, and Key](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#room2%E2%80%99sswitches,traps,andkey)
* [Next Up](/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Create an Enemy

![Create an Enemy](https://dev.epicgames.com/community/api/documentation/image/4fbadab0-8092-43bc-9cd7-af30b9660238?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine)

[Blueprint Foundations

![Blueprint Foundations](https://dev.epicgames.com/community/api/documentation/image/d5519c66-d202-42af-bd24-b32ac0bbe537?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprint-foundations)
