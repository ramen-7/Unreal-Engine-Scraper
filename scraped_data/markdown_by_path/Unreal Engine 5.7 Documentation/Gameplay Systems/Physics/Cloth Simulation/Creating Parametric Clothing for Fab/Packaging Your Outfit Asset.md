<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-outfit-asset?application_version=5.7 -->

# Packaging Your Outfit Asset

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
9. Packaging Your Outfit Asset

# Packaging Your Outfit Asset

Packaging a MetaHuman Outfit Asset in Unreal Engine.

![Packaging Your Outfit Asset](https://dev.epicgames.com/community/api/documentation/image/d8b241b9-5c28-48a2-94c7-49ce4261cd1e?resizing_type=fill&width=1920&height=335)

 On this page

The **MetaHuman Manager** is a UI that verifies if assets are MetaHuman compatible, and generates `.mhpkg` files. Mhpkg is the format we use to upload and sell MetaHuman compatible assets on FAB. Mhpkgs from MetaHuman Manager are the only file type that is accepted by FAB when creating a listing in the new MetaHuman format. Packages can then be imported into **Unreal Engine** (UE) using the standard FAB import procedure.

## Packaging Your Outfit

1. To package your outfit, in the Unreal Editor, navigate to **Window > MetaHuman** **Manager**.

   [![UE MetaHuman Manager](https://dev.epicgames.com/community/api/documentation/image/e2824719-2135-446e-889b-bf079afb399a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2824719-2135-446e-889b-bf079afb399a?resizing_type=fit)

   MetaHuman Manager will scan the folders that are in the settings of MetaHuman Packaging Paths, and look for valid assets.
2. Your outfit should show up in the **Clothing (Outfit)** section. Click **Verify** at the bottom of the window.

   [![MetaHuman Manager](https://dev.epicgames.com/community/api/documentation/image/99c09eaf-706e-46f6-aba2-b30dcd10966d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99c09eaf-706e-46f6-aba2-b30dcd10966d?resizing_type=fit)

   Errors and warnings may appear. If an asset has errors, you will not be able to package it. If it has warnings, you will be able to package it, but it may not be an optimal asset.

   It is recommended to fix them and re-verify.
3. Once you’ve passed verification, you will be able to use the **Package** button next to it. Click **Package**, select where you’d like to save that package, and make note of that location.

   The total size (estimate shown under **Disk Size** in the image above) must be 6 GB or less. Anything larger cannot be uploaded to FAB. Ideally, it’s best to keep the package smaller, closer to the 1.5 GB range, but can be larger so long as it doesn’t exceed 6 GB.
4. To test your asset, create a blank project in Unreal Editor. Your outfit asset must be placed inside a folder structure identical to the one it was created in.

   For this tutorial, create the following structure:

   `Content/Outfits/techwearOutfit`

   The materials in your asset will break unless you create a folder structure identical to the one it was created in.
5. Drag-and-drop your packaged file into the techwearOutfit folder. You can now test your outfit asset.

## Next Step

* [![Uploading to Fab Marketplace](https://dev.epicgames.com/community/api/documentation/image/f02b51d2-0d10-4c0a-913a-a0cccc2feb9d?resizing_type=fit&width=640&height=640)

  Uploading to Fab Marketplace

  Uploading your MetaHuman to Fab Marketplace.](https://dev.epicgames.com/documentation/en-us/unreal-engine/uploading-to-fab-marketplace)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Packaging Your Outfit](/documentation/en-us/unreal-engine/packaging-your-outfit-asset?application_version=5.7#packagingyouroutfit)
* [Next Step](/documentation/en-us/unreal-engine/packaging-your-outfit-asset?application_version=5.7#nextstep)
