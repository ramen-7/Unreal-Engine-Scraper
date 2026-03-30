<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine?application_version=5.7 -->

# Create Camera Animation

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
7. [Sequencer Basics](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine "Sequencer Basics")
8. Create Camera Animation

# Create Camera Animation

A beginner's look at how to create camera animation in Sequencer.

![Create Camera Animation](https://dev.epicgames.com/community/api/documentation/image/d7b300d0-deb4-416a-880d-d526fe4fa7a3?resizing_type=fill&width=1920&height=335)

 On this page

This page provides a beginner's overview of creating camera animations in Sequencer and is intended for those who are new to Cinematics and Unreal Engine.

#### Prerequisites

* You have read through the [Sequencer Basics](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) page and have already created and opened a **Level Sequence** in your level.
* You have a basic understanding of [Viewport navigation and controls](/documentation/en-us/unreal-engine/viewport-controls-in-unreal-engine).

## Creating a Camera

Start by creating a [Cine Camera Actor](/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine) in your sequence. The quickest way to do this is by clicking **Create New Camera** in the Sequencer toolbar. This will create a Cine Camera Actor as a [spawnable](/documentation/404) for this sequence and automatically update your viewport's perspective to the Camera Actor's (this is referred to as **Piloting**).

![create camera sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9b3f29d-052f-4cf8-91b4-f994bb4c2d5c/createcamera.png)


To ensure that you are correctly piloting the camera, make sure **Lock Cine Camera** is enabled on the camera you want to control.

![enable camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f61850d0-64f6-4109-9ad2-bfed50354e4f/cameraenable.png)

## Creating Transform Keyframes

Next, you can start setting up your camera animation. From the viewport, align your camera to the initial position and framing you want to use. Then, navigate to the camera's [Transform Track](/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine#transformtrack), select it, and press **Enter**. This will set an initial transform [keyframe](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine) for the camera.

![create camera keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5a26c83-7473-44ec-872b-16c0e4218127/setfirstkey.gif)

Next, move the playhead marker to a later point in the sequence by dragging it along the timeline.

![sequencer scrub](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/710028b8-062d-4a48-b30c-a4650a256e1c/timeadjust.png)

Lastly, move the camera in the viewport to a new position. Once done, return to the **Transform track**, select it, and press the **Enter** key to place another transform keyframe.

![create camera keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffb282d5-0dad-4275-a6f4-ade46180fe07/setsecondkey.gif)

## Previewing your Results

To preview your camera animation, click **Play** in the Sequencer playback controls. You may now also continue to further refine your camera animation by adding more keyframes to your sequence.

![play sequencer camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a4cdf59-e4bd-40fc-914b-f97d6a06a422/play.gif)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [camera](https://dev.epicgames.com/community/search?query=camera)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine?application_version=5.7#prerequisites)
* [Creating a Camera](/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine?application_version=5.7#creatingacamera)
* [Creating Transform Keyframes](/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine?application_version=5.7#creatingtransformkeyframes)
* [Previewing your Results](/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine?application_version=5.7#previewingyourresults)
