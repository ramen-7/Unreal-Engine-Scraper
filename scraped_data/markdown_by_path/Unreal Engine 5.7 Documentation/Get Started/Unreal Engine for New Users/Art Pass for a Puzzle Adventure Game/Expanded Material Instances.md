<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7 -->

# Expanded Material Instances

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game "Art Pass for a Puzzle Adventure Game")
8. Expanded Material Instances

# Expanded Material Instances

Use dynamic material instances to create an interactive tech demo.

![Expanded Material Instances](https://dev.epicgames.com/community/api/documentation/image/51065f3e-2f47-4003-959a-cc6f6237181a?resizing_type=fill&width=1920&height=335)

 On this page

Changing an asset’s material properties during gameplay is a useful way to give the player visual feedback, gameplay information, or create immersion. For example:

* Player skins can change looks to signal different status effects.
* Pickups can shine to attract attention from nearby players.
* During rain, the ground turning from dry to wet can increase immersion.

[![](https://dev.epicgames.com/community/api/documentation/image/40d44538-133d-4c97-a727-7fc2a96eb562?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40d44538-133d-4c97-a727-7fc2a96eb562?resizing_type=fit)

A character's arm becomes emissive after a powerup.

In this tutorial, you’ll use **Blueprints** to change Material properties at runtime in an interactive tech demo. For this demo, you’ll create a ball of water that soaks the floor as the player pushes it around the level.

[![](https://dev.epicgames.com/community/api/documentation/image/adef914d-01eb-417f-86fb-a772dd81a6b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/adef914d-01eb-417f-86fb-a772dd81a6b9?resizing_type=fit)

You’ll also experiment with **emissive materials**, simple **masks**, and **static switches** to create set dressing that reflects off the wet floor.

[![](https://dev.epicgames.com/community/api/documentation/image/928599e7-dec1-4f40-becc-e97edc4c6193?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/928599e7-dec1-4f40-becc-e97edc4c6193?resizing_type=fit)

## Create a Game-Ready Floor Asset

The first asset you'll build for the tech demo will be the floor. In Room 3 of **Lvl\_Adventure**, you’ll create a surfaced, game-ready floor asset to replace the placeholder floor mesh.

[![Placeholder-floor-mesh-of-Room-3](https://dev.epicgames.com/community/api/documentation/image/f741eb46-c668-4299-8e0f-6815e6c8cd28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f741eb46-c668-4299-8e0f-6815e6c8cd28?resizing_type=fit)

Placeholder floor mesh of Room 3.

Before you begin, let’s pause to consider your approach. In the [previous tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances#reuse-material-instances), you learned that **tiling** **textures** are an inexpensive way to surface large meshes such as a floor. You also learned that a mesh’s [UVs](https://dev.epicgames.com/documentation/en-us/unreal-engine/uvs-category-in-unreal-engine) affect how textures appear.

[![](https://dev.epicgames.com/community/api/documentation/image/00f0045c-6da3-4796-a167-6b0c4cd19dc7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00f0045c-6da3-4796-a167-6b0c4cd19dc7?resizing_type=fit)

(1) Appropriately scaled material. (2) Uniformly scaled-up material. (3) Non-uniformly scaled-up material.

The placeholder floor in Room 3 is made up of three meshes and each one has different UVs.

In the demonstration below, notice that the tiling textures seem to be different sizes because of UV inconsistencies between the meshes. This poses a challenge for cohesively surfacing the floor.

[![Floor-pattern-sliding-over-platforms](https://dev.epicgames.com/community/api/documentation/image/475ba245-e05c-4477-8453-d8030bc78490?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/475ba245-e05c-4477-8453-d8030bc78490?resizing_type=fit)

Scaling a non-world-aligned texture across meshes with different UVs.

You’ll solve this challenge by using **triplanar projection**. Triplanar projection is a surfacing technique that disregards UVs and makes a texture **world-aligned**. This is useful for cases when you cannot correct UVs or are working with geometry that’s difficult to UV map.

[![Floor-pattern-moving-over-platforms](https://dev.epicgames.com/community/api/documentation/image/e6858217-9674-4705-bfb7-2c10f0db753e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e6858217-9674-4705-bfb7-2c10f0db753e?resizing_type=fit)

Scaling a world-aligned texture across meshes with different UVs.

With this approach in mind, you’ll use **expressions** to make `M_Surfaces` world-aligned. Because instances inherit properties from parent Materials, `MI_Surfaces_Floor` will be world-aligned as well. Then, you’ll apply `MI_Surfaces_Floor` to a blueprint that will replace the placeholder meshes.

To avoid UV issues in advance, we recommend scaling your UVs appropriately across modular assets when creating them in modeling software.

### Create a World-Aligned Material

To make your parent Material world-aligned, follow these steps:

1. In the **Content Browser**, navigate to **All > Content > AdventureGame > Artist > Materials** and open `M_Surfaces`.
2. Select all nodes in the **UV Tiling** comment box, the diffuse map, and normal map. **Delete** them.

   ![Delete-the-UV-box-and-2-maps](https://dev.epicgames.com/community/api/documentation/image/5489496f-9be6-4787-8448-2d6d8e5ac76b?resizing_type=fit)
3. Right-click the graph and search for [Texture Object](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine). Create two of these nodes.

   ![Create-2-texture-target-nodes](https://dev.epicgames.com/community/api/documentation/image/d5c44299-43dc-44d9-bad4-924833388555?resizing_type=fit)
4. Select the first **Texture Object**. In the **Details** panel, set its **Texture** to **DefaultDiffuse**.
5. Right-click the **Texture Object** and select **Convert to Parameter**. Name the new parameter `Diffuse`.
6. Select the second **Texture Objec**t. In the **Details** panel, set its **Texture** to **DefaultNormal**.
7. Right-click the **Texture Object** and select **Convert to Parameter**. Name the new parameter `Normal`.
8. On the **Diffuse** node, drag from the output and add a **World Aligned Texture** node.

   ![Add-world-aligned-texture-mode](https://dev.epicgames.com/community/api/documentation/image/a0031b61-0e76-4e27-a2b8-e46b7d6652a4?resizing_type=fit)
9. From the **XYZ Texture** output, connect it to the **A** input of the **Multiply** node (inside the Diffuse Hue comment box).
10. On the **Normal** node, drag from the **output** and add a **World Aligned Normal** node.
11. From the **XYZ Texture** output, connect it to the **Normal** input of the **M\_Surfaces** material root node.
12. Right-click in the graph and search for **Scalar Parameter**. Name it `Texture Scaling`.
13. Set its **Default Value** to `214`.
14. Connect the output from **Texture Scaling** to the **TextureSizeV3** inputs on both **WorldAligned** nodes.
15. **Save** your Material.

Your Material Graph should now look like this:

[![Finished-graph-with-all-nodes-shown](https://dev.epicgames.com/community/api/documentation/image/f1e49d97-3853-4876-94c8-8586709cd979?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1e49d97-3853-4876-94c8-8586709cd979?resizing_type=fit)

Next, you’ll create a blueprint that will replace the placeholder floor.

### Create a Floor Blueprint

To create the blueprint, follow these steps:

1. In the **Content Browser**, at the path **All > Content > AdventureGame > Artist**, right-click and select **New Folder**.
2. Name the folder `Blueprints`.
3. Right-click in the **Blueprints** folder, select **Blueprint Class**, and select **Actor** as the Parent Class.
4. Name the blueprint `BP_Floor` and double-click to open it in the **Blueprint Editor**.
5. In the Content Browser, select the **All** folder, and search for `SM_Cube`.

   [![SM-cube-in-the-content-browser](https://dev.epicgames.com/community/api/documentation/image/3a841036-c318-432b-a13d-e68fe568050a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a841036-c318-432b-a13d-e68fe568050a?resizing_type=fit)
6. Drag **SM\_Cube** into the **Components** panel of the Blueprint Editor, as a child of **BP\_Floor**.

   ![Drag-SM-cube-to-the-editor](https://dev.epicgames.com/community/api/documentation/image/0d4f881a-2f31-4b66-9a81-23a81c6a5601?resizing_type=fit)
7. Name the SM\_Cube `Floor`.
8. In the **Details** panel, ensure that its **Scale** is `1.0, 1.0, 1.0`.
9. Next to **Materials > Element 0**, set its material to `MI_Surfaces_Floor`.

   [![Materials-setting-in-the-details-tab](https://dev.epicgames.com/community/api/documentation/image/894ab43b-7104-42da-b9a0-01b26490235e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/894ab43b-7104-42da-b9a0-01b26490235e?resizing_type=fit)
10. In the **Components** tab, select **DefaultSceneRoot**, click **Add**, and add a `Box Collision`.
11. Name the box collision `Trigger`.

    [![Box-collision-named-trigger](https://dev.epicgames.com/community/api/documentation/image/b03dc250-1a99-4d96-9a23-78b05ca94438?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b03dc250-1a99-4d96-9a23-78b05ca94438?resizing_type=fit)
12. In the **Details** panel, set Trigger’s **Scale** to `1.5, 1.5, 1.5`.
13. Set Trigger’s Location to `50, 50, 55`.
14. **Save** and **Compile** your blueprint.

Drag an instance of `BP_Floor` into your level and move it around. Notice that as you move the mesh, the texture stays in the same place. If you try scaling it, the mesh changes but the texture does not.

[![](https://dev.epicgames.com/community/api/documentation/image/86d20b2e-2415-4a7a-94ce-624142b1c0ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86d20b2e-2415-4a7a-94ce-624142b1c0ea?resizing_type=fit)

Next, you’ll replace the placeholder flooring in Room 3 with instances of `BP_Floor`.

### Replace the Placeholder Meshes

You can now replace the placeholder meshes in Room 3 with `BP_Floor` in whatever arrangement you prefer. We created a floor that matches the placeholders:

[![Surfaced Floor](https://dev.epicgames.com/community/api/documentation/image/44f4ddb5-75f5-47da-a6cd-06c5470d7f1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/44f4ddb5-75f5-47da-a6cd-06c5470d7f1a?resizing_type=fit)

If you prefer to use what is shown above, you can copy this level by following these steps:

1. Verify that you’ve updated `M_Surfaces` and created `BP_Floor` per the tutorial above.
2. In the **Outliner**, select everything inside the Room 3 folder, and press **Delete**.
3. **Copy** the following snippet.

   Console Output

   ```
   Begin Map
      Begin Level
         Begin Actor Class=/Script/Engine.StaticMeshActor Name=StaticMeshActor_2 Archetype="/Script/Engine.StaticMeshActor'/Script/Engine.Default__StaticMeshActor'" ExportPath="/Script/Engine.StaticMeshActor'/Game/SFEFWFWEEEWEF.SFEFWFWEEEWEF:PersistentLevel.StaticMeshActor_2'"
            Begin Object Class=/Script/Engine.StaticMeshComponent Name="StaticMeshComponent0" Archetype="/Script/Engine.StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/SFEFWFWEEEWEF.SFEFWFWEEEWEF:PersistentLevel.StaticMeshActor_2.StaticMeshComponent0'"
            End Object
            Begin Object Name="StaticMeshComponent0" ExportPath="/Script/Engine.StaticMeshComponent'/Game/SFEFWFWEEEWEF.SFEFWFWEEEWEF:PersistentLevel.StaticMeshActor_2.StaticMeshComponent0'"
               StaticMesh="/Script/Engine.StaticMesh'/Game/LevelPrototyping/Meshes/SM_Cylinder.SM_Cylinder'"
               StaticMeshImportVersion=1
               bUseDefaultCollision=False
               StaticMeshDerivedDataKey="STATICMESH_FD1BFC73B5510AD60DFC65F62C1E933E_228332BAE0224DD294E232B87D83948FQuadricMeshReduction_V2$2e1_6D3AF6A2$2d5FD0$2d469B$2dB0D8$2dB6D9979EE5D2_CONSTRAINED0_100100000000000000000000000100000000000080FFFFFFFFFFFFFFFFFFFFFFFF000000000000803F00000000000000803F0000803F00000000000000003D19FC1626C9B2485E57DB4B8EC731318B8215AE8D46FAD400000000010000000100000000000000010000000100000000000000000000000100000001000000400000000000000001000000000000000000F03F000000000000F03F000000000000F03F0000803F00000000050000004E6F6E65000C00000030000000803FFFFFFFFF0000803FFFFFFFFF0000000000000041000000000000A0420303030000000000000000_RT00_0"
   ```

   Expand code  Copy full snippet(2319 lines long)
4. In the **Viewport**, press **Ctrl + V**.

   ![](https://dev.epicgames.com/community/api/documentation/image/7f0119a0-ae83-4b0b-a43e-5f9070f28422?resizing_type=fit)

Next, you’ll create the water ball and use **Dynamic Materials Instances** to turn the floor from dry to wet.

## Change Materials Using Player Interaction

The water ball will be a physics-enabled object that triggers a property change in the floor, making it appear wet.

[![](https://dev.epicgames.com/community/api/documentation/image/de1e460c-cce0-48ba-95ca-4584c8d1b236?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de1e460c-cce0-48ba-95ca-4584c8d1b236?resizing_type=fit)

### Create a Water Ball

To create and surface the water ball, follow these steps:

1. In the **Content Browser**, in the **Blueprints** folder, right-click to create a new **Blueprint Class**.
2. Select **Actor** as the Parent Class.
3. Name the new blueprint `BP_WaterBall` and open it in the **Blueprint Editor**.
4. In the **Components** tab, click **Add** and search for `Sphere`.
5. In the **Details** panel, set **Materials > Element 0** to `M_Water`.

   `M_Water` comes with the Unreal Engine; you do not have to download or create it. If you don’t see this asset, click the **Settings** button in the asset picker or Content Browser, and enable **Plugin Content**.

   [![Enabling-plugin-content-checkmark](https://dev.epicgames.com/community/api/documentation/image/db3521b5-3e3e-4939-ac86-7481f3c3b521?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db3521b5-3e3e-4939-ac86-7481f3c3b521?resizing_type=fit)
6. Still in the **Details** panel, under **Physics**, check **Simulate Physics**.

   [![Simulate-physics-checkbox-selected](https://dev.epicgames.com/community/api/documentation/image/3888ddbd-9701-46c6-be93-1e13dfa28371?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3888ddbd-9701-46c6-be93-1e13dfa28371?resizing_type=fit)
7. **Save** and **Compile** your blueprint.
8. Drag an instance of `BP_WaterBall` into your level.

Test the water ball in your level by right-clicking in the Viewport and selecting **Play From Here**. The ball should bounce along the ground when you run into it.

[![](https://dev.epicgames.com/community/api/documentation/image/42dcebca-636c-44e5-a589-41705400c26a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/42dcebca-636c-44e5-a589-41705400c26a?resizing_type=fit)

If there are enemies your level, set their **Max Speed** to `0` to avoid them chasing you, or remove them.

Next, you’ll use logic within `BP_Floor` to create a Dynamic Material Instance.

### Create a Dynamic Material Instance

A [Dynamic Material Instance](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine) is a material instance generated by script (such as Blueprint) that can change its properties at runtime.

In this section, you'll create Blueprint logic that references the Material assigned to the Floor mesh (`MI_Surfaces_Floor`), generates a Dynamic Material Instance from it, and assigns the new instance to the Floor. Then, the Dynamic Material Instance alters the properties that you exposed in the [previous tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances#convert-static-values-to-parameters), Roughness and Diffuse Hue, to mimic a wet floor.

During runtime, this swap will make it appear as if the floor becomes soaked with a thin layer of water.

[![](https://dev.epicgames.com/community/api/documentation/image/3b97aafe-8fb2-4af5-9aa9-899fbf57b341?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3b97aafe-8fb2-4af5-9aa9-899fbf57b341?resizing_type=fit)

To create a dynamic material instance, follow these steps:

1. In the **Content Browser**, double-click `BP_Floor` to open it in the **Blueprint Editor**.
2. In the **EventGraph**, delete all nodes except for **Event BeginPlay**.
3. From the **Components** tab, drag an instance of **Floor** into the EventGraph.
4. From the **output** of **Floor**, drag off and search for **Get Material**.

   ![](https://dev.epicgames.com/community/api/documentation/image/3181eee7-847b-4cec-b46e-440e16aea570?resizing_type=fit)
5. From the **Return Value** output of **Get Material**, drag off and add a **Create Dynamic Material** **Instance** node where the target is Kismet Material Library.

   [![Bueprint-of-return-value](https://dev.epicgames.com/community/api/documentation/image/71dfa483-4359-4e98-91c4-face0a84f827?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/71dfa483-4359-4e98-91c4-face0a84f827?resizing_type=fit)
6. Connect the **output** of **Event BeginPla****y** to the **input Exec pin** of **Create Dynamic Material Instance**.

   ![](https://dev.epicgames.com/community/api/documentation/image/1d8c7f4c-3aad-4977-b84d-9d19a6919e7b?resizing_type=fit)
7. From the **Return Value** of the **Dynamic Material Instance**, drag out and select **Promote to Variable**.
8. In the **Details** panel, rename this variable as `Dynamic Mat Ref`.
9. Drag another instance of **Floor** into the EventGraph.
10. From Floor’s **output**, drag off and search for **Set Material**.
11. Connect the **white Exec output** on the Set node to the **Exec input** of the Set Material node.
12. Connect the **blue output** on the Set node to the **Material input** of the Set Material node.

    ![Connect-the-set-node-to-the-set-material-node](https://dev.epicgames.com/community/api/documentation/image/ca807980-f8a6-4681-9f3b-bd96bccd125a?resizing_type=fit)
13. To keep your graph organized, select all nodes and press **C**. Name the comment box `Create Dynamic Material`.
14. **Save** and **Compile**.

Your EventGraph should now look like this:

[![Final-event-graph](https://dev.epicgames.com/community/api/documentation/image/1e9c9ec7-56b7-4bf3-a90e-7b2b14896b80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e9c9ec7-56b7-4bf3-a90e-7b2b14896b80?resizing_type=fit)

### Call Events

To trigger the floor’s wet look, you’ll need an **event** that checks if `BP_Floor` is overlapping `BP_WaterBall` and an event that calls the correct look as a result.

Let’s draft the logic:

* When an actor overlaps `BP_Floor`:

  + Check if the other actor is (equal to) `BP_WaterBall`. If it is (true), then:

    - Call `BP_Floor`’s wet look.
  + Else, if it’s not true (false) then:

    - Do nothing.

To create this logic, follow these steps:

1. Right-click in `BP_Floor`’s **EventGraph** and search for **Add Custom Event**. Name this node `Call Wet Look`.
2. In the **Components** tab, right-click on **Trigger** and create **Add Event > Add OnComponentBeginOverlap**.

   [![Add-event-on-trigger](https://dev.epicgames.com/community/api/documentation/image/b27a5f28-2b2c-4960-b019-4fbaa143de9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b27a5f28-2b2c-4960-b019-4fbaa143de9e?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/ce59b28a-3bfc-4b23-a586-b57bdd3ad7ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce59b28a-3bfc-4b23-a586-b57bdd3ad7ba?resizing_type=fit)

   **OnComponentBeginOverlap** looks for collision.
3. From the **Other Actor** output in **OnComponentBeginOverlap**, drag out and create **Get Class**.
4. From the **Return Value** output, drag out and create **Equal**.
5. Right-click the **Select Class** input and select **Promote to Variable**.
6. Name the variable `WaterBall` and **Compile** your blueprint.

   [![Trigger-node-with-function-to-get-water-ball](https://dev.epicgames.com/community/api/documentation/image/df30b86a-bfc6-4c48-9f9c-ec7a26d95d99?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df30b86a-bfc6-4c48-9f9c-ec7a26d95d99?resizing_type=fit)
7. In the **Details** panel, set the **Default Value** of WaterBall to `BP_WaterBall`.

   [![Set-default-variable-name-to-water-ball](https://dev.epicgames.com/community/api/documentation/image/20ca67df-0a05-4bbe-b462-5f9f3986ffd0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20ca67df-0a05-4bbe-b462-5f9f3986ffd0?resizing_type=fit)
8. From the **output** of the **Equal** node, drag out and create a **Branch**.
9. From the **True** output from the **Branch**, drag out and search for **Call Wet Look**.
10. Connect the **Exec output** from **OnComponentBeginOverlap** to the **E****xec input** in the **Branch** node.

Your EventGraph should now look like this:

[![Trigger-to-branch-to-call-wet-look](https://dev.epicgames.com/community/api/documentation/image/8c081608-f70d-44e2-82ba-1fbe23072da1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c081608-f70d-44e2-82ba-1fbe23072da1?resizing_type=fit)

### Control Material Properties

Now, you'll build the wet variation of your floor. Since the floor is stone-like and porous, it should darken as it absorbs water (**Diffuse Hue**). Due to a thin layer of water sitting on top, the surface should appear glossy (**Roughness**).

To build logic for the wet look, follow these steps:

1. Drag **Dynamic Mat Ref** variable into the EventGraph and select **Get** from the list.

   ![Dynamic-mat-ref-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/324333b2-29f8-4048-942f-14bd99454ff6?resizing_type=fit)
2. From the **output** pin, drag out and create **Set Scalar Parameter Value**.
3. From the same **output** pin, drag out and create **Set Vector Parameter Value**.

   Remember the parameters you [exposed](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances#convert-static-values-to-parameters) in `M_Surfaces`? **Roughness** is a **scalar** (single value) and **Diffuse Hue** is a **vector** (three values; the RGB).
4. On the **Set Scalar Parameter Value** node, right-click **Parameter Name** and select **Promote to Variable**. Name the variable `Roughness`.
5. On the **Set Vector Parameter Value** node, right-click **Parameter Name** and select **Promote to Variable**. Name the variable `Diffuse Hue`.
6. **Compile** the blueprint and enter values for each parameter name:

   1. Select the Roughness variable and enter `Roughness` as its Default Value.
   2. Select the **Diffuse Hue** variable and enter `Diffuse Hue` as its **Default Value**.

      [![Default-value-for-roughness-and-diffuse-hue](https://dev.epicgames.com/community/api/documentation/image/9ceafced-c972-48c1-bcf4-058f6eaa7d9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9ceafced-c972-48c1-bcf4-058f6eaa7d9e?resizing_type=fit)

      The Default Values must match the corresponding parameters in `M_Surfaces`.
7. Connect the **output Exec** pin from the **Set Scalar Parameter Value** node to the **input Exec** of the **Set Vector Parameter Value** node.

   [![Connect-set-scaler-node-to-set-vector-node](https://dev.epicgames.com/community/api/documentation/image/50d16797-50a3-4d06-a6c6-730de6efce79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50d16797-50a3-4d06-a6c6-730de6efce79?resizing_type=fit)

In addition to turning from dry to wet, you can use logic to control how quickly that change occurs. Since saturating a substance takes time, you’ll gradually transition the material properties from one to another. You can do this with a linear interpolation (**lerp**) node.

A **Lerp** node blends, or **interpolates**, smoothly between two values. It's useful for fading from one color, texture, or effect to another.

To create a lerp, follow these steps:

1. From the **Value** input of the Scalar Parameter node, drag out and create a **Lerp**. This will control **Roughness**.

   ![](https://dev.epicgames.com/community/api/documentation/image/b2600807-eca4-4303-b8dd-07ed36896437?resizing_type=fit)
2. On the Lerp, set the **A** value to `1.0`. This will be the value of Roughness for the **dry look**. Leave the **B** value at `0.0`. This will be the value of the **wet look**.

   In the [previous tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances#control-properties-through-constants), you learned that Roughness set to 1 is matte and 0 is glossy. You want your water to look glossy.
3. From the **Value** input of the **Set Vector Parameter Value** node, drag out and create a **Lerp (Linear Color)**. This will control **Diffuse Hue**.

   ![](https://dev.epicgames.com/community/api/documentation/image/95d351aa-c3af-4724-a8ad-8dd6cdb540ae?resizing_type=fit)
4. From the **A** value of the new **Lerp**, drag out and select **Promote to Variable** (linear color). Name the variable **Unsaturated**.

   ![](https://dev.epicgames.com/community/api/documentation/image/f5f3e033-4d18-4fb0-9aa8-72cebbc72543?resizing_type=fit)
5. From the **B** value of the **Lerp**, drag out and select **Promote to Variable**. Name the variable `Saturated`.
6. **Compile** your blueprint. In the **Details** panel, set the default value of **Unsaturated** to `CDDAFFFF`.

   [![Details-panel-showing-unsaturated-color](https://dev.epicgames.com/community/api/documentation/image/88550bfd-4910-4f09-a434-8cd2dd5685d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88550bfd-4910-4f09-a434-8cd2dd5685d6?resizing_type=fit)
7. In the **Details** panel, set the default value of **Saturated** to something darker, such as `656C7FFF`.

Your EventGraph should now look like this:

[![Blueprint-of-event-graph](https://dev.epicgames.com/community/api/documentation/image/24088a30-80eb-479a-a8d5-ae3122c86b56?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24088a30-80eb-479a-a8d5-ae3122c86b56?resizing_type=fit)

You’ve now created a brand new look for the floor using blueprint logic. However, you’re missing an engine to power this logic: a **Timeline**.

### Power Your Logic with Timelines

Much like the timeline in animation software, **Timeline** nodes drive values between keyframes over time. You’ll use this node to power the interpolation between the dry and wet looks over a specified amount of time.

To create a timeline, follow these steps:

1. Right-click in the EventGraph, search for and create **Add Timeline**.

   ![Create-add-timeline](https://dev.epicgames.com/community/api/documentation/image/fa976ad8-4b06-4032-bea3-24defaa430ee?resizing_type=fit)
2. Double-click the **Timeline** node to open the **Timeline\_Template** tab.
3. Click **Track**, and select **Add Float Track** from the list.
4. Name the track `Alpha`. This track name will appear as an output pin on the Timeline node.
5. Set the timeline **Length** to `3.0` seconds.

   [![Save-timeline-length](https://dev.epicgames.com/community/api/documentation/image/b179b916-5c12-43c1-b809-44500ca86420?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b179b916-5c12-43c1-b809-44500ca86420?resizing_type=fit)
6. Right-click in the timeline and select **Add Key**.
7. With the key selected and highlighted in blue, set the **Time** and **Value** for this key to `0.0`.

   [![Setting-the-time-and-value](https://dev.epicgames.com/community/api/documentation/image/bad9f422-d4b0-4e53-b141-6dff5c65f5e4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bad9f422-d4b0-4e53-b141-6dff5c65f5e4?resizing_type=fit)
8. Create a second key and set its **Time** and **Value** to `1.0`.
9. Right-click the first **key** and select **User**.

   [![Right-click-menu-to-select-user](https://dev.epicgames.com/community/api/documentation/image/a418ea31-06c7-4224-8a16-807c6ba8087e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a418ea31-06c7-4224-8a16-807c6ba8087e?resizing_type=fit)

   The **User** setting gives you control over the animation’s easing. We chose to slowly increase the speed of the saturated effect.

   [![Graph-showing-effect-increasing-over-time](https://dev.epicgames.com/community/api/documentation/image/79e92e31-93b4-458c-a4e4-d0d732a5244e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79e92e31-93b4-458c-a4e4-d0d732a5244e?resizing_type=fit)
10. **Save** and **Compile**.

This timeline now outputs a value that blends from 0 – 1 over three seconds. Now, you can connect your remaining nodes to the Timeline:

1. Back in the **EventGraph**, connect the **Call Wet Look** output to the **Play** input on the **Timeline**.
2. Connect the **Update** output on the **Timeline** to the **Exec input** of the **Set Scalar Parameter Value**.
3. Connect the **Timeline’s Alpha** output to the **Alpha** inputs on both **Lerps**.

   ![](https://dev.epicgames.com/community/api/documentation/image/6ddb623e-bada-4dbe-9732-918f24a9993c?resizing_type=fit)
4. Select the nodes and press **C** to comment. Name the comment box `Lerp Dynamic Materials`.

   [![Dynamic-lerp-comment-box-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/f11e6e5e-038b-4d5a-8129-22ea41aaaf41?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f11e6e5e-038b-4d5a-8129-22ea41aaaf41?resizing_type=fit)
5. **Save** and **Compile**.

Your complete EventGraph should now look like this:

[![Node-structure-in-three-comment-boxes](https://dev.epicgames.com/community/api/documentation/image/6ed542f5-8302-4287-a851-1c8e57886fd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6ed542f5-8302-4287-a851-1c8e57886fd1?resizing_type=fit)

To test your work, right-click in your level and select **Play From Here**. When you push the water ball around the room, the floor should “flood.”

The reflectiveness of the wet surface is a little difficult to see in daylight. To show off the floor’s reflectivity, you’ll make the level darker and add lighting using an **Emissive Material**.

## Emissive Materials

**Emissive Materials** are an inexpensive way to create self-illumination. They can be used for creating glow that’s incorporated into more complex materials, such as LEDs on a character’s sci-fi armor or a car’s brake lights.

[![Long-red-line-of-a-car's-tail-light](https://dev.epicgames.com/community/api/documentation/image/86fbddfc-dacd-4b9f-85b5-aa74ac99454b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86fbddfc-dacd-4b9f-85b5-aa74ac99454b?resizing_type=fit)

Emissive Materials can also interact with the [Lumen Global Illumination and Reflections](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine) system, meaning they interact with the environment around them.

The brightness of an emissive material can be controlled with float values ranging from **0** (no light) to **1** (emissive light), or above **1** (emissive light that creates [bloom](https://dev.epicgames.com/documentation/en-us/unreal-engine/bloom-in-unreal-engine)).

[![](https://dev.epicgames.com/community/api/documentation/image/2d3a640a-22b1-4db3-8a5f-d047a7f9b319?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d3a640a-22b1-4db3-8a5f-d047a7f9b319?resizing_type=fit)

Emissive materials and reflections are more noticeable in dark levels. To change the overall lighting in your level, follow these steps:

1. In the **Outliner**, select **Directional Light**.
2. In the **Viewport**, press **Ctrl + L**, and move your mouse to adjust the position of the directional light and relative time of day in your level.

   ![](https://dev.epicgames.com/community/api/documentation/image/b3ce9b1e-792c-4909-8177-49f19a0e7a20?resizing_type=fit)

Emissives are generally not recommended for environmental lighting. Using emissive materials as light sources can produce unintended results. Instead, we recommend using light sources for environments.

### Create an Emissive Material

For this tutorial, you’ll build neon signs that reflect off the wet stone when placed around the level. To do this, you’ll create a flexible parent Material that can propagate the following parameters to its child instances:

* Emissive Color
* Emissive Brightness
* Texture Mask

[![](https://dev.epicgames.com/community/api/documentation/image/43748cb8-f7ef-4e6b-b02a-7894879da8ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43748cb8-f7ef-4e6b-b02a-7894879da8ee?resizing_type=fit)

To create an emissive material, follow these steps:

1. In the **Content Browser**, at the path **All > Content > AdventureGame > Artist > Materials**, create a new **Material**.
2. Name the Material `M_EmissiveSign` and double-click to open it in the Material Editor.
3. In the **Material Graph**, drag off the **Emissive Color** input on the material root node, and add a **Multiply** node from the selection list.
4. Drag off the **Multiply** node’s **A** input and add a **Constant3Vector**.

   [![Constant-3-vector-node-to-m-emissive](https://dev.epicgames.com/community/api/documentation/image/eb269885-63c4-4dbf-8ba7-6aaa090e2365?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eb269885-63c4-4dbf-8ba7-6aaa090e2365?resizing_type=fit)
5. Right-click the **Constant3Vector** and select **Convert to Parameter**.
6. Rename the parameter `Color`.
7. Double-click the color swatch and choose a color for your emissive.
8. Drag off the **Multiply** node’s **B** input and add a **Constant** node from the selection list.

   [![Emissive-color-in-the-color-node](https://dev.epicgames.com/community/api/documentation/image/eaf9b9bc-8f58-40ad-a46f-392b8b63d82e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eaf9b9bc-8f58-40ad-a46f-392b8b63d82e?resizing_type=fit)
9. Convert the constant to a parameter, name it `Brightness`, and set its **Valu****e** to `25`.

Your Material Graph should now look like this:

[![Color-and-emissive-nodes-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/a9bd756e-a34b-4dbe-af1e-4b1543d77246?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9bd756e-a34b-4dbe-af1e-4b1543d77246?resizing_type=fit)

### Limit Parameters with Clamps

Although emissive brightness has no upper limit, you can set your own custom limits for the minimum and maximum brightness in the parent Material using a **clamp**. Clamping can make adjusting values with a slider easier, especially when dealing with small numbers and sensitive adjustments.

Like other parameters, clamps are propagated to Material instances.

To clamp the brightness constant, follow these steps:

1. In the Material Graph, select the **Brightness** parameter.
2. In the **Details** panel, set **Slider Max** to `50`.

   [![Setting-the-brightness-parameter-to-50](https://dev.epicgames.com/community/api/documentation/image/c2f60ddf-54fe-4682-b7b3-4c41e2326676?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2f60ddf-54fe-4682-b7b3-4c41e2326676?resizing_type=fit)

Next, you'll give your signage content by using texture masks.

### Create a Simple Mask

A [texture mask](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine) is a grayscale (alpha) or single-channel texture map, used to reveal or hide certain areas of a Material. You can picture an alpha mask like layers; the white area of the mask reveals information on a lower layer and the black area hides it.

[![Image-of-light-being-contained-by-a-black-planar-mask](https://dev.epicgames.com/community/api/documentation/image/d5005643-c913-49ef-8380-5871ef67ccbb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5005643-c913-49ef-8380-5871ef67ccbb?resizing_type=fit)

(1) Alpha mask (2) Emissive Material

In your emissive Material, you’ll use an alpha mask to reveal or block areas of emissive glow to create the content of the neon sign.

To create a mask inside the `M_Emissive` parent Material, follow these steps:

1. With no nodes selected, navigate to the **Details** panel. Next to **Blend Mode**, click the dropdown menu and select **Masked**.

   [![Set-blend-mode-to-masked](https://dev.epicgames.com/community/api/documentation/image/87c8174e-d918-461d-acd6-4cc99eda0fa6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87c8174e-d918-461d-acd6-4cc99eda0fa6?resizing_type=fit)
2. In the **EventGrap**h, right-click and create a **Texture Sample**.
3. In the **Details** panel, next to **Textur**e, search for `T_UE_Logo_M`.

   This texture comes with Unreal Engine, you do not have to download or create it.
4. Connect the **RGB** output on the Texture Sample to the **Opacity Mask** input on the material root node.
5. Right-click the **Texture Sample** and select **Convert to Parameter**. Name the parameter `LED Sign`.

Your Material Graph should now look like this:

[![Final-blueprint-with-color-and-led-sign-nodes](https://dev.epicgames.com/community/api/documentation/image/dc4fbc4d-a30f-4570-99ab-3a01f5cc39e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc4fbc4d-a30f-4570-99ab-3a01f5cc39e3?resizing_type=fit)

You’ve now created a Material that mimics a neon sign. Next, you'll further increase the flexibility of your parent Material, and the number of unique assets you can create, by inverting the mask:

|  |  |
| --- | --- |
| [Glowing-Unreal-logo](https://dev.epicgames.com/community/api/documentation/image/b646c06a-1304-47ad-8afb-7911b9370d0f?resizing_type=fit) | [Glowing-masked-unreal-logo](https://dev.epicgames.com/community/api/documentation/image/e89b1744-8fe8-4bb4-b22e-11c1ecc98716?resizing_type=fit) |
| Original mask. | Inverted mask. |

To achieve this, you could create unique Material Instances for inverted and non-inverted masks. Instead, you’ll use a **Static Switch** to **toggle** inversion from within any Material instance made from `M_EmissiveSign`.

## Toggle Parameters with Static Switches

In the [previous tutorial](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances#the-anatomy-of-a-material), you learned about the Material propagation hierarchy; child instances inherit properties from parent Materials.

[![](https://dev.epicgames.com/community/api/documentation/image/091d49eb-8ef8-4c01-a4aa-2e3340195b9b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/091d49eb-8ef8-4c01-a4aa-2e3340195b9b?resizing_type=fit)

An instance can customize an inherited parameter, but can’t ignore it altogether — unless you use a **Static Switch**. Static switches, set in the parent Material, give child instances the ability to toggle parameters on or off.

Because parameters that are toggled off are not compiled, static switches can improve performance at **runtime**. However, because each boolean creates a new shader permutation, this has the potential to drastically increase **compile time** (depending on the complexity of the material). The value of switches depends on how you use them and your project’s development needs.

**Runtime** refers to the period when a game is running. **Compile time** refers to the stage where a game is compiling, before runtime.

To create a static switch that controls mask inversion, follow these steps:

1. In the **Material Graph**, select the **LED Sign** node and duplicate it by pressing **Ctrl + D**.
2. Rename the new node `Screen`.
3. From the **RGB** output of **Screen**, drag out and search for **One Minus**.
4. Right-click in the graph and search for **Static Switch Parameter**. Name the switch `Flip Mask?`
5. Connect the **output** of **One Minus** to the **False** input of the switch.
6. Connect the **RGB** output of **LED Sign** to the **True** input of the switch.
7. Connect the **output** of the switch to the **Opacity Mask** input of the material root node.
8. **Save** your Material.

Your Material Graph should now look like this:

[![Finished-nodes-in-blueprints](https://dev.epicgames.com/community/api/documentation/image/1d601cc6-aa91-40fc-9e9b-fdfecf7c05a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d601cc6-aa91-40fc-9e9b-fdfecf7c05a5?resizing_type=fit)

Now you can create Material instances from `M_EmissiveSign` that uniquely control the **brightness**, **color**, **texture ma****p**, or **mask inversion**.

[![Viewport-with-logo-sign-and-details-panel](https://dev.epicgames.com/community/api/documentation/image/e0c632a7-cb10-46d9-a246-22de1ef96350?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0c632a7-cb10-46d9-a246-22de1ef96350?resizing_type=fit)

Apply instances of `M_EmissiveSign` to new or existing mesh in your level to create a scene of your choosing. As you roll the water ball around the level, your signs will reflect off the wet floor using Lumen's [Global Illumination and Reflections System](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine) — which is on by default. You'll learn more about Lumen and other reflection systems in the next tutorial.

## Next Up

In the next tutorial, you’ll learn more about reflections within Post-Process Volumes, illumination systems, and how to apply different in-camera effects to your level.

* [![Add Post Process Volumes](https://dev.epicgames.com/community/api/documentation/image/77b586de-baf5-45f8-bc6b-125bcd355f18?resizing_type=fit&width=640&height=640)

  Add Post Process Volumes

  Create post process volumes to control the look and performance of a level.](https://dev.epicgames.com/documentation/en-us/unreal-engine/add-post-process-volumes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create a Game-Ready Floor Asset](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#createagame-readyfloorasset)
* [Create a World-Aligned Material](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#create-a-world-aligned-material)
* [Create a Floor Blueprint](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#createafloorblueprint)
* [Replace the Placeholder Meshes](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#replacetheplaceholdermeshes)
* [Change Materials Using Player Interaction](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#changematerialsusingplayerinteraction)
* [Create a Water Ball](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#createawaterball)
* [Create a Dynamic Material Instance](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#createadynamicmaterialinstance)
* [Call Events](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#callevents)
* [Control Material Properties](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#controlmaterialproperties)
* [Power Your Logic with Timelines](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#poweryourlogicwithtimelines)
* [Emissive Materials](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#emissivematerials)
* [Create an Emissive Material](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#create-an-emissive-material)
* [Limit Parameters with Clamps](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#limit-parameters-with-clamps)
* [Create a Simple Mask](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#createasimplemask)
* [Toggle Parameters with Static Switches](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#toggleparameterswithstaticswitches)
* [Next Up](/documentation/en-us/unreal-engine/artist-04-expanded-material-instances?application_version=5.7#nextup)
