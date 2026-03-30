<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# Ribbon Effect

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
7. Ribbon Effect

# Ribbon Effect

This document describes how you can create a ribbon visual effect using Niagara.

![Ribbon Effect](https://dev.epicgames.com/community/api/documentation/image/1375d6f4-7fc4-45b5-bfed-ee654104b344?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

 On this page

Prerequisite Step: This tutorial uses the DefaultRibbonMaterial, which is included in the content for the Niagara plugin. However, you can also use the M\_Balloon material you created in the [Create a Mesh Particle Effect](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine) tutorial if you have already completed it.

Simulating natural phenomena is challenging, especially when using sprite or mesh-based particles to simulate smoke or vapor trails. **Ribbon Emitters** are an excellent solution for simulating these objects. In the following tutorial, you will learn how to set up a Niagara Emitter to create a continuous ribbon-style particle effect into the world. Your end result will look like the following.

![Ribbon Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76864bb6-a382-4708-a490-48d10548ac89/ribbon-final.gif)

## Create System and Emitter

Unlike in Cascade, Niagara emitters and systems are independent. The current recommended workflow is to create a system from existing emitters or emitter templates.

1. First, create a Niagara System by right-clicking in the Content Drawer, and selecting **FX > Niagara System**.

   [![Create Niagara System Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7edc91b-8e94-44e5-9b48-f1136487cf02/01-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7edc91b-8e94-44e5-9b48-f1136487cf02/01-create-niagara-system.png)

   Click image for full size.
2. Select **New system from selected emitters**. Then click **Next**.

   [![New System from Selected Emitters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d38ecfa9-6f30-4408-bd78-e55cfc2e88b6/02-new-system-from-selected-emitters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d38ecfa9-6f30-4408-bd78-e55cfc2e88b6/02-new-system-from-selected-emitters.png)

   Click image for full size.
3. Under **Templates**, select **Simple Sprite Burst**.

   Using a template will place an emitter instance in your new system, and that emitter instance will have no inheritance.

   [![Select Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58b08389-81ed-47d6-8288-b7e3bc1cd72e/03-simple-sprite-burst-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58b08389-81ed-47d6-8288-b7e3bc1cd72e/03-simple-sprite-burst-template.png)

   Click image for full size.
4. Click the **Plus sign** icon (**+**) to add the selected emitter to the list of emitters to add to the system. Then click **Finish**.

   [![Add Selected Emitter and Finish](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa0573ce-c993-479d-8875-1a876fc8d6be/04-create-ribbon-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa0573ce-c993-479d-8875-1a876fc8d6be/04-create-ribbon-system.png)

   Click image for full size.
5. Name the new system **RibbonSystem**.

   ![Name New System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/75e77c7e-601e-4b95-9229-a1129d6b4028/05-rename-ribbon-system.png "Name New System")
6. Drag the **RibbonSystem** into your Level. Double-click to open the system in the Niagara Editor.

   When you make a particle effect, it is always a good idea to drag your system into a Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your Level.
7. The emitter instance in your new system has the default name of **SimpleSpriteBurst**, but you can rename it. Click the name of the emitter instance in the **System Overview**, and the field will become editable. Name the emitter **FX\_Ribbon**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19f18458-b62b-4938-a4a5-067a5d6cc1da/06-rename-ribbon-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19f18458-b62b-4938-a4a5-067a5d6cc1da/06-rename-ribbon-emitter.png)

   Click image for full size.

## Change Renderer

The **Render** group is last in the stack, but you need to change some things so that the effect displays the way it is supposed to. The original template used a Sprite Renderer, but this effect needs a Ribbon Renderer.

1. In the **System Overview**, click **Render** to open it in the **Selection** panel.

   [![Open Render Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b41dd66-487a-458a-9b59-ef37c1c96982/07-select-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b41dd66-487a-458a-9b59-ef37c1c96982/07-select-render-group.png)

   Click image for full size.
2. To make a ribbon effect, you need a **Ribbon Renderer** module. But the template has a **Sprite Renderer** module. Click the **Trashcan** icon to delete the Sprite Renderer.

   [![Remove Sprite Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b1542f6-6f04-4ff7-8a26-3c51cc43703c/08-delete-sprite-renderer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b1542f6-6f04-4ff7-8a26-3c51cc43703c/08-delete-sprite-renderer.png)

   Click image for full size.
3. Click the **Plus sign** icon (**+**) for **Render** and select **Ribbon Renderer**.

   [![Add Ribbon Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c8da25f-78de-4d6b-8497-f5612c8c95a6/09-add-ribbon-renderer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c8da25f-78de-4d6b-8497-f5612c8c95a6/09-add-ribbon-renderer.png)

   Click image for full size.
4. The material you want is not displayed by default. Click the dropdown for **Material**, and click **View Options** to open a list of options. Check the boxes for **Show Engine Content** and **Show Plugin Content**. Now you will be able to see the material.

   [![Set View Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5fa07e94-d85d-406f-8428-d840a9994112/10-show-engine-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5fa07e94-d85d-406f-8428-d840a9994112/10-show-engine-content.png)

   Click image for full size.
5. Click the dropdown for **Material** and select **DefaultRibbonMaterial**.

   If you completed the [Create a Mesh Particle Effect](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine) tutorial, you can select the **M\_Balloon** material instead. This will give you an opaque ribbon, rather than the translucent one created by the DefaultRibbonMaterial.

   [![Select Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdc6bd1c-bd7d-45bd-a74a-affc0e5d3053/11-select-ribbon-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdc6bd1c-bd7d-45bd-a74a-affc0e5d3053/11-select-ribbon-material.png)

   Click image for full size.

## Edit the Emitter Update Group Settings

First, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

Even after adding a Ribbon Renderer and editing the settings in the Emitter Update group, you will not see a ribbon appear. This is normal! When you get to the Particle Spawn section of this document, you will start to see the actual ribbon.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Open Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05bba791-fd37-4b6f-aa17-3f45980e246c/12-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05bba791-fd37-4b6f-aa17-3f45980e246c/12-select-emitter-update-group.png)

   Click image for full size.
2. Expand the **Emitter State** module. This module controls time and scalability for this emitter. Because you used the **Simple Sprite Burst** template, the **Life Cycle Mode** is set to **Self**. Normally this is used for complete customization of emitter life cycle logic for this specific emitter, but it is not needed for this effect. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3c0615a-78a4-4bc0-bd6f-500ae4d815c0/13-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3c0615a-78a4-4bc0-bd6f-500ae4d815c0/13-life-cycle-mode.png)

   Click image for full size.
3. The **Spawn Rate** module creates a continuous stream of particles while the emitter is active. Add the **Spawn Rate** module by clicking the **Plus sign** icon (**+**) for **Emitter Update** and selecting **Spawning > Spawn Rate**.

   [![Add the Spawn Rate Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ddc6c47-9799-4f21-96ce-f8a9d74d2ecc/14-add-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ddc6c47-9799-4f21-96ce-f8a9d74d2ecc/14-add-spawn-rate.png)

   Click image for full size.
4. Set the **Spawn Rate** to **100**.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8638ee9-c193-4a58-b94e-3ea802fa193d/15-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8638ee9-c193-4a58-b94e-3ea802fa193d/15-set-spawn-rate.png)

   Click image for full size.

## Edit the Particle Spawn Group Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Open Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc6ecfef-39d2-47ef-b493-b262d98b320b/16-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc6ecfef-39d2-47ef-b493-b262d98b320b/16-select-particle-spawn-group.png)

   Click image for full size.
2. Under **Point Attributes**, locate the **Lifetime** parameter. This parameter determines how long particles will display before they disappear. Set the **Lifetime** to **5**.

   [![Set Ribbon Lifetime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/70f27c71-3a36-48be-95a1-b8d77887a05c/17-set-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/70f27c71-3a36-48be-95a1-b8d77887a05c/17-set-lifetime.png)

   Click image for full size.
3. For the **Color** parameter, set it to a color of your choosing. You can do this either by typing in RGB values, or by clicking on the swatch to open a color picker.

   [![Set Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28652ab0-63b2-4bf0-b4b7-205e3624e341/18-set-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28652ab0-63b2-4bf0-b4b7-205e3624e341/18-set-color.png)

   Click image for full size.
4. Set the **Mass** parameter to **10**. This will affect how the ribbon spreads outward, as well as how quickly it falls.

   [![Set Mass](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdf44b19-d1c7-493f-809a-f35223b4b7ea/19-set-mass.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdf44b19-d1c7-493f-809a-f35223b4b7ea/19-set-mass.png)

   Click image for full size.
5. Under **Ribbon Attributes**, set the **Ribbon Width** to **10**.

   [![Set Ribbon Width](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c8a1bddf-d407-49e8-9905-5536c3103472/20-set-ribbon-width.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c8a1bddf-d407-49e8-9905-5536c3103472/20-set-ribbon-width.png)

   Click image for full size.
6. To make the ribbon spin in a spiral, you can add a **Shape Location** module. Location modules affect the shape of the location where the particles spawn. Click the **Plus sign** icon (**+**) for **Particle Spawn** and select **Location > Shape Location**.

   [![Add Shape Location Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3223a3ac-afb6-4e06-9d56-7b80547bce59/21-add-shape-location-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3223a3ac-afb6-4e06-9d56-7b80547bce59/21-add-shape-location-module.png)

   Click image for full size.
7. Under **Shape**, click the dropdown for **Shape Primitive** and select **Ring / Disk**.

   [![Select Shape Primitive](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17baac93-4208-4ca9-983f-000b29b0c095/22-select-ring-shape.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17baac93-4208-4ca9-983f-000b29b0c095/22-select-ring-shape.png)

   Click image for full size.
8. Set the **Ring Radius** to **50**. The Ring Radius determines how large the primary ring shape is.

   [![Set Ring Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d78cba2-07d6-425f-9267-1a108962d40c/23-set-ring-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d78cba2-07d6-425f-9267-1a108962d40c/23-set-ring-radius.png)

   Click image for full size.
9. Under **Distribution**, click the dropdown for **Ring Distribution Mode** and select **Direct**.

   [![Set Distribution Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be5ee849-b578-4806-a6db-7932f9dc0d33/24-set-ring-distribution-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be5ee849-b578-4806-a6db-7932f9dc0d33/24-set-ring-distribution-mode.png)

   Click image for full size.
10. Now you will add some velocity to the ribbon. Click the **Plus sign** icon (**+**) for **Particle Spawn** and select **Velocity > Add Velocity**.

    [![Add the Add Velocity Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8485b5a-7bc4-438d-9977-c95e5a4d4fa4/25-add-velocity-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8485b5a-7bc4-438d-9977-c95e5a4d4fa4/25-add-velocity-module.png)

    Click image for full size.
11. Click the dropdown to **Velocity Mode** and select **From Point**.

    [![Select Velocity From Point Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbf1032b-0ca1-42d5-99a1-966ca998c240/26-velocity-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbf1032b-0ca1-42d5-99a1-966ca998c240/26-velocity-mode.png)

    Click image for full size.
12. Set the **Velocity Speed** to **50**. Now you will see the ribbon start to spiral! This happens because as the position is moving around the Large Radius, the velocity pushes the ribbon outward from the original ring.

    [![Set Velocity Speed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6c08111-6b79-4923-ad2f-5084a345df72/27-set-velocity-speed.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6c08111-6b79-4923-ad2f-5084a345df72/27-set-velocity-speed.png)

    Click image for full size.

## Edit the Particle Update Group Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Open Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/016ca1e0-9cbe-4d79-b480-d2329ff5352f/28-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/016ca1e0-9cbe-4d79-b480-d2329ff5352f/28-select-particle-update-group.png)

   Click image for full size.
2. This effect has a single color, so the **Scale Color** module is not needed. Click the **Trashcan** icon to delete it.

   [![Remove Scale Color Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ba7c987-b671-4235-a13e-154a94a83aee/29-delete-scale-color-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ba7c987-b671-4235-a13e-154a94a83aee/29-delete-scale-color-module.png)

   Click image for full size.
3. Add the **Acceleration Force** module. This is what makes the spiraling ribbon fall down, simulating gravity. Click the **Plus sign** icon (**+**) for **Particle Update** and select **Forces > Acceleration Force**.

   [![Add the Acceleration Force Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c09aa1eb-42ef-4d0e-a156-285fa99ca4d7/30-add-acceleration-force.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c09aa1eb-42ef-4d0e-a156-285fa99ca4d7/30-add-acceleration-force.png)

   Click image for full size.
4. Set the **Z** value of the **Acceleration** to **-200**. A positive Z value would make the ribbon spiral upwards; using a negative value makes it drop downward in a parabolic shape.

   [![Set Acceleration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7b80322-f0d6-46cc-942d-74f7f936bab5/31-set-acceleration.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7b80322-f0d6-46cc-942d-74f7f936bab5/31-set-acceleration.png)

   Click image for full size.

## End Result

Congratulations! You have created a Niagara ribbon effect.

![Ribbon Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29663a4b-ee7a-499d-a3bb-0344525dc38e/ribbon-final.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create System and Emitter](/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7#createsystemandemitter)
* [Change Renderer](/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7#changerenderer)
* [Edit the Emitter Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheemitterupdategroupsettings)
* [Edit the Particle Spawn Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticlespawngroupsettings)
* [Edit the Particle Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticleupdategroupsettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-ribbon-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
