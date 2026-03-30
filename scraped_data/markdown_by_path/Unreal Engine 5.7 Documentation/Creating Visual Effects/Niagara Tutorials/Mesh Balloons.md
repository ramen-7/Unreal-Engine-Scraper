<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# Mesh Balloons

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
7. Mesh Balloons

# Mesh Balloons

This document describes how you can use a static mesh to create a balloon effect using Niagara.

![Mesh Balloons](https://dev.epicgames.com/community/api/documentation/image/86131df2-87bb-4bbc-9d72-72bd25cf9245?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

 On this page

Spawning a Static Mesh instead of a [camera-facing sprite](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine) can increase the realism of the effects you are creating. In the following tutorial, we will show how to set up a Niagara Emitter to spawn Static Meshes instead of sprites.

**Prerequisite Step:** This tutorial uses an imported balloon mesh. You can find free meshes online by doing a simple search. Otherwise, you can practice by using the **Shape\_Sphere** static mesh, which is found with the **Starter Content**. If you have not done so already, make sure that you have added your own mesh for the balloon to this project, or add the Starter Content to your project.

## Create a Material

The effect in this guide is meant to look like a cloud of balloons being released. To enhance this effect, you will make a simple material that makes the mesh look like a rubber balloon.

1. Right-click in the Content Browser and under Create Basic Asset select **Material**.

   [![Create New Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db47fc0c-3f27-43dd-8fb3-864ee9c972aa/01-create-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db47fc0c-3f27-43dd-8fb3-864ee9c972aa/01-create-material.png)

   Click image for full size.
2. Name the new Material **Balloon\_Material**. Double-click it to open in the Material Editor.

   [![Name Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed307e83-8079-4a4d-a490-d61f3dfc2e20/02-rename-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed307e83-8079-4a4d-a490-d61f3dfc2e20/02-rename-material.png)

   Click image for full size.
3. In the **Palette** panel, type `Particle` in the search bar. Select **Particle Color** and drag it into the Graph to add a Particle Color node.

   [![Add Particle Color Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4ab2dcd-e21a-40a5-a003-10331c9a165c/03-add-particle-color-to-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4ab2dcd-e21a-40a5-a003-10331c9a165c/03-add-particle-color-to-material.png)

   Click image for full size.
4. Drag off the **RGB output** and connect the wire to the **Base Color** input on the **Material** node.

   [![Connect Particle Color to Base Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4e277ce-ab3c-4754-b918-31330d6a3a13/04-connect-particle-color-to-base-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4e277ce-ab3c-4754-b918-31330d6a3a13/04-connect-particle-color-to-base-color.png)

   Click image for full size.
5. While holding down the **1** key, click in the Graph. This creates a **Constant** node. Copy and paste it twice, for a total of **three Constant nodes**.

   [![Add Constant Nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a71091b0-415f-4bb6-ac76-ad8c3fc58503/05-add-three-constants.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a71091b0-415f-4bb6-ac76-ad8c3fc58503/05-add-three-constants.png)

   Click image for full size.
6. Connect the output on one **Constant** node to the **Metallic** input on the **Material** node.

   [![Connect Constant to Metallic](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3579691-34b9-41b2-823c-a84fdd4af150/06-connect-constant-to-metallic.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3579691-34b9-41b2-823c-a84fdd4af150/06-connect-constant-to-metallic.png)

   Click image for full size.
7. You can set the **Value** of a selected constant in the **Details** panel, under **Material Expression Constant**. This material is not metallic, so leave the **Metallic** constant's value at **0**.

   [![Set Metallic Constant](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd037e9c-e08d-4961-ba97-aaa543c48e19/07-set-metallic-to-zero.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd037e9c-e08d-4961-ba97-aaa543c48e19/07-set-metallic-to-zero.png)

   Click image for full size.
8. Connect the output on the second **Constant** node to the **Specular** input on the **Material** node.

   [![Connect Specular Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a28e689-94b6-408a-8243-9271f9b37620/08-connect-constant-to-specular.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a28e689-94b6-408a-8243-9271f9b37620/08-connect-constant-to-specular.png)

   Click image for full size.
9. With the **Specular** constant node selected, set the Specular **Value** in the **Details** panel to **0.7**. This will give the material a slightly reflective surface.

   [![Set Specular Value](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2165a529-c548-48ea-8a85-4bcf99f082bd/09-set-specular-value.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2165a529-c548-48ea-8a85-4bcf99f082bd/09-set-specular-value.png)

   Click image for full size.
10. Connect the output on the third Constant node to the **Roughness** input on the **Material** node.

    [![Connect Roughness Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/120e740b-9774-416d-a622-593beaa2a369/10-connect-constant-to-roughness.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/120e740b-9774-416d-a622-593beaa2a369/10-connect-constant-to-roughness.png)

    Click image for full size.
11. With the **Roughness** constant node selected, set the Roughness **Value** in the **Details** panel to **0.2**. This will create a mostly smooth surface.

    [![Set Roughness Value](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/206075ec-50f3-49b0-b716-ded06d6ba3a7/11-set-roughness-value.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/206075ec-50f3-49b0-b716-ded06d6ba3a7/11-set-roughness-value.png)

    Click image for full size.

Your final result for the Material should look like the image below.

![Material Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e050e40-df69-4bfe-b0c8-b4cbc06fa6b5/12-final-material-result.png)

## Create the System and Emitter

Niagara emitters and systems are independent. The current recommended workflow is to create a system from existing emitters or emitter templates.

1. First, create a Niagara System by right-clicking in the Content Drawer and selecting **FX > Niagara System**. The Niagara Emitter wizard displays.

   [![Create Niagara System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d6bd748-450c-469f-8934-9b7a0aa01d3d/13-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d6bd748-450c-469f-8934-9b7a0aa01d3d/13-create-niagara-system.png)

   Click image for full size.
2. Select **New system from selected emitters**. Then click **Next**.

   [![Create Niagara System from Selected Emitters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb158632-153d-450a-a40d-38db5bb3e248/14-new-system-from-selected-emitters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb158632-153d-450a-a40d-38db5bb3e248/14-new-system-from-selected-emitters.png)

   Click image for full size.
3. Under **Templates**, select **Fountain**.

   [![Select Fountain Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b242477-dfa9-4ecb-a6a8-77a9d10db605/15-select-fountain-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b242477-dfa9-4ecb-a6a8-77a9d10db605/15-select-fountain-template.png)

   Click image for full size.
4. Click the **Plus sign** (**+**) icon to add the emitter to the list of emitters to add to the system. Then click **Finish**.

   [![Add Emitter and Finish](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d5e714a-44d4-4462-92fb-66d427ebec76/16-add-fountain-and-finish.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d5e714a-44d4-4462-92fb-66d427ebec76/16-add-fountain-and-finish.png)

   Click image for full size.
5. Name the new system **Balloon\_System**. Double-click to open it in the Niagara Editor.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46c3bddd-de07-4c4e-8446-190fa8f0707c/17-rename-balloon-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46c3bddd-de07-4c4e-8446-190fa8f0707c/17-rename-balloon-system.png)

   Click image for full size.
6. The emitter instance in your new system has the default name of **Fountain**, but you can rename it. Click the name of the emitter instance in the **System Overview**, and the field will become editable. Name the emitter **Balloons**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c9b5ab5-7988-49cd-b479-8915dd854856/18-rename-balloon-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c9b5ab5-7988-49cd-b479-8915dd854856/18-rename-balloon-emitter.png)

   Click image for full size.
7. Drag your **MeshSystem** into your Level.

   [![Drag System Into Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba14ec6a-20dd-4c5e-aee2-524112e313ef/19-drag-balloon-system-into-scene.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba14ec6a-20dd-4c5e-aee2-524112e313ef/19-drag-balloon-system-into-scene.png)

   Click image for full size.

   When you make a particle effect, it is always a good idea to drag your system into a Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your level.

## Change the Renderer

The Render group is last in the stack, but you need to change some things so that the effect displays the way it is supposed to. In this case, the template contains a Sprite Renderer, and this effect needs a Mesh Renderer.

1. In the **System Overview**, click **Render** to open it in the **Selection** panel.

   [![Select Render Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17014771-1c80-4f4a-9618-2df422287bfc/20-select-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17014771-1c80-4f4a-9618-2df422287bfc/20-select-render-group.png)

   Click image for full size.
2. To make a mesh particle effect you need a **Mesh Renderer** module, but the template has a **Sprite Renderer** module. Click the **Trashcan** icon to delete the Sprite Renderer.

   [![Remove Sprite Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ca112c6-d231-439d-8f17-9e4588300d75/21-delete-sprite-renderer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ca112c6-d231-439d-8f17-9e4588300d75/21-delete-sprite-renderer.png)

   Click image for full size.
3. Click the **Plus sign** (**+**) icon for Render and select **Mesh Renderer**.

   [![Add Mesh Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8dd5c61a-2f6f-4ebf-ac0a-88f194104e58/22-add-mesh-renderer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8dd5c61a-2f6f-4ebf-ac0a-88f194104e58/22-add-mesh-renderer.png)

   Click image for full size.
4. Click the dropdown for **Particle Mesh** and select your mesh. If you imported your own balloon model, select that. Or to test, you can select **Shape\_Sphere** from the sample material.

   [![Select Mesh Shape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/244313f3-fb06-416d-ae04-24b80a61a664/23-select-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/244313f3-fb06-416d-ae04-24b80a61a664/23-select-mesh.png)

   Click image for full size.
5. Your mesh may be too small or too big to show up well in your level. If needed, adjust the size here. Your mesh may have a default material applied to it. By enabling Override Materials, you can use the custom material you created instead. Click to enable **Override Materials**, then click the **Plus sign** (**+**) icon to add an element to the array.

   [![Enable Override Materials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/75d79feb-25f3-46e1-99d5-891fdf44ba25/24-set-mesh-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/75d79feb-25f3-46e1-99d5-891fdf44ba25/24-set-mesh-properties.png)

   Click image for full size.
6. Click the dropdown for **Explicit Mat**, and select the material you created earlier, **Balloon\_Material**.

   [![Select Balloon Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e901f8dd-2ecd-4eb4-9b6b-dcdbb39cfb66/25-select-balloon-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e901f8dd-2ecd-4eb4-9b6b-dcdbb39cfb66/25-select-balloon-material.png)

   Click image for full size.

## Edit Emitter Update Group Settings

First, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Select Emitter Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5967ee3d-3a47-4bcf-8529-8bc4cc1c1698/26-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5967ee3d-3a47-4bcf-8529-8bc4cc1c1698/26-select-emitter-update-group.png)

   Click image for full size.
2. Expand the **Emitter State** module. Because you used the Fountain template, the Life Cycle Mode is set to **Self**. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate the lifecycle settings, which usually optimizes performance.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80192724-c38b-483c-8022-cd91c9286e28/27-set-life-cycle-mode-to-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80192724-c38b-483c-8022-cd91c9286e28/27-set-life-cycle-mode-to-system.png)

   Click image for full size.
3. The **Spawn Rate** module creates a continuous stream of particles while the emitter is active. This module is already present in the Fountain template. Set the **Spawn Rate** to **100**.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e8b8576-d7a9-48f6-8429-64e25bcbdacc/28-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e8b8576-d7a9-48f6-8429-64e25bcbdacc/28-set-spawn-rate.png)

   Click image for full size.

## Edit Particle Spawn Group Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Select Particle Spawn](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c40a321-b0ff-4145-bdef-d2da23669adf/29-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c40a321-b0ff-4145-bdef-d2da23669adf/29-select-particle-spawn-group.png)

   Click image for full size.
2. Expand the **Initialize Particle** module. This module collects several related parameters together in one module, minimizing clutter in your stack. Under **Point Attributes**, locate the **Lifetime** parameter. This parameter determines how long particles will display before they disappear. For **Lifetime Mode**, select **Random**. Set the **Minimum** and **Maximum** values to the following.

   [![Set Lifetime Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f351a2e-77a4-4108-9095-ab96f727ca3d/30-set-lifetime-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f351a2e-77a4-4108-9095-ab96f727ca3d/30-set-lifetime-properties.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Minimum** | 2.0 |
   | **Maximum** | 4.0 |
3. Locate the **Color** parameter. You can choose to have all your balloons be one solid color, or use one of the other modes to add some variety. In this example, you can set the **Color Mode** to **Random Range**. This will create your balloons in random colors that fall in a range between two set colors. Change the **RGB** values until you achieve the look you like. The colors you set here are applied to the material you created earlier. In this example, the colors are set to red and blue.

   [![Set Color Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/655d8564-a003-485c-8ed7-3d111be42fa6/31-set-color-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/655d8564-a003-485c-8ed7-3d111be42fa6/31-set-color-properties.png)

   Click image for full size.

   | Setting | Color Minimum | Color Maximum |
   | --- | --- | --- |
   | **Red** | 1.0 | 0.0 |
   | **Green** | 0.0 | 0.0 |
   | **Blue** | 0.0 | 1.0 |
4. Under **Sprite Attributes**, set **Sprite Size Mode**, **Sprite Rotation Mode**, and **Sprite UV Mode** to **Unset**. Since you are using a mesh, these attributes are not needed for this effect.

   [![Disable Sprite Attributes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97f6e60a-2dc5-436d-8859-c97bf1147fc5/32-unset-sprite-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97f6e60a-2dc5-436d-8859-c97bf1147fc5/32-unset-sprite-properties.png)

   Click image for full size.
5. When you first set your mesh, you may have resized it at that time. But you may want some variation in the size, so some balloons are larger than others. Under **Mesh Attributes**, set **Mesh Scale Mode** to **Random Uniform**. Set the **Mesh Uniform Scale Min** to **0.7** and **Mesh Uniform Scale Max** to **1.0**. If you used a sphere instead of a balloon mesh, you may want to set the **Mesh Scale Mode** to **Random Non-Uniform** to give some irregularity to the shape of your spheres.

   [![Set Mesh Scale](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56994f3f-5453-493a-99be-f318a8192d17/33-set-mesh-scale-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56994f3f-5453-493a-99be-f318a8192d17/33-set-mesh-scale-properties.png)

   Click image for full size.
6. The **Add Velocity in Cone** module is not needed for the effect you are making. You don't want the balloons to spread out in a cone shape. Click on the trash can to remove this module from your stack.

   [![Remove the Add Velocity In Cone Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8fa5a7f-f26d-4ac8-95d7-2b74850ca68b/34-delete-velocity-in-cone-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8fa5a7f-f26d-4ac8-95d7-2b74850ca68b/34-delete-velocity-in-cone-module.png)

   Click image for full size.
7. The **Add Velocity** module will give the particles movement as soon as they spawn. Add the Add Velocity module to the Particle Spawn section by clicking the **Plus sign** (**+**) icon and selecting **Add Velocity**.

   [![Add the Add Velocity Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2f1bfd5-9723-4871-9c24-1940c1331969/35-add-velocity-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2f1bfd5-9723-4871-9c24-1940c1331969/35-add-velocity-module.png)

   Click image for full size.
8. Because this effect is meant to look like balloons being released, some randomness to the speed of the particles is needed. Click the downward arrow next to the **Velocity** value fields, and select **Random Range Vector**. This adds minimum and maximum velocity fields so that each balloon can be assigned a velocity value from within this range, adding randomness.

   [![Add Velocity Random Ranged Vector](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df987034-287b-4b2d-b030-2ddb41ef7e8a/36-set-velocity-to-random-range-vector.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df987034-287b-4b2d-b030-2ddb41ef7e8a/36-set-velocity-to-random-range-vector.png)

   Click image for full size.
9. Set the Velocity **Minimum** and **Maximum** values to the following. This gives the effect a small amount of movement on the X and Y axes, and a larger amount of movement on the Z axis.

   [![Set Velocity Minimum and Maximum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af96c0e8-2897-470d-bfbb-8ee5f8678760/37-set-velocity-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af96c0e8-2897-470d-bfbb-8ee5f8678760/37-set-velocity-properties.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Minimum** | **X**: 15, **Y**: 25, **Z**: 50 |
   | **Maximum** | **X**: 30, **Y**: 30, **Z**: 100 |
10. The **Sphere Location** module module controls the shape of the location where sprites spawn. You can have the sprites spawn in a sphere shape, and you can set the size of the sphere shape by indicating a radius. Set the **Sphere Radius** to **200**. This spreads the particles out more, as balloons would do when released.

    [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/009538c1-f2aa-4c34-bb55-1b9023358eb0/38-set-sphere-location-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/009538c1-f2aa-4c34-bb55-1b9023358eb0/38-set-sphere-location-radius.png)

    Click image for full size.

## Edit Particle Update Group Settings

Now you will edit the modules in the Particle Update group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Select Particle Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/523ccbf0-45c4-4501-877e-84faafa29c46/39-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/523ccbf0-45c4-4501-877e-84faafa29c46/39-select-particle-update-group.png)

   Click image for full size.
2. Typically, you would use the **Gravity Force** module to simulate how gravity affects objects. You can also use it more generally to add acceleration to your particles. Set the Gravity Force **X, Y and Z** values to the following.

   [![Set Gravity Force](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0eb7bdfd-4f78-4965-a177-f57f5a4fb524/40-set-gravity-values.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0eb7bdfd-4f78-4965-a177-f57f5a4fb524/40-set-gravity-values.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **X** | 10 |
   | **Y** | 10 |
   | **Z** | 40 |
3. The **Drag** module applies drag to the particles, which slows them down. Set the **Drag** to **1.0**.

   [![Set Drag](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a509efef-b33d-4a79-b123-4e9a8442efad/41-set-drag-value.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a509efef-b33d-4a79-b123-4e9a8442efad/41-set-drag-value.png)

   Click image for full size.
4. The **Scale Color** module is part of the Fountain template, but this effect does not require it. Click the **Trash can** icon to remove the Scale Color module.

   [![Remove Scale Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc74786e-64ec-4a1e-86e2-804202664a39/42-delete-scale-color-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc74786e-64ec-4a1e-86e2-804202664a39/42-delete-scale-color-module.png)

   Click image for full size.

## End Result

Congratulations! You've made a mesh particle effect in Niagara. You learned how to create a material, apply the particle color to that material, and use a static mesh as your particles. Continue to explore the options in the modules to refine the effect.

![Balloon Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2d48d1f-b64a-4f6c-a8f3-e73f52f172dc/balloon-final.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create a Material](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#createamaterial)
* [Create the System and Emitter](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#createthesystemandemitter)
* [Change the Renderer](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#changetherenderer)
* [Edit Emitter Update Group Settings](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#editemitterupdategroupsettings)
* [Edit Particle Spawn Group Settings](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#editparticlespawngroupsettings)
* [Edit Particle Update Group Settings](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#editparticleupdategroupsettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-use-a-solid-mesh-to-create-a-balloon-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
