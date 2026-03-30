<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine?application_version=5.7 -->

# Stereoscopic Rendering with nDisplay

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
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. Stereoscopic Rendering with nDisplay

# Stereoscopic Rendering with nDisplay

Options for making nDisplay render stereoscopic images.

![Stereoscopic Rendering with nDisplay](https://dev.epicgames.com/community/api/documentation/image/d495d74e-a00c-4eb1-8f74-d14865799383?resizing_type=fill&width=1920&height=335)

 On this page

In stereoscopic rendering, each nDisplay cluster node generates the images for both the left and right eyes, and encodes the output images using your choice of standard formats for stereoscopic images. In this case, you are responsible for setting up your graphics card, display driver, or hardware to interpret the stereo images produced by nDisplay and route them appropriately.

## Tuning Stereoscopic Rendering

To tune stereoscopic rendering:

* Open your nDisplay Config Asset in the nDisplay 3D Config Editor.
* In the **Components** panel, select the **View Origin** Component to open its **Details** panel.
* In the **Details** panel, you'll need to define the interpupillary distance between the left and right eye. Set the **Interpupillary Distance** field to the distance you want between the left and right eyes, in centimeters.
  If you need to flip the left and right eyes for the images to show up correctly on your display hardware, you can also enable **Swap Eyes**.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/54801cbd-25d0-49e1-9175-751f5bdba73d/01-default-view-point-details.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/54801cbd-25d0-49e1-9175-751f5bdba73d/01-default-view-point-details.png)

  Click image to enlarge
* Open [Switchboard](/documentation/en-us/unreal-engine/switchboard-in-unreal-engine) and go to its **Settings**.
* In the Switchboard Settings window, go to the **nDisplay Settings** section, and set Render Mode to one of the stereo options: **Side-by-Side** or **Top-bottom**.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af0d8e7f-af84-407d-bf0f-68b81e3dd458/02-switchboard-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af0d8e7f-af84-407d-bf0f-68b81e3dd458/02-switchboard-settings.png)

  Click image to enlarge

For details on the available settings, see the [Stereoscopic Rendering Formats](/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine#stereoscopicrenderingformats) section below.

### Stereoscopic Rendering Formats

nDisplay can render stereoscopic images in any of the following standard formats.

| Render mode | Description |
| --- | --- |
| **Frame sequential** | This mode produces sequential stereo pairs for each frame of the engine's main loop. For example, it first renders the left eye for frame 1, then the right eye for frame 1, then the left eye for frame 2, then the right eye for frame 2, then the left eye for frame 3, and so on. In most cases, this option requires a GPU with specialized support for stereoscopic rendering.  This format is known in OpenGL as a *quad buffer*. |
| **Side by side** | In this mode, the image produced for each frame of the engine's main loop is divided in two. The left half of the image contains the view from the position of the left eye, and the right half of the image contains the view from the position of the right eye. This mode has two advantages. First, it may produce higher frame rates because the rendering time is shorter for each image. Second, you can use it with any GPU. On the other hand, the disadvantage is that the images are of lower quality. |
| **Top-bottom** | This mode is almost the same as the **Side by side** option described above. The only difference is that the image for each frame is divided in half horizontally instead of vertically. The top half of the image shows the view from the left eye, and the bottom half of the image shows the view from the right eye. |

## Monoscopic Rendering with Stereo Offset

In this approach, you have one viewport render a monoscopic view of the scene from the point of view of the left eye, and another viewport render a different monoscopic view of the scene from the point of view of the right eye. These viewports can be on the same computer, or on different computers entirely. This approach can also improve rendering speed in the same way as a multi-GPU hardware setup.

For this to work, you need to have two different View Origin components attached to your root component, one for the left eye, and one for the right eye.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Components** panel, click **Add Component** and add a second **View Origin** component. This should be placed in the same location as the default View Origin.

   ![Add a second View Origin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/800e07b4-c5d8-49d5-bd57-aeb83de4ee42/03-ndisplay-view-origin.png)
3. In the **Details** panel, set the **Stereo Offset** of one of the **View Origins** to **Left Eye**, and the **Stereo Offset** of the other to **Right Eye**.
4. Bind one viewport to the first **View Origin**, and the other viewport to the second **View Origin**.

Each View Origin will have an offset equal to half the Interpupillary Distance to the left or right, depending on the Stereo Offset setting for that View Origin. As a result, you will have a stereopair generated by different rendering sources.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [graphics](https://dev.epicgames.com/community/search?query=graphics)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Tuning Stereoscopic Rendering](/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine?application_version=5.7#tuningstereoscopicrendering)
* [Stereoscopic Rendering Formats](/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine?application_version=5.7#stereoscopicrenderingformats)
* [Monoscopic Rendering with Stereo Offset](/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine?application_version=5.7#monoscopicrenderingwithstereooffset)
