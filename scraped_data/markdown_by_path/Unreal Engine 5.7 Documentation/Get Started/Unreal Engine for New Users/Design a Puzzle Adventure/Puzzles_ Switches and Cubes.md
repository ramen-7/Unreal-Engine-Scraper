<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7 -->

# Puzzles: Switches and Cubes

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
8. Puzzles: Switches and Cubes

# Puzzles: Switches and Cubes

In the first part of the platformer puzzle section, use materials, physics, and blueprints to create a switch that’s activated by a cube.

![Puzzles: Switches and Cubes](https://dev.epicgames.com/community/api/documentation/image/0d9aba62-823e-4861-bb54-3384d9397dae?resizing_type=fill&width=1920&height=335)

 On this page

In this tutorial, you’ll create a platforming puzzle by building two common gameplay objects:

* A pressure-plate switch.
* A physics cube that reacts to the player.

You’ll use level design and game mechanics such as **time**, **physics**, and **damage** to adjust the puzzle’s **difficulty** and introduce **consequences** for player actions.

## Before You Begin

This tutorial assumes you already have an understanding of the following topics, which are covered in the previous sections of the [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

* Materials
* Blueprints and variables
* Blueprint Interfaces

You’ll need the following assets created in [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine).

* `M_BasicColor_Blue`

## An Approach to Gameplay Design

Regardless of genre, compelling gameplay makes players feel something; the excitement of player-versus-player or the comfort of a farming simulator. That emotional response contributes to player engagement. If a game isn’t engaging, players are less likely to continue playing — which can impact your project’s success.

As a game designer, it’s your job to engineer gameplay through level design and game mechanics. You can design a level intuitively but, for the purpose of this tutorial, let’s use formulas to visualize the process.

### Level Design

Through level design, you can increase or decrease the **difficulty** of a task. For example, in a platformer, jumping onto a platform is a task. If you place a platform at the upper limit of a character’s jump distance, you’re increasing how difficult it is to reach the platform and complete the task.

However, if there are no **consequences** for failing, even a high-difficulty task will likely make the player feel safe.

[![Player-investment-based-on-feeling-safe-with-no-consequences](https://dev.epicgames.com/community/api/documentation/image/da92d19d-43cf-4f3e-ab0e-a2143163466c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da92d19d-43cf-4f3e-ab0e-a2143163466c?resizing_type=fit)

A feeling of safety is useful in tutorial sections of gameplay, where the player can learn controls without consequences.

However, a constant feeling of safety may not be useful for your game. For example, without tension, a boss fight might feel boring, resulting in a lack of player engagement.

To make the player feel *tense*, you could introduce consequences by using the game mechanic **damage**.

### Game Mechanics

**Damage** numerically represents the player’s chances of losing something valuable, such as:

* Equipment
* Powerups
* Level progress
* A playable character or non-playable companion.

The difficulty of the task combined with the severity of the consequences can impact how much tension the player feels:

[![Expected-player-response-to-game-consequences](https://dev.epicgames.com/community/api/documentation/image/90a112e7-70c6-464a-b1b1-848c1c1cf74f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90a112e7-70c6-464a-b1b1-848c1c1cf74f?resizing_type=fit)

Unnecessarily difficult tasks with low consequences or payoff can cause player *frustration*.

The amount of tension when performing a task can impact the amount of satisfaction the player feels when they meet a win condition. Satisfaction, especially when combined with a reward, creates motivation to continue playing.

[![Emotional-progression-path-chart-during-gameplay](https://dev.epicgames.com/community/api/documentation/image/27f5f4f2-c37f-493d-9bec-bac693c02110?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27f5f4f2-c37f-493d-9bec-bac693c02110?resizing_type=fit)

A **win condition** is a condition that the player must meet to successfully complete a task.

## Create a Switch

![Video-of-cube-dropping-onto-a-platform-that-changes-color](https://dev.epicgames.com/community/api/documentation/image/791c9297-8557-439f-bb5e-9a538311e893?resizing_type=fit)

A **switch** is a gameplay object that produces an effect when something interacts with it.

By learning how to create a switch, you can design gameplay functionality such as pressing a button to open a door. In this case, you’ll use the switch to change color on collisions with in-game actors.

### Build with Logic

kkYour switch will activate when an object or player overlaps it. Before you begin building, let’s draft the logic that powers this interaction by answering the questions: *what* needs to happen to *who* — and *when*?

Here’s a breakdown of the switch’s logic:

* At runtime, the switch is off.
* If a player steps on the switch, then the switch turns on.
* If a player steps off the switch, then the switch turns off.

Since the switch has two states (**on** and **off**), you can use materials to visualize each state at runtime. During testing, this will quickly verify that the logic is working correctly.

### Create Materials

For the switch’s off state, you'll use `M_BasicColor_Blue` and for the on state you’ll create an **emissive** material.

An emissive material emits light.

  To create the emissive material, follow these steps:

1. In the **Content Browser**, at **AdventureGame > Designer > Materials**, right-click and select **Material**.

   [![Right-click-menu-in-content-drawer-showing-material-selected](https://dev.epicgames.com/community/api/documentation/image/d67f787c-afc2-404b-bf02-b328dcb5a9aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d67f787c-afc2-404b-bf02-b328dcb5a9aa?resizing_type=fit)
2. Name the new material `M_EmissiveColor` and double-click it to open the Material Editor.
3. In the **Material Graph**, right-click and search for **Vector Parameter**. Click it to populate it to the graph and name it `Color`. This controls the color of the material’s light.

   [![Emissive-color-emitter-in-blueprints](https://dev.epicgames.com/community/api/documentation/image/f20f9883-cfec-4bfe-9fe2-65ea312fac77?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f20f9883-cfec-4bfe-9fe2-65ea312fac77?resizing_type=fit)
4. On the **Color** node, click the color swatch to open the **Color Picker**.
5. Choose your own color or set it to **Hex sRGB** `27F774FF` to follow along.

   [![Color-picker-chart-with-hex-color-shown](https://dev.epicgames.com/community/api/documentation/image/6fe0f0fd-1a70-46b5-b701-599fbdd31051?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6fe0f0fd-1a70-46b5-b701-599fbdd31051?resizing_type=fit)
6. Right-click and search for two more nodes: a **constant** and a **multiply** node.
7. Connect the **Color** node to the **A** pin of the **Multiply** node. Then, connect the **C****onstant** to the **B** pin of the **Multiply** node. Finally, connect the **Multiply** node to the **Emissive Color** pin of the **M\_EmissiveColor** node.

   [![In-Blueprints-the-color-node-flowing-to-emissive-color-node](https://dev.epicgames.com/community/api/documentation/image/6e016257-920b-4855-8c89-a6226ae4a14b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e016257-920b-4855-8c89-a6226ae4a14b?resizing_type=fit)
8. The **Value** of the constant controls the material’s emissive power or brightness. Adjust it as preferred or set it to `25` to follow along.

   [![Emissive-color-node-with-details-panel](https://dev.epicgames.com/community/api/documentation/image/5b501530-79e0-4740-9b77-a3662df6dadb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b501530-79e0-4740-9b77-a3662df6dadb?resizing_type=fit)
9. **Save** and close the material.

Your Materials folder should now look like this:

[![A-collection-of-basic-colors-in-the-content-drawer-materials-folder](https://dev.epicgames.com/community/api/documentation/image/075d906d-d001-480d-adad-f71032df091b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/075d906d-d001-480d-adad-f71032df091b?resizing_type=fit)

Because `M_EmissiveColor` is the only emissive material in this tutorial, you don’t need to create any instances. However, material instances are an elegant way of keeping your project modular and working efficiently in a development environment.

Next, you’ll build the switch.

### Set Up a Blueprint Class

The switch will be a Blueprint that consists of a static mesh and a box collision. The box collision will detect contact with the player, which triggers the switch’s on and off states.

[Collision](https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview) is the detection of two objects coming into contact at runtime. Box collisions, along with sphere and capsule collisions, are volumes used to make these detections. For example, hitboxes are an example of using collision shapes to detect a successful attack.

To begin, follow these steps:

1. In the **Content Browser**, at **AdventureGame > Designer > Blueprints**, create a new folder called `Activation`.
2. Inside Activation, right-click to create a new **Blueprint Class**.

   [![Right-click-menu-selecting-blueprint-class](https://dev.epicgames.com/community/api/documentation/image/e9e11058-e392-4f67-8530-a2a1e90f0695?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9e11058-e392-4f67-8530-a2a1e90f0695?resizing_type=fit)
3. In the **Pick Parent Class** dialog, select **Actor**.

   [![Pick-parent-class-dialog-box](https://dev.epicgames.com/community/api/documentation/image/1b0f9eaa-d94e-48db-9b01-13c9720c1110?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b0f9eaa-d94e-48db-9b01-13c9720c1110?resizing_type=fit)
4. Name the new Blueprint `BP_Switch` and double-click it to open `BP_Switch` in the Blueprint Editor.
5. In the **Components** tab, create a static mesh by clicking **Add**, search for `cube`, and select it.
6. Name the cube `Switch`.

   [![Viewport-with-switch-cube](https://dev.epicgames.com/community/api/documentation/image/6e907933-ff6e-42bc-93b1-069ec086e0ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e907933-ff6e-42bc-93b1-069ec086e0ab?resizing_type=fit)
7. In the **Details** panel, under **Transform**, adjust **Switch**’s scale to `2.0`, `2.0`, `0.1`.

   [![Details-panel-showing-scale-settings](https://dev.epicgames.com/community/api/documentation/image/20612e9e-7211-46ce-ab42-7c89b4e34849?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20612e9e-7211-46ce-ab42-7c89b4e34849?resizing_type=fit)
8. In the **Components** tab, with **Switch** selected, create a box collision by clicking **Add** and search for `box collision`.
9. Name it `Trigger`.

   [![Trigger-component-inside-of-platform-but-taller-than-platform](https://dev.epicgames.com/community/api/documentation/image/1f2b351c-7574-465d-ba8b-7496d8e12304?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1f2b351c-7574-465d-ba8b-7496d8e12304?resizing_type=fit)
10. In the **Details** panel, under **Location**, adjust the box collision’s **Z** value to `200`.
11. Under **Scale**, adjust its scale  to `1.5`, `1.5`, `5.0`. This box collision is thicker than the static mesh to easily capture collisions.

    [![Scale-inputs-for-the-trigger-component](https://dev.epicgames.com/community/api/documentation/image/36000fc5-048d-461f-8146-1d4145d7d4c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36000fc5-048d-461f-8146-1d4145d7d4c3?resizing_type=fit)
12. **Save** and **Compile** the Blueprint.

Your Blueprints folder should now look like this:

[![Five-folders-in-the-blueprints-folder](https://dev.epicgames.com/community/api/documentation/image/fa93d93a-497e-449c-91cc-27e246ed8926?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa93d93a-497e-449c-91cc-27e246ed8926?resizing_type=fit)

To avoid losing work if compiling fails, **Save** and then **Compile** a Blueprint after any significant change.

Next, you’ll create variables to control the switch’s behavior.

### Create Variables

Through variables, `BP_Switch` can reference the material that you just created. Instead of hardcoding a particular material into the switch, you can swap out materials on the fly — which you’ll do later in this tutorial.

To create the on and off materials, follow these steps:

1. In the **MyBlueprint** tab, under **Variables**, create two new variables by clicking the **+** button twice.
2. Name one `OnMaterial` and the other `OffMaterial`.
3. Set their pin type to **Material Interface (Object Reference)**.

   [![Adding-variables-in-the-my-blueprint-tab](https://dev.epicgames.com/community/api/documentation/image/3ccee58e-1356-41ba-a7fa-0bfa841781ef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ccee58e-1356-41ba-a7fa-0bfa841781ef?resizing_type=fit)

   A Material Interface variable can reference a Material or a Material Instance.
4. Select **OnMaterial**. In the **Details** panel, next to **Category**, create a new category called `Setup`.
5. Click **Compile** to get access to its **Default Value**. Under **Default Value**, select `M_EmissiveColor`. This variable is done for now.

   [![On-material-shown-for-emissive-color](https://dev.epicgames.com/community/api/documentation/image/a56e8a37-89bf-4071-b11c-af8119754769?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a56e8a37-89bf-4071-b11c-af8119754769?resizing_type=fit)
6. Select **OffMaterial**. In the **Details** panel, add it to the **Setup** category.

   [![](https://dev.epicgames.com/community/api/documentation/image/41727325-b62b-47be-b9de-0e147078e15d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41727325-b62b-47be-b9de-0e147078e15d?resizing_type=fit)
7. Under **Default Value**, select `M_BasicColor_Blue`.
8. **Save** and **Compile**.

Now that the Blueprint can reference the materials, you’ll use logic to instruct the switch when to use them.

### Implement Your Logic

You should have a box collision, a static mesh, and two materials. Now the switch’s logic can be written as:

* At runtime, **Switch** should display **OffMaterial**.
* If **Trigger** detects a collision, then set **Switch**’s material to **OnMaterial**.
* If **Trigger** stops detecting a collision, then set **Switch**’s material to **OffMaterial**.

To build this logic, you’ll use a construction script to instruct `BP_Switch` to use **OffMaterial** at runtime:

1. In the **Construction Script** tab, drag off the **Exec** pin on the Construction Script node and search for **Set Material (Switch)**. Click to create it.

   [![Construction-script-node-and-set-material-node](https://dev.epicgames.com/community/api/documentation/image/973e751c-5fde-4722-b400-912bafc51636?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/973e751c-5fde-4722-b400-912bafc51636?resizing_type=fit)
2. On the **Set Material** node, drag off the **Material** pin and search for **Get OffMaterial**. Select it.

   [![Set-material-node-connecting-to-off-material-node](https://dev.epicgames.com/community/api/documentation/image/265cdc9d-9436-481f-be9f-0ee17f7a32d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/265cdc9d-9436-481f-be9f-0ee17f7a32d3?resizing_type=fit)
3. **Save** and **Compile**.

You’ll handle the remaining logic in the **EventGraph**. To instruct the switch to turn on and off upon overlap, follow the steps below:

1. In the EventGraph, delete the **Event BeginPlay**, **Event ActorBeginOverlap**, and **Event Tick** nodes. You won't need them.
2. In the **My Blueprint** tab, under the **Components** heading, right-click on **Trigger** and select **Add Event > Add OnComponentBeginOverla****p**.

   [![File-path-for-trigger-add-event-to add-on-component](https://dev.epicgames.com/community/api/documentation/image/2fd84c87-b634-40b4-9797-95d73d2b18a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2fd84c87-b634-40b4-9797-95d73d2b18a5?resizing_type=fit)
3. Repeat this process to add an **OnComponentEndOverlap** node as well.

   [![Image-of-the-on-component-end-overlap-node](https://dev.epicgames.com/community/api/documentation/image/d2641d11-5ff9-42a7-98f0-8314d393b5a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2641d11-5ff9-42a7-98f0-8314d393b5a5?resizing_type=fit)
4. From the **Exec** pin of the **OnComponentBeginOverlap(Trigger)** node, drag and search for **Set Material (Switch)**.

   [![Image-of-the-blueprint-with-the-set-material-node](https://dev.epicgames.com/community/api/documentation/image/15ee9b38-624c-4294-9c75-d001277d8a76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/15ee9b38-624c-4294-9c75-d001277d8a76?resizing_type=fit)
5. From the **Material** pin of the **Set Material** node, drag and search for **Get OnMaterial**.

   [![Image-showing-the-get-on-material-node](https://dev.epicgames.com/community/api/documentation/image/67e1b62b-2562-4610-af6d-f4d997440983?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67e1b62b-2562-4610-af6d-f4d997440983?resizing_type=fit)
6. From the **Exec** pin of the **OnComponentEndOverlap(Trigger)** node, drag and search for **Set Material (Switch**).
7. From the **Material** pin of the **Set Material** node, drag and search for **Get OffMaterial**.
8. Your switch is done for now, **Save** and **Compile**.

Your **Construction Script** graph should now look like this:

Blueprint

Construction Script

Copy full snippet(32 lines long)

Your **EventGraph** should now look like this:

Blueprint

EventGraph Code

Copy full snippet(88 lines long)

Now you can test your project to see if your switch functions correctly.

Drag an instance of `BP_Switch` from the **Content Browser** into **Room 1**. Click the three-dot menu in the **Playmode** toolbar, and select **Current Camera Location**. This ensures you enter PIE mode from your current location in the viewport, instead of running through the entire level to test one feature.

[![Menu-showing-current-camera-option-under-spawn-player-at-section](https://dev.epicgames.com/community/api/documentation/image/e4deea71-465f-4918-b6e1-8ef553707298?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4deea71-465f-4918-b6e1-8ef553707298?resizing_type=fit)

In PIE mode, when you step onto the switch, it should light up. When you step off, it should return to blue.

![PIE-clip-of-player-stepping-on-platform-that-lights-up](https://dev.epicgames.com/community/api/documentation/image/82ee7a2b-3b5e-4832-b9f4-95516520b44b?resizing_type=fit)

### The Benefit of Modular Development

Let’s say you want two switches instead of one, but you want the second switch to light up red instead of green. You could build a new switch with the same logic and assign a red material, but that would cost you development time and create more overhead for your project.

**Overhead** refers to the expenditure of resources (processing power, time, storage amounts, and so on).

Since **platforms** (computers and consoles) have finite processing power, game developers usually want to work modularly to reduce overhead.

Because you’ve used Blueprints and variables to build your switch, you’re already working modularly. Let’s see your work in action:

1. Open `BP_Switch` in the **Blueprint Editor** by double-clicking it in the **Content Browser**.
2. Under **Variables**, select **OnMaterial** and click the **eye** icon so that it’s open.

   [![Off-material-with-eye-icon-closed-or-off](https://dev.epicgames.com/community/api/documentation/image/0d8b36c2-1313-4d93-b520-5888b60a84a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d8b36c2-1313-4d93-b520-5888b60a84a6?resizing_type=fit)
3. Select **OffMaterial** and we’ll do the same thing in a different way; in the **Details** panel enable **Instance Editable**. You’ll notice that the eye icon opens; it’s now a public and editable variable.

   [![Material-interface-as-instance-editable](https://dev.epicgames.com/community/api/documentation/image/c0c73e3e-292f-4a93-9112-33a6107f8814?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0c73e3e-292f-4a93-9112-33a6107f8814?resizing_type=fit)
4. **Save**, **Compile**, and close it.

You should already have one instance of `BP_Switch` in the level, so drag in a second instance. With either switch selected in the viewport, the **Details** panel has a new UI category called **Setup**. **Setup** displays your public and editable variables as parameters that you can change on the fly from the viewport.

Try changing the materials to anything you want and testing how the switches react in PIE mode. You’ll notice that each instance of your switch can hold unique On and Off materials without creating new switches from scratch — speeding up your development and reducing overhead.

![Gif-clip-of-changing-instance-color-from-blue-to-red](https://dev.epicgames.com/community/api/documentation/image/3861de3e-1a0c-4b6e-a35d-5cb6711de935?resizing_type=fit)

If you want your viewport to look exactly like ours, delete the second instance of your switch before you proceed with this tutorial.

### Create Single and Multiple Activations

Your switch currently turns on and off indefinitely. In certain cases, it’s valuable to only activate it once. For example, in a hallway that leads to loot, you might want a switch to activate a trap that the player must avoid. If the player successfully avoids the trap and collects the loot, the switch should not activate the trap again.

Rather than discard what you’ve built already, you’ll add a **boolean** to permit only one use of your switch.

To do this, follow these steps:

1. In the Blueprint Editor for `BP_Switch`, under **Variables**, click the **+** button to add a new variable.
2. Name it `ActivateOnce` and set the pin type to **Boolean**.
3. In the **Details** panel, check the **Instance Editable** box.
4. Click the dropdown menu next to **Category** and select **Setup**.
5. Click **Compile** to access the variable’s **Default Value** and verify that it is unchecked. This means that **ActivateOnce** will not be on by default for this Blueprint.

   [![Variable-type-showing-boolean-option](https://dev.epicgames.com/community/api/documentation/image/87707d25-e54e-4295-9553-f8cb9921ea3f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87707d25-e54e-4295-9553-f8cb9921ea3f?resizing_type=fit)
6. In the EventGraph, right-click and search for a **Branch** node.
7. From the **Condition** pin on the **Branch** node, drag out and search for **Get ActivateOnce**.

   [![In-blueprints-the branch-node-connected-to-activate-once](https://dev.epicgames.com/community/api/documentation/image/a822ddd9-33e2-47ec-92ac-cac28bc37532?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a822ddd9-33e2-47ec-92ac-cac28bc37532?resizing_type=fit)
8. Drag the **Exec** pin of the **On Component End Overlap (Trigger)** node to the **Exec** pin of the **Branch** node. It should disconnect from the SetMaterial node.

   ![GIF-of-on-component-connecting-to-branch-node](https://dev.epicgames.com/community/api/documentation/image/3e3b8c9d-5b66-4979-88a3-31b27205b889?resizing_type=fit)
9. Connect the **False** pin of the **Branch** node to the **Exec** pin of the **Set Material** node. This means that when the object moves off of the switch, a decision is made: if **ActivateOnce** is **True**, the switch stops detecting collision. If **ActivateOnce** is **False**, the switch works indefinitely.

   [![Blueprint-of-the-final-event-graph](https://dev.epicgames.com/community/api/documentation/image/f98a28c5-c188-476c-a917-ad02de360402?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f98a28c5-c188-476c-a917-ad02de360402?resizing_type=fit)
10. **Save**, **Compile**, and close the Blueprint.
11. Select `BP_Switch` in the viewport. In the Details panel, **ActivateOnce** should be an toggleable checkbox for this instance. Enable it to see how it works.

    [![Final-details-panel-settings-with-viewport](https://dev.epicgames.com/community/api/documentation/image/43e3d930-a058-41dd-bd48-653ec471501c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43e3d930-a058-41dd-bd48-653ec471501c?resizing_type=fit)

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(105 lines long)

Click **Play** to test your variable in game. With **ActivateOnce** enabled, the switch should stay lit even after walking off of it.

![GIF-clip-of-player-stepping-on-platform-and-it-changes-color](https://dev.epicgames.com/community/api/documentation/image/ca55a9cb-ccf2-4a7b-ba5a-e89ce12e3a26?resizing_type=fit)

## Activate Switches with Physics

Later in this tutorial, your player will need to hold the switch down while they navigate the rest of the level. For this purpose, you’ll create the second gameplay object of this puzzle; the physics cube. This incorporates the game mechanic, **physics**, into the puzzle you design.

To create a physics cube using Blueprints, follow these steps:

1. In the **Content Browser**, navigate to **AdventureGame > Designer > Blueprints > Activation**, right-click and create a new **Blueprint Class**.
2. In the **Pick Parent Class** dialog, select **Actor**.
3. Name the new Blueprint `BP_Cube`.
4. Double-click it to open `BP_Cube` in the Blueprint Editor.
5. In the **Components** tab, create a static mesh by clicking **Add**, search for `cube`, and select it.
6. Name the mesh `Cube`.

   [![Viewport-with-the-cube-component-selected](https://dev.epicgames.com/community/api/documentation/image/51963adb-9f4a-403b-ad68-c236600e6f28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51963adb-9f4a-403b-ad68-c236600e6f28?resizing_type=fit)
7. In the **Details** panel, under **Static Mesh**, search for and select **SM\_ChamferCube**.

   [![Detials-panel-showing-sm-chamfer-cube-option](https://dev.epicgames.com/community/api/documentation/image/2321606c-51f4-42a6-9de8-01bedaa41488?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2321606c-51f4-42a6-9de8-01bedaa41488?resizing_type=fit)
8. Under **Transform**, set the Location property's **Z** value to `50.0`.
9. Under **Materials**, set **Element 0** to `M_BasicColor_Blue`.

   [![Details-panel-open-with-m-basic-color-blue-selected](https://dev.epicgames.com/community/api/documentation/image/3c4a21cc-4317-43fb-8c02-e8492ac3b019?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c4a21cc-4317-43fb-8c02-e8492ac3b019?resizing_type=fit)
10. Under **Physics**, enable **Simulate Physics**. This setting enables the use of UE’s [Chaos Physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine) Engine, letting the cube react to the player’s pushing.

    [![Details-tab-with-enable-physics-checkbox-selected](https://dev.epicgames.com/community/api/documentation/image/c27cb22e-c8ea-4dde-93aa-4d8dd3ecf430?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c27cb22e-c8ea-4dde-93aa-4d8dd3ecf430?resizing_type=fit)
11. **Save** and **Compile**.

To test functionality, drag an instance of `BP_Cube` into your level, near your switch. Press **Play** to enter PIE mode and use **WASD** letter keys to push `BP_Cube` onto a switch to turn it on.

![GIF-clip-of-player-pushing-a-cube-onto-the-platform-with-a-color-change](https://dev.epicgames.com/community/api/documentation/image/a4b38b6b-82e2-49e3-b966-ce0f6bb9b9f6?resizing_type=fit)

### Debug

If you push the cube onto the switch, it turns on, but you might notice a problem. If you walk off the switch, the switch turns off even if the cube is still overlapping it.

![GIF-clip-showing-player-steps-off-platform-which-turns-off-with-cube-on-still](https://dev.epicgames.com/community/api/documentation/image/7c3625fb-f719-466b-a533-50b601b1e9ff?resizing_type=fit)

Look at the current logic to find the error:

* If Trigger stops detecting a collision, then set Switch’s material to OffMaterial.

The switch turns off when **Trigger** stops detecting any collision, even if there is still one actor overlapping it. To solve this problem, instruct **Trigger** to check for any overlapping actors before proceeding:

* If Trigger stops detecting a collision, and if there are no actors overlapping it, then set Switch’s material to OffMaterial.

To make this adjustment to your Blueprints, follow these steps:

1. In the Blueprint Editor for `BP_Switch`, right-click and create a **Branch** node.
2. Drag off the **Condition** pin, search for and create an **Is Empty (Array)** node.

   [![Blueprint-showing-is-empty-node](https://dev.epicgames.com/community/api/documentation/image/b6a96940-4ee9-4ec8-8aef-433bd3e53364?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b6a96940-4ee9-4ec8-8aef-433bd3e53364?resizing_type=fit)
3. From the **Target Array** pin of the **Is Empty** node, search for and create **Get Overlapping Actors (Trigger)**.
4. Set the **Class Filter** to **Actor**.

   [![Setting-the-class-filter-to-actor](https://dev.epicgames.com/community/api/documentation/image/50cb7ea6-502e-405b-8201-a833d814615c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50cb7ea6-502e-405b-8201-a833d814615c?resizing_type=fit)
5. Connect this logic to the existing nodes by dragging from the **False** pin of the first **Branch** node and connect it to the **Exec** pin of the second **Branch** node.
6. Connect the **True** pin on the second **Branch** node to the **Exec** pin of the **Set Material** node.
7. **Save** and **Compile**.

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(142 lines long)

To adjust **Trigger**’s collision settings, follow these steps:

1. In the **Components** tab, select **Trigger**.
2. In the **Details** panel, expand **Collision Presets**. Set the **Collision Presets** dropdown to **Custom**.
3. In the **Collision Enabled** dropdown, select **Collision Enabled (Query and Physics)**.

   This setting enables trace detection and physical collision responses on the **Trigger** box collision, so the box doesn't block anything physically but generates overlap events.
4. In the **Object Type** dropdown, select **WorldDynamic**.

   [![Collision-presets-menu-in-the-details-tab](https://dev.epicgames.com/community/api/documentation/image/b2f519f5-7664-4fc2-a298-db4642172717?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2f519f5-7664-4fc2-a298-db4642172717?resizing_type=fit)

   Use
   WorldDynamic for interactive or moveable actors and gameplay objects.
5. Next to **WorldDynamic**, add a checkmark next to **Ignore**.

   [![](https://dev.epicgames.com/community/api/documentation/image/db913be4-3a3b-4df4-9bb2-9652098254fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db913be4-3a3b-4df4-9bb2-9652098254fd?resizing_type=fit)

   Setting **WorldDynamic** to **Ignore** here ensures other WorldDynamic objects can't physically collide with the collision box.
6. **Save** and **Compile**.

Now, you've set up the switch's collision box to not block anything and not interfere physically with characters or objects, but detect when something steps into the box and triggers and overlap event.

Play the game to test your solution. The switch should stay lit as long as any actor overlaps it, regardless if one moves off.

## Control Other Objects With the Switch

So far, you’ve created a switch that turns on and off. That’s excellent for visualizing if the switch is functioning correctly, but it could be more useful. Next, you’ll use the switch to activate other objects within the level.

First, you’ll create a **Blueprint interface** with two functions; each one representing the on and off state of the switch. These functions are used like events signaled between objects.

To set up a Blueprint Interface with two functions, follow these steps:

1. In the **Content Browser**, navigate to **AdventureGame > Designer > Blueprints > Core**, right-click, and highlight **Blueprint**. Then, select **Blueprint Interface**.

   [![Image-showing-file-path-of-blueprint-to-blueprint-interface](https://dev.epicgames.com/community/api/documentation/image/f34da145-cd0b-4866-a58c-56d14ae83b39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f34da145-cd0b-4866-a58c-56d14ae83b39?resizing_type=fit)
2. Name the interface `BPI_Interaction`. Double-click to open the Blueprint Interface window.

   [![Image-showing-asset-of-bpi-interaction](https://dev.epicgames.com/community/api/documentation/image/e8810ed9-4a19-484d-9aaa-61cf86e35914?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8810ed9-4a19-484d-9aaa-61cf86e35914?resizing_type=fit)
3. In the **MyBlueprint** panel, a new function should already exist. Name it `fnBPISwitchOn`.

   [![Image-showing-fn-bpi-switch-node](https://dev.epicgames.com/community/api/documentation/image/efe3e98d-693e-4282-9745-fe2c2d12fb56?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efe3e98d-693e-4282-9745-fe2c2d12fb56?resizing_type=fit)
4. Click **Add**, and then function to create a second function. Name it `fnBPISwitchOff`.
5. Your interface is complete. 
   Save, **Compile**, and close it.

Next, you’ll create an **array** that contains all objects you want the switch to activate. In this tutorial, you’ll use an array to manage which objects your switch activates, rather than creating unique logic for each new object.

To create the array of objects the switch should trigger, follow these steps:

1. In the **My Blueprint** tab of `BP_Switch`, under **Variables**, click the **+** button to create a new variable.
2. Name it `InteractObjectList` and set the pin type to **Actor (Object Reference)**.
3. In the **Details** panel, next to **Variable Type**, set the container type to **Array**.

   [![Dropdown-menu-of-actor-types](https://dev.epicgames.com/community/api/documentation/image/6ff0941a-e4d9-471b-a7d2-dd85899ea1a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6ff0941a-e4d9-471b-a7d2-dd85899ea1a6?resizing_type=fit)
4. To make it a UI parameter, check **Instance Editabl****e** and add it to the **Setup** category.
5. **Save** and **Compile**.

Using logic, you’ll instruct the switch to iterate through each object in the array (which is currently empty) and signal it using the `BPI_Interaction` interface you created earlier. To do this, you’ll use a **For Each Loop**.

To signal all items in the array, follow these steps:

1. In the **EventGraph**, drag out from the **Exec** pin of the **Set Material** node (of the **On Component Begin Overlap** node), and search for **For Each Loop**.

   [![Event-graph-showing-for-each-loop](https://dev.epicgames.com/community/api/documentation/image/420ed955-15b1-4df8-a1b5-8006d8bfbc46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/420ed955-15b1-4df8-a1b5-8006d8bfbc46?resizing_type=fit)
2. To instruct which objects to perform the event for, drag out the **Array** pin on the **For Each Loop** and search for **Get InteractObjectList**.

   [![Showing-blueprint-with-get-interact-object-node](https://dev.epicgames.com/community/api/documentation/image/156fb99b-8e10-4116-84f0-54f7477405dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/156fb99b-8e10-4116-84f0-54f7477405dd?resizing_type=fit)
3. Finally, drag out the **Loop Body** pin on the **For Each Loop** and search for **fnBPISwitchOn**. This is the event you’re calling.

   [![Blueprint-showing-fnBPI-switch-node](https://dev.epicgames.com/community/api/documentation/image/870f8ddb-5a11-4cc5-9a57-d1a6ed60d5ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/870f8ddb-5a11-4cc5-9a57-d1a6ed60d5ab?resizing_type=fit)
4. Connect the **Array Element** pin on the **For Each Loop** to the **Target** pin on the **fnBPISwitchOn** node.

   [![BP-showing-the-array-connected-to-the-target](https://dev.epicgames.com/community/api/documentation/image/9c5881a7-45c0-4306-90c2-aa3ef47e8d39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c5881a7-45c0-4306-90c2-aa3ef47e8d39?resizing_type=fit)
5. The same must be done for **On Component End Overlap (Trigger)**. To speed up the process, select the For Each Loop and Interact Object List node and copy it using **right-click > Copy** or **Ctrl + C**. Press **Ctrl + V** to paste it in the graph.

   ![Showing-clip-of-copy-pasting-nodes](https://dev.epicgames.com/community/api/documentation/image/8c262f3d-4e17-4e3a-be8b-e39223741395?resizing_type=fit)
6. Connect the **Exec** pin of the **Set Material** node to the **Exec** pin of the new **For Each Loop**.
7. From the **Loop Body** pin of the **For Each Loop**, drag out and search for **fnBPISwitchOff**. Connect the **Array Element** pin to the **Target** pin.
8. Your switch is done for now. **Save**, **Compile**, and close it.

Your **EventGraph** should now look like this:

Blueprint

EventGraph Snippet

Copy full snippet(200 lines long)

You’ve now laid the groundwork for activating a unique list of objects in your level when a player overlaps the switch. In the next tutorial, you’ll create the third gameplay object of this challenge — a moving platform.

## Next Up

* [![Puzzles: Moving Platforms](https://dev.epicgames.com/community/api/documentation/image/368c36ed-f258-4eac-87e0-5c3076b944d1?resizing_type=fit&width=640&height=640)

  Puzzles: Moving Platforms

  In the second part of the platformer puzzle, create the moving platforms with blueprints and learn how to debug your script.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [level design](https://dev.epicgames.com/community/search?query=level%20design)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [An Approach to Gameplay Design](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#anapproachtogameplaydesign)
* [Level Design](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#leveldesign)
* [Game Mechanics](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#gamemechanics)
* [Create a Switch](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#createaswitch)
* [Build with Logic](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#buildwithlogic)
* [Create Materials](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#creatematerials)
* [Set Up a Blueprint Class](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#setupablueprintclass)
* [Create Variables](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#create-variables)
* [Implement Your Logic](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#implementyourlogic)
* [The Benefit of Modular Development](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#thebenefitofmodulardevelopment)
* [Create Single and Multiple Activations](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#createsingleandmultipleactivations)
* [Activate Switches with Physics](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#activateswitcheswithphysics)
* [Debug](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#debug)
* [Control Other Objects With the Switch](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#controlotherobjectswiththeswitch)
* [Next Up](/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Puzzles: Moving Platforms

![Puzzles: Moving Platforms](https://dev.epicgames.com/community/api/documentation/image/368c36ed-f258-4eac-87e0-5c3076b944d1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine)

[Collision Overview

![Collision Overview](https://dev.epicgames.com/community/api/documentation/image/4688b209-85a3-46e2-b104-dcf7372c540c?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview)
