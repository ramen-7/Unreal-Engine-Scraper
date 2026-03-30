<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/editing-physics-asset-constraints-in-unreal-engine?application_version=5.7 -->

# Editing Physics Asset Constraints

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
9. Editing Physics Asset Constraints

# Editing Physics Asset Constraints

This tutorial covers the procedures for editing the Physics Constraints of a Physics Asset.

![Editing Physics Asset Constraints](https://dev.epicgames.com/community/api/documentation/image/9c104146-3adf-4901-9aa8-4b9143b3376c?resizing_type=fill&width=1920&height=335)

 On this page

Below are several common procedures, and steps, associated with editing **Physics Constraints** in the **Physics Asset Editor**.

## Editing Physics Constraints

The use of Physics Constraints is covered in the [Physics Constraints User Guide](/documentation/en-us/unreal-engine/constraints-user-guide-in-unreal-engine) and their properties are covered in the [Physics Constraint Reference](/documentation/en-us/unreal-engine/physics-constraint-reference-in-unreal-engine). This section will only cover workflows that are specific to the Physics Asset Tool or ones that have deviated substantially from the norm.

1. Double-click your **Physics Asset** to open it in the Physics Asset Editor.
2. Select a **Physics Constraint** in the **Viewport** or in the **Skeleton Tree** panel.
3. **Move and rotate** the Physics Constraint using the **Translation** and **Rotation** tools to create the rotational point of the "joint" the Physics Constraint will form.
4. Edit the Physics Constraint's properties in the **Details** panel.

   You can switch Swing1, Swing2, and Twist from Limited to Locked quickly by using the "**1**", "**2**", and "**3**" keys respectively. The "**4**" key can be used cycle through
   them setting one to limited and the other two to locked.
5. **Save** often.

See the [Physics Constraint Reference](/documentation/en-us/unreal-engine/physics-constraint-reference-in-unreal-engine) for more information on the Physics Constraint properties in the Physics Asset Editor.

## Aligning Physics Constraints

If you are using the Physics Constraint's **Linear** or **Angular** limits, you will be able to see their alignment:

![You will be able to see  alignment](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ab7bc10-892c-4904-8a4e-a239bc468046/physics-asset-user-guide-limits.png)

By then translating and rotating the Physics Constraint, you can align the limits to give the desired results. In the most basic of terms, when a Physics Constraint is limited, you can see a yellow line suspended in a green arc or cone structure. The line will be "constrained" within this arc or cone.

For more information on Physics Constraints and their properties, see the [Physics Constraints User Guide](/documentation/en-us/unreal-engine/constraints-user-guide-in-unreal-engine).

## Copying Physics Constraints

While in either mode, properties from one Constraint can be copied to other Constraints:

1. Select the **Physics Constraint** you wish to copy data from.
2. **Press Ctrl + C**.
3. Select **Physics Constraints** you wish to apply data to.
4. **Press Ctrl + V**.

## Deleting Physics Constraints

There is no easy way to recreate a Physics Constraint, be mindful of this when deleting them.

1. Double-click your **Physics Asset** to open it in the Physics Asset Editor.
2. Select the **Physics Constraint** you want to delete in the **Viewport** or in the **Skeleton Tree** panel.
3. Press the **Delete** key.

## Recreating a Physics Constraint

There is no easy way to recreate a Physics Constraint, be mindful of this when deleting them.

Physics Constraints are only created on the generation of a Physics Body and are only generated upstream. So, if you remove a Physics Constraint from the shoulder, you would have to remove the upper arm Physics Body (which will remove the elbow Physics Constraint), then re-create the upper arm Physics Body. This would create the shoulder Physics Constraint, but not the elbow Physics Constraint, so you would have to continue this process down the arm.

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [constraint](https://dev.epicgames.com/community/search?query=constraint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Editing Physics Constraints](/documentation/en-us/unreal-engine/editing-physics-asset-constraints-in-unreal-engine?application_version=5.7#editingphysicsconstraints)
* [Aligning Physics Constraints](/documentation/en-us/unreal-engine/editing-physics-asset-constraints-in-unreal-engine?application_version=5.7#aligningphysicsconstraints)
* [Copying Physics Constraints](/documentation/en-us/unreal-engine/editing-physics-asset-constraints-in-unreal-engine?application_version=5.7#copyingphysicsconstraints)
* [Deleting Physics Constraints](/documentation/en-us/unreal-engine/editing-physics-asset-constraints-in-unreal-engine?application_version=5.7#deletingphysicsconstraints)
* [Recreating a Physics Constraint](/documentation/en-us/unreal-engine/editing-physics-asset-constraints-in-unreal-engine?application_version=5.7#recreatingaphysicsconstraint)
