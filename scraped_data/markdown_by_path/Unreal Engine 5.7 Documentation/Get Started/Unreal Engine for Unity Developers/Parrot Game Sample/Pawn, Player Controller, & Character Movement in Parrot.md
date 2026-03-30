<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7 -->

# Pawn, Player Controller, & Character Movement in Parrot

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
6. [Unreal Engine for Unity Developers](/documentation/en-us/unreal-engine/unreal-engine-for-unity-developers "Unreal Engine for Unity Developers")
7. [Parrot Game Sample](/documentation/en-us/unreal-engine/parrot-game-sample-for-unreal-engine "Parrot Game Sample")
8. Pawn, Player Controller, & Character Movement in Parrot

# Pawn, Player Controller, & Character Movement in Parrot

Project Parrot's pawns, player controller, and character movement functionality.

![Pawn, Player Controller, & Character Movement in Parrot](https://dev.epicgames.com/community/api/documentation/image/83b67f36-d506-4280-bff4-5c84df11fc42?resizing_type=fill&width=1920&height=335)

 On this page

## What are the pieces of a character in Unreal Engine?

As mentioned in the **Game Mode** / **Game State** section, the [Unreal Engine Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) helps in understanding how characters work in Unreal Engine. Conceptually, a player consists of a pawn representing the physical presence in the game world, and a controller determines the behavior. This decoupling is useful for AI as well as network replication. For reference, the hierarchy looks like this:

[![Character components tree with player controller at the top.](https://dev.epicgames.com/community/api/documentation/image/17fa50e8-54ed-4aa9-96f2-fd3a6bfbda63?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17fa50e8-54ed-4aa9-96f2-fd3a6bfbda63?resizing_type=fit)

Let’s start with importing the assets, creating the pawn, and working up to the player controller. For Parrot, our player-controlled hero will be Captain Barbarossa (visit the Quaternius website to get the [Pirate Kit provided by Quaternius](https://quaternius.com/packs/piratekit.html)).

## Importing Art Assets

In a 3D modeling tool of your choice, export your mesh/animations to an engine compatible format. In this case, the developers used `.fbx`. Barbarossa’s assets are under `Content/Assets/Quaternius/PirateKit/Characters/Barbarossa`. You can import your `.fbx` by right clicking the context menu or dragging and dropping it into the content browser. You’ll be met with an `.fbx` import settings window. Choose the appropriate options for your import. In this case, be sure that no existing skeleton is selected and that **import animations** is ticked. Also necessary is creating a new atlas material that can be indexed by your mesh. This material can be reused across assets in the Pirate Kit. You should now have these 3 files and any animations included in your `.fbx.`

For cleanliness, **Animation Sequence** files are located underneath the **Animations** folder adjacent to the 3 files:

[![Icon images for files in the Animations folder.](https://dev.epicgames.com/community/api/documentation/image/5815f300-2b2f-4e85-a2ff-99d7b16f3d2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5815f300-2b2f-4e85-a2ff-99d7b16f3d2c?resizing_type=fit)

## Skeleton, Skeletal Mesh, and Physics Assets

A Skeleton is a hierarchy that is used to define Bones (sometimes called joints) in a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine). These bones should match the rig in your 3D modeling tool. Skeletons can be reused across Skeletal Meshes so long as the rigs are compatible. You will also notice a created [Physics Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine). Physics Assets define the physics and collision used by a Skeletal Mesh. They contain rigid bodies and constraints for simulation. You can only have one Physics Asset per Skeletal Mesh and they can conditionally be toggled on or off. You can adjust Physics Assets as they’re imported or create new assets from a skeletal mesh.

## Animation Blueprint

Now that there is a Skeletal Mesh to work with, you can start animating it with the [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine). The Animation Blueprint is similar to Unity’s **Mecanim Animation System**. The **Animation Graph** in **Animation Blueprints** should look familiar and function in a similar way. Both systems have conditional logic flow that can transition animation states to a final output pose. In your folder, create a new Animation Blueprint from the context menu and select your Skeleton. Our Animation Blueprint will be called `ABP_Captain_Barbarossa` under ****Content/Blueprints/Player****.

[![Image of animation blueprint option in the cascading menu.](https://dev.epicgames.com/community/api/documentation/image/e5011e22-193b-4808-85be-3502ece08a52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5011e22-193b-4808-85be-3502ece08a52?resizing_type=fit)

On the left hand side of the **Blueprint Inspector**, you’ll notice there are two graphs: **Event Graph** and **Animation Graph**. The Animation Graph is the state machine that controls your final output pose. The Event Graph is where you can define any logic related to Animation. Unlike Unity, where you need to pass data to the Mecanim component, Animation Blueprints can pull what they need on a given event. For example, you might want to query the character’s velocity and drive your animation based on that value. A clean way to do this is to use the **Event Blueprint Initialize Animation Node** in the Event Graph, **Get the Owning Actor**, and cache their movement component in a variable. From there, every tick of `BlueprintThreadSafeUpdateAnimation`, you can query velocity right from your movement component. Variables can also be shared between the Event Graph and Animation Graph.

The configured Animation Blueprint for Barbarossa is worth exploring further on your own. By double clicking into nodes you can see how the state machines, states, and state rules are configured for the final output pose. There are also examples of using a sequence player and using a blend space. Similarly, the event graph shows how the animation is driven by character data - this relationship will become more clear as this article continues.

## Pawn

Now that there is a Skeletal Mesh that can animate, you can begin creating your [Pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine) that will be used by the Game Mode. The developers chose to build on Unreal Engine's default [Character](https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine) which is a child class of the default Pawn C++ class. The Character class has a **Character Movement** component which is especially useful for this game and is another class to be built on.

Both the player and enemy pawns have some shared functionality such as hitpoints, getting hit, and death. This functionality is shared by creating a `AParrotCharacterBase` C++ class which inherits from `ACharacter`. This class provides a good baseline to build from as enemy and player pawns diverge in behavior.

Next, create a `AParrotPlayerCharacter` C++ to handle player specific logic. Lastly, you will create a blueprint to handle the visual representation of your character. Parrot's Blueprint is `BP_ParrotPlayerCharacter` under **Content/Blueprints/Player**. The inheritance hierarchy looks like this:

[![Image of the instance hierarchy component stack.](https://dev.epicgames.com/community/api/documentation/image/f76ec3a3-b8b2-4c19-830d-0dc5f5e40b4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f76ec3a3-b8b2-4c19-830d-0dc5f5e40b4e?resizing_type=fit)

Opening up `BP_ParrotPlayerCharacter`, you should see some components under the component inspector on the left of the editor window. The **Mesh Component** is where you can set your **Skeletal Mesh Asset** as well as the Animation Blueprint under **Anim Class**. If the mesh is not positioned correctly, you can adjust the transform values to align with your capsule component. You should have something like this:

[![Image of the Mesh dropdown and where the transform menu is located on the right-side menu.](https://dev.epicgames.com/community/api/documentation/image/1ec64da2-944d-4b0a-a0c4-5a986eeb0e55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ec64da2-944d-4b0a-a0c4-5a986eeb0e55?resizing_type=fit)

Next, you can assign the default pawn class to the Blueprint in the game mode asset.

[![Default pawn class option in the Classes menu.](https://dev.epicgames.com/community/api/documentation/image/8207cb94-e863-4ddc-98f2-8af2b65de109?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8207cb94-e863-4ddc-98f2-8af2b65de109?resizing_type=fit)

Now there is an animating pawn that can be used in the game!

## Player Controller

With a usable pawn, you can now create the player controller. Player controllers essentially represent the human player’s will. Something to consider when making your game is where to define input events. For simple games where pawns do not change, the pawn is suitable for this. However, when behavior starts to get complex, the player controller is a better option for this. Pawns are transient and can be possessed or unpossessed by player controllers. Pawns can be spawned or destroyed while player controllers persist throughout the game.

You won’t need any C++ logic in the player controller, so just create a blueprint to do what is needed. `BP_ParrotPlayerController` is located under **Content/Blueprints/Player**. The inheritance hierarchy looks like this:

[![Inheritance hierarchy for the Player Controller.](https://dev.epicgames.com/community/api/documentation/image/ad181a96-7793-4a51-b4c5-a2b83b5dd9f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad181a96-7793-4a51-b4c5-a2b83b5dd9f3?resizing_type=fit)

Inside the Blueprint, notice there are input event nodes that lead to some basic gameplay logic. These input events are specifically related to **Enhanced Input**. You can learn more about how that is configured in the [Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-parrot-for-unreal-engine) documentation. Caching the Parrot Player Character Pawn on Begin Play, we can use that to call base movement functions later. Such as **Add Movement Input**, **Jump**, and **StopJump**.

Time to test! In the Game Mode BP, set the new player controller class and then verify you can use the controller in game:

[![Image showing Player Controller Class location in menu.](https://dev.epicgames.com/community/api/documentation/image/82e27acb-0c56-47bd-b04d-6ffa9e324fe6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82e27acb-0c56-47bd-b04d-6ffa9e324fe6?resizing_type=fit)

   From this drop down in the level editor, verify that the right game mode is selected:

[![Image confirming that the correct GameMode is selected for the project.](https://dev.epicgames.com/community/api/documentation/image/99baab71-5730-469f-a981-349014f96209?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99baab71-5730-469f-a981-349014f96209?resizing_type=fit)

Lastly, make sure that your map has a `PlayerStart` actor and a camera you can view. When you hit the play button you should see your character moving around and animating:

![Short video of Captain Barbarosa character moving in the world.](https://dev.epicgames.com/community/api/documentation/image/03d0b1b5-fec0-47f2-bc2d-cec516d28b4d?resizing_type=fit)

## Parrot Character Movement Component

The base `ACharacter` class has a lot of great functionality built-in. An example of this is the `UCharacterMovement` actor component. The character movement component handles all logic for how a character moves through the world. It supports walking, running, falling, swimming, flying, and custom movement modes. It is definitely worth exploring on your own to get an idea of how basic character movement works and to also get an idea of how powerful actor components are.

For Parrot, the base character movement component did not provide the game feel that the developers were looking for out of the box. However, it did provide a solid foundation to build on. The `UParrotCharacterMovementComponent` C++ class derives from `UCharacterMovementComponent`. We then can set the movement component on the CDO movement component in `BP_ParrotPlayerCharacter` like so:

[![Image of the Parrot Character Movement Component being selected as the component class.](https://dev.epicgames.com/community/api/documentation/image/e17bc4fa-ee48-4574-8b9d-098ad777b0f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e17bc4fa-ee48-4574-8b9d-098ad777b0f3?resizing_type=fit)

But what does the Parrot Movement Component actually do? In essence, the component allows you to define a ‘platformer style’ jump by overriding functions from the base movement component related to jumping. Using some design-tunable values, when a jump occurs, you can modify the player character’s gravity scale and jump velocity to reach an apex height in a fixed amount of time. Upon reaching the apex, you can then start to apply a falling gravity scale. If the player releases the jump input early, you can apply a multiplier to scale the gravity up.

The result is a jump that ‘feels’ more like what you’d expect in a platformer, as opposed to just applying an impulse on the Z-axis.

Leaning on the heavy lifting of the base character movement component, you can just focus the Parrot movement component logic on the jump. The values in the inspector for `BP_ParrotPlayerCharacter` on the movement component are also worth looking at to get a full picture of how all the pieces of the movement component work together. The movement logic can be expanded to fit any variety of use cases.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What are the pieces of a character in Unreal Engine?](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#whatarethepiecesofacharacterinunrealengine?)
* [Importing Art Assets](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#importingartassets)
* [Skeleton, Skeletal Mesh, and Physics Assets](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#skeleton,skeletalmesh,andphysicsassets)
* [Animation Blueprint](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#animationblueprint)
* [Pawn](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#pawn)
* [Player Controller](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#playercontroller)
* [Parrot Character Movement Component](/documentation/en-us/unreal-engine/parrot-pawn-player-controller-and-character-movement-in-unreal-engine?application_version=5.7#parrotcharactermovementcomponent)
