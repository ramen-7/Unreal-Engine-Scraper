<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7 -->

# Player Start Actor

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. [Actors Reference](/documentation/en-us/unreal-engine/unreal-engine-actors-reference "Actors Reference")
8. Player Start Actor

# Player Start Actor

Use Player Start Actors to set up starting locations for players.

![Player Start Actor](https://dev.epicgames.com/community/api/documentation/image/82b7c586-5bc2-4ade-8b96-3b22c484e101?resizing_type=fill&width=1920&height=335)

 On this page

For any Unreal Engine project that uses playable characters, you can use the **Player Start** Actor to control where, in the game world, each player character will spawn at runtime.

The Player Start Actor is visually represented as a game controller icon with a flag and an arrow that indicates which direction the player will be facing when they spawn.

When you select a Player Start Actor, you will see two additional components: a Capsule that is a visual representation of the physical space the Actor occupies in the game world, and a Transform widget.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f2ab129-d04b-41af-a1d7-92dd207ce665/ue5_1-player-start-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f2ab129-d04b-41af-a1d7-92dd207ce665/ue5_1-player-start-actors.png)

A Player Start Actor in the Level. Left: Unselected; Right: Selected.
Click the image for full size.

If your Level doesn't have a Player Start Actor, the player will always start at the 0,0,0 coordinates in the world.

## Placing a Player Start Actor

Player Start Actors are placed into the Level via drag-and-drop, same as other Actors.

You can have multiple Player Start Actors into the Level and control which Player Start is used as the player spawn location using Blueprint or C++.

To place a Player Start Actor, follow these steps:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c39cc1d-e845-4d1a-b8ae-4228140d0260/ue5_1-place-player-start-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c39cc1d-e845-4d1a-b8ae-4228140d0260/ue5_1-place-player-start-actor.png)

Click the image for full size.

1. Click the **Quick Add** button on the **Main Toolbar**.
2. Select **Basic > Player Start**.
3. Click and drag the **Player Start** Actor into the Level Viewport.

When using a Player Start Actor to spawn a player, the position and rotation of the player character will match the Player Start's position and rotation. If you want to have a player look at something specific when they spawn, make sure that the **arrow** component of the Player Start you use to spawn them is pointing in the direction that you want the player to look.

If you have more than one Player Start Actor in your Level, the player will start from a random Player Start each time, prioritizing Player Start Actors that are unobstructed.

## Player Start BADsize Warning

While placing or moving a Player Start Actor, you may see a white label with red borders and the text **BADsize**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8078a65-1f33-467a-8a59-84a361942a1f/ue5_1-player-start-badsize.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8078a65-1f33-467a-8a59-84a361942a1f/ue5_1-player-start-badsize.png)

Click the image for full size.

This warning appears when the Player Start Actor overlaps or intersects with something else in the Level, such as props or terrain. To resolve this, move the Player Start until its **Capsule** component no longer overlaps or intersects with anything else.

## Using Player Start Actors in Blueprints

Unreal Engine has several Blueprint nodes that you can use to work with Player Start Actors. These are useful for a number of different scenarios, including respawning players at a Player Start Actor's location or spawning a player at a different Player Start based on different conditions.

The following nodes for working Player Start Actors are available in the **Game Mode** Blueprint:

* [FindPlayerStart](https://docs.unrealengine.com/en-US/BlueprintAPI/Game/FindPlayerStart/): Finds a Player Start Actor in the Level based that has a specific **tag** (defined in the **IncomingName** property). You can set a Player Start Actor's tag from the Actor's **Details** panel.

  ![FindPlayerStart node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56b9e873-fe2d-4dcd-8f40-1f499f98b7c5/ue5_1-findplayerstart-node.png)
* [Restart Player at Player Start](https://docs.unrealengine.com/en-US/BlueprintAPI/Game/RestartPlayeratPlayerStart/): Respawns a player using a specified Player Start Actor.

  ![Restart Player at Player Start node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90d0a5b0-6b91-4c6a-8308-a1b31af54a4d/ue5_1-restart-player-at-player-start-node.png)

The screenshot below shows an example of how to use these nodes to restart a player at the location of a Player Start with the tag `TheStartIWant` when pressing the **E** key. If you want to try this yourself, recreate these nodes in your project's **Game Mode** Blueprint.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/194a4867-1862-4219-bb7f-187827c78e44/ue5_1-player-start-blueprint-example.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/194a4867-1862-4219-bb7f-187827c78e44/ue5_1-player-start-blueprint-example.png)

Click the image for full size.

## Ignoring Player Start in PIE

When you preview your game in the Unreal Editor using [Play-in-Editor (PIE)](/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine), you may not want to spawn your character at the position of the Player Start actor. Instead, you might want to navigate to a specific location in your level first, and start your PIE session from that location.

There are two ways you can achieve this:

* In the Play Options menu, in the **Spawn Player At** section, you can choose either to spawn at the current camera location or at the default Player Start location.

  ![Play Options menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b0fef2e-a152-494e-89b2-c8ddc105a57f/play-options-spawn-player-at.png)]
* You can **right-click** your desired starting location in the Level Viewport and select **Play From Here** from the context menu.

## Customizing Player Start Behavior

Most of the behavior of the Player Start Actor is implemented in the `FindPlayerStart()` and `ChoosePlayerStart()` functions of the Game Mode Base class (`AGameModeBase`). If you want a different behavior, you can override one or both of these functions in your project's Game Mode class.

For example, instead of having these functions choose a Player Start Actor at random as described above on this page, you might want them to choose one according to a different set of criteria, like:

* the Player Start Actor that is closest to the last checkpoint the player reached.
* the Player Start Actor that is closest to the current location of the player's teammates.
* other attributes associated with the player or their character, like their starting team assignment.

Both the `FindPlayerStart()` and `ChoosePlayerStart()` functions are passed the Controller for the player being spawned in the Player parameter. You can use this reference to access information about the player in your own implementations if necessary.

### FindPlayerStart

The engine calls `FindPlayerStart()` automatically whenever it needs a new starting position for a player. If that player has previously been spawned with an Actor to mark its starting location, this function returns that Actor. Otherwise, it calls `ChoosePlayerStart()` to select an Actor.

This is a good choice to override if you may want to determine a different starting location when a player restarts than the one that was chosed when they initially joined the game.

`FindPlayerStart()` also accepts an Incoming Name parameter. If this name is provided, the default implementation looks for a Player Start Actor that has been assigned the matching string in its Player Start Tag setting. If it finds a matching Player Start Actor, it returns that Actor. This behavior can be useful if you call `FindPlayerStart()` in your own gameplay code. However, the engine does not provide an Incoming Name in most cases when it calls `FindPlayerStart()` internally.

### ChoosePlayerStart

The default implementation of `ChoosePlayerStart()` chooses a Player Start Actor at random, preferring those that are not obstructed by other blocking geometry.

This is a good choice to override if you want to keep the default behavior of `FindPlayerStart()` in place, but you want to use your own custom logic to choose a starting location when a player first joins the game.

### Example

The following implementation of `FindPlayerStart()` is from a Blueprint class that derives from Game Mode Base. It gets the current Game State, and looks for a reference position called Checkpoint Location that has been saved in that Game State. If it is able to get that reference position from the Game State, it returns the Player Start Actor that is closest to that position. Otherwise, it falls back on choosing a Player Start Actor at random by calling the original implementation in the base class.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea161cba-3e81-4c87-a315-7164d427e7b0/game-mode-find-player-start.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea161cba-3e81-4c87-a315-7164d427e7b0/game-mode-find-player-start.png)

Click the image for full size.

For more information on the Game Mode and Game State, see [Game Mode and Game State](/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine).

* [actors](https://dev.epicgames.com/community/search?query=actors)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Placing a Player Start Actor](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#placingaplayerstartactor)
* [Player Start BADsize Warning](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#playerstartbadsizewarning)
* [Using Player Start Actors in Blueprints](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#usingplayerstartactorsinblueprints)
* [Ignoring Player Start in PIE](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#ignoringplayerstartinpie)
* [Customizing Player Start Behavior](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#customizingplayerstartbehavior)
* [FindPlayerStart](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#findplayerstart)
* [ChoosePlayerStart](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#chooseplayerstart)
* [Example](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine?application_version=5.7#example)
