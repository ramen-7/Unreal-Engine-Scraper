<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7 -->

# Create an Enemy

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
8. Create an Enemy

# Create an Enemy

Build game logic to create Enemy Characters that deal and receive damage.

![Create an Enemy](https://dev.epicgames.com/community/api/documentation/image/ffac73a1-0f27-4e85-9629-70348c2d5795?resizing_type=fill&width=1920&height=335)

 On this page

In this part of the tutorial, you will create an enemy NPC that detects, chases, and damages the player. In addition, the enemy will be able to receive damage and navigate around the environment to avoid obstacles using a **Navigation Mesh**.

First you will create the enemy logic using Blueprint Visual Scripting as with the previous tutorials. Then, you’ll create the Navigation Mesh to define the zones that **AI Controller**-possessed characters can navigate during gameplay.

## Before You Begin

Make sure you understand these topics covered in the previous section of the [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

* Blueprints and Blueprint Functions

You’ll need the following assets from [Create a Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine):

* `BPL_FPGame` Blueprint Function Library

## Create NavMesh for the Enemy’s Navigation

Before you can add the enemy to a level and make it chase after the player, you have to build the NavMesh that the Enemy AI will use to navigate the level.

NavMesh is short for Navigation Mesh and it defines areas on the level that the AI can navigate within. By creating a NavMesh in this tutorial, you will define a zone in which the enemy can move to chase the player.

To add navigation mesh to your level, follow these steps:

1. In Unreal Editor’s Level Editor, in the **Main Toolbar**, click the **Create** button, go to **Volumes** and select **Nav Mesh Bounds Volume**. This creates a navigable zone for the AI in your project.

   [![](https://dev.epicgames.com/community/api/documentation/image/9644f0ce-1014-42ee-bee8-895200757569?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9644f0ce-1014-42ee-bee8-895200757569?resizing_type=fit)
2. Using the **Transform** tools, move the NavMesh to intersect with the floor in your level.
3. Press **P** on your keyboard to toggle the debug view. Use this to view the NavMesh details in the level viewport — including the navigable zones on the level, as well as text-based debug information on the left-hand side of the viewport.

   If you see a “NavMesh Needs To Be Rebuilt” message in the debug info, navigate in the **Menu Bar** to **Build > Build Paths**. This rebuilds your NavMesh.
4. Continue to move and scale (**W** and **R** keys on your keyboard) the NavMesh to modify the NavMesh bounds. Scale this volume up to your liking.

   Ensure the bottom of the NavMesh is low enough to include any recessed floor pieces and that the top of the NavMesh is high enough to accommodate the height of the enemy.

   If you’re using the tutorial sample level, create and scale two Nav Mesh Bounds Volumes so they fill Hallway 3 and Room 3.

   [![](https://dev.epicgames.com/community/api/documentation/image/6d1bd313-7808-45c2-a08e-82028259f606?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d1bd313-7808-45c2-a08e-82028259f606?resizing_type=fit)

   As you scale and move the NavMesh, you will see the green zones expanding with the size of the bounding box — unless you have some obstacles, like cubes. Any parts that are cut-off in red mean that they are unnavigable by AI in your game.

If Unreal Editor is including anything in the NavMesh that it shouldn’t, select that mesh level object and disable **Can Ever Affect Navigation** in the **Details** panel.

## Create an Enemy

You’ll create the enemy from the Character class since it already includes movement and animation features that make sense for a humanoid opponent. The Character class actually extends Pawn, which is the more general “controllable actor” used for things like vehicles, cameras, or non-humanoid creatures. For enemies shaped like people, Character is the better starting point.

Since you’re making this character from scratch, you’ll add a mesh to visually represent the enemy and play an animation using an **Animation Blueprint**. The Animation Blueprint is provided in the project files, so you will not create it by scratch, but it’s important to learn how you can integrate one with the enemy character’s Blueprint.

First, create the Enemy Blueprint. Follow these steps:

1. In the **Content Browser**, go to **Content > AdventureGame > Designer > Blueprints > Characters**.
2. Right-click anywhere that is empty in the **Content Browser**, and click **Blueprint Class**.
3. In the new window, select **Character** as the base class.
4. Name this class `BP_Enemy`, and open it in the Blueprint Editor by double-clicking it.

When you create a **Blueprint Class**, you pick a parent class to build from. That parent already comes with built-in features. For example, when you made Blueprints from the Actor class, you started with a transform and the ability to hold components and run logic. Now, by starting from the Character class, you also get movement, collision, and animation support. You use the **Base Class** in a similar manner to a template. When you add functionality, you’re extending that base class.

With the `BP_Enemy` Blueprint Window open, enter the **Viewport** tab and take a look at the **Components** panel. You will see a **Character Movement (CharMoveComp)** component at the bottom of the list. All Character classes come with a Character Movement component. Click the component and look at the **Details** panel to see all the settings inside. You’ll override some of these settings as you create the enemies in your project.

## Add a 3D Model to the Enemy

Your character also comes with a **Mesh** component, but instead of a static mesh, this component is a **skeletal mesh**. The static meshes you’ve been working with so far are fixed 3D models that don’t move, while a skeletal mesh has an internal skeleton so it can animate and deform.

First, set up the character’s mesh and animations. Follow these steps:

1. Select the **Mesh** component and look under the **Details** panel. Find the **Mesh** category and click the dropdown next to **Skeletal Mesh Asset**. In the list, search for the `SKM_Manny_Simple` model and select it. This assigns the Manny model to the blueprint.
2. In the **Details** panel, go to the **Animation** category. Click the dropdown next to **Anim Class**, and assign the `ABP_Unarmed` Animation Blueprint. Now, the enemy character should be playing an idle animation in the **Viewport** tab.

   [![](https://dev.epicgames.com/community/api/documentation/image/b52058ef-c60c-48ab-a0cc-b273b58ecf29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b52058ef-c60c-48ab-a0cc-b273b58ecf29?resizing_type=fit)
3. Modify the animation blueprint to work properly with our enemy:

   1. In the enemy mesh’s **Anim Class** property, click **Browse to Asset in Content Browser** next to `ABP_Unarmed`.
   2. Double-click the `ABP_Unarmed` animation blueprint to open it.
   3. Go to the group of logic that comes after the **Then 1** pin of the **Sequence** node.
   4. You don’t want the acceleration check here to prevent the enemy characters from moving, so delete the wire between the And node and Set Should Move node.
   5. Connect the **Greater (>)** node’s output pin to the **Should** **Move** pin, bypassing the acceleration check.

      [![](https://dev.epicgames.com/community/api/documentation/image/c86b5176-b276-4362-9c2d-820f28ccf7ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c86b5176-b276-4362-9c2d-820f28ccf7ba?resizing_type=fit)
   6. **Compile**, **Save**, and close the blueprint.

In the viewport, you can see a cylindrical capsule shape around the enemy character. This is a visual representation of the **Capsule Component** that detects collisions with other objects, including the ground. The character’s mesh is a more complex shape, so the simple collision cylinder smoothes out the shape for better collision detection performance.

The mesh is offset and not aligned with the capsule. To make the character’s **Mesh** line up with the **Capsule Component**, move the character down so the feet meet the bottom part of the capsule component.

To align the character mesh with its collision volume, follow these steps:

1. Select the **Mesh** component again to highlight the 3D model.
2. In the **Details** panel, use the **Transform** category’s **Location** field to change the **Z** axis, which is the last field with a blue color. Set the value to `-96`.

Now both components are centered at the origin so the enemy does not float above the ground in the game.

Last, you’ll see the character has an **Arrow Component (Arrow)**. The arrow indicates the front-facing direction of the blueprint. Make sure this arrow lines up with the direction the mesh is facing so the character runs in the correct direction.

[![Arrow Component in the Viewport](https://dev.epicgames.com/community/api/documentation/image/90d76e68-7a78-46e5-b4ab-8b1a636c8520?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90d76e68-7a78-46e5-b4ab-8b1a636c8520?resizing_type=fit)

Arrow Component in the Viewport

To make the character mesh face forward, follow these steps:

1. Select the **Mesh** component again. Use the rotate gizmo or **Transform** category of the **Details** panel to rotate the character 90 degrees on the Z axis. Its last **Rotation** value should be **-90**.

| Incorrect Orientation | Correct Orientation |
| --- | --- |
|  |  |

### Change the Material of the 3D Model

Before moving on to creating functionality, change the color of the enemy model to make it red. This distinguishes it from the player and make it look more like an enemy, instead of the current white color.

To make the enemy character a different color, follow these steps:

1. Under the **Materials** section in the **Details** panel, there are two elements:

   * `MI_Manny_01_New` is the material that affects various places on the enemy model like the upper arms, legs, and head.
   * `MI_Manny_02_New` is the material that affects the forearms and torso.
2. Next to the **Element 0**, click the **Browse in Content Browser** button which looks like a folder and a magnifying glass. This opens the folder containing this material in the **Content Browser**. The second material, `MI_Manny_02_New` is in here too.
3. Right-click the `MI_Manny_01_New` asset, and click **Create Material Instance**.
4. Name the **Material Instance** `MI_Enemy_01` and double-click on it to open it.
5. In the **Details** panel, expand **01 - BaseColor**, and enable the **Paint Tint**property.
6. Click the color swatch next to **Paint Tint** property and select a color. This tutorial uses **Hex sRGB** = `F60E6EFF`.

   [![](https://dev.epicgames.com/community/api/documentation/image/e6dc8184-f3a5-4755-8e9c-c23de67f09e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e6dc8184-f3a5-4755-8e9c-c23de67f09e0?resizing_type=fit)
7. Click **Save** and close the window.
8. Back in the **Content Browser**, right-click `MI_Manny_02_New`, and click **Create Material Instance**.
9. Name this Material Instance `MI_Enemy_02` and repeat the previous steps to change the color and save the asset.

Once you have repeated the steps, you should have two new material instances: **MI\_Enemy\_01** and **MI\_Enemy\_02**.

[![Material Instances in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/76cbea9a-0530-47b8-8767-2686331e6355?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76cbea9a-0530-47b8-8767-2686331e6355?resizing_type=fit)

Material Instances in the Content Browser

Next, to assign these materials to the enemy character, follow these steps:

1. In the `BP_Enemy` blueprint, in the **Details** panel, go to the **Materials** section.
2. Click the dropdown for **Element 0** and select the new material you created, `MI_Enemy_01`.
3. For **Element 1**, change it to the `MI_Enemy_02` material.

[![Character using Material Instances](https://dev.epicgames.com/community/api/documentation/image/962e23d5-6fcd-4e15-8ebe-a2c359902aab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/962e23d5-6fcd-4e15-8ebe-a2c359902aab?resizing_type=fit)

Character using Material Instances

## Add an Enemy to the Level

Add an enemy to your level to see how it’s looking and behaving so far.

From the **Content** **Browser**, drag the enemy blueprint into the Level Viewport and place it in front of the player.

When you play the game, you should see the enemy animate with an idle animation.

[![](https://dev.epicgames.com/community/api/documentation/image/2bb6ebe4-7930-4c13-9303-dd5000e15e2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2bb6ebe4-7930-4c13-9303-dd5000e15e2c?resizing_type=fit)

## Set Up the Enemy When Gameplay Starts

With the enemy ready visually, you can create the gameplay functionality. First, you’ll set up the enemy’s properties needed when they spawn.

To set the enemy’s movement speed when the game starts, follow these steps:

1. In the `BP_Enemy` Blueprint Editor window, go to the **EventGraph** tab. By default, there are three events: **Event BeginPlay**, **Event ActorBeginOverlap**, and **Event Tick**. Select **ActorBeginOverlap** and delete it, as it is not necessary for this tutorial.
2. Using the **Components** panel, drag the **Character Movement** component into the Event Graph. This creates a **Character Movement** node. With this component node, you can check or change properties in that component from the graph.
3. Drag the pin of the **Character Movement** node and create a **Set Max Walk Speed** node.
4. Right-click the green **Max Walk Speed** pin of the **Set** node and select **Promote to Variable**.

   This creates a new variable in the My Blueprint panel, under the Variables list.
5. Rename this variable `Max Speed`. Click the **eye** icon next to the variable to turn this into a public and editable variable.
6. Change its **Category** to **Setup**.
7. **Compile** the blueprint, and in the **Details** panel, set **Max Speed**’s **Default Value** to `200`.

   Always assign your editable variables a default value. If you forgot to change its value in the level editor, and the default value was 0, the enemy would not be able to move.
8. Connect **Event BeginPlay** to the **Set Max Walk Speed** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/fa25a216-6794-4f9b-b0b4-f98e6f73684b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa25a216-6794-4f9b-b0b4-f98e6f73684b?resizing_type=fit)

Next, two variables will track the enemy’s health. **TotalHP**, an instance-editable variable, sets the enemy’s starting HP. **CurrentHP** tracks how much health the enemy has during gameplay as they’re damaged by the player or environment.

To set the enemy’s HP, follow these steps:

1. In the **Variables** list, add a new variable called `CurrentHP` of type **Float**.
2. Drag the **CurrentHP** variable from the **Variables** list into the Event Graph and select the **Set Current HP** option. Drag the **Exec** pin of the **Set Max Speed** node and connect it to the **Set Current HP** node’s **Exec** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/2f5f409a-494b-400c-a3b2-3ece391b6151?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f5f409a-494b-400c-a3b2-3ece391b6151?resizing_type=fit)
3. On the **Set Current HP** node, right-click the **Current HP** float pin and click **Promote to Variable**.
4. Rename this variable **TotalHP**. Ensure its type is **Float** and click its **eye** icon to make it public and editable. In the **Details** panel, set its **Category** to **Setup**. Compile the blueprint and set the default value to `100`.
5. Connect the **exec** pins between the **Set** nodes.

You’ll be performing a lot of actions with the player character in this event graph, so next, save a reference to the player as a variable.

To set up a variable for the player character, follow these steps:

1. In the **Variables** list, create a new variable named `PlayerRef` and change its type to **Character** (Object Reference).

   [![](https://dev.epicgames.com/community/api/documentation/image/40c49512-b622-4af3-9249-46223601747a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40c49512-b622-4af3-9249-46223601747a?resizing_type=fit)

   Creating a reference variable for the Character Object is better for your project’s performance than calling the **Get Player Character** function each time you need to reference the player.
2. After the Set Current HP node, connect a Set PlayerRef node.
3. For its **Player Ref** input pin, connect a **Get Player Character** node. Ensure the **Player Index** value is **0**. This is the default index for the first player character spawned into the level.

   [![](https://dev.epicgames.com/community/api/documentation/image/8657b742-15a2-45ab-9eec-49a52a6e6cc3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8657b742-15a2-45ab-9eec-49a52a6e6cc3?resizing_type=fit)

## Make the Enemy Chase the Player

Next, you’ll create the logic for moving the enemy towards the player. You can do this by creating a Custom Event. Call custom events from anywhere in the blueprint to trigger and execute some logic.

To create a custom event that triggers a move action, follow these steps:

1. Right-click anywhere in the event graph and enter `Custom Event` in the search field. Click the **Add Custom Event** option in the list and name this event **MoveToPlayer**.
2. Drag the pin of the **MoveToPlayer** event node and search for and create an **AI MoveTo** node. This node is an action that pawns with an AI Controller use to move to a specific location. In this case, you will use it to move the enemy to the player.

   Just like your player character is possessed with a Player Controller, NPC characters can be possessed with an AI Controller. To view **Auto Possess AI** settings in the `BP_Enemy` blueprint, select the root component and go to the **Pawn** category in the **Details** panel.

   [![](https://dev.epicgames.com/community/api/documentation/image/ac31fed1-c43b-40c0-b8e7-e9176a31867f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac31fed1-c43b-40c0-b8e7-e9176a31867f?resizing_type=fit)
3. On the **AI MoveTo** node, drag the **Pawn** pin and enter `Self` in the search field. Select **Get a reference to self** to create a node that refers to the actor of this blueprint in-game.
4. Drag the **Target Actor** pin of the **AI MoveTo** node and create a **Get PlayerRef** node.
5. Set **Acceptance Radius** to `10`. This is the distance in centimeters at which the enemy considers itself to have arrived at its destination. It gives you more control than **Stop on Overlap**.

   [![](https://dev.epicgames.com/community/api/documentation/image/16e12da9-59eb-436b-8f9f-da9069350946?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16e12da9-59eb-436b-8f9f-da9069350946?resizing_type=fit)

In this case, you are using the **Self** node to define this enemy as the Pawn that should move. Then, you set the player as the **Target Actor**, which is the target the Pawn moves towards.

The **AI MoveTo** node comes with **On Success** and **On Fail** events. These define what happens if the enemy reaches the player, or if it fails.

To define what happens after the enemy moves, follow these steps:

1. In the **AI MoveTo** node, drag the **On Success** pin and create a **Delay** node.
2. Right-click the **Duration** pin from the **Delay** node and select **Promote to Variable**.
3. Name this variable **WaitAtDestination** and ensure its type is **Float**.
4. **Compile** the blueprint and change **WaitAtDestination**’s default value to `5`. Click its **eye** icon to make it editable, and change its **Category** to **Setup**.
5. In the Event Graph, drag the **Delay** node’s **Exec** pin and create a **Move To Player** node. This ensures the enemy continues to chase the player if they move away, but after a delay that gives the player a chance to gain some distance.
6. From the **AI MoveTo** node, drag the **On Fail** pin and create a new **Delay** node.
7. Drag the **Completed** pin of the **Delay** and create a **Move To Player** node. Leave the **Duration** at **0.2**. This ensures the enemy keeps moving if they haven’t reached the player yet.

   [![](https://dev.epicgames.com/community/api/documentation/image/b3880a9d-b3cb-4d86-9b5f-61528df4d8e4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3880a9d-b3cb-4d86-9b5f-61528df4d8e4?resizing_type=fit)
8. In the **Event BeginPlay** group of logic. At the end of this sequence, after the **Set Player Ref** node, connect a **Move To Player** node to trigger this event. This gets the enemy moving at the start of the game so you can test the enemy’s movement.

   [![](https://dev.epicgames.com/community/api/documentation/image/ae18c417-bc40-47f5-8ffc-b3cc06a9f736?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae18c417-bc40-47f5-8ffc-b3cc06a9f736?resizing_type=fit)
9. **Save** and **Compile** the blueprint.

Your event graph should now look like this:

[![](https://dev.epicgames.com/community/api/documentation/image/54ae4825-e1eb-4670-83f9-f4b78eeddc69?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54ae4825-e1eb-4670-83f9-f4b78eeddc69?resizing_type=fit)

### Test Enemy Movement

In your level, move your enemy actor to be within the bounds of the NavMesh, meaning on the green zones.

Select the `BP_Enemy` actor in the Level Viewport or the Outliner. In the **Details** panel, you will see the variables you have added in the blueprint in the **Setup** section. You can change these values to fit your project’s needs, or turn on **Debug Detection** to enable the debug drawing of the line trace.

Play your level again and see how the enemy behaves now. It should walk towards the player, stop when it reaches the player, wait 5 seconds, and then try to walk towards the player again.

If anything doesn't work as intended, check if the variables you have created in the blueprint have correct values set in the `BP_Enemy` in the scene. If you don’t set the values of the **Max Speed**, or the **Max Detection Distance**, the enemy will not move. The same thing might happen if the values are too low.

## Deal Damage to the Player

Now that the enemy can reach the player, you can add functionality that makes the enemy damage the player when they collide. In this tutorial, you’ll create an enemy that self-destructs on contact with the player, so you’ll also add logic to remove that enemy after it damages the player once.

To check if the enemy has collided with the player, follow these steps:

1. In the **Components** panel, right-click **Capsule Component (CollisionCylinder)**, go to **Add Event**, and select **Add OnComponentHit**.

   [![](https://dev.epicgames.com/community/api/documentation/image/dd8c3b36-a097-4bc2-87cd-06fece16ffb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd8c3b36-a097-4bc2-87cd-06fece16ffb1?resizing_type=fit)

   This creates a new event node in the Event Graph that executes when the Capsule Component hits something.
2. Drag the pin of the **On Component Hit** node and create a **Branch** node.
3. Connect the **Condition** pin to the **Other Actor** pin of the **On Component Hit** node, which prompts you to create a new node.
4. Create an **Equal** node. Drag out the **Select Asset** pin of the **Equal** node and add a reference to the **PlayerRef** variable.

   [![](https://dev.epicgames.com/community/api/documentation/image/0d130749-a563-4814-8466-7de60a3f8999?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d130749-a563-4814-8466-7de60a3f8999?resizing_type=fit)

Now, this logic triggers an event when the enemy’s Capsule Component hits something in the game. The event checks if the Capsule Component hit the player character.

To deal one hit of damage to the player and remove the enemy, follow these steps:

1. In the **Variables** list, create a new variable named **Eliminated** and change its type to **Boolean**. You’ll use this when the enemy is defeated and should be removed from the game.
2. To ensure they only damage the player once, drag off the **Branch** node’s **True** pin and create a **Do Once** node.
3. From the **Do Once** node’s **Completed** pin, create an **Apply Damage** node. Drag the **Damaged Actor** pin and connect a reference to the **PlayerRef** variable. This is the actor who should receive the damage.
4. Right-click the **Base Damage** pin and select **Promote to Variable**.

   [![](https://dev.epicgames.com/community/api/documentation/image/235ef302-058b-472f-9fb9-a0248e2a75ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/235ef302-058b-472f-9fb9-a0248e2a75ed?resizing_type=fit)
5. In the **Variables** list, click **Base Damage**’s **eye** icon to make it editable, and change its **Category** to Setup. Compile the blueprint and set the default value to `25`.
6. Drag the **Eliminated** variable from the **Variables** list into the Event Graph and select **Set**. In the node, click the checkbox to set **Eliminated** to true.
7. Connect the **Exec** pin of the **Apply Damage** node to the **Set Eliminated** node.
8. Drag the **Exec** pin of the **Set Eliminated** node and create a **Delay** node. Set the **Duration** to `2.0`.
9. Drag the **Exec** pin of the **Delay** node and create a **Destroy Actor** node. The **Target** property should be set to **self** by default.

When the enemy collides with the player, it applies damage to the player and kills the enemy after a 2-second delay.

[![](https://dev.epicgames.com/community/api/documentation/image/9d074961-334c-4e3a-bbc7-d76df629728b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d074961-334c-4e3a-bbc7-d76df629728b?resizing_type=fit)

Now, the enemy can run towards the player and then apply damage and self-destruct when it collides with the player. However, it does not consider the distance or obstacles between the player and the enemy. So the enemy always chases the player no matter the distance or line of sight.

`BP_Enemy`’s finished **On Component Hit** logic should look like the following:

To copy the blueprint snippet below into your `BP_Enemy` event graph, ensure your variable names match those in the sample project.

Blueprint

Copy full snippet(156 lines long)

## Add Distance and Obstacle Logic

Next, add a maximum detection distance so the enemy can only detect the player when they are close enough to the enemy. Then, finish by implementing enemy line-of-sight restrictions so they can’t see the player through walls.

To do this, you’ll first create a new function in your blueprint library that performs a line trace between the enemy and the player.

### Calculate Line of Sight and Distance With a Line Trace

A **Line Trace** (or raycast) is a common practice in game development. Line Traces draw an invisible line from a point in the world (like a source actor) to see what the line hits. It’s often used to detect objects or surfaces at runtime so you can trigger logic depending on the result of the trace.

In this tutorial, you’ll cast a line trace from the enemy character to detect when the player character is in the enemy’s line of sight.

For more information about Line Traces, see the [Traces with Raycasts](https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-with-raycasts-in-unreal-engine) documentation.

To set up a function that uses a line trace to find the player, follow these steps:

1. In the **Content Browser**, go to your **Core** folder and open the `BPL_FPGame` blueprint library.
2. Add a new function named `fnBPLFindPlayer`.
3. In the new function’s **Details** panel, in the **Inputs** section, click **Add (+)** to create the following inputs:

   1. **Player Reference** (Pawn Object Reference)
   2. **Start Location** (Vector)
   3. **Max Detection Distance** (Float)
   4. **Debug** (Boolean)

      [![](https://dev.epicgames.com/community/api/documentation/image/ef11431f-a5b7-4b6b-b48a-1315983ff672?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef11431f-a5b7-4b6b-b48a-1315983ff672?resizing_type=fit)

      After adding these inputs, the **fnBPLFindPlayer** function entry node now has corresponding pins for each of the variables.
4. In the function’s **Details** panel, in the **Outputs** section, click **Add (+)** to create a **Boolean**-type output value named **Found**.

   [![](https://dev.epicgames.com/community/api/documentation/image/dc8e7737-eb7f-47fe-aff8-daa1dda6cd27?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc8e7737-eb7f-47fe-aff8-daa1dda6cd27?resizing_type=fit)

   After adding the **Found** output, a new **Return Node** appears in your graph with the **Found** pin.
5. In the **My Blueprint** panel, in the **Local Variables** section, click **Add (+)** to create a local variable named **PlayerFound** with type **Boolean**. Ensure its default value is false.

   [![](https://dev.epicgames.com/community/api/documentation/image/f75b664a-74fb-417c-9b32-537fd52b86c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f75b664a-74fb-417c-9b32-537fd52b86c6?resizing_type=fit)

The player reference is critical for the function to execute properly, so when the function starts, check for a valid player reference to avoid errors.

To check for valid input, follow these steps:

1. Delete the wire between the entry node and **Return Node** by holding **Alt** and clicking the wire or either exec pin.
2. After the function entry node, create and connect an **Is Valid** node.

   Ensure you create an **Is Valid** node represented with a question mark (**?**) icon near the bottom of the node actions list.
3. Connect the **Player Reference** pin from the entry node to the **Input Object** pin on the **Is Valid** node.
4. Connect the **Is Not Valid** exec pin to the **Return Node**.
5. For the **Found** return value, connect a reference to the **PlayerFound** variable. This exits the function, returning PlayerFound=False back to the enemy’s event graph.

   [![](https://dev.epicgames.com/community/api/documentation/image/053cdb12-59d2-46d9-9c56-76face3851fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/053cdb12-59d2-46d9-9c56-76face3851fd?resizing_type=fit)

If the player is valid, the function should execute the line trace object, then return **PlayerFound**.

To set up the line trace, follow these steps:

1. From the **Is Valid** exec pin, add a **Sequence** node to organize your logic.
2. Drag off the **Sequence** node’s **Then 0** pin and add a **Line Trace By Channel** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/f7a2d930-e0b8-4824-98cc-49158384c31e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7a2d930-e0b8-4824-98cc-49158384c31e?resizing_type=fit)

   **Line Trace By Channel** detects objects on a specific collision channel. To view collision channel settings for a blueprint, select the blueprint’s collision component, and go to the **Collision > Collision Presets** properties in the **Details** panel. The **Trace Responses** section has **Visibility** and **Camera** channels.
3. From the function entry node, drag the **Start Location** pin and connect it to the **Line Trace By Channel** node’s **Start** pin. This sets the enemy character’s location as the starting point for the line trace.
4. To keep your graph tidy, create a **Get Player Referenc**e node. The **f** icon in the top-right corner of the node shows it’s a function input. You can add references to these inputs like you would any other variable.
5. Drag off the **Player Reference** pin to a blank spot in the graph. This opens the node actions list. In the list, search for and create a **Get Actor Location** node.
6. Connect its **Return Value** to the **End** pin of the **Line Trace** node. This ends the line trace at the player’s location.
7. On the **Line Trace By Channel** node, set the **Trace Channel** property to **Camera** using the dropdown menu.

   [![](https://dev.epicgames.com/community/api/documentation/image/14bc7406-eaaa-4d15-a4b4-fd8d33946aaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14bc7406-eaaa-4d15-a4b4-fd8d33946aaf?resizing_type=fit)

Now that you’ve set where the line trace begins and ends, define what happens when the trace hits something.

To check if a line trace has hit the player, follow these steps:

1. Drag off the line trace’s **Out Hit** pin and add a **Break Hit Result** node. When a line trace hits an object, a lot of information is collected. You only need to use a few specific values, so a **Break Hit** **Result** node is needed to split the data into the individual components of the returned data.
2. In the **Break Hit Result** node, click the arrow at the bottom to see more options.

   You want to know if the player is in line of sight and within a certain distance of the enemy, so you’ll use the **Hit Actor**pin to check for the player, and use **Trace Start**and **Trace End**to measure the distance to the hit object.
3. Drag off the **Hit Actor** pin and add an **Equal** operator node. For the bottom input, connect a reference to the **Player Reference** function input.

   To reference function input values, you can add a **Get** node similar to other variables.

   [![](https://dev.epicgames.com/community/api/documentation/image/f50da774-308a-455b-95f9-563878122a98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f50da774-308a-455b-95f9-563878122a98?resizing_type=fit)
4. Create a **Distance (Vector)** node. Connect **V1** to **Trace Start** and connect **V2** to **Trace End**.

   A vector is a set of X, Y, and Z values that represent an object or point’s position in 3D space. The **Distance** node calculates the distance between two of these points, which results in a float value.
5. Drag off the **Distance** node’s **Return Value** and add a **Less (<)** node. For the bottom input, connect a reference to the **Max Detection Distance** function input.
6. Create an **AND (Boolean)** node.
7. Connect both the **Equals (==)** and **Less (<)** nodes’ boolean output pins to the **AND** node’s input pins.

   [![](https://dev.epicgames.com/community/api/documentation/image/1aeade31-6892-421f-9dba-c5ef528e2fa9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1aeade31-6892-421f-9dba-c5ef528e2fa9?resizing_type=fit)

   With this logic, the **AND** node returns true if the line trace hits an actor that’s equal to **Player Reference**, and the distance between the start of the trace (the enemy) and the end (the hit object) is less than **Max Detection Distance**.

To use the trace result to set and return **PlayerFound**'s value, follow these steps:

1. Drag off the **AND** node’s output and add a **Branch** node.
2. Connect its **exec** pin so it executes after **Line Trace By Channel**.
3. From the **Branch** node’s **True** exec pin, create a **Set** variable node to set the local **PlayerFound** variable to true.
4. From the **Branch** node’s **False** pin, create a **Set PlayerFound** variable. Keep the value false.

   [![](https://dev.epicgames.com/community/api/documentation/image/52025996-51e5-400a-a610-16f3a88331ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52025996-51e5-400a-a610-16f3a88331ad?resizing_type=fit)
5. You’re finished with the line trace logic, so go back to the **Sequence** node and connect its **Then 1** pin to the **Return Node** to exit the function and send the **PlayerFound** result back to the enemy blueprint.

   [![](https://dev.epicgames.com/community/api/documentation/image/c0580a5c-b52f-4068-9257-82104dc2c763?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0580a5c-b52f-4068-9257-82104dc2c763?resizing_type=fit)

### Add a Line Trace Debug Option

You want to be able to easily toggle a debug visual of the line trace on and off from the level editor. However, the Line Trace node only lets you pick one option from the **Draw Debug Type** list. You can use a **Select** node to make the debug type editable in the level editor.

[![](https://dev.epicgames.com/community/api/documentation/image/a9ad1786-d226-4db3-a61b-61c191a85654?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9ad1786-d226-4db3-a61b-61c191a85654?resizing_type=fit)

To set up a customizable debug option to the line trace, follow these steps:

1. Drag from the **Line Trace By Channel** node’s **Draw Debug Type** pin and create a **Select** node.
2. Connect the **Select** node’s **Index** pin to a reference to the function’s **Debug** input.

   The **Select** node’s index is a wildcard, so when you connect the boolean-type **Debug** value, the options change to **False** and **True**.
3. Set the **False** option to **None**. Set the**For Duration** option to **True**.
4. At the bottom of the **Line Trace By Channel** node, click the arrow button to see more options. Change the **Draw Time** to `0.1` seconds.

   [![](https://dev.epicgames.com/community/api/documentation/image/6b5cd5cf-65dc-4dce-af05-18e2ef05a19f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6b5cd5cf-65dc-4dce-af05-18e2ef05a19f?resizing_type=fit)
5. **Save** and **Compile** your Blueprint Function Library.

This logic uses the **Debug** variable to determine if the Line Trace debug drawing is active or not:

* When the **Debug** variable is false, the **Draw Debug Type** is set to **None**, meaning no debug drawing is rendered.
* When **Debug** is set to true, the **Select** node changes the **Draw Debug Type** to **For Duration**, which renders the line trace at runtime for a set duration.

The finished **fnBPLFindPlayer** function should look like the following:

If you copy this blueprint snippet into your project, you’ll need to connect the function entry node’s **Exec** and **Player Reference** pins to the **Is Valid** node’s **Exec** and **Input Object** pins. For the snippet to copy properly, ensure the names of your function inputs match those in the sample project.

Blueprint

Copy full snippet(302 lines long)

### Update the Move-to-Player Logic

Now that you can call a function that looks for the player while considering distance and line of sight, add logic to the enemy that makes them look for and chase the player only on sight, or when the line trace successfully finds the player.

To make the enemy chase the player after finding the player, follow these steps:

1. Go back to the `BP_Enemy` blueprint. In the Event Graph, find the provided **Event Tick** node.
2. Drag the **Exec** pin of the **Event Tick** node and create a **Branch** node.

   The **On Tick** event runs every frame while the game is playing. Use it to make the enemy constantly check for the player’s position and determine whether to start chasing.
3. Drag the **Condition** pin of the **Branch** node and create a **NOT Boolean** node, which returns the inverse of a boolean’s value.
4. In this case, you want to negate the **Eliminated** variable, so drag the input pin of the **NOT** node and search for **Get Eliminated**.

   [![](https://dev.epicgames.com/community/api/documentation/image/b43ba716-9282-487d-8f05-4421c64708fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b43ba716-9282-487d-8f05-4421c64708fc?resizing_type=fit)

   This checks if the enemy is not eliminated before proceeding with the **True** pin of the **Branch** node.
5. Drag the **True** pin of the **Branch** node and create a **FnBPLFindPlayer** node. This node performs a line trace to find the player in the world and checks the current distance between the enemy and player.
6. On the **Fn BPLFind Player** node, make these following connections using its pins:

   * **Player Reference**: Connect a reference to the **PlayerRef** variable.
   * **Start Location**: Create a **Get Actor Location** node with the **Target** property set to **self**. This assigns the start location of the line trace to the enemy’s position in the world.
   * **Max Detection Distance**: Right-click the pin and select **Promote to Variable**. Click its **eye** icon to make it editable, and change its **Category** to **Setup**. Compile, and set its **Default Value** to `20000` (200 meters). The smaller this value is, the closer the player has to be for enemies to detect them.
   * **Debug**: Select **Promote to Variable** and name it `DebugDetection`. Also make this variable editable and appear in the **Setup** category.

     [![](https://dev.epicgames.com/community/api/documentation/image/135ef143-f9f1-4304-b7c8-f220a6221e50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/135ef143-f9f1-4304-b7c8-f220a6221e50?resizing_type=fit)

If the player is found by the line trace, set the maximum movement speed of the enemy to a desired amount, moving the enemy towards the player. If not, you should set the speed to 0 so the enemy can’t move towards the player.

To make the enemy move when the player is found and stop when the player is not found, follow these steps:

1. In the **FnBPLFindPlayer** node, right-click the **Found** pin and select **Promote to Variable**. This automatically connects a **Set** node for that new variable. Now you can use this **Found** result elsewhere in the graph.
2. After the **Set** node, connect a **Branch** node. Drag the **Condition** pin of the **Branch** node to the **Set Found** node’s output pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/f7980e0e-1440-495a-afa0-f52c6f5a2f3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7980e0e-1440-495a-afa0-f52c6f5a2f3d?resizing_type=fit)
3. From the **Components** panel, drag the **Character Movement (CharMoveComp)** into the Event Graph. Drag its pin and create a **Set Max Walk Speed** node.
4. Drag the **True** pin of the **Branch** node and connect it to the **Set Max Walk Speed** node.
5. For the **Set** node’s **Max Walk Speed** pin, connect a reference to the **Max Speed** variable.
6. After the **Set** node, connect a **MoveToPlayer** node to call that event and make the enemy move only if they’ve found the player.

   [![](https://dev.epicgames.com/community/api/documentation/image/52fb2d6e-295f-4191-9494-4d15030a17f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52fb2d6e-295f-4191-9494-4d15030a17f0?resizing_type=fit)
7. Duplicate the **Set Max Walk Speed** and **Character Movement** nodes. Connect the **False** pin of the **Branch** node to the new **Set** node.
8. In the second **Set Max Walk Speed** node, ensure the walk speed value is **0**. This makes the enemy stop moving without canceling its **AI MoveTo** task and needing to run the task again.

   [![](https://dev.epicgames.com/community/api/documentation/image/de03dd81-9833-4668-8621-ceda028f0e8c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de03dd81-9833-4668-8621-ceda028f0e8c?resizing_type=fit)
9. Now that you have the enemy looking for the player every frame, delete the **Move to Player** node that you added at the end of the **Event BeginPlay** logic. This node was useful for testing a partially-completed enemy, but you don’t need it anymore.
10. Go to your **MoveToPlayer** event logic. Now, you only want the enemy to execute this if the player was found:

    1. Drag off the **MoveToPlayer** node and create a **Branch** node.
    2. For the **Branch**’s **Condition**, add a reference to the **Found** variable.

       [![](https://dev.epicgames.com/community/api/documentation/image/378ff59c-ed92-43b0-93d2-e240c5733170?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/378ff59c-ed92-43b0-93d2-e240c5733170?resizing_type=fit)

Now, If the player is within the given distance to the enemy, and there are no obstacles in between the two, the enemy’s movement speed will be set to the **MaxSpeed** variable and they’ll execute the **MoveToPlayer** logic. If either of those conditions are not met, the enemy’s movement speed will be set to 0 — blocking the enemy from moving towards the player.

`BP_Enemy`’s final variable list should look like the following:

[![](https://dev.epicgames.com/community/api/documentation/image/d7119fe3-452f-43f6-ba4d-7de4ec715f53?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7119fe3-452f-43f6-ba4d-7de4ec715f53?resizing_type=fit)

To copy the blueprint snippets below into your `BP_Enemy` event graph, ensure your variable names match those in the sample project.

`BP_Enemy`’s final **Event BeginPlay** logic should look like the following:

Blueprint

Copy full snippet(102 lines long)

`BP_Enemy`’s final **MoveToPlayer** logic should look like the following:

Blueprint

Copy full snippet(153 lines long)

`BP_Enemy`’s final **Event Tick** logic should look like the following:

Blueprint

Copy full snippet(205 lines long)

## Allow Enemies to Receive Damage

Before finishing up this blueprint, you need to make sure that the enemy can be damaged as well. If you continue working on your game beyond this tutorial series, you may want enemies to be damaged by the traps or give the player an equippable item that can damage and eliminate enemies.

To make enemies take damage, follow these steps:

1. Right click anywhere in the Event Graph and create an **Event AnyDamage** node.
2. Drag the **exec** pin from **Event AnyDamage** and create a **Set CurrentHP** node.
3. To subtract the damage dealt from the CurrentHP, drag the **Current HP** property’s pin and create a **Subtract** node.
4. Drag the upper pin of the **Subtract** node and create a **Get Current HP** node.
5. Connect the bottom pin of the **Subtract** node to the **Damage** property of the **Event AnyDamage** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/c2e80e50-1926-41c6-9bf5-cc4420af0eb5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2e80e50-1926-41c6-9bf5-cc4420af0eb5?resizing_type=fit)

When any damage is dealt to this actor, this takes the CurrentHP variable’s value and subtracts the Damage from it, and then sets the CurrentHP value to the new value.

Next, check if the CurrentHP is less than or equal to 0, which should eliminate the enemy.

To remove the enemy when its HP is 0, follow these steps:

1. Drag the **Set** node’s pin, and create a new **Branch** node.
2. Drag the **Condition** pin of the **Branch** node and create a **Less Equal (<=)** node.
3. Connect the **Set Current HP** node’s output pin to the **Less Equal** node’s upper input pin. Make sure that the lower pin is set to **0**.
4. Drag the **True** pin of the **Branch** node, and create a **Do Once** node.
5. Drag its **Completed** pin and create a **Set Eliminated** node. In the **Set** node, toggle the **Eliminated** property to **true**.
6. After the **Set** node, connect a **Delay** node with the **Duration** set to `2`.
7. Drag the **Completed** pin of the **Delay** node and create a **Destroy Actor** node with the **Target** property set to **self**.

   [![](https://dev.epicgames.com/community/api/documentation/image/6e5c7a6c-5136-4f0c-9253-1a1c4aa8696b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e5c7a6c-5136-4f0c-9253-1a1c4aa8696b?resizing_type=fit)
8. **Save** and **Compile** the blueprint.

`BP_Enemy`’s finished **Event AnyDamage** logic should look like the following:

Blueprint

Copy full snippet(146 lines long)

## Test the Finished Enemy Character

If you now play the game, depending on the distance between the enemy and the player, the enemy might not be moving. If you move closer to the enemy, it should start chasing the player.

Try it with an obstacle. Exit play mode and add a blockout cube or wall in the middle of the NavMesh zone by pressing the **Create** button in the **Main Toolbar** and selecting **Shapes > Cube**. This obstacle cuts into the NavMesh.

If the player starts behind this obstacle, the enemy won’t be able to chase the player since the linetrace is blocked by the cube, resulting in the enemy failing to find the player. If the player walks around the cube and the enemy has direct sight of the player, it starts chasing the player. Once the enemy starts its AI MoveTo action, hiding behind an obstacle won’t stop the enemy’s pursuit.

If you’d like an enemy to see through an obstacle to the player, select the level object and go to **Collision > Collision Presets** in the **Details** panel. Change the preset to **Custom** and enable **Ignore** in the **Camera** channel. To make an object block the line trace, change the preset back to **Default**.

[![](https://dev.epicgames.com/community/api/documentation/image/00921a6a-442d-45b9-b43a-48cb24e63ec3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00921a6a-442d-45b9-b43a-48cb24e63ec3?resizing_type=fit)

## Placing Enemy Locations in Your Project

For our sample level, we placed several enemies in Hallway 3 and Room 3. The first enemy is alone in Hallway 3 to give the player a simple first encounter and help them learn the enemy character’s behavior and abilities. After encountering the single enemy in the hallway, we placed two additional enemy characters in Room 3 to introduce more of a challenge to the player.

[![](https://dev.epicgames.com/community/api/documentation/image/00f193c5-7c39-460d-a041-6e64d21f3454?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00f193c5-7c39-460d-a041-6e64d21f3454?resizing_type=fit)

You can vary enemy numbers and types to provide different levels of difficulty throughout your project. Introducing players to new enemies and challenges slowly creates a balanced difficulty curve that the player can become accustomed to over time. Creating a difficult enemy encounter after allowing the player to learn how to navigate and defeat enemies provides a challenge that can feel rewarding to the player.

## Next Up

In the next module, you will learn how to add a sprint mechanic to the player’s moveset. This helps the player move through familiar places in the level and also gives them a tool to avoid the enemies you just added to the project.

* [![Add a Sprint Mechanic to the Player](https://dev.epicgames.com/community/api/documentation/image/270b9145-0c98-4508-bc16-cac1a9c05617?resizing_type=fit&width=640&height=640)

  Add a Sprint Mechanic to the Player

  Use Input Actions to add a sprint mechanic to the player character's move set.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-09-sprint-input-action-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [damage](https://dev.epicgames.com/community/search?query=damage)
* [character](https://dev.epicgames.com/community/search?query=character)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Create NavMesh for the Enemy’s Navigation](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#createnavmeshfortheenemy%E2%80%99snavigation)
* [Create an Enemy](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#createanenemy)
* [Add a 3D Model to the Enemy](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#adda3dmodeltotheenemy)
* [Change the Material of the 3D Model](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#changethematerialofthe3dmodel)
* [Add an Enemy to the Level](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#addanenemytothelevel)
* [Set Up the Enemy When Gameplay Starts](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#setuptheenemywhengameplaystarts)
* [Make the Enemy Chase the Player](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#maketheenemychasetheplayer)
* [Test Enemy Movement](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#testenemymovement)
* [Deal Damage to the Player](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#dealdamagetotheplayer)
* [Add Distance and Obstacle Logic](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#adddistanceandobstaclelogic)
* [Calculate Line of Sight and Distance With a Line Trace](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#calculatelineofsightanddistancewithalinetrace)
* [Add a Line Trace Debug Option](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#addalinetracedebugoption)
* [Update the Move-to-Player Logic](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#updatethemove-to-playerlogic)
* [Allow Enemies to Receive Damage](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#allowenemiestoreceivedamage)
* [Test the Finished Enemy Character](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#testthefinishedenemycharacter)
* [Placing Enemy Locations in Your Project](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#placingenemylocationsinyourproject)
* [Next Up](/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
