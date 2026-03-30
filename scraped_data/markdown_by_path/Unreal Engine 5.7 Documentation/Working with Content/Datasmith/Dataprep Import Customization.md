<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine?application_version=5.7 -->

# Dataprep Import Customization

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine "Datasmith")
7. Dataprep Import Customization

# Dataprep Import Customization

Make reusable recipes that import assets and prepare them for real-time rendering.

![Dataprep Import Customization](https://dev.epicgames.com/community/api/documentation/image/9f81b60d-660d-4a64-90f8-c68fdfb3b97f?resizing_type=fill&width=1920&height=335)

 On this page

When Datasmith imports a scene into Unreal Engine, it does its best to preserve the geometry, materials, and scene hierarchy that you created in your source application. However, when you build 3D models in specialized applications for purposes other than real-time rendering, the scenes are often not prepared in a way that makes sense for a real-time rendering engine like Unreal. For example, this is often the case for models you create in applications like Rhino for the primary purpose of manufacturing or extruding physical parts, scenes you create in Revit or an IFC-compliant application for the primary purpose of documenting a construction project, scenes you create with procedurally generated elements in Cinema 4D, and so on.

You can always import the raw scene data, then make use of the tools offered by Unreal Editor to adjust your Assets and Actors after the import is complete. However, this has some limitations. For example, you may need to repeat these steps when you reimport the scene to pick up changes made in the source application or when you reimport a different scene with the same settings.

You can use the Visual Dataprep system to create reusable import "recipes" that reorganize, clean, merge, and modify scene elements before creating the final Assets and Actors in your Unreal Engine Project. You can create a recipe once, then reuse it each time you need to import a scene. You can also reuse the same recipe to import different source files, and even reuse it across different Projects. This effectively allows you to create your own standardized set of Asset import pipelines that match the needs of your content.

With the Visual Dataprep system, you can build common data preparation tasks like these into the import process:

* Replacing Materials used in your source scene with high-quality Materials made specifically for real-time visualization.
* Identifying unnecessary geometry and removing it from the scene.
* Merging geometry together to reduce the number of separate objects in the scene.
* Creating Levels of Detail to render complex geometry more efficiently.
* Creating collisions for Objects that need collision meshes to work in your runtime experience, such as floors and walls.

As you get started with Visual Dataprep, you will discover some other operations that you can use to prepare reusable dataprep recipes for real-time scenes.

## Get Started

[![Dataprep Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe5bad24-c913-4332-b3ca-1f08946fd067/topic-image.png)

Dataprep Overview

Overview of the Dataprep system and how it works.](/documentation/en-us/unreal-engine/dataprep-overview-in-unreal-engine)

## Tutorials

[![Working With Dataprep Instances](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe83ead6-0443-4c81-b6d7-1385e6670dea/topic-image.png)

Working With Dataprep Instances

How to create parent Dataprep recipes that expose limited customization parameters to Dataprep Instances.](/documentation/en-us/unreal-engine/working-with-dataprep-instances-in-unreal-engine)
[![Creating Custom Dataprep Blocks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42d91491-d08b-4652-a672-6da93892267a/5-0-custom-dataprep-blocks-topic-image.png)

Creating Custom Dataprep Blocks

How to create your own custom filters and operators for the Dataprep system in Blueprint.](/documentation/en-us/unreal-engine/creating-custom-dataprep-blocks-in-unreal-engine)

## Reference

[![Dataprep Selection Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d96f72a-f0a8-43ed-ad90-c4c36f84326b/topic-image.png)

Dataprep Selection Reference

Details on the ways you can filter and select scene elements in Dataprep steps.](/documentation/en-us/unreal-engine/dataprep-selection-reference-in-unreal-engine)
[![Dataprep Operation Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26d3e8eb-1990-4a66-9fbe-cc2acc945377/topic-image.png)

Dataprep Operation Reference

Details on the operations you can apply to selected scene elements in the Dataprep system.](/documentation/en-us/unreal-engine/dataprep-operation-reference-in-unreal-engine)
[![Dataprep Selection Transform Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0370edd4-8e78-45f6-9e29-a21576a81a2e/topic-image.png)

Dataprep Selection Transform Reference

Details on ways you can transform the list of objects you want to modify in the Dataprep system.](/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine)

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [dataprep](https://dev.epicgames.com/community/search?query=dataprep)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Get Started](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine?application_version=5.7#getstarted)
* [Tutorials](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine?application_version=5.7#tutorials)
* [Reference](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine?application_version=5.7#reference)
