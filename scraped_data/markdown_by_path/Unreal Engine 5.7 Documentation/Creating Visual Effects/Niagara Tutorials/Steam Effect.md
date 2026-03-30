<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-steam-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# Steam Effect

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
7. Steam Effect

# Steam Effect

This how-to describes how to create a steam effect using Niagara.

![Steam Effect](https://dev.epicgames.com/community/api/documentation/image/8cda2ca7-b2bf-47d8-8f7a-2cae5b277d49?resizing_type=fill&width=1920&height=335)

 On this page

**Prerequisite Steps:**

This How-To uses the M\_smoke\_subUV Material, which can be found with the Starter Content. If you have not done so already, make sure that your project includes the Starter Content. This how-to also uses the FX\_Smoke emitter created in [Create a Sprite Particle Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine).

## Create the Steam Emitter and System

Niagara emitters and systems are independent. The current recommended workflow is to create a system from existing emitters or emitter templates. However, since you are duplicating an existing emitter, the process will be slightly different.

1. Create a new folder for this How-To in the **Content** folder for your project.
2. Locate the FX\_Smoke emitter you saved when working through [Create a Sprite Particle Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-beam-effect-in-niagara-for-unreal-engine). Right-click on the emitter, and select **Duplicate Emitter**.

   [![Duplicate Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ea2ac3e-c4d8-4236-8796-7baa8426629d/ue5_01-duplicate-emitter-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ea2ac3e-c4d8-4236-8796-7baa8426629d/ue5_01-duplicate-emitter-1.png)

   Click image for full size.
3. Drag this duplicate emitter to the folder you created in step 1. In the popup context menu, select **Move**.
4. Rename the copied emitter **FX\_Steam**.

   ![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f4c4c21-be74-435b-9f25-a7c7785ddeed/ue5_02-rename-emitter.png "Rename Emitter")
5. Now create a system for your steam effect. Right-click on your new steam emitter, and select **Create Niagara System**.

   [![Create New System from Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ecac335-5e11-45d8-9ec3-781618449a8c/ue5_03-create-new-system-from-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ecac335-5e11-45d8-9ec3-781618449a8c/ue5_03-create-new-system-from-emitter.png)

   Click image for full size.

   There are multiple ways to create new Niagara systems. Because you are starting with an emitter you have already created, the method used here quickly creates a system containing that emitter. However, as you saw in the Create a Sprite Particle Effect how-to, there are emitter and system wizards that give you many other options for creating and setting up a Niagara system.
6. Name the system **Steam**.

   ![Name System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/60c11b39-58f9-4dc7-8182-2df7a288ab4d/ue5_04-name-system.png "Name System")
7. Open your Level in the Level Editor, if it isn't open already. Drag the Steam system into your level.

   [![Drag System Into Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/794694d4-10c3-42dd-8a4a-c4a1981e2875/ue5_05-drag-system-into-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/794694d4-10c3-42dd-8a4a-c4a1981e2875/ue5_05-drag-system-into-level.png)

   Click image for full size.

     


   When you make a particle effect, it is always a good idea to drag your system into your level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your level.

## Edit the Emitter Update Settings

First you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter itself, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Open Emitter Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6be462fd-ea19-4d8f-ba8a-e111f1ac953c/ue5_06-open-emitter-update.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6be462fd-ea19-4d8f-ba8a-e111f1ac953c/ue5_06-open-emitter-update.png)

   Click image for full size.
2. Expand the **Emitter State** module.This module controls time and scalability for this emitter. Because you used the Simple Sprite Burst template, the **Life Cycle Mode** is set to **Self**. Normally this is used for complete customization of emitter life cycle logic for this specific emitter, but it is not needed for this effect. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Set Emitter Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53e5c5e3-2794-4c48-b765-fd8305d71530/ue5_07-set-emitter-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53e5c5e3-2794-4c48-b765-fd8305d71530/ue5_07-set-emitter-life-cycle-mode.png)

   Click image for full size.
3. Expand the **Spawn Rate** module. Change the **Spawn Rate** setting to **30**.

   [![Open Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05290313-d799-42fa-bac8-909375adf1d6/ue5_08-open-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05290313-d799-42fa-bac8-909375adf1d6/ue5_08-open-spawn-rate.png)

   Click image for full size.

## Edit the Particle Spawn Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Open Particle Spawn](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b0fcc76-f106-4e6b-a010-4c3589d92a85/ue5_09-open-particle-spawn.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b0fcc76-f106-4e6b-a010-4c3589d92a85/ue5_09-open-particle-spawn.png)

   Click image for full size.
2. Open the **Initialize Particle** module. Under **Point Attributes**, expand **Lifetime**. Change the Minimum and Maximum values to the following:

   [![Set Particle Lifetime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b49902b3-a5cf-44ce-98ec-7b6b6d4f25e3/ue5_10-set-particle-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b49902b3-a5cf-44ce-98ec-7b6b6d4f25e3/ue5_10-set-particle-lifetime.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Minimum** | 3.0 |
   | **Maximum** | 7.0 |
   |  |  |
3. Expand **Color**. Change the **RGB** values to the following:

   [![Set Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95f6e991-af7b-46bb-bf4e-e521f3a2fab2/ue5_11-set-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95f6e991-af7b-46bb-bf4e-e521f3a2fab2/ue5_11-set-color.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Red** | 1.0 |
   | **Green** | 1.0 |
   | **Blue** | 1.0 |
   |  |  |
4. Under **Sprite Attributes**, expand **Sprite Size**. Change the **Minimum** and **Maximum** values to the following:

   [![Set Sprite Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d09c71f-2761-4b0f-ba5d-ee401d180f2b/ue5_12-set-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d09c71f-2761-4b0f-ba5d-ee401d180f2b/ue5_12-set-sprite-size.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Minimum** | 100 |
   | **Maximum** | 200 |
   |  |  |
5. Open the **Add Velocity** module. Change the Velocity **Minimum** and **Maximum** values to the following:

   [![Set Velocity Minimum and Maximum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61c93a42-3534-4a52-bd20-e0afbdaffc69/ue5_13-set-velocity-minimum-and-maximum.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61c93a42-3534-4a52-bd20-e0afbdaffc69/ue5_13-set-velocity-minimum-and-maximum.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Minimum** | X: 16, Y: -5.0, Z: 35 |
   | **Maximum** | X: 32, Y: 5.0, Z: 50 |
   |  |  |
6. Open the **Sphere Location** module. Change the **Sphere Radius** value to **20**.

   [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49125bf5-7c1f-40d7-8c2e-28dd02bdbd1b/ue5_14-set-sphere-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49125bf5-7c1f-40d7-8c2e-28dd02bdbd1b/ue5_14-set-sphere-radius.png)

   Click image for full size.

## Edit the Particle Update Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Open Particle Update](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5793dd31-421f-44ce-b454-b970c31e01fc/ue5_15-open-particle-update.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5793dd31-421f-44ce-b454-b970c31e01fc/ue5_15-open-particle-update.png)

   Click image for full size.
2. Open the **Acceleration Force** module. Set the Acceleration **Minimum** and **Maximum** values to the following:

   [![Set Acceleration Minimum and Maximum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6de09a81-658a-499a-8eea-f2160d4a222c/ue5_16-set-acceleration-minimum-and-maximum.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6de09a81-658a-499a-8eea-f2160d4a222c/ue5_16-set-acceleration-minimum-and-maximum.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Minimum** | X: 25, Y: -10.0, Z: 15 |
   | **Maximum** | X: 55, Y: 10.0, Z: 25 |
   |  |  |
3. Open the **Scale Color** module. Click on the **Pulse Out** curve template to apply that shape to the curve.

   [![Curve Templates](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d98873c4-9562-4a1f-bef1-6abd0756c96c/ue5_17-curve-templates.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d98873c4-9562-4a1f-bef1-6abd0756c96c/ue5_17-curve-templates.png)

   Click image for full size.
4. Just click on the template that matches that curve.

   [![Curve Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10e49670-4035-4500-8ea6-63d5c3cd0b38/ue5_18-curve-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10e49670-4035-4500-8ea6-63d5c3cd0b38/ue5_18-curve-settings.png)

   Click image for full size.
5. Click the **Plus sign** icon (**+**) in the **Particle Update** group, and select **Forces > Drag** to add the **Drag** module.

   [![Add Drag Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ca2d284-52b0-4b28-a8f2-b755abb266b4/ue5_19-add-drag-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ca2d284-52b0-4b28-a8f2-b755abb266b4/ue5_19-add-drag-module.png)

   Click image for full size.
6. Because Niagara adds new modules to the bottom of the group's stack, you will get an error stating "The module has unmet dependencies." That is because the Drag module was placed after the **Solve Forces and Velocity** module. Click the **Fix Issue** button to move the module and resolve the error.

   [![Position Error Click Fix Issue](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5566ae3-f071-42c7-b2d1-37398c46156d/ue5_20-position-error-click-fix-issue.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5566ae3-f071-42c7-b2d1-37398c46156d/ue5_20-position-error-click-fix-issue.png)

   Click image for full size.
7. Set the **Drag** to **.8**.

   [![Set Drag](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c21b23f-638c-4ed9-aa1f-c7a09b11b109/ue5_21-set-drag.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c21b23f-638c-4ed9-aa1f-c7a09b11b109/ue5_21-set-drag.png)

   Click image for full size.

## End Result

After following these steps, the Steam system in your level will produce a steam effect similar to the one in the image below.

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create the Steam Emitter and System](/documentation/en-us/unreal-engine/how-to-create-a-steam-effect-in-niagara-for-unreal-engine?application_version=5.7#createthesteamemitterandsystem)
* [Edit the Emitter Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-steam-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheemitterupdatesettings)
* [Edit the Particle Spawn Settings](/documentation/en-us/unreal-engine/how-to-create-a-steam-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticlespawnsettings)
* [Edit the Particle Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-steam-effect-in-niagara-for-unreal-engine?application_version=5.7#edittheparticleupdatesettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-steam-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
