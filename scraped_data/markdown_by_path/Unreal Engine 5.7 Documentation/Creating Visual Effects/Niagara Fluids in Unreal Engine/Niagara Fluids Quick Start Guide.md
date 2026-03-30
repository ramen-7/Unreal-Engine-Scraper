<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7 -->

# Niagara Fluids Quick Start Guide

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
6. [Niagara Fluids in Unreal Engine](/documentation/en-us/unreal-engine/niagara-fluids-in-unreal-engine "Niagara Fluids in Unreal Engine")
7. Niagara Fluids Quick Start Guide

# Niagara Fluids Quick Start Guide

A quick start guide for using the Niagara Fluids plugin to create real-time fluid simulation.

![Niagara Fluids Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/b00052e1-039e-423e-91f5-51ce319e046d?resizing_type=fill&width=1920&height=335)

 On this page

Pre-Requisite Tasks:

* [Create a New Project](/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine)
* [Enable the Niagara Plugin](/documentation/en-us/unreal-engine/how-to-enable-the-niagara-effects-plugin-in-unreal-engine)

**Niagara Fluids** is a plugin that you can enable to add templates to your project for real-time fluid simulation.

## Goals

In this tutorial, you will learn how to enable the Niagara Fluids plugin and create your first project.

## Objectives

* Enable the Niagara Fluids plugin
* Create a new Niagara System from a Fluids template
* Modify the parameters to achieve a new look

## 1 - Enable the Niagara Fluids Plugin

To begin working, first enable the Niagara Fluids plugin.

1. Click on **Edit > Plugins**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9af3dc56-a1e4-48bf-837c-c3b2e5fa5793/plugins.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9af3dc56-a1e4-48bf-837c-c3b2e5fa5793/plugins.png)

   Click for full size.
2. Search for **Niagara** in the search bar. Click the checkbox to the left of **Niagara Fluids**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48a0e07f-8d60-44aa-8160-f666f1618e84/niagara-plugins.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48a0e07f-8d60-44aa-8160-f666f1618e84/niagara-plugins.png)

   Click for full size.
3. A warning message is displayed, because this plugin is still in Beta. Click **Yes** to enable the plugin.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31fc4d30-aaa0-4286-8d09-38faaf0e87fc/beta-warning.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31fc4d30-aaa0-4286-8d09-38faaf0e87fc/beta-warning.png)

   Click for full size.
4. You are then prompted to restart Unreal Engine. Click **Restart Now**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ebd63e3-f69a-4adf-9133-8d148d6be822/restart-now.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ebd63e3-f69a-4adf-9133-8d148d6be822/restart-now.png)

   Click for full size.

The fluids templates will now be available to you when you create a new Niagara system.

## 2 - Create the Niagara System

Next, you will create a new Niagara system from a Fluids template.

1. Right-click in the **Content Drawer**. Under the **Create Basic Asset** section, select **Niagara System**.

   ![Select Niagara system in the right-click menu.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/18c559e9-c9a2-40c9-a7af-2e0505717180/niagara-fluids-quickstart-1.png)
2. Select **Niagara Fluids > 3D Gas** from the left menu, then select **Grid3D\_Gas\_Explosion** and click **Create**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08555b70-01e2-48f7-8327-4cc4bd48ef76/niagara-fluids-quickstart-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08555b70-01e2-48f7-8327-4cc4bd48ef76/niagara-fluids-quickstart-2.png)

   Click for full size.
3. Rename the Niagara system to **Grid3DGasExplosion**.

   ![Rename your new Niagara system.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/04da3a67-47e6-4dac-899e-32b3f48fcfa0/gas-explosion-system.png)
4. Drag the Niagara system into your level. The explosion triggers in the scene when you drop it.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4cbf5022-dbc5-4b6b-a4b3-c1cb1eed2f21/drag-system-into-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4cbf5022-dbc5-4b6b-a4b3-c1cb1eed2f21/drag-system-into-level.png)

   Click for full size.

## 3 - Add an Actor to Collide With

The first place you can adjust the actor is within the level itself. For this example, you are using a simple sphere.

1. Select the Niagara system in the level.
2. In the **Details** panel, under **Override Parameters**, adjust any of the exposed parameters as needed. Since this system does not loop, toggle on and off **Show Overlays** to force the explosion to restart. This is a good way to test as you adjust the parameters.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1e285ef-d329-400f-96d3-a30132e495c5/override-parameters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1e285ef-d329-400f-96d3-a30132e495c5/override-parameters.png)

   Click for full size.

   | Parameter | Description |
   | --- | --- |
   | **Collide\_GeometryCollection, Collide\_PhysicsAsset, Collide\_StaticMesh** | Use these data interfaces to add actors in your level to affect your simulation. |
   | **DirectionalLight1, DirectionalLight2** | Link up to two directional lights to your system. In this way, you can use lights that are already in your level to illuminate your simulation.  If you leave these empty, the system sets some default values. |
   | **ResolutionMaxAxis** | Set the resolution of your simulation. Try to keep this as small as possible to preserve memory and performance. |
   | **ShowOverlays** | Toggle the bounds of the system on and off. |
   | **SourceOffset** | Position the explosion inside the system's bounding box. By default, this is set to the center of the domain. |
   | **WorldSpaceSize** | Change the size of the bounding box for the simulation. |
3. Set the **WorldSpaceSize** to **300**, **300**, **600**.
4. To show how to have the explosion interact with an object, add a simple sphere to the scene and position it above the explosion. Click the **Quick Add Content** button, then select **Shapes > Sphere**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac1ab84e-6714-424a-ad01-49feff5d0d9c/add-sphere.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac1ab84e-6714-424a-ad01-49feff5d0d9c/add-sphere.png)

   Click for full size.
5. Move the sphere into position above your explosion, but within its bounding box.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea722b19-b72f-482c-a261-ce28c8082275/sphere-explosion-bounding.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea722b19-b72f-482c-a261-ce28c8082275/sphere-explosion-bounding.png)

   Click for full size.
6. To reduce the pixelation of the simulation, you need to increase the resolution. Select the **simulation, then** in the **Details** panel, in the **Override Parameters** section, adjust the **ResolutionMaxAxis** to **300**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aceb18c7-5e69-47e6-93c2-61840f8b493b/increase-resolution.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aceb18c7-5e69-47e6-93c2-61840f8b493b/increase-resolution.png)

   Click for full size.
7. Next, you need to add a tag to the sphere to indicate to the level that it is a collider object.

   * Click the **sphere** to select it.
   * In the **Details** panel, search for 'tag'.
   * Under the **Actor** section, in **Advanced > Tags**, click **plus(+)** to add a new tag.
   * Type in 'collider' for the name of the tag. The explosion will now collide with the sphere.[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1776d120-cd6c-4abc-976b-3a0f5c933252/collider-tag.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1776d120-cd6c-4abc-976b-3a0f5c933252/collider-tag.png)

   Click for full size.

## 4 - Adjust the Look of the Explosion

Next, you fine-tune the look of the explosion.

1. Double-click on the **Niagara system** in the **Content Drawer** to open it in the **Niagara Editor**.
2. You should see the explosion playing in the **Preview** panel. In the **System Overview**, there are two emitters set up. If you don't see them right away, click F to fit them in the window.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1eca0b0c-3447-430a-b10f-b47a5cb88fba/system-overview-emitters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1eca0b0c-3447-430a-b10f-b47a5cb88fba/system-overview-emitters.png)

   Click for full size.
3. The emitter on the left, **ParticleSourceEmitter**, injects values into the simulation. The emitter on the right, **Grid3D\_Gas\_CONTROLS\_Emitter**, is known as a Controls emitter. This is the primary emitter you will use to adjust the look. Click on **Emitter Summary** to view the parameters you can adjust.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/534814fa-9fe5-424f-9227-66bab2a5ce0a/emitter-summary.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/534814fa-9fe5-424f-9227-66bab2a5ce0a/emitter-summary.png)

   Click for full size.

   Shift-click the triangle to the left of a section heading to collapse all sections.
4. First, adjust the dissipation values. **Dissipation** defines how quickly the data fades over time. The higher the number, the faster the data will drop to zero. Lowering the number will maintain the values for longer. Set the values to the following for a shorter, burst-like explosion.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/986d4765-5211-43e9-972b-48a5d4417c60/density-temperature-velocity-dissipation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/986d4765-5211-43e9-972b-48a5d4417c60/density-temperature-velocity-dissipation.png)

   Click for full size.

   | Parameter | Value |
   | --- | --- |
   | **Density Dissipation** | 3.0 |
   | **Temperature Dissipation** | 1.5 |
   | **Velocity Dissipation** | 0.8 |
5. Next, adjust the buoyancy values. In this simulation, buoyancy from temperature causes the simulation to rise. Buoyancy from density causes the simulation to fall. Velocity can be added to the simulation by adjusting the density and/or the temperature values. If you change the direction of the **Gravity** parameter, then the buoyancy adapts to the new direction. To make the explosion rise more quickly, change the **Temperature Buoyancy** value to **3.5**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93187f72-a3a2-42bf-9940-2ab5b0d1874e/temperature-buoyancy.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93187f72-a3a2-42bf-9940-2ab5b0d1874e/temperature-buoyancy.png)

   Click for full size.
6. To finalize the look, adjust the parameters in the **Render** section. By default, **Render Density** is set to **Linear**. This means that the values defined by **Render Density Range** will start at **0.0** opacity, and ramp up to an opacity of **1.0** when rendered. You can change the opacity overall by adding to the **Render Density Gain** value. For this example, set it to **0.5**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdbb6609-41f0-4f0d-8512-0b256485b7bf/render-density.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdbb6609-41f0-4f0d-8512-0b256485b7bf/render-density.png)

   Click for full size.

   By default, the colors transition from black, to red, orange, and then white, using a black body curve. This black body curve is a physically plausible mapping that gives a realistic look. It is based on the color of the wavelengths of light emitted by a hot black body at different temperatures.
7. Change **Render Temperature** to **Curve**. This property is where you can input your own custom values for the color.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9dc00f81-fe8e-4ccd-a4e2-900cf141e533/render-temperature.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9dc00f81-fe8e-4ccd-a4e2-900cf141e533/render-temperature.png)

   Click for full size.
8. Expand the **Render Temperature Curve**, then **Curve**. Adjust the colors freely to achieve the look you want.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76e89347-a2da-461c-b0e5-87cfd97821b5/render-temperature-curve.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76e89347-a2da-461c-b0e5-87cfd97821b5/render-temperature-curve.png)

   Click for full size.
9. When you are satisfied with the look, **Save** and then close the Niagara system. In the **Level Editor**, you now see the explosion in your scene with the adjustments you made.

## End Result

Your final result now looks like the following.

![The final result of the Niagara Fluids quickstart.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6df0650-c4cd-4fac-b802-2720ce69938b/final-result.gif)

## Further Reading

To continue learning more about the parameters you can adjust, read the [Niagara Fluids Reference Guide](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine).

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Goals](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#goals)
* [Objectives](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#objectives)
* [1 - Enable the Niagara Fluids Plugin](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#1-enabletheniagarafluidsplugin)
* [2 - Create the Niagara System](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#2-createtheniagarasystem)
* [3 - Add an Actor to Collide With](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#3-addanactortocollidewith)
* [4 - Adjust the Look of the Explosion](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#4-adjustthelookoftheexplosion)
* [End Result](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#endresult)
* [Further Reading](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine?application_version=5.7#furtherreading)
