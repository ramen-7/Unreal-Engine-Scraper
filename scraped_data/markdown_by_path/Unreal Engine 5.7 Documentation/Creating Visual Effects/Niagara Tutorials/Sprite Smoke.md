<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7 -->

# Sprite Smoke

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
7. Sprite Smoke

# Sprite Smoke

This document describes how you can create a smoke effect using sprite particles in Niagara.

![Sprite Smoke](https://dev.epicgames.com/community/api/documentation/image/560514ec-9f25-45b4-8848-efcf5188315b?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

 On this page

A commonly used visual effects (VFX) technique is rendering Texture and Materials to 2D camera-facing planes, which are called *sprites*. In the following tutorial, you will set up a Niagara Emitter to work with sprites. When you place the Niagara System containing the Niagara Emitter into a Level, you will see the effect displayed in that Level.

**Prerequisite Steps:**

This how-to uses the **M\_smoke\_subUV** Material, which can be found with the **Starter Content**. If you have not done so already, make sure that this Material or the Starter Content has been added to your project.

## Project Setup

1. First, make a new folder in the Content Browser to hold the assets for your effect. Make sure you are at the top level (Content), then right-click in the **Content Browser** and select **New Folder**. Name your folder something like **SpriteEffect**.

   If you are going to create multiple Niagara effects in your project, you might want to create a folder called NiagaraFX (or something similar), and then create a sub-folder for your sprite effect.
2. Before you can create this effect, you need to make or locate a material to use for the sprites in our emitter. For this example, you will use a material from the Starter Content. It is possible to pull in this material without locating it or moving it anywhere, but in some cases you might want to make a copy of the original and put that either in the folder for your effect, or in a separate Materials folder you have previously created. To do so, follow these steps:

   1. Type `m_smoke` in the search bar of the Content Browser. You should see the **M\_smoke\_subuv** material in your search results.

      [![Search for Smoke Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f324617b-b8d0-4bd4-8b7d-2491d09ab380/01-search-for-smoke-texture.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f324617b-b8d0-4bd4-8b7d-2491d09ab380/01-search-for-smoke-texture.png)

      Click image for full size.
   2. To put a copy of it in another folder, just click and drag that material to the desired folder, and in the popup menu select either **Move Here** or **Copy Here**. **Moving** it will delete the original material in its previous location, and move it to the new location. **Copying** it will create a copy in the new location, while leaving the original in its original location. If you want to create your own material for the sprite, see pages in the **Materials** section of our documentation.

## Create the System and Emitter

Next you will create a Niagara system, and inside it an emitter. The system is a container within which you can put one or more emitters. The emitter is the source of new particles that are generated.

1. First, create a **Niagara System** by right-clicking in the Content Browser, and from the displayed menu select **FX > Niagara System**. The Niagara System wizard displays.

   [![Create Niagara System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/203af48e-0c71-45dd-a5a8-cbd083683c71/02-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/203af48e-0c71-45dd-a5a8-cbd083683c71/02-create-niagara-system.png)

   Click image for full size.
2. Select **New system from selected emitters**. Then click **Next**.

   [![New System From Selected Emitters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/549a7efb-3536-4d05-8cf9-47abc79ee5cb/03-new-system-from-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/549a7efb-3536-4d05-8cf9-47abc79ee5cb/03-new-system-from-emitter.png)

   Click image for full size.
3. Under **Template**, select **Simple Sprite Burst**. Click the **Plus sign** icon (**+**) to add the emitter to the list of emitters to add to the system. Then click **Finish**.

   [![Add Sprite Burst Emitter to System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf15cf8f-0608-459c-aa3f-d9c4dc410637/04-select-emitters-to-add.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf15cf8f-0608-459c-aa3f-d9c4dc410637/04-select-emitters-to-add.png)

   Click image for full size.
4. Name the new system **SmokeSystem**. Double-click to open it in the Niagara Editor.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d0cac6a-5a95-4d65-95c0-2496912b7e76/05-rename-smoke-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d0cac6a-5a95-4d65-95c0-2496912b7e76/05-rename-smoke-system.png)
5. The emitter instance in your new system has the default name of **SimpleSpriteBurst**. You can rename it, however. Click the name of the emitter instance in the System Overview, and the field will become editable. Name the emitter **FX\_Smoke**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ceb3b19-ddab-4e04-a7f1-a2be77fbf6ca/06-rename-smoke-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ceb3b19-ddab-4e04-a7f1-a2be77fbf6ca/06-rename-smoke-emitter.png)

   Click image for full size.

## Change Renderer Settings

1. In this guide, you will go through the Emitter module groups as they appear in the stack. However, until you set your material in the Renderer you won't see anything in your preview or in your Level. So first, in the **System Overview** select the **Sprite Renderer** to open it in the **Selection** panel.

   [![Open Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e6953299-1648-4a80-88c8-fda81476e66a/07-open-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e6953299-1648-4a80-88c8-fda81476e66a/07-open-render-group.png)

   Click image for full size.
2. This is where you select the material for our effect. Since the material is a SubUV material, you need to tell the renderer how many images are in the image grid. Set the following properties to the following values.

   [![Change Renderer Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b10f59b-1eb0-4915-980f-ce9fa76f8723/08-set-sprite-renderer-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b10f59b-1eb0-4915-980f-ce9fa76f8723/08-set-sprite-renderer-settings.png)

   Click image for full size.

   | Property Name | Value |
   | --- | --- |
   | **Material** | M\_smoke\_subUV |
   | **Sub Image Size** | X: 8.0, Y: 8.0 |
   | **Sub UV Blending Enabled** | Checked |
3. Drag the **SmokeSystem** into your Level.

   When you make a particle effect, it is always a good idea to drag your system into your Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your Level.

## Edit the Emitter Update Group Settings

First you will edit the modules in the Emitter Update group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Open Emitter Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7873ba97-6f9c-4d9c-9050-05750598ae1d/09-open-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7873ba97-6f9c-4d9c-9050-05750598ae1d/09-open-emitter-update-group.png)

   Click image for full size.
2. You want to create a constant column of smoke, not a burst of smoke. Click the **Trashcan** icon to delete the **Spawn Burst Instantaneous** module.

   [![Remove Sprite Burst Instantaneous Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4705def-70bc-4c80-bd55-4de507e8f46a/10-delete-spawn-burst-instantaneous-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4705def-70bc-4c80-bd55-4de507e8f46a/10-delete-spawn-burst-instantaneous-module.png)

   Click image for full size.
3. Add the **Spawn Rate** module to the **Emitter Update** group by clicking the **Plus sign** icon (**+**) and selecting **Spawn Rate**.

   [![Add Spawn Rate Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55725c69-5c25-431f-9ab5-3817ece3e637/11-add-spawn-rate-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55725c69-5c25-431f-9ab5-3817ece3e637/11-add-spawn-rate-module.png)

   Click image for full size.
4. In the **Spawn Rate** module, set the Spawn Rate to **50**. This will give us a good-sized puffy shape made of smoke. This is a good start to your effect.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69e7479c-bcaa-42ea-b1a1-a5d90be66bf6/12-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69e7479c-bcaa-42ea-b1a1-a5d90be66bf6/12-set-spawn-rate.png)

   Click image for full size.
5. For now, while you are building the effect, you want to set the simulation to run on an infinite loop. This gives you more time to evaluate how the settings are affecting the effect. In the **Emitter State** module, click the dropdown for **Life Cycle Mode** and select **Self**. Then click the dropdown for **Loop Behavior**, and select **Infinite**.

   [![Emitter State Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58da0401-2559-4b61-8dd7-cfd5d011dd16/13-set-emitter-state-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58da0401-2559-4b61-8dd7-cfd5d011dd16/13-set-emitter-state-module.png)

   Click image for full size.

## Particle Spawn Group Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Open Particle Spawn](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a85e75a-af41-4bde-ae5d-8e473035eb71/14-open-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a85e75a-af41-4bde-ae5d-8e473035eb71/14-open-particle-spawn-group.png)

   Click image for full size.
2. Expand the **Initialize Particle** module. This module collects several related parameters together in one module, minimizing clutter in your stack. Under **Point Attributes**, locate the **Lifetime** parameter. This parameter determines how long particles will display before they disappear. You want a little randomness in the Lifetime parameter to better simulate real smoke. Set **Lifetime Mode** to **Random**, **Lifetime Min** to **2**, and **Lifetime Max** to **3**.

   [![Set Lifetime Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09ff08ed-739b-481d-9f51-e6b5f358a097/15-set-lifetime-min-and-max.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09ff08ed-739b-481d-9f51-e6b5f358a097/15-set-lifetime-min-and-max.png)

   Click image for full size.

   | Property Name | Value |
   | --- | --- |
   | **Lifetime Mode** | Random |
   | **Minimum** | 2.0 |
   | **Maximum** | 3.0 |
3. You are going to adjust the size of the sprite particles, to continue making the smoke effect more realistic. The original bundle of particles is rather small, so you are now going to increase the size. You will also make the size a little random, so the sprite particles overlap and make a more consistent smoke effect. Under **Sprite Attributes**, locate the **Sprite Size** parameter and make sure it is enabled. Set **Sprite Size Mode** to **Random Uniform**. Enter the following values for **Minimum** and **Maximum**.

   [![Set Size Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79a16e14-949a-4c96-9783-861064861040/16-set-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79a16e14-949a-4c96-9783-861064861040/16-set-sprite-size.png)

   Click image for full size.

   | Property Name | Value |
   | --- | --- |
   | **Sprite Size Mode** | Random Uniform |
   | **Uniform Sprite Size Min** | 75 |
   | **Uniform Sprite Size Max** | 200 |
4. You now have a larger mass of smoke. Now you are going to add some rotation, to add more variation to the particles' shape. Additionally, you will add randomness to the rotation to increase the variation. Set the dropdown next to **Sprite Rotation Mode** to **Direct Normalized Angle (0-1)**. This means the rotation angle is calculated as a number between 0 and 1 instead of degrees.

   [![Set Sprite Rotation Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a735d79-0ab6-431f-b706-9ad69e9d98f7/17-set-sprite-rotation-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a735d79-0ab6-431f-b706-9ad69e9d98f7/17-set-sprite-rotation-mode.png)

   Click image for full size.
5. Now click the dropdown arrow next to **Sprite Rotation Angle**, and select **Dynamic Inputs > Random Range Float**. This adds **Minimum** and **Maximum** fields to the Normalized Angle. The particles will rotate a random number of degrees when they spawn.

   [![Set Sprite Rotation Angle to Random Range Float](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3043cc4a-00d3-4274-8068-908d767734e1/18-set-angle-to-random-range-float.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3043cc4a-00d3-4274-8068-908d767734e1/18-set-angle-to-random-range-float.png)

   Click image for full size.
6. Set the **Minimum** and **Maximum** values as shown below.

   [![Set Sprite Rotation Angle Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd3fe096-30e0-408d-bc21-79920ce73dce/19-set-sprite-angle-min-and-max.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd3fe096-30e0-408d-bc21-79920ce73dce/19-set-sprite-angle-min-and-max.png)

   Click image for full size.

   | Property Name | Value |
   | --- | --- |
   | **Minimum** | 0.25 |
   | **Maximum** | 0.5 |
7. So now you have a fairly good size cloud of smoke, but it is just spinning in place. You want the smoke particles to start moving as soon as they spawn. So now you will add some initial velocity. Add the **Add Velocity** module to the Particle Spawn group by clicking the **Plus sign** (**+**) icon and selecting **Velocity > Add Velocity**.

   [![Add the Add Velocity Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ea6f1fe-9fa9-4e15-99ce-a30b5d4b86db/20-add-velocity-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ea6f1fe-9fa9-4e15-99ce-a30b5d4b86db/20-add-velocity-module.png)

   Click image for full size.
8. Click the dropdown arrow next to **Velocity** and select **Dynamic Inputs > Random Range Vector**. This adds **Minimum** and **Maximum** fields to the Velocity. Again, the slight randomness adds variation and naturalness to the effect.

   [![Add Random Ranged Vector to Velocity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc6e5c89-1c1e-4f34-873b-a7a23bfe2c82/21-set-velocity-to-random-range-vector.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc6e5c89-1c1e-4f34-873b-a7a23bfe2c82/21-set-velocity-to-random-range-vector.png)

   Click image for full size.
9. Set the Velocity **Minimum** and **Maximum** values as shown below.

   [![Set Velocity Minimum and Maximum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff3d2f3e-24e8-4738-b01c-25bd354609bb/22-set-velocity-min-and-max.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff3d2f3e-24e8-4738-b01c-25bd354609bb/22-set-velocity-min-and-max.png)

   Click image for full size.

   | Property Name | Value |
   | --- | --- |
   | **Minimum** | X: 0, Y: 0, Z: 50 |
   | **Maximum** | X: 1, Y: 1, Z: 200 |
10. Shape location controls the shape and origin of where sprites spawn. By adding a **Shape Location** module, you can have the sprites spawn in different shape primitives. Add the **Shape Location** module to the Particle Spawn group by clicking the **Plus sign** (**+**) icon and selecting **Location > Shape Location**.

    [![Add Shape Location Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/754d4aa9-71d7-4a7c-b66b-68bc9afacc1e/23-add-shape-location-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/754d4aa9-71d7-4a7c-b66b-68bc9afacc1e/23-add-shape-location-module.png)

    Click image for full size.
11. Set **Shape Primitive** to **Sphere**. By indicating a radius, you can set the size of the sphere shape. Set the **Sphere Radius** to 64. Make sure the **Sphere Distribution** is set to **Random**.

    [![Sphere Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f94f38d-63ce-474e-b3ff-11af474ca978/24-set-shape-location-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f94f38d-63ce-474e-b3ff-11af474ca978/24-set-shape-location-settings.png)

    Click image for full size.
12. The sprite material that we are using for this smoke effect uses a sprite sheet, which has multiple images that are designed to be strung together and animated. When you do not account for this, your renderer will only use the first sprite on the sheet. You can add a **SubUV Animation** module to solve this problem. Click the **Plus sign** (**+**) icon for Particle Spawn and select **Sub UV > SubUV Animation**.

    [![Add SubUV Animation Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/102f035e-f8b5-48bb-b054-a6f18e8499dd/25-add-sub-uv-animation-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/102f035e-f8b5-48bb-b054-a6f18e8499dd/25-add-sub-uv-animation-module.png)

    Click image for full size.
13. In the **Sub UV Animation** module, click the dropdown for **SubUV Animation Mode** and select **Linear**. For **Start Frame** type **0**, and for **End Frame** type **63**. The sprite sheet has an 8x8 grid of images, so the total number of images is 64.

    [![SubUV Animation Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/432d961c-02d3-4f71-afdf-01d1a640a9e5/26-set-sub-uv-animation-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/432d961c-02d3-4f71-afdf-01d1a640a9e5/26-set-sub-uv-animation-settings.png)

    Click image for full size.

## Particle Update Group Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to particles, and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Open Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d832c622-2036-421e-a99b-9c33b90a237d/27-open-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d832c622-2036-421e-a99b-9c33b90a237d/27-open-particle-update-group.png)

   Click image for full size.
2. The velocity you added in Particle Spawn gave the particles some movement when they initially spawn. Now you want to add movement over time, and you want the smoke to rise.
   Now you will add movement over time, and make the smoke rise. Add the Acceleration Force module by clicking the **Plus sign** (**+**) icon for **Particle Update** and selecting **Forces > Acceleration Force**.

   [![Add Acceleration Force](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1e15445-ca73-40fa-a2d0-40f84d4ea4d9/28-add-acceleration-force-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1e15445-ca73-40fa-a2d0-40f84d4ea4d9/28-add-acceleration-force-module.png)

   Click image for full size.
3. Leave the **X** and **Y** values set to **0**, and the **Z** value to **500**. This will give the smoke significant upward movement over time. You can adjust this setting, or even remove this module, depending on the type of smoke effect you want to create.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92dce7cc-32e1-4d90-aff9-e6dfd9bb72ae/29-set-acceleration-values.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92dce7cc-32e1-4d90-aff9-e6dfd9bb72ae/29-set-acceleration-values.png)

   Click image for full size.
4. If you want to be able to reuse the smoke emitter in your system, you can save it as a separate asset. Click the **Gear** icon to open the **Emitter Settings** menu, and select **Create Assset From This**. The result is an independent Niagara Emitter asset.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5bba9531-81d5-441e-a7c7-57b8f4ae67cd/30-create-asset-from-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5bba9531-81d5-441e-a7c7-57b8f4ae67cd/30-create-asset-from-emitter.png)

   Click image for full size.
5. Then click the **Save** button to apply and save the changes.  
   ![Save System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6ef8822-6eea-478b-a3c0-4b90704d87a2/31-save-file.png)

## End Result

Congratulations! You have created a simple smoke effect using sprites.

![Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7e8c89c-60c1-4a96-bb24-84ce4fafad87/final-sprite-effect.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Project Setup](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#projectsetup)
* [Create the System and Emitter](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#createthesystemandemitter)
* [Change Renderer Settings](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#changerenderersettings)
* [Edit the Emitter Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#edittheemitterupdategroupsettings)
* [Particle Spawn Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#particlespawngroupsettings)
* [Particle Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#particleupdategroupsettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine?application_version=5.7#endresult)
