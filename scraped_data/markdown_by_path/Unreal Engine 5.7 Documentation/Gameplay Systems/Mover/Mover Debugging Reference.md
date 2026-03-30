<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mover-debugging-reference-for-unreal-engine?application_version=5.7 -->

# Mover Debugging Reference

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
7. Mover Debugging Reference

# Mover Debugging Reference

Learn how to debug your Mover project.

![Mover Debugging Reference](https://dev.epicgames.com/community/api/documentation/image/c3d6e40b-4aa8-4348-a993-4e68af7f7108?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

This document covers some debugging options to help you solve problems with your **Mover** project.

## Visualization and State Readout Information

![Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c97529f-43fe-46f8-a1e3-db0acc9b5ccd/visualization.png)

You can review visualization and state readout information through the [Gameplay Debugger Tool (GDT)](/documentation/en-us/unreal-engine/using-the-gameplay-debugger-in-unreal-engine).

To activate GDT for Mover during Play In Editor (PIE):

1. Press the apostrophe key (`'`) to display the GDT panel.
2. In the GDT panel, find the number associated with the Mover category.
3. Press the Mover category number on your numpad.

GDT selects the locally-controlled player character by default, but you can change this via GDT input and `gdt.*` console commands.

You can find Mover logging information in the Output Log by filtering with the **LogMover** category.

## Console Commands

| **Command** | **Description** |
| --- | --- |
| `Mover.Debug.MaxMoveIntentDrawLength=X` | The max length (in cm) of the move intent visualization arrow. |
| `Mover.Debug.OrientationDrawLength=X` | The max length (in cm) of the orientation visualization arrows. |
| `Mover.Debug.ShowTrail` | Toggles the trail display for the selected server-controlled actor. The trail displays the previous path and rollback information. For the local player, use `Mover.LocalPlayer.ShowTrail` instead. |
| `Mover.Debug.ShowTrajectory` | Toggles the trajectory prediction display for the selected server-controlled actor. For the local player, use `Mover.LocalPlayer.ShowTrajectory` instead. |
| `Mover.Debug.ShowCorrections` | Toggles the network corrections display for the selected server-controlled actor. For the local player, use `Mover.LocalPlayer.ShowCorrections` instead. |
| `Mover.Debug.LogAnimRootMotionSteps=X` | If enabled, logs detailed information about anim root motion layered moves. (0: Disable, 1: Enable) |
| `Mover.Debug.LogRootMotionAttrSteps=X` | If enabled, logs detailed information about root motion attribute layered moves. (0: Disable, 1: Enable) |
| `Mover.Debug.DisableRootMotionAttributes=X` | If enabled, ignores contributions from root motion attributes in favor of other Mover influences. (0: Disable, 1: Enable) |
| `Mover.LocalPlayer.ShowTrail` | Toggles the player's trail according to the Mover component. The trail displays the previous path and rollback information. By default, this applies to the first local player controller. |
| `Mover.LocalPlayer.ShowTrajectory` | Toggles the player's trajectory according to the Mover component. By default, this applies to the first local player controller. |
| `Mover.LocalPlayer.ShowCorrections` | Toggles the player's network corrections display. Green represents the updated position after correction, and red represents the position before correction. By default, this applies to the first local player controller. |

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [character](https://dev.epicgames.com/community/search?query=character)
* [mover](https://dev.epicgames.com/community/search?query=mover)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Visualization and State Readout Information](/documentation/en-us/unreal-engine/mover-debugging-reference-for-unreal-engine?application_version=5.7#visualizationandstatereadoutinformation)
* [Console Commands](/documentation/en-us/unreal-engine/mover-debugging-reference-for-unreal-engine?application_version=5.7#consolecommands)
