<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7 -->

# In-Editor Testing (Play and Simulate)

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Level Editor](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine "Level Editor")
7. In-Editor Testing (Play and Simulate)

# In-Editor Testing (Play and Simulate)

Guide to testing levels and gameplay directly in the Editor

![In-Editor Testing (Play and Simulate)](https://dev.epicgames.com/community/api/documentation/image/2f048745-5dcf-45b5-90b5-edab7dd24dd2?resizing_type=fill&width=1920&height=335)

 On this page

Operating System 

×Windows

Select an option from the dropdown to see content relevant to it.

Unreal Editor allows you to spawn a player anywhere and instantly preview your game from within the editor without waiting for files to save. There are two preview types available: **Play In Editor** (PIE) which is directly accessed via the **Play** button located on the Main Toolbar
and **Simulate In Editor** (SIE) which is accessed via the **Play** dropdown menu (**Alt+S**). The in-editor preview system supports toggling between Play In Editor and Simulate In Editor sessions, so that you can quickly iterate on gameplay and asset tweaks
and see how your game changes as a result.

When you launch a game preview session, the editor quickly creates a duplicate copy of your level. Changes can be saved back to the editor copy of the level using Keep Simulation Changes.
This duplication of the level keeps the editor's copy of the world safely immutable.

Game previewing includes level streaming, and the **Outliner** will update accordingly so that you can select and edit Actors that are streamed in as a result of gameplay.
Any Actors you have selected when you begin testing your game with a Play In Editor or Simulate In Editor session will remain selected. The reverse is also true, so any Actors selected
during in-editor testing will remain selected after you end the testing session. This means that the **Details** panel will show the properties for an Actor you select because you want to change its
appearance or behavior, even if you begin gameplay in a distant section of the level.

## Toolbar

You can begin a Simulate In Editor or Play In Editor session from either the **Level Editor** or the **Blueprint Editor**, using the appropriate Toolbar buttons or dropdown menus.

From the **Level Editor**, you can click the **Play** button.

[![Toolbar Buttons](https://dev.epicgames.com/community/api/documentation/image/4ca96da1-99eb-405a-a3f8-65dae5181685?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ca96da1-99eb-405a-a3f8-65dae5181685?resizing_type=fit)

Click image for full size.

This will start a Play In Editor (PIE) session, so that gameplay can be tested directly from the editor. Different modes and options for Play In Editor sessions can be selected in the dropdown menu, and the Play In button will use the same settings that were selected for the previous session.

Click the **Play** dropdown button to display the **Play Options** dropdown menu.

[![Play Menu](https://dev.epicgames.com/community/api/documentation/image/1e2df8c6-3d9b-4d91-a90b-875d99f98f3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e2df8c6-3d9b-4d91-a90b-875d99f98f3d?resizing_type=fit)

Click image for full size.

You can change your [Play In Editor mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine#modes), set basic [networked Play In Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-in-editor-multiplayer-options-in-unreal-engine) options, or open the [full Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine). Clicking on **Simulate** begins Simulate In Editor mode, which changes the testing section of the Toolbar. While simulating, you can pause or stop gameplay, as well as swap to a Play In Editor session with the **Possess** button.

[![Simulate In Editor Toolbar](https://dev.epicgames.com/community/api/documentation/image/7b2beacf-a541-4592-824c-e7d600686d35?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b2beacf-a541-4592-824c-e7d600686d35?resizing_type=fit)

Click image for full size.

## Play In Editor

Clicking on the **Play** button in the toolbar (**Alt + P**) or selecting **Play From Here** in the **Viewport** context menu begins a Play In Editor session.
Play In Editor allows you to play the current level directly from the editor, so that you can test gameplay functionality, including player controls and level events triggered by players' actions.

### Modes

Launching a game preview with a different mode will change the default Play mode that is activated by the **Play** button.

#### Display Types

$ Viewport : Gameplay will be shown in the active Level Editor viewport.

**Click to see full-size image:**

[![](https://dev.epicgames.com/community/api/documentation/image/80b76fd5-2296-494f-8602-e1b6a8b70c1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80b76fd5-2296-494f-8602-e1b6a8b70c1c?resizing_type=fit)

This is the only display type that allows toggling between *Play In Editor* and *Simulate in Editor* by using the Possess and Eject buttons. In the **Viewport** modes, you can also use the Pause and Stop buttons to interrupt gameplay.

[![](https://dev.epicgames.com/community/api/documentation/image/c42bf45b-2225-411b-b42b-b74cef8827aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c42bf45b-2225-411b-b42b-b74cef8827aa?resizing_type=fit)

By default, the preview window does not automatically get control of the mouse cursor. You can click in the preview window to turn control of the mouse cursor over to the game.

[![](https://dev.epicgames.com/community/api/documentation/image/1bee3fbb-c2b9-4356-aca3-cf43b22cc2a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1bee3fbb-c2b9-4356-aca3-cf43b22cc2a7?resizing_type=fit)

To regain control of the mouse cursor, press **Shift+F1**.

[![](https://dev.epicgames.com/community/api/documentation/image/40d1a788-4262-42de-b83a-801aa02090e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40d1a788-4262-42de-b83a-801aa02090e9?resizing_type=fit)

Small labels will appear in the preview window when you toggle mouse control. To change the options for mouse control or how the mouse control label displays, use the [Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine).

$ New Window : Gameplay will be shown in a new window. To change the default size of new windows, use the [Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine).

**Click to see full-size image:**

[![](https://dev.epicgames.com/community/api/documentation/image/034c80b4-454e-4254-8a4d-b24d5f88d145?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/034c80b4-454e-4254-8a4d-b24d5f88d145?resizing_type=fit)

When playing a game preview in a new window, you cannot switch to a *Simulate In Editor* session. However, you can still pause and stop gameplay with the toolbar buttons that appear.

[![](https://dev.epicgames.com/community/api/documentation/image/8fa783b1-63e5-4266-ba32-12ab38db54ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8fa783b1-63e5-4266-ba32-12ab38db54ff?resizing_type=fit)

By default, playing in a new window will give mouse control to the game automatically. You can press **Shift+F1** to regain control of your mouse cursor.

$ Standalone Game : Gameplay will be shown in a new window that runs in its own process. To change the default standalone window size, use the [Play In Editor settings window](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-settings-in-unreal-engine).

**Click to see full-size image:**

[![](https://dev.epicgames.com/community/api/documentation/image/c01f1811-cfe7-4f42-89c3-c2d593d2a88a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c01f1811-cfe7-4f42-89c3-c2d593d2a88a?resizing_type=fit)

Because this display type lets you play the game in its own process, you cannot pause or stop the game. You also cannot switch to *Simulate In Editor*. As a result, the toolbar buttons do not change when playing a standalone game preview.

By default, playing in a standalone window will give mouse control to the game automatically. You can press **Shift+F1** to regain control of your mouse cursor.

#### Start Locations

$ Camera Location : Gameplay begins at the current camera location.

$ Default Player Start : Gameplay begins at the Player Start location.

If your game uses a NavMesh for either player-controlled or AI-controlled movement, using Camera Location for your Play In Editor starting location could cause you to spawn
in a location that breaks pathing. In this case, starting a Play In Editor session from the Default Player Start is recommended.

### Play From Here

You can access an additional Play In Editor mode by right-clicking in the **Viewport** and selecting **Play From Here**.

[![Play from here](https://dev.epicgames.com/community/api/documentation/image/e59cdbee-eec8-4ed2-9de4-f214943e62aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e59cdbee-eec8-4ed2-9de4-f214943e62aa?resizing_type=fit)

Click image for full size.

**Play From Here** begins gameplay at the location that you have clicked, and acts as if your **Display Type** is set to **Level Viewport**.

### Switching to Simulate In Editor

While in a Play In Editor session in a viewport, press **Shift+F1** to regain your mouse control. Then, click on **Eject** in the **Toolbar** to switch to a Simulate In Editor session.
You will detach from the player controller, and begin a Simulate In Editor session at your current location.

You can also press the **Eject** keyboard shortcut (**F10**) to switch to Simulate In Editor from Play In Editor.

If you have set up more than one client for your Play In Editor testing with [Networked Play In Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-in-editor-multiplayer-options-in-unreal-engine), only the first session (the one in the **Viewport**) will support
switching to Simulate In Editor mode. Even for single-player gameplay testing, *Play In Editor* sessions where the game is in a new window or in a standalone game process do not support switching to Simulate In Editor.

## Simulate In Editor

Using the **Simulate** button begins a **Simulate In Editor** session in the currently active viewport. While simulating, gameplay begins, including the execution of Blueprints and C++ code that do not rely on a player's interaction with the game. While simulating, you have full access to the Editor's tools, so you can modify the scene and its contents, or even place new Actors. You can also select and inspect Pawns controlled by AI right as they are performing actions, and quickly debug and tweak gameplay behaviors. However, because you are not using a PlayerController while simulating, you cannot enter game controls. You can save certain changes made in a Simulate In Editor session using **Keep Simulation Changes**.

### Switching to Play In Editor

While in a Simulate In Editor session, you can click on **Possess** in the **Toolbar** to switch to a Play In Editor session.
You will attach to the player controller, and begin a Play In Editor session in the active level viewport.

You can also press the **Possess** keyboard shortcut (**F10**) to switch to Play In Editor from Simulate In Editor.

If you began in-editor testing with a Simulate In Editor session, and then used Possess to attach to the player controller, you will begin
your Play In Editor session at the default player start. This is equivalent to selecting **Play** > **Selected Viewport** > **Default Player Start** from the **Play** dropdown menu.
However, if you had previously swapped from a Play In Editor session to a Simulate In Editor session, without leaving in-editor testing mode, when you click **Possess**,
you will re-attach to the player controller and resume gameplay at the location in the level where you previously clicked on **Eject**.

## Testing Gameplay

### Blueprints

When you enter Play In Editor or Simulate In Editor mode, all your Blueprint are compiled, although they are not saved. While playing or simulating, all Blueprint graphs are read-only, so you cannot add additional nodes or connect wires differently.

[![Simulating readonly](https://dev.epicgames.com/community/api/documentation/image/c0694ce2-627e-4e1f-983d-3f9f7d00c956?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0694ce2-627e-4e1f-983d-3f9f7d00c956?resizing_type=fit)

However, you can change Blueprint defaults while a preview session is active, and the changes will be applied to all instances of that Blueprint in the level you are testing.

### C++

For projects that contain C++ code, there is a **Compile** button on the **Level Editor Toolbar**. This button recompiles and reloads game code on the fly. If you change a property or a function in
a C++ file in your project, clicking the **Compile** button will recompile and reload your game module, so that your code changes are reflected in the editor. In some cases, you can even compile
while using Play In Editor or Simulate In Editor, and your code changes will update without you needing to stop gameplay or simulation.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Toolbar](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#toolbar)
* [Play In Editor](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#play-in-editor)
* [Modes](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#modes)
* [Display Types](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#display-types)
* [Start Locations](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#start-locations)
* [Play From Here](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#play-from-here)
* [Switching to Simulate In Editor](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#switching-to-simulate-in-editor)
* [Simulate In Editor](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#simulate-in-editor)
* [Switching to Play In Editor](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#switching-to-play-in-editor)
* [Testing Gameplay](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#testing-gameplay)
* [Blueprints](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#blueprints)
* [C++](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine?application_version=5.7#c)
