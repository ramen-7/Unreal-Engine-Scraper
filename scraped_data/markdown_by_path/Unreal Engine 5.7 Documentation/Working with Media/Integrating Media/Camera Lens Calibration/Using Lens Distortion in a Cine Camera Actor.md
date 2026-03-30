<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-lens-distortion-in-a-cine-camera-actor-in-unreal-engine?application_version=5.7 -->

# Using Lens Distortion in a Cine Camera Actor

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
7. [Camera Lens Calibration](/documentation/en-us/unreal-engine/camera-lens-calibration-in-unreal-engine "Camera Lens Calibration")
8. Using Lens Distortion in a Cine Camera Actor

# Using Lens Distortion in a Cine Camera Actor

How to use the Camera Calibration plugin to apply lens distortion to a CineCamera Actor.

![Using Lens Distortion in a Cine Camera Actor](https://dev.epicgames.com/community/api/documentation/image/5b1d6091-ef25-4f28-9f60-e762c02d0009?resizing_type=fill&width=1920&height=335)

 On this page

1. Select your **CineCamera Actor** in the **Outliner** and go to the **Details** panel.

   ![Select the CineCamera Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d66ebcfc-b45f-42b8-8040-1de2a6274e89/ue5_01-cine-camera-actor.png "Select the CineCamera Actor")
2. Select the **LiveLink Component Controller component** and scroll down to the **Camera Role** category. Verify that the correct **Lens File** is assigned to the **Lens File** slot. In this example the **LumixLens** file is used from the [Quick Start Guide](/documentation/en-us/unreal-engine/camera-lens-calibration-quick-start-for-unreal-engine).

   ![Select the Live Link Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f034d12d-2704-4a11-bf12-c3bff00a6d2e/ue5_02-live-link-controller.png "Select the Live Link Component")
3. Click the **Add Component** button, then search for and select **Lens Distortion** to add the component.

   ![Add the Lens Distortion component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fed68a59-10c8-4479-9abe-8386d7217b36/ue5_04-lens-distortion.png "Add the Lens Distortion component")
4. Scroll down to the **Default** section and click the dropdown next to **Distortion Source**. Select the **LumixLens** file and **enable** the **Apply Distortion** checkbox.

   ![Add the Lens Distortion Source](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48d6f86f-89d1-4bc4-b109-9056f00e54e4/ue5_05-distortion-source.png "Add the Lens Distortion Source")
5. You should now see the lens distortion applied to the CineCamera Actor in the viewport.

## Section Results

In this guide you learned how to apply the lens distortion effect from the Camera Calibration plugin to the CineCamera Actor.

* [camera](https://dev.epicgames.com/community/search?query=camera)
* [camera lens calibration](https://dev.epicgames.com/community/search?query=camera%20lens%20calibration)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Section Results](/documentation/en-us/unreal-engine/using-lens-distortion-in-a-cine-camera-actor-in-unreal-engine?application_version=5.7#sectionresults)
