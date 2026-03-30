<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-dark-smoke-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# Dark Smoke

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
7. Dark Smoke

# Dark Smoke

This tutorial shows how to modify the sprite smoke effect to create a dark smoke effect.

![Dark Smoke](https://dev.epicgames.com/community/api/documentation/image/5566e1d6-2092-49ac-b5a5-d1ce26a3a0a2?resizing_type=fill&width=1920&height=335)

 On this page

You created a basic sprite effect by completing the [Create a Sprite Smoke Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine) tutorial. In this tutorial, learn how to duplicate an emitter, create a Niagara system from a pre-existing emitter, and make further adjustments to change the look of the smoke.

**Prerequisite Steps:**

This how-to uses the **M\_smoke\_subUV** Material, which can be found with the Starter Content. If you have not done so already, make sure that your project includes the Starter Content. This how-to also uses the **FX\_Smoke** emitter created in the tutorial [Create a Sprite Smoke Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine).

## Create System and Emitter

You can create a Niagara system from scratch by right-clicking in the Content Drawer as has been done in previous tutorials. However, if you already have a saved emitter to use as a starting point, it's also possible to duplicate it and start from there.

1. Create a new folder for this tutorial in the Content folder for your project.
2. Make a copy of the **FX\_Smoke** emitter you created in [Create a Sprite Particle Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine).

   [![Duplicate FX_Smoke Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b78a84b3-7c1f-4750-91a5-2a6dfc56b95a/01-duplicate-smoke.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b78a84b3-7c1f-4750-91a5-2a6dfc56b95a/01-duplicate-smoke.png)

   Click image for full size.
3. Drag this duplicate emitter to the folder you created in step 1. In the popup context menu, select **Move**.
4. Rename the copied emitter **FX\_DarkSmoke**. This distinguishes it from the smoke effect created in the [Create a Sprite Smoke Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine) tutorial.

   ![Rename the Duplicate Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b867fab-71dd-4eeb-86ed-78078b238a06/02-rename-emitter.png "Rename the Duplicate Emitter")
5. Right-click on your new smoke emitter, and select **Create Niagara System**.

   [![Create Niagara System from Existing Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d98076f3-21de-4b2b-8e71-fc411605ecb5/03-create-niagara-system-from-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d98076f3-21de-4b2b-8e71-fc411605ecb5/03-create-niagara-system-from-emitter.png)



   There are multiple ways to create new Niagara systems. Because you are starting with an emitter you have already created, the method used here quickly creates a system containing that emitter.
6. Name the system **DarkSmoke**. This is to distinguish it from the smoke effect created in the [Create a Sprite Smoke Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine) tutorial.

   ![Rename System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad310be5-9a74-44e3-8cb8-03f6c6ced461/04-dark-smoke-system.png "Rename System")
7. Drag the DarkSmoke system from the **Content Drawer** into your Level, so you can preview the changes in the context of your project's world.

   [![Drag the System into Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0b6e19b-0824-4b4c-bf2f-5eec792481fc/05-drag-system-into-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0b6e19b-0824-4b4c-bf2f-5eec792481fc/05-drag-system-into-level.png)

   Click image for full size.

   When you make a particle effect, it is always a good idea to drag your system into your Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your Level.
8. Double-click the **FX\_DarkSmoke** emitter to open it in the Niagara Editor. After you have edited the settings in the emitter, you will need to save the DarkSmoke system also.

## Edit the Emitter Update Settings

First you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter itself, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Open Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8e984ed-7e0e-439e-8152-98f4dfad0060/06-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8e984ed-7e0e-439e-8152-98f4dfad0060/06-select-emitter-update-group.png)

   Click image for full size.
2. Expand the **Emitter State** module. This module controls time and scalability for this emitter. Because you used the Simple Sprite Burst template, the **Life Cycle Mode** is set to **Self**.

   Normally this is used for complete customization of emitter life cycle logic for this specific emitter, but it is not needed for this effect. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06ee1b44-b547-4ee2-aa00-b16f212dad53/07-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06ee1b44-b547-4ee2-aa00-b16f212dad53/07-life-cycle-mode.png)

   Click image for full size.
3. Open the **Spawn Rate** module. Set the **Spawn Rate** to **25**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b546f897-f62a-4661-bb4f-5848fe93384f/08-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b546f897-f62a-4661-bb4f-5848fe93384f/08-spawn-rate.png)

   Click image for full size.

## Edit the Particle Spawn Settings

Next, you will edit the modules in the Particle Spawn group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Open Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9996d34a-08b3-4de8-b26c-c17c3353374c/09-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9996d34a-08b3-4de8-b26c-c17c3353374c/09-select-particle-spawn-group.png)

   Click image for full size.
2. Open the **Initialize Particle** module. Under **Point Attributes**, expand **Lifetime**. The Lifetime parameter determines how long particles will display before they disappear. Change the **Lifetime Mode**, **Minimum** and **Maximum** values to the following.

   [![Set Particle Lifetime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b3346f1-e213-42ac-a73f-a4edae2898aa/10-lifetime-attributes.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b3346f1-e213-42ac-a73f-a4edae2898aa/10-lifetime-attributes.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Lifetime Mode** | Random |
   | **Minimum** | 3.0 |
   | **Maximum** | 5.0 |
3. Expand **Color**. You can set the smoke to a single color, or change the **Color Mode** to **Random Range** to get some variability in the color of each particle. Change the RGB values to the following:

   [![Set Initial Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab2903a9-a390-4f15-91ac-d35ea6bd50ab/11-color-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab2903a9-a390-4f15-91ac-d35ea6bd50ab/11-color-settings.png)

   Click image for full size.

   | Color | Minimum | Maximum |
   | --- | --- | --- |
   | **Red** | 0.5 | 0.205 |
   | **Green** | 0.5 | 0.205 |
   | **Blue** | 0.5 | 0.205 |
4. Under **Sprite Attributes**, expand **Sprite Size**. Make sure **Sprite Size Mode** is set to **Random Uniform**, which gives minimum and maximum values. New particles will be created at a random size between these values. Change the **Minimum** and **Maximum** values to the following:

   [![Set Sprite Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86be1eb1-14ed-4de6-bf69-839e30882f8f/12-sprite-size-attributes.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86be1eb1-14ed-4de6-bf69-839e30882f8f/12-sprite-size-attributes.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Minimum** | 50 |
   | **Maximum** | 90 |
5. Open the **Add Velocity** module. In the previous tutorial, we had set the Velocity to Random Range Vector. This adds Minimum and Maximum values. Each new particle that is created has a random value between these two ranges set for its initial velocity. Change the **Velocity** Minimum and Maximum values to the following:

   [![Set Velocity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ccf0c87-b311-4580-b625-29b26508c561/13-velocity-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ccf0c87-b311-4580-b625-29b26508c561/13-velocity-settings.png)

   Click image for full size.

   | Value | Minimum | Maximum |
   | --- | --- | --- |
   | **X** | 12 | 32 |
   | **Y** | 0 | 0 |
   | **Z** | 5 | 7 |
6. Open the **Sphere Location** module. New particles are generated within the sphere when they are first created. Change the **Sphere Radius** value to **30**.

   [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e67e55e-6df4-43c4-89db-df3f682b84be/14-sphere-location-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e67e55e-6df4-43c4-89db-df3f682b84be/14-sphere-location-radius.png)

   Click image for full size.

## Edit the Particle Update Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Open Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8390335-49e6-4e9c-bf98-df94391d9c5a/15-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8390335-49e6-4e9c-bf98-df94391d9c5a/15-select-particle-update-group.png)

   Click image for full size.
2. Open the **Acceleration Force** module. Set the Acceleration **Z** value to **20**.

   [![Set Acceleration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5437b82-4293-47d4-8e95-50dc6c80ed9a/16-acceleration-values.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5437b82-4293-47d4-8e95-50dc6c80ed9a/16-acceleration-values.png)

   Click image for full size.
3. Open the **Scale Color** module. Make sure the **Scale Mode** is set to **RGB and Alpha Separately**. You only want to adjust the alpha values so that the color fades in and then pulses out as the particle ages. **Scale Alpha** should be set to **Float from Curve**. Click on the **Pulse** template in the curve editor to quickly apply this shape to the curve.

   [![Set Curve to Pulse](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/866aa226-923a-463d-a47a-c18cbd77b57b/17-set-color-pulse-out-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/866aa226-923a-463d-a47a-c18cbd77b57b/17-set-color-pulse-out-template.png)

   Click image for full size.

## End Result

After following these steps, the Smoke system in your level will produce a smoke effect similar to the one in the image below.

![Dark Smoke Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9200e9f7-1127-4df7-9431-973296185d5f/dark-smoke-final.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create System and Emitter](/documentation/en-us/unreal-engine/how-to-create-a-dark-smoke-effect-in-niagara-for-unreal-engine?application_version=5.7#createsystemandemitter)
* [Edit the Emitter Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-dark-smoke-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheemitterupdatesettings)
* [Edit the Particle Spawn Settings](/documentation/en-us/unreal-engine/how-to-create-a-dark-smoke-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticlespawnsettings)
* [Edit the Particle Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-dark-smoke-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticleupdatesettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-dark-smoke-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
