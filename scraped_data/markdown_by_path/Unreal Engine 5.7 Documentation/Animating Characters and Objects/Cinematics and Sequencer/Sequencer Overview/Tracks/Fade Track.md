<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7 -->

# Fade Track

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Sequencer Overview](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview "Sequencer Overview")
8. [Tracks](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine "Tracks")
9. Fade Track

# Fade Track

The Fade Track in Sequencer is used to fade the entire screen to a solid color. With it, you can fade to black, white, or any other color.

![Fade Track](https://dev.epicgames.com/community/api/documentation/image/ac5e0f6e-21e7-4c06-9837-17a5e097b171?resizing_type=fill&width=1920&height=335)

 On this page

There may be times when you want to fade in or out of your Level Sequence. You can accomplish this using the Fade Track. This page provides an overview of the Fade Track, as well as additional considerations when fading your cinematics.

#### Prerequisites

* You have an understanding of [Sequencer](/documentation/404).
* If you are fading between gameplay and cinematics, then you should have an understanding of [Blueprints](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine).

## Fade Track Overview

### Creation and Usage

To create a Fade Track, click **Add track (+)** and select **Fade Track**.

![create fade track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65bf0e8d-2e87-49b4-bfe5-1895d717d344/create1.png)

The Fade Track is a [Float Property Track](/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#float) that you animate between values of **0** (no fade) and **1** (fully faded).

Set keyframes on the track by selecting the Fade Track and pressing **Enter**, which keys the default value of **0**. Next, move the playhead to a new time and change the track value to **1**, which sets a new key with that value at the playhead time.

![keyframe fade track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0219568-5fa4-422c-a537-fc9bba54f02a/create2.gif)

Now, when playing your sequence, you should see the fade happen gradually.

![fade track playing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88c335b1-0427-49d1-8e68-1cb4cede45f2/create3.gif)

### Fade Color and Settings

You can change the color of the fade and adjust other fade settings by right-clicking the fade section and navigating to the **Properties** menu.

![fade track properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f82b45c5-7a32-499f-bccd-4e3d012ce3ec/properties1.png)

The following properties have special interaction with the **Fade Track**:

| Name | Description |
| --- | --- |
| **When Finished** | Determines what the property should do when the section finishes. You can select either:   * **Keep State**, which can be used to persist your fade after the sequence ends for the length of the fade section. * **Restore State**, which restores the fade back to its state before it was animated. * **Project Default**, which uses the settings defined in your `DefaultEngine.ini` project file. By default, it is set to **Restore State**. |
| **Fade Color** | You can change the color of the fade effect to be any color you want. In some cases, you may want to fade to white instead of fading to black. The track section inherits the color specified here to indicate the color the Fade Track is fading to. |
| **Fade Audio** | Enabling this causes the fade effect to also reduce the audio of all sounds playing, including sounds from the [Audio Track](/documentation/en-us/unreal-engine/cinematic-audio-track-in-unreal-engine), during runtime. |

Because Fade Color is set on the [section](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine#sections), you need to create two different fade sections if you want to have fades with different colors in a single sequence.

![create different sections for each fade color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41fa5a44-3996-48e8-8031-9ef6b756d324/colornote.png)

## Fading Between Gameplay and Cinematics

The Fade Track is essentially a track version of the **Set Manual Camera Fade** Blueprint function. Because of this, you can use both the Fade Track and camera fade functions to script fading behavior. This can be useful if your project requires you to create fade transitions between gameplay and cinematics.

![camera fade functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93b8c2b2-6e8d-4e1f-858f-a7d737e17f59/transition1.png)

Fading using these Blueprint functions requires targeting the **Player Camera Manager**. You can get a reference to this Object by right-clicking in the graph and selecting **Get Player Camera Manager**.

![get player camera manager function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0a7c217-217a-407d-81af-916d42aa6e4b/transition2.png)

In your Sequence, you must also set your fade section property **When Finished** to **Keep State**. By default, when the Sequence ends, the fade state reverts back to its previous state before Sequencer begins to play. Keep State overwrites this with the final value from the Fade Track. This may be required in cases to ensure that the Fade Track propagates after the Sequence ends.

![set when finished to keep state](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/255fe40e-e6de-4690-892a-5c64639f283a/transition4.png)

### Gameplay to Cinematic

If you need to cover a transition from gameplay to cinematic with a fade, do the following:

![fade from gameplay to cinematic](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9b3d9b3-2b37-4299-a4e3-ec1bd48a7c1c/transition3.png)

1. Create a **Start Camera Fade** node and set the following parameters on it:

   * Connect **Get Player Camera Manager** to **Target**.
   * Set **To Alpha** to **1**.
   * Set **Duration** to any number greater than **0**, which is the length (in seconds) of the blend. The fade will not work if Duration is 0.
   * Enable **Hold when Finished**, which holds the fade until Sequencer fades in with the Fade Track.
2. Add a **Delay** node that executes after Start Camera Fade and set **Duration** to the same number as Start Camera Fade's Duration. Start Camera Fade's out execution does not occur on fade complete, so you need a delay to wait for the fade to complete before continuing.
3. Play your Sequence, which contains a **Fade Track** fading in, and **When Finished** is set to **Keep State**, to ensure the fade does not revert after the Sequence ends.

### Cinematic to Gameplay

If you need to cover a transition from cinematic to gameplay with a fade, do the following:

![fade from cinematic to gameplay](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a8359e9-22a8-4013-b05f-56abcaca2e15/transition5.png)

1. Create an **On Finished** event bound to your Sequence, which contains a **Fade Track** fading out, and **When Finished** is set to **Keep State**.
2. Create a **Start Camera Fade** node and set the following parameters on it:

   * Connect **Get Player Camera Manager** to **Target**.
   * Set **From Alpha** to **1**.
   * Set **Duration** to any number greater than **0**, which is the length (in seconds) of the blend. The fade will not work if Duration is 0.
   * Enable **Hold when Finished**, which holds the fade in and does not revert back to faded out, due to Sequencer keeping the Fade Track state.

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#prerequisites)
* [Fade Track Overview](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#fadetrackoverview)
* [Creation and Usage](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#creationandusage)
* [Fade Color and Settings](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#fadecolorandsettings)
* [Fading Between Gameplay and Cinematics](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#fadingbetweengameplayandcinematics)
* [Gameplay to Cinematic](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#gameplaytocinematic)
* [Cinematic to Gameplay](/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine?application_version=5.7#cinematictogameplay)
