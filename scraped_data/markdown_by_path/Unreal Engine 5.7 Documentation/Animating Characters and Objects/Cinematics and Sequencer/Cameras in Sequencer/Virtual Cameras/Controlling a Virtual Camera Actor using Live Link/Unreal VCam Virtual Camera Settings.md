<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7 -->

# Unreal VCam Virtual Camera Settings

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
7. [Cameras in Sequencer](/documentation/en-us/unreal-engine/movie-and-cinematic-cameras-in-unreal-engine "Cameras in Sequencer")
8. [Virtual Cameras](/documentation/en-us/unreal-engine/virtual-cameras-in-unreal-engine "Virtual Cameras")
9. [Controlling a Virtual Camera Actor using Live Link](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine "Controlling a Virtual Camera Actor using Live Link")
10. Unreal VCam Virtual Camera Settings

# Unreal VCam Virtual Camera Settings

Settings and configuration information for the Unreal VCam app

![Unreal VCam Virtual Camera Settings](https://dev.epicgames.com/community/api/documentation/image/1abd0228-df9f-4e9d-b41b-2b51eff7c066?resizing_type=fill&width=1920&height=335)

 On this page

The **Virtual Camera** settings are located on the left side of the Unreal VCam app. This menu includes options to control the different camera, lens, and exposure settings of the virtual camera in your scene.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/5fbcb313-891d-40b2-bdff-3d41a7a05ca1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fbcb313-891d-40b2-bdff-3d41a7a05ca1?resizing_type=fit)

The menu includes the following settings:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/883752d8-b575-46c0-b650-e333cd46a4c8?resizing_type=fit) | **Lens Settings** | Set virtual camera parameters including lens size, focus, iris, and more. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/eb37e126-6272-4fc4-bc4b-51df92edc861?resizing_type=fit) | **Focus Settings** | Set the virtual camera’s focus mode and focus distance. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/7b28e3b3-b1a6-4621-a9fc-6cf150c74a6d?resizing_type=fit) | **Filmback Settings** | Configurable settings for the virtual camera's image sensor. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/3992fdf3-d17e-4b48-bde4-0bccb6e87e63?resizing_type=fit) | **ISO and Exposure Compensation Settings** | Configurable settings for how the virtual camera's exposure is handled. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/8d33a328-9ff7-4987-937d-c2f03de2f080?resizing_type=fit) | **Near Clip Plane Settings** | Set the distance from the camera where polygons no longer render. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/139448e8-c0ff-4189-bbc0-0d2a28c1361b?resizing_type=fit) | **Mask / Overlay / Reticle Settings** | Set what type of aspect ratio mask, grid overlay, and reticle are used with the virtual camera. |

### Lens Settings

The **Lens** settings include virtual camera presets for lenses, focus, and iris settings.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/608f8e2f-c112-4cbd-a456-ec59684ecdba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/608f8e2f-c112-4cbd-a456-ec59684ecdba?resizing_type=fit)

#### Lens Preset and Focal Length

When in **Lens Mode**, you can adjust between configurable presets for common focal lengths and iris. You can also set the iris and dial-in the focus distance manually.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/d2f901f1-b51b-4f93-980a-41a028327744?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2f901f1-b51b-4f93-980a-41a028327744?resizing_type=fit)

You can configure Lens presets in the **Project Settings** under **Cinematic Camera > Lens Presets**. Here, you can add your own, alter, or remove any existing presets.

| Dial Name / Action | Description |
| --- | --- |
| **Left Dials** |  |
| **Lens Preset** | Select from a list of presets for focal lengths and irises. Some presets include the Focal Length dial. Lens presets include:   * 12mm Prime f/2.8 * 12mm Prime f/2.8 * 12mm Prime f/2.8 * 30mm Prime f/1.4 * 50mm Prime f/1.8 * 85mm Prime f/1.8 * 105mm Prime f/2 * 200mm Prime f/2 * 24-70mm Zoom f/2.8 * 70-200mm Zoom f/2.8 * Universal Zoom   Lens presets are set up in the Project Settings in the **Cinematic Camera** category. You can add new presets and edit existing ones. |
| **Focal Length** | Sets the length of the lens (in millimeters). Longer lengths lead to higher magnification with a narrower angle of view. Shorter lengths have lower magnification and a wider angle of view. (Only available on some Lens Presets.) |
| **Right Dials** |  |
| **Focus Distance** | Sets the distance (in meters) from the virtual camera lens where objects are in focus. |
| **Iris** | Controls the amount of light (in f-stops) by making the aperture wider (low f-stop) or narrower (high f-stop). |

#### Using Pinch to Zoom

Pinching in and out with two fingers on the center of the virtual camera screen zooms in and out within the range of your currently selected lens. If your lens is a prime that has a set focal length and cannot zoom, pinch to zoom does nothing.

### Focus Settings

The **Focus** settings contain options for configuring how the virtual camera focuses on objects.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/85ffe658-98fb-43c9-8117-2a8114bdbf28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/85ffe658-98fb-43c9-8117-2a8114bdbf28?resizing_type=fit)

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/9b19a651-3d91-47d5-bc48-2c57d19695f3?resizing_type=fit) | **Focus Method** | Choose how you want the virtual camera to apply focus in the scene:   * **Do Not Override** removes the ability to change the focus distance dial in any menu and causes the **Post Process Volume** settings to persist * **Manual** lets you manually adjust the focus using the **Focus Distance** dial to set the distance from the camera to the subject * **Tracking** locks focus on specific actors in the shot * **Disable** stops all depth of field from happening |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/048ad70c-a734-41c9-8d3f-451e2689fe0b?resizing_type=fit) | **Focus Distance** | Specifies the distance (in meters) from the virtual camera lens to the point where objects appear in focus. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/97a1bc8a-7fbf-4f2a-88f5-a85a996a9b3f?resizing_type=fit) | **Pick Actor to Track** | Use this to pick an actor in the scene to focus on. When in **Tracking** mode, the selected actor always remains in focus, and its distance from the camera drives the Focus Distance. When in **Manual** mode, the Manual Focus Distance is set to the distance to this target, but it does not track the selected actor ifthe camera or target moves. |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/4679e95d-0721-4d06-a818-afc6ae635133?resizing_type=fit) | **Toggle Focus Peaking** | Toggles a visual reference in the scene where the focus distance is currently set. |

#### Using Tap to Focus

You can select a focus target by double tapping on that actor in the scene. A yellow focus indicator appears to confirm where you have tapped. Tap to focus is available even if you are not in **Focus Mode.**

The behavior of tap to focus differs based on your current mode:

* In **Manual Focus**, tapping an actor sets the manual focus distance to the distance to the tapped actor. This value does not update if the actor or camera moves.
* In **Tracking Focus**, tapping an actor sets the tracking focus target and lock focus distance to the tapped point on the selected actor or skeletal mesh socket. If the actor/socket or camera moves, focus adjusts to keep the point in focus.

Only actors with collision (or physics assets in the case of skeletal actors) can be detected with tap to focus.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/d427d018-5866-4caa-86da-5c088cee1765?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d427d018-5866-4caa-86da-5c088cee1765?resizing_type=fit)

#### Using Tracking Focus

You can track an actor in the scene and maintain the virtual camera's focus on it by using the **Pick Actor to Track** option in the HUD or by using **Tap to Focus**.

To use Tracking Focus:

1. In the **Lens settings** menu, navigate to the **Focus** settings. Here, **Focus Method** is selected by default with its adjustable dials present on screen.
2. Drag the **left dial** to **Tracking**.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/83175694-5ea9-401e-9851-140389965bbc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/83175694-5ea9-401e-9851-140389965bbc?resizing_type=fit)

While holding and looking at your device, double-tap on an actor in the scene. Alternatively, point the virtual camera **Reticle** at the object you want to keep focused on. Tap the **Pick Actor to Track** icon in the left menu. Once you've done this, look at the **Right** dial and you'll see the **Tracking Offset** along with the **Name** of the focused asset/skeletal mesh socket below.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/4ec4c2d8-ea69-44d9-8117-8cc0405e1bb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ec4c2d8-ea69-44d9-8117-8cc0405e1bb1?resizing_type=fit)

When using the Tracking focus method, use the right dial for **Tracking Focus Offset** to dial-in the focus on the subject. When tracking a Skeletal Mesh actor, the target point moves to the closest socket for focus, which may not always be the exact spot you're wanting to focus on.

Tracking focus is effective as long as the target actor remains within the camera view. When the target actor moves out of the view, the system automatically switches to **Manual**focus mode. By switching to Manual, the focus distance stays stable and is not influenced by objects that are no longer visible from the camera.

#### Using Focus Peaking

You can use the **Focus Peaking** toggle to see exactly where the focus distance is in the scene. A red outline represents the focal distance. **Focus Peaking** is useful for quickly seeing where the focus distance is in the scene to dial it in. The outlined area expands and contracts to show the **depth of field** based on your current **iris**. To dial in the focus, use the **Focus Distance** dial on the right side of the app.

### Filmback Settings

**Filmback** describes the dimensions of the frame for the digital imaging sensor. This size determines what the camera sees through its viewfinder. The filmback determines frame size, depth of field, resolution, and more.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/ec3c012c-a2a0-4f95-9e4c-cc8a468c6239?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec3c012c-a2a0-4f95-9e4c-cc8a468c6239?resizing_type=fit)

There standard presets are:

* 16:9 Film
* 16:9 Digital Film
* 16:9 DSLR
* Super 8mm
* Super 16mm
* Super 35mm
* 35mm Academy
* 35mm Full Aperture
* 35mm Vista Vision
* IMAX 70mm
* APS-C (Canon)
* Full Frame DSLR
* Micro Four Thirds

The examples below are using the **30mm Prime f/1.4** Lens Preset.

|  |  |  |  |
| --- | --- | --- | --- |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/a892da76-6dd0-4c29-93fb-76ea7cf59775?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/da80574e-266c-4fb1-8737-bb04832f14aa?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/35dab7e2-f75d-46fc-86ee-ea8b94258247?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/ab371692-321a-4e7d-9a65-4138981e46d6?resizing_type=fit) |

You can configure Filmback presets in the Project Settings under **Cinematic Camera > Filmback Presets**. Here, you can add your own, alter, or remove any existing presets.

### ISO, Iris, Shutter Speed and Exposure Compensation Settings

The **Exposure** settings control how bright or dark the image is.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/b5adff93-ebf2-41c4-beca-bb2aa2a2442d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5adff93-ebf2-41c4-beca-bb2aa2a2442d?resizing_type=fit)

| Dial Name / Action | Description |  |
| --- | --- | --- |
| **Left Dials** |  |  |
| **ISO** | Sets the sensitivity of the camera's sensor. Lower numbers have a lower sensitivity to light, which makes the image darker. Higher numbers have a higher sensitivity to light, which makes the image brighter. When not set to **Auto Exposure**, the ISO is dependent on what f-stop the camera iris is set to. |  |
| **Iris** | Sets the diameter (measured in f-stops) of the aperture's opening. This controls the amount of light that is allowed to pass through the lens of the camera. It also has an effect on depth of field. For more information, see [Cinematic Depth of Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-depth-of-field-in-unreal-engine). |  |
| **Right Dials** |  |  |
| **Exposure Compensation** | Applies a compensation (measured in stops) to override exposure to brighten or darken the frame. Lower numbers give a higher exposure, which makes the result brighter. Higher numbers give a lower exposure, which makes the result darker. |  |
| **Shutter Speed** | Adjusts the camera’s "exposure time" (measured in fractions of a second). Slower shutter speeds result in a brighter image. Faster speeds result in a darker image. Unlike a physical camera, shutter speed on the Virtual Camera only affects exposure and not motion blur. |  |

#### Using Zebra Striping

Tapping the **Zebra striping** button from **Exposure Mode** or the top quick action buttons toggles zebra striping. When enabled Zebra Striping marks areas of the frame that are over-exposed.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/21b457a2-51b6-4f15-8254-136a85cb1c9b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21b457a2-51b6-4f15-8254-136a85cb1c9b?resizing_type=fit)

### Near Clip Plane

The **Near Clip Plane** sets the distance (measured in centimeters) from the camera that polygons no longer render. This option is useful when you want to not render objects blocking the view but also continue to render their shadows and interaction with the scene.

In the example below, the virtual camera is using a longer lens to capture the subject, but the view is partially obstructed by a plant. Using the near clip plane, Unreal doesn't render any geometry within the set distance from the camera.

### Mask, Overlay, and Reticle Settings

The **Mask / Overlay / Reticle** settings include optional visual guides for the virtual camera viewfinder. This includes grids, safe zones, different reticles, and mattes to mask off different aspect ratios.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/d73e1ba8-07a6-479c-baba-1053faf26119?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d73e1ba8-07a6-479c-baba-1053faf26119?resizing_type=fit)

Each of the groups for overlays, reticles, and masks include their own **Opacity** dial. You can use this to set how opaque or transparent each is. At 0, they are not visible, at 0.5 they're partially transparent, and at 1.0 they're fully opaque.

|  |  |  |
| --- | --- | --- |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/46f7363d-d4f1-4d28-b1a5-4e80adc46238?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/6cec3dc3-7cdf-4dcc-bf0b-113f6588ef99?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/ce19b57d-2162-4e2b-9089-76661b5da621?resizing_type=fit) |

#### Overlay Selections

Use the **Overlay** dial to choose the type of grid to overlay on the virtual camera viewfinder.

You can choose from the following options:

|  |  |  |  |
| --- | --- | --- | --- |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/5dbca373-0edf-4f3c-9b73-00a0c9604d35?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/2c4bbfd9-c374-4276-a40e-a580a2aad75d?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/e5c5d24d-e175-4b48-a4f5-89f876bc157e?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/af72c516-f1e7-492b-8efd-1c3526e34b2c?resizing_type=fit) |

#### Reticle Selections

You can use the **Reticle** dial to choose the design for the center of the frame used to aim what the virtual camera is looking at.

You can choose from the following options:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [image alt text](https://dev.epicgames.com/community/api/documentation/image/409a37ac-36f5-413f-8b62-afc82bea6906?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/d03247d6-a2b3-4898-9374-a3f4eac9f045?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/8b2c7684-b1d7-41b2-9990-5935e4cd9b90?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/586309f4-7566-4bfd-b711-37ecc8da5959?resizing_type=fit) | [image alt text](https://dev.epicgames.com/community/api/documentation/image/79270561-91ca-42a1-bdf5-9e116314a4e9?resizing_type=fit) |

#### Mask Selections

You can use the **Mask** dial to choose from the presets for different size aspect ratio mattes in the virtual camera viewfinder. The mask presets include common industry standards.

You can choose from:

* 9:16 (0.562)
* 1:1
* 4:3 (1.333)
* 3:2 (1.5)
* 16:9 (1.778)
* 1.85:1 (1.85)
* 2:1
* 2.39:1 (2.39)
* 2.4:1 (2.4)
* 2.76:1 (2.76)
* Custom

Below is an example of the mask presets overlaying the virtual camera viewfinder:

If none of the included presets fit your requirements, you can use the **Custom** option to define your own masked area. When selected, a new dial appears on the right side of the screen. Drag the dial to the left to make the mask smaller, drag the dial to the right to make the mask larger. The mask can fill the tops and bottoms of the frame or the sides of the frame.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/ad04690e-380a-4ac2-8fec-d07e98a721b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad04690e-380a-4ac2-8fec-d07e98a721b2?resizing_type=fit)

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [virtual camera](https://dev.epicgames.com/community/search?query=virtual%20camera)
* [working with media](https://dev.epicgames.com/community/search?query=working%20with%20media)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Lens Settings](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#lens-settings)
* [Lens Preset and Focal Length](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#lens-preset-and-focal-length)
* [Using Pinch to Zoom](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#using-pinch-to-zoom)
* [Focus Settings](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#focus-settings)
* [Using Tap to Focus](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#using-tap-to-focus)
* [Using Tracking Focus](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#using-tracking-focus)
* [Using Focus Peaking](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#using-focus-peaking)
* [Filmback Settings](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#filmback-settings)
* [ISO, Iris, Shutter Speed and Exposure Compensation Settings](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#iso-iris-shutter-speed-and-exposure-compensation-settings)
* [Using Zebra Striping](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#using-zebra-striping)
* [Near Clip Plane](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#near-clip-plane)
* [Mask, Overlay, and Reticle Settings](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#mask-overlay-and-reticle-settings)
* [Overlay Selections](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#overlay-selections)
* [Reticle Selections](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#reticle-selections)
* [Mask Selections](/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings?application_version=5.7#mask-selections)
