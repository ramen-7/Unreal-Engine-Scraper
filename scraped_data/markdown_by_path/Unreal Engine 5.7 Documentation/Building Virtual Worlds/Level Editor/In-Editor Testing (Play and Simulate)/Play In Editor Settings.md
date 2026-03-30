<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7 -->

# Play In Editor Settings

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
7. [In-Editor Testing (Play and Simulate)](/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine "In-Editor Testing (Play and Simulate)")
8. Play In Editor Settings

# Play In Editor Settings

Set up window sizes and other options for the Play In feature.

![Play In Editor Settings](https://dev.epicgames.com/community/api/documentation/image/bdcf3e25-f341-4cbd-b28b-fdf4863924ef?resizing_type=fill&width=1920&height=335)

 On this page

Choose your operating system

Windows
macOS
Linux

There are two ways to open the **Play** settings panel.

* Open the **Play** settings panel by clicking **Edit** > **Editor Preferences**.

  [![PIE Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf634d0c-e34a-42bc-9698-d0a80c51f68e/01-pie-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf634d0c-e34a-42bc-9698-d0a80c51f68e/01-pie-settings.png)

  Click image for full size.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a84e12a-5dbb-46ef-9a0f-14a6c61e622e/piesettings_mac.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a84e12a-5dbb-46ef-9a0f-14a6c61e622e/piesettings_mac.png)

  Then, select the **Play** in the Editor Preferences window.

  [![PIE Setting from Preferences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a51a0b7-8230-4ebb-969a-50284ea00bb5/02-pie-setting-from-preferences.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a51a0b7-8230-4ebb-969a-50284ea00bb5/02-pie-setting-from-preferences.png)

  Click image for full size.
* Or, from the **Play** dropdown menu, click **Advanced Settings**.

  [![PIE Settings from Play Button Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d31689f-5562-49d3-8ebd-cc89336ac977/03-pie-settings-from-play-button-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d31689f-5562-49d3-8ebd-cc89336ac977/03-pie-settings-from-play-button-menu.png)

  Click image for full size.

## Play In Editor

The **Play In Editor** settings allow you to change different behaviors during a session. These settings only apply for Play In Editor sessions that display in the **Level Viewport**.
As a result, there are no default window sizes to set.

| **Setting** | **Description** |
| --- | --- |
| **Game Gets Mouse Control** | Enables game mouse control when PIE starts. |
| **Use Mouse for Touch** | Sends mouse movement and clicks as touch events during PIE |
| **Show Mouse Control Label** | Displays "Click for Mouse Control" and "Shift + F1 for Mouse Cursor" messages during PIE. |
| **Mouse Control Label Position** | Determinies location to anchor the Mouse Control label on screen during PIE. |
| **Viewport Gets HMDControl** | Determines if HMD orientation should be used while playing in viewport. |
| **Should Minimize Editor on VRPIE** | Minimizes editor on VR PIE. |
| **Auto Recompile Blueprints** | Determines whether to automatically recompile Blueprints used in the level when initiating a Play In Editor session. |
| **Enable Game Sounds** | Enables sound during a Play In Editor session. |
| **Play In Editor Sound Quality Level** | Determines quality level of sound during a Play In Editor session. |
| **Stream Sub-Levels during Play in Editor** | Streams sub-levels from disk instead of duplicating editor sub-levels. |
| **Enable PIE Enter and Exit Sounds** | Plays a sound when exiting or entering PIE. |

## Game Viewport Settings

| **Setting** | **Description** |
| --- | --- |
| **New Viewport Resolution** | Sets the width and height of floating Play In Editor windows (in pixels):   * Pick from a list of common window sizes, including settings for devices like phones and tablets. * **New Window Width**: Sets the width of the new viewport window (in pixels). A value of zero will use the desktop's screen resolution. * **New Window Height**: Sets the height of the new viewport window (in pixels). A value of zero will use the desktop's screen resolution. |
| **New Window Postion** | Sets the screen coordinates for the top-left corner of floating Play In Editor windows (in pixels) This will affect both Play In New Editor Window and Standalone Game:   * **Left Position**: Sets the position of the new viewport on the screen, starting from the left (in pixels). * **Top Position**: Sets the position of the new viewport on the screen, starting from the top (in pixels). * **Center Viewport Position**: Enable to always center the position of the first viewport to screen. |
| **Safe Zone Preview** | Enables a visual preview of the device safe zone for UI testing. |

## Play in New Window

When starting a Play In Editor session that displays in a new window, these settings determine the size and starting position of the new window that appears.

| **Setting** | **Description** |
| --- | --- |
| **Always On Top** | Always have the PIE window on top of the parent windows |

## Play in Standalone Game

When starting a Play In Editor session that displays in a standalone game window, these settings determine the size and starting position of the new window that appears. You can use these options to pass additional command line settings on to the game client.

| **Setting** | **Description** |
| --- | --- |
| **Client Command Line Options** | Generates a command line for additional settings that will be passed to the game clients:   * **Disable Sound (~nosound)**: Disables sound in your standalone games. |
| **Additional Launch Parameters** | Adds extra parameters to be included as part of the command line for standalone games. |
| **Additional Launch Parameters for Mobile** | Adds extra parameters to be included as part of the command line for mobile-on-PC standalone games. |

## Multiplayer Options

These are basic and advanced options for [Play In Editor Multiplayer Options](/documentation/en-us/unreal-engine/play-in-editor-multiplayer-options-in-unreal-engine). In addition to the number of players and dedicated server options
from the **Play** dropdown menu, there are settings for URL parameters, gamepad routing, and reverting to the multiple-process testing method.

| **Setting** | **Description** |
| --- | --- |
| **Launch Separate Server** | Launches a separate server even if the net mode doesn't require it. This allows you to test offline --> server workflows by connecting to a server from the offline game. |
| **Play Net Mode** | Sets the net mode used for Play In Editor session:   * **Play Standalone**: Starts a standalone game. This will not create a dedicated server, nor automatically connect to one. * **Play As Listen Server**: Enables the Editor to act as both the server and the client. Additional clients can be opened depending on the number of clients. * **Play As Client**: Enables the Editor to act as a client. A dedicated server spawns behind the scenes to connect to. |
| **Run Under One Process** | Spawns multiplayer windows under a single instance of UE5. This will load much faster but have the potential for more issues. |
| **Enable Network Emulation** | Applies the selected network emulation settings when starting the game for the purpose of testing how your game handles network issues:   * **Emulation Target**: Applies the emulation settings to the Server Only, Clients Only, or Everyone. * **Network Emulation Profile**: Applies a preset for incoming traffic and outgoing traffic. Options are Average, Bad, or Custom * **Incoming traffic**: Applies settings that add latency and packet loss to all incoming packets. Can add minimum and maximum latency, as well as a percentage amount of packet loss. * **Outgoing traffic**: Applies settings that add latency and packet loss to all outgoing packets. Can add minimum and maximum latency, as well as a percentage amount of packet loss. |
| **Client** | Applies the selected client settings when starting the game:   * **Play Number of Clients**: Opens a number of client windows. The first one will respect Play In Editor Modes options. The rest will respect the Run Under One Process settings. * **Route Gampad to Second Window**: Routes the gamepad input suring a multiplayer session. If unchecked, then the first gamepad is attached to the first multiplayer window, the second to the second window, and so on. If checked, then the gamepad is routed to the second multiplayer window, allowing the first to be controlled by keyboard and mouse. * **Create Audio Device for Every Player**: Controls how many audio devices are created. If checked, a separate audio device is created for every player. This will render accurate audio for every player's perspective at the cost of CPU performance. If unchecked, a separate audio device is created for only the first two players. * **Client Fixed FPS**: Sets each client's framerate to an element in the list. Includes a Listen Server. |
| **Server** | Applies the selected server settings when starting the game:   * **Server Port**: Opens the chosen port for simple server networking. * **Server Map Name Override**: Overrides the map launched by the server. Currently only used by the PIE\_StandaloneWithServer net mode. * **Additonal Server Game Options**: Adds additional parameters that are passed to the server as URL parameters. * **Additonal Server Launch Parameters**: Adds additional parameters that are passed to the server as arguments. * **Server Fixed FPS**: Sets the server to run at the specified framerate. Does not impact Listen Server. * **Multiplayer Viewport Size (in pixels)**: Spawns additional clients at the width and height specified. Useful when you need multiple clients but only want to interact with one window. |

## Play On Device

| **Setting** | **Description** |
| --- | --- |
| **Build Game Before Launch** | Builds the game before launching it on the device:   * **Always**: Always build. * **Never**: Never build. * **If project has code, or running locally build editor.**: Build based on project type. * **If running a locally built editor**: Build if using a locally built (i.e non-promoted) editor. |
| **Launch Configuration** | Uses the selected build configuration when launching on a device:   * **Same as Editor**: Launches on device with the same build confoguration as the editor. * **Debug**: Launches on device with a Debug build configuration. * **Development**: Launches on device with a Development build configuration. * **Test**: Launches on device with a Test build configuration. * **Shipping**: Launches on device with a Shipping build configuration. |
| **Auto Compile Blueprints on Launch** | Recompiles dirty Blueprints before launching. |

For more information on build configurations, please see the [Build Configurations Reference](/documentation/404) page.

## Multiplayer Options (Server Debug Settings)

| **Setting** | **Description** |
| --- | --- |
| **Show Server Debug Drawing by Default** | Controls the default value of the show flag ServerDrawDebug. |
| **Show Server Debug Drawing Color Tint Strength** | Controls how strongly the debug drawing originating from the server will be biased towards the tint color. |
| **Show Server Debug Drawing Color Tint** | Debug drawing originating from the server will be biased towards this color. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Play In Editor](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#playineditor)
* [Game Viewport Settings](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#gameviewportsettings)
* [Play in New Window](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#playinnewwindow)
* [Play in Standalone Game](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#playinstandalonegame)
* [Multiplayer Options](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#multiplayeroptions)
* [Play On Device](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#playondevice)
* [Multiplayer Options (Server Debug Settings)](/documentation/en-us/unreal-engine/play-in-editor-settings-in-unreal-engine?application_version=5.7#multiplayeroptions(serverdebugsettings))
