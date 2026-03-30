<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# GPU Sprite Effect

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
7. GPU Sprite Effect

# GPU Sprite Effect

This document describes how you can use your GPU to spawn millions of sprite particles.

![GPU Sprite Effect](https://dev.epicgames.com/community/api/documentation/image/4735fd1c-fceb-4e26-acf8-044208c7ddf9?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

 On this page

For some effects, you may need to spawn tens of thousands of particles. However, using the standard CPU to generate this many particles can cause performance issues. In this guide, we will show you how to create a sprite particle effect that uses the GPU instead of the CPU to run the simulation.

## Create the System and Emitter

Niagara emitters and systems are independent. The current recommended workflow is to create a system from existing emitters or emitter templates.

1. First, create a Niagara System by right-clicking in the Content Browser, and from the displayed menu select **FX > Niagara System**. The Niagara System wizard displays.

   [![Create Niagara System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e429db0b-bb9d-4656-a26a-532fcbe5c9cc/ue5_01-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e429db0b-bb9d-4656-a26a-532fcbe5c9cc/ue5_01-create-niagara-system.png)

   Click image for full size.
2. Select **New system from selected emitters**. Then click **Next**.

   [![System Wizard](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e61cf85a-e01a-4ed5-be19-51290f47d97d/ue5_02-system-wizard.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e61cf85a-e01a-4ed5-be19-51290f47d97d/ue5_02-system-wizard.png)

   Click image for full size.
3. Under **Templates**, select **Simple Sprite Burst**.

   [![Select the Sprite Burst Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fb792c9-e4e8-4767-879d-e9a35f79e28d/ue5_03-select-the-sprite-burst-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fb792c9-e4e8-4767-879d-e9a35f79e28d/ue5_03-select-the-sprite-burst-template.png)

   Click image for full size.
4. Click the **Plus icon** (**+**) to add the emitter to the list of emitters to add to the system. Then click **Finish**.

   [![Add Emitter and Finish](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d044750-51e3-4a44-8a20-03c65146d6ef/ue5_04-add-emitter-and-finish.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d044750-51e3-4a44-8a20-03c65146d6ef/ue5_04-add-emitter-and-finish.png)

   Click image for full size.
5. Name the new system **GPUSprite**. Double-click to open it in the Niagara Editor.

   [![Name New System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f1c14dd-c73b-4dce-8467-446b3f11ab55/ue5_05-name-new-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f1c14dd-c73b-4dce-8467-446b3f11ab55/ue5_05-name-new-system.png)

   Click image for full size.
6. The emitter instance in your new system has the default name of **SimpleSpriteBurst**, but you can rename it. Click the name of the emitter instance in the **System Overview**, and the field will become editable. Name the emitter **FX\_GPUSprite**.

   [![Open Emitter Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b5e2d5c-0cf2-4cab-aeba-2fb0055e550f/ue5_06-open-emitter-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b5e2d5c-0cf2-4cab-aeba-2fb0055e550f/ue5_06-open-emitter-properties.png)

   Click image for full size.
7. Drag the **GPUSprite** system into your Level.

When you make a particle effect, it is always a good idea to drag your system into your Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your Level.

## Emitter Settings - Emitter Properties

First, you need to change some settings in the **Emitter Properties**. This is where you switch from CPU simulation to GPU simulation.

1. In the **System Overview**, click **Emitter Settings** to open it in the **Selection** panel.

   [![Open Emitter Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17008e3b-b18c-4d8f-b9aa-c47cf1de9e10/ue5_07-open-emitter-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17008e3b-b18c-4d8f-b9aa-c47cf1de9e10/ue5_07-open-emitter-settings.png)

   Click image for full size.
2. Expand **Emitter Properties**. Locate the **Sim Target** field. This is where you tell Unreal Engine to use the GPU for the simulation. Click the dropdown and select **GPUComputeSim**.

   [![Change Emitter Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/158c8265-6462-4216-89ac-473bc05ec576/ue5_08-change-emitter-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/158c8265-6462-4216-89ac-473bc05ec576/ue5_08-change-emitter-properties.png)

   Click image for full size.
3. You may trigger a warning about the Fixed Bounds not being set. Click the box for **Fixed Bounds**. This will resolve the error. Leave the **Minimum** and **Maximum** set to the default values.

   Because the particle simulation is done on the GPU, the system cannot read how big the effect is. This is why it is necessary to set fixed bounds. You can do so in the emitter, as shown in this step, or you can set fixed bounds for the entire system in the **System Properties** item.

## Emitter Update Group Settings

Next, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click **Emitter Update** to open it in the **Selection** panel.

   [![Open Emitter Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1ba17a4-2115-47b5-b3d0-15a9323ae050/ue5_09-open-emitter-update.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1ba17a4-2115-47b5-b3d0-15a9323ae050/ue5_09-open-emitter-update.png)

   Click image for full size.
2. Expand the **Emitter State** module. This module controls time and scalability for this emitter. Because you used the Simple Sprite Burst template, the **Life Cycle Mode** is set to **Self**. Normally this is used for complete customization of emitter life cycle logic for this specific emitter, but it is not needed for this effect. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate the life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Change Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1265b72a-ba7f-4fa1-a977-39ea210e86b3/ue5_10-change-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1265b72a-ba7f-4fa1-a977-39ea210e86b3/ue5_10-change-life-cycle-mode.png)

   Click image for full size.
3. The **Spawn Burst Instantaneous** module creates a large burst of particles when the emitter spawns. This module is included in the Simple Sprite Burst template. Set the **Spawn Count** to **2500**. Because **Spawn Time** is set to **0**, the burst occurs immediately upon startup.

   [![Set Burst Spawn Count](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bba51667-db30-46c6-9d86-7de032074294/ue5_11-set-burst-spawn-count.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bba51667-db30-46c6-9d86-7de032074294/ue5_11-set-burst-spawn-count.png)

   Click image for full size.
4. For this effect, you need more than just a burst of particles when the emitter spawns. The **Spawn Rate** module creates a continuous stream of particles while the emitter is active. Add the **Spawn Rate** module by clicking the **Plus sign** icon (**+**) for Emitter Update and selecting **Spawning > Spawn Rate**.

   [![Add Spawn Rate Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/757aec6e-4794-496b-8791-e1c2b986d8cc/ue5_12-add-spawn-rate-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/757aec6e-4794-496b-8791-e1c2b986d8cc/ue5_12-add-spawn-rate-module.png)

   Click image for full size.
5. Set the **Spawn Rate** to **500**. This will spawn particles at the rate of 500 per second, which will provide a continuous stream of particles after the initial burst.

   [![Set Continuous Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b00e0ca-2e35-4f94-a454-f22a7e370c02/ue5_13-set-continuous-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b00e0ca-2e35-4f94-a454-f22a7e370c02/ue5_13-set-continuous-spawn-rate.png)

   Click image for full size.

## Particle Spawn Group Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click **Particle Spawn** to open it in the **Selection** panel.

   [![Open Particle Spawn](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e2a670e-d2c4-4c60-933a-9b720f18123d/ue5_14-open-particle-spawn.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e2a670e-d2c4-4c60-933a-9b720f18123d/ue5_14-open-particle-spawn.png)

   Click image for full size.
2. Expand the **Initialize Particle** module. This module collects several related parameters together in one module, minimizing clutter in your stack. Under **Point Attributes**, locate the **Lifetime** parameter.
3. The Lifetime parameter determines how long particles will display before they disappear. For this effect you want a constant value, so that the particles will display for the entire duration of the effect. Set the **Lifetime** to **5**.

   [![Set Lifetime Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fdff22a-e3d1-4262-ad44-da8f097ba531/ue5_15-set-lifetime-parameter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fdff22a-e3d1-4262-ad44-da8f097ba531/ue5_15-set-lifetime-parameter.png)

   Click image for full size.
4. You will make the sprite size randomized in another part of this guide, but here we will set the base size of the sprite. Under **Sprite Attributes**, locate the **Sprite Size** parameter and make sure it is enabled. Set the **Sprite Size** to the following.

   [![Set Base Sprite Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f19ebc7-e888-4d5d-a5ba-15605bfca185/ue5_16-set-base-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f19ebc7-e888-4d5d-a5ba-15605bfca185/ue5_16-set-base-sprite-size.png)

   Click image for full size.

   | Size Vector | Value |
   | --- | --- |
   | **X** | 5 |
   | **Y** | 5 |
5. Sphere location controls the shape of the location where sprites spawn. Add the **Sphere Location** module by clicking the **Plus sign** icon (**+**) for Particle Spawn and selecting **Location > Sphere Location**.

   [![Add Sphere Location Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e68680fc-0ab2-40bb-b517-08340ca0159a/ue5_17-shape-location.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e68680fc-0ab2-40bb-b517-08340ca0159a/ue5_17-shape-location.png)

   Click image for full size.
6. By adding the **Sphere Location** module, the sprites spawn in a sphere shape, and you can set the size of the sphere shape by indicating a radius. Select **Sphere** from the drop down menu **Shape Primitive > Sphere**.

   [![Select Sphere from the Shape Primitive menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0924516-2712-456c-a3be-648d80ba8354/ue5_18-add-sphere-location-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0924516-2712-456c-a3be-648d80ba8354/ue5_18-add-sphere-location-module.png)

   Click image for full size.

## Particle Update Group Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Open Particle Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26c7a8fc-3128-4e19-bdf8-5b38ad7c9189/ue5_19-open-particle-update.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26c7a8fc-3128-4e19-bdf8-5b38ad7c9189/ue5_19-open-particle-update.png)

   Click image for full size.
2. In the Initialize Particle module of the Particle Spawn group, you picked the base size of the sprites. You can randomize the size of the sprites by adding the Scale Sprite Size module. This applies a scaling factor to the base size. Add the **Scale Sprite Size** module by clicking the **Plus sign** icon (**+**) and selecting **Size > Scale Sprite Size**.

   [![Add Scale Sprite Size Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e3bc0a5-e25d-4ea4-8fff-47ac2fa11d67/ue5_20-add-scale-sprite-size-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e3bc0a5-e25d-4ea4-8fff-47ac2fa11d67/ue5_20-add-scale-sprite-size-module.png)

   Click image for full size.
3. Select **Non-Uniform** from the drop down menu **Scale Sprite > Non-Uniform**.

   [![Select Non-Uniform from the Scale Sprite menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b619f7f-8a69-4efc-b3e8-a46883f654c7/ue5_21-scale-sprite-parameter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b619f7f-8a69-4efc-b3e8-a46883f654c7/ue5_21-scale-sprite-parameter.png)

   Click image for full size.
4. The default values for Scale Sprite Size are **X: 1** and **Y: 1**. Changing these default values will uniformly make all the particles bigger or smaller. However, random size variation is more visually interesting than a static size. Click the downward arrow next to the **Scale Factor** field, and select **Dynamic Inputs > Vector2D from Float**.

   [![Add Vector2D from Float](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38ed63e3-a9dd-4bf8-953a-86ccf5edd9af/ue5_22-add-vector2d-from-float.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38ed63e3-a9dd-4bf8-953a-86ccf5edd9af/ue5_22-add-vector2d-from-float.png)

   Click image for full size.
5. Notice that the value for **Scale Factor** has changed to one static value. There are several ways to add a float value, depending on what you want the particles to look like. For a flowing and gradual size change, a curve is ideal. Click the downward arrow next to **Value**, and select **Dynamic Inputs > Float from Curve**.

   [![Add Float from Curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8488717-0885-4ffa-b2bb-b5bd4ea336b6/ue5_23-add-float-from-curve.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8488717-0885-4ffa-b2bb-b5bd4ea336b6/ue5_23-add-float-from-curve.png)

   Click image for full size.
6. Open the **Scale Sprite Size** module. Click on the **Ramp Up Down** curve template to apply that shape to the curve.

   [![Curve Templates](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa140eaf-ef64-4d91-98c8-b7c99d4bb082/ue5_24-curve-templates.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa140eaf-ef64-4d91-98c8-b7c99d4bb082/ue5_24-curve-templates.png)

   Click image for full size.
7. Just click on the template that matches that curve.

   [![Curve Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0232f036-5ff2-4050-97d1-73e97fa91291/ue5_25-curve-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0232f036-5ff2-4050-97d1-73e97fa91291/ue5_25-curve-settings.png)

   Click image for full size.
8. Right now, your current settings just create a ball of particles that is not very interesting. You can add some additional elements that increase the variation and movement of the particles. Click the **Plus sign** icon (**+**) for Particle Update, and select **Forces > Curl Noise Force**.

   [![Add Curl Noise Force Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ae5bcec-0c76-4f14-aa30-045d2e2d55b2/ue5_26-add-curl-noise-force-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ae5bcec-0c76-4f14-aa30-045d2e2d55b2/ue5_26-add-curl-noise-force-module.png)

   Click image for full size.
9. There are a lot of things you can do with Curl Noise Force. **Noise Strength** controls how large the overall noise field is (in other words, how much the noise disrupts the original sphere of particles). **Noise Frequency** controls how often the curl noise is applied to the particles: the smaller the number, the more warped the sphere location of the particles will become. Use the settings below for now, but later you can experiment with these to get a different look.

   [![Curl Noise Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80bc25a8-536e-4a83-bade-71496be6e60d/ue5_27-curl-noise-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80bc25a8-536e-4a83-bade-71496be6e60d/ue5_27-curl-noise-settings.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Noise Strength** | 72 |
   | **Noise Frequency** | .02 |
   |  |  |
10. Now you will see that the particles swirl at first, then just move outward continuously until they die. For this effect, the particles should move outward and then back in toward their origin point, to make a swirling mass. The **Point Attraction Force** module makes the particles move toward a single point (by default, this point is the emitter's position). Click the **Plus sign** icon (**+**) for Particle Update, and select **Forces > Point Attraction Force**.

    [![Add Point Attraction Force Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52964101-3587-4663-b752-587a33ae8daa/ue5_28-add-point-attraction-force-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52964101-3587-4663-b752-587a33ae8daa/ue5_28-add-point-attraction-force-module.png)

    Click image for full size.
11. **Attraction Strength** is the amount of force pulling the particles to the attractor point. **Attraction Radius** delineates the size of the field in which the point attraction force applies to the particles. The **Falloff Exponent** controls how much the sphere spreads; the smaller the number, the more the sphere of particles spreads out. The **Kill Radius** sets the size of the area where the particles dissolve at the end of their life cycle. Set the **Attraction Strength**, **Attraction Radius**, **Falloff Exponent**, and **Kill Radius** to the following values.

    Click the triangle at the bottom of the module to display the **Kill Radius** parameter. Check the box to enable it, if it is not already checked.

    [![Point Attraction Force Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53dd3d95-5a26-4567-8cff-097396549731/ue5_29-point-attraction-force-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53dd3d95-5a26-4567-8cff-097396549731/ue5_29-point-attraction-force-settings.png)

    Click image for full size.

    | Parameter | Value |
    | --- | --- |
    | **Attraction Strength** | 5.5 |
    | **Attraction Radius** | 300.0 |
    | **Falloff Exponent** | 0.6 |
    | **Kill Radius** | 4.0 |
    |  |  |
12. Now for changing the color. Add the **Color** module by clicking the Plus sign icon (+) for Particle Update and selecting **Color > Color**.

    [![Add Color Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5329408d-b669-4a36-a2eb-f633145bcc2f/ue5_30-add-color-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5329408d-b669-4a36-a2eb-f633145bcc2f/ue5_30-add-color-module.png)

    Click image for full size.
13. Click the downward arrow next to **Color**, and select **General > Dynamic Inputs > Color from Curve**.

    [![Add Color from Curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c62f6013-df59-4a6a-ae57-1d5b381224a4/ue5_31-add-color-from-curve.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c62f6013-df59-4a6a-ae57-1d5b381224a4/ue5_31-add-color-from-curve.png)

    Click image for full size.
14. You can add a color stop to the curve by clicking the space above the colored bar, and you can change the color by double clicking a stop to open the Color Picker.

    [![Color Picker](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14f8e3e8-483a-4893-8883-2464c0901eac/ue5_32-color-picker.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14f8e3e8-483a-4893-8883-2464c0901eac/ue5_32-color-picker.png)

    Click image for full size.
15. To set an opacity stop, click in the space below the bar.

    [![Set an Opacity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a93566ee-830f-4fc5-84da-2f90df1d2572/ue5_33-set-an-opacity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a93566ee-830f-4fc5-84da-2f90df1d2572/ue5_33-set-an-opacity.png)

    Click image for full size.
16. To set the time, click in the space below the bar.

    [![Set the time](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f024c7fb-173e-41e7-8579-587a98563a78/ue5_34-set-the-time.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f024c7fb-173e-41e7-8579-587a98563a78/ue5_34-set-the-time.png)

    Click image for full size.
17. Set the colors and opacity as shown below.

    [![Set Color and Opacity Stops](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11ed119b-770c-4161-89fc-e88346f274d3/ue5_35-set-color-and-opacity-stops.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11ed119b-770c-4161-89fc-e88346f274d3/ue5_35-set-color-and-opacity-stops.png)

    Click image for full size.

    | Color or Opacity Stop | Time | Values |
    | --- | --- | --- |
    | Color |  |  |
    | **Stop 1** | 0.0 | R: 1, G: 0, B: 1 |
    | **Stop 2** | .35 | R: .08, G: 0, B: 1 |
    | **Stop 3** | ..60 | R: .2 , G: 1, B: .8 |
    | **Stop 4** | .8 | R: 1, G: .96, B: .3 |
    | Opacity |  |  |
    | **Stop 1** | 0 | 1 |
    | **Stop 2** | .7 | 1 |
    | **Stop 3** | 1 | 0 |
    |  |  |  |

## End Result

Congratulations! You've created a cool sprite effect that uses the GPU instead of the CPU.

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create the System and Emitter](/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7#createthesystemandemitter)
* [Emitter Settings - Emitter Properties](/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7#emittersettings-emitterproperties)
* [Emitter Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7#emitterupdategroupsettings)
* [Particle Spawn Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7#particlespawngroupsettings)
* [Particle Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7#particleupdategroupsettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
