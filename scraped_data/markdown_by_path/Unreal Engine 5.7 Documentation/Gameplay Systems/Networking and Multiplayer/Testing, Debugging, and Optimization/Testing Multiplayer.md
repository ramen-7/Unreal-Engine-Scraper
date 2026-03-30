<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7 -->

# Testing Multiplayer

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
6. [Networking and Multiplayer](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine "Networking and Multiplayer")
7. [Testing, Debugging, and Optimization](/documentation/en-us/unreal-engine/network-debugging-for-unreal-engine "Testing, Debugging, and Optimization")
8. Testing Multiplayer

# Testing Multiplayer

Set up the Unreal Editor for testing multiplayer games.

![Testing Multiplayer](https://dev.epicgames.com/community/api/documentation/image/aa1e8019-41cd-4572-ac4c-9cd90d339ef4?resizing_type=fill&width=1920&height=335)

 On this page

This page shows you how you can change some of the settings for the editor for testing different multiplayer scenarios.

## Multiplayer Play Options

### Set Number of Players

Click the more options button next to the **Play** button and enter a value for **Number of Players**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/484578d0-627b-4ac7-8be1-68aa326d53fe/play-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/484578d0-627b-4ac7-8be1-68aa326d53fe/play-options.png)

By default, the server uses the **Selected Viewport** as the play window and new windows will be created for each client that is added:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48581031-89d1-4f79-af11-6c332e0b7ed7/multiplayer-preview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48581031-89d1-4f79-af11-6c332e0b7ed7/multiplayer-preview.png)

### Adjusting Play Windows

While it is perfectly okay to use the Editor's Viewport as a play window, for clarity you may want to use windows for each player. To adjust the play window for the server, click the more options button next to the **Play** button then select **New Editor Window (PIE)**. While simulated clients have their own windows, this setting will also create a separate window for the simulated server.

## Advanced Settings

If you have set up the **Play** method to use new editor windows, you may want to adjust the size of the editor windows. Click the more options button next to the **Play** button then select **Advanced Settings**. Set the desired window sizes under the **Multiplayer Viewport Size (in pixels)** section. The **Multiplayer Viewport Size (in pixels)** size option allows you to set the size of windows that are created. You can choose from a number of preset window sizes or manually enter a window size (we specified `640x480` in our example). Once you have entered a window size, when you play in the editor, each new window will be of the same size.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bef90bd1-fc17-440f-990b-eb88fe3e683f/new-editor-window.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bef90bd1-fc17-440f-990b-eb88fe3e683f/new-editor-window.png)

When playing in the editor using new windows for each play session, you will notice at the top of each window it will display if the player is a server or client. Also while in **Play** mode, when you move windows around, their locations will be remembered for your next **Play** in editor session (so you will not have to keep moving them around which makes testing easier).

### Multiplayer Options

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51473be4-4eef-4cdf-b2d7-ede77facc26a/multiplayer-editor-preferences.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51473be4-4eef-4cdf-b2d7-ede77facc26a/multiplayer-editor-preferences.png)

Also inside **Advanced Settings**, there is a section for setting up additional multiplayer options:

| Option | Description |
| --- | --- |
| **Number of Players** | This option defines the number of players to spawn in the game when launched. The editor and listen server count as players, a dedicated server will not. Clients make up the remainder of players. |
| **Server Game Options** | Here you can specify additional options that will be passed to the server as URL parameters. |
| **Run Dedicated Server** | If checked, a separate dedicated server will be launched. Otherwise the first player will act as a listen server that all other players can connect to. |
| **Route 1st Gamepad to 2nd Client** | When running multiple player windows in a single process, this option determines how the game pad input get routed. If unchecked (default) the 1st game pad is attached to the 1st window, 2nd to the 2nd window, and so on. If it is checked, the 1st game pad goes to the 2nd window. The 1st window can then be controlled by keyboard/mouse, which is convenient if two people are testing on the same computer. |
| **Use Single Process** | This spawns multiple player windows in a single instance of Unreal Engine. This will load much faster, but has potential to have more issues. When this is unchecked, additional options become available. |
| **Create Audio Device for Every Player** | Enabling this will allow rendering accurate audio from every player's perspective but will use more CPU. |
| **Play In Editor Description** | This is a description of what will occur when playing based on the currently applied multiplayer settings. |

When **Use Single Process** is checked, multiple windows are spawned in a single instance of Unreal Engine. When this option is unchecked, multiple instances of UE will be launched for each player that is assigned and additional options become available:

| Option | Description |
| --- | --- |
| **Editor Multiplayer Mode** | This is the NetMode to use for Play In Editor (**Play Offline**, **Play As Listen Server** or **Play As Client**). |
| **Command Line Arguments** | Here you can assign additional command line options that will be passed to standalone game instances. |
| **Multiplayer Window Size (in pixels)** | Define the width/height to use when spawning additional standalone game instances. |

## Listen Server vs. Dedicated Server

When launching a multiplayer game, there are two methods in which the game can be hosted. The first, is by using a **Listen Server** (default setting) which means that the machine that has the authority is also running a client and can play the game normally while hosting for other players.

The second method is by using a **Dedicated Server**, which as the name implies, is dedicated to only hosting the game and no local players play on the machine as everyone connected is a client. Usually running as a Dedicated Server is more optimized than running as a Listen Server as there are no visuals or input being registered.

By default, the server type is set to a Listen Server when playing in the editor or standalone game.

### Run a Dedicated Server

Click the more options button next to the **Play** button then check the **Run Dedicated Server** checkbox. For more information about setting up a dedicated server for your project, see our [Setting Up Dedicated Servers](/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine) documentation.

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [how-to](https://dev.epicgames.com/community/search?query=how-to)
* [multiplayer](https://dev.epicgames.com/community/search?query=multiplayer)
* [network](https://dev.epicgames.com/community/search?query=network)
* [basics/gettingstarted](https://dev.epicgames.com/community/search?query=basics%2Fgettingstarted)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Multiplayer Play Options](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#multiplayerplayoptions)
* [Set Number of Players](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#setnumberofplayers)
* [Adjusting Play Windows](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#adjustingplaywindows)
* [Advanced Settings](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#advancedsettings)
* [Multiplayer Options](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#multiplayeroptions)
* [Listen Server vs. Dedicated Server](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#listenservervsdedicatedserver)
* [Run a Dedicated Server](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine?application_version=5.7#runadedicatedserver)
