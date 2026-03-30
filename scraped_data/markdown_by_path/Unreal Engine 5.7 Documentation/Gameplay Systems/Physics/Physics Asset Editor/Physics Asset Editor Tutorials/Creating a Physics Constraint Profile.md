<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-physics-constraint-profile-in-unreal-engine?application_version=5.7 -->

# Creating a Physics Constraint Profile

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
9. Creating a Physics Constraint Profile

# Creating a Physics Constraint Profile

This how-to will show you how to create a Physics Constraint Profile using the Physics Asset Editor.

![Creating a Physics Constraint Profile](https://dev.epicgames.com/community/api/documentation/image/1ee82dec-3918-4c2b-a549-2c9b3d7e7b6d?resizing_type=fill&width=1920&height=335)

 On this page

In this How-To, we will cover the basics of creating a **Constraint Profile** and adding **Physics Constraints** to it.

## Steps

1. Find or [Create](/documentation/en-us/unreal-engine/creating-a-new-physics-asset-in-unreal-engine) a **Physics Asset** for your **Skeletal Mesh** using the **Content Drawer**.

   ![Physics Asset in the Content Drawer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/947d8198-b3e1-4b43-a805-934cd2b1b133/physics-asset.png)


   If opting to create a new **Physics Asset**, you will need to set it up before continuing.
2. Double-click the Physics Asset to open the **Physics Asset Editor**.

   ![The Physics Asset Editor main user interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f7dd9f1-6781-4655-b574-186d38ce9604/physics-asset-editor.png)
3. Under the **Windows** menu, select **Profiles**; the **Profiles** window should appear as a docked tab.

   ![Windows menu with Profiles highlighted](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e26c58ea-f1a8-4bd5-82c8-10c4f9d2993f/profiles-window-menu.png)
4. Add a **Profile** using the **New** button on the **Constraints Profiles** section, and set its name (in the image below we've named it `DocsConstraintProfile`).

   ![Adding and naming a new Constraints Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7148c83d-c1b4-416d-9ec0-3810dbf82cd1/docs-constraint-profile.png)
5. Select the **Physics Constraint** you want to include in your new **Constraint Profile** in the **Skeleton Tree** panel, the **Physics Graph** panel, or the **Viewport**.

   To see Constraints in the Skeleton Tree panel, select **Show Constraints** in the **Options** dropdown menu.
6. Press the **Assign** button in the **Profiles** panel.

   ![Assigning Constraints to a Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/074c8dfd-8121-449a-acca-d692919f036c/assign-constraints-to-profile-2.png)

   1 - Assign a button
   2 - Constraints selected in the Skeleton Tree panel
   3 - Constraints selected in the Physics Graph panel
   4 - Constraints selected in the Viewport
7. Adjust the properties for the selected **Physics Constraints**.

   ![Adjusting Physical Constraint Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ddb7925-0887-460e-8975-7d6dd9b83ef3/physics-constraints-profile-adjust.png)
8. Repeat steps 5-7 for all the **Physics Constraints** you want to add to the **Constraint Profile**.

   You can select, assign, and edit the Properties of multiple Constraints simultaneously. You only need to edit them individually if you want their Properties to be different.
9. Save your **Physics Asset** using the **Save** button in the **Physics Asset Editor**.

   ![Save your Physics Asset using the Save button in the Physics Asset Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99122110-e34c-497a-ad23-64b3cb7b9eec/save-button.png)

You can edit an existing Constraints Profile by selecting it in the dropdown menu, then using **Assign** to add new Constraints, or using **Unassign** to remove existing Constraints.

## Result

The **Physics Asset** now has a profile that can be called upon from Blueprint or C++ to change its **Physical Constraint** properties.

## Additional Resources

* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/creating-a-physics-constraint-profile-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/creating-a-physics-constraint-profile-in-unreal-engine?application_version=5.7#result)
* [Additional Resources](/documentation/en-us/unreal-engine/creating-a-physics-constraint-profile-in-unreal-engine?application_version=5.7#additionalresources)
