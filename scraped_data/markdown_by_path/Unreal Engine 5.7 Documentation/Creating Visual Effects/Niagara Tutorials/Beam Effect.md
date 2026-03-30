<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# Beam Effect

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Tutorials](/documentation/en-us/unreal-engine/tutorials-for-niagara-effects-in-unreal-engine "Niagara Tutorials")
7. Beam Effect

# Beam Effect

This page shows how to create a beam effect that simulates lightning.

![Beam Effect](https://dev.epicgames.com/community/api/documentation/image/84e16f0c-a623-4b34-b40f-6740ec7b67a8?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

 On this page

Prerequisite Step: This how-to uses the DefaultRibbonMaterial, which is included in the content for the Niagara plugin. However, you can use the M\_Balloon material used in the [Create a Mesh Balloon Effect](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine) how-to if you have already completed that tutorial.

In Niagara, the Ribbon Renderer is used along with specific modules that indicate that the ribbon is being used as a beam. In this guide, you will learn how to create a beam that simulates lightning.

## Create System and Emitter

In Niagara, systems and emitters are independent. The current recommended workflow is to create a system from existing emitters or emitter templates.

1. First, create a Niagara System by right-clicking in the Content Browser, and selecting **FX > Niagara System**.

   [![Create System Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdaaf943-7648-47fa-9c85-ac3445462085/01-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdaaf943-7648-47fa-9c85-ac3445462085/01-create-niagara-system.png)

   Click image for full size.
2. Select **New system from selected emitters**. Then click **Next**.

   [![New System from Selected Emitters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e040c9ca-f62f-40e3-9180-07306d8d0f46/02-new-system-from-selected-emitters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e040c9ca-f62f-40e3-9180-07306d8d0f46/02-new-system-from-selected-emitters.png)

   Click image for full size.
3. Under **Templates**, select **Static Beam**. Click the plus sign (**+**) to add this template. Then, click **Finish**.

   [![Select Static Beam Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eef3e427-e100-4562-b424-664344438089/03-select-static-beam-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eef3e427-e100-4562-b424-664344438089/03-select-static-beam-template.png)

   Click image for full size.
4. Name the new system **BeamSystem**. Double-click to open it in the Niagara Editor.

   ![Name System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b657211-c690-4e79-a2f8-d7b0f39c8a0d/04-rename-system.png "Name System")
5. Drag your \*\*BeamSystem into your Level.

   [![Drag System Into Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5698e43-d514-40a3-afda-4764e7ebf97f/05-drag-system-into-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5698e43-d514-40a3-afda-4764e7ebf97f/05-drag-system-into-level.png)

   Click image for full size.

   When you make a particle effect, it is always a good idea to drag your system into a Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your Level.
6. The emitter instance in your new system has the default name of **StaticBeam**, but you can rename it. Click the name of the emitter instance in the System Overview, and the field will become editable. Name the emitter **FX\_Beam**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76c8720b-a4ce-4765-8109-2e0a808f99c1/06-rename-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76c8720b-a4ce-4765-8109-2e0a808f99c1/06-rename-emitter.png)

   Click image for full size.

## Change Renderer Settings

The **Render** group is last in the stack, but you need to change some things so that the effect displays the way it is supposed to.

1. In the **System Overview**, click **Render** to open it in the **Selection** panel.

   [![Select the Render Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1dd994f0-e906-46e1-bdc6-baed744063d3/07-select-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1dd994f0-e906-46e1-bdc6-baed744063d3/07-select-render-group.png)

   Click image for full size.

   The emitter template in this system already has a ribbon renderer included. You will add specific modules later in this guide to indicate that the ribbon is used as a beam.
2. The Material used for this renderer is the **DefaultRibbonMaterial**. If you want to use a different material, you can click the dropdown to search for and select that Material.
3. If you scroll past the settings in the **Ribbon Rendering** section, you will find a section called **Tessellation**. In that section, set the **Curve Tension** to **.5**. This will affect how spikey the lightning effect is. You can raise or lower that value to vary your effect.

   [![Set Curve Tension](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1fb9db14-e5a4-4d1a-a189-d4ed0e0b0d6b/08-set-curve-tension.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1fb9db14-e5a4-4d1a-a189-d4ed0e0b0d6b/08-set-curve-tension.png)

   Click image for full size.

## Edit the Emitter Update Group Settings

First, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Select Emitter Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/735fd5c7-a35d-4834-8a13-9a9564019f70/09-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/735fd5c7-a35d-4834-8a13-9a9564019f70/09-select-emitter-update-group.png)

   Click image for full size.
2. The **Static Beam** emitter template has the **Life Cycle Mode** set to **Self** by default. This means the life cycle and loop behavior of the emitter is set directly, instead of being handled by the System. For this effect, you will add some randomness to the **Loop Duration** by adding a float to the value. Click the dropdown arrow for **Loop Duration**, and select **Dynamic Inputs > Random Ranged Float**. This adds **Minimum** and **Maximum** fields under Loop Duration.

   [![Set Loop Duration to Random Range Float](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e636678-cdfc-48e4-9c41-1067b85b51e9/10-set-loop-duration-to-random-range-float.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e636678-cdfc-48e4-9c41-1067b85b51e9/10-set-loop-duration-to-random-range-float.png)

   Click image for full size.
3. Set the Loop Duration Minimum and Maximum values to the following.

   [![Set Loop Duration Minimum and Maximum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf62fcae-84a9-4d16-801f-20abd18e2b8f/11-loop-duration-min-and-max.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf62fcae-84a9-4d16-801f-20abd18e2b8f/11-loop-duration-min-and-max.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Minimum** | .1 |
   | **Maximum** | .2 |
4. The first module that indicates this effect uses a beam is the **Beam Emitter Setup** module. Since you started with the Static Beam template, this module is already included. For **Beam Start** and **Beam End**, leave the position at its default. Check the boxes to enable **Absolute Start** and **Absolute End**.

   The start position of the beam is defined by the position of the Niagara system in the scene. The end position is defined by the static coordinates set in Beam End, which you can change by editing the values directly. At the end of the tutorial you will learn how to connect the end point of the beam to an actor.

   [![Enable Absolute Start and Absolute End](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46f59fd7-2644-4e9a-af9e-45ebc5b03f48/12-set-absolute-beam-start-and-end.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46f59fd7-2644-4e9a-af9e-45ebc5b03f48/12-set-absolute-beam-start-and-end.png)

   Click image for full size.
5. To add an arc or curve to the effect, check the box to enable **Use Beam Tangents**. This displays the **Beam Start Tangent** and **Beam End Tangent** settings. Click the **Reset to Default** (small yellow arrow) icon for **Beam Start Tangent** to change the value to **Multiply Vector by Float**.

   [![Reset Beam Start Vector](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16339f84-63c3-41b3-bc14-4daa3aa9b883/13-reset-beam-start-vector.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16339f84-63c3-41b3-bc14-4daa3aa9b883/13-reset-beam-start-vector.png)

   Click image for full size.
6. Set the Beam Start Tangent **Vector** and **Float** to the following values.

   [![Set Beam Start Tangent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f95dd93-8e5b-4a69-ac47-b8b0e90e5a82/14-set-beam-start-vector-and-float.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f95dd93-8e5b-4a69-ac47-b8b0e90e5a82/14-set-beam-start-vector-and-float.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Vector** | **X**: 0, **Y**: 0, **Z**: 1 |
   | **Float** | .5 |
   |  |  |
7. Set the Beam End Tangent Vector and Float to the following values.

   [![Set Beam End Tangent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13ba38de-9806-4ee9-9934-2fd73b75f97f/15-set-beam-end-vector-and-float.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13ba38de-9806-4ee9-9934-2fd73b75f97f/15-set-beam-end-vector-and-float.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Vector** | **X**: 0, **Y**: 0, **Z**: 1 |
   | **Float** | 1 |
   |  |  |
8. In the **Spawn Burst Instantaneous** module, set the **Spawn Count** to **35**.

   [![Set Spawn Count](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94ba7494-05c8-445b-b6b1-874c4489d144/16-set-spawn-count.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94ba7494-05c8-445b-b6b1-874c4489d144/16-set-spawn-count.png)

   Click image for full size.

## Edit the Particle Spawn Group Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Select Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39635d3f-b2f9-452e-9a10-7ac0ea9b30f6/17-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39635d3f-b2f9-452e-9a10-7ac0ea9b30f6/17-select-particle-spawn-group.png)

   Click image for full size.
2. In the **Initialize Particle** module, locate the **Lifetime** parameter. This parameter determines how long particles will display before they disappear. Set the **Lifetime** to **.2**. This short Lifetime will cause the beam to flicker, which will make the lightning more realistic.

   [![Set Lifetime Value](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5628029f-8fb2-4984-995b-9d7ad89bb413/18-set-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5628029f-8fb2-4984-995b-9d7ad89bb413/18-set-lifetime.png)

   Click image for full size.
3. The **Spawn Beam** module is the second beam-specific module. You do not need to set anything with this module, it just needs to be present.
4. The third beam-specific module is the **Beam Width** module. The Beam Width is set to **Float from Curve**. Select the **Ramp Up Down** template to apply this shape to the curve.

   [![Set Beam Width](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10350134-62d2-404a-abf4-8ccff4bc9696/19-set-beam-width-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10350134-62d2-404a-abf4-8ccff4bc9696/19-set-beam-width-template.png)

   Click image for full size.
5. Below the Curve diagram you will see some additional settings. Set the **Scale Curve** to **5**.

## Edit the Particle Update Group Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Select Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b41aa08-0d54-4db4-be64-db0797de2acb/20-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b41aa08-0d54-4db4-be64-db0797de2acb/20-select-particle-update-group.png)

   Click image for full size.
2. In the **Color** module, set the **RGB** values to the following.

   [![Set Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b72a693-f2ff-45b5-a70d-c96029adf705/21-set-particle-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b72a693-f2ff-45b5-a70d-c96029adf705/21-set-particle-color.png)

   Click image for full size.
3. To break up the curve and make the beam crackle and jump like lightning, add the **Jitter Position** module by clicking the **Plus sign** (**+**) icon for **Particle Update** and selecting **Location > Jitter Position**.

   [![Add Jitter Position Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/738ec17b-749b-4a5a-9249-b3af2c02118a/22-add-jitter-position-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/738ec17b-749b-4a5a-9249-b3af2c02118a/22-add-jitter-position-module.png)

   Click image for full size.
4. To make the **Jitter Position** module work correctly, you need an Update Beam module. Add the **Update Beam** module by clicking the **Plus sign** (**+**) icon for **Particle Update** and selecting **Beam > Update Beam**. In the **System Overview**, drag the **Update Beam** module to a position above the **Jitter Position** module in the stack.

   [![Add Update Beam Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6395063e-d109-4768-976f-5211ce3a0c6e/23-add-update-beam-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6395063e-d109-4768-976f-5211ce3a0c6e/23-add-update-beam-module.png)

   Click image for full size.
5. Now go back to the **Jitter Position** module. The default setting for **Jitter Amount** is **10**, and the default for **Jitter Delay** is **.25**. However, if you decrease the **Jitter Delay** to **.1** you will start to see the beam bend with an angular, jagged motion. With the value at **.1** you can still see the original arc shape under the jagged beam, which is not ideal. To fix this, you have to set the Jitter Delay to a negative number. Set the **Jitter Delay** to **-.01**. Set the **Jitter Amount** to **15**.

   [![Set Jitter Amount and Delay](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f1e134b-9bec-46c0-ada5-be6a245d1892/24-set-jitter-amount-and-delay.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f1e134b-9bec-46c0-ada5-be6a245d1892/24-set-jitter-amount-and-delay.png)

   Click image for full size.

## Adjusting the Beam's End Position

You can set the Start and End positions of the beam in the **Beam Emitter Setup** module, which is in the **Emitter Update** group. By default, the end position of the beam is set to a static world location value, which you can edit manually by adjusting the value.

However, it could be useful to be able to link that end position to an actor in your scene. This way, when you want to edit the end position of the beam, you simply move that actor. One way of doing this would be to use Blueprints. Another, more simple way, would be to use a Scratch Pad to set a dynamic input.

1. Click the **Beam Emitter Setup** module to select it in the **Selection** panel.

   [![Select Beam Emitter Setup Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52d4b818-7a32-4a9c-802c-767d1ecf8e85/25-select-beam-emitter-setup-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52d4b818-7a32-4a9c-802c-767d1ecf8e85/25-select-beam-emitter-setup-module.png)

   Click image for full size.
2. Click the dropdown arrow next to **Beam End**, then search for **scratch** and select **New Dynamic Scratch Input**.

   [![Set Beam End to Dynamic Scratch Input](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f247fd5c-51bd-4641-a761-b345e379f54e/26-set-beam-end-to-scratch-dynamic.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f247fd5c-51bd-4641-a761-b345e379f54e/26-set-beam-end-to-scratch-dynamic.png)

   Click image for full size.
3. This will open a scratch pad with a basic setup. It consists of an input, a Map Get that you can use to pull in some values, and an output. Right-click on the default input and select **Remove Pin** as this default input will not be needed.
4. Click on the plus sign (**+**) to add a new pin. Search for **actor** and select **Make New > Actor Component Interface**. This will add a section to the **Details Panel** in the **Level Editor** when you select your Niagara object, so that you can select the object you would like to link it to.

   [![Add Pin for New Actor Component Interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af1875ee-d43a-4348-8a36-e9ea3a34b3b1/27-add-actor-component-interface.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af1875ee-d43a-4348-8a36-e9ea3a34b3b1/27-add-actor-component-interface.png)

   Click image for full size.
5. Drag the pin from **New Actor Component Interface** and release. Select **Get Transform**. This will provide the transformation information of the object it's linked to.

   [![Add Get Transform](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf69c382-83ec-46a4-a7c3-4fb805e7b86a/28-add-get-transform.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf69c382-83ec-46a4-a7c3-4fb805e7b86a/28-add-get-transform.png)

   Click image for full size.
6. Connect the Position value to the Output.

   [![Connect Position to Output](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5913794e-8c9a-496f-bcce-2c3766433b02/29-connect-position-to-output.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5913794e-8c9a-496f-bcce-2c3766433b02/29-connect-position-to-output.png)

   Click image for full size.
7. The system automatically adds a **Position -> Vector3f**  node. This helps to transform vecctors to the proper format for large world coordinates. You can organize your canvas to make sure they don't overlap.

   [![Position to Vector 3f node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bacba7d0-5a24-4704-b5dd-489a278feaca/30-vector-3f.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bacba7d0-5a24-4704-b5dd-489a278feaca/30-vector-3f.png)

   Click image for full size.
8. Now that the scratch is complete, in order for the changes to propogate back out into the Niagara system, you must hit **Apply**.

   [![Apply the Scratch Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05929729-9601-4243-9954-1f7609feb1c2/31-apply-the-scratch.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05929729-9601-4243-9954-1f7609feb1c2/31-apply-the-scratch.png)

   Click image for full size.
9. In the Niagara Editor, select again the **Beam Emitter Setup** module. You will notice now there is a **New Actor Component Interface** linked to the **Beam End**. Click on the dropdown arrow, then select **Make** > **Read from new User parameter**. This will create a new user parameter that you will be able to set from outside the Niagara system.

   [![Set Actor Component Interface to Make New User Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa19bae1-f6dc-4001-849f-0603e444d8af/32-set-component-interface-to-user-parameter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa19bae1-f6dc-4001-849f-0603e444d8af/32-set-component-interface-to-user-parameter.png)

   Click image for full size.
10. By default, the system creates a User Parameter with the name of the object and the name of the parameter, so it's quite long. If you'd like to rename this, go to the Parameters panel.

    [![Parameters Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9a7aca6-5bcb-45eb-a15a-2f3a2d345ab0/33-new-actor-component-user-parameter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9a7aca6-5bcb-45eb-a15a-2f3a2d345ab0/33-new-actor-component-user-parameter.png)

    Click image for full size.
11. Double-click to rename **New Actor Component Interface\_Beam End** to something shorter, such as **Beam\_End**.

    [![Rename User Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cd6acfd-5831-46ae-9ecd-59646fa43b18/34-rename-user-parameter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cd6acfd-5831-46ae-9ecd-59646fa43b18/34-rename-user-parameter.png)

    Click image for full size.
12. Save your Niagara System and close the editor to return to the **Level Editor**. You should see the beam system that you had dragged in the level earlier. You can already manipulate the start position of the beam by moving the Niagara system's start point. However the end point is fixed. What we will do next is to attach it to an object in the scene.
13. First, create a basic sphere to link the end point to. From the **Create** menu, select **Shapes > Sphere**.

    [![Create Sphere](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d013af9-447b-4da4-8eaf-4f4171905361/35-create-new-sphere.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d013af9-447b-4da4-8eaf-4f4171905361/35-create-new-sphere.png)

    Click image for full size.
14. In the **Outliner**, select your sphere and double-click to rename it to **Sphere\_BeamEnd**.

    [![Rename Sphere](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c0001aa-9d10-464b-a79e-44c01ad8a279/36-rename-sphere.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c0001aa-9d10-464b-a79e-44c01ad8a279/36-rename-sphere.png)

    Click image for full size.
15. In the **Outliner**, select your Niagara system **BeamSystem**. In the **Details** panel, scroll down to the **Override Parameters** section. Here, you should see the **Beam\_End** user parameter that you set up when you created the scratch module. Select the dropdown menu for **Source Actor**, then select **Sphere\_BeamEnd**. Alternatively, you can use the eye dropper to select any object in your level. Now, when you move that object, the beam end position moves with it.

    [![Link Sphere to Beam End](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/429e8084-2d5b-40fd-b404-349a477f2b8a/37-set-sphere-in-override-parameters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/429e8084-2d5b-40fd-b404-349a477f2b8a/37-set-sphere-in-override-parameters.png)

    Click image for full size.

## End Result

Congratulations! You have created a beam effect that simulates lightning. In the video below, you can see an example of the lightning beam effect. You can use beams for all kinds of visual effects: lasers, weapon rays, tesla coils and so on.

![Beam Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d12014b-dc44-43ae-83b3-55fc366761f3/beam-effect-final.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create System and Emitter](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#createsystemandemitter)
* [Change Renderer Settings](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#changerenderersettings)
* [Edit the Emitter Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheemitterupdategroupsettings)
* [Edit the Particle Spawn Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticlespawngroupsettings)
* [Edit the Particle Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticleupdategroupsettings)
* [Adjusting the Beam's End Position](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#adjustingthebeam'sendposition)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
