<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-physics-body-in-unreal-engine-by-using-the-physics-asset-editor?application_version=5.7 -->

# Creating a New Physics Body in the Physics Asset Editor

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
9. Creating a New Physics Body in the Physics Asset Editor

# Creating a New Physics Body in the Physics Asset Editor

This how-to covers the procedures for creating new Physics Bodies in a Physics Asset using the Physics Asset Tool.

![Creating a New Physics Body in the Physics Asset Editor](https://dev.epicgames.com/community/api/documentation/image/1ee03ef1-ef29-4910-8b83-403d5238d01b?resizing_type=fill&width=1920&height=335)

 On this page

The Physics Asset Tool enables you to add or replace the **Physics Bodies** and their associated **Shapes** (**Boxes**, **Spheres**, **Capsules**, **Tapered Capsules**, and so on) attached to the **Bones** make up your Physics Asset.

By default, the **Physics Editor Skeleton Tree** panel only shows the Physics Bodies. Adding and replacing Physics Bodies is easier if you use the **Options** dropdown menu in the Skeleton Tree panel to show the **Bones** and **Primitives** as well.

## Adding Physics Bodies to Bones

![The right-click context menu for a bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e98cc6dc-6b50-4127-ac31-55fcb27ff21d/add-body.png)

1. Right-click on a **Bone** in the **Skeleton Tree** panel, then click on **Add/Replace Body** in the **Context Menu**.

   * You can also right-click on a **Bone** in the **VIewport** to open the Context Menu.
2. A new Physics Body will be added to the Bone, with the default Capsule Shape attached.

   * If there was already a Physics Body attached to the Bone, the new Physics Body and Capsule Shape will replace it.
3. Alternatively, when starting with a Bone with no attached Physics Body, you can directly select one of the shapes under **Add Shape** in the **Context Menu**. This will create a new Physics Body with the selected Shape attached.
4. If you right-click on a **Physics Body** and select **Regenerate Bodies**, a new Physics Body with a default Capsule Shape attached will be created to replace every currently-selected Physics Body.

## Adding Shapes to Physics Bodies

![The right-click context menu for a physics body](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2be66b1b-7ec6-4760-ae41-ab060b0ae674/add-shape.png)

To add a Shape to an existing Physics Body, right-click the Physics Body, then under **Add Shape** in the **Context Menu**, select the Shape you wish to add.

* A Physics Body can have more than one attached Shape, so delete the default Capsule if you do not want it to remain attached to the Physics Body.

## Result

You should see that a corresponding body and shape have been added (and parented) to the selected bone.

* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding Physics Bodies to Bones](/documentation/en-us/unreal-engine/creating-a-new-physics-body-in-unreal-engine-by-using-the-physics-asset-editor?application_version=5.7#addingphysicsbodiestobones)
* [Adding Shapes to Physics Bodies](/documentation/en-us/unreal-engine/creating-a-new-physics-body-in-unreal-engine-by-using-the-physics-asset-editor?application_version=5.7#addingshapestophysicsbodies)
* [Result](/documentation/en-us/unreal-engine/creating-a-new-physics-body-in-unreal-engine-by-using-the-physics-asset-editor?application_version=5.7#result)
