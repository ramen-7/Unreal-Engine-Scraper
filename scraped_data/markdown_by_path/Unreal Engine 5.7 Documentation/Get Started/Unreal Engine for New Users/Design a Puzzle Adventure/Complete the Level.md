<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7 -->

# Complete the Level

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
8. Complete the Level

# Complete the Level

Finish the level by completing the gameplay loop and configuring an end state for the player.

![Complete the Level](https://dev.epicgames.com/community/api/documentation/image/9bc9fd90-bb8d-4408-86e3-3b5f01278239?resizing_type=fill&width=1920&height=335)

 On this page

In this tutorial series, you’ve used level design and game mechanics to engineer gameplay for your players. The puzzles, keys, and doors that you’ve built are all parts of a **gameplay loop**.

A gameplay loop is a series of actions that the player repeats, making up the core of your gameplay.

[![Infographic-of-gameplay-reward-loop](https://dev.epicgames.com/community/api/documentation/image/b0cd37a1-8e55-4432-a7a1-80aec4826cac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b0cd37a1-8e55-4432-a7a1-80aec4826cac?resizing_type=fit)

You still need to close the loop for the level you’ve built. In this tutorial, you’ll build a win screen that communicates to the player that they’ve completed the current level. You’ll also build a level transition point that verifies a **win conditio****n** and takes the player to the next level.

Once your level is complete, you’ll explore ways to expand on everything you’ve learned in this track.

A **win condition** is an objective the player must meet in order to complete a gameplay task, quest, level, or game. Your gameloop must provide the means to meet the win condition. In nonlinear games, you might have more than one win condition.

## Before You Begin

This tutorial assumes you already have an understanding of the following topics, which are covered in the previous sections of [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

* Widget Blueprints
* Blueprints
* Variables
* Collision Volumes
* Play-In-Editor Mode
* Parent and child assets

You’ll need the following assets from [Traps and Damage](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine):

* `WBP_EliminatedScreen` Widget Blueprint
* `BP_Key` Blueprint Class
* `Enum_KeyType` Enumeration

## Build the Level End

![Gif-clip-of-player-using-jump-pad-onto-a-platform](https://dev.epicgames.com/community/api/documentation/image/2de312d4-9343-4894-9018-ef87b7d99f86?resizing_type=fit)

Even though you’ve finished building your level’s core gameplay, the transition point is a good opportunity to give players an interesting way to finish your level. In this case, you’ll build a jump pad to launch players onto a raised platform. Later on, you’ll place the level transition point on the platform.

### Build a Platform

To build an elevated platform in one of your rooms, use the `SM_Cube` and `SM_Cylinder` static meshes in the **LevelPrototyping > Meshes** folder.

The tutorial sample level uses a 3.5m square platform with four columns that looks like this:

[![Platform-raised-with-4-columns-surrounding-it](https://dev.epicgames.com/community/api/documentation/image/d497434c-d1d0-4db2-9415-667e77d28feb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d497434c-d1d0-4db2-9415-667e77d28feb?resizing_type=fit)

If you’d like to copy these blockout pieces into your level, copy the snippet below. If you’ve been following along with the sample level, these shapes will appear near the back corner of Room 3. You can move them as desired.

To copy the platform, follow these steps:

1. Click **Copy Full Snippet**.

   Command Line

   ```
   Begin Map
      Begin Level
         Begin Actor Class=/Script/Engine.StaticMeshActor Name=StaticMeshActor_785 Archetype="/Script/Engine.StaticMeshActor'/Script/Engine.Default__StaticMeshActor'" ExportPath="/Script/Engine.StaticMeshActor'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.StaticMeshActor_785'"
            Begin Object Class=/Script/Engine.StaticMeshComponent Name="StaticMeshComponent0" Archetype="/Script/Engine.StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.StaticMeshActor_785.StaticMeshComponent0'"
            End Object
            Begin Object Name="StaticMeshComponent0" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.StaticMeshActor_785.StaticMeshComponent0'"
               StaticMesh="/Script/Engine.StaticMesh'/Game/LevelPrototyping/Meshes/SM_Cylinder.SM_Cylinder'"
               StaticMeshImportVersion=1
               bUseDefaultCollision=False
               StaticMeshDerivedDataKey="STATICMESH_FD1BFC73B5510AD60DFC65F62C1E933E_228332BAE0224DD294E232B87D83948FQuadricMeshReduction_V2$2e1_6D3AF6A2$2d5FD0$2d469B$2dB0D8$2dB6D9979EE5D2_CONSTRAINED0_100100000000000000000000000100000000000080FFFFFFFFFFFFFFFFFFFFFFFF000000000000803F00000000000000803F0000803F00000000000000003D19FC1626C9B2485E57DB4B8EC731318B8215AE8D46FAD400000000010000000100000000000000010000000100000000000000000000000100000001000000400000000000000001000000000000000000F03F000000000000F03F000000000000F03F0000803F00000000050000004E6F6E65000C00000030000000803FFFFFFFFF0000803FFFFFFFFF0000000000000041000000000000A0420303030000000000000000_RT00_0"
   ```

   Expand code  Copy full snippet(89 lines long)
2. In Unreal Editor, ensure the viewport or **Outliner** is the active panel, and press **Ctrl + V**.

Next, you’ll add a jump pad that launches the player up onto the platform.

### Use the Jump Pad

While you could build a jump pad from scratch, this would cost you time. In a development environment, where time is often limited, it can be useful to import **prefabricated (prefab)** assets instead of making your own. Choosing prefab that aligns with the visual style of your game can speed up development without standing out.

For this tutorial, you’ll use an asset that comes with the First Person Template, `BP_JumpPad`.

To integrate `BP_JumpPad`, follow these steps:

1. In the **Content Browser**, navigate to **LevelPrototyping > Interactable > JumpPad**.

   [![Image-of-jump-pad-asset](https://dev.epicgames.com/community/api/documentation/image/78fa2ff0-a878-4c5b-b9a4-851e3893ff16?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/78fa2ff0-a878-4c5b-b9a4-851e3893ff16?resizing_type=fit)
2. Drag an instance of `BP_JumpPad` into your level, in front of the platform. If you want to match the exact location shown in this tutorial, set `BP_JumpPad`’s **Location** to `1790`, `-1460`, `10`.

Your level should now look similar to this:

[![Image-of-raised-platform-with-jump-pad](https://dev.epicgames.com/community/api/documentation/image/d6b30fba-2c8e-4902-a3b0-dea6ae00cfe3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6b30fba-2c8e-4902-a3b0-dea6ae00cfe3?resizing_type=fit)

It’s time to test your work. First, make sure any `BP_Enemy` has a **Max Speed** of `0`. This ensures you’re not dealing with moving enemies while testing.

Right-click in the viewport and select **Play From Here** to playtest your level from your current location. Step onto the jump pad and try to reach the platform.

Notice that even with the jump pad’s boost, your player character can’t reach the platform. You can solve this by adjusting the jump pad’s **Velocity** parameter.

Like the many editable variables you’ve created in your blueprints, the Velocity parameter is a premade, instance-editable variable for the jump pad asset.

To adjust the **Velocity**, follow these steps:

1. Select `BP_JumpPad` in the viewport.
2. In the **Details** panel, set **Velocity** (**Z**) to `1000`.

   [![Image-of-jump-pad-variable-in-details-tab](https://dev.epicgames.com/community/api/documentation/image/db7a2f09-ebb4-4f06-9e83-8483845fc9d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db7a2f09-ebb4-4f06-9e83-8483845fc9d6?resizing_type=fit)

Now, test your level again. You should be able to jump onto the platform.

Next, you’ll create a win screen that displays when the player completes the level.

## Create a Win Screen

You’ll create a win screen by using a widget blueprint, similar to the `WBP_EliminatedScreen` game-over screen you created in [Traps and Damage](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine). Since these two screens are so similar, you’ll use `WBP_EliminatedScreen` as a starting point.

To create a win screen by duplicating your game-over screen, follow these steps:

1. In the **Content Browser**, navigate to **AdventureGame > Designer > Blueprints > Widgets**.
2. Right-click `WBP_EliminatedScreen` and click **Duplicate**.
3. Name the new widget blueprint `WBP_WinScreen` and double-click it to open it in the Widget Editor. Your **Widgets folder** should now look like this:

   [![A-win-bp-asset-in-the-widget-folder](https://dev.epicgames.com/community/api/documentation/image/e18115c0-7d76-4483-8502-e1b38c96ae2e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e18115c0-7d76-4483-8502-e1b38c96ae2e?resizing_type=fit)
4. To change the message, click the **Text** widget in the **Hierarchy**.
5. In the **Details** panel, under the **Content** heading, next to **Text**, enter `Level Complete! …Loading the Next Level.` in the text field.
6. Under the **Appearance** heading, next to **Color** and **Opacity**, click the color swatch to open the color picker. Choose a color you like, or set the **Hex sRGB** value to `FFE000FF` to follow along.
7. The win-screen text is shorter, so you can increase its size to fill the screen better. Under the **Font** heading, change the **Size** to `72` or a size you feel is most readable.
8. **Save**, **Compile**, and close the widget editor.

Next, you’ll create a level transition point.

## Create a Level Transition

[![Image-of-a-level-trigger-component](https://dev.epicgames.com/community/api/documentation/image/322b1bef-30dd-48f8-8a29-190e923ea570?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/322b1bef-30dd-48f8-8a29-190e923ea570?resizing_type=fit)

A **level transition** loads the next level. You can trigger a level transition in many ways; when a player finishes a cutscene, collects a pickup, or reaches the end of a level.

In this tutorial, the level transition will be a Blueprint that triggers when two things occur:

* The player overlaps the level transition.
* The win condition is met.

To create a new Blueprint, follow these steps:

1. In the **Content Browser**, navigate to **A****dventureGame > Designer > Blueprints**.
2. Right-click and select **New Folder**. Name this folder `LevelTransition`.

   [![New-level-transition-folder](https://dev.epicgames.com/community/api/documentation/image/a2bdea81-edda-48f3-87fc-7582fbc4cf1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2bdea81-edda-48f3-87fc-7582fbc4cf1a?resizing_type=fit)
3. Inside the **Level Transition** folder, right-click and select **Blueprint Class** to create a new Blueprint.
4. Select **Actor** as the parent class.
5. Name this new Blueprint `BP_LevelTransition` and double-click it to open it in the Blueprint Editor.

Your Level Transition folder should now look like this:

[![New-level-transition-blueprint-class-asset](https://dev.epicgames.com/community/api/documentation/image/e8389c26-e388-423d-a9ce-2bc38cb6da28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8389c26-e388-423d-a9ce-2bc38cb6da28?resizing_type=fit)

Much like the other blueprints you’ve created so far, your level transition needs the following:

* A **static mesh** that the player can see during runtime.
* A **collision shape** to detect when the player collides with it.
* **Logic** to power the interaction.

Let’s build out the mesh and box collision first, and then move onto the logic.

To create a static mesh and collision shape, follow these steps:

1. In the **Components** tab of `BP_LevelTransition`, click the **Add** button and search for `cube` to create a new static mesh.
2. Name this static mesh `TransitionPoint`.

   [![Static-mesh-transition-type](https://dev.epicgames.com/community/api/documentation/image/4b9947e3-513c-4a9e-89d7-318020408443?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b9947e3-513c-4a9e-89d7-318020408443?resizing_type=fit)
3. With **TransitionPoint** selected, in the **Details** panel, set its **Scale** to `3.0`, `3.0`, `0.1`. This is sized to fit the sample level’s end platform; you can resize yours to what works best in your level.
4. Back in the **Components** tab, select **DefaultSceneRoot**. Click the **Add** button and search for `box collision` to create a collision shape.
5. Name the box collision `LevelTrigger`.

   [![Level-trigger-box-collision](https://dev.epicgames.com/community/api/documentation/image/78476897-aa36-495b-bcd5-549f3ec2ff6a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/78476897-aa36-495b-bcd5-549f3ec2ff6a?resizing_type=fit)
6. With **LevelTrigger** selected, in the **Details** panel, set its **Scale** to `4.0`, `4.0`, `2.0`. Set its **Z** location to `55.0`.

   [![Collision-box-outline](https://dev.epicgames.com/community/api/documentation/image/4f2356f6-7f79-4665-b41d-09b88f871850?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f2356f6-7f79-4665-b41d-09b88f871850?resizing_type=fit)

   If the box collision isn’t appearing as the correct shape, make sure it’s not a child of **TransitionPoint**.
7. **Save** and **Compile**.

## Build with Logic

`BP_LevelTransition` should do five things in sequence:

1. Check for overlap.
2. Verify the win condition.
3. Disable player input.
4. Display the win screen.
5. Load the next level.

Step by step, let’s create the logic that powers these interactions.

### Check for Overlap

To build logic that checks for overlap, follow these steps:

1. In the **MyBlueprint** tab of `BP_LevelTransition`, In the **Variables** section, click the **+** button to create a new variable and name it `OtherActor`.
2. Set the pin type to **Actor** (**Object Reference**).

   [![Image-of-other-actor-variable](https://dev.epicgames.com/community/api/documentation/image/afc5515d-9a0a-41bb-98c9-340c81f2ff78?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afc5515d-9a0a-41bb-98c9-340c81f2ff78?resizing_type=fit)
3. In the **EventGraph**, delete the three existing event nodes. You won’t need them.
4. In the **Components** tab, right-click on **LevelTrigger** and click **Add** **Event > Add OnComponentBeginOverlap**. This function checks when an object overlaps the collision shape.
5. From the **Exec** pin, drag out and create **Set Other Actor**.
6. Connect both **Other Actor** pins.

   [![Blueprint-of-other-actor-pins-connected](https://dev.epicgames.com/community/api/documentation/image/743f93c4-1cb6-48cc-9a5c-02a56855cdb7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/743f93c4-1cb6-48cc-9a5c-02a56855cdb7?resizing_type=fit)

Next, you’ll build logic that verifies the win condition.

### Verify the Win Condition

In this tutorial, the win condition will be collecting all three keys. The reason for choosing this particular condition is to anticipate and prevent game-breaking player actions.

For example, if the win condition was “player overlaps the level transition” and a player finds a way over the room walls, they could bypass your entire level. By using the keys as a win condition, the player must complete your game loop — even if they find a way past the walls and doors.

While it's impossible to predict every bug, design that thinks ahead can prevent players from breaking your game.

To create an array to store the key data, follow these steps:

1. In the **MyBlueprint** tab of `BP_LevelTransition`, click the **+** button to create a new variable and name it `HeldKeys`.
2. Set the pin type to **Enum Key Type** and the container type to **Array**.

   [![Variable-type-enum-key](https://dev.epicgames.com/community/api/documentation/image/d4629653-4e30-472b-a913-ec4224a5ec1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4629653-4e30-472b-a913-ec4224a5ec1c?resizing_type=fit)
3. From the **Exec** pin of the **Set** node, drag out and create **fnBPIGetKeys**.
4. From the **Target** pin, drag out and create **Get Other Actor**.
5. From the **Exec** pin on **fnBPIGetKeys**, drag out and create **Set Held Keys**.
6. Connect both **Held Keys** array pins.

   [![BP-showing-held-key-array-pins-connected](https://dev.epicgames.com/community/api/documentation/image/e5973914-4b42-4ea5-b260-109a49b7d0b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5973914-4b42-4ea5-b260-109a49b7d0b6?resizing_type=fit)

To create an enum key type to set a win condition, follow these steps:

1. Create a new variable and name it `RequiredKeys`. This is your win condition.
2. Make sure the pin type is **Enum Key Type** and the container type is **Array**.
3. In the **Details** panel, enable **Instance Editable** and set the **Category** to `Setup`.
4. **Compile** the Blueprint to gain access to the **Default Value**. Click the **+** button to add three new elements to the array.
5. Click the index dropdown menus and set the indexes to **Yellow**, **Blue**, and **Red**.

   [![Array-elements-indexed-as-yellow-blue-red](https://dev.epicgames.com/community/api/documentation/image/38b74bee-e823-4b82-aa75-9a4e34e0b26b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38b74bee-e823-4b82-aa75-9a4e34e0b26b?resizing_type=fit)

You’ll create a boolean to verify whether the condition is met or not. A **For Each Loop** **with Break** will cycle through the `HeldKeys` array to check for each key — and break if there are keys missing.

To build logic that checks for missing keys, follow these steps:

1. Create a new variable and name it `FoundAllKeys`.
2. Set the pin type to **Boolean** and the container type to **Single**.

   [![Found-all-keys-as-boolean](https://dev.epicgames.com/community/api/documentation/image/15b3fa08-4b28-4e4e-85ef-c941f5b8b209?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/15b3fa08-4b28-4e4e-85ef-c941f5b8b209?resizing_type=fit)
3. From the **Exec** pin of **SetHeldKeys**, drag out and create a **For Each Loop with Break**.
4. From the **Array** pin of the **For Each Loop**, drag out and create a **Get Required Keys** node.
5. From the **Loop Body** pin on the loop, drag out and create a **Branch**.
6. From the **Condition** pin, drag out and create a **Contains Item (Array)** node.
7. From the **Target Array** pin on the **Contains** node, drag out and create **Get Held Keys**.
8. Connect the **Item to Find** pin on the **Condition** node to the **Array Element** pin on the loop node.

   [![BP-of-array-element-node-to-condition-pin](https://dev.epicgames.com/community/api/documentation/image/175c834a-a6c7-4c28-9e4a-b644b58170f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/175c834a-a6c7-4c28-9e4a-b644b58170f0?resizing_type=fit)
9. From the **True** pin of the **Branch** node, drag out and create **Set Found All Keys**. Click the checkbox next to **FoundAllKeys** to set it to true.
10. From the **False** pin of the **Branch** node, drag out and create **Set Found All Keys**. Leave the checkbox empty and connect the **Exec** pin to the **Break** pin on the **For Each Loop**.

    [![BP-of-for-each-loop](https://dev.epicgames.com/community/api/documentation/image/cc3704be-a288-4bda-b0f1-063123339d54?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc3704be-a288-4bda-b0f1-063123339d54?resizing_type=fit)

You have three more steps to do in the sequence we looked at earlier, but only if the player has all keys:

* Disable player input.
* Display the win screen.
* Load the next level.

To use the **FoundAllKeys** result to start a sequence of logic, follow these steps:

1. From the **Completed** pin of the **For Each Loop**, drag out and create a **Branch**.
2. Drag out from the **Condition** pin and create **Get FoundAllKeys**.
3. From the **True** pin of the **Branch** node, drag out and create a **Sequence** node.
4. Since you need to build three actions in this sequence, click the **Add Pin** button.

   [![BP-showing-the-sequence-node-with-add-pin](https://dev.epicgames.com/community/api/documentation/image/ca899b05-a8d9-4bf9-a3a1-f886c05cb698?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca899b05-a8d9-4bf9-a3a1-f886c05cb698?resizing_type=fit)

Let’s move onto the next step in the sequence; disabling player input.

### Disable Player Input

While displaying the win screen, disabling player input prevents players from moving around and receiving unintended damage.

To disable player input, follow these steps:

1. From the **Then 0** pin of **Sequence**, drag out and create a **Disable Input** node.
2. From the **Target** pin of the **Disable Input** node, create **Get Other Actor**.
3. From the **Player Controller** pin, drag out and create a **Get Player Controller** node.

   [![Get-player-controller-node-to-player-controller-pin](https://dev.epicgames.com/community/api/documentation/image/e270ca9a-3dd4-4efe-aae4-08016460428f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e270ca9a-3dd4-4efe-aae4-08016460428f?resizing_type=fit)

Next, you’d build logic to display the win screen.

### Display the Win Screen

To display your `WBP_Winscreen` widget, follow these steps:

1. From the **Then 1** pin of the **Sequence** node, drag out and create a **Create Widget** node.
2. Set the **Class** to **WBP\_WinScreen**.
3. From the **Exec** node on the **Create Widget** node, drag out and create an **Add to Viewpor****t** node.
4. Connect the **Return Value** pin on **Create Widget** to the **Target** node on **Add to Viewport**.

   [![Add-to-viewport-node-in-blueprint](https://dev.epicgames.com/community/api/documentation/image/9e1a9181-2445-4c1b-8af9-87624d5d44ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e1a9181-2445-4c1b-8af9-87624d5d44ba?resizing_type=fit)

Do you see an issue with this logic? For now, you’ll move on and build the final step without fixing the issue. Later on, you’ll playtest the level to discover the problem and build a solution.

### Load the Next Level

For this tutorial, you’ll use your current level as a placeholder for the next level. When you're designing your own game, the transition point should take players to a brand new level.

To build logic that loads the current level, follow these steps:

1. From the **Then 2** pin of the **Sequence** node, drag out and create an **Open Level (by Object Reference)** node.
2. From the **Level** pin of **Open Level**, drag out and search for **Promote** to **Variable**. This will force the creation of a **World**-type variable.

   [![Open-level-node-to-next-level](https://dev.epicgames.com/community/api/documentation/image/5e684df7-582f-4a9e-8860-f06df03f3793?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e684df7-582f-4a9e-8860-f06df03f3793?resizing_type=fit)

   You can also create this variable through the MyBlueprints tab, but the World pin type can be difficult to locate.
3. With the World variable selected, in the **Details** panel, rename the variable to `NextLevel`.
4. Add it to the **Setup** category and enable **Instance Editable**.
5. **Compile** your Blueprint to gain access to the variable’s **Default Value** and set it to the level you’d like to load. If you’re following along with this tutorial, set it to `Lvl_Adventure` to loop the current level.

   [![Details-tab-showing-next-level](https://dev.epicgames.com/community/api/documentation/image/66f685e2-1f42-4aa9-9cea-53e159801120?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/66f685e2-1f42-4aa9-9cea-53e159801120?resizing_type=fit)
6. **Save** and **Compile**.

It’s time to test your work. Drag an instance of `BP_LevelTransition` onto the raised platform.  Then, give yourself easy access to the keys to meet the win condition. You can do this by placing instances of the yellow, blue, and red keys you created in [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine) into the same room.

Your level should now look something like this:

[![High-level-view-of-the-level](https://dev.epicgames.com/community/api/documentation/image/8e87f953-abbf-442f-9836-c7276e455fb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e87f953-abbf-442f-9836-c7276e455fb3?resizing_type=fit)

Right-click in the viewport and select **Play From Here** to playtest your level from your current location. If you jump onto the platform and activate the level transition, you’ll notice the screen freezes and the next level opens without giving the player time to read the win screen message.

![View-of-player-jumping-to-platform-and-clipped-message](https://dev.epicgames.com/community/api/documentation/image/6c3bfb1b-305b-4ef5-83f3-51ada5798fa6?resizing_type=fit)

You’ll solve this issue in the next section.

### Create a Delay

This tutorial uses **Open Level** to close the current level and open the next as a new game instance. During loading, Open Level freezes the game. Depending on the player’s system, that freeze might be too short (to read your win screen), or too long (appearing as if the game has crashed).

Many games, even those using [Level Streaming](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-streaming-overview-in-unreal-engine), utilize loading screens to let the player know that the game is working properly and that they should wait. Loading screens also solve another problem; long, frequent, or boring wait times can break immersion and cause frustration. Loading screens often include tips, animation, or audio to retain the player’s attention while they aren’t playing.

To solve this technical issue with design, you’ll create an intentional delay that achieves the following:

* Equalize the loading times for all players.
* Ensure the player has enough time to read the win screen.
* Disguise loading times by giving the player something to look at.

To insert a delay, follow these steps:

1. Open up `BP_LevelTransition`. In the **MyBlueprint** tab, click **+** to add a new variable and name it `LevelLoadDelay`.
2. Set the pin type to **Float**.
3. In the **Details** panel, enable **Instance Editable** and set the **Category** to **Setup**.
4. **Compile** the blueprint to gain access to the **Default Value**. **Level Load Delay** will set the amount of time you want the delay to last. To follow along, set it to `5.0` seconds.

   [![Level-load-delay-as-variable-name](https://dev.epicgames.com/community/api/documentation/image/ac940695-6852-4097-8845-b399c9295a09?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac940695-6852-4097-8845-b399c9295a09?resizing_type=fit)
5. In the **EventGraph**, navigate to the **Sequence** node. To insert a delay, drag out from the **Then 2** pin and create a **Delay** node.
6. From the **Duration** pin, drag out and create **Get LevelLoadDelay**.

   [![Level-load-delay-in-blueprints](https://dev.epicgames.com/community/api/documentation/image/1baf2d74-cdaf-410e-ab87-ab40276bc998?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1baf2d74-cdaf-410e-ab87-ab40276bc998?resizing_type=fit)
7. **Save**, **Compile**, and close your blueprint.

Your final `BP_LevelTransition` **EventGraph** should look like this:

Blueprint

Level Transition

Copy full snippet(268 lines long)

Now, test your level again. When you overlap the level transition point, the win screen should display, the background should blur, and player input should be disabled for five seconds before your player character appears in the next level.

![Level-complete-with-accurately-timed-end-message](https://dev.epicgames.com/community/api/documentation/image/3f7f2ef8-09dc-4689-ba77-b4b2405794b5?resizing_type=fit)

Before you playtest your level for the final time, remember to remove the keys from Room 3 and set `BP_Enemy`’s **Max Speed** back to `200`.

## From Concept to Creation

Let's take a look at the blockout we created in [Project Setup and Level Blockout](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine) compared to the final level. From its initial design, our level design and gameplay loop changed to address bugs, create new features, or work around limitations that playtesters discovered during development.

By blocking out your level, working modularly, solving technical problems with design, and keeping your assets organized, you can stay flexible when limitations or new features change the course of your game’s development.

|  |  |
| --- | --- |
|  |  |

By completing this track, you've taken a level from concept to playable demo. You now have the building blocks to design more than just one level. You can combine switches, traps, keys, doors, and enemies in unlimited ways to design new gameplay loops in your own style. When connected together, each level becomes part of a much larger project; an entire game.

## Example Project

Below is a link to download the final project that you can build using this tutorial series of documentation. You can use this example project to see what your final project might look like, or as a reference to see how we built and designed the project.

[Download the Designer Track here](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/691d5f75-5649-4521-95de-3d759a6f1c82/adventuredesigner.zip)

*(Download size: 75 MB)*

To open the project, unzip the file and move the adventuredesigner folder to your Unreal Projects directory (by default, find this in `C:\Users\UserName\Documents\Unreal Projects`).

## Next Up

To continue working on your level by adding materials, lighting, post-process effects, sound, and visual effects, try the Artist Track Tutorial Series:

* [![Art Pass for a Puzzle Adventure Game](images/static/document_list/empty_thumbnail.svg)

  Art Pass for a Puzzle Adventure Game

  Learn how you can apply art workflows with materials, sounds, and visual effects to the Puzzle Adventure game.](https://dev.epicgames.com/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

If you'd like to walk through building another blueprint, continue to this bonus module of the Designer Track Tutorial Series:

* [![Bonus: Spawn New Cubes](https://dev.epicgames.com/community/api/documentation/image/74689b74-657d-4bee-87d4-35498f257195?resizing_type=fit&width=640&height=640)

  Bonus: Spawn New Cubes

  Add a new mechanic to your puzzle adventure game where BP\_Cube actors spawn to a specified limit.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-11-spawn-new-cubes-mechanic-in-unreal-engine)

If you are interested in packaging your project, as a standalone program to test and share, see the following documentation:

* [![Packaging Unreal Engine Projects](https://dev.epicgames.com/community/api/documentation/image/d1a0635f-ebb0-4dae-bc3c-9f68a7d2e9c2?resizing_type=fit&width=640&height=640)

  Packaging Unreal Engine Projects

  Packaging Unreal game projects for distribution.](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-project)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [hud](https://dev.epicgames.com/community/search?query=hud)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)
* [end stated](https://dev.epicgames.com/community/search?query=end%20stated)
* [gameplay loop](https://dev.epicgames.com/community/search?query=gameplay%20loop)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Build the Level End](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#buildthelevelend)
* [Build a Platform](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#buildaplatform)
* [Use the Jump Pad](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#usethejumppad)
* [Create a Win Screen](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#createawinscreen)
* [Create a Level Transition](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#createaleveltransition)
* [Build with Logic](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#buildwithlogic)
* [Check for Overlap](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#checkforoverlap)
* [Verify the Win Condition](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#verifythewincondition)
* [Disable Player Input](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#disableplayerinput)
* [Display the Win Screen](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#displaythewinscreen)
* [Load the Next Level](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#loadthenextlevel)
* [Create a Delay](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#createadelay)
* [From Concept to Creation](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#fromconcepttocreation)
* [Example Project](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#exampleproject)
* [Next Up](/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Packaging Unreal Engine Projects

![Packaging Unreal Engine Projects](https://dev.epicgames.com/community/api/documentation/image/d1a0635f-ebb0-4dae-bc3c-9f68a7d2e9c2?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/packaging-your-project)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Your First Hour in Unreal Engine

![Your First Hour in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b68b5e7a-09df-4354-acb4-2fb8b3291793?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/first-hour-in-unreal-engine)
