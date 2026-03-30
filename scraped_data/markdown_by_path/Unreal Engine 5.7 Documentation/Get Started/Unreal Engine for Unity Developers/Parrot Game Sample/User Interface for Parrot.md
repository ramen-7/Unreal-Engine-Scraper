<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine?application_version=5.7 -->

# User Interface for Parrot

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
8. User Interface for Parrot

# User Interface for Parrot

How to set up the systems used in the Parrot game user interface.

![User Interface for Parrot](https://dev.epicgames.com/community/api/documentation/image/7d10e554-c811-407f-81d8-fa934bd6a1c2?resizing_type=fill&width=1920&height=335)

 On this page

## UMG

Unreal’s UI system is called **Unreal Motion Graphics** or **UMG**. It is very different from Unity’s standard uGUI system. UMG’s UI Designer authoring tool is most similar to Unity’s UI Toolkit UI Builder if you have worked with that system before. The designer is covered in detail in the official documentation; the [Building Your UI](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-your-ui-in-unreal-engine) and [UMG Best Practices](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-best-practices-in-unreal-engine) pages are particularly useful for transitioning Unity developers. At the core of UMG are **widgets**, which are a series of pre-made functions and hierarchy you can use to construct your user interface.

## CommonUI

**CommonUI** is a first-party plugin created by Epic Games we are using in Parrot. CommonUI sets up “common” styles and actions across widgets that would normally take a lot of time to repeatedly set up manually. A practical example is detecting input device changes and automatically switching input icons on screen. This would take a lot of time to do manually, but Common UI automates this process. CommonUI is also required for Enhanced Input’s key remapping support which is covered more in depth in the [Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine) documentation.

1. To set up CommonUI, you first need to enable it in the Plugins window. In the menu, go to **Edit > Plugins**, search for “Common UI Plugin”, enable it, then restart the editor.

   [![Enable CommonUI plugin](https://dev.epicgames.com/community/api/documentation/image/de99bbc9-ae3b-4eed-84d4-6158c69bb395?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de99bbc9-ae3b-4eed-84d4-6158c69bb395?resizing_type=fit)
2. Go to **Project Settings > General Settings** and change the **Game Viewport Client Class**
   from “GameViewportClient” to “CommonGameViewportClient”. This makes it
   possible for CommonUI widgets to receive input events from the Engine.

   [![Project Settings General Settings - Game Viewport Client Class](https://dev.epicgames.com/community/api/documentation/image/e29fb327-2fdd-42d6-8850-1d27831a3cd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e29fb327-2fdd-42d6-8850-1d27831a3cd1?resizing_type=fit)
3. Under **Project Settings > Common Input Settings**, select the checkbox for **Enable Enhanced Input Support**. This makes it possible for Enhanced Input to work with CommonInput. CommonInput is what handles the input inside CommonUI widgets.

   [![CommonInput settings - Enable Enhanced Input Support](https://dev.epicgames.com/community/api/documentation/image/f14e8ed4-8d14-4ef2-9ac0-9d61e75ecfaa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f14e8ed4-8d14-4ef2-9ac0-9d61e75ecfaa?resizing_type=fit)
4. Lastly, you need to enable some modules in your project for you to use them in code. Go to the `$ProjectName.Build.cs` file, in this case it’s the `Parrot.Build.cs` file. Add the following to the list of **PublicDependencyModuleNames**:

   * `CommonInput`
   * `CommonUI`
   * `EnhancedInput`
   * `GameplayTags`
   * `UMG`

## Parrot Specific Widget Hierarchy

The first UI class to look at in Parrot is `AParrotHUD`. The `HUD` class in Unreal Engine is an actor created for each local player and handles the heads-up display. It has a canvas and debug canvas that can be directly drawn to. You can also assign it as part of your game mode configuration. Where you use this class in Parrot, it is as an actor that owns the root widget from which all your widgets are created and managed.

The class type for this owning widget is UParrotGameLayout. UParrotGameLayout is the C++ base widget container for all your other UI widgets. Inside it, there is a list of “layers” which are of type UCommonActivatableWidgetContainerBase. All other widgets you want to show will get pushed onto one of these layers.

The basic layers we set up are:

* **Game**: The layer where you push your UMG HUD widget
* **GameMenu**: The layer where you push any widget you want to show on top of the HUD.
* **Menu**: The layer for all the screen widgets such as a Pause Screen, Settings Screen, Inventory Screen, and other similar screens.
* **Modal**: The layer for all modal popups.

Only one widget per layer is active at a time. You can push several different screen widgets onto the “Menu” layer, but only the last one is active and shown.

In Parrot, we’ve also created a class hierarchy for activatable screens since those widgets all share common functionality and push to the Menu layer. The class hierarchy is as follows:

[![Activatable screen class hierarchy](https://dev.epicgames.com/community/api/documentation/image/a5ffa5fc-bbbb-4af5-a4ae-867dd4627d05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a5ffa5fc-bbbb-4af5-a4ae-867dd4627d05?resizing_type=fit)

With this setup we create all the UI screens in Parrot.

## Widget Styling

With the Common UI plugin and screen setup you can start styling your widgets. `W_ButtonBase` under `Content/UI/Widgets/Common` is a good example to look at. It uses the `ButtonStyle_Base` styling data under `Content/UI/Styling`. It uses the `UCommonButtonStyle` class from Common UI. There are a lot of options you can customize. Some examples are sounds and brushes based on the state of the button. Common UI has a lot of different styling classes like this depending on the widget you’re using. If you need to do something custom, the engine code for these styled widgets is a good place to look for reference.

## Loading Screen

The loading screen in Parrot uses a first-party plugin from Epic Games: **CommonLoadingScreen**. Another example of this plugin in practice is found in the Lyra sample project from Epic Games. To understand why we’re using this plugin, we first need to understand level loading basics in Unreal Engine.

There are a few ways to handle level loading in UE. A simple approach is to call the `Open Level` node in a blueprint. This function can load a map by a string or a soft object reference to the map. This works well for simple maps but there is a caveat. When this function is invoked, the map is loaded synchronously, which can cause a noticeable stutter depending on how much data needs to be loaded for the new map. Another problem here is that a widget added to the viewport will be tied to a player controller that exists in the previous level. When the level transitions, it will be cleaned up as part of unloading the level.

It can be beneficial to load a new game mode based on the map (for example, Single Player level versus Multiplayer level). But how do you persist the loading screen and avoid the potential loading hitch with `Open Level`? Let’s take a look at `BP_ParrotGameInstance`

[![Parrot Game Instance Blueprint](https://dev.epicgames.com/community/api/documentation/image/602cc239-7e42-4a68-8c73-b5bd93e9394c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/602cc239-7e42-4a68-8c73-b5bd93e9394c?resizing_type=fit)

Asynchronously load your soft object reference to your map data asset. Since you've already loaded the level, you can call Open Level directly without worrying about a synchronous loading hit. The CommonLoadingScreen plugin is also invoked here. The loading screen widget will be invoked "preload" of the next map, and removed during the "postload".

Loading the level asynchronously here solves the problem of assets not being ready by the time Open Level is called. As the comment mentions, the loading screen work is already handled here too. Configuring the plugin is simple and you can set the loading screen widget from **Edit > Project Settings > Common Loading Screen**.

[![Common Loading Screen settings](https://dev.epicgames.com/community/api/documentation/image/58ed08df-8a45-4df4-a924-ffaa0ca78243?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58ed08df-8a45-4df4-a924-ffaa0ca78243?resizing_type=fit)

Also pay attention to the debugging toggles here. Testing with these in-editor gives you a better idea of how the loading screen will perform in a packaged version.

You now have levels loading with a loading screen. `BP_ParrotGameInstance` is worth exploring further on your own to see how we set up the single player and multiplayer level order. Setup of the game state is covered in the [Unreal Gameplay Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-gameplay-framework-in-parrot) documentation.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [UMG](/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine?application_version=5.7#umg)
* [CommonUI](/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine?application_version=5.7#commonui)
* [Parrot Specific Widget Hierarchy](/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine?application_version=5.7#parrotspecificwidgethierarchy)
* [Widget Styling](/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine?application_version=5.7#widgetstyling)
* [Loading Screen](/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine?application_version=5.7#loadingscreen)
