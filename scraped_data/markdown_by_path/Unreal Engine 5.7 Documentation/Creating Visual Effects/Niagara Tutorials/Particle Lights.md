<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7 -->

# Particle Lights

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
7. Particle Lights

# Particle Lights

How to create particles that emit light in your Niagara system.

![Particle Lights](https://dev.epicgames.com/community/api/documentation/image/68092798-b339-4586-aa0e-a3af3d6d10d2?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

 On this page

When you give particles the ability to illuminate the world around them, it can add an extra layer of realism to any of your project's visual effects. In the following tutorial, we will take a look at setting up a Niagara emitter so that particles and lights are spawned at the same time. The final result of this tutorial will look like the following.

![Particle Lights Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3decd016-6167-4dfd-9b4f-e04ab3458a41/particle-lights-final.gif)


**Prerequisite step**: This tutorial uses the **M\_Radial\_Gradient** Material, which is found with the **Starter Content**. You should create a new project that includes the Starter Content, or use a project that was created with Starter Content included.

## Create the System and Emitter

Niagara emitters and systems are independent. The current recommended workflow is to create a system from existing emitters or emitter templates.

1. First, create a Niagara System by right-clicking in the Content Browser, and from the displayed menu select **FX > Niagara System**. The Niagara Emitter wizard displays.

   [![Create Niagara System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bad8496-bc86-48fa-a551-0b564d720e85/01-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bad8496-bc86-48fa-a551-0b564d720e85/01-create-niagara-system.png)

   Click image for full size.
2. Select **New system from selected emitters**, then click **Next**.

   [![New System from Selected Emitters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d6eb12c-5743-436d-a5a0-c655cc5603ee/02-new-system-from-selected-emitters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d6eb12c-5743-436d-a5a0-c655cc5603ee/02-new-system-from-selected-emitters.png)

   Click image for full size.
3. Under **Templates**, select **Fountain**.

   [![Select Fountain Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7abf58dc-1d99-4b70-a662-3789a6fb1b2c/03-select-fountain-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7abf58dc-1d99-4b70-a662-3789a6fb1b2c/03-select-fountain-template.png)

   Click image for full size.
4. Click the **Plus sign** (**+**) icon to add the emitter to the list of emitters to add to the system, then click **Finish**.

   [![Add Emitter and Click Finish](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb390d56-92c5-4fb4-a569-884f45d64c6f/04-create-system-with-fountain.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb390d56-92c5-4fb4-a569-884f45d64c6f/04-create-system-with-fountain.png)

   Click image for full size.
5. Name the new system **ParticleLights**. Double-click to open it in the Niagara Editor.

   ![Name System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b54fc0e2-057b-4704-9b4f-4caf960796c7/05-rename-niagara-system.png "Name System")
6. The emitter instance in your new system has the default name of **Fountain**. You can rename it, however. Click the name of the emitter instance in the **System Overview**, and the field will become editable. Name the emitter **FX\_ParticleLight**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf0005c8-0b60-4c0b-b63d-a6350468b6f8/06-rename-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf0005c8-0b60-4c0b-b63d-a6350468b6f8/06-rename-emitter.png)

   Click image for full size.
7. Drag your **ParticleLight** system into your Level.

When you make a particle effect, it is always a good idea to drag your system into a Level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your level.

## Edit the Emitter Update Group Settings

First, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Open Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13ace9ff-189b-4a3e-8828-9fe7f724360b/07-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13ace9ff-189b-4a3e-8828-9fe7f724360b/07-select-emitter-update-group.png)

   Click image for full size.
2. Expand the **Emitter State** module. Because you used the Fountain template, the Life Cycle Mode is set to Self. Click the dropdown and set the Life Cycle Mode to System. This enables your system to calculate the lifecycle settings, which usually optimizes performance.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4aa0d00c-b97c-4504-b8b6-180840e7dbce/08-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4aa0d00c-b97c-4504-b8b6-180840e7dbce/08-life-cycle-mode.png)

   Click image for full size.
3. The **Spawn Rate** module creates a continuous stream of particles while the emitter is active. This module is already present in the Fountain template. Set the **Spawn Rate** to **500**.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38b5b181-ec80-476e-9551-3b96ecb1b8a0/09-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38b5b181-ec80-476e-9551-3b96ecb1b8a0/09-set-spawn-rate.png)

   Click image for full size.

## Edit the Particle Spawn Group Settings

Next, you will edit the modules in the Particle Spawn group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Open Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48efebd5-2272-4a77-ba85-dac4b50638f2/10-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48efebd5-2272-4a77-ba85-dac4b50638f2/10-select-particle-spawn-group.png)

   Click image for full size.
2. Expand the **Initialize Particle** module. This module collects several related parameters together in one module, minimizing clutter in your stack. Under **Point Attributes**, locate the **Lifetime Mode** dropdown and set to **Random**. This parameter determines how long particles will display before they disappear. For this effect, you will use a dynamic input called **Random Ranged Float** to randomize how long the particles display. Random Ranged Float is already applied to the Lifetime parameter in the Fountain template. Set the **Minimum** and **Maximum** values to the following.

   [![Set Lifetime Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0687c1a9-659d-4545-a87e-c23f93a6161d/11-set-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0687c1a9-659d-4545-a87e-c23f93a6161d/11-set-lifetime.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Lifetime Mode** | Random |
   | **Minimum** | 1.75 |
   | **Maximum** | 2.5 |
3. Also under **Point Attributes**, locate the **Color** parameter. This sets the initial color of the particles when they spawn. Set the **RGB** fields to the following values.

   The Unreal Engine Color Picker normalizes RGB color values to an integer between 0 and 1. However if you set a color value greater than 1, it becomes emissive color. The particles will glow that color when the system is placed in the Level.

   [![Set Color Parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af8155b8-4e35-473c-9966-c165519b34b0/12-set-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af8155b8-4e35-473c-9966-c165519b34b0/12-set-color.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Red** | 0.1 |
   | **Green** | 0.3 |
   | **Blue** | 50 |
4. Under **Sprite Attributes**, locate the **Sprite Size** parameter. To add some randomness to the size of the fountain particles, adjust the Sprite Size Mode. Click on the dropdown menu and select Random Uniform. This adds **Minimum** and **Maximum** fields to the Value. Set the **Sprite Size** **Minimum** and **Maximum** values to the following.

   [![Set Sprite Size Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/124474ae-5615-49c2-bbec-4af70bff83ed/13-set-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/124474ae-5615-49c2-bbec-4af70bff83ed/13-set-size.png)

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Sprite Size Mode** | Random Uniform |
   | **Minimum** | 2.5 |
   | **Maximum** | 8.0 |
5. **Sphere location** controls the shape and origin of where sprites spawn. You can set the size of the sphere shape by indicating a radius. The **Sphere Location** module is included in the Fountain template. Set the **Sphere Radius** to **15**.

   [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d5ef21c-4117-4d73-bd04-6bf9ce7a979c/14-set-sphere-location-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d5ef21c-4117-4d73-bd04-6bf9ce7a979c/14-set-sphere-location-radius.png)

   Click image for full size.
6. The Fountain template also contains the **Add Velocity in Cone** module. This adds movement to the particles when they spawn. The point of the cone is at the particle spawn point, and you can set **X**, **Y**, and **Z** values to determine in which direction the cone expands. The **Velocity Strength** has a dynamic input called **Random Ranged Float** applied. Set the **Minimum** and **Maximum** values to the following. Leave the other settings at their default values.

   [![Add Velocity in Cone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/777443bf-d23f-4873-ab8f-a11fdf9abc26/15-set-velocity-in-cone-min-and-max.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/777443bf-d23f-4873-ab8f-a11fdf9abc26/15-set-velocity-in-cone-min-and-max.png)



      

   Click image for full size.

   | Setting | Value |
   | --- | --- |
   | **Minimum** | 300 |
   | **Maximum** | 600 |

## Edit the Particle Update Group Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Open Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5481eb85-1cda-49e5-9263-2ed9a1938368/16-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5481eb85-1cda-49e5-9263-2ed9a1938368/16-select-particle-update-group.png)

   Click image for full size.
2. The **Gravity Force** module simulates how gravity affects objects. The **Drag** module applies drag to the particles, which slows them down. The default settings for Gravity Force and Drag work for this effect, so you can leave them that way.
3. Without setting up collision, the particles in your effect will just fall through the floor or any other solid objects in the level. To add a **Collision** module, click the **Plus sign** (**+**) icon for **Particle Update** and select **Collision > Collision**.

   [![Add Collision Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b6e45bd-d543-4f7a-930e-f49a636f6838/17-add-collision-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b6e45bd-d543-4f7a-930e-f49a636f6838/17-add-collision-module.png)

   Click image for full size.
4. The **Collision** module is inserted at the bottom of the stack, after the **Solve Forces and Velocity** module. This causes an error. Click **Fix Issue** to move the Collision module and resolve the error.

   [![Fix Collision Module Error](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/335ab824-ac1b-4b30-b13d-ce96386d4c05/18-fix-issue.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/335ab824-ac1b-4b30-b13d-ce96386d4c05/18-fix-issue.png)

   Click image for full size.
5. Leave the default settings for the **Collision** module in place.

## Add the Light Renderer

Now you will add the Light Renderer to the fountain effect.

1. In the **System Overview**, click the **Render** group to open it in the **Selection** panel.

   [![Open Render Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb3a1794-a0ce-4ab0-951e-0b4d3215fb8a/19-select-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb3a1794-a0ce-4ab0-951e-0b4d3215fb8a/19-select-render-group.png)

   Click image for full size.
2. Click the **Plus sign** (**+**) icon for **Render**, and select **Light Renderer**.

   [![Add Light Renderer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8d4b897-6833-4a64-b4e9-3da0bf9bda4c/20-add-light-renderer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8d4b897-6833-4a64-b4e9-3da0bf9bda4c/20-add-light-renderer.png)

   Click image for full size.
3. Set the **Radius Scale** to **5.0**. This determines how far from the particle spawn point the light spreads.

   [![Light Renderer Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2089a04-c609-4f04-96ec-4f02a5c5c26b/21-set-light-renderer-values.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2089a04-c609-4f04-96ec-4f02a5c5c26b/21-set-light-renderer-values.png)

   Click image for full size.
4. The **Color Add** values enable you to change the color of the light emitted by the effect. These values are labeled with **X**, **Y**, and **Z**; however they correspond to RGB values, with **X=Red**, **Y=Green**, and **Z=Blue**. To match the light color with the particle color, set the values to the following.

   | Setting | Value |
   | --- | --- |
   | **Red** | 0 |
   | **Green** | 0 |
   | **Blue** | 15 |

## End Result

Congratulations! You have created an effect that includes a particle light, and that emits light in your scene.

![Particle Lights Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c359195-4e0b-44f8-9898-bd354bb2462b/particle-lights-final.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create the System and Emitter](/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7#createthesystemandemitter)
* [Edit the Emitter Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7#edittheemitterupdategroupsettings)
* [Edit the Particle Spawn Group Settings](/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7#edittheparticlespawngroupsettings)
* [Edit the Particle Update Group Settings](/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7#edittheparticleupdategroupsettings)
* [Add the Light Renderer](/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7#addthelightrenderer)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-particle-effects-that-emit-light-in-niagara-for-unreal-engine?application_version=5.7#endresult)
