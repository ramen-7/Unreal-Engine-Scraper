<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7 -->

# Blueprints Visual Scripting Overview

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Introduction to Blueprints](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine "Introduction to Blueprints")
7. Blueprints Visual Scripting Overview

# Blueprints Visual Scripting Overview

Learn about Unreal Engine's Blueprint Scripting System.

![Blueprints Visual Scripting Overview](https://dev.epicgames.com/community/api/documentation/image/5f742ac9-5625-4620-9573-1554b7c00e39?resizing_type=fill&width=1920&height=335)

 On this page

The **Blueprint Visual Scripting** system in Unreal Engine (often referred to as just “**Blueprints**”) is a visual scripting language that uses a node-based interface to create gameplay functionality without writing code. Similar to a written scripting language, the Blueprints system works with typed data like numbers, booleans, arrays, and structs. Logic flows through execution wires, meaning each node runs only when something explicitly tells it to run.

With Blueprint Classes, you can pair physical components with scripted behavior. For example, a Blueprint could contain a coin static mesh and behavior that makes the player pick up the coin when they touch it.

As with many common scripting languages, you can use the system to define object-oriented classes or objects in the engine. For programmers, Unreal Engine’s C++ implementation includes Blueprint-specific markup so you can create baseline systems that designers can extend.

In this overview, you’ll learn about the different types of blueprint assets and take a tour of a sample Blueprint Class, where you'll modify certain elements of that Blueprint and see how those changes affect those Blueprint actors in the level editor and during gameplay.

## Types of Blueprints

There are different types of Blueprint assets that each have their own role. When you create and save a Blueprint, it becomes an asset file in in your content package.

### Blueprint Class

A **Blueprint Class**, often shortened as **Blueprint**, is an asset that allows content creators to easily add functionality on top of existing gameplay classes. Blueprints are created inside of Unreal Editor visually, instead of by typing code, and saved as assets in a content package. These essentially define a new class or type of Actor which can then be placed into maps as instances that behave like any other type of Actor.

A Blueprint Class is like a recipe that uses components, variables, and Blueprint Visual Scripting to describe the properties and behaviors of objects in your game. You add instances of Blueprint classes to your level.

This is the most common type you’ll be working with is a Blueprint Class, often shortened and referred to as a Blueprint.

Blueprint Classes can be **data-only** when they contain no execution logic and only override variables or components inherited from a parent Blueprint. Data-Only Blueprint Classes open in a compact editor, but convert to a full Blueprint Editor if you add new logic, graphs, or other scripted elements.

Refer to [Class Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine) for additional documentation.

### Level Blueprint

Every level has a **Level Blueprint**. When you create a new level, Unreal Engine automatically creates a Level Blueprint for that level. This type of Blueprint acts as a level-wide global event graph.

Level Blueprints also provide a control mechanism for level streaming and [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) cinematics as well as for binding events to Actors placed within the level.

To open a level's Level Blueprint, use the **Blueprint** menu in the level editor's Main Toolbar.

[![](https://dev.epicgames.com/community/api/documentation/image/b8dccb6c-5d09-420b-a99d-300099711f33?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8dccb6c-5d09-420b-a99d-300099711f33?resizing_type=fit)

Refer to [Level Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine) for additional documentation.

### Blueprint Interface

A **Blueprint Interface** asset is a collection of one or more functions - name only, no implementation - that can be added to other Blueprints. Any Blueprint that has the Interface added is guaranteed to have those functions. The functions of the Interface can be given functionality in each of the Blueprints that added it. This is essentially like the concept of an interface in general programming, which allows multiple different types of Objects to all share and be accessed through a common interface. Put simply, Blueprint Interfaces allow different Blueprints to share and send data to one another.

Blueprint Interfaces can not:

* Add new variables
* Edit graphs
* Add Components

Refer to [Blueprint Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine) and [Interface Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/interface-quick-start-guide-in-unreal-engine) for additional documentation.

### Blueprint Libraries

You can reuse logic by creating functions and macros in "library" assets so they are accessible to all Blueprints in your project.

#### Blueprint Function Library

A Blueprint Function Library is a blueprint asset that stores a collection of reusable functions. These functions are not tied to a specific Blueprint or Actor. Instead, they’re globally accessible across your entire project and can be called from any Blueprint Class. Libraries keep useful functions in one place so you don’t have to copy and paste the same nodes into multiple Blueprints.

Functions in a Blueprint Function Library are **static**, meaning they don't store or remember information between calls, and they don't know information about a specific blueprint instance unless you pass that data in as parameters. Because of this, function libraries are best for general-purpose logic that operates on inputs and returns a result. When functionality depends on an object’s internal variables (like a player’s inventory), it usually belongs in that object’s Blueprint instead of a library.

#### Blueprint Macro Library

A **Blueprint Macro Library** is a container that holds a collection of **Macros** or self-contained graphs that can be placed as nodes in other Blueprints. These can be time-savers as they can store commonly used sequences of nodes complete with inputs and outputs for both execution and data transfer.

Macros are shared among all graphs that reference them, but they are auto-expanded into graphs as if they were a collapsed node during compiling. This means that Blueprint Macro Libraries do not need to be compiled. However, changes to a Macro are only reflected in graphs that reference that Macro when the Blueprint containing those graphs is recompiled.

Refer to [Blueprint Macro Library](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-macro-library-in-unreal-engine) and [Making Macros](https://dev.epicgames.com/documentation/en-us/unreal-engine/making-macros-in-unreal-engine) for additional documentation.

Functions are reusable blocks of logic that take inputs, run once, and can return a result. They are ideal for calculations or checks. Macros are reusable graph layouts that expand directly into the Blueprint where they’re used. They can have multiple execution outputs and are useful for visual flow control.

### Blueprint Utilities

A **Blueprint Utility** (or **Editor Utility**), is an editor-only Blueprint that can be used to perform editor actions or extend editor functionality. These can expose Events with no parameters as buttons in the UI and have the ability to execute any functions exposed to Blueprints and act on the current set of selected Actors in the viewport.

## Tour a Blueprint Class

Before you begin, you’ll need a Unreal Editor project based on the **First Person** or **Third Person** template (any variant).

For help creating a new project in Unreal Engine, see [Create your First Project in Unreal](https://dev.epicgames.com/documentation/en-us/unreal-engine/create-your-first-project-in-unreal-engine)

### Open an Existing Blueprint

You created your project from a template, so there are several blueprints that are already included in your project that you can explore and use. One example of an included Blueprint Class is the Jump Pad Blueprint, which has functionality that boosts the player upwards. You can add instances of this Blueprint anywhere in your level.

To open the Jump Pad Blueprint, follow these steps:

1. In Unreal Engine, click the **Content Drawer** button at the bottom-left corner of the screen. Alternatively, you can hold down **CTRL** and press **Space**.
2. Navigate to the **Content > LevelPrototyping > Interactable > JumpPad** folder.
3. You will see a `BP_JumpPad` asset, which is a Blueprint Class. Double-click the asset to open it in the **Blueprint Editor**.

   [![BP_JumpPad](https://dev.epicgames.com/community/api/documentation/image/701373b2-6062-4716-98cc-547a3dbec934?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/701373b2-6062-4716-98cc-547a3dbec934?resizing_type=fit)
4. By default, the blueprint opens in a new window. You can dock a window by dragging the tab with the asset’s name next to the level’s tab in the main editor.

In the Blueprint Editor, you can define Components, perform setup operations, respond to events, organize and modularize operations, define properties, and more. Visuals and functionality you add to the Blueprint applies to all instances of that Blueprint that are in your game.

Let’s take a look at `BP_JumpPad`. At the top portion of the window, you can see three tabs: **Viewport**, **EventGraph**, and **Construction** **Script**.

[![Blueprint Editor](https://dev.epicgames.com/community/api/documentation/image/2f7145a6-4b61-4f94-b9f2-74db5f48b259?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f7145a6-4b61-4f94-b9f2-74db5f48b259?resizing_type=fit)

### Build a Level Object With Components

Click the **Viewport** tab. Similar to using the viewport in the main level editor, you use a Blueprint’s **Viewport** to see and edit a Blueprint.

In this tab, you'll see the jump pad’s visual representation which includes a platform, light, and particle effect.

On the left side of the window, you'll also see the Blueprint’s **Components**, or the pieces that define what the Blueprint is made from and what appears in your level. Use the **Components** panel to add, remove, and reorganize the Blueprint’s components.

[![Components Panel and Viewport of BP_JumpPad](https://dev.epicgames.com/community/api/documentation/image/416d3a3b-81c5-46ed-ac35-b51ae927fa97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/416d3a3b-81c5-46ed-ac35-b51ae927fa97?resizing_type=fit)

The building blocks you can add to your Blueprint with components includes:

* Collision geometry with Capsule Collision, Box Collision, or Sphere Collision components.
* Rendered geometry in the form of Static Mesh Components or Skeletal Mesh Components.
* Movement controls with Movement Components.

You can create a Blueprint that only contains components and no scripted behavior, acting as a reusable level object that can be edited in one place.

You can also reference your Blueprint's components or their properties in the EventGraph, so you can perform actions on those components during runtime.

Let’s take a closer look at the components that are part of `BP_JumpPad`:

[![](https://dev.epicgames.com/community/api/documentation/image/a03f39d8-0f4e-4fa6-8449-f8c52561da55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a03f39d8-0f4e-4fa6-8449-f8c52561da55?resizing_type=fit)

`BP_JumpPad` has a **Point Light** component. Click the **Point Light** object in the **Components** list or **Viewport**. You can use the **Transform** tools to move and rotate this light source.

On the right side of the Blueprint Editor, you will see the **Details** panel, which lists the properties related to the selected component. You can edit the **Intensity** of this light source, the **Light Color**, and more.

[![Details Panel of BP_JumpPad](https://dev.epicgames.com/community/api/documentation/image/04aab6e0-3f19-4900-84db-00dd0d7914ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04aab6e0-3f19-4900-84db-00dd0d7914ac?resizing_type=fit)

### Create Blueprint Functionality

Next to the **Viewport** tab, you can see the **EventGraph** and **Construction Script** tabs. If you create any functions in your Blueprint, the tabs for those function graphs appear here as well.

Graphs contain the design-time and game-time behavior and functionality of your Blueprints. Here, you’ll create the logic that tells the Blueprint’s components how to behave.

**Logic** refers to a Blueprint's nodes and connections.

#### Construction Script

When a Blueprint actor spawns in the level, either in the level editor viewport or during gameplay, Unreal Engine builds its components first and then executes its **Construction Script** to . It also executes in the editor when you transform or change a property of an actor, so you see the result immediately in the viewport. It's used to perform initialization actions that set up the Blueprint actor for gameplay. These initialization actions can be context-specific; for example, applying different materials to an object depending on what type of ground it's placed on.

If you click `BP_JumpPad`'s **Construction Script** tab, you will see a **Construction Script** node that executes a chain of actions that set up the jump pad’s color and other properties when it first appears (or spawns) in the level.

[![BP_JumpPad Construction](https://dev.epicgames.com/community/api/documentation/image/9d432044-7dee-4cd2-a0db-7413524ab4d1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d432044-7dee-4cd2-a0db-7413524ab4d1?resizing_type=fit)

Navigating Blueprint graphs:

* **Pan:** Right-click and drag.
* **Zoom:** Use the mouse wheel.
* **Frame selection:** Press **F** to center on selected nodes.
* **Fit all:** Press **A** to view the entire graph.
* J**ump to:** Double-click a function or event node to find it in a graph or its graph tab.

#### Event Graph

The **Event Graph** of a Blueprint contains a node graph that uses events and function calls to perform actions in response to gameplay events. This is where interactivity and dynamic responses are set up. For example, a light Blueprint could respond to a damage event by turning off its Light component and changing a material.

All logic in the Event Graph is a response to something happening during gameplay, such as responding to player input, triggering animations, or playing sounds. Any time you think, “when this happens, I want to do that,” you need to start with an **event**.

A Blueprint can contain multiple Event Graphs that all run as part of the same Blueprint. Multiple Event Graphs are used only to organize logic into separate sections and don't affect how the Blueprint behaves.

In the `BP_JumpPad` **EventGraph** tab, you will see a sequence of nodes that get executed when an actor overlaps with this Blueprint, like when the player walks over the jump pad in-game. When this event happens, the Blueprint makes that actor perform a jump move, but with a higher velocity than normal.

[![BP_JumpPad EventGraph](https://dev.epicgames.com/community/api/documentation/image/1fca07ed-b2ee-476e-a30e-a4872c48a90a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1fca07ed-b2ee-476e-a30e-a4872c48a90a?resizing_type=fit)

To find a specific node in a graph, use the **CTRL + F** shortcut in the graph views to search for a node. For example, to take a look at the **Event ActorBeginOverlap** node, use the **CTRL + F** shortcut and type **Event ActorBeginOverlap** in the search field. Select the result to pan the view to that node.

A node that can execute (or run) actions has an **Execution pin**, also known as an **exec** pin, represented by the white triangle on the node. If a node’s exec pin is not connected to another node, the triangle has white outline.

| Connected Nodes | Disconnected Nodes |
| --- | --- |
| [Two Connected Nodes](https://dev.epicgames.com/community/api/documentation/image/d334b796-40f4-494f-8053-468def77812d?resizing_type=fit) | [Two Disconnected Nodes](https://dev.epicgames.com/community/api/documentation/image/5892ac6c-2747-4535-aed3-1804fdc6fafa?resizing_type=fit) |

You’ll notice that the Event node does not have an input exec pin. This is because an Event node runs as soon as the defined event has been triggered in the game world. In this example, when an actor overlaps with `BP_JumpPad`’s actor in-game, this event will trigger.

A node can also have **data pins**. For example, the **Event ActorBeginOverlap** has a pin for **Other Actor**, which is a reference to the level object (actor) that overlaps with the `BP_JumpPad` level object. Data pins pass values between nodes and execution pins control the order in which nodes are executed.

The **Event ActorBeginOverlap** node’s exec pin is connected to the **Cast To Character** node. This means that when an actor in the world, like the player, overlaps with the jump pad actor, this Blueprint will execute the **Cast To Character** node.

Connections between notes are often referred to as **wires**.

If you disconnect the **Event ActorBeginOverlap** node’s **exec** pin from the **Cast To Character** node, but keep the **Other Actor** pin connected, nothing will happen since the exec pins are not connected — meaning that the **Event** node does not trigger the **Cast To Character** node.

To remove a connection, or wire, hold **Alt**and click that wire. Drag from one pin to another to connect a wire.

[![](https://dev.epicgames.com/community/api/documentation/image/c13c2056-3fe9-4114-98dc-de5f57796d43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c13c2056-3fe9-4114-98dc-de5f57796d43?resizing_type=fit)

To reroute a wire, double-click the wire to create a reroute node. Hover over the reroute note so your cursor changes to four arrows, and then drag the reroute node to move it.

To learn more about working with node actions in the Event Graph, see [Placing Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-nodes-in-unreal-engine) and [Connecting Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/connecting-nodes-in-unreal-engine).

#### Variables

**Variables** are properties that either:

* Hold a value, like a distance measurement or the velocity a character can move.
* Reference something in the world, like the static mesh than an actor uses.

You can set up variables to only be accessible to Blueprints, or make them editable in the level editor so designers can easily customize Blueprint instances placed in a level.

In `BP_JumpPad`'s **EventGraph** tab, take a look at the **My Blueprint** panel on the left side of the Blueprint Editor.

[![BP_JumpPad My Blueprint Panel](https://dev.epicgames.com/community/api/documentation/image/5d0d4751-4206-44a3-a0ec-ad0e4730fec6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d0d4751-4206-44a3-a0ec-ad0e4730fec6?resizing_type=fit)

In the **Variables** section, you can see two variables: **Velocity** and **Color Target**.

Click the **Velocity** variable to select it. In the **Details** panel, there various properties related to this variable. At the very bottom of the list, you will see the **Default Value** category, where you can set the **Velocity** variable's value.

[![BP_JumpPad Velocity Default Value](https://dev.epicgames.com/community/api/documentation/image/99c3f9b8-8105-4aa7-96ba-8fe8a96610c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99c3f9b8-8105-4aa7-96ba-8fe8a96610c3?resizing_type=fit)

In this case, **Velocity** is set to **0**, **0**, **800**. This means that the velocity that’s applied to the player is **800** units in the **Z axis**, or **upwards**.

So, the jump pad’s functionality says, “when the player walks over this jump pad, move them **upwards** at **800** cm/second.”

If you look at the jump pad’s variables, you’ll see they have open **Eye** icons next to them. This means that these variables are **public and editable** variables, which makes them editable on all instances of that Blueprint in your level.

[![BP_JumpPad Editable and Public Variables](https://dev.epicgames.com/community/api/documentation/image/e2271533-bfdc-498b-8c7f-6573f3966230?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2271533-bfdc-498b-8c7f-6573f3966230?resizing_type=fit)

You can override an editable variable's default values per-instance from the Level Editor without needing to open and edit the Blueprint.

To see an example of how you can edit variables outside of a Blueprint, follow these steps:

1. Click your level’s tab near the top-left corner of Unreal Editor to go back to the Level Editor.
2. Open the **Content Browser** and, in the **JumpPad** folder, drag the `BP_JumpPad` asset into the level on the ground. Make sure it’s selected.
3. In the **Details** panel, find the category named **Default**. Under this category, you can see the two variables you saw earlier — **Velocity** and **Color Target**. These are visible here since these two variables are set up as editable in the Blueprint (their **eye** icon is open).

   [![Editable variables appearing in the Level Editor](https://dev.epicgames.com/community/api/documentation/image/5389357f-fa0c-4c9c-8417-0fbedd61dea8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5389357f-fa0c-4c9c-8417-0fbedd61dea8?resizing_type=fit)
4. Go back to the `BP_JumpPad` tab. Under the **My Blueprint > Variables** section, click the **Velocity** variable's e**ye** icon to make it not public and not editable. The open eye changes to a closed eye.

   [![](https://dev.epicgames.com/community/api/documentation/image/66052282-eb3c-4c6d-ae58-707829347aff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/66052282-eb3c-4c6d-ae58-707829347aff?resizing_type=fit)
5. To apply your changes, click the **Compile** button in the top-left corner of the Blueprint Editor.

   [![](https://dev.epicgames.com/community/api/documentation/image/164e9728-7667-4987-90c9-906323cd3ed0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/164e9728-7667-4987-90c9-906323cd3ed0?resizing_type=fit)

   Compiling checks your Blueprint for errors and updates it so the latest changes work in your level.
6. Return to the Level Editor, select the **BP\_JumpPad** actor, and look under the **Details > Default** section again. The **Velocity** variable is missing because it’s no longer instance editable.
7. To restore the Blueprints to their original set up, return to the Blueprint Editor and click the eye icon next to the **Velocity** variable again.
8. Click **Compile** and **Save**.

When variables are public and editable, they can also be used by other Blueprints. For example, your level's Level Blueprint could access and use the jump pad's **Color Target** variable to change the pad's color.

For more information about variable types, creating and editing variables, and referencing variables in your Blueprint graphs, see [Blueprint Variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine).

#### Functions

**Functions** are node graphs belonging to a particular Blueprint that can be executed, or called, from another graph within the Blueprint. Functions have a single entry point designated by a node with the name of the function containing a single exec output pin. Calling the function from another graph executes the logic in the function, starting with the **function entry node**.

[![](https://dev.epicgames.com/community/api/documentation/image/e4d71b02-c160-46a1-ae4f-01f07fad629a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4d71b02-c160-46a1-ae4f-01f07fad629a?resizing_type=fit)

When building Blueprint Classes, you may want to reuse some of the Event Graph’s logic in multiple locations or even in other Blueprints. Instead of rebuilding the same logic in many places, you can create a function where you add the nodes, and then call that function from any blueprint.

When you call a function that lives in another blueprint, the function still runs on the blueprint where it was created. The call simply gives you access to that function from outside.

For example, you could create a `HasKey` function in a player character blueprint that takes a required key, compares that key to the player's inventory, and then returns true or false. Then, other blueprints (a door, a chest, a NPC character) could all call that function to check if the player has a certain key before performing some other behavior. Each of these different level objects can reuse the logic in the player character's `HasKey` function without needing to recreate it in their blueprints.

If you find yourself using the same set of nodes more than twice in a graph, consider making it a function or a macro so you can reuse it.

For more information, see [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/functions-in-unreal-engine).

### Add Comments to Blueprint Logic

You can add comments into your blueprints to create visual-only notes that group nodes together and explain what each part of the Blueprint does. Comments help you and your team members know at a glance what functionality your nodes are performing and keep your Blueprints organized.

When building Blueprint logic, first focus on creating the functionality, and then highlight the nodes you have added and add a comment to contain and describe them.

To add a comment in a blueprint, follow these steps:

1. Click the graph to ensure it's the active panel.
2. Press **C** on your keyboard. This adds a comment box.
3. Double-click the text field at the top of the box to enter a comment.
4. To resize the comment, ensure the comment is selected (highlighted with a yellow outline), and drag an edge or corner.
5. To group notes within a comment, drag those nodes inside the bounds of the comment.

You can also select one or multiple nodes and press **C** to add a comment that contains the selected nodes.

You can also change the color of comments to help identify different areas of your graph at a glance.

## Continue Exploring Blueprints

Now that you know the basics, continue learning about Blueprints by exploring the topics or tutorials below.

* [![Blueprints Workflows](https://dev.epicgames.com/community/api/documentation/image/37e5c68b-f856-4939-824a-9eb4921e34c4?resizing_type=fit&width=640&height=640)

  Blueprints Workflows

  The Blueprint Tutorial page provides several short step-by-step guides for working with Blueprints.](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-workflows-in-unreal-engine)

* [![Specialized Blueprint Node Groups](https://dev.epicgames.com/community/api/documentation/image/2125c14e-5c38-4de0-9258-5ff865440462?resizing_type=fit&width=640&height=640)

  Specialized Blueprint Node Groups

  The User Guide is the go-to source to learn the different parts of Blueprints and nodes that are available to use within Blueprint graphs.](https://dev.epicgames.com/documentation/en-us/unreal-engine/specialized-blueprint-visual-scripting-node-groups-in-unreal-engine)



* [![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=640&height=640)

  Design a Puzzle Adventure

  Learn how to design a full level and gameplay loop in this getting started tutorial!](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

* [![Blueprints Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/958201ab-7025-4afc-b577-cb621a268545?resizing_type=fit&width=640&height=640)

  Blueprints Quick Start Guide

  Get up and running by creating your first Blueprint.](https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-start-guide-for-blueprints-visual-scripting-in-unreal-engine)

* [![Blueprint Editor Reference](https://dev.epicgames.com/community/api/documentation/image/6522008c-d13e-46b2-b539-c4c6a16880af?resizing_type=fit&width=640&height=640)

  Blueprint Editor Reference

  The Blueprint Editor Reference page outlines the Blueprint Editor's Interface elements and its basic usage instructions.](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Types of Blueprints](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#typesofblueprints)
* [Blueprint Class](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintclass)
* [Level Blueprint](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#levelblueprint)
* [Blueprint Interface](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintinterface)
* [Blueprint Libraries](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintlibraries)
* [Blueprint Function Library](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintfunctionlibrary)
* [Blueprint Macro Library](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintmacrolibrary)
* [Blueprint Utilities](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintutilities)
* [Tour a Blueprint Class](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#tourablueprintclass)
* [Open an Existing Blueprint](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#openanexistingblueprint)
* [Build a Level Object With Components](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#buildalevelobjectwithcomponents)
* [Create Blueprint Functionality](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#createblueprintfunctionality)
* [Construction Script](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#constructionscript)
* [Event Graph](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#eventgraph)
* [Variables](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#variables)
* [Functions](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#functions)
* [Add Comments to Blueprint Logic](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#addcommentstoblueprintlogic)
* [Continue Exploring Blueprints](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#continueexploringblueprints)

Related documents

[Blueprint Editor Reference

![Blueprint Editor Reference](https://dev.epicgames.com/community/api/documentation/image/ae690bbf-3a1f-47ea-b311-687f4d4eec51?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine)
