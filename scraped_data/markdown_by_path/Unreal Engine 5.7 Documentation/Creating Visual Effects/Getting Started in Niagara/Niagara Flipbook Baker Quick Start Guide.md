<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7 -->

# Niagara Flipbook Baker Quick Start Guide

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
6. [Getting Started in Niagara](/documentation/en-us/unreal-engine/getting-started-in-niagara-effects-for-unreal-engine "Getting Started in Niagara")
7. Niagara Flipbook Baker Quick Start Guide

# Niagara Flipbook Baker Quick Start Guide

A quick start guide for creating Niagara flipbooks in Unreal Engine.

![Niagara Flipbook Baker Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/b45676ae-9bd1-4f4c-927a-bcf25937a8cb?resizing_type=fill&width=1920&height=335)

 On this page

**Niagara systems** create visually stunning effects. However, when designing simulations it's important to balance the visual look with the performance. At times, you may create a nice effect, but find it takes up too much memory to use on a target device.

One solution to this is to bake out the Niagara simulation to a **flipbook**. This creates a tiled image that can then be loaded onto any material.

For example, you want to create a 3D fluid effect, but you are not able to run it in realtime on your target platform. So, after creating the 3D fluid effect, you can use the **Baker** to bake it to a flipbook, and then apply this back to a 2D sprite emitter. This way, you have very efficient performance for games or for non-hero effects that may be farther in the background.

## Goals

In this tutorial, use the Niagara Baker to export a flipbook from a simulation.

## Objectives

* Set up the capture for the flipbook
* Perform the capture
* Connect the flipbook to a new emitter

## Set Up the Capture

1. Open an existing Niagara system in the **Niagara Editor**. In this example, the **Grid 3D Gas Colored Smoke** example is used, however you can use any Niagara system. To use Grid 3D Gas Colored Smoke, right-click in the **Content Drawer** and select **Create Basic Asset > Niagara System**.

   ![Creating a new Niagara system.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32d5f8e8-934e-4737-9558-a66c24238278/niagara-flipbook-baker-1.png)
2. Create a flipbook from a Niagara Fluids template. These templates are available when you have the Niagara Fluids plugin enabled. However, a flipbook can be generated from any Niagara system. Select **Niagara Fluids > 3D Gas** from the left menu, then select **Grid 3D Gas Colored Smoke** and click **Create**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f232eca-072c-4c6f-850f-a5ff58eb1cc6/niagara-flipbook-baker-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f232eca-072c-4c6f-850f-a5ff58eb1cc6/niagara-flipbook-baker-2.png)

   Click image for full size.
3. On the **main toolbar**, there is a new button called **Baker**. Select **Open Baker Tab** to display the **Baker panel**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dacc0e0f-62a0-41a5-ae3f-48c1fd1dfa4a/baker-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dacc0e0f-62a0-41a5-ae3f-48c1fd1dfa4a/baker-button.png)

   Click image for full size.

### Navigating the User Interface

The Baker panel user interface has the following parts.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cff291bb-1c10-41d2-81b2-af8698a1db30/baker-panel-ui.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cff291bb-1c10-41d2-81b2-af8698a1db30/baker-panel-ui.png)

Click image for full size.

1. Bake button
2. Niagara Preview
3. Flipbook Preview
4. Playback Toolbar
5. Flipbook Options

### Frame the Niagara Preview

To get started, you need to frame the simulation within the **Niagara Preview** window. It will bake out the simulation to a series of flat, 2D frames, so make sure that you set up the desired angle and size.

To adjust the framing, you can click and drag directly in the Niagara Preview window.

* Left-click and drag to orbit.
* Middle-click and drag to pan.
* Right-click and drag to zoom.
* Click **F** to center the frame on the system origin.

You can also enter the values numerically in the **Camera** settings. Select the **Camera Viewport Mode** as desired, then edit the numerical values in the corresponding field.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8e1bd30-93f6-48a7-94ad-c07ea35dc0f2/camera-viewport-mode-perspective.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8e1bd30-93f6-48a7-94ad-c07ea35dc0f2/camera-viewport-mode-perspective.png)

Click image for full size.

### Adjust the Timing

Use the **Playback Toolbar** to play, pause, step forward, and step backward in the simulation to preview what will be baked out.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c70ffa80-1f80-4afb-8070-5afac78db1b6/playback-toolbar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c70ffa80-1f80-4afb-8070-5afac78db1b6/playback-toolbar.png)

Click image for full size.

You can also adjust the timing in the **Timeline** settings, so that you only bake out a portion of the simulation. For example, adjust **Start Seconds** to start the flipbook partway through the simulation playback. Adjust **Duration Seconds** to change when it will end.

Set the **Frames Per Second** to adjust the tick rate of the component. You usually should not need to adjust this value. Set it to the same value as for the content you author. The Niagara System Editor defaults to 30 fps. Setting this value too low can result in the same flipbook frame being rendered multiple times, for example if you were to render a flipbook over 1 second with 30 frames captured and you set the Frames Per Second to 20 you would only record 20 unique frames rather than 30.

### Adjust the Texture Size

The way the flipbook bakes, it will export a tiled image where each tile represents a frame of the flipbook. You need to set how many tiles you want to map onto the texture, as well as the total texture size. By default, the texture is set up with 8 tiles along the X axis, 8 tiles along the Y axis, and a total texture size of 1024 x 1024 pixels.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68033155-baf3-4a36-92ac-c6a718fe89ed/flipbook-tiling.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68033155-baf3-4a36-92ac-c6a718fe89ed/flipbook-tiling.png)

Click image for full size.

That means that each tile will be a size of 128 x 128 pixels. You can adjust these values under the **Texture** settings.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78b17519-2cb6-4f88-820d-55194cdc9d7b/setting-tiling-frames-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78b17519-2cb6-4f88-820d-55194cdc9d7b/setting-tiling-frames-size.png)

Click image for full size.

Set the number of tiles by adjusting **Frames Per Dimension**. Adjust the size of the overall texture by changing **Texture Size**.

The baker does not scale your tiles to fit into the final resolution. For an ideal result, make sure that the number of tiles divides evenly into the overall texture size.

For example, if you set Frames Per Dimension to be 10 x 10, but kept the Texture Size at 1024 x 1024, then the system would try to map 10 tiles into 1024. However, that would result in each tile being 102.4 pixels wide, and the system cannot account for a partial pixel. Therefore, it would map each tile to a size of 102, and you would end up with 4 extra pixels of padding at the right and bottom of your texture.

This can cause the sub UV mapping to be slightly off, and cause your atlas to jitter as it plays. For ideal behavior, set your Texture Size to be a power of 2, and the Frames Per Dimension to be a number that divides evenly into that texture size.

### Set Additional Texture Properties

By default, when **Source Binding** is set to **None**, the Baker will output the **SceneColorHDR** values. Usually, this is the desired outcome. However, all available GBuffers and particle attributes are available, and you can choose from any of them from the dropdown menu for Source Binding.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/835c3841-ce14-4ea6-82f9-d5a1cbea5b91/source-binding.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/835c3841-ce14-4ea6-82f9-d5a1cbea5b91/source-binding.png)

Click image for full size.

Before you generate your first flipbook, the **Generated Texture** is set to None. After you perform your first capture, this is replaced by the new texture that you create.

## Perform a Capture

Now that you have set up the texture to look the way you want, with the correct framing and timing, you can perform a capture.

1. From the Niagara Preview window, click **Bake**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a9c9eae-636d-4349-822e-ef94915c9ef2/bake.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a9c9eae-636d-4349-822e-ef94915c9ef2/bake.png)

   Click image for full size.
2. You now see a progress bar as the system renders out the flipbook. When complete, a dialog opens and you can name your texture file.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a96aa56e-42d1-4d76-978d-63918f4a573b/name-texture.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a96aa56e-42d1-4d76-978d-63918f4a573b/name-texture.png)

   Click image for full size.
3. Now that it has rendered out, your new texture replaces the active texture in the Texture settings of the Baker window.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1cad10e8-9d48-4db7-bbef-7c204651d793/generated-texture.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1cad10e8-9d48-4db7-bbef-7c204651d793/generated-texture.png)

   Click image for full size.

   If you generate another capture, with this texture selected under **Generated Texture**, it will overwrite this texture.
4. If you would like to generate a new variation of the texture, click the dropdown for the **Generated Texture**, then select **Clear**. You can then adjust any of the settings and create a new texture.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e16229a6-715d-4a39-9c6a-f33e6059f144/clear-generated-texture.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e16229a6-715d-4a39-9c6a-f33e6059f144/clear-generated-texture.png)

   Click image for full size.

Now that you exported the texture, you can add it into any new emitter. You can also see the final preview of what the flipbook texture looks like.

![Comparing the baked flipbook with the live Niagara system.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f950b0ff-f6b7-49af-8779-264766e7f42d/flipbook-comparison.gif)

## Use the Flipbook Texture in an Emitter

To use the flipbook in an emitter, you must use a **Sprite Renderer**.

1. To set this up, right-click in the **Content Drawer** and create a new **Niagara System**.
2. Select **New system from selected emitter(s)**, and then **Simple Sprite Burst**.
3. Click **plus (+)** to add the emitter, then click **Finish**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31029713-fe73-4674-befb-25a09fb7ce92/simple-sprite-burst.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31029713-fe73-4674-befb-25a09fb7ce92/simple-sprite-burst.png)

Click image for full size.

### Add the Sub UV Animation Module

To add in your flipbook, you need to add a new module in the Particle Update group, as well as adjust some parameters on the Sprite Renderer.

1. First, click **plus (+)** next to **Particle Update**, and select **Sub UVAnimation**. This will add the module to the stack.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8596e4b4-e0d4-46a7-87dd-6cbf56c0a679/sub-uv-animation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8596e4b4-e0d4-46a7-87dd-6cbf56c0a679/sub-uv-animation.png)

   Click image for full size.
2. Adjust the **start frame** and **end frame** in the module properties to match the number of frames in your animation. In this example, there were 8 x 8 frames, for a total of 64. Since the frame starts on frame 0, leave the settings at 0 and 63.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09e9b3ed-b981-410d-aff0-d5540116388c/start-end-frame.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09e9b3ed-b981-410d-aff0-d5540116388c/start-end-frame.png)

   Click image for full size.

### Adjust the Settings on the Sprite Renderer

1. Select the **Sprite Renderer** to adjust the properties. In the **Sub UV** section, specify the number of tiles in the grid in the **Sub Image Size** field. In this example, leave this as 8 x 8.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bc5624b-c6e1-4a6a-838c-a5332bcc27be/sprite-renderer-sub-image-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bc5624b-c6e1-4a6a-838c-a5332bcc27be/sprite-renderer-sub-image-size.png)

   Click image for full size.
2. Now you need to create a new Material to link your Sub UV texture to, and add that into the Sprite Renderer. Click the dropdown menu next to **Material**, then select **Create New Asset > Material**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/60a637c3-44a0-4a1c-aaca-395f39142778/sprite-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/60a637c3-44a0-4a1c-aaca-395f39142778/sprite-material.png)

   Click image for full size.
3. A dialog box appears. Name your Material and choose where to save it.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea02bd88-2d23-403b-8f48-c21f9b4f3b97/name-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea02bd88-2d23-403b-8f48-c21f9b4f3b97/name-material.png)

   Click image for full size.
4. Double-click the Material in the **Content Browser** to open it in the **Material Editor**. In the **Details** panel, set the **Blend Mode** to **Translucent**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0044045-6c38-48f9-8ed1-ec05e17e70f4/blend-mode-translucent.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0044045-6c38-48f9-8ed1-ec05e17e70f4/blend-mode-translucent.png)

   Click image for full size.
5. In the **Material Editor**, right-click and search for 'texture sample' to add the **TextureSample** node.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/200b641f-dd02-48a1-9245-da12ddfe44c0/search-texture-sample-node.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/200b641f-dd02-48a1-9245-da12ddfe44c0/search-texture-sample-node.png)

   Click image for full size.
6. Select the **TextureSample node**. In the **Details** panel, set the **Texture** to be the one you saved from the flipbook baker.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bee58d38-6ab5-4b34-9d58-e11ce8d31cfd/set-texture.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bee58d38-6ab5-4b34-9d58-e11ce8d31cfd/set-texture.png)

   Click image for full size.

   By default, the color channels are premultiplied with black. To avoid black fringing around the sprites, you can use a divide node to remove this from the RGB channels.
7. Right-click to add a **Divide** node.
8. Conenct the **RGB** value from the **TextureSample** node to the **A** pin on **Divide** node, and the alpha **A** from the **TextureSample** value to the **B** pin on **Divide** node.
9. Connect the output of the **Divide** node to **Emissive Color**.
10. Finally, connect the alpha **A** value from the **TextureSample** to the **Opacity** on the material.

    [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23467aae-7f6f-427e-a4f8-f5fb2e8254c1/connect-blueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23467aae-7f6f-427e-a4f8-f5fb2e8254c1/connect-blueprint.png)

    Click image for full size.

### Final Result

Now that your Material is properly set in the Sprite Renderer, open the Niagara System in the Niagara Editor. You now see the flipbook that you rendered out playing in the Preview window.

![The flipbook preview in the Niagara Editor.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea39a07f-9359-4dbd-8ab9-8630e74aa065/flipbook-preview.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Goals](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#goals)
* [Objectives](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#objectives)
* [Set Up the Capture](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#setupthecapture)
* [Navigating the User Interface](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#navigatingtheuserinterface)
* [Frame the Niagara Preview](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#frametheniagarapreview)
* [Adjust the Timing](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#adjustthetiming)
* [Adjust the Texture Size](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#adjustthetexturesize)
* [Set Additional Texture Properties](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#setadditionaltextureproperties)
* [Perform a Capture](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#performacapture)
* [Use the Flipbook Texture in an Emitter](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#usetheflipbooktextureinanemitter)
* [Add the Sub UV Animation Module](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#addthesubuvanimationmodule)
* [Adjust the Settings on the Sprite Renderer](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#adjustthesettingsonthespriterenderer)
* [Final Result](/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?application_version=5.7#finalresult)
