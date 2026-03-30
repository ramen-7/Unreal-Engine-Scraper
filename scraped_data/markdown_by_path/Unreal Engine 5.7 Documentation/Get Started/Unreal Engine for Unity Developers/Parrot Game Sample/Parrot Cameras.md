<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/parrot-cameras-in-unreal-engine?application_version=5.7 -->

# Parrot Cameras

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
8. Parrot Cameras

# Parrot Cameras

All about the Project Parrot cameras.

![Parrot Cameras](https://dev.epicgames.com/community/api/documentation/image/f668814a-cd80-4327-8c52-15156977ddd2?resizing_type=fill&width=1920&height=335)

 On this page

There are many different ways to work with a **camera** in games, and it can vary a lot depending on the type of game that you’re making. In Unreal Engine, cameras are typically composed of an actor with a spring-arm component, and a camera component, which renders the view. For basic camera setup, check out [Using Cameras in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-cameras-in-unreal-engine).

In this document, the developers will cover how they decided to implement the camera for Parrot specifically, and any settings of note worth pointing out.

### Parrot Camera Subsystem

To start, each map that may have camera settings specific to the world was identified.

The developers created `UParrotCameraSubsystem` which shares the lifetime of the world and initializes the camera with these settings on `BeginPlay`. The map specific settings are stored on `AParrotWorldSettings`, which is useful for storing any per map data. For the camera, this is the desired camera class, the movement mode, and the upper/lower boundary on Z where we no longer want the camera to follow the player. The class itself is optional and not providing one is a valid path. This is done on the main menu.

For the reasoning on choosing to use a subsystem, refer to the [Subsystems in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsystems-in-parrot-in-unreal-engine) documentation.

The world settings can be found in the **World Settings** panel in the editor.

[![Image of World Settings tab with what is chosen for each option.](https://dev.epicgames.com/community/api/documentation/image/a9ea8ff9-4f25-4a64-81b2-c243ab9a12c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9ea8ff9-4f25-4a64-81b2-c243ab9a12c7?resizing_type=fit)

### Parrot Camera

`AParrotCamera` is where the bulk of the logic happens. When the camera is initialized by the subsystem, it is given: the player to follow, the movement mode, and the boundaries from the world settings.

The camera has three possible movement modes: **None**, **Fixed**, and **Follow**.

**None** is exactly as described. The camera will do nothing.

The **Fixed** movement mode is simple. When the player enters a bound volume, a fixed location is given to the camera by the camera subsystem and it will interpolate to it. The player is then free to move about until the movement mode is updated.

The **Follow** movement mode is more complex and best understood by looking at `Content/Blueprints/BP_PlatformerCamera` for a visual reference. `AParrotCamera` has a movement-trigger box and a blocking mesh as default subobjects. This means every instance of AParrotCamera has them automatically added in its hierarchy. Both are aligned with the camera frustum, spring arm, and perspective for the desired effect. Both of these components are attached to the camera actor and follow it within the world.

The blocking mesh prevents the player from moving backwards by colliding with the player in the world.

When the player overlaps the movement-trigger box, the camera will attempt to interpolate to the player’s X value at a set speed. The speed is also multiplied by the player’s distance past the left-most extent of the trigger volume. This way, the farther the player is into the volume, the faster the camera should move to catch up.

The result is that the player is able to roam freely on the left side of the screen up to the blocking mesh, yet the camera will move with the player when they pass the threshold. This provides a nice effect as the player moves through the world on the X-axis.

Another area of note on the Follow movement mode is that the player’s last known location is tracked. If the player’s Z surpasses the world bounds, or the player character is destroyed, we interpolate the camera to the player’s last known location. This prevents any jarring camera behavior based on the player’s movement/state.

Lastly, the **Camera Component** itself on `BP_PlatformerCamera` has a few settings worth pointing out. The **Projection Mode** is Perspective with a 90 degree FOV and an aspect ratio of 1.77 which is standard HD. Under **Camera Options**, we constrain the aspect ratio so that the camera always looks correct regardless of the application's running resolution.

[![View of camera settings menu with FOV being 90 degrees and aspect ratio shown.](https://dev.epicgames.com/community/api/documentation/image/4a6dfba4-194e-4ff1-bc07-9f6adc9c963d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a6dfba4-194e-4ff1-bc07-9f6adc9c963d?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Parrot Camera Subsystem](/documentation/en-us/unreal-engine/parrot-cameras-in-unreal-engine?application_version=5.7#parrotcamerasubsystem)
* [Parrot Camera](/documentation/en-us/unreal-engine/parrot-cameras-in-unreal-engine?application_version=5.7#parrotcamera)
