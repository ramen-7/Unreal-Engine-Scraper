<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine?application_version=5.7 -->

# Hair Rendering and Simulation

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
6. Hair Rendering and Simulation

# Hair Rendering and Simulation

Information on rendering, simulation, creation, and editing of hair grooms in Unreal Engine.

![Hair Rendering and Simulation](https://dev.epicgames.com/community/api/documentation/image/e540e8e6-24ef-4433-b6ec-ff6e9ba29d28?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine's groom rendering and simulation system uses a strand-based workflow to render each individual strand of hair with physically accurate motion, enabling artists to simulate and render hundreds of thousands (or more) photo-real hairs in real-time. Traditionally, hair created for use in real-time projects has been created using card-based techniques, or other similar approximations. The groom system in Unreal Engine manages and utilizes these methods, as well.

![Example of Groom using Strands and Cards](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20fa603f-9b5b-407a-874f-a9954e9fec88/groom-card-strands-example.png)

MetaHuman character example with grooms showing their strands (left) and cards (right).

## Getting Started

[![Groom Simulation and Rendering Quick Start Guide](images/static/document_list/empty_thumbnail.svg)

Groom Simulation and Rendering Quick Start Guide

A guide to getting started using hair rendering and simulation with characters in your project.](/documentation/en-us/unreal-engine/hair-simulation-and-rendering-quick-start-guide-in-unreal-engine)
[![Setting Up a Project to use Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eddf744f-4962-4407-8ad6-6cba74920b20/placeholder_topic.png)

Setting Up a Project to use Grooms

Setup your projects to import and render groom assets.](/documentation/en-us/unreal-engine/setting-up-a-project-for-grooms-in-unreal-engine)
%working-with-content/hair-rendering/groom-platform-support:Topic%
[![Importing Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/04a157fc-f6ce-4fc2-895b-9c239f736bb1/placeholder_topic.png)

Importing Grooms

Learn about importing grooms into your project and about the groom importer settings.](/documentation/en-us/unreal-engine/importing-grooms-into-unreal-engine)
[![Groom Components and Assets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa4d2a00-1597-4470-911e-51072ee39a28/placeholder_topic.png)

Groom Components and Assets

The assets and components to use and render grooms.](/documentation/en-us/unreal-engine/groom-components-and-assets-in-unreal-engine)
[![Groom Asset Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/394d6c65-59ae-4ca6-81f2-132377cd8811/groom-editor-topic-image.png)

Groom Asset Editor

A reference and user guide for the managing attributes and editing Groom Assets.](/documentation/en-us/unreal-engine/groom-asset-editor-user-guide-in-unreal-engine)
[![Hair Card Generator](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/865b4acd-1660-49e6-97f3-0ad8f2d900a5/groom-card-strands-example.png)

Hair Card Generator

Overview of using the hair card generator plugin to create card grooms.](/documentation/en-us/unreal-engine/hair-card-generator-for-grooms-in-unreal-engine)

## Additional Topics

[![Groom Strands](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e43a1d4d-2aa7-4324-95ad-782ba715f9a5/placeholder_topic.png)

Groom Strands

Configure settings for strand geometry.](/documentation/en-us/unreal-engine/groom-strands-in-unreal-engine)
[![Setting Up Bindings for Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c9a5437-0de3-40c3-8fab-dcf27a47ccd0/placeholder_topic.png)

Setting Up Bindings for Grooms

Learn how to bind groom components to skeletal meshes.](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine)
[![Groom Interpolation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d45458ef-cfc7-46c3-88bb-449366a28898/placeholder_topic.png)

Groom Interpolation

Define how a groom's curves should move with respect to skinned meshes and phyics simulation.](/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine)
[![Enabling Physics Simulation on Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c6019dc-661e-413d-81cd-f657fd7c3415/placeholder_topic.png)

Enabling Physics Simulation on Grooms

Learn how to enable and configure physics on grooms.](/documentation/en-us/unreal-engine/enabling-physics-simulation-on-grooms-in-unreal-engine)
[![Setting Up Level of Detail for Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9c0682c-d1fb-43be-a533-32d2dd025339/placeholder_topic.png)

Setting Up Level of Detail for Grooms

Learn how you can set up and manage level of detail groups for your grooms.](/documentation/en-us/unreal-engine/setting-up-level-of-detail-for-grooms-in-unreal-engine)
[![Setting Up Cards and Meshes for Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80f26adf-9f77-452c-ba1e-77378aea5fda/placeholder_topic.png)

Setting Up Cards and Meshes for Grooms

Set up and assign cards and meshes to levels of detail for your groom.](/documentation/en-us/unreal-engine/setting-up-cards-and-meshes-for-grooms-in-unreal-engine)
[![Groom Materials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c583d10-21d1-46e9-a6ae-6bdc6796a4d2/placeholder_topic.png)

Groom Materials

Manage materials for your grooms.](/documentation/en-us/unreal-engine/groom-materials-in-unreal-engine)
[![Generating Groom Textures](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2755eff4-8a8a-4603-9bfb-15545b6ab3b5/groom-textures-topic-image.png)

Generating Groom Textures

Create follicle and strands textures for groom assets.](/documentation/en-us/unreal-engine/generating-groom-textures-in-unreal-engine)
[![Setting Up A Groom Deformer Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97b087a7-5bf4-4632-8a6c-c02c090f99eb/placeholder_topic.png)

Setting Up A Groom Deformer Graph

Use deformer graphs to define groom behaviors with mesh deformations.](/documentation/en-us/unreal-engine/setting-up-a-groom-deformer-graph-in-unreal-engine)
[![Groom Caches](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23d7dbdc-ba8d-4165-b256-e2eb9556f775/placeholder_topic.png)

Groom Caches

An overview of using imported Groom Caches with grooms.](/documentation/en-us/unreal-engine/using-groom-caches-with-hair-in-unreal-engine)
[![Groom Scalability and Performance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8156d73-fed5-484c-957f-ccf97bc69736/placeholder_topic.png)

Groom Scalability and Performance

Learn about using scalability options for you grooms and optimizing them for your projects.](/documentation/en-us/unreal-engine/groom-scalability-and-performance-with-unreal-engine)
[![Debugging Grooms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/757ab409-3cbe-4faf-a1ad-334d48768e83/placeholder_topic.png)

Debugging Grooms

An overview of the ways in which you can debug grooms.](/documentation/en-us/unreal-engine/debugging-grooms-in-unreal-engine)
[![Alembic for Grooms Specification](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23288670-c4b0-4ea8-a72d-ca454a85534d/placeholder_topic.png)

Alembic for Grooms Specification

Describes guidelines for exporting Grooms as Alembic files for use with Unreal Engine.](/documentation/en-us/unreal-engine/using-alembic-for-grooms-in-unreal-engine)
[![XGen Guidelines for Groom Creation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1524ff9f-08e3-4f3f-9bc7-7967581bf6f6/placeholder_topic.png)

XGen Guidelines for Groom Creation

Describes guidelines for exporting grooms as Alembic files for use with Unreal Engine.](/documentation/en-us/unreal-engine/xgen-guidelines-for-hair-creation-in-unreal-engine)

## Additional Resources

* [MetaHuman Creator](https://www.unrealengine.com/metahuman)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine?application_version=5.7#gettingstarted)
* [Additional Topics](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine?application_version=5.7#additionaltopics)
* [Additional Resources](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine?application_version=5.7#additionalresources)
