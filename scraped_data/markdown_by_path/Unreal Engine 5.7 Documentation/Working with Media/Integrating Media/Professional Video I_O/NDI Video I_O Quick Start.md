<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7 -->

# NDI Video I/O Quick Start

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Professional Video I/O](/documentation/en-us/unreal-engine/professional-video-io-in-unreal-engine "Professional Video I/O")
8. NDI Video I/O Quick Start

# NDI Video I/O Quick Start

A step-by-step guide to getting video from an NDI source into Unreal Engine, and sending captured video output from Unreal Engine out to an external NDI application.

![NDI Video I/O Quick Start](https://dev.epicgames.com/community/api/documentation/image/80dc9256-fa91-4f10-9c74-2bd3a10ec10d?resizing_type=fill&width=1920&height=335)

 On this page

In this Quick Start guide, we walk through the process of setting up an Unreal Engine Project to work with NDI for both video input and output. At the end of this guide:

* You'll have video input from your NDI source playing inside your Unreal Engine Project.
* You'll be able to capture camera viewpoints both from the Editor and from your runtime application, and send them out as a stream through NDI.

For a working example that shows many of the elements described below put into practice, see the [Virtual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine) showcase, available on the Samples tab of the Epic Games Launcher.

**Prerequisites**:

* Make sure that you download and install the NDI Tools from the NDI site.
* Make sure that your NDI source is set up, and that you have some video streaming from it. The NDI Test Patterns are a good starting point.
* Open an Unreal Engine Project that you want to integrate with your video stream. This page shows the steps in an empty Blueprint-enabled project, but the same steps will work equally well in any Project.

The NDI Media components used in this guide are built on top of the [Media Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-in-unreal-engine), and you'll use [Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) to script the video capturing process at runtime. Some prior knowledge of these topics is recommended but not required.

## 1 - Set Up the Project

Before you can get video input from your NDI source into your Unreal Engine Level, and stream output from Unreal Engine using NDI, you'll need to do some basic setup to enable the NDI Media Player Plugin in your Project.

### Steps

1. Open the Project that you want to use with NDI in the Unreal Editor.
2. From the main menu, select **Edit > Plugins**.
3. In the Plugins window, find the NDI Media Player plugin under the Media Players category. Check its Enabled checkbox.

   [![NDI plugin](https://dev.epicgames.com/community/api/documentation/image/fc203e36-2d94-4270-a623-59220611b82d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc203e36-2d94-4270-a623-59220611b82d?resizing_type=fit)
4. Find the Media Framework Utilities Plugin under the Media Players category. Check its Enabled checkbox, if it's not already checked.

   [![Media Framework Utilities plugin](https://dev.epicgames.com/community/api/documentation/image/1a9c2690-f9a9-4d16-b000-9558cda3d692?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a9c2690-f9a9-4d16-b000-9558cda3d692?resizing_type=fit)
5. Click **Restart Now** to restart the Unreal Editor and reopen your Project.

   [![Restart Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/2bf83106-1dac-424f-88b6-d1815bde0e42?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2bf83106-1dac-424f-88b6-d1815bde0e42?resizing_type=fit)

### End Result

Your Project is now ready to accept video from your NDI source, and to stream rendered output using NDI. In the next sections, you'll set it up and start playing video in and out.

## 2 - Rendering Video Input in Unreal Engine

In this process, you'll make video input from the NDI source visible in the current Level in the Unreal Editor. This process uses a [Media Plate](https://dev.epicgames.com/documentation/en-us/unreal-engine/the-media-plate-actor-in-unreal-engine) actor, a direct way to show the video input that automatically sets up standard settings which are functional in most cases.

### Steps

1. Open the **Content Drawer**, and select the **Content** folder. Right-click, and choose **New Folder** from the context menu. Name your new folder **NDI**.

   [![New NDI folder](https://dev.epicgames.com/community/api/documentation/image/04e81ef1-6319-4c5d-9d4e-679a4489b5ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04e81ef1-6319-4c5d-9d4e-679a4489b5ec?resizing_type=fit)
2. Open your new folder, then right-click and select **Media > NDI Media Source**.

   [![New NDI Media Source](https://dev.epicgames.com/community/api/documentation/image/267bf408-84b0-47b6-9575-1d210a8834aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/267bf408-84b0-47b6-9575-1d210a8834aa?resizing_type=fit)
3. Your new asset is named automatically by UE, so rename it something descriptive like **NDI\_Quick\_Start\_Source**.

   [![Rename NDI Media Source](https://dev.epicgames.com/community/api/documentation/image/841aa496-8e66-4e0e-a239-2abaecd70bac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/841aa496-8e66-4e0e-a239-2abaecd70bac?resizing_type=fit)
4. Save your new asset by clicking the **Save All** button in the **Content Drawer**, or by pressing ctrl+S.

   [![Save all](https://dev.epicgames.com/community/api/documentation/image/cb3db292-4f7f-400f-85db-e73a8e6372fb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb3db292-4f7f-400f-85db-e73a8e6372fb?resizing_type=fit)
5. Double-click your **NDI Media Source** asset to open it in the **Media Editor**. If you only have one NDI source running locally, it is automatically detected as the default media source in the **Configuration** dropdown menu. However, the NDI test pattern doesn't show in the playback window yet.

   [![NDI Media Source open in Unreal Editor](https://dev.epicgames.com/community/api/documentation/image/a28a58b8-810a-4453-8a83-b74d28d337d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a28a58b8-810a-4453-8a83-b74d28d337d0?resizing_type=fit)
6. Click **Open** in the Toolbar to show the media from the NDI source. You now see the NDI test pattern you chose in the playback window. The other settings are fine for the purposes of this quick start. Save and close your Media Source when you're done.

   For more information on the NDI Media Source settings, refer to the [NDI Media Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndi-media-reference).

   [![Open the NDI test pattern source](https://dev.epicgames.com/community/api/documentation/image/d4507999-d8eb-4973-a9dd-1327653ff0d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4507999-d8eb-4973-a9dd-1327653ff0d0?resizing_type=fit)
7. Go back to the **Content Drawer**, then drag your **NDI Media Source** asset into the level. This automatically creates a **Media Plate** actor connected to your NDI Media Source.

   [![Drag NDI Media Source](https://dev.epicgames.com/community/api/documentation/image/0ac5478b-9a3e-41c7-9ba0-994e5587e821?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ac5478b-9a3e-41c7-9ba0-994e5587e821?resizing_type=fit)
8. Initially, the Media Plate actor does not show the NDI test pattern. Select the **Media Plate** actor in the **World Outliner** panel, then click **Open Media Plate** in the **Details** panel to open the Media Plate actor in the editor.

   [![Media Plate actor before opening media](https://dev.epicgames.com/community/api/documentation/image/e4a17518-395d-4dd4-89b4-a0775e1e03b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4a17518-395d-4dd4-89b4-a0775e1e03b4?resizing_type=fit)
9. In the editor, click **Open** in the **Toolbar**. The NDI test pattern now appears in the playback window.

   [![NDI test pattern in Media Plate actor in the Unreal Editor](https://dev.epicgames.com/community/api/documentation/image/6a294ff0-c41d-49af-abf4-3803f5441db1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6a294ff0-c41d-49af-abf4-3803f5441db1?resizing_type=fit)
10. Return to the Viewport, where your Media Plate actor is now displaying the NDI media in your level.

    [![NDI test pattern on Media Plate actor in UE level](https://dev.epicgames.com/community/api/documentation/image/395941ac-10e7-45e0-b690-68804e3489b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/395941ac-10e7-45e0-b690-68804e3489b5?resizing_type=fit)

### End Result

At this point, you should have media from an NDI source appearing inside your Unreal Engine level on a Media Plate actor. If you want to modify the display settings of your Media Plate actor, refer to the [Media Plate](https://dev.epicgames.com/documentation/en-us/unreal-engine/the-media-plate-actor-in-unreal-engine) documentation for more information.

## 3 - Output Captures from the Unreal Editor

In this process, you'll set up an NDI Media Output object, and use the **Media Captures** panel in the Unreal Editor to output the view from selected cameras in the level to an external NDI playback app like NDI Studio Monitor.

### Steps

1. Right-click in the **Content Drawer**, and select **Media > NDI Media Output**.

   [![Create NDI Media Output](https://dev.epicgames.com/community/api/documentation/image/ccad19e1-8e74-4138-9fa5-105b17b1f067?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ccad19e1-8e74-4138-9fa5-105b17b1f067?resizing_type=fit)
2. Your new asset is named automatically by UE, so rename it something descriptive like  **NDI\_Quick\_Start\_Output**.

   [![Rename NDI Media Output](https://dev.epicgames.com/community/api/documentation/image/395f314f-38b0-447c-ad88-e1c1de0a2e8a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/395f314f-38b0-447c-ad88-e1c1de0a2e8a?resizing_type=fit)
3. Double-click your new Asset to open it up for editing. Your Source Name has a default name defined by UE, so change it to something more specific, like **NDI Quick Start**. This name is how the source is designated in the NDI tools. All the other settings are fine as they are for the purposes of this quick start. Save and close your Media Output when you're done.

   For more information on the NDI Media Output settings, refer to the [NDI Media Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndi-media-reference).

   [![Change NDI Source Name](https://dev.epicgames.com/community/api/documentation/image/6b8ac9ff-1479-4f64-a48e-2698d0b85c16?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6b8ac9ff-1479-4f64-a48e-2698d0b85c16?resizing_type=fit)
4. Now you'll place two cameras in the level, to create viewpoints for the output you'll send to the external NDI playback app. In the Place Actors panel, open the Cinematic tab, and drag two instances of the Cine Camera Actor into the Viewport.

   [![Place Cine Camera actors](https://dev.epicgames.com/community/api/documentation/image/5377626a-86cf-4d70-b8d0-25940448e47f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5377626a-86cf-4d70-b8d0-25940448e47f?resizing_type=fit)

   Place the cameras where you want them in the Level, so that they're showing different viewpoints on the scene.

   Piloting the camera is a fast and easy way to set its viewpoint exactly the way you want it. See [Using Editor Viewports](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine) for more information.
5. From the main menu, select **Window > Virtual Production > Media Capture**. You'll use the **Media Captur**e window to control when the Editor sends output to your NDI external app, and what camera it should use in the level.

   [![Media Capture window](https://dev.epicgames.com/community/api/documentation/image/28145fc1-e5b9-42c9-bbe0-6da2048b0d8f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28145fc1-e5b9-42c9-bbe0-6da2048b0d8f?resizing_type=fit)
6. Under the **Media Viewport Capture** area, find the **Viewport Captures** control. Click the **Add (+)** button to add a new capture to this list.

   [![Add a Viewport Capture](https://dev.epicgames.com/community/api/documentation/image/ef0fc496-0768-4d0a-a32b-9cafa7996fdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef0fc496-0768-4d0a-a32b-9cafa7996fdc?resizing_type=fit)
7. Expand the new entry. First, add the cameras that you want to capture from. In the **Cameras** array, click the **Add (+)** button to add a new entry.

   [![Add a Camera to the array](https://dev.epicgames.com/community/api/documentation/image/e4aa2851-7e2f-413a-bd9f-9ec6d0252dcf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4aa2851-7e2f-413a-bd9f-9ec6d0252dcf?resizing_type=fit)

   Then, use the drop-down list to choose one of the cameras you placed in the level.

   [![Add a Camera actor to the array](https://dev.epicgames.com/community/api/documentation/image/ffebf540-6e8f-41a2-a224-04c91aefdb4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ffebf540-6e8f-41a2-a224-04c91aefdb4e?resizing_type=fit)

   Repeat the same steps to add the other camera to the list.
8. Next, set up the output that you want to capture these cameras to. Set the **Media Output** control to point to the new NDI Media Output Asset that you created above. You can do this by selecting it in the drop-down list, or drag your NDI Media Output Asset from the Content Drawer and drop it into this slot.

   [![Select the Media Output](https://dev.epicgames.com/community/api/documentation/image/5af3ccdc-c544-4f49-bde9-5abcbb79fc50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5af3ccdc-c544-4f49-bde9-5abcbb79fc50?resizing_type=fit)
9. At the top of the window, click the Capture button.

   [![Capture Media button](https://dev.epicgames.com/community/api/documentation/image/0bc06276-0a8c-4ac2-807c-61648c1b4b9d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0bc06276-0a8c-4ac2-807c-61648c1b4b9d?resizing_type=fit)

   You'll see a new frame at the bottom of the window that shows a preview of the output being sent to the external NDI output. If you have your external NDI source connected to another playback app or device, you should start to see the output coming through.

   [![Camera Viewport Capture](https://dev.epicgames.com/community/api/documentation/image/2e6b2551-f1eb-44d3-9369-8775e33f439c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e6b2551-f1eb-44d3-9369-8775e33f439c?resizing_type=fit)
10. Each camera that you added to the Cameras array list for this viewport capture is represented by a corresponding button above the video preview. Click the buttons to switch the capture back and forth between the two views.

    [![Swap viewport captures](https://dev.epicgames.com/community/api/documentation/image/58223fb2-fa12-4d92-a668-0c660cb5a92a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58223fb2-fa12-4d92-a668-0c660cb5a92a?resizing_type=fit)

### End Result

Now you've set up the Unreal Editor to stream output from cameras in your level to an external NDI playback app. Next, you'll explore how to use Blueprint scripting to do the same thing in a running Unreal Engine project.

[![UE output playing in the NDI Studio Monitor app](https://dev.epicgames.com/community/api/documentation/image/471990bb-6c82-497b-95b6-7a272fcb9e55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/471990bb-6c82-497b-95b6-7a272fcb9e55?resizing_type=fit)

## 4 - Output Captures at Runtime

The **Media Capture** window that you used in the last section is a practical and easy way to send captures to an external NDI playback app. However, it only works inside the Unreal Editor. To do the same thing when you're running your project as a standalone application, you'll need to use the Blueprint API provided by the Media Output. In this procedure, we'll set up a simple toggle switch in the level Blueprint that starts and stops capturing when the player presses a key on the keyboard.

The [Virtual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine)
showcase, available on the **Samples** tab of the Epic Games Launcher,
contains a UMG interface widget that demonstrates how you could control
capturing from an on-screen user interface.

### Steps

1. From the main toolbar in the Unreal Editor, choose **Blueprints > Open Level Blueprint**.

   [![Open Level Blueprint](https://dev.epicgames.com/community/api/documentation/image/5e0629b6-1c03-4883-ad16-fef6ac57c472?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e0629b6-1c03-4883-ad16-fef6ac57c472?resizing_type=fit)
2. Start from the NDI Media Output Asset that you've created. In the **Variables** list in the **My Blueprint** panel, click the **Add (+)** button to add a new variable.

   [![Create a new variable](https://dev.epicgames.com/community/api/documentation/image/044645c4-4e01-46ba-adc1-05e1a4235278?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/044645c4-4e01-46ba-adc1-05e1a4235278?resizing_type=fit)
3. In the **Details** panel, set the **Variable Name** to **NDI\_Media\_Output**, and use the **Variable Type** drop-down list to make it an **NDI Media Output Object Reference**.

   [![NDI Media Output Object Reference variable](https://dev.epicgames.com/community/api/documentation/image/c6f480a2-4b4e-4bc0-b81e-e651f45daa52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c6f480a2-4b4e-4bc0-b81e-e651f45daa52?resizing_type=fit)
4. Enable the **Instance Editable** setting (1), and compile the Blueprint. Then, in the **Default Value** section, set the variable to point to the NDI Media Output asset that you created in your Content Drawer (2).

   [![Edit the variable settings](https://dev.epicgames.com/community/api/documentation/image/f6156cb4-b9da-488b-b81c-4b61b784d5b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f6156cb4-b9da-488b-b81c-4b61b784d5b9?resizing_type=fit)
5. Press **Ctrl**, and drag the **NDI\_Media\_Output** from the **Variables** list in the **My Blueprint** panel into the **Event Graph**.

   [![Drag variable on to the Event Graph](https://dev.epicgames.com/community/api/documentation/image/2d5dc31e-68ce-4123-891c-69521da7f834?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d5dc31e-68ce-4123-891c-69521da7f834?resizing_type=fit)
6. Click and drag from the output port of the **NDI\_Media\_Output** variable node, and choose **Media > Output > Create Media Capture**.

   [![Create Media Capture node](https://dev.epicgames.com/community/api/documentation/image/e2d8035e-e902-43b1-8a2c-1dcf9b6c63b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2d8035e-e902-43b1-8a2c-1dcf9b6c63b2?resizing_type=fit)

   Connect your nodes to the **Event BeginPlay** node as shown below:

   [![Connect the Event BeginPlay node](https://dev.epicgames.com/community/api/documentation/image/da481a70-7733-4ca2-94b1-d2ac75410502?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da481a70-7733-4ca2-94b1-d2ac75410502?resizing_type=fit)

   This creates a new Media Capture object from your NDI Media Output. The Media Capture offers two main Blueprint functions that you'll use to control the capturing: **Capture Active Scene Viewport** and **Stop Capture**.
7. First, save the new Media Capture object into its own variable, so you can access it again elsewhere. Click and drag from the output port of the **Create Media Capture** node, and choose **Promote to Variable**.

   [![Promote to variable](https://dev.epicgames.com/community/api/documentation/image/4855214a-0cdb-4b83-bbb9-a8384305dfd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4855214a-0cdb-4b83-bbb9-a8384305dfd3?resizing_type=fit)

   Rename the new variable **Media\_Capture** in the Variables list in the My Blueprint panel.

   [![Rename the variable](https://dev.epicgames.com/community/api/documentation/image/aa1d0b0f-1098-4bac-8f58-de83790b31b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa1d0b0f-1098-4bac-8f58-de83790b31b8?resizing_type=fit)

   It's important to save the Media Capture to a variable here. If you don't, the Unreal Engine's garbage collector may destroy it automatically before you're done with it.
8. Press **Ctrl** and drag the **Media\_Capture** variable into the **Event Graph**.

   [![Drag Media_Capture variable into the Event Graph](https://dev.epicgames.com/community/api/documentation/image/7a13b38c-a7a7-43a7-9976-8a34af00d3fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a13b38c-a7a7-43a7-9976-8a34af00d3fa?resizing_type=fit)
9. Click and drag from the output port of the **Media\_Capture** variable node, and choose **Media > Output > Capture Active Scene Viewport**. Do it again, and choose **Media > Output > Stop Capture**.

   [![Create Media Output control options](https://dev.epicgames.com/community/api/documentation/image/446a9a72-938f-4cd8-b979-fed9dfadb1de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/446a9a72-938f-4cd8-b979-fed9dfadb1de?resizing_type=fit)
10. Right-click in the **Event Graph** and choose **Input > Keyboard Events > P**.   Click and drag from the **Pressed** output of the **P** node and choose **Flow Control > Flip Flop**.

    [![Create Keyboard Input P and Flip Flop nodes](https://dev.epicgames.com/community/api/documentation/image/8543276d-6a37-4e2e-8d1e-70369ecb98a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8543276d-6a37-4e2e-8d1e-70369ecb98a7?resizing_type=fit)
11. Connect the **A** output of the **Flip Flop** node to the input event of the **Capture Active Scene Viewport** node, and connect the **B** output of the **Flip Flop** node to the input event of the **Stop Capture** node, as shown below:

    [![Connect the Flip Flop node to the Media Output nodes](https://dev.epicgames.com/community/api/documentation/image/4c65f986-6c53-44de-94fe-933fc26afdcb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4c65f986-6c53-44de-94fe-933fc26afdcb?resizing_type=fit)
12. Compile and save the Blueprint, and try playing your Project. Click the arrow next to the Play button in the main Toolbar, and choose either the **New Editor Window (PIE)** or **Standalone Game** option.

    [![Select Play mode](https://dev.epicgames.com/community/api/documentation/image/502e4a03-8733-4f9b-baf6-fa7d746aadee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/502e4a03-8733-4f9b-baf6-fa7d746aadee?resizing_type=fit)

    Video capture from the Editor will only work when you play your Project in a New Editor Window (PIE) or a Standalone Game. It won't work in the default Selected Viewport mode, or in Simulate mode. In addition, the viewport resolution of your project (that is, the size of the rendered image the Unreal Engine generates each frame) must match the output resolution set in the active Media Profile, so that it will be the right size for the output video feed.

    After your project starts up, you should be able to press the P button on your keyboard to toggle sending the output from the engine to the external NDI app.

### End Result

At this point, you should have a basic idea of how to work with NDI Media Source assets, NDI Media Output assets, and the Media Capture system, and you should understand how all of these elements work together to send and receive video using NDI and Unreal Engine.

## On Your Own

Now that you've seen the basics of how to get a new Project exchanging video input and output with NDI tools, you can continue learning on your own:

* Explore the [Virtual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine) showcase to see what it adds to this basic setup, like its on-screen UI that switches cameras and controls video capture at runtime.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1 - Set Up the Project](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#1-setuptheproject)
* [Steps](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#endresult)
* [2 - Rendering Video Input in Unreal Engine](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#2-renderingvideoinputinunrealengine)
* [Steps](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#steps-2)
* [End Result](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#endresult-2)
* [3 - Output Captures from the Unreal Editor](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#3-outputcapturesfromtheunrealeditor)
* [Steps](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#steps-3)
* [End Result](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#endresult-3)
* [4 - Output Captures at Runtime](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#4-outputcapturesatruntime)
* [Steps](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#steps-4)
* [End Result](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#endresult-4)
* [On Your Own](/documentation/en-us/unreal-engine/ndi-video-io-quick-start-for-unreal-engine?application_version=5.7#onyourown)
