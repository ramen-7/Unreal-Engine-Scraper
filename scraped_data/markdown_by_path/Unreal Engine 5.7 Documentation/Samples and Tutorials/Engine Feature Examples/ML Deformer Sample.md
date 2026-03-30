<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7 -->

# ML Deformer Sample

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Engine Feature Examples](/documentation/en-us/unreal-engine/engine-feature-examples-for-unreal-engine "Engine Feature Examples")
7. ML Deformer Sample

# ML Deformer Sample

Example use of Unreal Engine's Machine Learning (ML) techology to create a high-fidelity character with realistic deformations.

![ML Deformer Sample](https://dev.epicgames.com/community/api/documentation/image/28cdb6fe-b7de-40d5-b7a9-a3cfe5dec03e?resizing_type=fill&width=1920&height=335)

 On this page

The Machine Learning (ML) Deformer Sample demonstrates how you can use Unreal Engine's Machine Learning (ML) technology to create a high-fidelity real-time game character, with realistic deformations driven by learned offline muscle, flesh and cloth simulations. The sample uses the [ML Deformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-the-machine-learning-deformer-in-unreal-engine) plugin.

This main Level in the sample is an interactive demo sequence. It shows muscles bulging and sliding under the skin and folds forming on clothing. You can also compare the results with ML Deformer on and off, and animate the model with the included ControlRig Asset.

## Downloading the Sample

To create a project with the ML Deformer sample, follow these steps:

1. Access the [ML Deformer sample](https://fab.com/s/fb59a5b662f2) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Navigating the Scene

While the scene is playing in-Editor, you can use keyboard or PlayStation gamepad controls to navigate the scene. These controls are configured in the `KeyboardGamepadMapping` file, located in the `Content/Input/` folder, and you can customize them.

### ML Deformation Toggle and Layers

While the scene is playing, press and hold the **M** key, or **left D-pad** button on your gamepad, to temporarily disable ML deformation.

![ML Deformer off](https://dev.epicgames.com/community/api/documentation/image/fcd160c6-242d-4bb5-9747-f43b81d92363?resizing_type=fit&width=1920&height=1080)

![ML Deformer on](https://dev.epicgames.com/community/api/documentation/image/7c32fc5d-315d-4da6-9194-d344fc8d25d4?resizing_type=fit&width=1920&height=1080)

ML Deformer off

ML Deformer on

Press the **Up** and **Down** arrow keys or use the D-pad **up / down** buttons to switch between the cloth, skin, and muscle layers.

[![Character layers](https://dev.epicgames.com/community/api/documentation/image/5130ddeb-685e-4dc0-8f19-4f3220fcf409?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5130ddeb-685e-4dc0-8f19-4f3220fcf409?resizing_type=fit)

Toggle between normal Materials and a clay shader with the **N** key or the **right D-pad** button.

![Clay shader on](https://dev.epicgames.com/community/api/documentation/image/74d40979-b5ed-4214-affd-726af70710c7?resizing_type=fit&width=1920&height=1080)

![Clay shader off](https://dev.epicgames.com/community/api/documentation/image/9a36d384-7188-4036-8bbe-646b0c73ba85?resizing_type=fit&width=1920&height=1080)

Clay shader on

Clay shader off

### Playback and HUD Controls

While the scene is playing in PIE, you can use the following playback controls:

| Action | Keyboard Shortcut | Gamepad Shortcut |
| --- | --- | --- |
| Pause playback | Spacebar | X button |
| Decrease playback speed | Comma | Square button |
| Increase playback speed | Period | Circle button |

You can also enable two separate Heads-Up Display (HUD) widgets:

| Widget | Keyboard Shortcut | Gamepad Shortcut |
| --- | --- | --- |
| Stats and performance widget | H | L1 button |
| Shortcut helper widget (shows gamepad button shortcuts) | Tab | Special button (right) |

### Camera Controls

Press the **O** key, or **triangle** button on your gamepad, to enable or disable camera controls.

While camera controls are enabled, you can use the following keyboard shortcuts:

| Action | Keyboard Shortcut | Gamepad Shortcut |
| --- | --- | --- |
| Orbit camera left / right | A / D | Left thumbstick (move horizontally) |
| Dolly (zoom) in / out | W / S | Left thumbstick (move vertically) |

## Character and Rig Details

The character used for the shot is a high-fidelity digital human, with a musculoskeletal system and true-to-life face and body materials.

The musculoskeletal system was created by combining MRI scan data, a 3D skeleton scan, and hand-authored muscles. For the face and body materials, 3D face and body scans were used, along with a reference shoot.

The sample contains a Control Rig that you can use to further explore how ML deformation interacts with different character poses. The rig is located in the `Content/Characters/Emil/Rig` folder, and the Asset file is named `CR_Emil`. Unlike a MetaHuman rig, the rig used in this sample is asymmetrical (that is, joint positions are not mirrored perfectly). This achieves the most realistic deformation possible.

## Further Information

The 2023 State of Unreal GDC presentation included an in-depth segment of how the results in this technical demo were achieved. You can learn about the whole process, from scanning the character, to training the ML model, then combining different software and technologies to achieve the final result. Watch the full segment on YouTube at [this link](https://www.youtube.com/watch?v=teTroOAGZjM&t=19000s).

To learn more about the ML Deformer plugin, see the [ML Deformer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-the-machine-learning-deformer-in-unreal-engine) page.

* [machine learning](https://dev.epicgames.com/community/search?query=machine%20learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Downloading the Sample](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#downloading-the-sample)
* [Navigating the Scene](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#navigating-the-scene)
* [ML Deformation Toggle and Layers](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#ml-deformation-toggle-and-layers)
* [Playback and HUD Controls](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#playback-and-hud-controls)
* [Camera Controls](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#camera-controls)
* [Character and Rig Details](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#character-and-rig-details)
* [Further Information](/documentation/en-us/unreal-engine/ml-deformer-sample-in-unreal-engine?application_version=5.7#further-information)
