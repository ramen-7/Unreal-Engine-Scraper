<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-parrot-for-unreal-engine?application_version=5.7 -->

# Enhanced Input in Parrot

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
8. Enhanced Input in Parrot

# Enhanced Input in Parrot

How to use Enhanced Input in the Parrot game.

![Enhanced Input in Parrot](https://dev.epicgames.com/community/api/documentation/image/335c42ba-aa9d-48fc-a56a-97fbedeca554?resizing_type=fill&width=1920&height=335)

 On this page

## Enhanced Input

Enhanced Input is a first-party plugin created by Epic Games that we’re using in Parrot. If you are using the latest version of Unreal Engine 5, it should be enabled by default. You can verify it is enabled by going to **Edit > Plugins** and selecting the checkbox.

Enhanced Input replaces the default input system of Unreal Engine and is the standard for complex input handling or runtime control remapping. The [official documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine) from Epic Games has an excellent overview of the system along with how to set up your input assets.

## Core Concepts

To reiterate the official documentation, the core concepts of Enhanced Input you need to understand are as follows:

1. **Input Actions**
2. **Input Mapping Contexts (IMCs)**
3. **Input Modifiers**
4. **Input Triggers**

If you have used Unity’s new input system, these concepts should be familiar.

1. **Input Actions** can best be thought of as ‘what the action that will be performed in the game does’ while in a particular context of the game. For example, if your character is in a car you would want to have ‘Accelerate’ or ‘Brake’ actions.
2. **Input Mapping Contexts** also work with this example. If the player enters or exits the car, you may want to change what certain keys or gamepad buttons do.
3. **Input Triggers** will prevent actions from firing unless all trigger conditions are met. For example, you may want to have the player hold a button for a set period of time in order to trigger an action.
4. **Input Modifiers** alter the value of the input itself. Dead Zones are a common Input Modifier used to ease raw input values. Enhanced Input solves all of these problems for you with some setup.

Let’s look at an example in Parrot. Under `Content/Input/Gameplay` you’ll find an `Actions` folder and an `IMC_Gameplay` asset file. In the `Actions` folder, locate the `IA_Jump` asset.

[![IA_Jump asset details](https://dev.epicgames.com/community/api/documentation/image/487babd9-eb09-4d68-97c7-6fe889be408a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/487babd9-eb09-4d68-97c7-6fe889be408a?resizing_type=fit)

The value type here is `Digital (bool)` which indicates the output type of this action. Under triggers, there are the following types:

* Pressed
* Released’

Looking at this Input Action, you can tell that whatever key or button is mapped must trigger through a press and have a bool output state. The release of the button triggers the end of the action. Another important detail here is that both triggers and modifiers can be overridden by an input mapping context. Let’s take a look at the gameplay input mapping context to see modifier overriding in practice.

[![Gameplay input mapping context](https://dev.epicgames.com/community/api/documentation/image/7fd4fa43-b55f-45ba-a8e0-485dc7983a32?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7fd4fa43-b55f-45ba-a8e0-485dc7983a32?resizing_type=fit)

`IA_MoveAxis` has no trigger set on it, so the value of Gamepad Left Thumbstick X-Axis here will be read immediately when a change is detected. To ease the raw input values, we use a Dead Zone modifier to set the upper and lower input bounds.

An example where we do not provide an override in the IMC is the jump mapping.

[![IMC jump mapping](https://dev.epicgames.com/community/api/documentation/image/799d72c8-68e7-4749-b20f-477a92997b5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/799d72c8-68e7-4749-b20f-477a92997b5e?resizing_type=fit)

Here you’ll notice that the trigger comes from the input action itself, so there’s no need to define a trigger on the mapping. Settings are also inherited from the action but you can ignore that for now as it will be covered in the remapping section.

## Enhanced Input Event Listeners

Now that you have your assets set up, you need to do some setup for runtime use. In Parrot, we bind to the Enhanced Input Local Player Subsystem to set up our event listeners in `BP_ParrotPlayerController`. Off of the `BeginPlay` node we add mapping context for `IMC_Gameplay`.

[![BP_ParrotPlayerController Enhanced Input example](https://dev.epicgames.com/community/api/documentation/image/721f5e5d-3e6b-413a-90e5-f437cef6c16b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/721f5e5d-3e6b-413a-90e5-f437cef6c16b?resizing_type=fit)

Subsystems can be referenced across different scopes. The Enhanced Input Local Player Subsystem is accessible in the player controller. Using that system, you can add an Enhanced Input Mapping context to listen for input events in this event graph. Here, we add the default mapping context for gameplay.

The priority parameter is important here. Input Mapping Contexts are evaluated by their priority so keep that in mind when layering contexts. For now, you’ll just use the gameplay context.

Make note of the `Notify User Settings` parameter set to `true` here - this is necessary for Runtime Input Remapping later.

With your mapping context ready to go, all that’s left is to add the enhanced input event nodes on the actions you care about. Here’s an example of jump:

[![Enhanced Input Action jump node](https://dev.epicgames.com/community/api/documentation/image/d79f4495-08b3-4087-a7a8-62ff697820f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d79f4495-08b3-4087-a7a8-62ff697820f9?resizing_type=fit)

The action starts when the player presses the button and is completed when the player releases the button. Look at the rest of the input actions in `BP_ParrotPlayerController` to see how other input types are processed. You can also bind input events in C++ if you prefer, which is covered in the official documentation.

## Runtime Input Remapping

Enhanced Input has the ability to remap keys bound to Input Actions at runtime. It is worth noting that while this feature does work, it is still experimental so use caution when trying to ship with this feature. In Parrot, we have a **Key Bindings** screen that allows the player to remap their keys. To accomplish this, we pair Enhanced Input with Epic Games' Common UI plugin to provide the correct metadata to the screen’s widgets. Common UI setup is covered in the [User Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine) documentation and you should read that section before proceeding further. With that plugin set up, you can also display platform-specific UI elements.

To start, enable User Settings for Enhanced Input in our project settings. This is located under **Edit > Project Settings > Engine > Enhanced Input**. Set your settings as follows

[![Enhanced Input settings for Parrot Game](https://dev.epicgames.com/community/api/documentation/image/e16e2d3c-00e9-4dcc-9350-520d1abee714?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e16e2d3c-00e9-4dcc-9350-520d1abee714?resizing_type=fit)

Next, navigate to an Input Action asset and adjust the **Player Mappable Key Settings**. The **Name** field needs to be unique across all your input actions. **Display Name** and **Category** are localized in Parrot.

[![Input Action Player Mappable Key Settings for Parrot Game](https://dev.epicgames.com/community/api/documentation/image/59068c4d-f4af-4b97-b852-755519682b25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/59068c4d-f4af-4b97-b852-755519682b25?resizing_type=fit)

You can also override the Player Mappable Key Settings when defining a key in an IMC. For the jump action in the Gameplay IMC, we’ve left this setting as ‘Inherit Settings from Action’ so we don’t need to do anything special there.

[![Gameplay IMC jump action - Inherit Settings from Action](https://dev.epicgames.com/community/api/documentation/image/c5f4207d-942a-423c-8b15-e1e3a14615d9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5f4207d-942a-423c-8b15-e1e3a14615d9?resizing_type=fit)

Verify that when you add your input mapping context on the player controller blueprint, the `Notify User Settings` parameter is set to `true`.

[![Add mapping Context node for Parrot Game](https://dev.epicgames.com/community/api/documentation/image/90d30d30-0fb9-4195-9c4e-eaba693420c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90d30d30-0fb9-4195-9c4e-eaba693420c7?resizing_type=fit)

The next part will cover how we can tie Enhanced Input actions in with Common UI. We will cover what is required for Input Remapping in Parrot but this documentation is supplementary to the official [Common UI quickstart guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/common-ui-quickstart-guide-for-unreal-engine).

For our next step, we created a new IMC: `IMC_UI_Generic` under `Content/Input/UI`.

You should set the Player Mappable Key Settings field on each input action and point it to the appropriate UI metadata data asset. Here’s an example of the generic Accept input action and the metadata asset itself.

[![Generic Accept input action](https://dev.epicgames.com/community/api/documentation/image/40ac7652-7d09-4b95-a3a6-a0a980d9151c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40ac7652-7d09-4b95-a3a6-a0a980d9151c?resizing_type=fit)

[![Accept input action metadata asset](https://dev.epicgames.com/community/api/documentation/image/d187d4bb-a648-44bb-b15b-8f3d3845d50b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d187d4bb-a648-44bb-b15b-8f3d3845d50b?resizing_type=fit)

These IMC and input actions are necessary for Common UI to know about actions invoked by UI navigation. The generic Accept and Back input actions are primary examples of this because a player will always want to invoke them when navigating UI screens. We define these mappings in a CommonUI specific data blueprint that subclasses from `CommonUIInputData`.

[![CommonUI specific data blueprint](https://dev.epicgames.com/community/api/documentation/image/fd85f354-4e71-48ff-8405-921fca26a388?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd85f354-4e71-48ff-8405-921fca26a388?resizing_type=fit)

Next, under **Edit > Project Settings > Common Input Settings**, set the input data to your generic input data blueprint.

[![Set input data to generic input data blueprint.](https://dev.epicgames.com/community/api/documentation/image/b58401eb-35b5-4504-86f0-805d24d34a3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b58401eb-35b5-4504-86f0-805d24d34a3a?resizing_type=fit)

With the important fields set, you can move on to setting up your widget screens. You start with a basic Parrot Screen class for static screens and an activatable one for others. Static screens would be something like the HUD, where you don’t need to worry about UI navigation. An activatable example would be the Pause Menu, since it needs to know when the back button is pressed and it exists on the Menu layer in the game layout.

The screen hierarchy is covered in the [User Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interface-for-parrot-in-unreal-engine) documentation but for reference it’s repeated here:

[![Activatable screen class hierarchy](https://dev.epicgames.com/community/api/documentation/image/b1a4ec01-1cba-4ede-8af0-a7e0d7e7602d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1a4ec01-1cba-4ede-8af0-a7e0d7e7602d?resizing_type=fit)

In the class defaults of BP screens, we set an optional input mapping context. This is applied on activation/deactivation of the widget and you can override it per class.

[![Setting the input mapping context.](https://dev.epicgames.com/community/api/documentation/image/269eadfb-7acb-4a8f-9d32-af200c119d26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/269eadfb-7acb-4a8f-9d32-af200c119d26?resizing_type=fit)

`UParrotActivatableScreen` has an implementation for handling back actions. The `IA_UI_GenericBack` event listener is defined in the event graph of derived blueprints that make use of it. You also need to enable the **Is Back Handler** checkbox in the Details panel.

[![Enable the Is Back Handler checkbox](https://dev.epicgames.com/community/api/documentation/image/3be8e085-0651-4251-8694-d3a32c6e09f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3be8e085-0651-4251-8694-d3a32c6e09f5?resizing_type=fit)

Refer to the comments in the C++ class and BP to see how the Back pattern is used in different screen widgets.

With the base classes covered, take a look at your keybindings screen. `WBP_KeyBindingsScreen` is located under `Content/UI/Widgets/Screens`. The event graph is worth reviewing on your own to see how the `User Settings` and `Key Profile` are queried to pull the `Player Key Mapping` types from Enhanced Input. The data is used to add and populate `WBP_InputSelectorBox` widgets. Inside the `WBP_InputSelectorBox` widget you’ll find two `W_ParrotInputSelector` widgets.

One is used for gamepad inputs and one is for keyboard inputs. The Parrot Input Selector is a custom widget inspired by the built-in Input Selector widget. Both of these widgets enter a selection state, wait for an input, and then update the display:

* For mouse and keyboard, we work with the returned text from the Enhanced Input subsystem and update the display.
* The gamepad implementation relies on Common UI to query for controller specific images. In this case, we set up one for Xbox images called `CommonInput_Gamepad_Xbox` under `Content/Input/UI/Platform`. This class derives from  `UCommonInputBaseControllerData`.

Deriving from this class you can map input keys to brushes with images. Next, set up the controller data under **Edit > Project Settings > Common Input Settings**, then navigate to the platform.

[![Setting up controller data in the Common Input Settings.](https://dev.epicgames.com/community/api/documentation/image/3de886a4-9930-4a32-a458-c4dbb7da33dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3de886a4-9930-4a32-a458-c4dbb7da33dd?resizing_type=fit)

With that data connected, the rest of the work takes place in the widgets. The code and comments in `UParrotInputSelector` and `WBP_InputSelectorBox` are worth looking at to see exactly how the remapping functionality works using the Enhanced Input and Common UI subsystems.

The last important functionality to highlight is how the mapped keys are saved. This takes place in `SaveKeyMappings` in `WBP_KeyBindingsScreen`. This function iterates over all the selector box widgets and then uses the user settings’ built-in `Apply Settings` and `Save Settings` functions. `Save Settings` writes a save game file, `EnhancedInputUserSettings.sav`, to disk. It is located under **Project Directory > Parrot > Saved-SaveGames**.

If everything was set up correctly, you should have a working keybindings screen!

You may notice that in the bottom right corner there is an action widget which updates when the key is remapped. This widget is `WBP_ParrotGamepadActionWidget` and is located under `Content/UI/Widgets/Common`. It makes heavy use of Common UI’s `UCommonActionWidget` class which is built to show platform specific icons given an input action using the common input data we created earlier. Leveraging Common UI, it’s easy to create new widgets as needed that reference your game’s Enhanced Input Actions.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enhanced Input](/documentation/en-us/unreal-engine/enhanced-input-in-parrot-for-unreal-engine?application_version=5.7#enhancedinput)
* [Core Concepts](/documentation/en-us/unreal-engine/enhanced-input-in-parrot-for-unreal-engine?application_version=5.7#coreconcepts)
* [Enhanced Input Event Listeners](/documentation/en-us/unreal-engine/enhanced-input-in-parrot-for-unreal-engine?application_version=5.7#enhancedinputeventlisteners)
* [Runtime Input Remapping](/documentation/en-us/unreal-engine/enhanced-input-in-parrot-for-unreal-engine?application_version=5.7#runtimeinputremapping)
