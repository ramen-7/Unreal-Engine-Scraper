<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-your-niagara-systems?application_version=5.7 -->

# Rendering your Niagara Systems

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Tutorials](/documentation/en-us/unreal-engine/tutorials-for-niagara-effects-in-unreal-engine "Niagara Tutorials")
7. [Niagara for Linear Content](/documentation/en-us/unreal-engine/niagara-for-linear-content "Niagara for Linear Content")
8. Rendering your Niagara Systems

# Rendering your Niagara Systems

Learn how to set up and render your Niagara systems in Unreal Engine.

![Rendering your Niagara Systems](https://dev.epicgames.com/community/api/documentation/image/13744d85-3dda-468e-9f13-af8d69625bf8?resizing_type=fill&width=1920&height=335)

 On this page

## Configuring your Project

Before creating a Level Sequence, click **Settings > Plugins** to open the **Plugins window** and **enable** the following plugins:

* Niagara MRQ Support
* Niagara SIM Caching

Restart the editor if prompted. Now you are ready to create your Level Sequence.

## Creating a Level Sequence

Follow these steps to create a **Level Sequence** with a **Camera** and generate frames with the **Movie Render Queue (MRQ)**:

1. Right-click in the **Content Browser**, navigate to **Cinematics** and create a **Level Sequence**.
2. Rename your Level Sequence to something appropriate.
3. Double-click the Level Sequence to open it.
4. Click the **Camera** button at the top of the Sequencer panel to create a new **Cine Camera** and a **Camera Cuts track**.
5. Use the 3D view controls to position your camera to a framing that you like.

## Rendering Frames with Movie Render Queue

1. Press the **Clapper Board** button on the top of the **Sequencer panel** to open **Movie Render Queue (MRQ)**.
2. If you have ffmpeg configured:
   * Click on the **Settings** for your sequence, probably called '**Unsaved Config**'.
   * Press the **+Setting** button
   * Add a **Command Line Encoder** settings block.
   * Press the **Accept** button to leave the Settings dialog.
3. On the Movie Render Queue panel, press the **Render (Local)** button.

MRQ will now run. It may compile necessary shaders as a first step before showing you a preview of the frames being generated.



If you do not have the FFmpeg codec installed on your computer, read the [How to use FFmpeg with the Command Line Encoder in Movie Render Queue](https://dev.epicgames.com/community/learning/tutorials/BbYV/unreal-engine-how-to-use-ffmpeg-with-the-command-line-encoder-in-movie-render-queue) document to learn how to install it.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuring your Project](/documentation/en-us/unreal-engine/rendering-your-niagara-systems?application_version=5.7#configuringyourproject)
* [Creating a Level Sequence](/documentation/en-us/unreal-engine/rendering-your-niagara-systems?application_version=5.7#creatingalevelsequence)
* [Rendering Frames with Movie Render Queue](/documentation/en-us/unreal-engine/rendering-your-niagara-systems?application_version=5.7#renderingframeswithmovierenderqueue)
