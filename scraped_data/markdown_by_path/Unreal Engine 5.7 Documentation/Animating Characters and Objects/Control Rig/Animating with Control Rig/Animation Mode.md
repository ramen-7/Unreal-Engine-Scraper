<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7 -->

# Animation Mode

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
6. [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine "Control Rig")
7. [Animating with Control Rig](/documentation/en-us/unreal-engine/animating-with-control-rig-in-unreal-engine "Animating with Control Rig")
8. Animation Mode

# Animation Mode

Enable Animation Mode to provide an animator-friendly workspace and tools in Unreal Engine.

![Animation Mode](https://dev.epicgames.com/community/api/documentation/image/310001eb-b34b-44f6-b2f9-c4420dce6bfe?resizing_type=fill&width=1920&height=335)

 On this page

**Animation Mode** is a [Mode](/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine) in Unreal Engine that exposes new tools, panels, and editor behaviors that assist your animation workflows. Using this Mode when animating with Control Rig offers a more animation-focused editor experience, with tabs to aid in selecting Controls, transform displays, and launching tools.

This document provides an overview of Animation Mode, including its user interface, tools, and settings.

#### Prerequisites

* You have created a **Control Rig Asset**. See the [Control Rig Quick Start](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine) page for information on how to do this.
* Animation Mode is mainly dependent on using Control Rig within Sequencer, therefore a [basic knowledge](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) of Sequencer is required.

## Enabling Animation Mode

Animation Mode can be enabled in the following ways:

1. Dragging a Control Rig Asset from the [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) into a Level. This will create a new [Level Sequence](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine), add the character with a **Control Rig Track**, and enable Animation Mode.

   ![enable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/841ca2b8-399d-4e89-92f7-756ab30dcd49/enable1.gif)
2. Selecting a Control Rig Track in Sequencer.

   ![enable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6d1615c-839d-48dd-baa9-f42c67a862c8/enable2.gif)
3. Manually enabling Animation Mode by clicking the **Mode** dropdown menu and selecting **Animation**. Alternatively, you can also press **Shift + 7**.

   ![enable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ccbbd586-6388-4f63-bae8-24e49dcc9de6/enable3.png)

Animation Mode can be disabled and normal level editing mode restored either by selecting the **Mode** dropdown menu and clicking **Select**, or by pressing **Shift + 1**.

![disable animation mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89a58254-93ff-4ee2-a0dc-4b5ec8041a73/disable.png)

## Animation Mode Overview

Animation Mode is a level editor [Mode](/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine) which contains specialized editing interfaces and workflows. Activating it will add the following panels to the Unreal Editor interface:

![animation mode user interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/309509a8-557c-4734-9e80-c54c715fc5e0/modeoverview.png)

1. The **Animation** panel, which contains [Animation Mode Tools](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#animationmodetools), [Settings](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#animationmodesettings), [Space Switching Controls](/documentation/en-us/unreal-engine/re-parent-control-rig-controls-in-real-time-in-unreal-engine), and [Constraints](/documentation/en-us/unreal-engine/animation-constraint-tools-in-unreal-engine).
2. The **[Anim Outliner](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#animoutliner)**, which is an Outliner modified to only show Controls on the selected Control Rig.
3. **[Anim Details](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#animdetails)**, which is a Details panel modified to only show relevant animatable properties of selected Controls.

### Anim Outliner

The Anim Outliner panel displays all animatable Controls and organizes them according to their hierarchy, as defined in the Control Rig.

![anim outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/caed4c01-bcd3-4f46-8eae-dfece5712c68/outliner.png)

Selecting Controls here will also select them in the Viewport and Sequencer. Inversely, selecting Controls in either the Viewport or Sequencer selects them here, too.

Control icons inherit the [control shape color](/documentation/en-us/unreal-engine/control-shapes-and-control-shape-library-in-unreal-engine#changeshape) of their control, which makes it easier to read the control and match it to the Viewport color.

### Anim Details

The Anim Details panel displays relevant animatable properties for the selected Control, including properties of children channel Controls.

![anim details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ebcf904-9052-433e-af8a-bc160299484f/details.png)

Transform values are relative to the Initial Local / Global values defined on the Control in the Control Rig Asset, therefore, the "zero-point" of these Controls is equal to those values.

Boolean, Float, Integer, and Enum Controls that are children of a selected Control will automatically be selected when selecting the parent, and will display within the Anim Details panel as **Channels**. This way, you can manipulate these Controls at the same time as the parent, and also create custom attributes and channels on a single Control.

## Animation Mode Tools

The Animation panel contains the following tools to aid your animation workflows:

| Name | Icon | Description |
| --- | --- | --- |
| **Select** | select tool | Enabling this will only make Control Rig controls be selectable in the Viewport. All other objects, including the character, will not be selectable. This can also be enabled from the [Animation Settings](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#animationmodesettings) by enabling **Only Select Rig Controls**. |
| **Poses** | poses tool | Opens the [Control Rig Pose Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#posestool). |
| **Tweens** | tweens tool | Opens the [Tween Controller](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#tweenstool). |
| **Snapper** | snapper tool | Opens the [Control Rig Snapper Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#snappertool). |
| **Trails** | motion trails | Opens the [Motion Trail Window](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#motiontrailtool). |
| **Pivot** | pivot tool | Creates a [temporary pivot](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine#pivottool) for alternative Control manipulation. |

### Poses Tool

The Control Rig Pose Tool is a tool that stores and retrieves data on your Controls. You can save the relative pose on selected Controls, adjust the thumbnail icon, and configure your saved pose to apply to symmetrical Controls.

![pose tool interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb8d493f-f65a-4b06-85a6-96f5d3d9d63b/pose1.png)

#### Saving Poses

To save a new pose, first select the Controls you want to include in the pose, then click **Create Pose** in the toolbar. You will then be prompted to name the pose Asset. Enter a name, then click **Create Asset** to create the pose. The new pose will be created within the selected folder.

![create pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9d3e6d7-d958-4df6-b7fc-7b57338a9728/pose2.png)

You can also adjust the Thumbnail by selecting the pose in the browser, changing your Viewport camera, and clicking **Capture Thumbnail**.

![pose tool capture thumbnail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c00779cd-27f7-4816-8ed7-e4e41c9861ab/pose3.gif)

#### Applying Poses

Before applying poses, you must ensure you have the appropriate Controls selected. You can do this either by manually selecting the Controls or by selecting the pose and clicking **Select Controls**, which selects all Controls from that pose.

![pose tool select controls](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/60924ba4-a777-4bb3-ad65-b51678bef19c/pose4.png)

There are several ways you can apply saved poses to your Controls. You can either:

* Double-click the pose from the browser, which will apply the selected pose.

  ![apply saved pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd18e9e3-515c-4c85-abfa-3101ea5628de/applypose1.gif)
* Click **Paste Pose**.

  ![apply pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9110f4ea-892f-4e61-8215-9a561378a357/applypose2.png)
* Manipulate the **Blend Pose Slider**, which will apply the pose partially based on a delta between the current pose of the Controls and the selected Pose. A value of **0** will maintain the current pose, whereas a value of **1** will fully apply the selected pose.

  ![apply pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c48b02dc-93ea-4719-b1ed-e03054ed496e/applypose3.gif)

Enabling the **Key** option will create [Keyframes](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine) when a pose is applied to the selected Controls.

![pose tool keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c59da194-325e-42d5-a999-d8fadc32f98c/keyframe.png)

#### Mirroring Poses

For humanoid and other symmetrical rigs, you can also apply your poses on either side of the line of symmetry. This is done with a combination of namespace searching and axis mirroring and flipping. Enabling the **Mirror** option will apply your saved poses to the other side, ensuring you select the Controls first.

![mirror pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ce92a72-004e-4b4a-8bba-461cea69bb49/mirror1.gif)

By default, the naming convention system assumes **Left** and **Right** are designated as `_l_` and `_r_` respectively. You can change this by editing the **Right Side** and **Left Side** property fields to match your Control Rig's symmetry designation. For example, you may want to change these properties to read as `_left` and `_right` if your symmetry designation is a postfix.

![mirror pose left side right side](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dce226fb-527b-4558-a218-130616f289f9/mirror2.png)

**Mirror Axis** is where you designate the axis of symmetry along your character. In most cases this will remain as **X** if you use a standard **Y - Facing** character in Unreal Engine.

![mirror axis](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/43b35191-a2c0-400d-9c31-432861323ecf/mirror3.png)

**Axis to Flip** is the rotation axis to maintain while inverting the others in order to calculate the mirrored pose. In most cases this should be set to **X**, which is meant to keep rotational **X** values the same, while inverting **Y** and **Z**.

Because of the arbitrary nature of some Control Rigs, you should ensure your Control Rig symmetry is constructed in such a way that it can appropriately comply with axis mirroring and flipping.

#### Additional Controls and Hotkeys

Right-clicking on a pose will expose a context menu with the following commands:

![pose context menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1f27a90-19f0-4592-afdd-b104a5427fee/posecontext.png)

| Name | Description |
| --- | --- |
| **Rename Asset** | Renames the pose. |
| **Save Asset** | Saves the pose. |
| **Delete Asset** | Deletes the pose. |
| **Paste Pose** | Applies the pose to the selected Controls. |
| **Paste Mirror Pose** | Applies the pose to the selected mirrored Controls. |
| **Select Controls** | Selects the Controls defined by the pose. |
| **Update Pose** | Updates the pose based on the currently selected Controls and their pose. |
| **Rename Controls** | Opens a property matrix for changing the names of the saved Controls within a pose. This is useful if you want a pose to apply to a different Control Rig with differently named Controls. |

Holding **Alt** and double-clicking a pose will select the Controls from that pose.

![alt click pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e0c60c9-205c-4ca1-b144-9bc0908161f7/posealtclick.gif)

#### Folder Display

By default, the folder structure for saving and using poses is `Content/ControlRig/Pose`. In cases where you want to save to a different directory, or have imported poses that are not within this default directory, you can add other folders to your pose tool directory.

To do this, right-click in the directory area and select **Add Existing Folder To View**. Select the folder you want to add and click **OK**.

![add existing folder to view](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a44f7b99-01d5-4a88-b505-685038fbc749/posefolder1.png)

The folder, and any poses within, should now display in the pose tool directory.

![add existing folder to view](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/223b4888-66e0-4abd-b29c-f02acdc75986/posefolder2.png)

### Tweens Tool

The Tweens Tool can be used to adjust the interpolation between selected keyframes or their neighbors in a variety of ways.

![tweens tool controller](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7137f0ef-1641-4895-ad1d-7159f3070a56/tweens1.png)

With the **Tween Controller** open, select your keyframed Controls and ensure your playhead is between two keyframes. Manipulate the Tween Controller value by either dragging the slider or typing in a value between **-1** and **1**. A value of **-1** will cause the new in-between keyframe to match the value of the preceding keyframe, whereas a value of **1** will match the next keyframe's value.

![tween controller edit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6d66f34-781c-4343-97f7-fc16a066202e/tweens2.gif)

The Tween Controller has several modes for adjusting the in-between keyframe available in the Tween tool dropdown menu.

| Tween Mode | Description |
| --- | --- |
| **Blend to Neighbor (BN)** | Moves the key to the previous (-1) or next (1) neighboring keyframes from its relative current position. |
| **Push Pull (PP)** | Softens (-1) or intensifies (1) the selected keyframes' overall values between the first and last key. |
| **Tween (TW)** | Moves the key to the previous (-1) or next (1) neighboring keyframes in absolute values. This means that **0** will always move the key's value half-way between neighboring values. |

### Snapper Tool

The Snapper Tool can be used to pin your Controls to other sources for a duration of time. Rather than attaching the Control, it bakes keyframes instead, so you can easily modify the resulting animation after snapping. You can snap to other Controls, objects in Sequencer, or the world.

![snapper tool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47a7fa68-430e-4f42-a240-b4ddd568d97a/snapper1.gif)

#### Snapper Tool Usage

To use the Snapper Tool, you must first define the Child and Parent actors. Clicking on the **Children** or **Parent** buttons will assign your current selection to that category. In this example, the **Hand Control** is selected to be the **Child**, and the **Ball** is selected to be the **Parent**.

![snapper tool parent child](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c278b220-3346-4a5c-81b8-a7f9144d2fd2/snapper2.gif)

Next, if needed, you can define the range of time for the snapping effect to be active and where [Keyframes](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine) will be baked. In this example the range of time is specified between frames **6 - 24**.

![snapper tool time region](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8478a2b3-01af-4849-a764-dc282b007850/snapper3.png)

Lastly, there are a few settings available that control the snapping behavior:

| Name | Description |
| --- | --- |
| **Keep Offset** | Whether to maintain the offset between the parent and child at the initial snap time. If disabled, then the child will attach to the same transform as the parent for the duration of the snap. |
| **Snap Position** | Whether or not to snap the child's position to the parent. |
| **Snap Rotation** | Whether or not to snap the child's rotation to the parent. |
| **Snap Scale** | Whether or not to snap the child's scale to the parent. |

Clicking **Snap Animation** will perform the snap operation. In this example, **Keep Offset** is enabled in order to maintain the hand at the top of the ball.

![snapper tool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5fbde8a1-c2e8-454b-9f9b-9596e9bc2c7d/snapper1.gif)

### Motion Trail Tool

The Motion Trail Tool previews your overall Control motion by drawing the motion as an interactable curve in the Viewport. You can then edit the motion by manipulating the keyframes along the curve.

![motion trail tool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32ebeb02-3aaf-4c25-850c-ec1a6c1b2444/motiontrail1.png)

#### Motion Trail Usage

After opening the **Motion Trail** window, enable the **Show Trails** option to make the motion curve visible for your selected Controls.

![motion trail show trails](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7bc016b0-a837-4f05-87e2-9af835eeeb58/motiontrail2.png)

Selecting other Controls or multi-selecting Controls while **Show Trails** is enabled will draw motion trails for those Controls, too.

![motion trails multi select](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/750c4d10-1e13-49fa-b967-c95f5d649512/motiontrail3.gif)

Enable the **Show Keys** option to draw the position information of [Keyframes](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine) along the curve. Select these keys in the Viewport to reveal a manipulator you can use to edit the position data of your motion from the Viewport.

![motion trails show keys](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f733482-2120-4af1-bd9c-331d68e39694/motiontrail4.gif)

#### Motion Trail Properties

The following properties and features are available in the Motion Trail tool:

| Name | Description |
| --- | --- |
| **Show Trails** | Draws a Motion Trail for the selected Controls. |
| **Trail Color** | Sets the color of the Motion Trail. |
| **Show Full Trail** | Enabling this draws the full Motion Trail based on all keyframes within Sequencer. Disabling this will only draw a section of the trail relative to the Playhead. motion trails show full trail |
| **Trail Thickness** | Controls the thickness of the Motion Trail. A value of **0** will make the trail be 1 pixel thin. |
| **Frames Before** | The amount of the trail, in Frames, to display before the current Playhead time when **Show Full Trail** is disabled. |
| **Frames After** | The amount of the trail, in Frames, to display after the current Playhead time when **Show Full Trail** is disabled. |
| **Evals Per Frame** | This controls the smoothness of the Motion Trail curve. Increasing this will result in a smoother-looking curve, but at a performance cost. |
| **Show Keys** | Enables the display of keyframes along the Motion Trail. Requires **Show Trails** to also be enabled. Keyframes can be selected and manipulated to change their position information. |
| **Show Frame Number** | Enables a frame counter display next to each keyframe. The number is based on the keyframe time in Frames, and adheres to Sequencer's **Frames Per Second** setting. |
| **Key Color** | Sets the color of the keyframe display, including the keyframe number. |
| **Key Size** | Controls the size of the keyframe points. |
| **Show Marks** | Enables the display of visual timing marks along the Motion Trail. These marks are useful for visualizing the speed of a motion along the curve. Marks that are spread apart denote high-speed regions, whereas marks that are close together denote lower-speed regions. motion trails show marks |
| **Mark Color** | Sets the color of the timing marks. |
| **Mark Size** | Controls the size of the timing marks. |
| **Lock Marks to Frames** | Sets the distribution of the timing marks to match Sequencer's **Frames Per Second** setting. |
| **Seconds Per Mark** | If **Lock Marks to Frames** is disabled, you can set an arbitrary time here (in seconds) for marks to be distributed along the curve. |

Motion Trails can be enabled for non-Control Rig objects and actors in Sequencer by using the console command: `Sequencer.UseOldSequencerTrails 0`. This will disable the legacy transform trajectory display, enabling the new Motion Trails tool to be used instead.

### Pivot Tool

The Pivot Tool creates a temporary pivot point for a selected Control, which can then be moved to any arbitrary point. This tool is useful if you need to temporarily manipulate a Control relative to other points. After enabling the Pivot Tool, clicking **Edit** enables the pivot to be moved to different points. Clicking **Pose** will lock the pivot to its current position, where manipulating it will move the selected Control relative to the pivot.

![pivot tool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca62120a-103a-469a-93a2-2a5ac7231f26/pivot1.gif)

#### Pivot Tool Usage

There are several hotkeys and behaviors to aid you using the Pivot Tool in different ways.

| Hotkey | Description |
| --- | --- |
| **Ctrl + Shift + Alt + G** | Resets the pivot position back to the Control. reset pivot tool |
| **Shift + LMB Pivot Tool** | When multiple Controls are selected, holding Shift and clicking the Pivot Tool will snap all pivots to the last selected Control. snap pivot |
| **Ctrl + LMB Pivot Tool** | When multiple Controls are selected, holding Ctrl and clicking the Pivot Tool will snap all pivots to the middle point of all selected Controls. snap pivot middle |
| **Ctrl + LMB in Viewport** | Holding Ctrl and clicking in the Viewport will snap the pivot point to the selected point. raycast pivot |
| **Shift + Pivot** | Holding **Shift** while pivoting will disable rotation on the Control when pivoting, causing it to only translate. pivot rotation off |

## Animation Mode Settings

In the **Animation Mode Panel**, you can expand the Animation Settings section to reveal the following additional settings:

![animation mode settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/992565bd-32ad-4243-9016-4bbf5e47535e/settings.png)

| Name | Description |
| --- | --- |
| **Display Hierarchy** | Enabling this will draw Bones on the character. animation mode display hierarchy |
| **Display Nulls** | Enabling this will draw all [Nulls](/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine#nulls) from the Control Rig in the Viewport. |
| **Hide Control Shapes** | Hides all Controls in the Viewport. This will also hide Bones and Nulls if **Display Hierarchy** or **Display Nulls** are enabled. |
| **Show All Proxy Controls** | Hides or shows all [Proxy Controls](/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine#controlandvaluetypes) in the viewport. Proxy Controls are invisible until you select one of the Controls they are driving. Enabling this can be a useful way to discover all Proxy Controls in a rig. |
| **Show Controls as Overlay** | Enabling this makes occluded Controls visible (similar to X-ray modes in other software), allowing them to be selected if they are behind other Controls or geometry. |
| **Driven Control Color** | When a Proxy Control is selected, this is the color that all driven Controls will exhibit, which can be useful to aid in selection feedback for your Proxy Control relationships. |
| **Display Axes on Selection** | Shows a preview axis on the selected element. |
| **Axis Scale** | The scale of the preview axis when **Display Axes on Selection** is enabled. |
| **Coord System Per Widget Mode** | Restores the coordinate space when changing Gizmo modes in the Viewport. |
| **Only Select Rig Controls** | Enabling this will only make Control Rig controls be selectable in the Viewport. All other objects, including the character, will not be selectable. This can also be enabled from the toolbar by clicking the **Select** button in the Animation panel toolbar. |
| **Local Transforms in Each Local Space** | Enabling this will transform each selected control relative to their local transform space, if your transformation gizmo is set to local coordinates. animation mode local transforms in each local space |
| **Gizmo Scale** | Increases or decreases the gizmo scale. animation mode gizmo scale |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [tool](https://dev.epicgames.com/community/search?query=tool)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#prerequisites)
* [Enabling Animation Mode](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#enablinganimationmode)
* [Animation Mode Overview](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#animationmodeoverview)
* [Anim Outliner](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#animoutliner)
* [Anim Details](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#animdetails)
* [Animation Mode Tools](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#animationmodetools)
* [Poses Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#posestool)
* [Saving Poses](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#savingposes)
* [Applying Poses](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#applyingposes)
* [Mirroring Poses](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#mirroringposes)
* [Additional Controls and Hotkeys](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#additionalcontrolsandhotkeys)
* [Folder Display](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#folderdisplay)
* [Tweens Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#tweenstool)
* [Snapper Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#snappertool)
* [Snapper Tool Usage](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#snappertoolusage)
* [Motion Trail Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#motiontrailtool)
* [Motion Trail Usage](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#motiontrailusage)
* [Motion Trail Properties](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#motiontrailproperties)
* [Pivot Tool](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#pivottool)
* [Pivot Tool Usage](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#pivottoolusage)
* [Animation Mode Settings](/documentation/en-us/unreal-engine/animation-editor-mode-in-unreal-engine?application_version=5.7#animationmodesettings)
