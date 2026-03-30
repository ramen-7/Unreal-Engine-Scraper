<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7 -->

# VR Template

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Getting Started with XR Development](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine "Getting Started with XR Development")
8. VR Template

# VR Template

Learn how to get started and use the VR Template as a starting point for your VR projects.

![VR Template](https://dev.epicgames.com/community/api/documentation/image/5776de84-1e70-4ef4-af66-4d6dac916d09?resizing_type=fill&width=1920&height=335)

 On this page

The **VR Template** is designed to be a starting point for all of your virtual reality (VR) projects in **Unreal Engine**. It includes encapsulated logic for teleport locomotion, an example VR spectator Blueprint and common input actions, such as grabbing and attaching items to your hand.

[![User stacking cubes in VR with their motion controllers](https://dev.epicgames.com/community/api/documentation/image/9a4d4bc9-d09c-4a7b-924f-3ec8979a6cec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a4d4bc9-d09c-4a7b-924f-3ec8979a6cec?resizing_type=fit)

This page shows you how to get started with the VR Template and how to use it to create your own VR experiences.

## Supported Devices

The VR Template is compatible with the following devices:

* Oculus Mobile

  + Quest 1
  + Quest 2
* Oculus PC

  + Rift S
  + Quest with Oculus Link
* Steam VR

  + Valve Index
  + HTC Vive
  + Android XR

    - Samsung Galaxy XR

Before you can use the VR Template, your device will need to be set up for development in Unreal Engine. See the documentation in [XR Development](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine) for your device to ensure it's set up correctly.

## OpenXR

The VR Template uses the [OpenXR](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) framework, the multi-company standard for VR and AR development. With the OpenXR plugin in Unreal Engine, the template's logic works on multiple platforms and devices without any platform-specific checks or calls.

The OpenXR plugin in Unreal Engine supports extension plugins. You can find extension plugins in the Marketplace or create your own to add functionality to OpenXR that isn't currently in the engine by default.

## Pawn, Game Mode, and Player Start

The following objects determine the rules of the VR Template experience and how it's set up.

| UE Object | Name of Object in VR Template | Location | Description |
| --- | --- | --- | --- |
| [Pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/player-controllers-in-unreal-engine) | VRPawn | Content > VRTemplate > Blueprints | In Unreal Engine, a Pawn is the physical representation of the user and defines how the user interacts with the virtual world. In the VR Template, the Pawn contains the logic for input events from the motion controllers. |
| [Game Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine) | VRGameMode | Content > VRTemplate > Blueprints | The Game Mode object defines the rules of the experience, such as which Pawn object to use. The Game Mode is set in **Project Settings**, in the **Maps & Modes** section. |
| [Player Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine) | Player Start | World Outliner | The Player Start Actor defines where the Pawn is spawned in the virtual world. For VR experiences, the Player Start's origin is the tracking origin in the virtual world. Since the VR Template is designed for standing experiences in VR, the Player Start is located at floor level. |

## Input

Input in the VRTemplate is based on the [Action and Axis Mappings Input System](https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine) in Unreal Engine. See [Input with OpenXR](https://dev.epicgames.com/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine) for more information on how to set up input with OpenXR.

[![Input action and axis mappings](https://dev.epicgames.com/community/api/documentation/image/8336510b-bf18-4d91-ba82-e06220690614?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8336510b-bf18-4d91-ba82-e06220690614?resizing_type=fit)

## Movement

Movement in VR experiences is referred to as *locomotion*. In the VR Template, there are two types of locomotion: **Teleport** and **Snap Turn**. In the Blueprint Editor, open the **VRPawn** to see how both are implemented.

### Teleport

To teleport to different locations in the Level:

1. Move your right Motion Controller's thumbstick or trackpad in the direction you want to move. The Teleport visualizer appears in the level to indicate where you will move to.
2. Release the thumbstick or trackpad to teleport to the selected location.

[![User moving the teleport indicator with their motion controller](https://dev.epicgames.com/community/api/documentation/image/25890bb3-1141-4668-a9e3-53b1ff67ffbe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25890bb3-1141-4668-a9e3-53b1ff67ffbe?resizing_type=fit)

### Snap Turn

To rotate your virtual character without moving your head, move your left Motion Controller's thumbstick or trackpad in the direction you want to turn.

[![User performing snap turns to rotate their view without moving](https://dev.epicgames.com/community/api/documentation/image/9a4767dd-2899-4e01-9ad3-af79c136e3a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a4767dd-2899-4e01-9ad3-af79c136e3a5?resizing_type=fit)

### Setting Allowed Areas for Movement

The Level uses a [Navigation Mesh](samples-and-tutorials/content-examples) to mark where the user is allowed to move. See the **NavModifierVolume** asset **NavModifier\_NoTeleport** as an example of how this can be implemented. The asset's **Area Class** parameter is set to **NavArea\_Null**, which prevents the user from moving to that volume.

[![The teleport indicator disappears when in the No Teleport Zone](https://dev.epicgames.com/community/api/documentation/image/0119aeaf-70e2-4e28-acc3-c0d99bd7c4b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0119aeaf-70e2-4e28-acc3-c0d99bd7c4b9?resizing_type=fit)

*The teleport visualizer disappears when it's in the NavModifier\_NoTeleport volume.*

Press the P key on your keyboard to toggle the visualization of navigable areas.

[![Visualization of the navigable areas in the level](https://dev.epicgames.com/community/api/documentation/image/a9083945-6798-4279-8856-e5bd825929b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9083945-6798-4279-8856-e5bd825929b7?resizing_type=fit)

## Grab

The VR Template shows a couple different ways to pick up objects and attach them to your hands.

To grab an object in the level:

* Reach out to a grabbable object, then press and hold the **Grip** button on your Motion Controller.
* This creates a [Sphere Trace](https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview) around the position of your Motion Controller's GripLocation. If there's an Actor with a **GrabComponent** in that sphere, it becomes attached to the hand that pressed the **Grip** button.
* Release the **Grip** button on the same Motion Controller to detach the object from your hand.

To enable grabbing on an actor, add the GrabComponent blueprint to the actor and select the Grab Type in the Details window. On BeginPlay, the collision profile of the component's parent is set to PhysicsActor, which is the trace channel used for the Sphere Trace in VRPawn.

You can open the GrabComponent Blueprint class to see how the grab system is implemented in the VR template.

### GrabType

You can set the type of grab in an object's **GrabComponent** to define how the object attaches to your hand.

The following grab types are defined in the **GrabType Enum** asset:

* **Free**: The Actor stays in the position and orientation relative to where the Motion Controller grabbed it. See the small cubes as an example.

  [![User grabbing and rotating cubes with their motion controller](https://dev.epicgames.com/community/api/documentation/image/e7185b2e-4b04-4057-a07b-9ed68b962fd2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e7185b2e-4b04-4057-a07b-9ed68b962fd2?resizing_type=fit)
* **Snap**: The Actor has a specific position and orientation relative to the Motion Controller. See the pistols as an example.

  [![User picking up the pistols which snap to the motion controllers](https://dev.epicgames.com/community/api/documentation/image/4068fe3b-90fd-4680-9bd3-09707fe48ffe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4068fe3b-90fd-4680-9bd3-09707fe48ffe?resizing_type=fit)
* **Custom:** With this option, you can add your own logic for the grab action, using the **OnGrabbed** and **OnDropped** events. You can also utilize other exposed variables, such as the **bIsHeld** boolean variable, which is a flag that specifies whether an object is currently held by the user. Examples of other types of custom grab actions that can be created include two-handed grabs, dials, levers, and other complex behaviors, such as Actors that don't overlap geometry when held.

You can define a haptic effect that occurs when grabbing an object by setting the OnGrabHaptic Effect variable in the GrabComponent for the object. An example of a haptic effect includes Motion Controller vibrations.

Important functions used in GrabComponent are abstracted into a common interface using the Blueprint Interface asset VRInteraction BPI. With this Blueprint Interface asset, the VRPawn can simplify its logic and avoid using multiple checks for each kind of object. For more on Blueprint Interface and their benefits, see [Blueprint Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine).

## Menu

Pressing the menu button on your motion controller opens the VR Template's menu. The menu is built with Unreal Motion Graphics (UMG). See [UMG UI Designer](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine) for more information on how to use this tool.

[![User interacting with the VR menu with two options: restart and real life](https://dev.epicgames.com/community/api/documentation/image/debf8229-a07f-4f4d-b7a3-bf8990f43490?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/debf8229-a07f-4f4d-b7a3-bf8990f43490?resizing_type=fit)

In the **Content Browser**, **Content > VRTemplate > Blueprints > WidgetMenu** is the UMG asset for designing and creating logic for the menu, and the **Menu** Blueprint defines how the controller interacts with the Widget.

## VR Spectator

With [Spectator Screen Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-reality-spectator-screen-in-unreal-engine), others can view the VR experience while someone uses the head-mounted display (HMD). The VR Template implements an example of Spectator Screen Mode using the **VR Spectator** Blueprint.

There are two ways to enable Spectator Mode in the VR Template:

* Press **Tab** to toggle Spectator Mode during the session.
* Set **VRSpectator bSpectatorEnabled** to **true**.

VR Spectator is not compatible with Mobile VR devices, such as Oculus Quest..

You can control the VR Spectator to view the user with the HMD in the virtual world, with your mouse and keyboard or a gamepad using the following inputs:

| Action | Mouse &amp; Keyboard Input | Gamepad Input |
| --- | --- | --- |
| **Toggle VRSpectator** | Tab | Bottom Face button |
| **Move Forward** | W | Left Thumbstick up |
| **Move Backward** | S | Left Thumbstick down |
| **Move Left** | A | Left Thumbstick left |
| **Move Right** | D | Left Thumbstick right |
| **Move Up** | E or Spacebar | Right shoulder button |
| **Move Down** | Q | Left shoulder button |
| **Pitch** | Move mouse forward or backward | Right thumbstick Y axis |
| **Yaw** | Move mouse left or right | Right thumbstick X axis |
| **Change Field of View (FOV)** | Move mouse wheel | Right trigger / left trigger |
| **Reset FOV** | Click middle mouse button | N/A |
| **Toggle Fade In and Out** | F | Top Face button |
| **Reset Rotation** | R | N/A |

You can use the VR Spectator as a starting point for implementing multiplayer experiences on the same PC.

* [template](https://dev.epicgames.com/community/search?query=template)
* [xr](https://dev.epicgames.com/community/search?query=xr)
* [vr](https://dev.epicgames.com/community/search?query=vr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Supported Devices](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#supported-devices)
* [OpenXR](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#open-xr)
* [Pawn, Game Mode, and Player Start](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#pawn-game-mode-and-player-start)
* [Input](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#input)
* [Movement](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#movement)
* [Teleport](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#teleport)
* [Snap Turn](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#snap-turn)
* [Setting Allowed Areas for Movement](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#setting-allowed-areas-for-movement)
* [Grab](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#grab)
* [GrabType](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#grab-type)
* [Menu](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#menu)
* [VR Spectator](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine?application_version=5.7#vr-spectator)

Related documents

[XR Development

![XR Development](https://dev.epicgames.com/community/api/documentation/image/af9790b9-1359-4e29-93b2-5adcad591639?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine)

[Developing for Head-Mounted Experiences with OpenXR

![Developing for Head-Mounted Experiences with OpenXR](https://dev.epicgames.com/community/api/documentation/image/e82d4ae1-3113-44c3-9863-528e2ca53a85?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine)

[Making Interactive XR Experiences

![Making Interactive XR Experiences](https://dev.epicgames.com/community/api/documentation/image/d40682e3-646b-4d1d-ae59-10546012822b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine)
