<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7 -->

# AJA Video I/O Quick Start

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
8. AJA Video I/O Quick Start

# AJA Video I/O Quick Start

A step-by-step guide to getting video from a supported AJA media card into the Unreal Engine, and sending captured video output from the Unreal Engine out to a port on the AJA card.

![AJA Video I/O Quick Start](https://dev.epicgames.com/community/api/documentation/image/210c9349-eec5-4d37-a3dd-d47db70a7c68?resizing_type=fill&width=1920&height=335)

 On this page

In this Quick Start guide, we walk through the process of setting up an Unreal Engine Project to work with a professional video card from AJA Video Systems. At the end of this guide:

* You'll have video input from your AJA card playing inside your Unreal Engine Project.
* You'll be able to capture camera viewpoints both from the Editor and from your runtime application, and send them out to an SDI port on your AJA card.
* You'll know where to go when you want to set up more advanced adjustments to your video inputs, such as correcting lens deformation and applying chroma-keying effects.

For a working example that shows many of the elements described below put into practice, see the **[Virtual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine)** showcase, available on the Samples tab of the Epic Games Launcher.

**Prerequisites:**

* Make sure that you have a supported card from AJA Video Systems, and that you've installed the necessary drivers and software. For details, see the [AJA Media Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/aja-media-reference-for-unreal-engine) page.
* Make sure that your card is working correctly, and that you have some video input feeding in to at least one of the card's SDI ports.
* Open an Unreal Engine Project that you want to integrate with your video feeds. This page shows the steps in the **Third Person** Blueprint template, but the same steps will work equally well in any Project.

The AJA Media components used in this guide are built on top of the [Media Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-in-unreal-engine), and we'll use [Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) to script the video capturing process at runtime. Some prior knowledge of these topics is recommended but not required.

## 1 - Set Up the Project

Before you can get video input from your AJA card into your Unreal Engine Level, and send output from Unreal Engine through one of your AJA card's SDI ports, you'll need to do some basic setup to enable the AJA Media Player Plugin in your Project.

If you started your Unreal Engine Project from one of the Templates in the **Film, Television, and Live Events** category, the necessary plugins may already be enabled for you. If not, follow the instructions below to enable them.

### Steps

1. Open the Project that you want to use with AJA video I/O in the Unreal Editor.
2. From the main menu, select **Edit > Plugins**.
3. In the **Plugins** window, find the **AJA Media Player** plugin under the **Media Players** category. Check its **Enabled** checkbox.

   [![Enable the AJA Media Player Plugin](https://dev.epicgames.com/community/api/documentation/image/a50f1a94-c3a8-4e98-b4c2-124b49fdd578?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a50f1a94-c3a8-4e98-b4c2-124b49fdd578?resizing_type=fit)

   Click image to expand.
4. Find the **Media Framework Utilities** Plugin under the **Media Players** category. Check its **Enabled** checkbox, if it's not already checked.

   [![Enable the Media Framework Utilities Plugin](https://dev.epicgames.com/community/api/documentation/image/1d0b73f0-214a-4008-98ee-679d84494776?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d0b73f0-214a-4008-98ee-679d84494776?resizing_type=fit)

   Click image to expand.
5. Click **Restart Now** to restart Unreal Engine and reopen your Project.

   [![Restart Now](https://dev.epicgames.com/community/api/documentation/image/bb1047df-2ce7-4817-b9b1-bc095deb14f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb1047df-2ce7-4817-b9b1-bc095deb14f8?resizing_type=fit)

   Click image to expand.

### End Result

Your Project is now ready to accept video from the AJA card, and to send rendered output to the card. In the next sections, we'll hook it up and start playing video in and out.

## 2 - Rendering Video Input in Unreal Engine

In this process, we'll make video input from the AJA card visible in the current Level in the Unreal Editor. This process uses a Media Bundle: a kind of Asset that packages together several different types of Assets involved in the Media Framework, and that offers you control over some advanced features like lens deformation, chroma-keying, color correction, and more.

### Steps

1. In your **Content Browser**, expand the **Sources** panel. Right-click, and choose **New Folder** from the context menu.

   Rename your new folder **AJA**.
2. Open your new folder, right-click in the **Content Browser** and choose **Media > Media Bundle**.

   [![New Media Bundle](https://dev.epicgames.com/community/api/documentation/image/0e39c0ea-3929-4760-b881-fa60059c9370?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e39c0ea-3929-4760-b881-fa60059c9370?resizing_type=fit)
3. Your new Asset's name is automatically selected in the Content Browser, so you can give it a descriptive name:

   [![Name the Media Bundle](https://dev.epicgames.com/community/api/documentation/image/72efd539-5cdc-48fa-80a1-d3fdd9fd0965?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/72efd539-5cdc-48fa-80a1-d3fdd9fd0965?resizing_type=fit)

   Type a new name, like **AjaMediaBundle**, and press **Enter**. A new folder of Media Framework Assets is automatically created next to your Media Bundle, named with the suffix **\_InnerAssets**.
4. Save your new Assets by clicking the **Save All** button in the **Content Browser**.

   [![Save All Assets](https://dev.epicgames.com/community/api/documentation/image/7e756fda-cc13-466d-b4ad-f6da1e209d82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e756fda-cc13-466d-b4ad-f6da1e209d82?resizing_type=fit)
5. Double-click your new Media Bundle to edit its properties. The Media Bundle is capable of playing video from any kind of media source the Engine supports, so you'll need to tell it that you want to get the video from your AJA card.

   In the **Media Source** property, select **Aja Media Source** from the drop-down list:

   [![Set the AJA Media Source](https://dev.epicgames.com/community/api/documentation/image/adb8eb9d-2078-4add-ab6d-7d421b12f0b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/adb8eb9d-2078-4add-ab6d-7d421b12f0b5?resizing_type=fit)

   Click image to expand.
6. Once you've identified the type of Media Source you want the Media Bundle to handle, you can then set up any configuration properties offered by that type of source.

   You can make Unreal Engine automatically match the format and framerate of the incoming video signal. To enable automatic format detection, click the **Configuration** dropdown, enable **Auto**, and then click **Apply**. The engine now seamlessly handles changes and restarts automatically if the signal is temporarily lost.

   [![Aja Media Source Configuration](https://dev.epicgames.com/community/api/documentation/image/449f9cb7-405e-4bd3-916b-8cd8feeacdf4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/449f9cb7-405e-4bd3-916b-8cd8feeacdf4?resizing_type=fit)

   Click image to expand.

   The options you see may vary depending on the devices you have installed. For details on all of the properties you can set for an AJA Media Source, see the [AJA Media Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/aja-media-reference-for-unreal-engine) page.
7. If you want to apply any compensation to the incoming video to account for lens distortion, you can set up the physical properties of the lens in the **Lens Parameters** section.

   [![Lens undistortion parameters](https://dev.epicgames.com/community/api/documentation/image/cdabd23c-fb62-48ea-a28b-dfaf2827a69b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cdabd23c-fb62-48ea-a28b-dfaf2827a69b?resizing_type=fit)

   Click image to expand.

   These **Lens Parameters** just set up the physical properties of the lens. You'll actually activate the lens compensation later, when you edit the Material Instance used by the Media Bundle.
   Save your Media Bundle when you're done setting up its properties, and return to the **AJA** folder in the Content Browser.
8. Drag your **AjaMediaBundle** Asset from the Content Browser into the Level Viewport.

   [![Drag and drop the Media Bundle](https://dev.epicgames.com/community/api/documentation/image/fb755f15-e094-4831-9ba9-ca0e25dadfc1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb755f15-e094-4831-9ba9-ca0e25dadfc1?resizing_type=fit)

   Click image to expand.

   You'll see a new plane appear, showing the video currently being played over the port configured for your Media Bundle. Use the transform tools in the Viewport toolbar to move, rotate, and resize it.
   If your Media Bundle doesn't start playing automatically, select it, then click the **Media Bundle > Request Play Media** button in the **Details** panel.

   [![Request Play Media](https://dev.epicgames.com/community/api/documentation/image/a239b22a-8650-4729-b576-59009b359b62?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a239b22a-8650-4729-b576-59009b359b62?resizing_type=fit)
9. Now, we'll see how to apply keying and compositing effects to the video stream.
   Back in the Media Bundle Editor, click the **Open Material Editor** button in the Toolbar to edit the Material Instance that this Media Bundle uses to draw its incoming video feed on to an object in the Level.

   [![Open Material Editor](https://dev.epicgames.com/community/api/documentation/image/1558f058-f8df-4ffa-ad59-dd8521ab1703?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1558f058-f8df-4ffa-ad59-dd8521ab1703?resizing_type=fit)

   This Material Instance is saved inside the **AjaMediaBundle\_InnerAssets** folder that was created automatically with your Media Bundle.

   [![Material Instance](https://dev.epicgames.com/community/api/documentation/image/41708217-9d17-441a-be83-32ec120e9a24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41708217-9d17-441a-be83-32ec120e9a24?resizing_type=fit)

   Click image to expand.
10. In the Material Instance Editor, you'll see a number of properties exposed for you to configure keying, cropping, and color correction, and to activate the correction for the lens distortion that you set up in the Media Bundle.

    [![Material Instance Editor](https://dev.epicgames.com/community/api/documentation/image/0d8cd090-56ac-4150-9002-5047b192939b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d8cd090-56ac-4150-9002-5047b192939b?resizing_type=fit)

    Click image to expand.

    While you adjust the settings in the Material Instance Editor, you can see the effect of your changes on the video feed playing back in the main Level Viewport.

    You may find it more convenient to see the effects of the changes you
    make in the preview panel of the Material Instance Editor instead. To do
    this, temporarily enable the **IsValid** setting, and set its value to `1.0`.

    [![IsValid](https://dev.epicgames.com/community/api/documentation/image/db0ca801-6a98-4b29-af46-79ab8e4ab553?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db0ca801-6a98-4b29-af46-79ab8e4ab553?resizing_type=fit)

    Click the arrow at the top left of the Viewport toolbar, and enable the **Realtime** option in the menu.

    [![Realtime Viewport](https://dev.epicgames.com/community/api/documentation/image/f0d189d3-0cec-441d-878a-3258f7fad6ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0d189d3-0cec-441d-878a-3258f7fad6ad?resizing_type=fit)

    You'll be able to judge the effect of your changes more easily by changing the preview mesh to a plane or a cube. Use the controls at the bottom of the Viewport:

    [![Preview mesh](https://dev.epicgames.com/community/api/documentation/image/77e25cc4-7319-4fe3-91de-e7acdba06584?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/77e25cc4-7319-4fe3-91de-e7acdba06584?resizing_type=fit)

    When you're done, return the **IsValid** setting to its previous value.
11. When you're done changing the Material Instance properties, click the **Save** button in the Toolbar.

### End Result

At this point, you should have video playing over an SDI port showing up inside your Unreal Engine Level, and you should understand where to set up more advanced features like lens deformation and chroma-keying.

If you're already familiar with the Media Framework, another way you could get video into your Level is to create a new **AjaMediaSource** Asset in your Project, and set it up with the same source properties you set up inside the Media Bundle in the procedure above. Then, create your own **MediaPlayer** and **MediaTexture** Assets to handle the playback of that source in your Level. For details, see the [Media Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-in-unreal-engine) documentation. However, we recommend using the Media Bundle, as shown above, to get the best balance between ease of use and professional quality video features.

## 3 - Output Captures from the Unreal Editor

In this process, you'll set up an AJA Media Output object, and use the **Media Captures** panel in the Unreal Editor to output the view from selected cameras in the Level to your AJA card.

### Steps

1. Right-click in the Content Browser, and select **Media > Aja Media Output**.

   [![New AJA Media Output](https://dev.epicgames.com/community/api/documentation/image/32394d47-8e28-4aa8-ab82-783af558edde?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32394d47-8e28-4aa8-ab82-783af558edde?resizing_type=fit)

   Click image to expand.

   Name your new Asset **AjaMediaOutput**.
2. Double-click your new Asset to open it up for editing. Just like when you created your Aja Media Source, you have to set up the **Configuration** property to control the properties of the video feed that the Unreal Engine sends to your AJA card. Click the arrow to open the submenu, select the options that match your video setup, then click **Apply** in the submenu.

   [![Aja Media Output Configuration](https://dev.epicgames.com/community/api/documentation/image/9e8ca7fe-99f8-4a76-a91b-fe645e1401e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e8ca7fe-99f8-4a76-a91b-fe645e1401e3?resizing_type=fit)

   Click image to expand.

   For details on all of the properties you can set in the AJA Media Output, see the [AJA Media Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/aja-media-reference-for-unreal-engine) page. Save and close your Media Output when you're done.
3. Now we'll place two cameras in the Level, to give us viewpoints for the output we'll send to the AJA card. In the **Place Actors** panel, open the **Cinematic** tab, and drag two instances of the **Cine Camera Actor** into the Viewport.

   [![Drag and drop Cine Camera Actors](https://dev.epicgames.com/community/api/documentation/image/8faad695-6856-4987-a67d-654f9e82ad46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8faad695-6856-4987-a67d-654f9e82ad46?resizing_type=fit)

   Place the cameras where you want them in the Level, so that they're showing different viewpoints on the scene.

   **Piloting** the camera is a fast and easy way to set its viewpoint exactly the way you want it. See [Pilot Actors in the Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine).
4. From the main menu, choose **Window > Virtual Production > Media Capture**. You'll use the **Media Capture** window to control when the Editor sends output to your AJA port, and what camera it should use in the Level.

   [![Media Capture window](https://dev.epicgames.com/community/api/documentation/image/1d42d82b-e384-485e-bc96-490740e91b80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d42d82b-e384-485e-bc96-490740e91b80?resizing_type=fit)
5. Under the **Media Viewport Capture** area, find the **Viewport Captures** control. Click the **Add (+)** button to add a new capture to this list.

   [![Add a viewport capture](https://dev.epicgames.com/community/api/documentation/image/73db1df1-8544-4b92-8eb3-0b20cafc7128?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/73db1df1-8544-4b92-8eb3-0b20cafc7128?resizing_type=fit)
6. Expand the new entry. First, we'll add the cameras that we want to capture from. In the **Locked Camera Actors** control, click the **Add (+)** button to add a new entry.

   [![Add a camera actor](https://dev.epicgames.com/community/api/documentation/image/07988d6a-9cb4-4310-af48-387e220862bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07988d6a-9cb4-4310-af48-387e220862bc?resizing_type=fit)

   Then, use the drop-down list to choose one of the cameras you placed in the Level.

   [![Select the camera actor](https://dev.epicgames.com/community/api/documentation/image/2da498ea-219d-4547-aa6a-d46f63118b5d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2da498ea-219d-4547-aa6a-d46f63118b5d?resizing_type=fit)

   Repeat the same steps to add the other camera to the list.
7. Now, set up the output that you want to capture these cameras to. Set the **Media Output** control to point to the new AJA Media Output Asset that you created above. You can do this by selecting it in the drop-down list, or drag your AJA Media Output Asset from the Content Browser and drop it into this slot.

   [![Set the AJA Media Output](https://dev.epicgames.com/community/api/documentation/image/86de142a-3197-41fe-ba3b-7e04dbe38843?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86de142a-3197-41fe-ba3b-7e04dbe38843?resizing_type=fit)
8. At the top of the window, click the **Capture** button.

   [![Start capturing](https://dev.epicgames.com/community/api/documentation/image/9e69efc3-e5eb-4f65-99ff-f2b28e68a972?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e69efc3-e5eb-4f65-99ff-f2b28e68a972?resizing_type=fit)

   You'll see a new frame at the bottom of the window that shows a preview of the output being sent to the AJA card. If you have this port hooked up to another downstream device, you should start to see the output coming through.

   [![Active Media Capture](https://dev.epicgames.com/community/api/documentation/image/5885568e-7b55-47b2-913d-d73620c7410f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5885568e-7b55-47b2-913d-d73620c7410f?resizing_type=fit)
9. Each camera that you added to the Locked Camera Actors list for this viewport capture is represented by a corresponding button above the video preview. Click the buttons to switch the capture back and forth between the two views.

   [![Switch Cameras](https://dev.epicgames.com/community/api/documentation/image/c2498f7a-4e62-448c-864b-7309b55d74c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2498f7a-4e62-448c-864b-7309b55d74c3?resizing_type=fit)

   Click image to expand.

### End Result

Now you've set up the Unreal Editor to stream output from cameras in your Level to a port on your AJA card. Next, we'll see how to use Blueprint scripting to do the same thing in a running Unreal Engine Project.

## 4 - Output Captures at Runtime

The **Media Capture** window that you used in the last section is a practical and easy way to send captures to the AJA card. However, it only works inside the Unreal Editor. To do the same thing when you're running your Project as a standalone application, you'll need to use the Blueprint API provided by the Media Output. In this procedure, we'll set up a simple toggle switch in the Level Blueprint that starts and stops capturing when the player presses a key on the keyboard.

The **[Virtual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine)** showcase, available on the **Samples** tab of the Epic Games Launcher, contains a UMG interface widget that demonstrates how you could control capturing from an on-screen user interface.

### Steps

1. From the main toolbar in the Unreal Editor, choose **Blueprints > Open Level Blueprint**.

   [![Open Level Blueprint](https://dev.epicgames.com/community/api/documentation/image/b8989705-87e4-4442-93f3-0331bad5e796?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8989705-87e4-4442-93f3-0331bad5e796?resizing_type=fit)
2. We'll need to start from the AJA Media Output Asset that you've created, where you identify the port you want to output to. In the **Variables** list in the **My Blueprint** panel, click the **Add (+)** button to add a new variable.

   [![New Variable](https://dev.epicgames.com/community/api/documentation/image/b1e8c4ae-9508-4392-a1be-130ea8295f24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1e8c4ae-9508-4392-a1be-130ea8295f24?resizing_type=fit)
3. In the **Details** panel, set the **Variable Name** to **AjaMediaOutput**, and use the **Variable Type** drop-down list to make it an **Aja Media Output Object Reference**.

   [![Aja Media Output Object Reference](https://dev.epicgames.com/community/api/documentation/image/20708e7c-f1c9-46ad-a992-f37836825154?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20708e7c-f1c9-46ad-a992-f37836825154?resizing_type=fit)
4. Enable the **Instance Editable** setting (1), and compile the Blueprint. Then, in the **Default Value** section, set the variable to point to the AJA Media Output Asset that you created in your Content Browser (2).

   [![Set the default value](https://dev.epicgames.com/community/api/documentation/image/21f96ce6-8865-4ec0-9298-8f0409a4be28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21f96ce6-8865-4ec0-9298-8f0409a4be28?resizing_type=fit)
5. Press **Ctrl**, and drag the **AjaMediaOutput** from the Variables list in the **My Blueprint** panel into the **Event Graph**.

   [![Control+drag the AjaMediaOutput](https://dev.epicgames.com/community/api/documentation/image/903c7e23-be15-435c-936b-dcce27de32b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/903c7e23-be15-435c-936b-dcce27de32b7?resizing_type=fit)
6. Click and drag from the output port of the **AjaMediaOutput** variable node, and choose **Media > Output > Create Media Capture**.

   [![Create Media Capture](https://dev.epicgames.com/community/api/documentation/image/aaec8cfc-e948-4af2-8092-129c360ff0a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaec8cfc-e948-4af2-8092-129c360ff0a8?resizing_type=fit)

   Hook up your nodes to the **Event BeginPlay** node as shown below:

   [![Event Begin Play](https://dev.epicgames.com/community/api/documentation/image/7e822386-af23-484b-9139-9f13c20cb8a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e822386-af23-484b-9139-9f13c20cb8a7?resizing_type=fit)

   This creates a new Media Capture object from your Aja Media Output. The Media Capture offers two main Blueprint functions that we'll use to control the capturing: **Capture Active Scene Viewport** and **Stop Capture**.
7. First, we'll save the new Media Capture object into its own variable, so we can get access to it again elsewhere. Click and drag from the output port of the **Create Media Capture** node, and choose **Promote to Variable**.

   [![Promote to variable](https://dev.epicgames.com/community/api/documentation/image/c5e545c6-5b7d-4907-a18a-302405b7b389?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5e545c6-5b7d-4907-a18a-302405b7b389?resizing_type=fit)

   Rename the new variable **MediaCapture** in the Variables list in the **My Blueprint** panel.

   It's important to save the Media Capture to a variable here. If you don't, the Unreal Engine's garbage collector may destroy it automatically before you're done with it.
8. Press **Ctrl** and drag the **MediaCapture** variable into the **Event Graph**.

   [![Control+drag the MediaCapture](https://dev.epicgames.com/community/api/documentation/image/7b853a55-b2a4-4c34-a1e7-d61d38c15027?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b853a55-b2a4-4c34-a1e7-d61d38c15027?resizing_type=fit)
9. Click and drag from the output port of the **MediaCapture** variable node, and choose **Media > Output > Capture Active Scene Viewport**. Do it again, and choose **Media > Output > Stop Capture**.

   [![Start and stop the capture](https://dev.epicgames.com/community/api/documentation/image/56d002cb-f60d-4904-aa4b-6dc63b92e6a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56d002cb-f60d-4904-aa4b-6dc63b92e6a2?resizing_type=fit)
10. Right-click in the **Event Graph** and choose **Input > Keyboard Events > P**.   Click and drag from the **Pressed** output of the **P** node and choose **Flow Control > FlipFlop**.

    [![FlipFlop](https://dev.epicgames.com/community/api/documentation/image/8d65a520-617d-4358-9412-5494635d30a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d65a520-617d-4358-9412-5494635d30a7?resizing_type=fit)
11. Connect the **A** output of the **FlipFlop** node to the input event of the **Capture Active Scene Viewport** node, and connect the **B** output of the **FlipFlop** node to the input event of the **Stop Capture** node, as shown below:

    [![Connect the nodes](https://dev.epicgames.com/community/api/documentation/image/7bef2ba2-9b2d-47ff-a589-9a9dcdcf21fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7bef2ba2-9b2d-47ff-a589-9a9dcdcf21fc?resizing_type=fit)
12. Compile and save the Blueprint, and try playing your Project. Click the
    arrow next to the Play button in the main Toolbar, and choose either the
    **New Editor Window (PIE)** or **Standalone Game** option.

    [![Launch the Project](https://dev.epicgames.com/community/api/documentation/image/24b48198-1db5-4e2d-9910-3e7b4964b665?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24b48198-1db5-4e2d-9910-3e7b4964b665?resizing_type=fit)

Video capture from the Editor will only work when you play your Project in a **New Editor Window (PIE)** or a **Standalone Game**. It won't work in the default **Selected Viewport** mode, or in **Simulate** mode.
In addition, the viewport resolution of your Project (that is, the size of the rendered image the Unreal Engine generates each frame) must match the output resolution set in the active Media Profile, so that it will be the right size for the output video feed.

After your project starts up, you should be able to press the **P** button on your keyboard to toggle sending the output from the Engine to the AJA card.

### End Result

At this point, you should have a basic idea of how to work with Aja Media Sources, Media Bundles, and the Media Capture system, and you should understand how all of these elements work together to get professional video in and out of the Unreal Engine.

## On Your Own

Now that you've seen the basics of how to get a new Project exchanging video input and output with an AJA card, you can continue learning on your own:

* Explore the in-engine keying solution in the Material Instance created by your Media Bundle. Try passing some green-screen video into your card's input port, and use the keying controls in the Material Instance to remove the background.
* Explore the **[Virtual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine)** showcase to see what it adds to this basic setup, like its on-screen UI that switches cameras and controls video capture at runtime.

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [professional video](https://dev.epicgames.com/community/search?query=professional%20video)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1 - Set Up the Project](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#1-set-up-the-project)
* [Steps](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#end-result)
* [2 - Rendering Video Input in Unreal Engine](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#2-rendering-video-input-in-the-unreal-engine)
* [Steps](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#end-result)
* [3 - Output Captures from the Unreal Editor](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#3-output-captures-from-the-unreal-editor)
* [Steps](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#end-result)
* [4 - Output Captures at Runtime](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#4-output-captures-at-runtime)
* [Steps](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#end-result)
* [On Your Own](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine?application_version=5.7#on-your-own)
