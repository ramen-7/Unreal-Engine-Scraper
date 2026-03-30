<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/loading-and-unloading-levels-using-blueprints-in-unreal-engine?application_version=5.7 -->

# Loading and Unloading Levels using Blueprints

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
6. [Level Streaming](/documentation/en-us/unreal-engine/level-streaming-in-unreal-engine "Level Streaming")
7. Loading and Unloading Levels using Blueprints

# Loading and Unloading Levels using Blueprints

How to stream levels with a custom streaming Actor created with Blueprints

![Loading and Unloading Levels using Blueprints](https://dev.epicgames.com/community/api/documentation/image/f29cbb69-dfe4-4ab9-a71c-52d02b84222c?resizing_type=fill&width=1920&height=335)

 On this page

We want to start streaming in the patio level here, so that by the time the player rounds the corner and begins approaching the patio, the streaming level
will be loaded and visible.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a81ef7b-e43b-43f8-8e96-900bea4afa74/streaminglevelvisible.png)

As part of the setup, we have two levels, **SunTemple\_Persistent** and **SunTemple\_Streaming**. Our **Player Start** is in **SunTemple\_Persistent**, and our player in the game is
represented by a *Character*.

1. Open **SunTemple\_Persistent** in the **Content Browser**.
2. Move the **Player Start** to the very beginning of the temple.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30c16336-b648-4b87-8463-c02960367f3d/playerstart.png)
3. Click on **Windows**, then select **Levels**.
4. Click on the **Levels** dropdown menu, then select **Add Existing...** to add a new sublevel.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c33361c-f475-4e57-8c74-1f651df6e6d9/addexisting.png)
5. Select **SunTemple\_Streaming** to add in the **Open Level** dialog, then click on **Open**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c701996-e294-4853-a97b-b7c0a60a0ec4/suntemplestreaming_select.png)
6. **Right-click** on **Persistent Level** and select **Make Current** from the dropdown menu.

## Streaming In Levels with Blueprints

1. Open the **Content Browser** and create a new **Blueprint Class**. This class is going to be based on **Actor**.
2. Name the new **Blueprint Class** "LevelStreamer", then save it.
3. Open **LevelStreamer** in the **Blueprint Editor**.

For this scenario, we want to stream the second level in once the **Character** overlaps the Box Component.

1. Add a **Box Collision** Component using the **Add Component** button in the **Components** tab.
2. Open the Blueprint's **Event Graph**. Select the **Box** Component in the **Components** tab, then **right-click** in the graph to summon the context menu.
3. Type "begin overlap" then select **On Component Begin Overlap** to add the event.
4. Click and drag off of the **Other Actor** pin, then type "=" into the context menu's search. Select the **Equal (Object)** entry to add the node.
5. Click and drag off of the second Object pin on the **==** node, then type "character" into the context menu's search. Select the **Get Player Character** entry to add the node.
6. Hold down the **B** key and click in the graph to add a **Branch** node, then connect the boolean pin of the **==** node to the input on the **Branch** node.
7. Connect the execution output pin of the **OnComponentBeginOverlap** node to the execution input pin of the **Branch** node.
8. **Right-click** in the graph, then type "level" to search in the context menu. Select **Load Stream Level** from the menu.
9. **Right-click** on the **Level Name** pin and promote it to a variable, then name the variable "LevelToStream" and make it **Editable** in the **Details** panel.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdb66b5d-bf3d-4b03-b08b-3217e7edb0bd/leveltostreamvar.png)
10. Toggle **Make Visible After Load** and **Should Block on Load** to true on the **Load Stream Level** node.

    For this example, we are going to have the same default loading behavior for all levels using this Blueprint, but you could also make those **Editable** variables.
11. Connect the **True** execution output pin of the **Branch** node to the input execution pin on the **Load Stream Level** node.

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38f438c5-c0bb-4892-a246-443bdf8608b7/finalloadbp.png)
12. Place your **LevelStreamer** Blueprint into your level, and adjust the placement and scale until it encompasses the part of the persistent world you want your **Character** to be
    in to begin streaming, as well as the entire walkable volume where the streaming level will be.
13. Enter **SunTemple\_Streaming** as the **Level to Stream**.
14. Use Play In Editor to test out your streaming level.

## Unloading Levels with Blueprints

To unload the level as your *Character* exits the **Box** component, your graph will have very similar logic but will end in an **Unload Stream Level** node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86fa77cc-1180-4f3e-9835-3a4febd67645/unloadlevel.png)

* [level streaming](https://dev.epicgames.com/community/search?query=level%20streaming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Streaming In Levels with Blueprints](/documentation/en-us/unreal-engine/loading-and-unloading-levels-using-blueprints-in-unreal-engine?application_version=5.7#streaminginlevelswithblueprints)
* [Unloading Levels with Blueprints](/documentation/en-us/unreal-engine/loading-and-unloading-levels-using-blueprints-in-unreal-engine?application_version=5.7#unloadinglevelswithblueprints)
