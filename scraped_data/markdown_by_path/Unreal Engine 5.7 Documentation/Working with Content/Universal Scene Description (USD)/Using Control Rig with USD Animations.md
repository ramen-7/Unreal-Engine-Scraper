<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7 -->

# Using Control Rig with USD Animations

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Universal Scene Description (USD)](/documentation/en-us/unreal-engine/universal-scene-description-usd-in-unreal-engine "Universal Scene Description (USD)")
7. Using Control Rig with USD Animations

# Using Control Rig with USD Animations

Use Control Rig to manage USD animations directly in Unreal Editor.

![Using Control Rig with USD Animations](https://dev.epicgames.com/community/api/documentation/image/d15dfb35-6713-44d2-865c-626154da16fb?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **USD Importer** can use **Control Rig** to bake and directly manipulate skeletal animation from opened USD Stages. It can then save and maintain changes to the animation in the USD file. This guide walks you through this workflow and provides a reference for some of its configuration options.

## Overview

When you bind a Control Rig to your SkelRoot prim in the **USD Stage** window, the USD Importer automatically performs the following processes:

* Adds a Control Rig track to **Sequencer**.
* Runs through the animation from start to finish, adding keyframes to the Control Rig for each frame of animation.
* Disables the skeletal animation section.

As a result, the Control Rig has one keyframe for each individual frame of animation, and it effectively assumes control of the animation. Any changes can then be saved out to the USD file, which preserves animation data between sessions. This reduces the amount of busywork needed to quickly edit animations in-engine.

For information about how to reduce the number of automatically generated keyframes from this process, refer to the section on [Reducing Keyframes](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine#reducingkeyframes) below.

## 1. Required Setup

To use the USD Importer, you need to enable the **USD Importer** plugin in the **Edit** > **Plugins** menu. Restart the editor after enabling the plugin.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c141a67e-33f3-48f5-8d3f-b7c5059c355a/usd-importer-plugin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c141a67e-33f3-48f5-8d3f-b7c5059c355a/usd-importer-plugin.png)

Click to enlarge image.

This guide uses a new project created using the **Third-Person template**. This includes the Unreal Engine mannequin models and the `CR_Mannequin_Body` control rig. Both of these are available in the `Content/Mannequins` folder in the **Content Browser**.

This guide uses these assets to provide an example, but they are not necessary to follow these instructions. You can follow along with any Skeletal Mesh as long as you have already created a Control Rig for that mesh. For more information on using Control Rigs, refer to the [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine) documentation.

## 2. Export a USD File

To take advantage of the USD Stage's functionality for setting up Control Rigs, you need to export a USD of the animation you want to edit.

1. Select an animation asset and a Control Rig that corresponds to that asset's skeletal mesh. This example uses the following assets from the third-person template:

   * Animation asset: Content/Characters/Mannequins/Animations/Manny/MM\_Walk\_InPlace
   * Control Rig: Content/Characters/Mannequins/Rigs/CR\_Mannequin\_Body
2. Right-click the **animation** in the **Content Browser**, then click **Asset Actions** > **Export**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2669411-7d6e-4318-9292-a6cd7a27d717/asset-actions-export.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2669411-7d6e-4318-9292-a6cd7a27d717/asset-actions-export.png)

   Click to enlarge image.
3. In the export dialog, select **Universal Scene Description file (\*.usda)** as the file type, then click **Save**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8be6d726-9bf8-4e21-9161-c42ec1ba4fd2/saving-a-usda.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8be6d726-9bf8-4e21-9161-c42ec1ba4fd2/saving-a-usda.png)

   Click to enlarge image.
4. In the **USD Export Options** dialog, click **Export**.

   ![Configure the USD export options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4abd209-a588-4b24-ba02-1a19acab916c/usd-export-options.png)

## 3. Set Up Control Rig in the USD Stage

Now that you have a USD file for your animation, you can open it using the USD Stage editor and set it up with a Control Rig.

1. Click **Window** > **Virtual Production** > **USD Stage** to open the **USD Stage** editor.

   ![Open the USD Stage window from Window > Virtual Production](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4671d8e1-1ea7-4331-9cab-827168a66f42/usd-stage-window.png)
2. In the USD Stage window, click **File** > **Open**, then select the `.usda` file for your animation and click **Open** in the open file dialog.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27534ae7-a5b6-4da7-850b-f6ca0f0848ae/open-usd-stage.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27534ae7-a5b6-4da7-850b-f6ca0f0848ae/open-usd-stage.png)

   Click to enlarge image.

   The model appears at the world's origin.
3. In the **USD Stage** window, right-click the **root** of the skeleton, then click **Set Up Control Rig**.

   ![Set up Control Rig in the USD stage](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9725b161-6893-4f7e-aaa9-017d17e3e871/set-up-control-rig.png)
4. The **Integrations** panel appears to the right of the Stage hierarchy. Set the **Control Rig asset** to your skeletal mesh's Control Rig.

   ![Set your Control Rig asset in the Integrations panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce6fe117-4899-4cdd-b6ab-51515bfcc4e9/set-control-rig-asset.png)
5. If you do not see the Sequencer window, click the **USD Stage Actor** in your world's **Hierarchy**, then double-click the **Level Sequence** in the **Details** panel.

   ![The Sequencer asset in the USD Stage Actor's details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2544996-7b8b-48cb-a28a-8b194bc74510/usd-stage-actor.png)
6. Click the newly created **Control Rig** track in the **Sequencer** track list.

   * In this example, the Control Rig is called `CR_Mannequin_Body`.[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c524b10-516a-44f1-b343-1f03a6eb0de7/control-rig-mannequin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c524b10-516a-44f1-b343-1f03a6eb0de7/control-rig-mannequin.png)

   Click to enlarge image.

## Result

The controls for the rig appear on the mesh in the world. You can now use Sequencer and the Control Rig to edit the existing animation or create new ones from scratch. Any time the system detects a change, it writes it out to the USD Stage, which can then be saved to the file on disk.

## Configuration

Setting up a SkelRoot prim for Control Rig will provide it with some attributes that can be configured as the following options on the USD Stage integrations panel.

### Forward Kinematic Control Rig

The **Use FKControlRig** setting disables your selected Control Rig asset and instead uses a default forward kinematic rig that has one control for each bone. You can use this for skeletal meshes you do not already have a Control Rig for.

### Reduce Keyframes

To reduce the number of auto-generated keyframes, enable the **Control Rig key reduction** setting in the Integrations panel. This removes keyframes similar to previous keyframes, relying on the system to tween the animation between the keyframes that remain. You can use the **Control Rig key reduction tolerance** setting to change the keyframe reduction sensitivity. The higher you make this value, the more aggressively it will reduce keyframes.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e6c6ae63-7443-47c7-a012-c7e7092ddd65/key-reduction-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e6c6ae63-7443-47c7-a012-c7e7092ddd65/key-reduction-options.png)

Click to enlarge image.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [animations](https://dev.epicgames.com/community/search?query=animations)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [usd](https://dev.epicgames.com/community/search?query=usd)
* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#overview)
* [1. Required Setup](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#1requiredsetup)
* [2. Export a USD File](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#2exportausdfile)
* [3. Set Up Control Rig in the USD Stage](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#3setupcontrolrigintheusdstage)
* [Result](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#result)
* [Configuration](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#configuration)
* [Forward Kinematic Control Rig](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#forwardkinematiccontrolrig)
* [Reduce Keyframes](/documentation/en-us/unreal-engine/using-control-rig-with-usd-files-in-unreal-engine?application_version=5.7#reducekeyframes)

Related documents

[Universal Scene Description in Unreal Engine

![Universal Scene Description in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/bff646fc-34ae-4f94-b81a-a32ae898ee59?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/universal-scene-description-in-unreal-engine)
