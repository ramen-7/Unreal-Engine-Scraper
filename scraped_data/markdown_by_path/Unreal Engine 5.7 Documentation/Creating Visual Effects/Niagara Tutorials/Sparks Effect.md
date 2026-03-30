<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7 -->

# Sparks Effect

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
7. Sparks Effect

# Sparks Effect

This tutorial shows how to create a sparks effect using Niagara. It shows how to use more than one emitter in a Niagara system.

![Sparks Effect](https://dev.epicgames.com/community/api/documentation/image/5687233e-ac0e-492a-bc60-23cb2dcd52b3?resizing_type=fill&width=1920&height=335)

 On this page

**Prerequisite Steps:**

This tutorial uses the **M\_smoke\_subUV**, **M\_Spark**, and **M\_Radial\_Gradient** materials, which can be found with the Starter Content. If you have not done so already, make sure that your project includes the Starter Content. This tutorial also uses the FX\_Smoke emitter created in the how-to [Create a Sprite Particle Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine).

To create the Sparks effect included in the Starter Content, you will need to make three Niagara emitters: one for the fountain of sparks, one for the spark at the center, and one for the small stream of smoke rising from the fountain of sparks.

The final effect will look like the following.

![Sparks Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97c48336-0fda-427a-b0cb-500f32cdd9a7/sparks-final.gif)

You will start with the smoke emitter, because you can create it using a copy of an existing emitter.

## Create the Smoke Emitter and the Sparks System

Niagara emitters and systems are independent. The current recommended workflow is to create a system from existing emitters or emitter templates.

1. Create a new folder for this tutorial in the Content folder for your project.
2. Make a copy of the **FX\_Smoke** emitter you created in [Create a Sprite Particle Effect in Niagara](/documentation/en-us/unreal-engine/how-to-create-a-smoke-effect-using-sprite-particles-in-niagara-for-unreal-engine).

   [![Duplicate the Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e461d3c-2c60-4eed-a9e5-47ba8f42a3da/01-duplicate-smoke-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e461d3c-2c60-4eed-a9e5-47ba8f42a3da/01-duplicate-smoke-emitter.png)

   Click image for full size.
3. Drag this duplicate emitter to the folder you created in step 1. In the popup context menu, select **Move**.
4. Rename the copied emitter **FX\_Sparks\_Smoke**.

   ![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e3c38527-23ab-40a7-9b90-638363cfb35c/02-rename-smoke-emitter.png)
5. Now create a system for your spark effect. Right-click on your new smoke emitter, and select **Create Niagara System**.

   [![Create the Niagara System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61f2af6b-cd64-4ff8-aecf-eac85ececfa7/03-create-niagara-system.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61f2af6b-cd64-4ff8-aecf-eac85ececfa7/03-create-niagara-system.png)

   Click image for full size.

   There are multiple ways to create new Niagara systems. Because you are starting with an emitter you have already created, the method used here quickly creates a system containing that emitter. However, as you saw in the Create a Sprite Particle Effect tutorial, there are emitter and system wizards that give you many other options for creating and setting up a Niagara system.
6. Name the system **SparksSystem**.

   ![Name System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/156d8a14-5d21-4494-8f7e-4512994a569e/04-rename-system.png "Name System")
7. Open your Level in the Level Editor, if it isn't open already. Drag the **SparksSystem** tile from the **Content Drawer** into your Level.

   When you make a particle effect, it is always a good idea to drag your system into your level. This gives you a chance to see every change and edit in context. Any changes you make to the system automatically propagate to the instance of the system in your level.

   [![Drag System Into Your Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d264fa8b-b921-47b8-abaf-781aeb085203/05-drag-system-into-scene.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d264fa8b-b921-47b8-abaf-781aeb085203/05-drag-system-into-scene.png)

   Click image for full size.

### Smoke Emitter - Edit the Emitter Update Settings

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Select Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b10cd59-f93e-47ed-a1b3-fb1de4663fe8/06-smoke-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b10cd59-f93e-47ed-a1b3-fb1de4663fe8/06-smoke-select-emitter-update-group.png)

   Click image for full size.
2. Open the **Emitter State** module. This module controls time and scalability for this emitter. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe7ea462-27ca-4d19-b728-da85ccc43645/07-smoke-set-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe7ea462-27ca-4d19-b728-da85ccc43645/07-smoke-set-life-cycle-mode.png)

   Click image for full size.
3. Open the **Spawn Rate** module. Change the **Spawn Rate** setting to **20**.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c4bab32d-038a-435c-9b23-1162d121b174/08-smoke-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c4bab32d-038a-435c-9b23-1162d121b174/08-smoke-set-spawn-rate.png)

   Click image for full size.

### Smoke Emitter - Edit the Particle Spawn Settings

Next, you will edit the modules in the Particle Spawn group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Select Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/809d227a-459c-4c32-a888-4115423dedac/09-smoke-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/809d227a-459c-4c32-a888-4115423dedac/09-smoke-select-particle-spawn-group.png)

   Click image for full size.
2. Open the **Initialize Particle** module. Under **Point Attributes**, expand **Lifetime**. Change the **Minimum** and **Maximum** values to the following.

   [![Set Particle Lifetime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec39ad01-bf2e-424f-8b02-31cf1f72f94b/10-smoke-set-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec39ad01-bf2e-424f-8b02-31cf1f72f94b/10-smoke-set-lifetime.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Lifetime Mode** | Random |
   | **Minimum** | 2.0 |
   | **Maximum** | 3.0 |
3. Locate the **Color** parameter. Change the **RGB** values to the following.

   [![Set Particle Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ba91a18-68a4-4ca3-b4d1-539f5ee97a20/11-smoke-set-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ba91a18-68a4-4ca3-b4d1-539f5ee97a20/11-smoke-set-color.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Red** | 0.3 |
   | **Green** | 0.3 |
   | **Blue** | 0.3 |
4. Under **Sprite Attributes**, expand **Sprite Size**. Set the Sprite Size Mode to **Non-Uniform**. Set the **Minimum** and **Maximum** values to the following.

   [![Set Sprite Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b5acf41-6e02-4432-9ff1-5213942a9d20/12-smoke-set-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b5acf41-6e02-4432-9ff1-5213942a9d20/12-smoke-set-sprite-size.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Sprite Size Mode** | Random Uniform |
   | **Minimum** | 20.0 |
   | **Maximum** | 40.0 |
5. Open the **Add Velocity** module. Change the Velocity **Minimum** and **Maximum** values to the following.

   [![Set Velocity Minimum and Maximum](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df6a4a76-75f8-4c6e-b768-11728f4dbbf3/13-smoke-set-velocity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df6a4a76-75f8-4c6e-b768-11728f4dbbf3/13-smoke-set-velocity.png)

   Click image for full size.

   | Velocity | Minimum | Maximum |
   | --- | --- | --- |
   | **X** | 0.0 | 1.0 |
   | **Y** | 0.0 | 1.0 |
   | **Z** | 25.0 | 35.0 |
6. Open the **Shape Location** module. Change the **Sphere Radius** value to **5**.

   [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c4596d31-43dd-44f4-a553-bf287b34c793/14-smoke-set-shape-location-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c4596d31-43dd-44f4-a553-bf287b34c793/14-smoke-set-shape-location-radius.png)

   Click image for full size.

### Smoke Emitter - Edit the Particle Update Settings

Now you will edit the modules in the Particle Update group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Select Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7ee05b8-2549-4989-ba97-089b1faef8e2/15-smoke-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7ee05b8-2549-4989-ba97-089b1faef8e2/15-smoke-select-particle-update-group.png)

   Click image for full size.
2. Open the **Scale Color** module. Click to deselect the box next to **Scale RGB**. Above the curve for **Scale Alpha**, click the **Smooth Ramp Down** template to apply that shape to the curve.

   [![Set Scale Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9272dbd9-7bbd-4ed8-92ed-00e0657986d2/16-smoke-set-scale-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9272dbd9-7bbd-4ed8-92ed-00e0657986d2/16-smoke-set-scale-color.png)

   Click image for full size.
3. Open the **Acceleration Force** module. Set the **Acceleration** values to **X: 0, Y: 0, Z: 20**.

   [![Set Acceleration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0879005-0a93-4e4a-8f86-fb6ed451ddc7/17-smoke-set-acceleration.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0879005-0a93-4e4a-8f86-fb6ed451ddc7/17-smoke-set-acceleration.png)

   Click image for full size.

At this stage in the process, you have finished configuring the first emitter in the system. It should look similar to the following.

![Sparks Effect First Emitter Configured](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/67c1748f-aefe-452a-81e0-b71823715883/sparks-stage-1.gif)

## Add the Spark Burst Emitter to the System

Next, you will create the spark burst at the center of the effect.

1. Right-click in the **System Overview** of your SparkFountain system. Click **Add Emitter**, and a list of existing emitters will display. From the list of emitters, select the **Simple Sprite Burst** template.

   [![Add Emitter from System Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1ffbb75-0ee9-4955-bbae-fcd50782535d/18-add-sparks-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1ffbb75-0ee9-4955-bbae-fcd50782535d/18-add-sparks-emitter.png)

   Click image for full size.
2. The default name for the template emitter is **SimpleSpriteBurst**, but you can rename it. Click on the emitter name, and the field becomes editable. Name the new emitter **FX\_SparkBurst**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7e61cec-9eb3-4d45-80ad-5699a9b53f69/19-rename-sparks-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7e61cec-9eb3-4d45-80ad-5699a9b53f69/19-rename-sparks-emitter.png)

   Click image for full size.

### Spark Burst Emitter - Edit Render Settings

The **Render** group is last in the stack, but you need to change the material so that the effect displays the way it is supposed to.

1. In the **System Overview**, click the **Render** group to open it in the **Selection** pane.

   [![Select Render Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e7b19ef-706b-4065-9bbb-bc382a4f9a09/20-sparks-select-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e7b19ef-706b-4065-9bbb-bc382a4f9a09/20-sparks-select-render-group.png)

   Click image for full size.
2. Under **Sprite Renderer**, click the dropdown for **Material**, and select the **M\_Spark** material from the Starter Content.

   [![Select Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4c4ae4c-69f1-478a-a765-1051a57efd8c/21-sparks-set-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4c4ae4c-69f1-478a-a765-1051a57efd8c/21-sparks-set-material.png)

   Click image for full size.

### Spark Burst Emitter - Edit the Emitter Update Settings

First, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Select Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8e606d6-8464-4e5c-97d3-86619af2cddd/22-sparks-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8e606d6-8464-4e5c-97d3-86619af2cddd/22-sparks-select-emitter-update-group.png)

   Click image for full size.
2. Remove the **Sprite Burst Instantaneous** module by clicking the **Trashcan** icon.

   [![Remove Sprite Burst Instantaneous](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a84186f4-8f8b-45e8-a200-26bee864943b/23-sparks-delete-spawn-burst.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a84186f4-8f8b-45e8-a200-26bee864943b/23-sparks-delete-spawn-burst.png)

   Click image for full size.
3. Open the **Emitter State** module. This module controls time and scalability for this emitter. Because you used the Simple Sprite Burst template, the **Life Cycle Mode** is set to Self. Normally this is used for complete customization of emitter life cycle logic for this specific emitter, but it is not needed for this effect. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fcf09d1-971a-40b9-a090-7b9954b3be08/24-sparks-set-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fcf09d1-971a-40b9-a090-7b9954b3be08/24-sparks-set-life-cycle-mode.png)

   Click image for full size.
4. Click the **Plus sign** (**+**) for Emitter Update, and select **Spawning > Spawn Rate**.

   [![Add Spawn Rate Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc7c1341-22db-4ec2-9ce1-ef11e2d5856c/25-sparks-add-spawn-rate-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc7c1341-22db-4ec2-9ce1-ef11e2d5856c/25-sparks-add-spawn-rate-module.png)

   Click image for full size.
5. Open the **Spawn Rate** module. Set the **Spawn Rate** to **50**.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9e52244-6634-41d3-a251-4de7d21c7bc4/26-sparks-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9e52244-6634-41d3-a251-4de7d21c7bc4/26-sparks-set-spawn-rate.png)

   Click image for full size.

### Spark Burst Emitter - Edit the Particle Spawn Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Select Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0ca2155-c228-4337-88a9-6857176295cb/27-sparks-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0ca2155-c228-4337-88a9-6857176295cb/27-sparks-select-particle-spawn-group.png)

   Click image for full size.
2. Under **Point Attributes**, set the **Lifetime** to **.2**.

   [![Set Particle Lifetime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d2ae503-9ee4-4d3b-bb1e-f8a95aa29d9b/28-sparks-set-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d2ae503-9ee4-4d3b-bb1e-f8a95aa29d9b/28-sparks-set-lifetime.png)

   Click image for full size.
3. Set the **Mass Mode** to **Random** and the **Minimum** and **Maximum** values to the following:

   [![Set Mass Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f9bfff6-a91f-480a-b260-f36072734e5d/29-sparks-set-mass.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f9bfff6-a91f-480a-b260-f36072734e5d/29-sparks-set-mass.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Mass Mode** | Random |
   | **Minimum** | 0.6 |
   | **Maximum** | 1.0 |
4. Under **Sprite Attributes**, expand **Sprite Size**. Set the **Sprite Size Mode** to **Random Non-Uniform**. Set the Sprite Size **Minimum** and **Maximum** values to the following:

   [![Set Sprite Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/349e7bf2-4bd8-4a24-88cd-ee8a531f91c9/30-sparks-set-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/349e7bf2-4bd8-4a24-88cd-ee8a531f91c9/30-sparks-set-sprite-size.png)

   Click image for full size.

   | Sprite Size | Minimum | Maximum |
   | --- | --- | --- |
   | **X** | 10.0 | 30.0 |
   | **Y** | 10.0 | 25.0 |
5. Click the box next to **Sprite Rotation** to enable it. Set the **Sprite Rotation Mode** to **Direct Angle (Degrees)**. Click the dropdown next to the Value field, and select **Dynamic Inputs > Random Range Float**.

   [![Set Rotation to Random Range Float](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d95d99d0-95e2-489c-9fed-143db326511d/31-sparks-sprite-rotation-random-range-float.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d95d99d0-95e2-489c-9fed-143db326511d/31-sparks-sprite-rotation-random-range-float.png)

   Click image for full size.
6. Set the **Minimum** and **Maximum** to the following:

   [![Set Sprite Size Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c742d83c-f3ee-4da4-8ffd-fcd0f738d2bf/32-sparks-set-sprite-rotation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c742d83c-f3ee-4da4-8ffd-fcd0f738d2bf/32-sparks-set-sprite-rotation.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Minimum** | -10.0 |
   | **Maximum** | 30.0 |
7. Click the **Plus sign** (**+**) for Particle Spawn, and select **Velocity > Add Velocity**.

   [![Add the Add Velocity Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec6a2b7a-895c-4d5c-bb79-f0562836c87a/33-sparks-add-velocity-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec6a2b7a-895c-4d5c-bb79-f0562836c87a/33-sparks-add-velocity-module.png)

   Click image for full size.
8. Open the **Add Velocity** module. Click the dropdown next to the value, and select **Dynamic Inputs > Random Range Vector**.

   [![Set Velocity to Random Ranged Vector](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b3274ff9-a6a5-4b14-ac3d-894596378298/34-sparks-velocity-random-range-vector.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b3274ff9-a6a5-4b14-ac3d-894596378298/34-sparks-velocity-random-range-vector.png)

   Click image for full size.
9. Set the Velocity **Minimum** and **Maximum** to the following:

   [![Set Velocity Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9d73016-9e67-4cf3-add1-9070c157911b/35-sparks-set-velocity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9d73016-9e67-4cf3-add1-9070c157911b/35-sparks-set-velocity.png)

   Click image for full size.

   | Velocity | Minimum | Maximum |
   | --- | --- | --- |
   | **X** | 0.0 | 5.0 |
   | **Y** | 0.0 | 5.0 |
   | **Z** | 0.0 | 5.0 |
10. Click the **Plus sign** (**+**) for Particle Spawn, and select **Location > Shape Location**.

    [![Add Shape Location Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3e4c283-757c-468b-991d-06113262ff44/36-sparks-add-shape-location-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3e4c283-757c-468b-991d-06113262ff44/36-sparks-add-shape-location-module.png)

    Click image for full size.
11. Open the **Shape Location** module. Set the **Sphere Radius** to **5**.

    [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13e55554-0b8f-467c-9c2e-9ffa7f680843/37-sparks-set-shape-location-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13e55554-0b8f-467c-9c2e-9ffa7f680843/37-sparks-set-shape-location-radius.png)

    Click image for full size.

### Spark Burst Emitter - Edit the Particle Update Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Select Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/539249fc-04d8-42a2-b4be-bbf31863bcee/38-sparks-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/539249fc-04d8-42a2-b4be-bbf31863bcee/38-sparks-select-particle-update-group.png)

   Click image for full size.
2. Open the **Scale Color** module. For **Scale RGB**, set the **RGB** values to the following. Under **Scale Alpha**, select the **Smooth Ramp Down** template.

   [![Set Scale Color RGB and Alpha](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49580cc4-91fe-4309-a946-d150a6cee493/39-sparks-set-scale-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49580cc4-91fe-4309-a946-d150a6cee493/39-sparks-set-scale-color.png)

   Click image for full size.

   | Color | Value |
   | --- | --- |
   | **R** | 2.0 |
   | **G** | 6.0 |
   | **B** | 25.0 |
3. Click the **Plus sign** icon (**+**) for **Particle Update**, and select **Size > Scale Sprite Size**. You can also type `scale` in the search bar, as shown below.

   [![Add Scale Sprite Size Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7019a12-c6c7-4088-9bee-c09bfaa01942/40-sparks-add-scale-sprite-size-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7019a12-c6c7-4088-9bee-c09bfaa01942/40-sparks-add-scale-sprite-size-module.png)

   Click image for full size.
4. Open the **Scale Sprite Size** module. Click the dropdown next to the **Scale Factor** value field, and select **Dynamic Inputs > Random Range Vector 2D**. You can also type `random` in the search bar.

   [![Set Sprite Size to Random Range Vector 2D](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c0cd104-8c91-4ac9-9a73-56b40b26ec1e/41-sparks-scale-sprite-size-random-range-vector.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c0cd104-8c91-4ac9-9a73-56b40b26ec1e/41-sparks-scale-sprite-size-random-range-vector.png)

   Click image for full size.
5. Set the Scale Factor **Minimum** and **Maximum** to the following:

   [![Set Scale Factor Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfa6dc9d-2a21-449e-b452-aa9bc0425709/42-sparks-set-scale-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfa6dc9d-2a21-449e-b452-aa9bc0425709/42-sparks-set-scale-sprite-size.png)

   Click image for full size.

   | Scale | Minimum | Maximum |
   | --- | --- | --- |
   | **X** | 1.0 | 3.5 |
   | **Y** | 2.5 | 5.0 |

At this stage in the process, you have finished configuring the second emitter in the system. It should look similar to the following.

![Sparks Effect Second Emitter Configured](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c155889-beba-4138-b283-d21a2b3974c9/sparks-stage-2.gif)

## Add the Radial Sparks Emitter to the System

1. Right-click in the **System Overview** of your SparkFountain system. Click **Add Emitter**, and a list of existing emitters will display. From the list of emitters, select the **Simple Sprite Burst** template.

   [![Add Emitter from System Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e41cd9dd-5ada-4caf-b9cb-bdd9b14dc508/43-add-radial-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e41cd9dd-5ada-4caf-b9cb-bdd9b14dc508/43-add-radial-emitter.png)

   Click image for full size.
2. The default name for the template emitter is **SimpleSpriteBurst**, but you can rename it. Click on the emitter name, and the field becomes editable. Name the new emitter **FX\_Sparks\_Radial**.

   [![Rename Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad972b57-19f4-476d-abd1-103607a6fd1f/44-rename-radial-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad972b57-19f4-476d-abd1-103607a6fd1f/44-rename-radial-emitter.png)

   Click image for full size.

### Radial Sparks Emitter - Edit Render Settings

The **Render** group is last in the stack, but you need to change the material so that the effect displays the way it is supposed to.

1. In the **System Overview**, click the **Render** group to open it in the **Selection** panel.

   [![Select Render Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bc4de3b-991d-4e5b-b2fe-69ca0f88250a/45-radial-select-render-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bc4de3b-991d-4e5b-b2fe-69ca0f88250a/45-radial-select-render-group.png)

   Click image for full size.
2. Click the dropdown for **Material**, and select the **M\_Radial\_Gradient** material from the Starter Content. To locate it, type `radial` in the search bar, as shown below.

   [![Select Render Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fab11e6a-3c9d-4b0d-b507-c91c97c21695/46-radial-set-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fab11e6a-3c9d-4b0d-b507-c91c97c21695/46-radial-set-material.png)

   Click image for full size.
3. Click the dropdown for **Alignment** and select **Velocity Aligned**.

   [![Set Alignment](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44f476ac-9ddb-4ff3-973a-0e21905611a5/47-radial-sprite-alignment.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44f476ac-9ddb-4ff3-973a-0e21905611a5/47-radial-sprite-alignment.png)

   Click image for full size.

### Radial Sparks Emitter - Edit the Emitter Update Settings

First, you will edit the modules in the **Emitter Update** group. These are behaviors that apply to the emitter, and that update each frame.

1. In the **System Overview**, click the **Emitter Update** group to open it in the **Selection** panel.

   [![Select Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4efe6914-ea06-4c39-847a-e990510d25cb/48-radial-select-emitter-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4efe6914-ea06-4c39-847a-e990510d25cb/48-radial-select-emitter-update-group.png)

   Click image for full size.
2. Remove the **Sprite Burst Instantaneous** module by clicking the **Trashcan** icon.

   [![Remove Sprite Burst Instantaneous](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c21da49-7678-494c-b975-872f6410e9b7/49-radial-delete-spawn-burst.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c21da49-7678-494c-b975-872f6410e9b7/49-radial-delete-spawn-burst.png)

   Click image for full size.
3. Open the **Emitter State** module. This module controls time and scalability for this emitter. Because you used the **Simple Sprite Burst** template, the **Life Cycle Mode** is set to **Self**. Normally this is used for complete customization of emitter life cycle logic for this specific emitter, but it is not needed for this effect. Click the dropdown and set the **Life Cycle Mode** to **System**. This enables your system to calculate life cycle settings, which usually optimizes performance. By default, the system loops infinitely on a 5 second interval.

   [![Set Life Cycle Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/295cf14e-ede2-45d6-bfcf-aa0d8b37d297/50-radial-set-life-cycle-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/295cf14e-ede2-45d6-bfcf-aa0d8b37d297/50-radial-set-life-cycle-mode.png)

   Click image for full size.
4. Click the **Plus sign** icon (**+**) for **Emitter Update**, and select **Spawning > Spawn Rate**.

   [![Add Spawn Rate Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6bb4f2f7-47af-4f31-8473-7d7c72b54eb4/51-radial-add-spawn-rate-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6bb4f2f7-47af-4f31-8473-7d7c72b54eb4/51-radial-add-spawn-rate-module.png)

   Click image for full size.
5. Open the **Spawn Rate** module. Set the **Spawn Rate** to **500**.

   [![Set Spawn Rate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/300ed4d4-de15-4344-a621-e5154f085864/52-radial-set-spawn-rate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/300ed4d4-de15-4344-a621-e5154f085864/52-radial-set-spawn-rate.png)

   Click image for full size.

### Radial Sparks Emitter - Edit Particle Spawn Settings

Next, you will edit the modules in the **Particle Spawn** group. These are behaviors that apply to particles when they first spawn.

1. In the **System Overview**, click the **Particle Spawn** group to open it in the **Selection** panel.

   [![Select Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13d1e4ca-a605-4228-b6ad-ea36bbe0d89d/53-radial-select-particle-spawn-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13d1e4ca-a605-4228-b6ad-ea36bbe0d89d/53-radial-select-particle-spawn-group.png)

   Click image for full size.
2. Open the **Initialize Particle** module. Under **Point Attributes**, expand **Lifetime**. Set the Lifetime Mode to **Random** and the **Minimum** and **Maximum** values to the following:

   [![Set Lifetime Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/388bda9c-c3c2-44c5-9aeb-290fcfc15a8e/54-radial-set-lifetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/388bda9c-c3c2-44c5-9aeb-290fcfc15a8e/54-radial-set-lifetime.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Lifetime Mode** | Random |
   | **Minimum** | 0.2 |
   | **Maximum** | 0.7 |
3. Expand **Color**. Set the **Color Mode** to **Direct Set** and the RGB values to the following:

   [![Set Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bcbe60af-c924-400b-aa70-31dae1def6b1/55-radial-set-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bcbe60af-c924-400b-aa70-31dae1def6b1/55-radial-set-color.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Red** | 2.0 |
   | **Green** | 8.0 |
   | **Blue** | 20.0 |
   | **Alpha** | 1.0 |
4. Expand **Mass**. Set the **Mass Mode** to **Random** and the **Minimum** and **Maximum** values to the following:

   [![Set Mass Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0aec183-9b32-48ee-a1c6-68e334d0c10b/56-radial-set-mass.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0aec183-9b32-48ee-a1c6-68e334d0c10b/56-radial-set-mass.png)

   Click image for full size.

   | Parameter | Value |
   | --- | --- |
   | **Mass Mode** | Random |
   | **Minimum** | 0.3 |
   | **Maximum** | 0.6 |
5. Under **Sprite Attributes**, set the **Sprite Size Mode** to **Non-Uniform**. Set the following values: **X: 0.25, Y: 0.5**.

   [![Set Sprite Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b80fa01-bebc-473f-aaf1-4f68a6c68c4c/57-radial-set-sprite-size.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b80fa01-bebc-473f-aaf1-4f68a6c68c4c/57-radial-set-sprite-size.png)

   Click image for full size.
6. Leave the **Sprite Rotation Mode** and **Sprite UV Mode** as **Unset**.
7. Click the **Plus sign** icon (**+**) for **Particle Spawn**, and select **Mass > Calculate Size and Rotational Inertia by Mass**. You can also type `calc` in the Search bar, as shown below.

   [![Add Calculate Size and Rotational Inertia by Mass](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c7548c9-c8ce-4322-8611-003f96abafe6/58-radial-add-calc-size-by-mass-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c7548c9-c8ce-4322-8611-003f96abafe6/58-radial-add-calc-size-by-mass-module.png)

   Click image for full size.
8. Open the **Calculate Size and Rotational Inertia by Mass** module. Under **Density**, set **Density by Material Type** to **Water**.

   [![Set Density](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/405e7db1-49da-460e-af94-de619a14e4b8/59-radial-set-density-to-water.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/405e7db1-49da-460e-af94-de619a14e4b8/59-radial-set-density-to-water.png)

   Click image for full size.
9. Under **Proportions**, change the **Height** to **0.5** and **Depth** to **0.0**.

   [![Set Proportions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc8bb2d1-b646-478e-a0f6-4bfb67703d37/60-radial-set-proportions.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc8bb2d1-b646-478e-a0f6-4bfb67703d37/60-radial-set-proportions.png)

   Click image for full size.
10. Click the **Plus sign** icon (**+**) for **Particle Spawn**, and select **Velocity > Add Velocity**. You can also type `velocity` in the Search bar.

    [![Add the Add Velocity Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb847883-c8e6-428b-8452-a6a40ce68a6a/61-radial-add-velocity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb847883-c8e6-428b-8452-a6a40ce68a6a/61-radial-add-velocity.png)

    Click image for full size.
11. Open the **Add Velocity** module. Click on the dropdown menu and select **Dynamic Inputs** then **Random Range Vector**.

    [![Set Velocity to Random Range Vector](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0bd81180-c6f2-47a7-9e89-49c064dede36/62-radial-velocity-random-range-vector.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0bd81180-c6f2-47a7-9e89-49c064dede36/62-radial-velocity-random-range-vector.png)

    Click image for full size.
12. Set the Velocity **Minimum** and **Maximum** to the following.

    [![Set Velocity Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72074736-4985-4614-98b7-0cd2520a66eb/63-radial-set-velocity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72074736-4985-4614-98b7-0cd2520a66eb/63-radial-set-velocity.png)

    Click image for full size.

    | Velocity | Minimum | Maximum |
    | --- | --- | --- |
    | **X** | -100.0 | 90.0 |
    | **Y** | -100.0 | 90.0 |
    | **Z** | 300.0 | 500.0 |
13. Click the **Plus sign** icon (**+**) for **Particle Spawn**, and select **Location > Shape Location**. You can also type `sphere` in the Search bar.

    [![Add Shape Location](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/536c4b92-65eb-44ae-b593-0d946eae4e96/64-radial-add-shape-location-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/536c4b92-65eb-44ae-b593-0d946eae4e96/64-radial-add-shape-location-module.png)

    Click image for full size.
14. Open the **Shape Location** module. Set the **Sphere Radius** to **2.0**.

    [![Set Sphere Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4cc2db1e-3040-4d32-b73a-244be188c398/65-radial-set-sphere-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4cc2db1e-3040-4d32-b73a-244be188c398/65-radial-set-sphere-radius.png)

    Click image for full size.

### Radial Sparks Emitter - Edit the Particle Update Settings

Now you will edit the modules in the **Particle Update** group. These behaviors apply to an emitter's particles and update each frame.

1. In the **System Overview**, click the **Particle Update** group to open it in the **Selection** panel.

   [![Select Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7f0e238-680c-4d6d-957a-14a934d22396/66-radial-select-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7f0e238-680c-4d6d-957a-14a934d22396/66-radial-select-particle-update-group.png)

   Click image for full size.
2. Click the **Plus sign** icon (+) for **Particle Update**, and select **Velocity > Scale Velocity**.

   [![Add Scale Velocity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4333b974-25ae-4339-aba4-5f64cc02794f/67-radial-add-scale-velocity-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4333b974-25ae-4339-aba4-5f64cc02794f/67-radial-add-scale-velocity-module.png)

   Click image for full size.
3. Set the **Scale Velocity** to **X: 3.0, Y: 4.0, Z: 1.0**.

   [![Set Scale Velocity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9887108-0bce-400d-88da-ebfb4d634457/68-radial-set-scale-velocity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9887108-0bce-400d-88da-ebfb4d634457/68-radial-set-scale-velocity.png)

   Click image for full size.
4. Click the **Plus sign** icon (**+**) for **Particle Update**, and select **Forces > Gravity Force**.

   [![Add Gravity Force Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bae32c53-d82d-4ae0-865e-30233c1f7354/69-radial-add-gravity-force-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bae32c53-d82d-4ae0-865e-30233c1f7354/69-radial-add-gravity-force-module.png)

   Click image for full size.
5. Open the **Gravity Force** module. Change the **Z** value to **-4500**.

   [![Set Gravity Values](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b310a008-1f04-4ba4-9f82-03ba146dcf3d/70-radial-set-gravity.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b310a008-1f04-4ba4-9f82-03ba146dcf3d/70-radial-set-gravity.png)

   Click image for full size.
6. Click the **Plus sign** icon (**+**) for **Particle Update**, and select **Forces > Drag**.

   [![Add Drag Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed0c9935-48af-43d6-8fc6-0d6f45b46ee2/71-radial-add-drag-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed0c9935-48af-43d6-8fc6-0d6f45b46ee2/71-radial-add-drag-module.png)

   Click image for full size.
7. Open the **Drag** module. Set the **Drag** value to **1.7**.

   [![Set Drag](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b18ff67-5dd4-434a-b902-45a18541adcd/72-radial-set-drag.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b18ff67-5dd4-434a-b902-45a18541adcd/72-radial-set-drag.png)

   Click image for full size.
8. Click the **Plus sign** (**+**) for **Particle Update** and select **Collision > Collision**. This module will make sure any sparks that hit something like a floor will collide and bounce back.

   [![Add Collision Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa93eeaf-3139-4bd9-a21e-5c6cabdfb567/73-radial-add-collision-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa93eeaf-3139-4bd9-a21e-5c6cabdfb567/73-radial-add-collision-module.png)

   Click image for full size.
9. Open the **Collision** module. Under **Bounce**, set the **Restitution** value to **0.4**.

   [![Set Collision Restitution](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d60f4738-8c64-4c45-b23b-a4018bb02249/74-radial-collision-set-restitution.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d60f4738-8c64-4c45-b23b-a4018bb02249/74-radial-collision-set-restitution.png)

   Click image for full size.
10. Under **Friction**, set the **Friction** value to **0.2**.

    [![Set Collision Friction](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05bdfd16-2e08-42ea-a05e-dfc7c50252d7/75-radial-collision-set-friction.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05bdfd16-2e08-42ea-a05e-dfc7c50252d7/75-radial-collision-set-friction.png)

    Click image for full size.
11. Remove the **Scale Color** module by clicking the **Trashcan** icon.

    [![Remove Scale Color Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e33b7aa4-ef44-415d-ad0f-f1161cf91750/76-radial-delete-scale-color.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e33b7aa4-ef44-415d-ad0f-f1161cf91750/76-radial-delete-scale-color.png)

    Click image for full size.
12. Click the **Plus sign** (**+**) and select **Size > Scale Sprite Size by Speed**.

    [![Add Scale Sprite Size by Speed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/803aa4c5-94b7-4084-b136-19cb3e2b5d58/77-radial-add-scale-sprite-by-speed-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/803aa4c5-94b7-4084-b136-19cb3e2b5d58/77-radial-add-scale-sprite-by-speed-module.png)

    Click image for full size.
13. Open the **Sprite Size Scale by Speed** module. Set the **Scale Factor** Minimum and Maximum to the following.

    [![Set Scale Factor Min and Max](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9577ad1d-8bd1-49df-ad9f-a75ef95e80a8/78-radial-set-scale-sprite-by-speed.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9577ad1d-8bd1-49df-ad9f-a75ef95e80a8/78-radial-set-scale-sprite-by-speed.png)

    Click image for full size.

    | Sprite Size Scale by Speed | Minimum | Maximum |
    | --- | --- | --- |
    | **X** | 0 | 0.5 |
    | **Y** | 3 | 6 |
14. Set the **Velocity Threshold** value to **2000**.

    [![Set Velocity Threshold](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/316f3bb6-77fc-43a0-a3e4-a23e4b8270ff/79-radial-set-scale-sprite-by-speed-threshold.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/316f3bb6-77fc-43a0-a3e4-a23e4b8270ff/79-radial-set-scale-sprite-by-speed-threshold.png)

    Click image for full size.

## End Result

Congratulations! After following these steps, the Sparks effect is complete. You can check the final results back in your level, and make any adjustments you like to fine-tune it.

![Sparks Effect Final Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b632ead6-8f82-4cb4-9f09-e45fa7469010/sparks-final.gif)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create the Smoke Emitter and the Sparks System](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#createthesmokeemitterandthesparkssystem)
* [Smoke Emitter - Edit the Emitter Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#smokeemitter-edittheemitterupdatesettings)
* [Smoke Emitter - Edit the Particle Spawn Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#smokeemitter-edittheparticlespawnsettings)
* [Smoke Emitter - Edit the Particle Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#smokeemitter-edittheparticleupdatesettings)
* [Add the Spark Burst Emitter to the System](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#addthesparkburstemittertothesystem)
* [Spark Burst Emitter - Edit Render Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#sparkburstemitter-editrendersettings)
* [Spark Burst Emitter - Edit the Emitter Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#sparkburstemitter-edittheemitterupdatesettings)
* [Spark Burst Emitter - Edit the Particle Spawn Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#sparkburstemitter-edittheparticlespawnsettings)
* [Spark Burst Emitter - Edit the Particle Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#sparkburstemitter-edittheparticleupdatesettings)
* [Add the Radial Sparks Emitter to the System](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#addtheradialsparksemittertothesystem)
* [Radial Sparks Emitter - Edit Render Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#radialsparksemitter-editrendersettings)
* [Radial Sparks Emitter - Edit the Emitter Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#radialsparksemitter-edittheemitterupdatesettings)
* [Radial Sparks Emitter - Edit Particle Spawn Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#radialsparksemitter-editparticlespawnsettings)
* [Radial Sparks Emitter - Edit the Particle Update Settings](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#radialsparksemitter-edittheparticleupdatesettings)
* [End Result](/documentation/en-us/unreal-engine/how-to-create-a-sparks-effect-in-niagara-for-unreal-engine?application_version=5.7#endresult)
