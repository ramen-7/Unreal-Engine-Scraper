<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7 -->

# Unreal VCam Tools and Configuration

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
10. Unreal VCam Tools and Configuration

# Unreal VCam Tools and Configuration

Tools and configuration options for the Unreal VCam app.

![Unreal VCam Tools and Configuration](https://dev.epicgames.com/community/api/documentation/image/1a428449-1322-4c29-b8e5-d9698228c665?resizing_type=fill&width=1920&height=335)

 On this page

The **Tools** menu includes configurable settings and toggles that let you adjust how you interact with the Live Link-enabled device and the virtual camera in the Unreal Engine scene.

To open the Tools menu, tap the **Wrench** icon on the right side of the screen.

[![](https://dev.epicgames.com/community/api/documentation/image/0b5c0d3a-8cdb-4a68-b5be-ac9f8d19a6d9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b5c0d3a-8cdb-4a68-b5be-ac9f8d19a6d9?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/2a60f142-54eb-49aa-82c6-397ff331a9d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2a60f142-54eb-49aa-82c6-397ff331a9d2?resizing_type=fit)

The **Tools** menu includes the following settings:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [Takes Browser icon](https://dev.epicgames.com/community/api/documentation/image/75be7a59-4391-45cb-a8a8-f3a9b19c3a3e?resizing_type=fit) | [Takes Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine) | Opens the Virtual Camera’s Takes Browser, where you can search for and open level sequences for review or recording. |
| [Scale and Gain icon](https://dev.epicgames.com/community/api/documentation/image/84b78c15-07f2-4e68-9e21-ff6120b37bcd?resizing_type=fit) | [Scale and Gain Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine) | Contains settings to configure how movement of the Live Link-enabled device works with the Unreal Engine scene. This includes how sensitive the movement of the device is in a physical space and the sensitivity of the joystick movement. |
| [Hold icon](https://dev.epicgames.com/community/api/documentation/image/be0b81e5-6ab0-465c-a82d-8d2220f7b4bd?resizing_type=fit) | **Hold** | Toggles whether the virtual camera's location and rotation is frozen. This is useful for repositioning your physical live link-enabled devices without losing your virtual camera's position in the scene. |
| [Zero to Stage icon](https://dev.epicgames.com/community/api/documentation/image/a6c346c0-987b-4c23-b245-5663fa31e220?resizing_type=fit) | **Zero To Stage** | Removes any offsets to the virtual camera’s tracked location. This puts the camera back into tracking space. |
| [Zero to Parent icon](https://dev.epicgames.com/community/api/documentation/image/8a79e118-8e02-4f0d-994f-31ecc8174950?resizing_type=fit) | **Zero to Parent** | Snaps the virtual camera onto its parent with an effective relative location of (0,0,0). If the virtual camera has no parent, this snaps to the world origin. |
| [Local Space Flight Mode icon](https://dev.epicgames.com/community/api/documentation/image/c43a694c-de3c-4df8-81c6-306625a01c47?resizing_type=fit) | **Local Space Flight Mode** | When enabled, this makes the forward joystick movement follow the forward direction of the camera instead of the world. When in Local Space Flight Mode, looking up or down moves the camera in that direction when you push a joystick forward. When disabled, the camera can freely look around the scene but move forward without moving in the direction the camera is pointed. |
| [Kill Roll icon](https://dev.epicgames.com/community/api/documentation/image/07435ed6-270b-4370-89e4-3fc064667c93?resizing_type=fit) | **Kill Roll** | Toggles whether the virtual camera rotation along the X-axis is disabled, keeping the camera level when moving around while the Live Link-connected device is moving in a physical space. |
| [Spline Mode icon](https://dev.epicgames.com/community/api/documentation/image/b539b04f-5415-4a1b-a1e1-74ce84fe5796?resizing_type=fit) | [Spline Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine) | When enabled, you can create and edit your own Rig Rails from the Unreal VCam app. |
| [Tile Offset icon](https://dev.epicgames.com/community/api/documentation/image/c1ca2d25-b779-4b78-8050-c1cbd5bd78b8?resizing_type=fit) | **Tile Offset** | Applies an arbitrary offset to the Tilt of the virtual camera. This makes holding shot angles more comfortable. When enabled, the Tilt HUD value will display a + symbol.  [Tile offset enabled HUD display](https://dev.epicgames.com/community/api/documentation/image/8ec9bda2-7566-4bf7-9ac9-47389a4e1d64?resizing_type=fit) |
| [Bookmark Browser icon](https://dev.epicgames.com/community/api/documentation/image/5104fec6-c63e-46dd-a856-7f99802f52b9?resizing_type=fit) | **Bookmark Browser** | Opens the Virtual Camera Bookmark Browser. |
| [Multi User Replication](https://dev.epicgames.com/community/api/documentation/image/4f3a8938-b875-4703-abd9-1b119d234812?resizing_type=fit) | **Multi User Replication** | Sets the current client as the author of the Virtual Camera in Multi User. Changes made from this client propagate to others, while changes from others are overridden from this client. |
| [The GameView icon](https://dev.epicgames.com/community/api/documentation/image/f77fa342-65ca-4291-b9dc-171647d40ff8?resizing_type=fit) | **GameView** | When enabled, the GameView displays the scene as if it would appear in the game. |

### Virtual Camera Movement with Scale and Gain Settings

Movement in the Live Link-enabled device is registered by tracking positional data from the device and through the use of touch-screen joysticks, including tilt, pan, and roll movement. The touch-screen joysticks layer directional and rotational movement on top of the ARKit motion.

Virtual camera movement from a Live-Link-enabled device is controlled by:

* ARKit tracked axial and locomotor movement.
* Touch-screen Joysticks
* The **Left** joystick controls directional forward, backward, diagonal, and side-to-side movement.
* The **Right** joystick includes two separate movement controls:
* **Rotational** movement by dragging left and right on the screen.
* **Vertical** movement by dragging up and down on the screen.

You can adjust the sensitivity of each type of movement so that small movements can have a bigger effect, or the opposite where bigger movements have smaller impact. You can find these controls under the **Scale and Gain** settings menu on the right side of the screen.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/9f6e84d0-4e48-4ac6-b4aa-ebca9dd5b2a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f6e84d0-4e48-4ac6-b4aa-ebca9dd5b2a3?resizing_type=fit)

The menu includes the following settings:

| Dial Name / Action | Description |
| --- | --- |
| Left Dials |  |
| **Axis** | Sets the axis constraint for movement:   * **All** allows movement along all axes. * **Planar** allows only movement along the X-axis and Y-axis to be scaled. Vertical movement is unaffected. * **Vertical** allows movement along the Z-axis to be scaled. Planar movement along the X-axis and Y-axis is unaffected. |
| **Scale** | Scales the ARKit tracked movement of the device in physical space. The scale adjusts how movements are translated from real-world physical space to the virtual camera digital space through Live ink. Small scale values translate as larger physical space movement to smaller digital space movement. Larger scale values translate as smaller physical space movement to larger digital space movement. |
| Right Dials |  |
| --- | --- |
| **Joystick Movement Gain** | Controls the speed of both the left directional joystick and the right vertical-only joystick movement. |
| **Joystick Rotation Gain** | Controls the speed of rotation when engaging the right joystick in left or right rotational movement. |

Setting any dial to **Locked** or **0** restricts movement being tracked through Live Link or any engagements of the joystick. For example, setting the Axis to Vertical with a Scale set to Locked means that vertical movement cannot happen. Another example is setting the Joystick Rotation Gain to 0 restricts any rotation applied through the joystick.

## Browsing for Sequences and Reviewing Takes

### Takes Browser

Tapping the **Takes Browser** button in the tools menu opens the Takes Browser. The Takes Browser displays a sorted list of level sequences that can be opened for review or recording.

[![The Takes Browser](https://dev.epicgames.com/community/api/documentation/image/212f73d8-c22b-4382-a18f-3f5302d40f46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/212f73d8-c22b-4382-a18f-3f5302d40f46?resizing_type=fit)

Tapping on a level sequence brings up two options

| Icon | Description |
| --- | --- |
| [Takes Reload icon](https://dev.epicgames.com/community/api/documentation/image/2ce8a66d-9470-4c6f-a965-fc0e41927c01?resizing_type=fit) | Tap this to load the selected sequence into the Take Recorder, making it the base for the next recording. Use this option to select the animation that you want to record cameras onto. |
| [Takes Review icon](https://dev.epicgames.com/community/api/documentation/image/80246419-1dd1-4199-af76-b14b24271332?resizing_type=fit) | Tap this to open a sequence into review. This pilots the camera cuts track of the sequence and provides simplified controls for reviewing the sequence. |

Holding on a level sequence shows the asset path. It also shows the dirty state when the level sequence is modified

[![Take overlay showing asset path](https://dev.epicgames.com/community/api/documentation/image/65818fb3-9403-4ea0-85ce-16947b808d3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/65818fb3-9403-4ea0-85ce-16947b808d3d?resizing_type=fit)

#### Tagging Takes

Swiping left or right on a sequence in the Takes Browser tags that sequence with the selected metadata, which can be used to filter the sequences in the Takes Browser.

| Option | Description |
| --- | --- |
| [Star tag](https://dev.epicgames.com/community/api/documentation/image/6568e328-7463-4de0-90b5-1c5b167d3f68?resizing_type=fit) | Swiping to the right illuminates one, two, or three stars, depending on how far you swipe. Stopping at a number of illuminated stars tags the take with that number of stars. |
| [Flag take](https://dev.epicgames.com/community/api/documentation/image/fb1a7808-5045-4fa5-a5d4-3f79574e3c53?resizing_type=fit) | Swiping to the left reveals a yellow flag. Tapping this tags the take as flagged. Use this flag to denote any information relevant to your workflow. |
| [Take no good](https://dev.epicgames.com/community/api/documentation/image/1ee948da-ecb2-4491-aac4-d6ef22accf2a?resizing_type=fit) | Swiping to the left reveals a red thumbs down. Tapping this marks the take as "no good" and filters it out of the Takes Browser. After tapping, you are presented with a short undo prompt. Tapping this before the time has elapsed removes the No Good tag and returns the take to the browser.  This does not delete the level sequence, only hides it from the Takes Browser list by default. |

#### Filtering and Ordering the Takes Browser

The top of the Takes Browser contains a search bar and filters dropdown. Typing into this search bar filters the list by takes containing the matching string.

[![Filter takes](https://dev.epicgames.com/community/api/documentation/image/c1a62b8b-9954-4a4b-9131-d2e8f9530f13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c1a62b8b-9954-4a4b-9131-d2e8f9530f13?resizing_type=fit)

Tapping the filters dropdown reveals or hides the Takes Browser filters and sorting options.

[![Take Sorting options](https://dev.epicgames.com/community/api/documentation/image/e608f6e1-5826-4f41-baaa-361572604bfe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e608f6e1-5826-4f41-baaa-361572604bfe?resizing_type=fit)

The available filters are:

| Icon | Description |
| --- | --- |
| [Show Only Take icon](https://dev.epicgames.com/community/api/documentation/image/4928efd4-cee3-41e0-bb53-4db0c5135e2f?resizing_type=fit) | Tap this to toggle showing only sequences recorded from Take Recorder and hide Non-recorded sequences. |
| [Show Flagged icon](https://dev.epicgames.com/community/api/documentation/image/4887ceff-4c37-4055-b426-d8fff58184c9?resizing_type=fit) | Tap this to toggle showing only sequences marked with the flag tag. |
| [Show No Good icon](https://dev.epicgames.com/community/api/documentation/image/59250262-2697-452a-8254-988ead5b3067?resizing_type=fit) | Tap this to toggle only sequences marked as "no good". Use this if a sequence needs to be recovered or was marked no good in error. |
| [Show Starred icon](https://dev.epicgames.com/community/api/documentation/image/5411cb83-7726-4710-aae0-05f88d04078c?resizing_type=fit) | Tap this to cycle between showing only sequences tagged with a number of stars greater than the number shown. For example, tapping until the star displays the number 2 shows only sequences with 2 or 3 stars. |
| [Sort Takes by Time icon](https://dev.epicgames.com/community/api/documentation/image/2c0887bc-21b0-4c5a-b73e-bace2240cda9?resizing_type=fit) | Tap this to cycle between sorting the Takes Browser newest to oldest or oldest to newest. There is no sub sorting, so the list can only be sorted by creation date or alphabetically. |
| [Sort Takes Alphabetical icon](https://dev.epicgames.com/community/api/documentation/image/a5e0a25f-dbe7-499c-be92-07aa6ac8b6c9?resizing_type=fit) | Tap this to cycle between sorting the Takes Browser in alphabetical or reverse alphabetical order. There is no sub sorting, so the list can only be sorted by creation date or alphabetically. |

### Take Viewer

You can use the Take Viewer to navigate between individual takes, so you can tag and smooth them.

The Take Viewer window opens when you load a take from the Takes Browser. Alternatively, you can tap the Take thumbnail in the lower left corner in the HUD to open the latest Take.

[![Take Viewer](https://dev.epicgames.com/community/api/documentation/image/af9497ab-ba93-4b46-99f8-e7c2a26cf6a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af9497ab-ba93-4b46-99f8-e7c2a26cf6a7?resizing_type=fit)

#### Tagging Takes

On the current Take, you can add stars, a flag tag, or mark the take as "no good.

[![Take tagging options](https://dev.epicgames.com/community/api/documentation/image/16671935-7a2b-4a99-8023-916c4bac8b44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16671935-7a2b-4a99-8023-916c4bac8b44?resizing_type=fit)

#### Smoothing Takes

When viewing a take, you can tap the button in the top right corner to show a slider to smooth the camera keyframes in the level sequence

[![Slider for Take smoothing](https://dev.epicgames.com/community/api/documentation/image/c2181a14-6ad9-43b5-a2ec-ee9df5357382?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2181a14-6ad9-43b5-a2ec-ee9df5357382?resizing_type=fit)

#### Navigating Takes With Carousel View

To open the carousel view, tap the Take thumbnail in the lower left corner. The carousel view lists all takes in chronological order.

[![Take Viewer carousel](https://dev.epicgames.com/community/api/documentation/image/8a1fef1a-866a-403b-b4aa-1a483a609b26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a1fef1a-866a-403b-b4aa-1a483a609b26?resizing_type=fit)

In the carousel view, you can do the following:

* Swipe the thumbnails to navigate the takes. The thumbnail in the center becomes the current item, which is indicated by the white highlight on top and the thumbnail being bigger in the preview window.
* Tap the preview window to open the level sequence for review. The blue highlight on the top indicates the current level sequence in review.
* Tap the down arrow in the lower button to close the carousel view.
* Tap the **<** and **>** buttons next to the carousel to navigate the takes one by one.

#### Open Takes Browser

You can tap the magnifier icon on the lower right corner to open Takes Browser for more search and filtering options. For more information about the Takes Browser, see the Takes Browser section under Browsing for Sequences and Reviewing Tasks further up on this page.

[![Open Takes Browser icon](https://dev.epicgames.com/community/api/documentation/image/e85271a1-934c-4687-bfaa-cdf21bc938de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e85271a1-934c-4687-bfaa-cdf21bc938de?resizing_type=fit)

## Teleporting

Pressing down on the screen with 2 fingers and dragging enables teleportation of the VCam for faster movement around the scene. While 2 fingers are held down, a blue landing zone indicator is displayed where you are touching. Moving your fingers causes the landing zone to follow your fingers. Upon releasing your fingers, the Virtual Camera teleports to the location indicated by the landing zone.

Teleportation can only detect surfaces with collision.

### Sequencer and Bookmarks Settings

The bottom-most section of the Virtual Camera actor includes quick reference to camera settings, and Sequencer playback. The top-most section contains camera bookmarks and recording.

[![Virtual Camera actor top](https://dev.epicgames.com/community/api/documentation/image/609c7fe1-fcd6-4021-8796-537b851dfb49?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/609c7fe1-fcd6-4021-8796-537b851dfb49?resizing_type=fit)

[![Virtual Camera actor bottom](https://dev.epicgames.com/community/api/documentation/image/16db90ca-b1a7-45f8-a8b6-b1815620b88b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16db90ca-b1a7-45f8-a8b6-b1815620b88b?resizing_type=fit)

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| Section 1 |  |  |
| [Create Bookmark icon](https://dev.epicgames.com/community/api/documentation/image/a1ec77b3-0996-484c-b4bf-df9eb52b3558?resizing_type=fit) | **Create Bookmark** | Tap this to create a bookmark of the current position and rotation and camera settings used by the virtual camera. If you have Photo Save Mode enabled, an icon image of a DSLR Camera appears instead. |
| [Re-inherit Camera Settings icon](https://dev.epicgames.com/community/api/documentation/image/0ef69b2a-17e6-415e-9621-9f84a66ec054?resizing_type=fit) | **Re-inherit Camera Settings** | Bookmarks store camera parameters (including aperture and focal length). This controls whether those stored camera parameters are loaded when jumping to a bookmark. |
| [Bookmark Navigation icon](https://dev.epicgames.com/community/api/documentation/image/7bf576bb-9ede-425a-b331-e9c034f13053?resizing_type=fit) | **Bookmark Navigation** | Navigational controls to cycle forward and backwards through any virtual camera bookmarks in the scene. |
| [Remove Bookmark icon](https://dev.epicgames.com/community/api/documentation/image/291caaa4-9749-41fd-9039-e20a40ec4c37?resizing_type=fit) | **Remove Bookmark** | Tap this to remove the currently selected bookmark from the Unreal VCam app. This button removes the bookmark scene actor from your Unreal Engine project. |
| [The Current/Select Bookmark button](https://dev.epicgames.com/community/api/documentation/image/9f31c659-9258-434e-9aef-638966635586?resizing_type=fit) | **Current/Select Bookmark** | Displays the most recently loaded bookmark. Tapping this brings up the Bookmark Browser. |
| Section 2 |  |  |
| --- | --- | --- |
| [Scale icon](https://dev.epicgames.com/community/api/documentation/image/30ac08f9-9106-4c64-b912-54c2502258e8?resizing_type=fit) | **Scale** | Displays the current scales applied to device movement. For more information, see [Virtual Camera Movement with Scale and Gain Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.5). |
| [Stabilization icon](https://dev.epicgames.com/community/api/documentation/image/f8f0ba86-5cda-4620-b48a-948a24ed6d37?resizing_type=fit) | **Stabilization** | Displays the amount of stabilization applied to the virtual camera's rotation and location movement. Higher values give more stabilization to movement at the cost of responsiveness creating smoother camera movement. Lower values give less stabilization and are more responsive, which creates rougher camera movement. For more information, see [Virtual Camera Stabilization](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.5). |
| [Orientation icon](https://dev.epicgames.com/community/api/documentation/image/a3f8a722-6e72-4fd4-8fde-24af455eb5e1?resizing_type=fit) | **Tilt, Pan, Roll Orientation** | Displays the virtual camera's rotational position. For more information, see [Virtual Camera Movement with Scale and Gain Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.5). |
| Section 3 |  |  |
| --- | --- | --- |
| [Timeline icon](https://dev.epicgames.com/community/api/documentation/image/1448a053-a341-4992-9e8b-77d5452c9302?resizing_type=fit) | **Timeline** | Displays the timeline for the currently loaded Sequence in the Unreal Editor. To move the slider to a different frame within the Sequence, drag your finger along the timeline. |
| [Sequencer Playback Controls icon](https://dev.epicgames.com/community/api/documentation/image/e8e2effb-0dfd-46f9-98fd-d8077fe3cd5f?resizing_type=fit) | **Sequencer Playback Controls** | The playback controls function similarly to standard media playback applications with play, skip frame, skip to beginning and end frames, and so on. For more information, see [Sequencer Cinematic Editor](animating-characters-and-objects\Sequencer). |
| [Playback TimeScale icon](https://dev.epicgames.com/community/api/documentation/image/b73067a0-1376-463f-ae68-255df32dc44f?resizing_type=fit) | **Playback TimeScale** | Use this to the time scale of the sequencer. For example, setting a value of 0.5x causes the sequence to playback at half speed. |
| [Slate icon](https://dev.epicgames.com/community/api/documentation/image/e7224838-a5b7-4f3a-b625-0a7d31e9c12c?resizing_type=fit) | **Slate** | Displays the slate name to be used for the next recording. This can be tapped to bring up the on screen keyboard, allowing the slate name to be edited |
| [Take number icon](https://dev.epicgames.com/community/api/documentation/image/4a946fb0-a4b2-4c6b-9be2-c30e81f59d67?resizing_type=fit) | **Take** | Displays the take number of the next recording. This can be tapped to bring up the on screen keyboard, allowing the take number to be edited. |
| [Sequencer Frame Counter icon](https://dev.epicgames.com/community/api/documentation/image/13327eee-a928-45c0-9b96-73ccc9086551?resizing_type=fit) | **Sequencer Frame Counter** | Displays the current frame number the timeline is reading. |
| [Take Recorder icon](https://dev.epicgames.com/community/api/documentation/image/051ce78c-e649-4ebf-9a00-71395f56027f?resizing_type=fit) | **Take Recorder** | Tap this to open Take Recorder and start recording of gameplay, live performance, and other sources directly into Unreal Engine. For more details, see [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine) and [Using Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/record-gameplay-in-unreal-engine). |
| [Recording Time Scale icon](https://dev.epicgames.com/community/api/documentation/image/3f32fac0-9a56-4f44-bab1-30ce2a127424?resizing_type=fit) | **Recording Time Scale** | Use this to set the current time scale for the recording. For example, recording at 0.5x plays the pending take back at half speed. When reviewed, your camera move is sped up 2x to match the original speed of the sequence. |
| [Open Last Take icon](https://dev.epicgames.com/community/api/documentation/image/ec2eae14-6ac7-49ea-b306-27b4ce2fe089?resizing_type=fit) | **Open Last Take** | Tap the thumbnail to open the last recorded take in Take Viewer. |

### Virtual Camera Stabilization

Tap on the **Stabilization** text to open the virtual camera stabilization dials. These dials affect how much the camera prevents or compensates for unwanted camera movement. Camera movement appears smoother and less responsive when using higher stabilization values. Lower values tend to be more responsive, causing a lot of shake and instability in camera movement.

The **Left** dial controls **Rotation Stabilization**, and the **Right** dial controls **Location Stabilization**. In the video below, you can see the difference between using a value of 0x, 50x (default), and 100x.

## Parenting and Platforming

When not in Spline Mode, the top right of the virtual camera displays the parenting and platforming control.

[![Parenting and Platforming controls](https://dev.epicgames.com/community/api/documentation/image/19771e52-3119-4dc9-91a3-10ddb26ae155?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19771e52-3119-4dc9-91a3-10ddb26ae155?resizing_type=fit)

### Creating an Attach Mount

Though the virtual camera can be attached to anything from the desktop, the available options to the handheld operator are limited to Cine Camera RigRails, Cine Camera Actors, and Cine Camera Attach Mounts. Using the Cine Camera Attach Mount gives you more control over how the virtual camera attaches to its parent, including enabling and disabling certain axes as well as introducing lag in following the parent for a more natural follow behavior.

To create an Attach Mount click the place actors menu and search for "attach." Drag and drop the **Cine Camera Attach Mount** into the world.

[![Create an Attach Mount](https://dev.epicgames.com/community/api/documentation/image/52a3caee-302e-4220-b6e7-0c1dbad41749?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52a3caee-302e-4220-b6e7-0c1dbad41749?resizing_type=fit)

To configure the parent for the attach mount, select it in the world outliner and in the **Details** panel**,** set the **Target Actor** to the desired actor. If the Target Actor is skeletal, specify the **Target Socket** to enable attachment to a specific bone or socket.

[![Configure an Attach Mount](https://dev.epicgames.com/community/api/documentation/image/dcf39790-d726-4748-a3ee-c6a4915e283f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dcf39790-d726-4748-a3ee-c6a4915e283f?resizing_type=fit)

Name the Attach Mount to something indicative of its parent for later.

### Selecting and Attaching to a Parent

Tapping the central dropdown brings up a list of available parents. Though the virtual camera can be attached to anything in your scene, the available options to the handheld operator are limited to Cine Camera Rig Rails, Cine Camera Actors, and Cine Camera Attach Mounts. Selecting an option from this drop-down automatically snaps the virtual camera to its new parent and enables attachment. Attachment can be toggled on and off using the **paperclip** button.

[![Select and attach a camera to a parent](https://dev.epicgames.com/community/api/documentation/image/0ab1d520-c145-410e-9558-983d07b1ebf4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ab1d520-c145-410e-9558-983d07b1ebf4?resizing_type=fit)

### Inheriting Specific Axes and Camera Parameters

By default, the virtual camera inherits all axes from its parent, though it can still move on top of this platform. Selecting the right most axis button, however, expands a list of axis and camera parameters that can optionally be disabled, inherited (the virtual camera inherits its parent’s axis value but can still offset on top), or locked (the virtual camera inherits its parent’s axis value but can’t offset on top). These options are only available if the parent is CineCamera Rig Rail, Cine Camera Actor, or Cine Camera Attach Mount.

The available options are:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [Dolly icon](https://dev.epicgames.com/community/api/documentation/image/e24b40d9-2907-48cd-bbd4-a2aaa58945c4?resizing_type=fit) | **Dolly** | Tap this to cycle between inheriting, locking, or ignoring the forward and backward movement of its parent. |
| [Truck icon](https://dev.epicgames.com/community/api/documentation/image/099f41f0-9f7f-4784-9cf6-247a01b7870e?resizing_type=fit) | **Truck** | Tap this to cycle between inheriting, locking, or ignoring the side to side movement of its parent. |
| [Crane icon](https://dev.epicgames.com/community/api/documentation/image/0b12e551-d659-4726-8ad2-3c502756ba1b?resizing_type=fit) | **Crane** | Tap this to cycle between inheriting, locking, or ignoring the up and down movement of its parent. |
| [Roll icon](https://dev.epicgames.com/community/api/documentation/image/47f1e30e-83b8-4006-be49-f8f8d34b784b?resizing_type=fit) | **Roll** | Tap this to cycle between inheriting, locking, or ignoring the roll rotation of its parent. |
| [Tilt icon](https://dev.epicgames.com/community/api/documentation/image/98107aaf-36ef-496f-b435-0a683d283108?resizing_type=fit) | **Tilt** | Tap this to cycle between inheriting, locking, or ignoring the tilt rotation of its parent. |
| [Pan icon](https://dev.epicgames.com/community/api/documentation/image/36f57a90-f6f7-4bd0-b41d-abaca5da272f?resizing_type=fit) | **Pan** | Tap this to cycle between inheriting, locking, or ignoring the pan rotation of its parent. |
| [Iris icon](https://dev.epicgames.com/community/api/documentation/image/e192791c-2e02-4cad-a62d-55412b602ecc?resizing_type=fit) | **Iris** | Tap this to cycle between inheriting, locking, or ignoring the iris camera parameter of its parent. Camera parameters can only be inherited from Cine Camera Rig Rails and Cine Camera Actor parents. |
| [Focal Length icon](https://dev.epicgames.com/community/api/documentation/image/7df36bb0-d398-4277-987c-d6dbb6f05733?resizing_type=fit) | **Focal Length** | Tap this to cycle between inheriting, locking, or ignoring the focal length camera parameter of its parent. Camera parameters can only be inherited from Cine Camera Rig Rails and Cine Camera Actor parents. |
| [Focus Distance icon](https://dev.epicgames.com/community/api/documentation/image/7f71dafa-840d-4edd-9b45-9042057b46ad?resizing_type=fit) | **Focus Distance** | Tap this to cycle between inheriting, locking, or ignoring the focus distance camera parameter of its parent. Camera parameters can only be inherited from Cine Camera Rig Rails and Cine Camera Actor parents. |

### Introducing Lag to the Attachment

If attached to a CineCameraAttachMount, the virtual camera has the additional ability to enable and disable lag into the follow. This allows for more natural feeling movement when following things like cars, where a physical camera would not immediately follow a movement. To toggle lag on and off, tap the lag button in the attach menu.

[![Toggle Lag](https://dev.epicgames.com/community/api/documentation/image/02290d60-e940-4aa7-ae12-a9e3e8000730?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/02290d60-e940-4aa7-ae12-a9e3e8000730?resizing_type=fit)

The speed of this lag can be controlled from the Details panel of the CineCameraAttachMount. Lower Values for Location/Rotation Lag Speed lead to a larger delay in response, while higher values lead to a faster response.

[![Set lag in the Details panel](https://dev.epicgames.com/community/api/documentation/image/9906e7cd-5216-4679-a67f-1adbe662b8dc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9906e7cd-5216-4679-a67f-1adbe662b8dc?resizing_type=fit)

## Creating and Operating Custom Rig Rails

Press the Spline icon in the tools menu to enter Spline Mode. In this mode, the attachment controls in the upper-right change to spline controls. The bottom-left now also includes keyframing controls.

Dolly splines for Virtual Camera are represented by CineCameraRigRail actors. The CineCameraRigRail allows for the creation of spline points which store both transform and camera parameters (Focus, Iris, and Zoom), which can be inherited back to and operated upon by the virtual camera.

[![Creating a Spline point](https://dev.epicgames.com/community/api/documentation/image/113d8b63-7ee3-4387-b4ec-f11f916cca70?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/113d8b63-7ee3-4387-b4ec-f11f916cca70?resizing_type=fit)

### Creating a New CineCameraRigRail

To create a new CineCameraRigRail, ensure the controls are set to the spline selection controls, represented by a spline icon.

[![Select the Spline controls](https://dev.epicgames.com/community/api/documentation/image/06fab365-113c-4f35-b89f-8d673401d499?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06fab365-113c-4f35-b89f-8d673401d499?resizing_type=fit)

This mode offers the following controls:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [Spline Mode Select icon](https://dev.epicgames.com/community/api/documentation/image/b6b291ee-5564-4baf-b9cb-17c90708397c?resizing_type=fit) | Mode | Tapping an option in this segmented control switches the current operating mode between **RigRail** selection mode, **Edit** mode, and **Drive** mode.  In **RigRail** selection mode, the blue spline icon is highlighted. |
| [Active RigRail icon](https://dev.epicgames.com/community/api/documentation/image/2817feb3-d2e0-449d-84f3-5cf052b16387?resizing_type=fit) | Active RigRail | This dropdown indicates the currently selected RigRail. This is the RigRail that is acted upon by all other editing, attachments, and driving tools. To change the current selection, expand the drop-down and select a new RigRail. |
| [New RigRail icon](https://dev.epicgames.com/community/api/documentation/image/31d18bce-c511-4fbe-a844-b3624eb04f57?resizing_type=fit) | New RigRail | Tapping this creates a new RigRail, and sets it to the current selection. |
| [Delete RigRail icon](https://dev.epicgames.com/community/api/documentation/image/def4b86c-7e2b-4d6b-a5b8-aee5a427c66c?resizing_type=fit) | Delete RigRail | Pressing this deletes the currently selected RigRail. To confirm deletion, hold the button until the red time indicator has completed a full circle. Releasing anytime before this cancels the action.  This is a destructive action that fully deletes the CineCameraRigRail from the scene. |
| [Attach icon](https://dev.epicgames.com/community/api/documentation/image/2c1599fd-7b60-4adc-a94c-943ddb58cd03?resizing_type=fit) | Attach | Toggling this attaches/detaches the virtual camera from the currently selected RigRail. |
| [Attach Axes icon](https://dev.epicgames.com/community/api/documentation/image/ddbff53d-8a18-4ea3-babd-c6ccea2e5d18?resizing_type=fit) | Attach Axes | This dropdown offers controls for axis inheritance from the RigRail to the Virtual Camera. |

Tapping the New Rig Rail button creates a new CineCameraRigRail with its first point set with the current transform and camera parameters of the virtual camera. The Controls immediately switch to Editing Mode.

### Editing a CineCameraRigRail

Switching the mode segmented control to the pencil icon switches the controls to Edit Mode. This mode is used to add, remove, and modify points on the currently selected RigRail.

[![Select Edit mode](https://dev.epicgames.com/community/api/documentation/image/0086e036-d517-4697-95d7-b8b4369b6760?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0086e036-d517-4697-95d7-b8b4369b6760?resizing_type=fit)

This mode offers the following controls:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [Edit Mode Select icon](https://dev.epicgames.com/community/api/documentation/image/a624d75c-9761-4b58-a19a-59f926f55ccd?resizing_type=fit) | Mode | Tapping an option in this segmented control switches the current operating mode between **RigRail** selection mode, **Edit** mode, and **Drive** mode.  In **Edit** mode, the blue pencil icon is highlighted. |
| [Current Point icon](https://dev.epicgames.com/community/api/documentation/image/15f193a6-1197-4463-ba83-95a5dd9f67b0?resizing_type=fit) | Current Point | This stepper displays the current position of the mount along the spline and the current point of editing. Tapping the forward and backward arrow jumps to the next or previous point, respectively. Interacting with the stepper in any way brings up a slider, which can be used to scrub along the RigRail. |
| [Delete Current Point icon](https://dev.epicgames.com/community/api/documentation/image/46c1faa6-46d2-45e6-b40c-8fdbe31d43ca?resizing_type=fit) | Delete Current Point | Pressing this deletes the currently selected Point. To confirm deletion, hold the button until the red time indicator has completed a full circle. Releasing anytime before this cancels the action. If the icon is grayed out, the current value of the stepper is between points.  This is a destructive action that fully deletes the point. |
| [Add Point icon](https://dev.epicgames.com/community/api/documentation/image/33a54c95-993e-4366-9f70-5d4403011a04?resizing_type=fit) | Add Point | Pressing this adds a new point to the RigRail with the current transform and camera parameters of the virtual camera. The position along spline value ascribed to this point is contextual to your current position value:   * If the current value *n* of the stepper is at the end of the RigRail, the value is *n+1.* * If the current value *n* is at a point and not at the end, the value is between the current value and the next point. For example, if you press this on point 1 when there is a point 2, this creates a point with position 1.5. * If the current value *n* is not at a point, the position value is *n.* |
| [The Update Point icon](https://dev.epicgames.com/community/api/documentation/image/7f149bad-6d08-496d-9348-c670dc4e20b5?resizing_type=fit) | Update Point | Updates the currently selected point using the current transform and camera parameters of the virtual camera. |
| [Attach icon](https://dev.epicgames.com/community/api/documentation/image/ba89c4bf-23a9-4986-b7e3-2561d2ddb63b?resizing_type=fit) | Attach | Toggling this attaches/detaches the virtual camera from the currently selected RigRail. |
| [Attach Axes icon](https://dev.epicgames.com/community/api/documentation/image/f0850080-05ae-4e5e-9c4b-28ff79a5ea24?resizing_type=fit) | Attach Axes | This dropdown offers controls for axis inheritance from the RigRail to the Virtual Camera. |

To create a RigRail, move the virtual camera to a position and add a point to the RigRail at that transform and with those camera parameters. Repeat this process for every point along the rail.

After completing the RigRail, tap the car icon to enter Drive mode.

### Riding and Driving a CineCamera RigRail

Switching the mode segmented control to the pencil icon switches the controls to Edit Mode. This mode is used to drive the RigRail mount movement and differs from the other two modes in that it uses the dials in addition to the spline controls.

[![Creating a Custom RigRail](https://dev.epicgames.com/community/api/documentation/image/a77746c4-66b2-49b9-a62f-77b725645d74?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a77746c4-66b2-49b9-a62f-77b725645d74?resizing_type=fit)

Drive Mode offers 3 drive modes for controlling the RigRail, selected by the right dial:

* **Manual:** Manual modeis used to drive RigRail by hand. When in this mode, drag the left dial to scrub the position along the rail. Manual mode should also be used if the position is being driven by hardware input or by sequencer.
* **Duration:** Duration modedrives the RigRail automatically to complete the full path within the set amount of time. When in this mode, a second right dial appears. Use this dial to set the desired amount of time for the completion of one full path.
* **Speed:** Speed modedrives the RigRail automatically to move at a set speed. When in this mode, a second right dial appears. Use this dial to set the desired speed (measured in cm/s). To speed up or slow down the RigRail, turn this dial while in motion.

Regardless of the mode selected, you can use the RigRail controls in the top-right to manage the attachment and to offer transport controls for the two automatic drive modes.

The available options are:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [Drive Mode Select icon](https://dev.epicgames.com/community/api/documentation/image/b00b1aef-fa8b-454f-b6ea-95407ed12fc7?resizing_type=fit) | Mode | Tapping an option in this segmented control switches the current operating mode between **RigRail** selection mode, **Edit** mode, and **Drive** mode.  In **Drive** mode, the blue car icon is highlighted. |
| [Back to Start icon](https://dev.epicgames.com/community/api/documentation/image/5c78ce7d-9053-4210-942d-84ec8ad1d32b?resizing_type=fit) | Back to Start | Tap this to reset the current position along the RigRail back to the first point. |
| [Play and Reverse Play icon](https://dev.epicgames.com/community/api/documentation/image/7231e32a-55e8-4938-a911-7c50ce26e1a0?resizing_type=fit) | Play and Reverse Play | These controls are only available in speed and duration modes. To make the mount move forward along the RigRail, tap the forward arrow. To make the mount move backward along the RigRail, tap the back arrow. The speed of the movement is determined by your current drive mode and settings.  While moving in either direction, the respective arrow changes to a pause icon. Tap this to pause the mount at its current position. |
| [Loop icon](https://dev.epicgames.com/community/api/documentation/image/063cf51c-9015-4b78-b12c-3be0eaee0d85?resizing_type=fit)  [The bouncing icon](https://dev.epicgames.com/community/api/documentation/image/d6be2ab1-10c3-46bc-a130-55e398d778e5?resizing_type=fit) | Loop | Tap this to cycle between looping, not looping, and bouncing the spline. When looping, the spine returns to its start upon completion and continues moving according to your drive mode.  When bouncing, the spline plays forward to the end, reverses direction to play backward, and repeats. |
| [Attach icon](https://dev.epicgames.com/community/api/documentation/image/b8444adf-6fa7-45fa-89a6-04b58b5228e7?resizing_type=fit) | Attach | Toggling this attaches/detaches the virtual camera from the currently selected RigRail. |
| [Attach Axes icon](https://dev.epicgames.com/community/api/documentation/image/27249751-a883-4b9c-b02e-d323a3add014?resizing_type=fit) | Attach Axes | This dropdown offers controls for axis inheritance from the RigRail to the Virtual Camera. |

### Using Cine Camera Rig Rails with Sequencer

When in Spline Mode, an additional set of controls in the bottom-left appears, which you can use for keyframing in Sequencer. You can add and remove keyframes for the Rig Rail mount manually or through autokey. Keyframing the Rig Rail mount position allows for specific positions along the Rig Rail to be tied to frames of the current sequence. Playing a level sequence with keyframes for a Rig Rail causes the mount to move according to the keyed positions. To prevent conflicting attempts to drive the rail, the Rig Rail should be either in Manual mode or should have speed/duration modes paused.

[![Using RigRail with Sequencer](https://dev.epicgames.com/community/api/documentation/image/906a5058-fbf4-4e5c-806a-06ccf6eb74a4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/906a5058-fbf4-4e5c-806a-06ccf6eb74a4?resizing_type=fit)

The color of the timeline indicates the relative speed that the mount moves during that portion of the sequence. Red indicates the fastest segments, gradienting to green for the slowest segments. A blue color indicates that the mount is stationary

The available keyframing commands are:

| Icon | Dial Name / Action | Description |
| --- | --- | --- |
| [Autokey icon](https://dev.epicgames.com/community/api/documentation/image/601066e3-b01d-4d07-9c3e-3281bd3a8ef0?resizing_type=fit) | Autokey | Tap this to toggle autokey on and off.  When autokey is enabled, any new points added to the Rig Rail keys the respective position of the mount into sequencer at the current frame. Removing a point along the rail removes its respective keyframe. |
| [Remove Keyframe icon](https://dev.epicgames.com/community/api/documentation/image/029f2eea-a463-4bc8-b3ec-abd568c02f6c?resizing_type=fit) | Remove Keyframe | Tap this to remove the keyframe at the current playhead position. To confirm removal, hold the button until the red time indicator has completed a full circle. Releasing anytime before this cancels the action. If the icon is grayed out, the sequencer playhead is not on a Rig Rail keyframe. |
| [Add Keyframe icon](https://dev.epicgames.com/community/api/documentation/image/2bf47222-dce8-49b0-abfe-adfd68c00d49?resizing_type=fit) | Add Keyframe | Tap this to add a new keyframe to the open level sequence. This keyframe is placed at the playhead position and uses the current mount position as indicated on the drive mode dial or the Rig Rail controls. |

## Virtual Camera Bookmarks

To create a new **VPBookmark** actor in the scene, press the green **Bookmark** icon in the top-left of the screen on your Live Link-enabled device. This actor stores information about the virtual camera, including its position and rotation. The bookmark also stores any settings that have been adjusted for the camera, for example, the exposure and lens settings.

You can reload any placed bookmark by using the Bookmark navigation controls in the bottom-left of the screen using the forward and backwards arrows, or by tapping the bookmark drop down and choosing a bookmark from the list. Toggle the **Camera** icon to load the camera parameters stored with this bookmark, such as the aperture, filmback, and focus settings.

Use the **Minus** (-) icon to remove a currently referenced bookmark from the Live Link-enabled device. Because bookmarks exist as an actor in your Unreal Engine scene, you can also add and remove them manually from the Editor using the **Outliner** panel.

### Bookmark Browser

You can also use the Bookmark Browser to list and manage VPBookmark actors in the scene. You can launch Bookmark Browser from the bookmark icon in the right ear menu, or from the bookmark name in the bookmark selector in the top left side of the viewport.

[![Bookmark ear menu icon](https://dev.epicgames.com/community/api/documentation/image/0b7c644b-edf8-48d8-9280-786149adef07?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b7c644b-edf8-48d8-9280-786149adef07?resizing_type=fit)

[![The bookmark selector in the viewport](https://dev.epicgames.com/community/api/documentation/image/835d0010-ea69-4bd3-a4ef-3e278b5f9d69?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/835d0010-ea69-4bd3-a4ef-3e278b5f9d69?resizing_type=fit)

The VPBookmark Actors are listed in the tile view:

[![The Bookmark Browser](https://dev.epicgames.com/community/api/documentation/image/bab9852f-cd4f-4ef0-8c33-454a6d2da5f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bab9852f-cd4f-4ef0-8c33-454a6d2da5f2?resizing_type=fit)

#### Loading a bookmark

To open a bookmark, tap the thumbnail for an entry to jump to the bookmark. Once you have opened a bookmark, you have several options.

#### Tagging bookmarks

| Icon | Description |
| --- | --- |
| [Bookmark swipe right options](https://dev.epicgames.com/community/api/documentation/image/d1abf063-35f7-4b0d-8058-a7153f756ccf?resizing_type=fit) | Swipe to the right to add stars. |
| [Bookmark swipe left options](https://dev.epicgames.com/community/api/documentation/image/98fd8fa3-38d2-4848-a469-cd2384d350c2?resizing_type=fit) | Swipe to the left to either add a flag tag, or delete the bookmark. |

#### Renaming bookmarks

To rename bookmarks, in the LiveLinkVCam app, tap and hold an entry to activate text input and type the new name.

#### Filtering and sorting bookmarks

The filtering and sorting options are displayed in the top part of the bookmark browser. Once you’ve expanded the Filter button, further options appear.

[![Bookmark Browser filtering and sorting](https://dev.epicgames.com/community/api/documentation/image/8b87f60b-414b-4c76-b58b-3e6a0873ed40?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8b87f60b-414b-4c76-b58b-3e6a0873ed40?resizing_type=fit)

| Icon | Description |
| --- | --- |
| [Bookmark search filter](https://dev.epicgames.com/community/api/documentation/image/463d7be7-1e2a-4d72-ad26-da7dec0cf367?resizing_type=fit) | Type in the search field to filter bookmarks with matching words or strings. |
| [Bookmark flag filter](https://dev.epicgames.com/community/api/documentation/image/a38f6c54-62a2-4b05-ac27-3f9b3d3179e1?resizing_type=fit) | Tap the flag icon to list only bookmarks that are flagged. |
| [Bookmark star filter](https://dev.epicgames.com/community/api/documentation/image/3d909728-314c-4956-8194-63aa65b428c7?resizing_type=fit) | Tap the star icon to cycle between showing only bookmarks tagged with a number of stars greater than the number shown. For example, tapping until the star displays the number 2 shows only bookmarks with 2 or 3 stars. |
| [Bookmark time filter](https://dev.epicgames.com/community/api/documentation/image/baae3da8-45a4-47e0-ba62-6b43a8af2dbb?resizing_type=fit) | Tap this to cycle between sorting the bookmarks newest to oldest or oldest to newest. The list can only be sorted by creation date or alphabetically. |
| [Bookmark alphabetical filter](https://dev.epicgames.com/community/api/documentation/image/0766723e-afd5-4627-8f5d-cb416964fbae?resizing_type=fit) | Tap this to cycle between sorting the bookmarks in alphabetical or reverse alphabetical order. The list can only be sorted by creation date or alphabetically. |

#### Other Options

Tap the gear icon to open the settings menu for the bookmark, which opens the following options:

[![Bookmark Browser settings](https://dev.epicgames.com/community/api/documentation/image/7df0930e-3f80-482d-87f1-3088dcede15f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7df0930e-3f80-482d-87f1-3088dcede15f?resizing_type=fit)

| Icon | Description |
| --- | --- |
| [Bookmark store camera parameters](https://dev.epicgames.com/community/api/documentation/image/65528749-65fe-45db-bd9e-161d4d300eb9?resizing_type=fit) | Bookmarks store camera parameters, including aperture and focal length. You can use this setting to determine if those stored camera parameters should be restored when jumping to a bookmark. |
| [Bookmark refresh thumbnails](https://dev.epicgames.com/community/api/documentation/image/5d2731a9-4065-4733-a454-d22504649ca4?resizing_type=fit) | Tap to refresh all thumbnails. |

### Controlling a Sequence

When a **Sequence** is open in the Unreal Editor, you can control the timeline and playback of it using the **Transport** buttons on your Live Link-connected device. You can use the playback controls for **Play**, **Pause**, and the **Scrub** marker on the timeline to observe the current Sequence's data.

### Using Take Recorder with Unreal VCam App

You can use **Take Recorder** to record your own Sequences (or shots) of the scene and characters in your Unreal Engine project. These can be played back within Unreal Editor using the Take Recorder and Sequencer for review.

To start recording a shot, tap the **Record** button in the top-right of the Unreal VCam app.

When you use Take Recorder with the Unreal VCam app, be aware of these things:

* The **Take Recorder** window automatically opens in Unreal Engine (if not already open) when a recording is started.
* When you start a recording, the current Level Sequence plays automatically.
* After recording a take, you can click **Review the last recording** button in the Take Recorder window to see the shot. This plays back the shot and hides the virtual camera HUD. Exiting review mode unhides the virtual camera HUD.
* All recorded takes are saved as **Sequencer Clips**. Saving the clip replaces the Virtual Camera actor with a [Cine Camera actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine), since virtual cameras are used to animate the camera and record its settings and movements.

When the Virtual Camera is active, it displays the current **Timecode**, **Slate**, and **Sequence Frame** in the HUD. This data is derived from the Take Recorder window, and displays the same information across the Unreal Editor and the Live Link-connected device.

For more information about using Take Recorder in a project, see:

* [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine)
* [Using Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/record-gameplay-in-unreal-engine)
* [Multi-User Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-take-recorder-in-unreal-engine)

In previous releases, the VCam actor used a separate CineCameraActor for recording, rather than recording on the VCam actor itself. If you prefer the previous workflow with the record camera, you can enable **Use Legacy Record Camera Workflow** in the following modifiers, and re-activate VCam.

[![The VCam actor](https://dev.epicgames.com/community/api/documentation/image/71d7947e-ce81-4b0d-8673-1c8d26bb71d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/71d7947e-ce81-4b0d-8673-1c8d26bb71d0?resizing_type=fit)

## VCam Photos

When using VCam, you can create a photo any time you create a bookmark.

When this mode is enabled in the Project Settings, the bookmark icon is replaced with a DSLR camera icon.

[![](https://dev.epicgames.com/community/api/documentation/image/b8a222c7-a275-4981-b2a5-47555824ef45?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8a222c7-a275-4981-b2a5-47555824ef45?resizing_type=fit)

The bookmark icon

[![](https://dev.epicgames.com/community/api/documentation/image/b9f5342c-a401-4bb3-8014-92dc2437ab42?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9f5342c-a401-4bb3-8014-92dc2437ab42?resizing_type=fit)

The DSLR camera icon

In the **Project Settings**, under **Plugins** > **Virtual Camera**, you can set the **Photo Save Mode** to save a texture asset, a PNG, or both. You can also disable it to prevent creating any photos when you create a bookmark. In this same window, you can set the desired destination for the assets or leave the default values.

[![The Photo Save Mode options](https://dev.epicgames.com/community/api/documentation/image/af53f30b-efa1-42f4-8d75-8661304bd845?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af53f30b-efa1-42f4-8d75-8661304bd845?resizing_type=fit)

You can change the size of the photos that get saved. In the **Details** panel for the VCam component, go to **Photo Modifier** > **Photo Settings**. Set **VcamPhoto Size Settings** to **1920**, **3840**, **Match Output**, or **Custom**. The saved Photos are cropped to match the VCam frame.

[![The VCam Photo Size Settings options](https://dev.epicgames.com/community/api/documentation/image/ecb055ed-4c43-4c56-85fb-bdf0f60e1aaa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ecb055ed-4c43-4c56-85fb-bdf0f60e1aaa?resizing_type=fit)

This setting indicates the highest dimension of the image. The other dimension is determined by the filmback currently being used. When you select **Custom**, you can set the **Custom Photo Size** to any value. Custom values over 4000 may take longer to process.

VCam photos are saved to the `Content/VCamPhotos` folder.

[![The VCamPhotos folder](https://dev.epicgames.com/community/api/documentation/image/9b0d9567-8a9b-42c8-a13a-0c55496a3a94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b0d9567-8a9b-42c8-a13a-0c55496a3a94?resizing_type=fit)

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [virtual camera](https://dev.epicgames.com/community/search?query=virtual%20camera)
* [working with media](https://dev.epicgames.com/community/search?query=working%20with%20media)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Virtual Camera Movement with Scale and Gain Settings](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#virtual-camera-movement-with-scale-and-gain-settings)
* [Browsing for Sequences and Reviewing Takes](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#browsing-for-sequences-and-reviewing-takes)
* [Takes Browser](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#takes-browser)
* [Tagging Takes](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#tagging-takes)
* [Filtering and Ordering the Takes Browser](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#filtering-and-ordering-the-takes-browser)
* [Take Viewer](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#take-viewer)
* [Tagging Takes](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#tagging-takes)
* [Smoothing Takes](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#smoothing-takes)
* [Navigating Takes With Carousel View](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#navigating-takes-with-carousel-view)
* [Open Takes Browser](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#open-takes-browser)
* [Teleporting](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#teleporting)
* [Sequencer and Bookmarks Settings](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#sequencer-and-bookmarks-settings)
* [Virtual Camera Stabilization](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#virtual-camera-stabilization)
* [Parenting and Platforming](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#parenting-and-platforming)
* [Creating an Attach Mount](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#creating-an-attach-mount)
* [Selecting and Attaching to a Parent](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#selecting-and-attaching-to-a-parent)
* [Inheriting Specific Axes and Camera Parameters](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#inheriting-specific-axes-and-camera-parameters)
* [Introducing Lag to the Attachment](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#introducing-lag-to-the-attachment)
* [Creating and Operating Custom Rig Rails](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#creating-and-operating-custom-rig-rails)
* [Creating a New CineCameraRigRail](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#creating-a-new-cine-camera-rig-rail)
* [Editing a CineCameraRigRail](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#editing-a-cine-camera-rig-rail)
* [Riding and Driving a CineCamera RigRail](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#riding-and-driving-a-cine-camera-rig-rail)
* [Using Cine Camera Rig Rails with Sequencer](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#using-cine-camera-rig-rails-with-sequencer)
* [Virtual Camera Bookmarks](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#virtual-camera-bookmarks)
* [Bookmark Browser](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#bookmark-browser)
* [Loading a bookmark](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#loading-a-bookmark)
* [Tagging bookmarks](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#tagging-bookmarks)
* [Renaming bookmarks](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#renaming-bookmarks)
* [Filtering and sorting bookmarks](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#filtering-and-sorting-bookmarks)
* [Other Options](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#other-options)
* [Controlling a Sequence](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#controlling-a-sequence)
* [Using Take Recorder with Unreal VCam App](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#using-take-recorder-with-unreal-v-cam-app)
* [VCam Photos](/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine?application_version=5.7#vcamphotos)
