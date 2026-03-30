<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7 -->

# Cinematic Shortcuts and Tips

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
7. Cinematic Shortcuts and Tips

# Cinematic Shortcuts and Tips

Tips, tricks, and shortcuts for your cinematic workflow.

![Cinematic Shortcuts and Tips](https://dev.epicgames.com/community/api/documentation/image/ba3cade3-4ee4-4ed8-b4c0-b21d75d5e4d6?resizing_type=fill&width=1920&height=335)

 On this page

To improve your cinematic animation productivity, several shortcuts have been built into the Sequencer Editor. This document provides tips for common workflows, overcoming problems, and other helpful features of Sequencer.

## Playback

### Spacebar Playback Toggle

By default, using the **Space Bar** as a hotkey to toggle playback of your sequence only works if your window focus is on Sequencer. If your focus is on the Viewport, then pressing the Space Bar will instead cycle between transform manipulation modes.

You can make the Space Bar toggle playback of Sequencer regardless of window focus by following these steps:

1. Open the [Editor Preferences](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-preferences) window and locate **Cycle Between Translate, Rotate, and Scale** under **General > Keyboard Shortcuts**. Unbind this shortcut by clicking **Remove this binding (X)**.

   [![unbind space bar hotkey](https://dev.epicgames.com/community/api/documentation/image/d27e0460-df84-47d6-b5cb-8c110eff5cd5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d27e0460-df84-47d6-b5cb-8c110eff5cd5?resizing_type=fit)

   You will still be able to use hotkeys to switch between these transform modes by pressing **Q**, **W**, **E**, and **R** to enable **Select**, **Translate**, **Rotate**, and **Scale**, respectively.
2. From the Viewport's **Perspective** menu, enable [Cinematic Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-viewport-controls-in-unreal-engine).

   [![enable cinematic viewport](https://dev.epicgames.com/community/api/documentation/image/537e0ec9-27e3-4fbe-9a4c-5f1785028ad3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/537e0ec9-27e3-4fbe-9a4c-5f1785028ad3?resizing_type=fit)
3. Now you can press the **Space Bar** while your focus is on either the Sequencer or the Cinematic Viewport, and the playback will toggle correctly.

   [![spacebar playback toggle](https://dev.epicgames.com/community/api/documentation/image/4cc93a17-fa8a-499a-abd4-689211526f4b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4cc93a17-fa8a-499a-abd4-689211526f4b?resizing_type=fit)

### Inclusive and Exclusive Frames

Animation within Unreal Engine uses the concepts of "inclusive" and "exclusive" frames, which determine if a full frame is being included or evaluated fully. Typically this matters when defining **start** and **end frames** in your sequence, such as for [animations](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine), [shots](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine), or overall Sequencer playback times.

For Sequencer, the start frame is inclusive and the end frame is exclusive, which causes all frame data up to the end frame to be evaluated. In this example, where the start time is set to **0**, and the end time is set to **10**, this means that the actual elapsed time is **9.999** (repeating) frames. In other words, it evaluates up to, but not completely to, the end time. This mimics behavior seen in most non-linear editing software such as Adobe Premiere.

[![sequencer exclusive frame](https://dev.epicgames.com/community/api/documentation/image/523967be-ebd1-441d-8404-0921f20c7e20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/523967be-ebd1-441d-8404-0921f20c7e20?resizing_type=fit)

Because of this functionality, you can expect the following behavior:

* If [Keep Cursor in Playback Range While Scrubbing](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) is enabled, then it should be impossible to scrub or view the exact end frame in a sequence. While data can exist on that frame, Sequencer will never reach it. In this example, the end time is **0346** frames, but playback only reaches **0345\*** .

  [![](https://dev.epicgames.com/community/api/documentation/image/17e1fa17-8c9e-4fa2-a5b5-b4525f69476d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17e1fa17-8c9e-4fa2-a5b5-b4525f69476d?resizing_type=fit)
* If the Playhead is at the same point where two sections touch, such as shots, then the data from the next shot will be shown instead of the previous shot.

  [![](https://dev.epicgames.com/community/api/documentation/image/8fb75dbf-59a7-4fbb-8c1c-bcfc942fea91?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8fb75dbf-59a7-4fbb-8c1c-bcfc942fea91?resizing_type=fit)
* When rendering image sequences with [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue), the end frame will be excluded. This means that if your sequence contains frames **0 - 50**, the image sequence will output frames **0 - 49**.

  [![](https://dev.epicgames.com/community/api/documentation/image/0ad1c064-ecfb-404e-afd9-e507cd1e71f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ad1c064-ecfb-404e-afd9-e507cd1e71f2?resizing_type=fit)

Sequencer's treatment of inclusive and exclusive frames differs from [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine), which includes both start and end frames. When an animation FBX is imported, Unreal Engine will include a small amount of data beyond the final frame, which causes the final frame to be fully included. This can be observed in Sequencer if you zoom in far enough on the end of an unedited Animation Section.

[![animation sequence inclusive](https://dev.epicgames.com/community/api/documentation/image/e0114b06-0869-4f46-85a7-39856743dfd4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0114b06-0869-4f46-85a7-39856743dfd4?resizing_type=fit)

However, trimming, and other [section editing](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine) operations on the animation will restore Sequencer's end frame exclusive behavior.

## Workflow Shortcuts

### Middle-Mouse Scrubbing

Similar to Autodesk Maya, you can change your current time without causing updates or evaluations to occur by clicking and dragging the **middle mouse button** in the timeline. This can be useful when you want to set additional bracketing keyframes at the same value but at different times. When manipulating the playhead in this way, it will change its color to **yellow** to indicate the sequence is not evaluating.

[![middle mouse scrub](https://dev.epicgames.com/community/api/documentation/image/2e24f221-7fc1-40d6-8198-1e1b7c455a60?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e24f221-7fc1-40d6-8198-1e1b7c455a60?resizing_type=fit)

### Adding Actors to Sequencer

When dragging new Actors into your Level from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) or by [placing Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine), pressing certain keys will also add them to Sequencer. Depending on the pressed key, it will add the Actor as either a [spawnable or possessable](https://dev.epicgames.com/documentation/en-us/unreal-engine/spawn-temporary-actors-in-unreal-engine-cinematics?application_version=5.5).

* Holding **Ctrl** will add the new actor to Sequencer as a possessable.
* Holding **Shift** will add the new actor to Sequencer as a spawnable.

### Default Tracks

When adding certain Actors to Sequencer, you may notice that tracks are automatically created with them. For example:

* **[Static Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine)** will automatically create a [Transform Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine).

  [![static mesh sequencer auto track](https://dev.epicgames.com/community/api/documentation/image/69c97169-46c3-4757-a6b3-822743a5d0d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69c97169-46c3-4757-a6b3-822743a5d0d0?resizing_type=fit)
* **[Skeletal Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine)** will automatically create a [Transform Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine) and an **[Animation Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine)**.

  [![skeletal mesh sequencer auto track](https://dev.epicgames.com/community/api/documentation/image/9d4be243-1dca-49ca-8320-16a2a89cdf7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d4be243-1dca-49ca-8320-16a2a89cdf7a?resizing_type=fit)
* **[Cine Camera Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)** will automatically create a [Transform Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine) and a **Camera Component** with **Aperture**, **Focal Length**, and **Focus Distance** property tracks.

  [![camera actor sequencer auto track](https://dev.epicgames.com/community/api/documentation/image/37fd134c-4036-4150-841e-0d2931ac62e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/37fd134c-4036-4150-841e-0d2931ac62e7?resizing_type=fit)
* **[Light Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine)** will automatically create a **Light Component** with **Intensity** and **Light Color** property tracks.

  [![lights sequencer auto track](https://dev.epicgames.com/community/api/documentation/image/acafaeac-584a-4556-a389-a4755c53961e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acafaeac-584a-4556-a389-a4755c53961e?resizing_type=fit)

This occurs because of the **Tracks Settings** located in the [Sequencer Plugins Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine). You can locate these settings by opening the **Project Settings** window, and locating **Level Sequencer** in the **Plugins** category.

[![sequencer track settings](https://dev.epicgames.com/community/api/documentation/image/494d01a5-5dce-426b-97ca-6b57155311b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/494d01a5-5dce-426b-97ca-6b57155311b4?resizing_type=fit)

The **Track Settings** array is populated by default with settings for the previously mentioned tracks. You can click the **Add (+)** button to add a new array item, and each array has the following categories:

[![add track setting](https://dev.epicgames.com/community/api/documentation/image/cd60bb81-c9a4-4c3b-b5f4-0402065a99e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd60bb81-c9a4-4c3b-b5f4-0402065a99e9?resizing_type=fit)

| Name | Description |
| --- | --- |
| **Matching Actor Class** | This is where you specify the Actor class to automatically create tracks for when adding it to Sequencer.  [matching actor class](https://dev.epicgames.com/community/api/documentation/image/eefa2b71-4383-43f1-904e-aa6fe1c0f204?resizing_type=fit) |
| **Default Tracks** | This array is where you specify the tracks that are added when the **Matching Actor Class** is added to Sequencer. Click the **Add (+)** button and click the dropdown menu to browse **Sequencer's** track types.  [default tracks](https://dev.epicgames.com/community/api/documentation/image/3e2eef31-19db-46d4-b824-9b4858f07b5a?resizing_type=fit) |
| **Exclude Default Tracks** | This array is where you specify tracks you don't want added for this Actor class. You may want to use this if you are specifying different tracks to add, such as when your class is inheriting from a parent class which also has its default tracks specified here. |
| **Default Property Tracks** | This array is where you specify the property tracks that are added when the Actor is added to Sequencer. Click the **Add (+)** button to add a new property item to the array.  [default property tracks](https://dev.epicgames.com/community/api/documentation/image/6ab5f728-a5c1-47eb-b4dc-ec7dd0b74753?resizing_type=fit)   * **Component Path** is where you specify the Actor's component you want to add the property from. * **Property Path** is where you specify the property name you want to automatically add. |
| **Exclude Default Property Tracks** | This array is where you specify property tracks you don't want added for this Actor class. You may want to use this if you are specifying different tracks to add, such as when your class is inheriting from a parent class which also has its default property tracks specified here. |

### Auto Size Shots

When adjusting start and end times of shots internally, you can automatically match the parent shot section to these edits using the **Auto Size** command. To do this, right-click the shot and select **Edit > Auto Size**. This can be useful if you are retiming your shot and want the shot section to match, without needing to re-trim manually.

### Shift Snapping and Alignment

When dragging section assets onto Sequencer tracks, such as [audio](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-audio-track-in-unreal-engine), [subsequence](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-subscequences-track-in-unreal-engine), or [animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine) tracks, holding **Shift** will snap the dropped section to the Playhead location.

[![shift dragging](https://dev.epicgames.com/community/api/documentation/image/cbd8f241-7c96-43d0-a0f7-b5b1010dada4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cbd8f241-7c96-43d0-a0f7-b5b1010dada4?resizing_type=fit)

If **Snap to the Pressed Key** is disabled, you can still align the Playhead to keyframes by holding **Shift** and clicking the keyframe. This makes it easy to perform subsequent actions, such as changing the value of this keyframe, or aligning other keys to it.

[![shift alignment](https://dev.epicgames.com/community/api/documentation/image/32723209-ff2a-4509-83d7-9f050696a179?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32723209-ff2a-4509-83d7-9f050696a179?resizing_type=fit)

## Workflow Tips

### Ultrawide Monitor Framing

When making cinematics with unconstrained aspect ratios, you may encounter situations where your shot composition can change if a monitor's aspect ratio differs greatly from the aspect ratio you originally intended. For example, if you created the following shot in a cinematic:

[![](https://dev.epicgames.com/community/api/documentation/image/0a50dff9-299b-46e0-8c8d-d9ea4cb8b233?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a50dff9-299b-46e0-8c8d-d9ea4cb8b233?resizing_type=fit)

Then, if this shot was played on an ultrawide monitor, the drastic change in aspect ratio may severely disrupt the original framing.

[![](https://dev.epicgames.com/community/api/documentation/image/6c6ff67b-22fe-40f3-804a-2e6552230371?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c6ff67b-22fe-40f3-804a-2e6552230371?resizing_type=fit)

In this situation, where maintaining the vertical framing is important, you can resolve this by navigating to the **Level Sequence Actor's Details** and do the following:

* Enable **Override Aspect Ratio Axis Constraint**.
* Set **Aspect Ratio Axis Constraint** to **Maintain Y-Axis FOV**.

[![](https://dev.epicgames.com/community/api/documentation/image/a7a3efcd-9c9f-40d7-97bf-9e8a30384787?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7a3efcd-9c9f-40d7-97bf-9e8a30384787?resizing_type=fit)

Once done, your vertical frame-space is constrained, maintaining the framing on these characters no matter the aspect ratio.

[![](https://dev.epicgames.com/community/api/documentation/image/1e2551fe-f561-4f00-8205-9c7660c3f348?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e2551fe-f561-4f00-8205-9c7660c3f348?resizing_type=fit)

## Warm-Up Rendering

When creating pre-rendered sequences with [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) (MRQ), it may be necessary to "warm up" each shot in order for various aspects of your scene to render correctly. For example, some common problems can be:

* Particles and other effects activating at the start of the shot, instead of already being active.
* Cloth and other physics-driven entities exhibit a noticeable "settle" at the start of the shot.
* The first rendered frame of a shot can exhibit noticeable aliasing or other temporal artifacts (sparkles).

You can use various warm-up properties within Movie Render Queue's [Anti-Aliasing Render Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) to resolve these scenarios. Depending on the scenario, there may also be different considerations to take into account that will determine which settings are best to use.

### Particles

In some cases, you may want particles and other effects to be active for a certain duration of time before a shot begins. While real-time previewing might show the correct behavior, rendering with MRQ may cause your particle system to activate at the start of the shot, which is undesirable.

|  |  |
| --- | --- |
|  |  |
| Particle with no warm-up | Particle with warm-up |

For this particle scenario, you can resolve it in either of the following ways:

* Create the particle's Activate keyframe at the start time of your shot, then set a frame value on **Engine Warm Up Count**. This value can be arbitrary depending on how many frames are needed for your particle to warm up.

  [![](https://dev.epicgames.com/community/api/documentation/image/223e8a17-8e46-4ec0-a68d-4398e36b8e50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/223e8a17-8e46-4ec0-a68d-4398e36b8e50?resizing_type=fit)
* Or, you can create or move the particle's Activate keyframe to the **pre-start** region of the sequence, along with the [Camera Cut](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine) section. Then, enable **Use Camera Cut for Warm Up**. This will cause the warm-up time to be defined by the pre-start area that the Camera Cut track section occupies.

  [![](https://dev.epicgames.com/community/api/documentation/image/4be571d6-95c9-470f-bfff-e93488f604d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4be571d6-95c9-470f-bfff-e93488f604d5?resizing_type=fit)

If your particle is **GPU-based**, then you will also need to enable **Render Warm Up Frames**.

[![render warm up frames](https://dev.epicgames.com/community/api/documentation/image/e5891dab-d171-43df-ad85-1eb553e6647f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5891dab-d171-43df-ad85-1eb553e6647f?resizing_type=fit)

### Cloth and Physics

For cloth and other physics objects, a common problem when rendering is that they can exhibit a noticeable settle at the start of a shot. This is due to the game simulation not starting until the rendering begins, therefore physics needs time to settle to its true simulated state.

|  |  |
| --- | --- |
|  |  |
| Cloth settles at start (no warm-up) | No cloth settling (with warm-up) |

#### No Starting Motion

For shots where the character or physics object is not initially moving, such as being in an idle pose, you can fix this by setting a frame value on **Engine Warm Up Count**. This value can be arbitrary depending on how many frames are needed for your physics to settle. Typically, a value greater than 30 should be used.

[![engine warm up count](https://dev.epicgames.com/community/api/documentation/image/46a22cff-5951-447c-b73b-49789190eb8a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46a22cff-5951-447c-b73b-49789190eb8a?resizing_type=fit)

#### Starting Motion

In scenarios where shots start with the physics object in motion, such as running or jumping, then **Engine Warm Up Count** will not produce an accurate result. This is because it only "warms up" the starting frame and does not take into account motion that may be occurring beforehand. Here you can observe the cloth in the left example starting at an unnatural rest position, then correcting as the simulation reacts to the motion.

|  |  |
| --- | --- |
|  |  |
| Cloth starts at rest (incorrect warm-up settings) | Cloth starts correctly behind (using correct warm-up settings) |

In order to resolve this, you must do the following:

1. Make sure that your physics character or object contains animation data in the pre-start region of Sequencer, including the **Camera Cuts** section. This may require you to alter your animation and transform track keyframes in order to extend it into the pre-start region.

   [![cloth prestart animation](https://dev.epicgames.com/community/api/documentation/image/4a9c8502-78d9-44e4-a798-ea0140c243ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a9c8502-78d9-44e4-a798-ea0140c243ee?resizing_type=fit)

   If you are previewing your shot [in context](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine), then you may want to enable **Evaluate Sub Sequences In Isolation** from Sequencer's [Playback Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) menu. Otherwise, scrubbing into the negative timeline region will preview the previous shot and not the pre-start region of your current shot.
2. In the Anti-Aliasing image settings, enable **Use Camera Cut for Warm Up**. This will cause the warm-up time to be defined by the pre-start area that the Camera Cut track section occupies. This will result in the sequence accumulating the pre-start motion so that the physics state at the start of the shot is accurate. Unlike **Engine Warm Up Count**, which evaluates and holds on the first frame, **Use Camera Cut for Warm Up** will evaluate the sequence leading up to the starting frame.

   [![cloth use camera cut for warm up](https://dev.epicgames.com/community/api/documentation/image/0f6400df-e8a4-42b2-8cc2-a0ebc374af7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f6400df-e8a4-42b2-8cc2-a0ebc374af7c?resizing_type=fit)

This technique can be used to also build a movement history for other things, such as trail particles.

### Temporal Artifacts

Aliasing and other artifacts caused by rendering features that have a temporal component, such as Temporal Anti Aliasing (TAA), Temporal Super Resolution (TSR), or raytracing denoisers, can also occur on the first few frames of your shots. Typically, this issue appears as noticeable hard edges or grainy sparkling on reflective surfaces. This is due to the lack of temporal history being accumulated at the start of a render.

|  |  |
| --- | --- |
|  |  |
| Sparkling and jagged edges (no warm-up) | Smooth edges and highlights (with warm-up) |

To resolve this issue, you can do either of the following:

* Set a frame value for **Render Warm Up Count**. This value will be the number of frames to render beforehand to build a temporal history for the first frame.

  [![temporal warmup settings](https://dev.epicgames.com/community/api/documentation/image/376a0d4c-0937-4aca-aeca-ecbaf9c41338?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/376a0d4c-0937-4aca-aeca-ecbaf9c41338?resizing_type=fit)
* If increasing **Render Warm Up Count** does not resolve the issue, then you can instead increase the **Engine Warm Up Count** value and enable **Render Warm Up Frames**. This will evaluate the first frame of the sequence and then continually tick the engine and renderer until the **Engine Warm Up Count** frames have passed.

  [![temporal warmup settings](https://dev.epicgames.com/community/api/documentation/image/096c2d7b-fde5-458e-b1bb-55b7e8cafa64?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/096c2d7b-fde5-458e-b1bb-55b7e8cafa64?resizing_type=fit)

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [tips](https://dev.epicgames.com/community/search?query=tips)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Playback](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#playback)
* [Spacebar Playback Toggle](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#spacebar-playback-toggle)
* [Inclusive and Exclusive Frames](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#inclusive-and-exclusive-frames)
* [Workflow Shortcuts](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#workflow-shortcuts)
* [Middle-Mouse Scrubbing](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#middle-mouse-scrubbing)
* [Adding Actors to Sequencer](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#adding-actors-to-sequencer)
* [Default Tracks](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#default-tracks)
* [Auto Size Shots](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#auto-size-shots)
* [Shift Snapping and Alignment](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#shift-snapping-and-alignment)
* [Workflow Tips](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#workflow-tips)
* [Ultrawide Monitor Framing](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#ultrawide-monitor-framing)
* [Warm-Up Rendering](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#warm-up-rendering)
* [Particles](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#particles)
* [Cloth and Physics](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#cloth-and-physics)
* [No Starting Motion](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#no-starting-motion)
* [Starting Motion](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#starting-motion)
* [Temporal Artifacts](/documentation/en-us/unreal-engine/cinematic-workflow-tips-for-sequencer-in-unreal-engine?application_version=5.7#temporal-artifacts)
