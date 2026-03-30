<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/parametric-asset-setup?application_version=5.7 -->

# Parametric Asset Setup

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
9. Parametric Asset Setup

# Parametric Asset Setup

Preliminary steps for creating your parametric outfit asset.

![Parametric Asset Setup](https://dev.epicgames.com/community/api/documentation/image/23aa46ee-9d21-43c7-b87c-859efadeff3a?resizing_type=fill&width=1920&height=335)

 On this page

Before we get started with asset creation, there are a few things we need to do. First, enable both **MetaHuman** and **Chaos Cloth** Plugins:

1. In **Unreal Engine** (UE) 5.6 or later, click **Edit > Plugins** in the menu bar.
2. Under the **Built-In** section of the **All Plugins** list:

   1. Click **MetaHuman**, and enable the **MetaHuman Creator** plugin.

      [![](https://dev.epicgames.com/community/api/documentation/image/ac68fbd6-c6d6-4163-8af0-a4035c78dec4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac68fbd6-c6d6-4163-8af0-a4035c78dec4?resizing_type=fit)
   2. Click **Physics**, and enable **Chaos Cloth Asset** and **Chaos Cloth Asset Editor**.

      [![](https://dev.epicgames.com/community/api/documentation/image/98feabc2-7748-49c1-8ef3-ba3bf242b0c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98feabc2-7748-49c1-8ef3-ba3bf242b0c4?resizing_type=fit)

   You must restart UE to apply this change.

   Instead of restarting UE, we recommend you close it completely to continue with the next step. Otherwise, you may need to restart again.
3. In the **Epic Games Launcher**, in the **Library** tab, click on the dropdown menu on the **Launch** button of the engine version you wish to use. Select **Options**.

   [![Epic Games Launcher Options](https://dev.epicgames.com/community/api/documentation/image/68f558d2-0804-4eb8-9f09-9cd9d28be98e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68f558d2-0804-4eb8-9f09-9cd9d28be98e?resizing_type=fit)
4. Check the box next to **MetaHuman Creator Core Data** and click **Apply**. This will download essential content for MetaHuman Creator.
5. In UE, click **Edit > Project Settings**. In the left-hand menu of the Project Settings window, scroll to the **Plugins** section, and click **MetaHuman SDK**. In these settings, are **MetaHuman Packaging Paths**.

   [![MetaHuman Packaging Paths](https://dev.epicgames.com/community/api/documentation/image/093d258e-a40a-4533-a8bc-2cbdb1271637?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/093d258e-a40a-4533-a8bc-2cbdb1271637?resizing_type=fit)

   Take note of the location for Outfits. As a default, this is `/Game/Outfits` which shows up in your Content Browser as **All > Content > Outfits**.

   Do not change the name of this folder at this time.

   This directory is where you will be creating and working on your outfit assets if you are planning to package your assets for upload to FAB.

   [MetaHuman Manager](https://dev.epicgames.com/documentation/en-us/metahuman/selling-metahumans-on-fab?application_version=5.6) is used to verify and package your asset, which requires your outfit asset and any dependencies it has to exist within a single folder within the folder you just specified. Otherwise, it will not pass verification and consequently will not be able to be packaged.

   For this example, we will use the default directory, **Outfits**, and be creating an asset called “techwearOutfit” (which you can download from [FAB](https://www.fab.com/listings/9e04c752-1979-4723-b78f-6d24afc532bc)).
6. In the Content Browser, inside of the Outfits folder, create a folder with the same name as your asset. In this case “techwearOutfit.” Then, create and nest a second folder inside the first, with the same name. You should end up with a folder structure that looks like this:

   [![Outfit Path](https://dev.epicgames.com/community/api/documentation/image/af033243-cd0d-462d-b4a7-7ff3fcee0e86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af033243-cd0d-462d-b4a7-7ff3fcee0e86?resizing_type=fit)

   This second folder will be referred to as your **working folder** for this tutorial.

   Within this working folder, you can arrange things in any way you want; you can create subfolders for different types of assets, such as meshes, cloth assets, materials and textures, or you can keep them all within this folder.

### Next Step

* [![Creating Your MetaHuman](https://dev.epicgames.com/community/api/documentation/image/12e35dc3-ee31-4127-86a4-9939ecee1bca?resizing_type=fit&width=640&height=640)

  Creating Your MetaHuman

  Creating your MetaHuman in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-your-metahuman-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Next Step](/documentation/en-us/unreal-engine/parametric-asset-setup?application_version=5.7#nextstep)
