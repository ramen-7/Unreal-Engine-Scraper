<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine?application_version=5.7 -->

# Add Sounds to Fire Traps

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
8. Add Sounds to Fire Traps

# Add Sounds to Fire Traps

Learn how to add a sound effect to a Blueprint.

![Add Sounds to Fire Traps](https://dev.epicgames.com/community/api/documentation/image/1a395027-9967-4729-be00-79e83a4aae1a?resizing_type=fill&width=1920&height=335)

 On this page

In this tutorial, you will add a sound effect to the fire traps in the level. You will create a **Sound Cue** asset to choose which audio file to play, which we have provided with the project files.

You’ll then create a **Sound Attenuation** asset to modify how the sound is perceived by the player. This asset contains settings such as attenuation inner radius and falloff distance, and whether the sound is spatialized in 3D space.

Finally, you’ll update the fire effect’s blueprint to add an **Audio** component, and start or stop the sound effect based on whether the fire is active.

## Before You Begin

Make sure you understand these topics covered in the [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users) documentation:

* Blueprint basics, such as adding and connecting nodes.

You’ll work with the following assets in the [Set Up Your Project and Import Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import):

* **S\_Fire** sound wave file
* **BP\_TrapFire** blueprint

## Create a Sound Cue

To begin, you’ll create a **Sound Cue**, which is a node-based audio asset.

A **Sound Cue** is an audio asset that can contain references to one or more audio files, and instructions on how to manipulate audio as it flows through the graph. This is similar to how Blueprints are used to add functionality and logic to gameplay objects. The **Sound Cue Editor** has a list of **Sound Node** types that you can use to control your sound effects.

To create a Sound Cue asset, follow these steps:

1. In the **Content Browser**, go to the **Content > AdventureGame > Artist** **> Audio** folder.
2. In the **Audio** folder, create a new folder named **Fire**.
3. In the **Fire** folder, right-click the asset area, go to **Audio**, and select **Sound Cue**.
4. Name this asset `SC_FireTrap` and open it.

   [![Content Browser view of Audio > Fire folder with a new Sound Cue](https://dev.epicgames.com/community/api/documentation/image/82ae485a-ec2f-4edf-80c7-1214b668d965?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82ae485a-ec2f-4edf-80c7-1214b668d965?resizing_type=fit)

  The asset opens in the **Sound Cue Editor**, which might feel similar to the Blueprint Editor.

[![](https://dev.epicgames.com/community/api/documentation/image/0dd5f462-40c6-4691-88c8-50691bfe51ae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0dd5f462-40c6-4691-88c8-50691bfe51ae?resizing_type=fit)

The Sound Cue Editor comes with many nodes and settings you can use to customize your sound effects. For this tutorial, you’ll add an audio file you’d like to play and make it loop.

To add an audio file to the Sound Cue, follow these steps:

1. Right-click and add a **Wave Player** node.

   [![Searching for a Wave Player node](https://dev.epicgames.com/community/api/documentation/image/38ca0e60-f768-478b-b827-46c14057279e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38ca0e60-f768-478b-b827-46c14057279e?resizing_type=fit)
2. Connect the Wave Player’s **Output** pin to the **Output** node. The Output node is always the last node in a Sound Cue.

   [![](https://dev.epicgames.com/community/api/documentation/image/46866256-72d7-4714-aa74-b18db6d1ffbc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46866256-72d7-4714-aa74-b18db6d1ffbc?resizing_type=fit)
3. Select the **Wave Player** node. In the panel to the left side of the window, change the **Sound Wave** to the `S_Fire` Sound Wave file you imported in [Set Up Your Project and Import Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import).

   [![](https://dev.epicgames.com/community/api/documentation/image/0a66e01c-a0c3-4390-aa7b-3135b7941ecc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a66e01c-a0c3-4390-aa7b-3135b7941ecc?resizing_type=fit)
4. Turn on **Looping** so the audio can play on repeat.

   [![](https://dev.epicgames.com/community/api/documentation/image/4eb1d257-8c1b-43b2-8344-07c99a15a3f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4eb1d257-8c1b-43b2-8344-07c99a15a3f3?resizing_type=fit)
5. Save the Sound Cue.

You have now created a Sound Cue with the audio file that should play for each fire trap. You can close the sound cue editor.

## Control the Sound With a Sound Attenuation

Next, you need to create a **Sound Attenuation** asset that you can use to change audio settings like the falloff distance, the radius of the audio zone, and more.

Your sound attenuation settings should be set up so that:

* The fire sound is at full volume only within that trap’s bounds.
* The fire sound’s volume decreases (falls off) as the player moves away from the trap.
* The fire sound isn’t audible once the player is a few meters away from the trap.

This ensures the player can’t hear the fire sound until they are in the same room as the traps and they don’t hear audio from all traps at once.

To create a sound attenuation asset, follow these steps:

1. Go to the **Content Browser**. In the **Audio** folder, right-click, go to **Audio**, and select **Sound Attenuation**.
2. Name this asset `SA_FireTrap` and open it. The sound attenuation asset is a data asset, which means that you will see a **Details** panel with several settings.

   [![](https://dev.epicgames.com/community/api/documentation/image/3d8ef8b8-7e87-4e76-bf5f-d9f50c5feaab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d8ef8b8-7e87-4e76-bf5f-d9f50c5feaab?resizing_type=fit)
3. Under the **Attenuation (Volume)** category, change the following settings in the sound attenuation asset:

   1. **Inner Radius: 100**
   2. **Falloff Distance: 600**

      [![](https://dev.epicgames.com/community/api/documentation/image/e8840607-2405-4d12-9637-57d850716441?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8840607-2405-4d12-9637-57d850716441?resizing_type=fit)
4. Save `SA_FireTrap` and close the window.

Now, you have the attenuation settings for your sound effect saved as an asset.

## Modify the Fire Trap Blueprint

In the **BP\_TrapFire** blueprint, you will bring together the **Sound Cue** and **Sound Attenuation** assets and define when the audio should start and stop.

To modify the blueprint, follow these steps:

1. Go to the **Content Browser** and navigate to the **AdventureGame > Designer > Blueprints > Traps** folder.
2. Open the `BP_TrapFire`blueprint.
3. In the **Components** panel, click **Add**, and add an **Audio** component.

   [![](https://dev.epicgames.com/community/api/documentation/image/e07f78ae-c990-41b0-8297-b52361f168dc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e07f78ae-c990-41b0-8297-b52361f168dc?resizing_type=fit)
4. Select the **Audio** component. In the **Details** panel, go to the **Sound** section, and set **Sound** to the `SC_FireTrap`asset you created.

   [![](https://dev.epicgames.com/community/api/documentation/image/97342eae-d8fc-4f2d-a337-036832568338?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97342eae-d8fc-4f2d-a337-036832568338?resizing_type=fit)
5. Optionally, you can modify the **Volume Multiplier** field to change the volume of this sound effect.
6. In the **Attenuation** section, set **Attenuation Settings** to the `SA_FireTrap`.
7. Ensure **Allow Spatialization** is enabled, which makes the audio play at a higher volume if the player is closer to it.

   [![](https://dev.epicgames.com/community/api/documentation/image/a7bb5a4e-ac0f-46a4-bd92-5d58cd6695e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7bb5a4e-ac0f-46a4-bd92-5d58cd6695e6?resizing_type=fit)

Next, you will change the graph of this blueprint to add the logic for starting and stopping the audio. The fire trap gets activated and deactivated, so since that logic already exists, you’ll extend it by adding the relevant nodes.

To add the functionality to stop the audio when the trap is disabled, follow these steps:

1. In the **BP\_TrapFire** blueprint editor, go to the **Event Graph** tab.
2. Locate the red Event **fnBPISwitchOn** node and go to the last node in that sequence. You can use **CTRL + F** to search for a node.

   [![](https://dev.epicgames.com/community/api/documentation/image/c78684df-79b2-4157-bd56-621e6bc4da94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c78684df-79b2-4157-bd56-621e6bc4da94?resizing_type=fit)
3. Drag the **Audio** component into the graph after the **Set Material** node. This creates an **Audio** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/7840513e-eb99-4e12-bf25-46c0d3a74a9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7840513e-eb99-4e12-bf25-46c0d3a74a9e?resizing_type=fit)
4. Drag off the **Audio** node’s pin and add a **Stop** node (under the **Audio** category).
5. From the **Audio** node, drag the **exec input** pin and connect it to the **Set Material** node’s **exec** pin. This will stop playing the sound that the **Audio** component plays.

   [![](https://dev.epicgames.com/community/api/documentation/image/a9236eeb-1511-48c3-9788-b0cf5bfe6deb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9236eeb-1511-48c3-9788-b0cf5bfe6deb?resizing_type=fit)

Under this sequence of nodes, you’ll see another sequence that starts with the **Event fnBPIButtonOff** node.

[![](https://dev.epicgames.com/community/api/documentation/image/64965840-2764-4d37-9278-05632e8e21cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64965840-2764-4d37-9278-05632e8e21cc?resizing_type=fit)

To play the audio when the trap is active, follow these steps:

1. Locate the red **Event fnBPISwitchOff** node and go to the last node in that sequence.
2. Drag off the **Set Material** node’s **exec** pin,  search for **play** **audio** in the node actions list, and add a **Play (Audio)** node. The Audio component is automatically added as the **Target**.

   [![](https://dev.epicgames.com/community/api/documentation/image/643b8a3f-05aa-42a0-b0e9-51cdbf9454c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/643b8a3f-05aa-42a0-b0e9-51cdbf9454c6?resizing_type=fit)
3. Compile and Save the blueprint.

Now, you have modified the fire trap’s blueprint to play the sound effect upon activation. Your final blueprint graph should look like this:

[![](https://dev.epicgames.com/community/api/documentation/image/a10ad5f9-6396-4c97-ae87-7e3c2acc8d24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a10ad5f9-6396-4c97-ae87-7e3c2acc8d24?resizing_type=fit)

You can now close the `BP_TrapFire`blueprint editor.

In the level viewport, if you select a fire trap in your level, you’ll see two spherical wireframes around the actor: the inner sphere shows the sound’s **Inner Radius**, and the outer sphere shows the sound’s **Falloff Distance**.

You can now play your game and hear the sound effect when the fire traps are active!

## Next Up

Next, you’ll continue working with audio and learn to use Unreal Engine’s Metasounds system to procedurally generate background music for your level.

* [![Create Procedural Music](https://dev.epicgames.com/community/api/documentation/image/ee725e45-9ab6-484f-b4c8-969dbba1fb80?resizing_type=fit&width=640&height=640)

  Create Procedural Music

  Create Procedural Music with MetaSounds.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine?application_version=5.7#beforeyoubegin)
* [Create a Sound Cue](/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine?application_version=5.7#createasoundcue)
* [Control the Sound With a Sound Attenuation](/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine?application_version=5.7#controlthesoundwithasoundattenuation)
* [Modify the Fire Trap Blueprint](/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine?application_version=5.7#modifythefiretrapblueprint)
* [Next Up](/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine?application_version=5.7#nextup)

Related documents

[Sound Sources

![Sound Sources](https://dev.epicgames.com/community/api/documentation/image/49e98eb3-8208-45d6-9b3b-39d305efdc4d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/sound-sources-in-unreal-engine)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
