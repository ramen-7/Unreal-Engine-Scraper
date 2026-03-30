<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7 -->

# Open Doors with Keys

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
8. Open Doors with Keys

# Open Doors with Keys

Configure the BP\_DoorFrame blueprint so the doors can change color and only open with the matching BP\_Key.

![Open Doors with Keys](https://dev.epicgames.com/community/api/documentation/image/049be744-b2b2-4da2-accf-781821e7a1af?resizing_type=fill&width=1920&height=335)

 On this page

Now that the player can pick up keys in the game, you’ll add the functionality to unlock and open doors when the player has picked up the required key. In this part of the tutorial, you will modify the `BP_DoorFrame` blueprint and explore **Functions** in Blueprints.

Unlockable doors provide a way to control the flow of the game and provide a sense of progression to the player. The project we are currently working on is divided into rooms. Therefore, picking up keys to unlock doors provides a logical progression path to the player.

## Before You Begin

Make sure you understand these topics covered in the previous sections of the [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) tutorial series:

* [Blueprint basics](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-foundations), including [Blueprint Interfaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine).
* Creating variants of an object using a Map variable.

You’ll need the following assets created in the previous tutorial, [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine):

* `BP_Key`
* `BPL_FPGame` Blueprint Function library
* `BPI_PlayerKeys` Blueprint Interface
* Three `BP_DoorFrame` instances placed in your level between rooms or hallways.

## Add Color Options to the Door

Since the first-person template already has a door blueprint, you can modify the existing blueprint to add the functionality of unlocking doors with a key.

Your door needs a few things to work with the key system you defined in the previous part of this tutorial. Just like the key, your door needs to know that the actor interacting with it implements the `BPI_PlayerKeys` interface.

The door should change its color to match the key that it accepts, meaning it needs to know what Key Type can unlock it. Last, it needs the same KeyMap variable with red, yellow, and blue color combinations.

### Create Variables for Interacting with the Player and Keys

To add new variables to the `BP_DoorFrame` blueprint, follow these steps

1. Go to the **Content Browser**, navigate to the **LevelPrototyping** > **Interactable** > **Door** folder, and open the `BP_DoorFrame` blueprint.
2. In the **My Blueprint** panel, in the **Variables** section, add a new variable named **UseKey**, with the type **Boolean**. This determines if the door needs a key to open it.
3. Create another variable named **RequiredKey** of the type **Enum Key Type**. This determines the key required to open the door.

   [![Add Variables](https://dev.epicgames.com/community/api/documentation/image/af3fe9dd-cf49-45b4-b7c9-6a65dcf62b33?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af3fe9dd-cf49-45b4-b7c9-6a65dcf62b33?resizing_type=fit)

   Add Variables
4. Click the **Eye** icon next to both variables so the eye is open, making them **editable**.
5. Select the **UseKey** variable. In the **Details** panel, enter `Setup`as its **Category**.
6. Select **RequiredKey** and change its **Category** to **Setup**.
7. Create a new variable named **Other Actor** of the type **Actor** > **Object Reference**. This stores the actor interacting with the door and you'll use it to check if the player has overlapped with the door volume.

   [![](https://dev.epicgames.com/community/api/documentation/image/c7b0d15b-b190-43f6-82c9-43515d0eb0ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7b0d15b-b190-43f6-82c9-43515d0eb0ec?resizing_type=fit)

### Build the Key Map Variable

Just like you did in `BP_Key`, you’ll add the map variable that maps key types to material colors. However, with the door, you don’t want the door meshes to change shape, so you won’t add new mesh shapes to the map.

To build the door’s KeyMap variable, follow these steps:

1. Create a variable named **KeyMap**, of the type **Enum Key Type**.
2. Click this variable, and in the **Details** panel, click the **Container** dropdown and select **Map**.
3. Change the map’s value type to **Struct Key Data**.

   [![Set Struct Key Data Type](https://dev.epicgames.com/community/api/documentation/image/f5dbf1cf-acdc-470c-b49a-8b34f8f6d497?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5dbf1cf-acdc-470c-b49a-8b34f8f6d497?resizing_type=fit)

   Set Struct Key Data Type
4. **Compile** the blueprint to add KeyMap values.
5. Under the map’s **Default Value** section,  **Add** (**+**) 3 new elements to the **Key Map**.

   When you add the first entry, change the type to another color so you can keep adding new entries, you can’t add the same entry more than once.

   [![Add Key Map Entries](https://dev.epicgames.com/community/api/documentation/image/e7df8100-5737-485f-a9ec-79171f8a6f75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e7df8100-5737-485f-a9ec-79171f8a6f75?resizing_type=fit)

   Add Key Map Entries
6. For each map element, add the corresponding **Key Material**:

   1. `M_BasicColor_Yellow`
   2. `M_BasicColor_Red`
   3. `M_BasicColor_Blue`

   [![Add materials to corresponding Key Map Index](https://dev.epicgames.com/community/api/documentation/image/63660e73-14e0-4fcb-b374-15fd6ce1da04?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/63660e73-14e0-4fcb-b374-15fd6ce1da04?resizing_type=fit)

   Add materials to corresponding Key Map Index
7. For each element, ensure the **Key Mesh** says **None**. To remove a mesh, click the dropdown and select **Clear** at the top of the list.
8. **Save** and **Compile** the door blueprint.

### Add Color-Changing Blueprint Logic

With your variables set up, you can add the color-changing functionality by modifying the blueprint graph.

First, you need to change the door to have red, blue, and yellow color options that are controlled by the new **RequiredKey** variable you added. The door should change its color as you set it up in the level, not when the gameplay starts. Therefore, you will use the **Construction Script** tab to create this functionality.

To add the door’s color options, follow these steps:

1. Navigate to the door’s **Construction Script** tab, where you can create functionality for when the door is created. In the graph, find the purple **Construction Script** node that starts off the logic in this function.
2. On the **Sequence** node that’s connected to the **Construction Script**, use **Add pin**(**+**) to create one more pin, named **Then 2**, which you can use to build upon the chain.

   [![Sequence Node Add Pin](https://dev.epicgames.com/community/api/documentation/image/744e84b2-c936-4b40-bd02-ec78cc0a397a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/744e84b2-c936-4b40-bd02-ec78cc0a397a?resizing_type=fit)

   Sequence Node Add Pin

   The **Sequence** node is used to build a sequence of actions, where **Then 0** gets executed first, **Then 1** after that, and so on, depending on how many pins you choose to add. They help organize your graph and prevent one chain of logic from getting too long.
3. Drag the **Then 2** pin to an empty part of the graph and create a **Branch** node.
4. Drag the **Condition** pin of the **Branch** node and create a **Get Use Key** node. Now, the Branch tests if the door should use keys or not.

   [![Branch Node Logic](https://dev.epicgames.com/community/api/documentation/image/e313562c-35a2-4382-a292-e4db858aa14e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e313562c-35a2-4382-a292-e4db858aa14e?resizing_type=fit)

   Branch Node Logic
5. Drag the **True** pin of the **Branch** node and create a **Fn BPLSet** Key node. This is the library function that applies a new material color (and mesh, if provided) to an array of static meshes.
6. Drag the **Fn BPLSet Key** node’s **Static Mesh Array** pin and create a **Make Array** node.
7. Click the **Add pin (+)** button on the **Make Array** node.
8. From the **Make Array** node, drag the first pin, **[0]**, and create a **Get Door** node.

   If you look in the **Variables** > **Components** list in the **My Blueprint** panel, you’ll see the door has **Door** and **Door2** static mesh components. These are what you want to change color.
9. Drag the second pin, **[1]**, and create a **Get Door 2** node. This makes an array based on the two static mesh components, **Door** and **Door 2**.
10. From the **Fn BPLSet Key** node, drag the **Key Map** pin and create a **Get Key Map** node. This is a reference to the door’s **KeyMap** variable.
11. Then, drag the **Key** pin and create a **Get Required Key** node, which is a reference to the **RequiredKey** variable you added earlier.
12. **Compile** and **Save** the blueprint.

The door’s Construction Script should now have the following after the **Then 3** pin of the **Sequence** node:

[![Final Door Blueprint Logic](https://dev.epicgames.com/community/api/documentation/image/9cfde287-a6b8-4f77-9e9e-b97b81ebaf97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9cfde287-a6b8-4f77-9e9e-b97b81ebaf97?resizing_type=fit)

Final Door Blueprint Logic

Here's a copyable version of this logic:

Blueprint

Door Construction Script

Copy full snippet(83 lines long)

If copying and pasting this snippet into `BP_DoorFrame’s Construction Script`, you’ll need to add a third pin to the existing **Sequence** node and then connect that pin to the **Branch** node’s exec pin.

### Test the Door Colors

After color-coding the door game object, you can set the doors to not open unless the player has the correct key.

In your level, select one of your `BP_DoorFrame` instances.

In the **Details** panel, enter Key in the search field at the top. This reveals two options: **Use Key** and **Required Key**. Change the **Required Key** to a different key type. The door’s color should change to match the key type.

If you toggle **Use Key** to **false**, the door’s color won’t update, since you set that as a condition in the blueprint.

Modifying the Door Color

As a reminder, this is the benefit of using the **Construction Script** graph tab in the Blueprint Editor. You can see changes happen in the level editor instead of having to wait to enter game mode.

## Build Key-Based Door Logic

Next, you can build the functionality to check what keys the player has. For this, you will define a custom function named **fnHasKey** in the `BP_DoorFrame` blueprint that checks if the player has the required key.

A function is a reusable set of blueprint nodes that performs a specific task.

### Create a Function That Checks for Keys

This function will compare the door's required key with the player character's array of keys and return a true or false (boolean) value. You'll use a local variable for that boolean return value.

To create a function with a local variable, follow these steps:

1. In the `BP_DoorFrame`blueprint, in the **My Blueprint** panel, use **Add** (**+**) next to the **Functions** section. This is similar to adding a variable, but instead, you’re adding a function.
2. Name the new function **fnHasKey**.

   [![Name the Function FnHasKey](https://dev.epicgames.com/community/api/documentation/image/b78b8e46-8833-410e-bad9-7b8d630e15df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b78b8e46-8833-410e-bad9-7b8d630e15df?resizing_type=fit)

   Name the Function FnHasKey
3. Since a function can have its own set of nodes, it opens in its own **fnHasKey** tab with a separate node graph. If you close this tab and need to re-open it, double-click the function in the **Functions** list.
4. In the **My Blueprint** panel, you will see a new section at the bottom that’s called **Local Variables (FnHasKey)**. Create a new **Local Variable** using **Add** (**+**) next to that section.
5. Name the variable **HasRequiredKey** and set its type to **Boolean**.

   [![Has Required Key Variable](https://dev.epicgames.com/community/api/documentation/image/ba20411a-e8e6-41ca-96b9-63f22c5b6a33?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ba20411a-e8e6-41ca-96b9-63f22c5b6a33?resizing_type=fit)

   Has Required Key Variable

   Local variables are similar to regular variables, but local to a particular function. They are useful for storing temporary values while the function runs. You can then pass this value back to the rest of the blueprint by using a **Return Node**.

With the function set up, you can add logic that checks if the player has the right key.

To check if the actor in the door’s volume has the required key, follow these steps:

1. Drag the pin of the **fnHasKey** function entry node and create a **Sequence** node. This organizes the function’s logic into a sequence of actions that run in order.
2. Drag the Then 0 pin of the Sequence node and create an **Fn BPIGet Keys (Message)** node. This is the interface function that returns an array of keys the player has already found.
3. Drag the **Target** pin of the **Fn BPIGet Keys** node and create a **Get Other Actor** node. Once you set up the door’s event graph, this variable will store the actor overlapping the door’s volume.

   [![FnKeys Logic](https://dev.epicgames.com/community/api/documentation/image/a15e8c58-2859-4c99-9590-8f86b35f95d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a15e8c58-2859-4c99-9590-8f86b35f95d5?resizing_type=fit)

   FnKeys Logic
4. Drag the **HasRequiredKey** local variable near the **Fn BPIGet Keys** node and select **Set**.
5. Drag the **Exec** pin of the **FN BPIGet Keys** node and connect it to the **Set** **HasRequiredKey** node.
6. From the Set **HasRequiredKey** node, drag the **HasRequiredKey** pin and create a **Contains Item** node, listed under the **Array** section of the search. This node checks if a specific item is in an array and returns true or false.

   You can also search for **Array Contains Item** to narrow down the search to that particular option.
7. From the **Contains Item** node, drag the **Target Array** pin (the square pin) and connect it to the **Held Keys** pin of the **Fn BPIGet Keys** node.
8. Drag the **Item to Find** pin (that looks like a circle) of the **Contains Item** node, and create a **Get Required Key** node.

  This is what your function’s graph should look like so far:

[![FnHasKey Function Logic](https://dev.epicgames.com/community/api/documentation/image/dfc1bca9-e042-4e9e-8bfa-44f099316fc8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dfc1bca9-e042-4e9e-8bfa-44f099316fc8?resizing_type=fit)

FnHasKey Function Logic

This sequence of actions checks if the keys held by the **OtherActor** (variable) contain the **RequiredKey** (variable). If so, it will set **HasRequiredKey** to **true**.

Now, pass the **HasRequiredKey** result to the rest of the blueprint. To do this, use a **Return** node, which stops the execution of a function and returns a value to the blueprint that called the function.

To end the function with a **Return** node, follow these steps:

1. From the **Sequence** node, drag the **Then 1** pin, search for **Return** in the node actions list, and select **Add Return Node**.
2. To make the function return a value, it needs an output. Click the **Return Node** to highlight it.
3. In the **Details** panel, use **Add** (**+**) next to the **Outputs** section at the bottom. This adds a new output, which is the value it passes out of this function.
4. Name this output **KeyFound** and change its type to **Boolean**.
5. Back in the graph, drag the **Key Found** pin of the **Return** node, and create a **Get HasRequiredKey** node.

The complete FnHasKey function graph should now look like the following:

Blueprint

FnHasKey Function

Copy full snippet(212 lines long)

If you copy this snippet into your project, you need to connect the **FnHasKey** function entry node to the **Sequence** node.

### Lock and Unlock Doors With Keys

Now you can modify the door to open if all the necessary conditions are true.

Just like with the key, you’ll need to check if the character implements the `BPI_PlayerKeys` interface (the player’s “permission slip”) before they can try to open a door that uses keys.

So before it opens, the door must check for the following conditions:

* The door is set up to use keys (UseKey = True).
* The overlapping actor is the player (it implements BPI\_PlayerKeys).
* The player has the required key type.

To test if the actor interacting with the door is the player, follow these steps:

1. In `BP_DoorFrame`’s Event Graph, find the **Event ActorBeginOverlap** node. This collection of nodes controls what happens when a character steps into the door’s collision volume. You’ll add a blueprint interface and key requirement to this logic so the door won’t open unless the actor is the player and they have the right key.

   You can use **Ctrl** + **F** to search for the name of a node. Click on the search result to go directly to it.
2. Disconnect the **Event ActorBeginOverlap** node from the **Door Control** node by holding **Alt** and clicking the wire between the two nodes. Move the **Event** node back so you have space for more node actions before the **Door Control**.

   Disconnect Blueprint Nodes
3. From the **Event ActorBeginOverlap** node, drag its pin and add a **Set Other Actor** node. Connect the **Other Actor** pin of the **Event** node to the **Other Actor** pin of the **Set** node.

   [![Event Actor Begin Overlap Set Other Actor Variable](https://dev.epicgames.com/community/api/documentation/image/0a2dde42-2081-4465-a859-0619fc4d3720?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a2dde42-2081-4465-a859-0619fc4d3720?resizing_type=fit)

   Event Actor Begin Overlap Set Other Actor Variable

   This stores the actor that overlapped with the door area.
4. From the **Set Other Actor** node, drag the blue **Value** pin and create a **Does Object Implement Interface** node. Set the **Interface** value to `BPI_PlayerKeys`.

   [![Does Object Implement Interface Node](https://dev.epicgames.com/community/api/documentation/image/406e3068-e75d-46ef-aa56-97bbc59b3c9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/406e3068-e75d-46ef-aa56-97bbc59b3c9a?resizing_type=fit)

   Does Object Implement Interface Node
5. From the **Set Other Actor** node, drag the **Exec** pin and create a new **Branch** node.

To check that the door uses keys, follow these steps:

1. Drag the **True** pin of the **Branch** node and create an **Fn Has Key** node, which is the function that you created earlier in this tutorial. It takes the key type required to open the door and checks the player’s **Held Keys** array for that key type. Calling this function here will execute the nodes in it.
2. From the **Fn Has Key** node, drag the **Exec** pin and create a new **Branch** node.
3. Connect the **Key Found** pin of the **Fn Has Key** node to the **Condition** pin of the **Branch** node.
4. Connect the new **Branch** node’s **True** pin to the **Door Control** node’s **Play** pin.

   [![Door Control Node](https://dev.epicgames.com/community/api/documentation/image/d51c5428-94ec-4723-a357-251eeb40e35f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d51c5428-94ec-4723-a357-251eeb40e35f?resizing_type=fit)

   Door Control Node

So far, this logic only allows the door to open when the player has the right key. The door should also open when:

* The door doesn’t require keys, or
* A non-player character tries to get through the door.

The first **Branch** node and **And** node tests for both of these conditions. If either is **false**, the **Branch** is also **false**.

To ensure the door opens for NPCs and when keys aren’t required, follow these steps:

1. Connect the **False** pin of the first **Branch** node directly to the **Door Control** node’s **Play** pin. You can use connectors by double-clicking on a wire between two nodes to organize your blueprint.

   [![Blueprint Connections Logic](https://dev.epicgames.com/community/api/documentation/image/9f921fc3-8ce3-48e8-aab9-5031a0dbe2c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f921fc3-8ce3-48e8-aab9-5031a0dbe2c5?resizing_type=fit)

   Blueprint Connections Logic
2. **Compile** and **Save** the blueprint.

Now, when the actor does not implement the key interface, or the door does not require keys (**UseKeys** = False), the door still opens.

In this tutorial, we designed the doors to allow NPCs to pass through them. If you’d like your game to work differently, go ahead and try to change the graph yourself.

The new `BP_DoorFrame`  Event Graph logic should look like the following:

[![BP_DoorFrame Event Graph Logic](https://dev.epicgames.com/community/api/documentation/image/cd144c2d-621f-48e8-87c4-0fe02d8bb0bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd144c2d-621f-48e8-87c4-0fe02d8bb0bf?resizing_type=fit)

BP\_DoorFrame Event Graph Logic

## Add Comments to a Blueprint

You can add comment blocks in your blueprints to create visual-only notes that group nodes together and explain what each part of the blueprint does. Comments help you and your team members know at a glance what functionality your nodes are performing and keep your blueprints organized.

When building blueprint logic, first focus on creating the functionality, and then highlight the nodes you have added and add a comment to contain and describe them.

To add a comment in a blueprint, follow these steps:

1. Click the graph to ensure it's the active panel.
2. Press **C** on your keyboard. This adds a comment box.
3. Double-click the text field at the top of the box to enter a comment.
4. To resize the comment, ensure the comment is selected (highlighted with a yellow outline), and drag an edge or corner.
5. To group notes within a comment, drag those nodes inside the bounds of the comment.

You can also select one or multiple nodes and press **C** to add a comment that contains the selected nodes.

Creating Comments in Blueprints

## Test Your Doors

Go back to your level in the **Level Editor**. Use your doors’ Required Key property to set them up with different colors and add a **BP\_Key** for each color.

Now, play the game. If you walk up to the door without picking up a key, the door will not open.

But if you pick up the key, the door opens when you approach it. When you move far enough away, it’ll close automatically.

After picking up one key color, try to open a door that’s a different color. The door should stay closed.

Testing Door Functionality

If you're working with this tutorial's sample level, select the door that leads to **Hallway 2** and change its required key to the blue key. Next, select the door that leads to **Hallway 3** and change its required key to the red key. Make the door to **Hallway 1** yellow.

[![Color Coded Doors and Keys](https://dev.epicgames.com/community/api/documentation/image/077f807d-a855-4788-b653-9ec08eab5506?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/077f807d-a855-4788-b653-9ec08eab5506?resizing_type=fit)

Color Coded Doors and Keys

### Add Feedback with Debug Messages

If you want to check what’s happening in a blueprint during gameplay, you can use **Print String** nodes to display messages on screen. Unreal Engine doesn’t display these messages in a final game.

Try adding a **Print String** node to confirm the type of key the player has picked up.

To display a debug message with Print String nodes, follow these steps:

1. In the `BP_AdventureCharacter` Event Graph, go to the set of nodes that starts with **Event fnBPIAddKey** and adds keys to the **HeldKeys** array.
2. Drag from the **Add** node’s **Exec** pin and add a **Print String** node.
3. The **In String** is the text that appears on-screen. Enter custom text, or connect the **Event** node’s **Key Type** pin to **In String**. This displays the key the player is picking up.

   [![Debug Logic](https://dev.epicgames.com/community/api/documentation/image/431a6198-18c0-47ee-bc29-63fc9bd33acf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/431a6198-18c0-47ee-bc29-63fc9bd33acf?resizing_type=fit)

   Debug Logic
4. **Compile** the blueprint.
5. Play your game again and pick up the keys. You’ll see debug text confirming each key color as you pick them up.
6. When you’re done, go back to the node graph and delete the **Print String** and **Enum to String** nodes. **Compile** and **Save** the blueprint.

If something isn’t working as expected in a blueprint, you can add Print String nodes after calculations, event calls, or function calls to help track what’s happening with values and flow.

You can also open a blueprint while the game is playing, its wires light up to show the logic running in real time. This **Execution Tracing** is a quick way to spot what’s happening alongside your Print String messages.

## Place Pickup Items

So far, you’ve been placing keys on the floor. To make this more interesting and engaging for the player, try introducing a platforming element.

In this tutorial’s sample level, we added some verticality by placing the key in a high place so the player has to jump to the key. Here, there’s a minor risk of falling and having to start over.

[![Level Layout with Functional Keys](https://dev.epicgames.com/community/api/documentation/image/3d00a4d8-f733-40ca-af13-34f558d89984?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d00a4d8-f733-40ca-af13-34f558d89984?resizing_type=fit)

Level Layout with Functional Keys

The player practices jumping on the first and second platforms before they are put to the test with the more difficult final jump to the pillar.

## Try the Sample Level

If you’d like to add the new pieces of the room designed in this part of the tutorial series instead of creating your own, copy the snippets below.

### Start Room’s Blockout

This text snippet contains the ramp, recessed floor, column, and two platform meshes added to create the path to the yellow key.

C++

Starting Room Layout

```
Begin Map
   Begin Level
      Begin Actor Class=/Script/Engine.StaticMeshActor Name=Floor_168 Archetype="/Script/Engine.StaticMeshActor'/Script/Engine.Default__StaticMeshActor'" ExportPath="/Script/Engine.StaticMeshActor'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.Floor_168'"
         Begin Object Class=/Script/Engine.StaticMeshComponent Name="StaticMeshComponent0" Archetype="/Script/Engine.StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.Floor_168.StaticMeshComponent0'"
         End Object
         Begin Object Name="StaticMeshComponent0" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/Designer/Lvl_Adventure.Lvl_Adventure:PersistentLevel.Floor_168.StaticMeshComponent0'"
            StaticMesh="/Script/Engine.StaticMesh'/Engine/MapTemplates/SM_Template_Map_Floor.SM_Template_Map_Floor'"
            bUseDefaultCollision=False
            StaticMeshDerivedDataKey="STATICMESH_34081786561B425A9523C94540EA599D_359a029847e84730ba516769d0f19427Simplygon_5_5_2156_18f808c3cf724e5a994f57de5c83cc4b_680318F3495BDBDEBE4C11B39CD497CE000000000100000001000000000000000000803F0000803F00000000000000000000344203030300000000"
            MaterialStreamingRelativeBoxes(0)=4294901760
```

Expand code  Copy full snippet(132 lines long)

To Start Room’s new blockout shapes, follow these steps:

* In Unreal Editor, remove all keys from **Start Room** so they don’t get lost in the new geometry.
* Click **Copy Full Snippet**.
* In Unreal Editor, ensure the viewport is the active panel (click anywhere in the viewport or **Outliner** and press **Esc**), and then press **Ctrl** + **V.**

  If you moved any of the blockout rooms from the previous part of this tutorial, the new meshes may not appear in the right place. Move them as needed.
* Three floor pieces are covering the new recessed floor. In the viewport, click each and press **Delete**.

  ![Sample Copy Paste Demo](https://dev.epicgames.com/community/api/documentation/image/753d0a8f-d593-4971-82c4-c913743a802b?resizing_type=fit)

  Sample Copy Paste Demo

## Next Up

Your player character can pick up keys, but there’s no feedback to tell them what they have picked up so far. In the next section, you’ll create a heads-up display (HUD) for the player that shows them the keys in their inventory.

* [![Player HUD](https://dev.epicgames.com/community/api/documentation/image/9b754da0-a689-4622-a7a9-9155cfd86535?resizing_type=fit&width=640&height=640)

  Player HUD

  Create a simple heads-up-display (HUD) that updates when the player picks up an item.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-04-player-hud-in-unreal-engine)

* [types](https://dev.epicgames.com/community/search?query=types)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [collision](https://dev.epicgames.com/community/search?query=collision)
* [attributes](https://dev.epicgames.com/community/search?query=attributes)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Add Color Options to the Door](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#addcoloroptionstothedoor)
* [Create Variables for Interacting with the Player and Keys](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#createvariablesforinteractingwiththeplayerandkeys)
* [Build the Key Map Variable](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#buildthekeymapvariable)
* [Add Color-Changing Blueprint Logic](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#addcolor-changingblueprintlogic)
* [Test the Door Colors](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#testthedoorcolors)
* [Build Key-Based Door Logic](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#buildkey-baseddoorlogic)
* [Create a Function That Checks for Keys](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#createafunctionthatchecksforkeys)
* [Lock and Unlock Doors With Keys](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#lockandunlockdoorswithkeys)
* [Add Comments to a Blueprint](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#addcommentstoablueprint)
* [Test Your Doors](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#testyourdoors)
* [Add Feedback with Debug Messages](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#addfeedbackwithdebugmessages)
* [Place Pickup Items](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#placepickupitems)
* [Try the Sample Level](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#trythesamplelevel)
* [Start Room’s Blockout](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#startroom%E2%80%99sblockout)
* [Next Up](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
