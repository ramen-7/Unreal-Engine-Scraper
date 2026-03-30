<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7 -->

# MetaSounds Quick Start

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
5. [Working with Audio](/documentation/en-us/unreal-engine/working-with-audio-in-unreal-engine "Working with Audio")
6. [Sound Sources](/documentation/en-us/unreal-engine/sound-sources-in-unreal-engine "Sound Sources")
7. [MetaSounds](/documentation/en-us/unreal-engine/metasounds-in-unreal-engine "MetaSounds")
8. MetaSounds Quick Start

# MetaSounds Quick Start

A quick guide on getting started with MetaSounds.

![MetaSounds Quick Start](https://dev.epicgames.com/community/api/documentation/image/0924b9f1-7ad9-4bed-b79d-abbddc976242?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

**MetaSound** is a high-performance audio system that provides audio designers with complete control over a Digital Signal Processing (DSP) graph to generate sound sources.

In this guide, you will learn how to create two gameplay-driven **MetaSound Sources**: a bomb sound effect and ambient wind.

## Prerequisites

Before creating your first MetaSounds with this guide, you must create a new [First Person Template](/documentation/en-us/unreal-engine/unreal-engine-templates-reference) project with **Starter Content**.

## 1 - Create the Bomb MetaSound

Though the rifle plays a sound when fired, the projectile is silent. Using MetaSound, you will create a bomb sound effect to be used by the projectile.

### 1A - Create the MetaSound Source

Because this will be a sound source within 3D space, start by creating a MetaSound Source with an attached **Sound Attenuation Asset**.

1. Create a MetaSound Source.

   1. In the **Content Browser**, click the **Add** button.
   2. Select **Audio > MetaSound Source**.
   3. Give the newly created Asset a name (such as MSS\_Bomb).
2. Double-click the MetaSound to open the **MetaSound Editor**.
3. Set the **Attenuation Settings** to spatialize and attenuate the MetaSound based on its position relative to the listener.

   1. Click the **Source** button on the **MetaSound Editor Toolbar**.
   2. In the **Details** panel, click the dropdown next to **Attenuation > Attenuation Settings**.
   3. Select **Sound Attenuation** under the Create New Asset heading.
   4. Give the newly created Asset a name (such as SA\_Bomb), then save it.

### 1B - Build the MetaSound Graph

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59995c9c-c8db-44a9-b324-7d90081bb692/bomb_ms_graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59995c9c-c8db-44a9-b324-7d90081bb692/bomb_ms_graph.png)

Click image for full size.

Build the **MetaSound Graph** that controls how your MetaSound Source sounds. Follow the instructions below to create the graph shown above.

1. Find the **On Play Input** node and drag off of the pin into an empty space. Enter "Wave Player (Mono)" into the node search to create a connected node. You can move the node around the graph by dragging it.
2. On the **Wave Player (Mono)** node:

   1. Click the **Wave Asset** dropdown and select the Fire\_Sparks01 Sound Wave.
   2. Enable **Loop**.
   3. Drag off the **Out Mono** pin and create a **Mono Mixer (2)**.
   4. Drag off the **Stop** pin and create another **Wave Player (Mono)**.
3. On the new **Wave Player (Mono)** node:

   1. Connect the **On Finished** pin to the **On Finished Output** node.
   2. Connect the **Out Mono** pin to the **In 1** pin on the **Mono Mixer (2)**.
   3. Drag off the **Play** pin and create a **Random Get (WaveAsset:Array)** node.
   4. Connect the **Wave Asset** pin to the **Value** pin on the **Random Get (WaveAsset:Array)** node.
4. On the **Random Get (WaveAsset:Array)** node:

   1. Drag off the **Next** pin and select **Promote to Graph Input**. This will create a **Trigger Input** node named Next.
   2. Drag off the **In Array** pin and select **Promote to Graph Variable**. This will create a **WaveAsset:Array Variable** node named In Array.
5. On the **Mono Mixer (2)**:

   1. Enter 2.0 for **Gain 1 (Lin)**.
   2. Connect the **Out** pin to the **Out Mono Output** node.

### 1C - Adjust the Explosion Wave Player Inputs

![Bomb MetaSound Inputs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b440be8d-5563-4892-9051-ef8e030279bc/bomb_ms_inputs.png)

Adjust the Next Trigger and the In Array Variable.

1. Select the Next **Trigger Input** node.
2. In the **Details** panel, enter "Explode" into **General > Input** to rename it. This will be the name of the Trigger you will set to execute from Blueprint.
3. Select the In Array **WaveAsset:Array Variable** node.
4. In the **Details** panel, enter "ExplosionArray" into **General > Variable** to rename it.
5. Click the **Add (+)** button twice for **Default Value > Default**. These indices will hold Sound Wave references to be randomly selected from.
6. Click the **Index[0]** dropdown and select the Explosion01 Sound Wave.
7. Click the **Index[1]** dropdown and select the Explosion02 Sound Wave.

### 1D - Play the MetaSound

![Explosion Trigger Input](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/faf3c04d-c2ef-427d-a275-6920d259f7fe/explode_input.png)

The MetaSound is now ready to play.

1. Click the **Play** button on the **MetaSound Editor Toolbar** to play the MetaSound. A spark sound will loop until the **Explode** Trigger executes, at which point a random explosion sound in the **ExplosionArray** will play before the MetaSound finishes. You can simulate the **Explode** Trigger execution by clicking the **Execute (Down Arrow)** button on the top-right corner of the **Trigger Input** node while the MetaSound is playing.
2. Save the MetaSound Source and close the MetaSound Editor.

## 2 - Add Bomb Logic to Blueprint

After designing the bomb sound, use the projectile's Blueprint to set up the runtime logic.

### 2A - Open the Projectile Blueprint

Open the pre-built projectile Blueprint.

1. In the **Content Browser**, navigate to `All/Content/FirstPerson/Blueprints`.
2. Double-click **BP\_FirstPersonProjectile** to open it in the **Blueprint Editor**.

### 2B - Build the Blueprint Graph

![Bomb Blueprint Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3274b6e4-ae9d-4ceb-9920-131b742a31a2/bomb_bp_graph.png)

Add to the existing **Blueprint Graph** to control the bomb MetaSound based on projectile lifecycle.

1. Right-click in an empty space and create an **Event BeginPlay** node.
2. Drag off the **Event BeginPlay** node and create a **Spawn Sound Attached** node.
3. On the **Spawn Sound Attached** node:

   1. Click the **Sound** dropdown and select your bomb MetaSound.
   2. Drag off the **Attach to Component** pin and create a **Get Sphere** node.
   3. Drag off the **Return Value** pin and create an **Execute Trigger Parameter** node.
   4. Hold Alt and click the **Exec Output (>)** pin to remove the connection between the **Spawn Sound Attached** and **Execute Trigger Parameter** nodes.
4. On the **Execute Trigger Parameter** node:

   1. Enter "Explode" for **In Name**.
   2. Drag off the **Exec Input (>)** pin and create an **Event Destroyed** node.
5. Save your changes to the Blueprint and close the Blueprint Editor.

### 2C - Test the Level

The Blueprint is now ready to test.

Click the **Play** button on the **Level Editor Toolbar**, pick up the rifle (by moving into it), and shoot it (by left-clicking) to verify your work.

The projectiles will produce spatialized, dynamic sounds. The spark sound loops until the projectile explodes by either making contact with a blue box or after a short time passes.

## 3 - Create the Wind MetaSound

Create a MetaSound for ambient wind to add some atmosphere to the scene.

### 3A- Create the MetaSound Source

Create another MetaSound Source Asset. This sound will not be spatialized within 3D space, so you don't have to attach a Sound Attenuation Asset.

1. Create a MetaSound Source.

   1. In the **Content Browser**, click the **Add** button.
   2. Select **Audio > MetaSound Source**.
   3. Give it a name (such as MSS\_Wind).
2. Double-click the MetaSound to open the MetaSound Editor.

### 3B - Adjust the MetaSound Details

![Wind MetaSound Details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0a9186a-4c04-4925-992c-a52933249175/wind_ms_details.png)

Before building the graph, adjust the default properties of the MetaSound to support persistent stereo audio.

1. In the Interfaces panel, click the **Remove (Trash Bin)** button next to the **UE.Source.OneShot** Interface entry. This will remove the **On Finished Output** node, which isn't used on persistent sounds such ambience or music.
2. Click the **MetaSound** button on the **MetaSound Editor Toolbar**.
3. In the **Details** panel, click the **MetaSound > Output Format** dropdown and select **Stereo**. This will replace the **Out Mono Output** node with **Out Left** and **Out Right Output** nodes.

### 3C - Build the MetaSound Graph

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/34b917dc-6cb1-4e2b-bd9c-08c78d80825c/wind_ms_graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/34b917dc-6cb1-4e2b-bd9c-08c78d80825c/wind_ms_graph.png)

Click image for full size.

Build the **MetaSound Graph** that controls how your MetaSound Source sounds. Follow the instructions below to create the graph shown above.

1. Select the **On Play Input** node and delete it using the Delete key. It will not be needed in this graph.
2. Drag off the **Out Left** pin and create a **Stereo Mixer (2)** node.
3. Connect the **Out Right** pin to the **Out R** pin on the **Stereo Mixer (2)** node.
4. Right-click in an empty space and create a **Noise** node.
5. On the **Noise** node, drag off the **Audio** pin and create a **One-Pole Low Pass Filter** node.
6. Drag a selection box to select the **Noise** and **One-Pole Low Pass Filter** nodes.
7. Right-click either selected node and select **Duplicate**.
8. On the new **Noise** node, enter 1 for **Seed**. This will introduce variance in the noise generation.
9. On one of the **One-Pole Low Pass Filter** nodes, connect the **Out** pin to the **In 0 L** pin on the **Stereo Mixer (2)** node.
10. On the other **One-Pole Low Pass Filter** node, connect the **Out** pin to the **In 0 R** pin on the **Stereo Mixer (2)**node.
11. Right-click in an empty space and create an **LFO** node.
12. On the **LFO** node:

    1. Enter 0.1 for **Frequency**.
    2. Enter 20.0 for **Min Value**.
    3. Enter 80.0 for **Max Value**.
    4. Connect the **Out** pin to both of the **Cutoff Frequency** pins on the **One-Pole Low Pass Filter** nodes.
13. On the **Stereo Mixer (2)** node, drag off the **Gain 0 (Lin)** pin and create an **InterpTo** node.
14. On the **InterpTo** node:

    1. Enter 0.3 for **Interp Time**.
    2. Drag off the **Target** pin to create an **Add (Float)** node.
15. On the **Add (Float)** node:

    1. Enter 2.0 for **Bottom Addend**.
    2. Drag off the **Top Addend** pin and create a **Multiply (Float)** node.
16. On the **Multiply (Float)** node:

    1. Enter 3.0 for **Bottom Multiplicand**.
    2. Drag off the **Top Multiplicand** pin and select **Promote to Graph Input**. This will create a **Float Input** node named PrimaryOperand.
17. Select the PrimaryOperand **Float Input** node.
18. In the **Details** panel, enter "PawnSpeed" into **General > Input** to rename it.

### 3D - Play the MetaSound

![Pawn Speed Float Input](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/adc32ff4-6d81-4159-9222-b85765445c78/pawn_speed_input.png)

The MetaSound is now ready to play.

1. Click the **Play** button on **MetaSound Editor Toolbar** to play the MetaSound. A dynamic wind-like sound will play in stereo until you click the **Stop** button. The signal gain is affected by the PawnSpeed **Float Input** node. You can simulate PawnSpeed values by clicking the **Input Widget (Dial)** on the node and dragging up or down.
2. Save the MetaSound Source and close the MetaSound Editor.

## 4 - Add Wind Logic to Blueprint

After designing the wind sound, use the **Level Blueprint** to set up the runtime logic.

### 4A - Open the Level Blueprint

To open the Level Blueprint, click the **Blueprint** button in the **Level Editor Toolbar** and select **Open Level Blueprint**.

### 4B - Build the Blueprint Graph

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da3c6278-432a-4d5e-8c01-8bb4920cbfd1/wind_bp_graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da3c6278-432a-4d5e-8c01-8bb4920cbfd1/wind_bp_graph.png)

Click image for full size.

Build the Blueprint Graph to control the wind MetaSound based on Player movement.

1. Right-click in an empty space and create an **Event BeginPlay** node.
2. Drag off the **Event BeginPlay** node and create a **Spawn Sound 2D** node.
3. On the **Spawn Sound 2D** node:

   1. Click the **Sound** dropdown and select your wind MetaSound.
   2. Drag off the **Return Value** and create a **Set Float Parameter** node.
   3. Hold Alt and click the **Exec Output (>)** pin to remove the connection between the **Spawn Sound 2D** and **Set Float Parameter** nodes.
4. On the **Set Float Parameter** node:

   1. Enter "PawnSpeed" for **In Name**.
   2. Drag off the **Exec Input (>)** pin and create an Event Tick node.
5. Right-click in an empty space and create a **Get Player Pawn** node.
6. On the **Get Player Pawn** node, drag off the **Return Value** pin and create a **Get Velocity** node.
7. On the **Get Velocity** node, drag off the **Return Value** pin and create a **Vector Length** node.
8. On the **Vector Length** node, drag off the **Return Value** pin and create a **Map Range Clamped** node.
9. On the **Map Range Clamped** node:

   1. Enter 200.0 for **In Range A**.
   2. Enter 1000.0 for **In Range B**.
   3. Enter 1.0 for **Out Range B**.
   4. Connect the **Return Value** pin to the **In Float** pin on the **Set Float Parameter** node.
10. Save your changes to the Blueprint and close the Blueprint Editor.

### 4C - Test the Level

The Blueprint is ready to test.

Click the **Play** button on the **Level Editor Toolbar** and move around to verify your work.

The wind sound will play at a low volume when idle and grow louder as your velocity increases.

## 5 - On Your Own!

Now that you've finished creating two basic MetaSounds, consider taking this project even further. Below are some suggestions you can explore on your own:

* Alter your MetaSounds with some additional nodes. See the [MetaSounds Reference Guide](/documentation/en-us/unreal-engine/metasounds-reference-guide-in-unreal-engine) for information on the node library and other MetaSound features.
* Replace the default rifle firing sound with a MetaSound. Consider altering the sound dynamically based on the rate of fire, shot angle, or other variables.
* Add MetaSounds for player actions such as walking, jumping, and item pickup.
* Improve on the simple wind implementation you created with this guide. See the [Lyra Sample Game](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine) project for an example of an advanced implementation that supports additional features, such as panning and environment response.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [audio](https://dev.epicgames.com/community/search?query=audio)
* [sound sources](https://dev.epicgames.com/community/search?query=sound%20sources)
* [metasounds](https://dev.epicgames.com/community/search?query=metasounds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#prerequisites)
* [1 - Create the Bomb MetaSound](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#1-createthebombmetasound)
* [1A - Create the MetaSound Source](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#1a-createthemetasoundsource)
* [1B - Build the MetaSound Graph](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#1b-buildthemetasoundgraph)
* [1C - Adjust the Explosion Wave Player Inputs](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#1c-adjusttheexplosionwaveplayerinputs)
* [1D - Play the MetaSound](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#1d-playthemetasound)
* [2 - Add Bomb Logic to Blueprint](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#2-addbomblogictoblueprint)
* [2A - Open the Projectile Blueprint](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#2a-opentheprojectileblueprint)
* [2B - Build the Blueprint Graph](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#2b-buildtheblueprintgraph)
* [2C - Test the Level](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#2c-testthelevel)
* [3 - Create the Wind MetaSound](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#3-createthewindmetasound)
* [3A- Create the MetaSound Source](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#3a-createthemetasoundsource)
* [3B - Adjust the MetaSound Details](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#3b-adjustthemetasounddetails)
* [3C - Build the MetaSound Graph](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#3c-buildthemetasoundgraph)
* [3D - Play the MetaSound](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#3d-playthemetasound)
* [4 - Add Wind Logic to Blueprint](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#4-addwindlogictoblueprint)
* [4A - Open the Level Blueprint](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#4a-openthelevelblueprint)
* [4B - Build the Blueprint Graph](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#4b-buildtheblueprintgraph)
* [4C - Test the Level](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#4c-testthelevel)
* [5 - On Your Own!](/documentation/en-us/unreal-engine/metasounds-quick-start?application_version=5.7#5-onyourown!)
