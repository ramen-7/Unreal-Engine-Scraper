<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7 -->

# Niagara Fluids Reference Guide

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
7. Niagara Fluids Reference Guide

# Niagara Fluids Reference Guide

Reference guide for the Niagara Fluids plugin.

![Niagara Fluids Reference Guide](https://dev.epicgames.com/community/api/documentation/image/f085ad2f-9ecd-497c-9ce8-1e0ff5d74ba0?resizing_type=fill&width=1920&height=335)

 On this page

**Niagara Fluids** is a plugin that provides you with templates to easily add real-time simulations to your projects. There are several different types of templates available:

* 2D Gas
* 2D Liquid
* 3D Gas
* 3D Liquid
* Shallow Water

2D simulations are more efficient and better suited for games and real-time use. 3D simulations have a more realistic look, but a tradeoff in higher memory and GPU cost. As such, 3D simulations are best for hero effects or cinematics. If needed, the results can also be baked into a flipbook and applied to textures for increased performance in real-time use.

This reference guide gives an overview of the **Grid 3D Gas Fire** template as an example of the design principles.

## Create a Niagara Fluids Simulation from a Template

To create a new Niagara Fluids simulation, right-click in the **Content Drawer** and select **Niagara System**, then select **Niagara Fluids > 3D Gas** from the left menu to see all available templates. To learn more about enabling the plugin and creating your first project, see the [Niagara Fluids Quick Start](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine).

You will see a variety of different 3D Gas examples to choose from.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5dbe272f-26ca-4591-93bc-77572b032abe/niagara-fluids-reference-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5dbe272f-26ca-4591-93bc-77572b032abe/niagara-fluids-reference-1.png)

Click image for full size.

## Inheritance

Fluid emitters use inheritance to progressively add functionality. For example, see the following diagram that shows the inheritance structure in the 3D Gas emitters.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d438d71f-1225-4432-ad8b-5e64715ca1c5/inheritance.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d438d71f-1225-4432-ad8b-5e64715ca1c5/inheritance.png)

Click image for full size.

The purpose of each emitter is the following:

| **Emitter** | **Purpose** |
| --- | --- |
| **Grid3D\_Gas\_Emitter** | This is the core simulation. |
| **Grid3D\_Gas\_Controls\_Base\_Emitter** | This emitter adds a centralized controller, debug slice functionality, and better render support. These controls are exposed in the **Emitter Summary**. |
| **Grid3D\_Gas\_CONTROLS\_Emitter** | This emitter adds particle source support. Density, temperature, and velocity are injected into the simulation from a second emitter. |
| **Grid3D\_Gas\_CONTROLS\_CINE\_Emitter** | This is an alternative controls emitter that uses a slower, deterministic form for the particle source algorithm. It includes advanced texture coordinates and is designed for cinematic use. |

## Fluids Emitter Summary

All the parameters you want to adjust to change the look and behavior of your simulation will be available in the Emitter Summary. For ease of organization, the summary has been broken down into the following sections:

* Grid
* Simulation
* Render
* Debug
* Scalability
* Source

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfc293a4-5a78-4379-8d62-0e80fc8bc7cd/fluids-emitter-summary.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfc293a4-5a78-4379-8d62-0e80fc8bc7cd/fluids-emitter-summary.png)

Click image for full size.

This reference guide describes the parameters available in each of these sections.

### Grid

Gas simulations are represented by a grid that is split into cells. Each cell contains information about the density, temperature, and velocity of the medium at that location. Smaller grid cells will increase the quality of the simulation, however with a cost in performance.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36af8e12-c09b-4718-8c83-538b25bb03ad/fluids-emitter-summary-grid.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36af8e12-c09b-4718-8c83-538b25bb03ad/fluids-emitter-summary-grid.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Grid Bounds Overlay** | Adds a toggle to the **Override Parameters** when you click the simulation in the **Level Editor**. From there, you can toggle the visibility of the red box around the simulation. |
| **Cell Size Guides** | Adds a toggle to the **Override Parameters** when you click the simulation in the **Level Editor**. From there, you can toggle the visibility of the guide cells on each major axis. |
| **World Space Size** | Adds a set of fields for the user to set in the **Override Parameters** when you click the simulation in the **Level Editor**. From there, you can change the size of the container box for the simulation. |
| **Local Pivot** | Change the offset for where the simulation origin should be. |
| **Resolution Max Axis** | Adds a toggle to the **Override Parameters** when you click on the simulation in the **Level Editor**. From there, you can set the resolution of the simulation, based on its longest side. A higher resolution will result in a more accurate look, but it will decrease performance. |
| **Open Boundary +/- X/Y/Z** | Toggle these options to adjust whether the edges of the simulation should be treated as a solid wall that particles can't travel through. |

### Simulation

The simulation section is broken down into three sub-sections: simulation, collide against, and turbulence. All of these parameters affect how the simulation changes over time based on properties like density, temperature, buoyancy, and more.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2032327-df6c-49d5-914d-01923d17aad9/fluids-emitter-summary-simulation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2032327-df6c-49d5-914d-01923d17aad9/fluids-emitter-summary-simulation.png)

Click image for full size.

#### Simulation

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3801fd77-2ea6-42c9-bfdd-67de0e374302/fluids-emitter-summary-simulation-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3801fd77-2ea6-42c9-bfdd-67de0e374302/fluids-emitter-summary-simulation-1.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Override Delta Time** | Set this value to override the engine's delta time with a fixed delta time. |
| **Delta Time Scale** | If **Override Delta** Time is not enabled, then the system uses the engine delta time. Enter a value in **Delta Time Scale** to modify the engine delta time by this amount. |
| **Vorticity Confinement** | Vorticity defines the spin of the simulation. Enter a value to amplify the vorticity in the simulation by this amount. |
| **Pressure Relaxation** | This value defines the pressure solver convergence. Enter a value between 0 and 1. We recommend keeping this value close to 1. |
| **Pressure Solve Iterations** | The more iterations you perform in the solver, the more accurate, however the slower it will be. Enter a value here that provides enough accuracy without a compromise in performance. |
| **Density Dissipation** | This value defines how quickly the density will dissipate to zero. The higher the number, the more quickly it will dissipate. |
| **Temperature Dissipation** | This value defines how quickly the temperature will dissipate to zero. The higher the number, the more quickly it will dissipate. |
| **Velocity Dissipation** | This value defines how quickly the velocity will dissipate to zero. The higher the number, the more quickly it will dissipate. |
| **Density Buoyancy** | This value defines the amount of downward velocity applied to the simulation based on its density. The higher this value, the more downward velocity. |
| **Temperature Buoyancy** | This value defines the amount of upward velocity applied to the simulation. The higher the number, the more upward velocity. |
| **Gravity** | Set the direction and magnitude of gravity in the simulation. |

#### Collide Against

You can have your simulation react to actors in your level. The most common way is to have those actors collide if they come into contact with the simulation. Enabling or disabling the parameters in the **Collide Against** section adds or removes data interfaces for those types of objects.

When Collide Against is enabled, select the simulation in the Level Editor to adjust the Override Parameters and select specific actors. Those actors will then collide with the simulation. See an example of this in the [Niagara Fluids Quick Start](/documentation/en-us/unreal-engine/niagara-fluids-quick-start-guide-for-unreal-engine).

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64146f4e-ab98-4509-90b1-33e8e5992a5e/fluids-emitter-summary-simulation-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64146f4e-ab98-4509-90b1-33e8e5992a5e/fluids-emitter-summary-simulation-2.png)

Click image for full size.

#### Turbulence

You can enable three bands of turbulence in the emitter. Seed Turbulence is applied on the initialization frame only. Turbulence 1 and 2 are applied while the simulation runs.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42f53380-f00f-4850-9c3b-ca2125be5020/fluids-emitter-summary-simulation-3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42f53380-f00f-4850-9c3b-ca2125be5020/fluids-emitter-summary-simulation-3.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Seed Turbulence Gain** | Set the strength of the turbulence. This is applied on the initialization frame only. |
| **Seed Turbulence Frequency** | This sets the size of the turbulence features. The smaller the number, the larger the features will look. This is applied on the initialization frame only. |
| **Seed Turbulence Speed** | Set how quickly the turbulence should move. This is applied on the initialization frame only. |
| **Seed Turbulence Local Space** | When enabled, the turbulence will follow the local space of the simulation. When disabled, turbulence will be fixed in world space. This is applied on the initialization frame only. |
| **Turbulence Density Gain** | Set the strength of the turbulence. This can be set as density and / or temperature. |
| **Turbulence Density Band** | Limit the turbulence between a defined range of densities. |
| **Turbulence Temperature Gain** | Set the strength of the turbulence. This can be set as density and / or temperature. |
| **Turbulence Temperature Band** | Limit the turbulence between a defined range of temperatures. |
| **Turbulence Frequency** | This sets the size of the turbulence features. The smaller the number, the larger the features will look. |
| **Turbulence Speed** | Set how quickly the turbulence should move. |
| **Turbulence Bias** | Bias the noise away from zero to give the turbulence direction. |
| **Turbulence Local Space** | When enabled, the turbulence will follow the local space of the simulation. When disabled, turbulence will be fixed in world space. |

### Render

Render properties are broken up into two sub-sections: Render and Lights.

#### Render

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df64dc1f-f1e2-4609-a7f5-f5fcbc30d5d6/fluids-emitter-summary-render-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df64dc1f-f1e2-4609-a7f5-f5fcbc30d5d6/fluids-emitter-summary-render-1.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Render Step Size Mult** | The simulation is calculated by breaking up the volume into cells, and then sampling the simulation in those cells. By default, the step size through the volume matches the size of the cells.  If you decrease the value in this multiplier, you will sample the simulation multiple times per cell. This is useful when a texture is modulating the simulation data, or if you are rendering detailed fire. |
| **Render Density** | This option controls whether to render the density or not. You can choose between **None**, **Linear**, or **Curve**. Linear mapping will map the data in the grid to the opacity of the gas. Or, you can set a curve for greater control. |
| **Render Density Range** | Set a density range to be rendered. The first value should be the density value that you want to be transparent, and the second should be the density value that gives the highest opacity. |
| **Render Density Curve** | If you set **Render Density** to **Curve**, then you can set the curve using this parameter. Expand the field to access the curve editor. |
| **Render Density Gain** | This value adds a multiplier on top of the final density being rendered. |
| **Render Density Albedo** | This value is a float which colors the smoke from black to white. |
| **Shadow Quality** | Baked shadows are calculated by breaking the volume up into cells, then stepping through the volume to sample the simulation in those cells. Adjust this value to sample the simulation multiple times per cell. |
| **Shadow Max Steps** | Limit the number of steps to take when sampling for shadows. |
| **Render Temperature** | Choose how to render the **Temperature** component. You can choose from None, Black Body, or Curve.  **None** will not render the Temperature values.  **Black Body** will render an environmentally realistic fire, from black, to red, orange, yellow, then white.  **Curve** will let you set your own custom color values. |
| **Render Temperature Range** | Set a range of temperature values to map to the **Render Temperature**. This only applies when **Render Temperature** is set to **Black Body** or **Curve**. |
| **Render Temperature Curve** | If Render Temperature is set to Black Body, the alpha component of this curve defines the opacity of the fire.  If Render Temperature is set to Curve, this curve defines both the color and the opacity of the gas. |
| **Render Temp Color Gain** | Add an additional multiplier to the gas color. |
| **Render Temp Opacity Gain** | Add an additional multiplier to the opacity of the gas. |

#### Lights

The **Lights** section contains data interfaces to bring in any directional lights that you set up in your level through **Override Parameters**. If no lights are connected to these data interfaces, then default lighting is applied. To adjust the properties of the default lighting, click the **Show Advanced** button.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28d20a47-33b1-4f06-af82-c1cf4e11710a/fluids-emitter-summary-render-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28d20a47-33b1-4f06-af82-c1cf4e11710a/fluids-emitter-summary-render-2.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Light1/2** | This data interface reads the attributes from a light you have connected to the **Override Parameters** of the Niagara system in the Level Editor. |
| **Lgt1/2 Shadow Density** | Set how much light the density component should occlude. |
| **Lgt1/2 Default Intensity** | Set the intensity of the default light. |
| **Lgt1/2 Default Color** | Set the color of the default light. |
| **Lgt1/2 Default Direction** | Set the direction of the default light. This direction is a vector that is set in world space. |

### Debug

Use these options to debug your simulation.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4c87106-a398-4f46-b9ec-735d9946b025/fluids-emitter-summary-debug.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4c87106-a398-4f46-b9ec-735d9946b025/fluids-emitter-summary-debug.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Debug Sources** | Enable this option to overwrite grid data on every frame with the source data. By doing this, you will see what the sources are introducing to the simulation. |
| **Render Debug Slice** | Enable this option to render a 2D slice inside the grid. Density is rendered in the red channel. Temperature is rendered in the green channel. Combined light intensity is rendered in the blue channel. |
| **Render Debug Slice Axis** | Choose which axis to orient the slice to. |
| **Render Debug Slice Offset** | Set how far along the axis to render the slice. This value should be between 0 and 1, with 0.5 being the center point. |
| **Render Debug Slice Lights** | Enable this option to render the light intensity in the blue channel. |

### Scalability

Use the scalability settings to override the parameters that depend on the **Quality** setting of your simulation. By default, scalability overrides are applied when the engine is running in **Cinematic** quality.

An example of when you might want to use a scalability override is when you want to render a cinematic sequence with **Movie Render Queue**. There is a setting in Movie Render Queue called **Game Overrides** that automatically changes the quality level to Cinematic when rendering. This way, you can set your Scalability Override quality to Cinematic, but you can work interactively in the scene at a lower quality, but faster, setting. Then, when you press the **Render** button in Movie Render Queue, the high quality settings will take effect.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf5acb14-ec3e-40e7-9c6d-f653da3d4ab2/fluids-emitter-summary-scalability.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf5acb14-ec3e-40e7-9c6d-f653da3d4ab2/fluids-emitter-summary-scalability.png)

Click image for full size.

### Source

Adjust source parameters to change information based on incoming particles.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/00c7b92f-8be1-4b5f-a4f0-3676ba82a71f/fluids-emitter-summary-source.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/00c7b92f-8be1-4b5f-a4f0-3676ba82a71f/fluids-emitter-summary-source.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Particle Attribute Reader** | This data interface reads from another emitter in the system. |
| **Scale Emission by dt** | Enable this to ensure that the source data remains consistent, even if the engine tick rate varies. |
| **Use Falloff** | Enable this to anti-alias data at the edges of particles. This keeps sourcing consistent, even if the resolution changes. |
| **Scatter Density** | Enable this to look for the density attribute on the incoming particle source, `fluids_source_density`. |
| **Scatter Temperature** | Enable this to look for the temperature attribute on the incoming particle source, `fluids_source_temperature`. |
| **Scatter Velocity** | Enable this to look for the velocity attribute on the incoming particle source, `fluids_source_velocity`. |
| **Use Radius** | Enable this to overlap all cells in the simulation based on the particle radius, `fluids_source_radius`. This keeps the sourcing consistent, even if the resolution changes. |
| **Density Mult** | Enter a value to multiply the incoming particle density attribute by. |
| **Splat Size Density** | If Use Radius is disabled, enter a value to set how many cells should be stamped with the particle density data. Enter 1 to indicate the closest cell, or 2 to indicate the closest cell and the cells touching the closest cell. As you increase this number, the number of cells being written to increases significantly. |
| **Temperature Mult** | Enter a value to multiply the incoming particle temperature attribute by. |
| **Splat Size Temperature** | If **Use Radius** is disabled, enter a value to set how many cells should be stamped with the particle temperature data. Enter 1 to indicate the closest cell, or 2 to indicate the closest cell and the cells touching the closest cell. As you increase this number, the number of cells being written to increases significantly. |
| **Local Space Particles** | Enable this value to set the particles to be local to this simulation. |
| **Velocity Mult** | Enter a value to multiply the incoming particle velocity attribute by. |
| **Splat Size Velocity** | If **Use Radius** is disabled, enter a value to set how many cells should be stamped with the particle velocity data. Enter 1 to indicate the closest cell, or 2 to indicate the closest cell and the cells touching the closest cell. As you increase this number, the number of cells being written to increases significantly. |

### Texture

There is an additional set of parameters in the template for **Grid 3D Gas Explosion Cine**. Select the **Emitter Summary** on the **Grid3D\_Gas\_CONTROLS\_CINE\_Emitter**. Then, select the **All** tab, and locate the **Texture** section.

This emitter includes a simulation stage that advects texture coordinates through the simulation. The included **MI\_RayMarch\_Fire\_Ramps\_Tex** material will use these coordinates to modulate the render with noise.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7c5b68f-fb77-45a0-80ea-f99f52eb64a3/fluids-emitter-summary-texture.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7c5b68f-fb77-45a0-80ea-f99f52eb64a3/fluids-emitter-summary-texture.png)

Click image for full size.

| **Parameter** | **Description** |
| --- | --- |
| **Texture Smoke Density Gain** | Enter a value to modulate the density with noise. |
| **Texture Smoke Color Gain** | Enter a value to modulate the smoke albedo with noise. |
| **Texture Fire Density Gain** | Enter a value to modulate the opacity of the fire contribution with noise. |
| **Texture Fire Color Gain** | Enter a value to modulate the fire color intensity with noise. |
| **Texture Scale** | Enter a value to adjust the size of the noise pattern. |
| **Texture Remap To 0** | This parameter performs a fit operation. Enter a value that will be remapped to 0, adding contrast and bias to the effect. |
| **Texture Remap To 1** | This parameter performs a fit operation. Enter a value that will be remapped to 1, adding contrast and bias to the effect. |
| **Value Data** | Choose whether to limit the influence of the texture to **Density** or **Temperature**. The option you choose here will determine how to apply the following parameters: **Value Band Min**, **Value Band Max**, and **Value Band Sharpness**. |
| **Value Band Min** | Set the lower value of the simulation data to which the texture will be applied. |
| **Value Band Max** | Set the upper value of the simulation data to which the texture will be applied. |
| **Value Band Sharpness** | Set how the texture will transition within the band. Enter a sharpness value of 0 to have the transition happen slowly within the band, reaching full influence at the midpoint of **Value Band Min** and **Value Band Max**. Enter a sharpness value of 1 to have it influence immediately as soon as the data falls anywhere within the band. |
| **Loop Duration** | The coordinates reset and transition back and forth to avoid stretching. Enter a value to adjust the loop duration. The higher the loop duration, the more stretching you will see. |
| **Debug Texture** | Enable this option to override the material and only show the texturing value. |

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create a Niagara Fluids Simulation from a Template](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#createaniagarafluidssimulationfromatemplate)
* [Inheritance](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#inheritance)
* [Fluids Emitter Summary](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#fluidsemittersummary)
* [Grid](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#grid)
* [Simulation](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#simulation)
* [Simulation](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#simulation-2)
* [Collide Against](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#collideagainst)
* [Turbulence](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#turbulence)
* [Render](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#render)
* [Render](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#render-2)
* [Lights](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#lights)
* [Debug](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#debug)
* [Scalability](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#scalability)
* [Source](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#source)
* [Texture](/documentation/en-us/unreal-engine/niagara-fluids-reference-in-unreal-engine?application_version=5.7#texture)
