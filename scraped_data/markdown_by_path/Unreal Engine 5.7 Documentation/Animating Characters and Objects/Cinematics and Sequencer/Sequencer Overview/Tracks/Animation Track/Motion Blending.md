<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7 -->

# Motion Blending

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
7. [Sequencer Overview](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview "Sequencer Overview")
8. [Tracks](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine "Tracks")
9. [Animation Track](/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine "Animation Track")
10. Motion Blending

# Motion Blending

Use Motion Blending tools to seamlessly transition animation motion between animations clips in Sequencer.

![Motion Blending](https://dev.epicgames.com/community/api/documentation/image/34fd7836-4523-4aa0-8c43-9f106b6fbdfe?resizing_type=fill&width=1920&height=335)

 On this page

When transitioning between character animation clips in the **Sequencer** [Animation Track](/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine), you can use the **Motion Blending** tools to further increase the blend quality. Using Motion Blending tools, you can dynamically transition an animation clip's motion and world position between clips. This is especially useful when working with animations that contain world displacement data.

Here, a character transitions from a walk animation to a run animation. Without any blending, the transition is a hard cut. Using a simple blend, but without motion blending, the animation still resets the character's position to the animation's origin point, but the character's mesh is transitioned smoothly. By blending the animations with motion blending, the world position is preserved and the animation transitions smoothly.

| Description | Example |
| --- | --- |
| **No Blending** | no blending demo |
| **Motion Blending with No Matching** | motion blending with no matching |
| **Motion Blending with Matching** | motion blending with matching(convert:false) |

Clip Matching references a bone from the character's skeleton and matches that bone's position and motion to the adjacent clip's bone that contains displacement data, such as a root or pelvis bone. By matching the selected bone with the adjacent clip's displacement, it automatically calculates and sets an offset to transition to the next animation while retaining the position of the character. The offset data will then be stored within the animation section in the Sequencer Asset.

## Using Motion Blending

This section contains information about how to blend animations using Motion Blending in Sequencer.

#### Prerequisites

* Your project contains at least two Animation Sequences that contain a bone, such as a root or non-root bone, with world displacement data.

### Motion Blending Set Up

To blend animations using Motion Blending in Sequencer, first add your animations to an animation track in the Sequencer Editor, ensuring they are playing sequentially or overlapping.

![blending clips in sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8be9e0a-c60c-4e79-80d9-eb14ec8cabe6/addsequences.png)

Navigate your playhead to the beginning of the second animation section to set the time for the animation offset to be calculated. Then, to blend the second animation from the final position of the first animation, right-click the second animation clip, navigate to **Match With This Bone In Previous Clip** and select a bone from the character's skeleton relevant to the animations you are transitioning. In this workflow example, the `l_foot` bone is used to blend the walk and run animations.

![set up motion bleeding demo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6125e42-f56a-4937-af6b-34da19ba5d31/setmbdemo.gif)

When played back, your Animation Clips will now blend the animation motion and the world displacement position.

![motion blending demo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f258715c-0b3b-4d74-abde-409df488d055/motionblendingdemo.gif)

## Motion Blending Properties

Motion Blending has the following properties:

| Property | Description |
| --- | --- |
| **Match With This Bone In Previous Clip** | Select a bone to match the selected animation clip's motion and position with the **previous** clip, at the playhead's location in time.  Using this property results in the animation's motion continuing from the previous clip's position. motion blending demo |
| **Match With This Bone In Next Clip** | Select a bone to match the selected animation clip's motion and position with the **following** clip, at the playhead's location in time.  Using this property results in the animation's motion playing centered around the origin point. match next clip demo |
| **Match X and Y Translation** | When enabled, the selected bone will match **X** and **Y** axes translations. This is useful for ground motion in order to retain the character's movement direction. motion blending x and y translation demo |
| **Match Z Height** | When enabled, the selected bone will match the **Z** axis height of the animation. This is useful for animations that influence a character's height in world space. motion blending height translation demo |
| **Match Yaw Rotation** | When enabled, the selected bone will match the **yaw** (**Z**) rotation. motion blending yaw rotation demo |
| **Match Pitch Rotation** | When enabled, the selected bone will match the **pitch** (**Y**) rotation. motion blending pitch rotation demo |
| **Match Roll Rotation** | When enabled, the selected bone will match the **roll** (**X**) rotation. motion blending roll rotation demo |
| **Show Root Motion Trail** | To view a debug render of the entire animation track's root motion trail, right-click your animation track and enable the **Show Root Motion Trail** property. The root motion trail will be rendered as a black-and-white, striped line that traces every animation clip's root bone translation. show root motion trail property |

### Root Motion Offset Settings

You can manually assign root motion offsets, such as translation and rotation, on each animation clip in your Level Sequence to influence the blending result. Adding root motion offsets only affects the clip, rather than the animation itself, and is applied in addition to any motion blending on a clip. Location and Rotation offsets also respect the start time of the animation clip and can be added to trimmed clips without issue.

To set a root motion offset for an animation clip, right-click the clip in the Sequencer Editor and navigate to **Properties** > **Root Motions**.

![root motion offset properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/336b2587-8130-497b-8e3d-b5804b076634/rootmotionoffset.png)

Root motion offset has the following properties:

| Property | Description |
| --- | --- |
| **Start Location Offset** | Set **X**, **Y**, and **Z** values to set the location (translation) offset applied to the root bone before the matched offset is applied. |
| **Start Rotation Offset** | Set **roll** (**X**), **pitch** (**Y**), and **yaw** (**Z**) values to set the rotation offset applied to the root bone before the matched offset is applied. |
| **Matched Location Offset** | Reference the **X**, **Y**, and **Z** values that set the location (translation) offset added to the root bone by the matched offset as a base value. |
| **Matched Rotation Offset** | Reference the **roll** (**X**), **pitch** (**Y**), and **yaw** (**Z**) values that set the rotation offset added to the root bone by the matched offset as a base value. |

You can also edit the Start Location Offset and Start Rotation Offset properties in the viewport by selecting a character's Transform Gizmo at the character's root bone location.

![root motion offset handles in viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a85247e6-ee34-4b3f-86fc-b6ac407388a1/handles.png)

After selecting the gizmo, you can edit the offset's position and rotation using the transform tools.

![transform tool for root motion offsets in viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17aaf0cd-aaab-4a17-a5f5-e59b2702ee57/manipulation.gif)

### Debug Settings

Use these debug tools to observe and debug motion blending behavior when creating cinematics in the Sequencer Editor:

| Property | Description |
| --- | --- |
| **Show Skeleton** | To view a debug drawing of an animation clip's skeleton and root motion displacement, right-click the animation clip and enable the **Show Skeleton** property from the context menu. Each animation clip will render the character's skeleton a different color to differentiate animations. Additionally, each animation's world displacement will be rendered as a red line between the animation's origin point and the bone that contains world displacement data. show skeleton property |
| **Color Tint** | You can manually set the color of each animation clip by right-clicking the clip in the Sequencer Editor, then navigating to Properties and setting a color value using the Color Tint property. set section color property Color-tinted animation clips will be color coded in the Sequencer Editor and on skeleton render in the viewport. section colors sync with skeleton drawing |

## Blending Motion from Non-Root Bones

If your animations don't store character displacement on the `root` bone or your root bone is static, for example when using animations created using motion capture data, you can still blend an animation's world displacement position using the first child bone of the root, often labeled `pelvis`. After enabling motion blending on your animation clip, right-click your animation track and enable the **Blend First Child of Root** property.

![blend first child of root property](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f132e45d-515e-49df-a35d-de3df46e3774/firstchild.png)

The **Blend First Child of Root** property ignores the root bone and insead blends the animation's motion using the first animated child bone in the character's skeleton.

| Without Blend First Child of Root | With Blend First Child of Root |
| --- | --- |
| without first child of root property | with first child of root property |

Blending between animation with root motion and animations with non-root motion may not have optimal results.

## Control Rig Integration

To further edit the blending between animations in Sequencer, such as making minor edits and tweaks to a character's limbs, foot placement, or position, you can use an [Additive FK Control Rig](/documentation/en-us/unreal-engine/fk-control-rig-in-unreal-engine#additivefk) to manually key a character's animations, without overriding the effect of motion blending.

For more information about animating in Unreal Engine, see the following documentation:

[![Animating with Control Rig](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/07699bb4-c5c2-4248-8b0b-69cd31e28ec0/topicimage.png)

Animating with Control Rig

Start animating your Control rig using various tools and workflows.](/documentation/en-us/unreal-engine/animating-with-control-rig-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [blending](https://dev.epicgames.com/community/search?query=blending)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using Motion Blending](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#usingmotionblending)
* [Prerequisites](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#prerequisites)
* [Motion Blending Set Up](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#motionblendingsetup)
* [Motion Blending Properties](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#motionblendingproperties)
* [Root Motion Offset Settings](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#rootmotionoffsetsettings)
* [Debug Settings](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#debugsettings)
* [Blending Motion from Non-Root Bones](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#blendingmotionfromnon-rootbones)
* [Control Rig Integration](/documentation/en-us/unreal-engine/motion-blending-tools-in-unreal-engine?application_version=5.7#controlrigintegration)
