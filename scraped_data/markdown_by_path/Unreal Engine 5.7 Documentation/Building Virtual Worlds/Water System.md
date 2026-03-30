<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/water-system-in-unreal-engine?application_version=5.7 -->

# Water System

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. Water System

# Water System

A collection of features, tools, and information about using the water rendering and meshing system.

![Water System](https://dev.epicgames.com/community/api/documentation/image/525d8463-848e-406a-948b-195f20f888a5?resizing_type=fill&width=1920&height=335)

 On this page

The Water system enables you to create rivers, lakes, and oceans that all interact and work together with your Landscape terrains using a spline-based workflow. The Water system unifies the shading and mesh rendering pipeline, with surfaces that support physics interactions and fluid simulation with gameplay, such as ripples caused by footsteps or the wake behind a boat moving through the water.

## Enabling the Water System Plugin and Content

The Water system is a self-contained plugin that can be enabled/disabled depending on whether you need it for your project. The plugin enables the rendering and meshing system for water, and also provides example and default content for you to use.

To enable the Water system, use **Edit > Plugins** to open the **Plugins** browser. Search for the **Water** plugin and check its box to enable it.

[![Water Plugin](https://dev.epicgames.com/community/api/documentation/image/c8e7d495-1f62-4993-b204-571a8ade28a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c8e7d495-1f62-4993-b204-571a8ade28a7?resizing_type=fit)

Click image for full size.

Restart the editor for changes to take effect.

### Additional Water Plugin Content

The Water plugin also contains some default materials and content that can be used in your own projects or for exploration. You can find it in the Content Browser under the **Water Content** folder.

[![Content Browser Settings](https://dev.epicgames.com/community/api/documentation/image/dbc0901a-a4c1-4b2a-8386-ee38f1b32581?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dbc0901a-a4c1-4b2a-8386-ee38f1b32581?resizing_type=fit)

Click image for full size.

[![Water Content Folder](https://dev.epicgames.com/community/api/documentation/image/ec4cc7bc-1acb-43b3-a9b0-a4c1269d1bc9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec4cc7bc-1acb-43b3-a9b0-a4c1269d1bc9?resizing_type=fit)

Click image for full size.

If you do not see this folder in your Content Browser, select **View Options** (located in the bottom-right) and check the boxes next to **Show Engine Content** and **Show Plugin Content**.

In this folder, there are example maps and content to try on your own, such as:

* Caustics generation
* Fluid simulation
* Physics simulation buoyancy Blueprints

## Getting Started

* [![Water Meshing System and Surface Rendering](https://dev.epicgames.com/community/api/documentation/image/f7e1b82a-9100-4b0e-b05c-04ac950a0933?resizing_type=fit&width=640&height=640)

  Water Meshing System and Surface Rendering

  An overview of how surface meshes and materials are used to render water.](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-meshing-system-and-surface-rendering-in-unreal-engine)

* [![Water Body Actors](https://dev.epicgames.com/community/api/documentation/image/d345fba0-a7f5-4f33-a25d-20ede30888f2?resizing_type=fit&width=640&height=640)

  Water Body Actors

  A look at the various water bodies available and how to use them to build worlds with the water system.](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-body-actors-in-unreal-engine)

## Essentials

* [![Simulating Waves Using The Water Waves Asset](https://dev.epicgames.com/community/api/documentation/image/8f9f289e-50b7-43b0-ae83-c437854cfd1b?resizing_type=fit&width=640&height=640)

  Simulating Waves Using The Water Waves Asset

  An overview of how to use the Water Waves Asset to drive wave simulation.](https://dev.epicgames.com/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine)

* [![Water Buoyancy Component](https://dev.epicgames.com/community/api/documentation/image/5783048d-acdf-498c-b071-213968157309?resizing_type=fit&width=640&height=640)

  Water Buoyancy Component

  A look at how to set up and use the Buoyancy Component to make objects float along water surfaces.](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-buoyancy-component-in-unreal-engine)

* [![Single Layer Water Shading Model](https://dev.epicgames.com/community/api/documentation/image/48031318-ef09-439d-a0a0-69c43a752825?resizing_type=fit&width=640&height=640)

  Single Layer Water Shading Model

  An overview of the Single Layer Water Material shading model used to render physically based water surfaces.](https://dev.epicgames.com/documentation/en-us/unreal-engine/single-layer-water-shading-model-in-unreal-engine)

* [![Water Debugging and Scalability Options](https://dev.epicgames.com/community/api/documentation/image/58fa1f33-22dc-4a01-ad46-7f21f02cbc15?resizing_type=fit&width=640&height=640)

  Water Debugging and Scalability Options

  A look at how you can debug and scale water to fit your project's needs.](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-debugging-and-scalability-options-in-unreal-engine)

## Additional Resources

* [water](https://dev.epicgames.com/community/search?query=water)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling the Water System Plugin and Content](/documentation/en-us/unreal-engine/water-system-in-unreal-engine?application_version=5.7#enabling-the-water-system-plugin-and-content)
* [Additional Water Plugin Content](/documentation/en-us/unreal-engine/water-system-in-unreal-engine?application_version=5.7#additional-water-plugin-content)
* [Getting Started](/documentation/en-us/unreal-engine/water-system-in-unreal-engine?application_version=5.7#getting-started)
* [Essentials](/documentation/en-us/unreal-engine/water-system-in-unreal-engine?application_version=5.7#essentials)
* [Additional Resources](/documentation/en-us/unreal-engine/water-system-in-unreal-engine?application_version=5.7#additional-resources)
