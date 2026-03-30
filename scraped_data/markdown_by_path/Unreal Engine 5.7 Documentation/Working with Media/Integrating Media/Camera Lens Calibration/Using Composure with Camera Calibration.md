<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-composure-with-camera-lens-calibration-in-unreal-engine?application_version=5.7 -->

# Using Composure with Camera Calibration

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
8. Using Composure with Camera Calibration

# Using Composure with Camera Calibration

How to use the Camera Calibration plugin with Composure.

![Using Composure with Camera Calibration](https://dev.epicgames.com/community/api/documentation/image/9bb2815b-c473-4b4d-a307-9ace5aa7524b?resizing_type=fill&width=1920&height=335)

 On this page

1. Go to **Window > Virtual Production > Composure Compositing** to open the **Composure** window.

   ![Open Composure Compositing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a03d4163-8cb0-4e1b-abde-6938a3ddd796/01-open-composure-window.png "Open Composure Compositing")
2. Right-click inside the **Composure** window and select **Create New Comp** from the menu. Click the **Empty Comp Shot** button to create a new empty composition.

   ![Create a new Comp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/160c217f-6f79-4adc-9d71-a15b795a5c2b/02-create-new-comp.png "Create a new Comp")
   ![Create an Empty Comp Shot](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f706612c-8c9f-4bfd-8e22-8345f19d8c05/03-empty-comp-shot.png "Create an Empty Comp Shot")
3. Right-click the composure and select **Add Layer Element**. Click the **Media Plate** button. This media plate will use the live video feed from your camera.

   ![Add Layer Element](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c46322ce-1735-4be3-97a8-ee6f880c058e/03-add-layer-element-1.png "Add Layer Element")
   ![Add a Media Plate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1271dd9-6742-48a2-80bb-c76a25b1f36f/04-create-media-plate.png "Add a Media Plate")
4. Navigate to **Content Browser > Your project folder for MediaIO >** and drag **MediaBundle-01** into your Level.

   [![Drag Your Media Bundle to the Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53578004-a8fa-41f4-b714-e81e2a768c0c/05-add-media-bundle.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53578004-a8fa-41f4-b714-e81e2a768c0c/05-add-media-bundle.png)

   Click image to expand.
5. Select the **media plate** in the **Composure** window and go to the **Details** panel. Scroll down to the **Composure** section and expand the **Input** category. Click the **Media Source** dropdown and select **T\_MediaBundle-01\_BC** from the list. You should now see the live video feed streamed on the media plate.

   ![Select the Media Plate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76978d3a-a221-4a6f-8251-13a81a29a82a/06-select-media-plate.png "Select the Media Plate")
   [![Set the Media Source](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/021f61fe-fa02-4fa0-b8e8-9c6aed87a9f6/07-new-media-source.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/021f61fe-fa02-4fa0-b8e8-9c6aed87a9f6/07-new-media-source.png)

   Click image to expand.
6. Right-click the composure and select **Add Layer Element**. Click the **CG Layer** button.

   ![Add a CG Layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59ecd8f5-7e96-48bc-9673-57dcd6b6c5b3/09-new-cg-layer.png "Add a CG Layer")
7. Go to **Window > Layers** to open the **Layers** window.

   ![Open the Layers Window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdbaf9a9-55d1-4865-b30f-1792a0824749/11-open-layers-window.png "Open the Layers Window")
8. Select the **BP\_UE\_Tracker3** and the **CameraCalibrationCheckerboard** Blueprints from the **Outliner**. Go to the **Layers** window then right-click and select **Add Selected Actors to New Layer** from the menu. Name the layer **cglayer**.

   [![Add Selected Actors to New Layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59ca623a-f148-420c-8768-bc9537bec4d7/12-add-selected-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59ca623a-f148-420c-8768-bc9537bec4d7/12-add-selected-actors.png)

   Click image to expand.

   You can also find **BP\_UE\_Tracker3** in the Content Browser under Engine content folder.

   [![BP UE Tracker3](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bade7cc8-7759-4c9d-af3f-4bd8b8bfc6ee/10-bp-ue-tracker3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bade7cc8-7759-4c9d-af3f-4bd8b8bfc6ee/10-bp-ue-tracker3.png)

   Click image to expand.
9. Select the **cg element** layer in the **Composure** window and go to the **Details** panel. Scroll down to the **Composure** section and click the **+** button to expand the **Capture Actors** options. Click the **ActorSet** dropdown and select **cglayer** from the list.

   [![Add a New Layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0357a799-e1c5-4b13-91d5-aed5c595f8d7/13-add-layers-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0357a799-e1c5-4b13-91d5-aed5c595f8d7/13-add-layers-actor.png)

   Click image to expand.
10. With the **cg element** layer selected, scroll down to the **LensDistortion** section and select the **Distortion Source** as the **LumixLens** file.

    ![Apply Distortion to the CG Layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38eace81-ba37-43bf-9010-c2d4e2faa99c/14-select-lens-file.png "Apply Distortion to the CG Layer")
11. Right-click in the **Content Browser** and select **Material** from the **Create Basic Asset** section. Name the Material **M\_SimpleComp**.

    ![Create a New Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1dab7bf6-2795-4e57-9bdc-890d8181a38c/15-create-new-material.png "Create a New Material")
12. Double-click **M\_SimpleComp** to open it. Select the Material node and go to the **Details** panel. Set the **Shading Model** to **Unlit**.

    ![Set the Material to Unlit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15659c40-0b05-46c8-8da9-368d8f56596c/15-unlit-shading-model.png "Set the Material to Unlit")
13. Right-click in the graph then search for and select **TextureSample**. Right-click the **Texture Sample** node and select **Convert to Parameter**. Name it **CGLayer**. Go to the **Details** panel and add a texture to the **CG Layer** dropdown.

    ![Add a Texture Sample](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2668841-304c-451e-a377-01183d130937/16-new-texture-sample.png "Add a Texture Sample")
    ![Convert the Texture to a Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f93e99e3-a98a-4ff2-813a-93bf320205ee/17-convert-to-parametr.png "Convert the Texture to a Parameter")
    ![Add a Texture](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6231802-762a-4d10-a528-e6b88c36c2e3/18-new-material-texture-base.png "Add a Texture")
14. Repeat the previous step and add another **Texture Sample**. Name the parameter **MediaPlate**.

    [![Add Another Texture Sample](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/151bf3aa-24b5-4ae5-959b-fc26caf05171/19-add-media-plate-parametr.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/151bf3aa-24b5-4ae5-959b-fc26caf05171/19-add-media-plate-parametr.png)

    Click image to expand.
15. Right-click in the graph then search for and select **Over**. Connect the **RGBA** pins of both nodes to the **A** and **B pins** of the **Over** node. Finally, connect the **RGBA** pin of the **Over** node to the **Emissive Color** pin of the Material node.

    ![Add an Over Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e553801-0205-4f69-bf29-631fa0e7a6de/20-add-over-node.png "Add an Over Node")
    [![New Material Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0ae3981-5877-4fa1-90cd-18a7d450a520/21-new-material-graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0ae3981-5877-4fa1-90cd-18a7d450a520/21-new-material-graph.png)

    Click image to expand.
16. Select your composition from the **Composure** window and go to the **Details** panel. Scroll down to the **Transform / Compositing Passes** section and expand **Transform Passes**. Add the **M\_SimpleComp** Material to the **Material** slot.

    [![Add your Material to the Composition](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1b3d265-a1c9-4649-9eed-70034cf48084/23-add-material-to-composure.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1b3d265-a1c9-4649-9eed-70034cf48084/23-add-material-to-composure.png)

    Click image to expand.
17. Expand **Input Elements** and add Media Plate and CG Element layers to their corresponding slots. You should now have the video feed streamed to the Media Plate and your selected Actors displayed in the CG Elements layer.

    [![Add your Material to the Composition](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee0fecf5-b86a-4146-8661-bbbb8bd721e3/24-set-input-elements.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee0fecf5-b86a-4146-8661-bbbb8bd721e3/24-set-input-elements.png)

    Click image to expand.

## Section Results

In this guide you learned how to use Composure with the Camera Calibration plugin.

* [composure](https://dev.epicgames.com/community/search?query=composure)
* [camera lens calibration](https://dev.epicgames.com/community/search?query=camera%20lens%20calibration)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Section Results](/documentation/en-us/unreal-engine/using-composure-with-camera-lens-calibration-in-unreal-engine?application_version=5.7#sectionresults)
