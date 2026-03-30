<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7 -->

# Create Procedural Music

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
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game "Art Pass for a Puzzle Adventure Game")
8. Create Procedural Music

# Create Procedural Music

Create Procedural Music with MetaSounds.

![Create Procedural Music](https://dev.epicgames.com/community/api/documentation/image/f3edc6fa-f47b-4c47-9455-3dc73c48aded?resizing_type=fill&width=1920&height=335)

 On this page

In this tutorial, you’ll learn how to create procedural music using **MetaSounds**. You’ll create procedurally-generated background music for your adventure game.

MetaSounds is a high-performance audio system that can generate sound sources using a node-based system, similar to the Blueprint Visual Scripting system.

## Before You Begin

Make sure you understand these topics covered in the [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users) documentation:

* Blueprint basics, such as adding and connecting nodes.

## Create Procedural Music with MetaSounds

You’ll start by creating a MetaSound asset. Follow these steps:

1. Go to the **Content** **Browser** and navigate to the **Content > AdventureGame > Artist > Audio** folder.
2. In the **Audio** folder, create a new folder named **Music**.
3. Right-click inside the **Music** folder and select **Audio > MetaSound Source**.
4. Name this asset `MS_BGM`, which stands for **MetaSound Background Music**.
5. Open the asset.

The asset opens in the **MetaSound Editor**. In the new window, you will see three nodes in the graph – **Input**, **Output On Finished**, and **Input Out Mono**.

[![](https://dev.epicgames.com/community/api/documentation/image/7603aeac-65d9-41c1-9a27-e18eaa00be82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7603aeac-65d9-41c1-9a27-e18eaa00be82?resizing_type=fit)

The **Input** trigger is executed when this audio source is played. A MetaSound always begins with an Input.

The **Output On Finished** trigger is executed to stop the source from playing. If you’re stopping the audio from somewhere else, like a blueprint, you don’t have to use this node to stop the audio source from playing. In this case, you’ll use a blueprint to start and stop the audio, so you won’t have to use this node.

The **Output** **Out Mono** node represents the final audio output of the MetaSound graph, routing all upstream audio signals into a single-channel (mono) output. Any nodes connected to it are effectively mixed down and sent to the engine as the sound’s output.

## Set Music Tempo and Rhythm

First, you’ll create the nodes to set the tempo and rhythm of the music. Follow these steps:

1. Drag the **Input** node’s pin and add a **Trigger Repeat** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/b9d71d94-fc7e-4a14-9658-e4305778b0a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9d71d94-fc7e-4a14-9658-e4305778b0a3?resizing_type=fit)
2. On the **Trigger** **Repeat** node, drag the **Period** pin and add a **BPM To Seconds** node. Set the **Divisions of** **Whole Note** to **16**.

   [![](https://dev.epicgames.com/community/api/documentation/image/fd8d7979-98cd-4d0c-a0d7-5e6a2743f66d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd8d7979-98cd-4d0c-a0d7-5e6a2743f66d?resizing_type=fit)
3. On the **BPM To Seconds** node, drag the **BPM** pin and select **Promote to Graph Input**.

   [![](https://dev.epicgames.com/community/api/documentation/image/1d601c72-8b3e-4ea8-b774-8bc763112138?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d601c72-8b3e-4ea8-b774-8bc763112138?resizing_type=fit)
4. In the **Members** panel in the top-left corner of the screen, rename **Input** from **BPM** to **Note In**.

   [![](https://dev.epicgames.com/community/api/documentation/image/4a13bb6e-27aa-418c-8685-111097bb6c2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a13bb6e-27aa-418c-8685-111097bb6c2c?resizing_type=fit)
5. In the **Details** panel, change the **Default Value** of the **Note In** node to **60**. You can also change this value at the bottom of the node.
6. From the **Trigger Repeat** node, drag the **RepeatOut** pin and add a new **Trigger** **Counter** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/98b02aaa-99e7-40c9-a738-70cba10d1f0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98b02aaa-99e7-40c9-a738-70cba10d1f0a?resizing_type=fit)
7. Select the **Trigger Counter** node and set the **Reset Count** to **8**.

   [![](https://dev.epicgames.com/community/api/documentation/image/791dabad-127b-4c22-9113-5ba88a1f452a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/791dabad-127b-4c22-9113-5ba88a1f452a?resizing_type=fit)

This section sets the tempo and rhythm. Additionally, you can highlight all four nodes you added – **Trigger Counter**, **Trigger Repeat**, **BPM To Seconds**, and **Input** – and press **C** to add a comment box that contains all of the nodes. Name this comment box **Tempo and Rhythm**.

[![](https://dev.epicgames.com/community/api/documentation/image/7d92f055-ce66-4113-8077-3904f23d5de2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d92f055-ce66-4113-8077-3904f23d5de2?resizing_type=fit)

## Generate a Melody

Next, you’ll create the functionality that generates the melody using the tempo and rhythm you defined. Follow these steps:

1. From the **Trigger Counter** node:

   1. Drag the **On Trigger** pin and add a **Random** **Get** **(Float:Array)** node.
   2. Drag the **Trigger** **Counter** node’s **On** **Reset** pin and connect it to the **Random Get** node’s **Reset pin**.

      [![](https://dev.epicgames.com/community/api/documentation/image/9970e1fe-df9d-41c5-9224-bd863bc505b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9970e1fe-df9d-41c5-9224-bd863bc505b8?resizing_type=fit)
2. From the **Random Get** node, drag the **In Array** pin and add a **Scale to Note Array** node.
3. From the **Scale to Note Array** node, drag the **Scale Degrees** pin and add select **Promote to Graph Input** and name it **Scale**.

   [![](https://dev.epicgames.com/community/api/documentation/image/a9bb1dda-086b-477c-85c3-0e1dd95cd416?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9bb1dda-086b-477c-85c3-0e1dd95cd416?resizing_type=fit)
4. From the **Random** **Get** node, drag the **Seed** pin and add a **Random (Int)** node.
5. From the **Random (Int)** node, drag the **Next** pin and connect it to the **Trigger Counter** node’s **On Reset** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/01f9195d-a7a7-448d-aa76-65e4d96e81d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01f9195d-a7a7-448d-aa76-65e4d96e81d7?resizing_type=fit)

This section generates the melody. Once again, you can highlight all of the new nodes and add a comment box called **Melody Generation**.

[![](https://dev.epicgames.com/community/api/documentation/image/712265e1-50ec-450c-ad1e-ac054cd951a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/712265e1-50ec-450c-ad1e-ac054cd951a0?resizing_type=fit)

## Synthesize the Melody

Next, you’ll shape how that melody actually sounds by creating the synthesis. This means turning the generated melody notes into audible sound. Follow these steps:

1. On the **Random Get** node, drag the **Value** pin and add an **Add (Float)** node.
2. On the **Add** node, change the second input pin’s value from 0 to **48**.

   [![](https://dev.epicgames.com/community/api/documentation/image/67ae9c35-faba-4d59-92d2-fad0e6800310?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67ae9c35-faba-4d59-92d2-fad0e6800310?resizing_type=fit)
3. From the **Add** node, drag the **exec** pin and add a **MIDI To Frequency** **(Float)** node.
4. From the **MIDI To Frequency (Float)** node, drag the **Out Frequency** pin and add a **Sine** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/a93e1b34-db97-4c91-af4f-dcc6d2ee54c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a93e1b34-db97-4c91-af4f-dcc6d2ee54c5?resizing_type=fit)
5. From the **Sine** node, drag the **Audio** output pin and add an **Add (Audio)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/9300a8f9-8913-4a0f-a1b8-c9c885bcc528?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9300a8f9-8913-4a0f-a1b8-c9c885bcc528?resizing_type=fit)
6. You’ll add one more **Sine** node that connects to this **Add** node. So, from the **Add** node, drag the other input pin and add a **Sine** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/03546337-6fdd-41ae-a4fa-e5e1deed2cca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03546337-6fdd-41ae-a4fa-e5e1deed2cca?resizing_type=fit)
7. On the new **Sine** node, drag the **Frequency** pin and add a **MIDI To Frequency (Float)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/9763e4ce-866e-4978-b4d0-b3ec742bcac7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9763e4ce-866e-4978-b4d0-b3ec742bcac7?resizing_type=fit)
8. From the **MIDI To Frequency** node, drag the **MIDI In** pin and add an **Add (Float)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/dafa78d2-9b01-4a85-934f-63f19b4390a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dafa78d2-9b01-4a85-934f-63f19b4390a6?resizing_type=fit)
9. On the **Add** node:

   1. Connect the first input pin to the **Add** node that is connected to the first **Sine** node.

      [![](https://dev.epicgames.com/community/api/documentation/image/e0a79e5a-6ef9-4ab1-b484-9ce7fedb2f86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0a79e5a-6ef9-4ab1-b484-9ce7fedb2f86?resizing_type=fit)
   2. Drag the second input pin and select **Promote to Graph Input**. Name it **Detune**.

      [![](https://dev.epicgames.com/community/api/documentation/image/ef2ad211-a655-4350-8afb-81aeea999fc2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef2ad211-a655-4350-8afb-81aeea999fc2?resizing_type=fit)
   3. Select the **Detune** input and in the **Details** panel, change its **Range** to **0** and **12**.

      [![](https://dev.epicgames.com/community/api/documentation/image/ccd23c66-fe65-4c95-adcd-6b16c87f593c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ccd23c66-fe65-4c95-adcd-6b16c87f593c?resizing_type=fit)
   4. In the **Details** panel, change the **Default** value to **12.**

Now, you’ve synthesized the melody that will be generated. You can once again add a comment box for this new section and name it **Synthesis**.

[![](https://dev.epicgames.com/community/api/documentation/image/c0d7eeb7-8668-4d4d-9b11-c1a52d6db54a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0d7eeb7-8668-4d4d-9b11-c1a52d6db54a?resizing_type=fit)

## Shape the Sound With an Envelope

Next, you’ll add an envelope to shape how the sound evolves over time, controlling its start, sustain, and fade-out for a more natural result.

To add an envelope, follow these steps:

1. Scroll to the melody generation section you created previously (if you added a comment box, it should be named **Melody Generation**). From the **Random Get (Float:Array)** node, drag the **On** **Next** pin and add an **AD Envelope (Audio)** node. Move this new node after the two Sine nodes you added in the synthesis section.
2. From this node, drag the **Out Envelope** pin and add a **Multiply (Audio)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/46de20ac-ea2a-48b7-be03-e971d0f559fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46de20ac-ea2a-48b7-be03-e971d0f559fa?resizing_type=fit)
3. From this **Multiply** node, drag the second input pin and connect it to the output pin of the **Add (Audio)** node that you connected the two **Sine** nodes to.

   [![](https://dev.epicgames.com/community/api/documentation/image/0221923b-6fdd-412f-8f1b-4f036026e0ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0221923b-6fdd-412f-8f1b-4f036026e0ac?resizing_type=fit)
4. On the **AD Envelope (Audio)** node, change the **Decay Time** to **0.2**.
5. From the **Multiply (Audio)** node, drag the output pin and connect it to the **Output** **Out** **Mono** node that was already in the MetaSound Source.

   [![](https://dev.epicgames.com/community/api/documentation/image/319131e3-08f2-4b9b-a2c6-bf34a0c071a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/319131e3-08f2-4b9b-a2c6-bf34a0c071a8?resizing_type=fit)

Now, press the **Play** button in the toolbar near the top of the MetaSound Source window. It will continuously play procedurally-generated music.

To learn more about crafting procedural music in Unreal Engine, see the [Creating Procedural Music with MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-procedural-music-with-metasounds) page.

## Play the Music In-Game With Blueprints

Before moving on, you’ll create a Blueprint that plays the background music in the level.

Since this blueprint will be added to the level but doesn’t have a visual representation, you’ll add a **Billboard** component to the blueprint. This component adds a 2D sprite that makes it visible in the editor so you can find it while editing your level, but it won’t be visible in the game.

To create the background music blueprint, follow these steps:

1. Go to the **Content** **Browser** and navigate to **Content > AdventureGame > Artist > Audio > Music**.
2. Right-click and create a new **Blueprint Class** that derives from the **Actor** parent class. Name this **BP\_BGM**, which stands for Blueprint Background Music.
3. In the **Components** panel, click **Add** and add a **Billboard** component. In the **Details** panel, you can see that the **Sprite** is set to **S\_Actor** by default. You can change the sprite or leave it as is.

   [![](https://dev.epicgames.com/community/api/documentation/image/dc7e5901-4950-4268-a6d7-22b5106560ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc7e5901-4950-4268-a6d7-22b5106560ba?resizing_type=fit)
4. Go to the **EventGraph** tab to start building the functionality.
5. Drag from the **Event** **BeginPlay** node and add a **Branch** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/8bacf55b-82a4-4eb2-b061-68fa475cc223?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8bacf55b-82a4-4eb2-b061-68fa475cc223?resizing_type=fit)
6. From the **Branch** node, drag the **Condition** pin and select **Promote to Variable**. Name this variable **Active**. This variable will be used to determine if this audio source is active or not.
7. In the **Variables** list in the **My Blueprints** panel, click the **eye** icon next to the **Active** variable so the eye is open, making it public and editable in the level editor.
8. **Compile** the blueprint, use the **Details** panel to ensure the **Active** variable’s **Default Value** is **true** (enabled).
9. From the **Branch** node, drag the **True** pin and add a **Play Sound 2D** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/96acb64f-f90a-479d-8901-b3bf88d06a02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96acb64f-f90a-479d-8901-b3bf88d06a02?resizing_type=fit)
10. On the **Play Sound 2D** node, use the dropdown to set the **Sound** pin to **MS\_BGM**.

    [![](https://dev.epicgames.com/community/api/documentation/image/df309ad3-54df-4d94-b0ee-2d60ebd61ef8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df309ad3-54df-4d94-b0ee-2d60ebd61ef8?resizing_type=fit)
11. From the **Play Sound 2D** node, click the down arrow to expand the node options. Drag the **Volume Multiplier** pin and select **Promote to Variable**.
12. Click the variable’s **eye** icon to make it public and editable, **Compile** the blueprint, and change its **default value** to **0.5**.
13. Save and compile your blueprint.

The “**2D**” in the **Play Sound 2D** node indicates that the sound will play independently of the player’s position in the level. In other words, it’s not spatialized in 3D space so distance and direction don’t affect how the player hears it.

## Test Your Music In-Game

You can now go back to the level editor and add the **BP\_BGM** blueprint into your level.

Select the **BP\_BGM** actor in the level, and in the **Details** panel, make sure that the two variables you added are correctly set up: **Active** should be toggled **on**, and the **Volume Multiplier** should be set to **0.5**.

You can try different values for the Volume Multiplier and see what works best for your use case. Since this is the background music, you might want to have its volume set to lower values to keep it subtle.

Now, play the game. You should hear the music that you created play in the background!

## Next Up

In the next module you will learn how to add dynamic footstep sound effects to your player character, that playback different sounds depending on the type of floor the character is currently moving across.

* [![Add Footstep Sounds to a Character](https://dev.epicgames.com/community/api/documentation/image/e85f58fa-4b9d-413d-87f2-9baacc3848e4?resizing_type=fit&width=640&height=640)

  Add Footstep Sounds to a Character

  Make a character produce different step sounds as they move across different surfaces.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#beforeyoubegin)
* [Create Procedural Music with MetaSounds](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#createproceduralmusicwithmetasounds)
* [Set Music Tempo and Rhythm](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#setmusictempoandrhythm)
* [Generate a Melody](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#generateamelody)
* [Synthesize the Melody](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#synthesizethemelody)
* [Shape the Sound With an Envelope](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#shapethesoundwithanenvelope)
* [Play the Music In-Game With Blueprints](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#playthemusicin-gamewithblueprints)
* [Test Your Music In-Game](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#testyourmusicin-game)
* [Next Up](/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds?application_version=5.7#nextup)

Related documents

[MetaSounds

![MetaSounds](https://dev.epicgames.com/community/api/documentation/image/74a01276-fceb-4414-9920-8f7aaddefcc5?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/metasounds-in-unreal-engine)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
