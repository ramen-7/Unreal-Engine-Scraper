<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7 -->

# Meerkat Demo

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Engine Feature Examples](/documentation/en-us/unreal-engine/engine-feature-examples-for-unreal-engine "Engine Feature Examples")
7. Meerkat Demo

# Meerkat Demo

How to set up the Meerkat demo, render it with Movie Render Queue, and explore its animation and optimization features

![Meerkat Demo](https://dev.epicgames.com/community/api/documentation/image/8b6a4c85-7bed-48fe-b760-add50cd6c95a?resizing_type=fill&width=1920&height=335)

 On this page

Real-time rendering technology is an increasingly important tool in the filmmaking process, from previsualization to the final render, as it enables filmmakers to review and iterate on digital scenes and effects very quickly. The **Meerkat Demo** by Weta Digital is a short film rendered entirely in **Unreal Engine**, built to explore the highest level of quality possible while maintaining as fast a rendering speed as possible. With the right graphics card, the Meerkat short will run in real time. This document will guide you through the process of outputting a high-quality render of the Meerkat short yourself using the **Movie Render Queue** plugin.

This sample is available for Unreal Engine 5 and later. Be aware that it is an especially graphically intensive scene, and needs a powerful video card to run at a stable framerate.

## Required Setup

To set up a project with the Meerkat sample, follow these steps:

1. Access the [Meerkat sample](https://fab.com/s/094cb6da0970) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

   1. To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).
4. Open your new project in the **Unreal Editor**.
5. Open the **Edit** > **Plugins** window and navigate to the **Built-In** > **Rendering** section. Make sure that the **Movie Render Queue** plugin is enabled and, if necessary, restart the editor.

   [![Enabling the Movie Render Queue plugin](https://dev.epicgames.com/community/api/documentation/image/003fcd3c-1b00-4fba-9ab1-076e13ceac24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/003fcd3c-1b00-4fba-9ab1-076e13ceac24?resizing_type=fit)

   Enabling the Movie Render Queue plugin. Click the image to enlarge it.

## Viewing the Meerkat Sequence

Once you have loaded Unreal Editor and opened the Meerkat Demo project, go to the **Content Drawer** and double-click **Master\_SEQ**.

[![Master_SEQ location in the content drawer](https://dev.epicgames.com/community/api/documentation/image/62901519-335f-4572-bd65-aaf0af5a1f0d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/62901519-335f-4572-bd65-aaf0af5a1f0d?resizing_type=fit)

This opens **Sequencer** and loads the Master\_SEQ level sequence.

[![The Master_SEQ level sequence loaded in the Sequencer tab](https://dev.epicgames.com/community/api/documentation/image/972dbb33-1ceb-4b02-9e03-a08b7da2f1f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/972dbb33-1ceb-4b02-9e03-a08b7da2f1f9?resizing_type=fit)

The Master\_SEQ level sequence is loaded in the Sequencer tab. Click the image to enlarge it.

You can scrub the timeline through the different shots by clicking on the timeline.

[![The timeline for Master_SEQ](https://dev.epicgames.com/community/api/documentation/image/09cbb294-eef8-44b0-829b-55dd63930ec3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/09cbb294-eef8-44b0-829b-55dd63930ec3?resizing_type=fit)

The timeline for the Master\_SEQ level sequence. Click the image to enlarge it.

If you want to be able to see the shots through the cinematic cameras set up in the scene, you can click on the **camera icon** for **Shots**. Your viewport will then look through the camera corresponding to the position of the timeline.

[![The toggle for Cinematic camera mode in the Sequencer tab](https://dev.epicgames.com/community/api/documentation/image/2d468a41-5f18-48df-ba02-719fa03e8ff7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d468a41-5f18-48df-ba02-719fa03e8ff7?resizing_type=fit)

The toggle button for Cinematic camera mode as it appears in the Sequencer tab. Click the image to enlarge it.

You can also change your viewport mode from Perspective to **Cinematic Viewport**.

[![Changing to Cinematic Viewport Mode using the Viewport controls](https://dev.epicgames.com/community/api/documentation/image/a6024aa8-5126-42b9-a5d9-36b695aee79c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a6024aa8-5126-42b9-a5d9-36b695aee79c?resizing_type=fit)

Changing to Cinematic Viewport Mode using the Viewport controls. Click the image to enlarge it.

For more information about working with Sequencer, refer to the [Sequencer Editor](animating-characters-and-objects/Sequencer/) section.

## Optimization Settings

To improve performance, the Meerkat demo uses low-resolution settings by default. If you want the highest-quality visual, there are several optimization settings you can change.

### Toggling High-Resolution Environment Meshes

In the **Outliner**, click the **VisualSettings\_BP** Blueprint. In the **Details** tab, under **Default**, you will find the **Highres Env Meshes** setting. Your scene will have improved fidelity with it turned on, but it will run slightly faster with it turned off.

![Highres Meshes Off](https://dev.epicgames.com/community/api/documentation/image/b60c424a-7664-416c-b722-5c592afe8c00?resizing_type=fit&width=1920&height=1080)

![Highres Meshes On](https://dev.epicgames.com/community/api/documentation/image/bccc6860-18c9-416e-b1fe-b85eeb87daca?resizing_type=fit&width=1920&height=1080)

Highres Meshes Off

Highres Meshes On

*Move the slider to compare the scene without high-resolution environment meshes versus with them turned on.*

### Changing the Eagle's Groom Resolution

The **Eagle** in the Meerkat demo uses a **Groom** hair asset to represent its feathers. By default, it uses a low-resolution groom to improve performance, but you can change this to a high-resolution asset instead.

1. In the **Outliner**, click the **Characters** group, then select **amlEagle\_BP** and look at its **Details** tab.
2. Select the **Groom** property, which is listed under **amlEagle\_BP(self)** in the **Details** tab.

   [![The Groom property in the Details tab](https://dev.epicgames.com/community/api/documentation/image/0c647ac3-9151-4e5c-8cae-ef176bab8f39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c647ac3-9151-4e5c-8cae-ef176bab8f39?resizing_type=fit)

   You can access the Groom properties from the Details tab. Click the image to enlarge it.
3. There are both a **Groom Asset** and **Binding Asset**, and each has a dropdown menu to the right of the icon.

   1. Click the **Groom Asset** menu, then change the groom from amlEagle\_groomLowRes\_r036\_GRO to **amlEagle\_highRes\_GRO**.
   2. Click the **Binding Asset**, then change it from amlEagle\_groomLowRes\_r036\_GRB to **amlEagle\_highRes\_GRB**.

![Low-res Groom Asset](https://dev.epicgames.com/community/api/documentation/image/577187f1-6169-4f6f-9bfe-cf64b8d49e48?resizing_type=fit&width=1920&height=1080)

![High-res Groom Asset](https://dev.epicgames.com/community/api/documentation/image/c0aae84c-5b94-49aa-a16f-0dada746457e?resizing_type=fit&width=1920&height=1080)

Low-res Groom Asset

High-res Groom Asset

*Move the slider to compare the Eagle with low-resolution groom assets versus high-resolution assets. Note the finer detail in the feathers.*

For more information about working with Groom assets, refer to the [Groom Asset Editor User Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-asset-editor-user-guide-in-unreal-engine).

## Rendering the Meerkat Demo With Movie Render Queue

To render the Meerkat Demo, you need the [Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine#movie-render-queue), which is used for outputting high-quality renders of Sequencer movies. Review the steps in [Required Setup](https://dev.epicgames.com/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine#required-setup) to ensure that you have the Movie Render Queue plugin enabled, then follow the steps below to set up a rendering job:

1. Launch the Movie Render Queue by selecting **Window** > **Cinematics** > **Movie Render Queue**.

   [![Accessing the Movie Render Queue](https://dev.epicgames.com/community/api/documentation/image/1e1e2d9e-c365-4d3b-a085-22e67d31d3e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e1e2d9e-c365-4d3b-a085-22e67d31d3e1?resizing_type=fit)
2. In the top-left corner of the **Movie Render Queue window**, click the **+ Render** button. Select **Master\_SEQ** from the dropdown menu.

   [![Accessing the Master_SEQ from the + Render dropdown](https://dev.epicgames.com/community/api/documentation/image/640bf602-a915-4cc7-a0ae-41a113fd5e02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/640bf602-a915-4cc7-a0ae-41a113fd5e02?resizing_type=fit)

   Accessing Master\_SEQ from the + Render dropdown. Click the image to enlarge it.

   This will add an entry to the Movie Render Queue's list of **jobs** to render.
3. In the entry for Master\_SEQ, click **Unsaved Config** under the **Settings** column to open the **Settings Window**.

   [![Clicking Unsaved Config opens the Settings window.](https://dev.epicgames.com/community/api/documentation/image/04f7c177-881b-4840-8473-98725a8b7059?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04f7c177-881b-4840-8473-98725a8b7059?resizing_type=fit)
4. In the Settings Window, click the **Load/Save Presets** dropdown in the top right corner and select the **MoviePipelineConfig\_Temporal** preset.

   [![Selecting the MoviePipelineConfig_Temporal preset](https://dev.epicgames.com/community/api/documentation/image/822cee90-c11a-4037-8125-1b776f25d195?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/822cee90-c11a-4037-8125-1b776f25d195?resizing_type=fit)

   Selecting the MoviePipelineConfig\_Temporal preset and applying it to the shot. Click the image to enlarge it.

You now have the settings needed for rendering the Meerkat demo. In the Settings window, you will see a list along the left side of the window that represents items that have been explicitly set for this project. You can edit these settings to change the output directory for the rendered images, change the type of image that will be saved, or edit post-processing settings. Click the **Accept** button on the bottom right corner to close the window.

[![Movie Render Queue settings window with the applied settings](https://dev.epicgames.com/community/api/documentation/image/d27b4509-6fcd-4968-9b34-29b195c0e606?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d27b4509-6fcd-4968-9b34-29b195c0e606?resizing_type=fit)

The Settings window with the applied settings from MoviePipelineConfig\_Temporal. Click the image to enlarge it.

Note: The image above displays a warning icon in the **Settings** window. If you click it, you can see the warning details. The TAA samples in the project are set to 16, but the warning will appear anyway. You can ignore this warning.

To launch the render, click the **Render (Local)** button in the lower-right corner of the Movie Render Queue window.

[![The Render (Local) button will start rendering your video](https://dev.epicgames.com/community/api/documentation/image/93f68181-3037-4136-a006-d5b6105523d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93f68181-3037-4136-a006-d5b6105523d2?resizing_type=fit)

Finalized settings in the Movie Render Queue window. Click the image to enlarge it.

A Render Preview window will appear, showing information related to the render.

[![The render preview for Movie Render Queue](https://dev.epicgames.com/community/api/documentation/image/26d0da71-3ded-422d-b7ac-3050663bffdb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/26d0da71-3ded-422d-b7ac-3050663bffdb?resizing_type=fit)

The Movie Render Queue preview window displays information about the rendering progress. Click the image to enlarge it.

For more information about how to use Movie Render Queue, refer to the [Movie Render Queue section](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) of the Sequencer workflow guides.

## Adding the Meerkat Control Rig to a Shot

This project includes a **control rig** for the Meerkat, which you can use to explore some keyframe animation inside Unreal Editor. To use this control rig, you need to add the **amlMeerkat\_BP** into a shot in Sequencer. The easiest way to do this is to create a new level sequence.

1. Select **Cinematics** > **Add Level Sequence**.

   [![Add Level Sequence](https://dev.epicgames.com/community/api/documentation/image/22bab12f-0172-4f52-ac9d-f25942a6faa6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22bab12f-0172-4f52-ac9d-f25942a6faa6?resizing_type=fit)
2. In the **Save Asset As** window, navigate to the **Levels** folder, name the level sequence **MeerkatAnim\_SEQ**, then click **Save**. The level sequence you just saved will become the active sequence in Sequencer.

   [![Saving the new sequence](https://dev.epicgames.com/community/api/documentation/image/ee999330-9fb6-449b-9bd0-ca508017006b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee999330-9fb6-449b-9bd0-ca508017006b?resizing_type=fit)

   Saving the new sequence to use with the Meerkat control rig. Click the image to enlarge it.

   You can return to the original sequence by locating Master\_SEQ in the Content Drawer and double-clicking it.
3. In the Content Drawer, open the **Content** > **Assets** > **meerkat** > **Blueprints** folder and locate the **amlMeerkat\_BP** asset.

   [![The location of the Meerkat control rig asset](https://dev.epicgames.com/community/api/documentation/image/6e6d1d05-2ab6-4080-a0fc-03522253d293?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e6d1d05-2ab6-4080-a0fc-03522253d293?resizing_type=fit)

   The Meerkat control rig asset in the Content Drawer. Click the image to enlarge it.
4. Click and drag the **amlMeerkat\_BP** asset into **MeerkatAnim\_SEQ**.

   [![Clicking and dragging the Meerkat control rig asset into the sequence](https://dev.epicgames.com/community/api/documentation/image/386eb864-464b-450a-9724-eee4b4a9e9b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/386eb864-464b-450a-9724-eee4b4a9e9b0?resizing_type=fit)

   Clicking and dragging the Meerkat control rig Blueprint into the sequence. Click the image to enlarge it.

You now have a copy of the Meerkat asset with a control rig that you can use in your level sequence.

[![The Meerkat control rig in the Sequencer timeline](https://dev.epicgames.com/community/api/documentation/image/346e84d1-e96f-460f-9755-56167163c859?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/346e84d1-e96f-460f-9755-56167163c859?resizing_type=fit)

Keyframing the Meerkat control rig in the Sequencer timeline. Click the image to enlarge it.

You can edit its parameters in the timeline or manipulate the control rig directly in the viewport.

[![The Meerkat control rig visible in the level](https://dev.epicgames.com/community/api/documentation/image/d774e23f-0ae6-49e0-8c68-8755de60f1d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d774e23f-0ae6-49e0-8c68-8755de60f1d2?resizing_type=fit)

Manipulating the control rig in the level viewport. Click the image to enlarge it.

If you are trying to use the Meerkat control rig and you do not have a high-end graphics card, you can turn the visibility of the groom component off to hide the fur, which will improve performance.

To do this, click on the Meerkat in your viewport to display its information in the details panel. Under SkeletalMeshComponent click on Groom(Inherited), scroll down to Rendering, and turn off the Visible flag.

[![Groom visibility checkbox](https://dev.epicgames.com/community/api/documentation/image/9f39679b-3cfd-473e-b59c-1652bd257071?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f39679b-3cfd-473e-b59c-1652bd257071?resizing_type=fit)

Manipulating the control rig in the level viewport. Click the image to enlarge it.

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [groom](https://dev.epicgames.com/community/search?query=groom)
* [movie render queue](https://dev.epicgames.com/community/search?query=movie%20render%20queue)
* [groom asset](https://dev.epicgames.com/community/search?query=groom%20asset)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Required Setup](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#required-setup)
* [Viewing the Meerkat Sequence](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#viewing-the-meerkat-sequence)
* [Optimization Settings](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#optimization-settings)
* [Toggling High-Resolution Environment Meshes](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#toggling-high-resolution-environment-meshes)
* [Changing the Eagle's Groom Resolution](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#changingtheeagle'sgroomresolution)
* [Rendering the Meerkat Demo With Movie Render Queue](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#rendering-the-meerkat-demo-with-movie-render-queue)
* [Adding the Meerkat Control Rig to a Shot](/documentation/en-us/unreal-engine/meerkat-sample-project-for-unreal-engine?application_version=5.7#adding-the-meerkat-control-rig-to-a-shot)
