<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-your-metahuman-in-unreal-engine?application_version=5.7 -->

# Creating Your MetaHuman

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Cloth Simulation](/documentation/en-us/unreal-engine/cloth-simulation-in-unreal-engine "Cloth Simulation")
8. [Creating Parametric Clothing for Fab](/documentation/en-us/unreal-engine/creating-parametric-clothing-for-fab "Creating Parametric Clothing for Fab")
9. Creating Your MetaHuman

# Creating Your MetaHuman

Creating your MetaHuman in Unreal Engine.

![Creating Your MetaHuman](https://dev.epicgames.com/community/api/documentation/image/e6e011c2-b387-4832-aa2b-81d404e025b3?resizing_type=fill&width=1920&height=335)

 On this page

Though not a requirement, we recommend that you create your **MetaHuman Character** inside your working folder. This way, all assets you create will be saved in the same place. When you export your package, the MetaHuman Character will be omitted from the export.

1. In the **Content Browser**, navigate to the folder where you’d like to create your MetaHuman. Right-click in the **Content Browser**, and select **MetaHuman > MetaHuman Character**.

   [![Content Browser MetaHuman](https://dev.epicgames.com/community/api/documentation/image/a355bf55-99c4-4d0a-a68f-0023885e78aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a355bf55-99c4-4d0a-a68f-0023885e78aa?resizing_type=fit)

   Give your MetaHuman a name and click Enter to save it. Once saved, double-click on it to open up **MetaHuman Creator** within Unreal Engine. There are several options to customize your character, but we will focus only on adjusting the body shape.

   * **Body > Model**: For in-depth information on these sliders, see [Body Controls](https://dev.epicgames.com/documentation/en-us/metahuman/body-controls?application_version=5.6).

     [![Body Controls](https://dev.epicgames.com/community/api/documentation/image/4a3be774-959a-430d-a7b7-97c00ece8771?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a3be774-959a-430d-a7b7-97c00ece8771?resizing_type=fit)

     If you want to convert existing clothing to parametric clothing, you need to enable the **Fixed (Compatibility)** option:

     1. In UE, select **Edit > Project Settings**.
     2. In the left-hand menu of the Project Settings window, navigate to the **Plugins** category and click on **MetaHuman Character**.
     3. Enable **Show Compatibility Mode Bodies**.

     This will give you access to the 18 fixed body types from the previous version of MetaHuman Creator (web app). You do not need to use all 18 bodies as source bodies; we recommend using 6 (all bodies of a single height) or 4 (excluding the "unw" bodies).
   * **Body > Blend**: This enables blending between up to three selected presets to change the shape of your character’s body features.

     [![Body Shape From Preset](https://dev.epicgames.com/community/api/documentation/image/76e8f323-3fff-44aa-bb7a-6903dc360cc0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76e8f323-3fff-44aa-bb7a-6903dc360cc0?resizing_type=fit)

     Alternatively, you can use a body shape from a preset or existing MetaHuman Character, while still retaining any previous selections you have made:

     1. Drag the desired Metahuman Character into the presets list. If it is already in your present list, skip this step.
     2. Click on the **Body** tab, then the **Blend** tab. Under **All Assets**, select the desired preset.

     For more information on using this option, see the [Body Blend Controls](https://dev.epicgames.com/documentation/en-us/metahuman/body-blend-controls?application_version=5.6) page.
   * **Body > Conform**: You can also conform your body to an existing DNA file or a static or skeletal mesh template. This is covered in the [Body Conform Controls](https://dev.epicgames.com/documentation/en-us/metahuman/body-conform-controls?application_version=5.6) section of the MetaHuman documentation.

   Make sure the armpits and thigh gap have a bit of clearance. When they are clipping into each other, it is likely to cause some issues with resizing. You can try to fix these issues by playing around with some of the measurements in that area such as bicep, thigh, and chest.

   [![](https://dev.epicgames.com/community/api/documentation/image/1b90cee1-1a46-4269-9fc0-0af2e87dac8f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b90cee1-1a46-4269-9fc0-0af2e87dac8f?resizing_type=fit)
2. Once you’ve prepared the body you want to use, navigate to the **MetaHuman Character** menu and select **Export Combined Skel Mesh**.

   [![](https://dev.epicgames.com/community/api/documentation/image/3c829a78-0265-467c-a26b-ffb0e91c596a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c829a78-0265-467c-a26b-ffb0e91c596a?resizing_type=fit)

   If you are interested in packaging for FAB, navigate to your working folder or a subfolder within it. For this example, we saved it in the path below, but the **Meshes** folder is not required.

   `/All/Content/Outfits/techwearOutfit/techwearOutfit/Meshes`

   If you intend on using more than one body, create a naming convention that helps you identify the primary body you’re working on, ensuring that you include the `_CombinedSkelMesh` suffix at the end.

   For the purpose of this tutorial, we named the body `bodyShapeG_CombinedSkelMesh` because the project already contains existing bodies A–F.

   At this stage, the head texture may look strange, but this is normal. The head textures are not necessary for this asset as it is being used solely as a utility mesh. It will not be part of the end result.
3. If you’re making an outfit asset with more than one source body, for the **first body only**:

   Right-click on the skel mesh and navigate to **Skeleton > Find Skeleton**. This will bring you to the skeleton that your skel mesh is using. Copy (don’t Move) that skeleton into the directory where your body is.

   [![Assign Skeleton](https://dev.epicgames.com/community/api/documentation/image/09dd1e00-575e-4b54-8cda-a360e8d5941d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/09dd1e00-575e-4b54-8cda-a360e8d5941d?resizing_type=fit)
4. Right-click on your body again, and go to **Skeleton > Assign Skeleton** to select the skeleton you just copied into your folder.

   [![](https://dev.epicgames.com/community/api/documentation/image/4a873e82-b246-4801-86dc-83e0a8035b26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a873e82-b246-4801-86dc-83e0a8035b26?resizing_type=fit)

   Search for the skeleton from the list, click to select it, and click **Apply**.

   [![](https://dev.epicgames.com/community/api/documentation/image/53be5761-dfa7-45bb-a795-ed4ac99ff0cb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/53be5761-dfa7-45bb-a795-ed4ac99ff0cb?resizing_type=fit)

   If you make multiple bodies for this one asset, you do not need to copy the skeleton over again, but you do need to assign the skeleton of each new body to this same skeleton.

   The skeleton is a dependency of the skel mesh. For this process to work, you must ensure that none of your skel meshes are linked to a skeleton outside your working folder.
5. Once you have all your bodies ready, you can export them into the DCC of your choice to create clothing. Right-click on your combined skel mesh and navigate to **Asset Actions > Export**. Click **Export**, and save it as an FBX.

   [![Export](https://dev.epicgames.com/community/api/documentation/image/0643d791-34f1-4204-93c2-4c86b0053f61?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0643d791-34f1-4204-93c2-4c86b0053f61?resizing_type=fit)

## Next Step

* [![Building an Outfit Asset](https://dev.epicgames.com/community/api/documentation/image/0b76f732-ce89-46f9-b777-bfa8331d1a0b?resizing_type=fit&width=640&height=640)

  Building an Outfit Asset

  Building an outfit asset in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Next Step](/documentation/en-us/unreal-engine/creating-your-metahuman-in-unreal-engine?application_version=5.7#nextstep)
