<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-physics-asset-in-unreal-engine?application_version=5.7 -->

# Creating a New Physics Asset

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
7. [Physics Asset Editor](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine "Physics Asset Editor")
8. [Physics Asset Editor Tutorials](/documentation/en-us/unreal-engine/physics-asset-editor-tutorial-directory-for-unreal-engine "Physics Asset Editor Tutorials")
9. Creating a New Physics Asset

# Creating a New Physics Asset

This how-to covers the procedures for creating a new Physics Asset.

![Creating a New Physics Asset](https://dev.epicgames.com/community/api/documentation/image/7640e7e3-d9a6-41d3-b828-61f8fa066176?resizing_type=fill&width=1920&height=335)

 On this page

There are two ways to create a new **Physics Asset**: on import or by using the context menu in the **Content Drawer**. Below are the steps and interfaces for both methods.

## Steps

When a Skeletal Mesh is imported, there is an option to generate a Physics Asset for it as it is imported. Once the imported file is processed, a new Physics Asset will be generated using the default properties, which can be modified using the **Physics Asset Editor**.

![An option to generate a Physics Asset for Skeletal Mesh as it is imported](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9acf6cfc-d1e8-48b9-9688-1e6e2b89144c/import-fbx-1.png)


You can choose to use an existing Physical Asset by disabling the **Create Physics Asset** checkbox, then selecting the appropriate Physics Asset using the dropdown menu.

![You can choose to use an existing Physical Asset by disabling the Create Physics Asset checkbox and select the appropriate Physics Asset using the dropdown menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed5c5a1c-a2d1-49cc-b616-caef1b5d0044/import-fbx-2.png)

However, you can follow these steps if you need to create a Physics Asset for a Skeletal Mesh at a later time:

1. in the **Content Drawer**, find the Skeletal Mesh asset to which you wish to add a Physics Asset.
2. Right-click on the **Skeletal Mesh** to open the **Context Menu**, the select **Create -> Physics Asset -> Create**.

   ![Right-click on the Skeletal Mesh to open the Context Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d76ce923-2b2a-4a18-a4fb-49bc9af4e1dc/create-physics-asset.png)
3. Adjust the properties to your liking.

   ![Adjust the properties to your liking](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab3d56da-e4e3-4fe2-8f3d-2ec108cb6a75/new-physics-asset.png)
4. Click **Create Asset**.

## Result

Upon creating a **Physics Asset** you will find it in the same folder as the **Skeletal Mesh** it is based on.

* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/creating-a-new-physics-asset-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/creating-a-new-physics-asset-in-unreal-engine?application_version=5.7#result)
