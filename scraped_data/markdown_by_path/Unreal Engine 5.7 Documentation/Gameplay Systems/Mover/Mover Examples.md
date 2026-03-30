<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7 -->

# Mover Examples

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
6. [Mover](/documentation/en-us/unreal-engine/mover-in-unreal-engine "Mover")
7. Mover Examples

# Mover Examples

A guide to the example content included in the Mover Examples plugin.

![Mover Examples](https://dev.epicgames.com/community/api/documentation/image/b877691c-a122-43e8-a57d-17c8a1045411?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

This document guides you through some example content in the **Mover Examples** plugin to introduce you to the **Mover** system.

The example content in the Mover Examples plugin is not intended to be used directly in a shipping product.

## Prerequisites

You must enable the Mover and Mover Examples plugins and adjust your project settings before using the example content.

### Enable Plugins

Enable the Mover and Mover Examples plugins in your project, by doing the following:

1. Open the **Plugin** panel by selecting **Edit > Plugins**.
2. In the **Plugin** panel, input "Mover" into the search bar.
3. Enable the **Mover** and **Mover Examples** plugins.
4. Restart **Unreal Editor**.

### Adjust Project Settings

Make the following adjustments to your project settings:

1. Open the **Project Settings** panel by selecting **Edit > Project Settings**.
2. Select the **Network Prediction** filter under the **Project** heading or use the search bar to find the following settings and adjust their values:
   1. Set **Preferred Ticking Policy** to **Fixed**.
   2. Set **Simulated Proxy Network LOD** to **Interpolated**.
   3. Set **Enable Fixed Tick Smoothing** to **True**.

These settings are recommendations for general use. We encourage you to explore and review the tooltips on related settings.

## Example Content Overview

The Mover Examples plugin contains a variety of valuable content for learning Mover, including levels and pawns.

### Levels

The Mover Examples plugin provides several example levels that demonstrate Mover functionality, including the following:

* **L\_CharacterMovementBasics**: Showcases various terrain features, movement, and an extended pawn with additional movement capabilities.
* **L\_PhysicsSimulatedCharacter**: Provides an example implementation of a physics-based pawn. For more information, see [Physics-Based Movement](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine#physics-basedmovement).
* **L\_LayeredMoves**: Demonstrates many layered move types with a variety of options.
* **L\_PathfindingMovement**: Focuses on demonstrating AI-driven movement methods with pathfinding, including a NavWalking mode.

You can find each level above and more in `All/Engine/Plugins/Mover Examples Content/Maps`.

Open each level and play around to get a better understanding of Mover's functionality. Each level is broken down into sections with notes to express the purpose of each area.

![Example Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b79e187-b2c4-4d9f-b177-3d08fea9fe0b/example-level.png)

### Pawns

The Mover Examples plugin provides several example pawn implementations that demonstrate Mover functionality, including the following:

* **AnimatedMannyPawn**: Designed to perform similarly to the default pawn used in project templates.
* **AnimatedMannyPawnExtended**: Provides an example of extending the default pawn implementation with additional movement capabilities, including dashing, multi-jump, vaulting, and ziplining. You can possess this pawn in the `L_CharacterMovementBasics` level by moving into the **Swap For Extended Pawn** area.
* **PathFollowingMannyPawn**: Demonstrates AI-driven path following as an example of nav-mesh movement.
* **PhysicsMannyPawn**: Implemented to use Chaos Networked Physics instead of Network Prediction. The associated movement modes are also customized to work within the constraints of the physics system. For more information, see [Physics-Based Movement](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine#physics-basedmovement).

The pawns above and more are in `All/Engine/Plugins/Mover Examples Content/Pawns`.

To familiarize yourself with an example pawn's movement modes and settings, you can do the following:

1. In the **Content Browser**, double-click the desired pawn to open the **Blueprint Editor**.
2. In the **Components** panel, select the **Character Motion Component (MoverComponent)**.
3. In the **Details** panel, review the pawn's properties. The **Movement Modes** and **Shared Settings** properties are good places to start.

![Mode Details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0edee7e4-a976-4264-b104-8a44dac7271d/mode-details.png)


The controls for player-controlled pawns will appear in the bottom-left corner of your viewport when playing a level.

## Physics-Based Movement

The `L_PhysicsSimulatedCharacter` level showcases the `PhysicsMannyPawn`, which is driven by the Chaos Networked Physics system instead of the Network Prediction plugin.

In addition to the changes in [Adjust Project Settings](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine#adjustprojectsettings), you must make the following changes to your project settings:

1. Enable **Tick Physics Async**.
2. For network play, enable **Enable Physics Prediction**.

The physics simulation runs ahead of the game thread at a fixed tick rate. As the simulation progresses, the game thread's character representation smoothly interpolates towards the most recent physics state. However, this means there is some delay between player input and pawn movement.

### Additional Considerations

* The **Character Ground Constraint** from the physics system handles performing the proposed motion that the Mover system generates.
* You need to set up replication for other interactable physics objects. Otherwise, the server and client will desync.
* Interactions with moving non-physics objects will produce poor results due to ticking differences between the physics simulation and the rest of the game world.
* Physics-driven Mover actors are not synchronized with those using Network Prediction.
* **Gameplay Events** are not connected to the Mover system.

## Customization and Extension

You can customize Mover actors by changing the movement mode map on the MoverComponent to grant access to new ways of moving through the world. You can switch between these modes during runtime using the `QueueNextMode` function or, if using the default character input struct, by setting the `SuggestedMovementMode`. You can even add or remove modes during runtime.

There are known issues with removing and replacing elements of the movement mode map on instances of actors placed within levels, potentially preventing these pawns from moving.

The default character movement modes have various settings to tailor their behavior and feel. You can find the individual settings on the modes themselves and the settings shared by multiple modes under Shared Settings.

To define your own movement modes, follow `UZipliningMode` as an example. Following this example, you will override the following functions:

* `OnGenerateMove`: Creates a proposed move.
* `OnSimulationTick`: Simulates the proposed move through the world to create the next state snapshot.

The zipline implementation adds some custom state data to track the character's progress along the line. `FZipliningState` defines the data, and `UZipliningMode::OnSimulationTick` adds and modifies it as part of the movement simulation state. The custom state data requires a native C++ definition, as does custom input data.

For inputs, the pawns in MoverExamples use a combination of C++ and Blueprint functions to author inputs for the movement simulation.

The common inputs (directional moving, jumping) for these pawns are authored in `AMoverExamplesCharacter::OnProductInput` with additional custom inputs authored in the `OnProduceInput` Blueprint function found in `AnimatedMannyPawnExtended`.

Although you can produce custom input in Blueprint, adding your own data requires C++. You can follow `FMoverExampleAbilityInputs` for an example of this. The type is defined in C++ but added to the simulation and authored in Blueprint.

The zipline example also demonstrates custom transitions and the modular addition of new movement mechanics in `UZiplineStartTransition` and `UZiplineEndTransition`.

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [character](https://dev.epicgames.com/community/search?query=character)
* [mover](https://dev.epicgames.com/community/search?query=mover)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#prerequisites)
* [Enable Plugins](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#enableplugins)
* [Adjust Project Settings](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#adjustprojectsettings)
* [Example Content Overview](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#examplecontentoverview)
* [Levels](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#levels)
* [Pawns](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#pawns)
* [Physics-Based Movement](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#physics-basedmovement)
* [Additional Considerations](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#additionalconsiderations)
* [Customization and Extension](/documentation/en-us/unreal-engine/mover-examples-in-unreal-engine?application_version=5.7#customizationandextension)
