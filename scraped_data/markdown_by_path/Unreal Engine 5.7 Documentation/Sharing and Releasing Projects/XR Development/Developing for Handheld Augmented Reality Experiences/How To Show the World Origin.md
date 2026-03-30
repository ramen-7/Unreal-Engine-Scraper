<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-show-the-world-origin-in-unreal-engine?application_version=5.7 -->

# How To Show the World Origin

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Developing for Handheld Augmented Reality Experiences](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine "Developing for Handheld Augmented Reality Experiences")
8. How To Show the World Origin

# How To Show the World Origin

How to show the world origin in augmented reality.

![How To Show the World Origin](https://dev.epicgames.com/community/api/documentation/image/89094ad6-23c3-4b7d-bb1c-6225f8133db1?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dba58806-80f1-4241-8dd9-f0e79631c8b5/ar_worldorigingraphic.png)


For this guide, we are using the **Handheld AR** template.

In the following How To, we will take a look at how the example project created by the **Handheld AR** template demonstrates drawing the world origin. Knowing where the augmented reality system (ARKit/ARCore) has placed the world origin, can be useful information when troubleshooting. Devices often decide what they consider World Location 0,0,0 (World Origin) based on unpredictable factors, potentially making it difficult to debug issues with the location, movement or spawning of content where tracked geometry transform information is not referenced. This becomes a bigger problem when working with baked lighting, as static content expects the World Origin to be in a specific spot.

## Steps

### Open an AR Project

1. Open the **Project Browser** and create a new **Handheld AR** Blueprint project, or open an existing augmented reality project.
   If you need assistance creating a new augmented reality project, see the [Handheld AR Template Quickstart](/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) documentation.
2. Open the **Find in Blueprints** menu item.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b77e62a-9a36-4db0-bc45-2d5930cfd85c/ar_findinblueprintsmenu.png)
3. Search for **Debug Draw World Origin**. In the results, double-click the **Debug Draw World Origin** function.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2926f9a-c2af-4723-ae01-6b331279b9e7/ar_blueprintsearch_debugdrawworldorigin.png)

### Show World Origin

The example project demonstrates a simple method of drawing the world origin. Drawing the world origin is a useful debugging exercise to help determine what the augmented reality system has determined as the world origin. As shown below, the world origin always starts at **0.0, 0.0, 0.0**.

#### Debug Draw World Origin

* **Draw Debug String** - This function is placing the text string "WORLD ORIGIN" at the world origin (0.0, 0.0, 0.0) location.
* **Draw Debug Arrow(s)** - These functions are drawing short arrows along X, Y, and Z axes respectively, starting from the world origin (0.0, 0,0, 0,0).

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92308c47-e462-4249-b1e2-f36a448991ef/ar_debugdrawworldoriginfunction.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92308c47-e462-4249-b1e2-f36a448991ef/ar_debugdrawworldoriginfunction.png)

### Explore Other AR Functions

Exploring a project based on the **Handheld AR** Blueprint template provides an opportunity to examine the actual use of the various augmented reality functions in context. There are dozens of new augmented reality functions, so take some time to dig into a new project and explore the implementation details demonstrated.

A good place to start exploring the project and the new augmented reality functions is to open the **Content Browser**, navigate to **Content\HandheldARBP\Blueprints\UI** and open the **BP\_DebugMenu** asset in the **Blueprint Editor**.

* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ar](https://dev.epicgames.com/community/search?query=ar)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [android](https://dev.epicgames.com/community/search?query=android)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/how-to-show-the-world-origin-in-unreal-engine?application_version=5.7#steps)
* [Open an AR Project](/documentation/en-us/unreal-engine/how-to-show-the-world-origin-in-unreal-engine?application_version=5.7#openanarproject)
* [Show World Origin](/documentation/en-us/unreal-engine/how-to-show-the-world-origin-in-unreal-engine?application_version=5.7#showworldorigin)
* [Debug Draw World Origin](/documentation/en-us/unreal-engine/how-to-show-the-world-origin-in-unreal-engine?application_version=5.7#debugdrawworldorigin)
* [Explore Other AR Functions](/documentation/en-us/unreal-engine/how-to-show-the-world-origin-in-unreal-engine?application_version=5.7#exploreotherarfunctions)

Related documents

[Handheld AR Template Quickstart

![Handheld AR Template Quickstart](https://dev.epicgames.com/community/api/documentation/image/994215b3-875d-4442-9ffe-a70974d62197?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine)
