<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine?application_version=5.7 -->

# Working with Content

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
5. Working with Content

# Working with Content

Information on using art created in external applications, importing it into Unreal Engine, and setting it up for use in visualization and interactive applications.

![Working with Content](https://dev.epicgames.com/community/api/documentation/image/87a57669-78b5-47f2-9723-3bfd93050588?resizing_type=fill&width=1920&height=335)

 On this page

Most of the artistic assets that you will use in Unreal Engine are created using external 3D applications, such as 3ds Max, Maya, Quixel, ZBrush, and others. Below, you will find information on the types of assets that are created externally and what tools are available for bringing them into the engine.

| Asset Creation Locations |  |
| --- | --- |
| Created in Unreal Editor | Created Using External Application |
| * Game Levels * Materials * Particle Systems * Cinematic Sequences * Blueprint Scripts * AI Navigation Meshes * Precalculated Light Maps * Level Lights | * Static Meshes * Skeletal Meshes * Skeletal Animation * Textures * Sounds (WAVs) * IES Light Profiles * NVIDIA APEX files (APB and APX) |

## Starting Out

[![Artist Quick Start](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47638e2b-ccde-44d1-a245-1292061413d0/topic-image.png)

Artist Quick Start

Learn how to get started with Unreal Engine 5 as a content creator.](/documentation/en-us/unreal-engine/artist-quick-start-in-unreal-engine)

## Content Guides

[![Skeletal Meshes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53f86d4d-4b9d-4002-a46e-f28b2eb3ea55/topicimage.png)

Skeletal Meshes

Create characters in Unreal Engine using Skeletal Mesh assets.](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine)
[![Alembic File Importer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0cd5f98-c825-4d02-93c4-bc1f996a8aaa/alembictopicimage.png)

Alembic File Importer

Describes the Alembic File import process along with import options.](/documentation/en-us/unreal-engine/alembic-file-importer-in-unreal-engine)
[![FBX Content Pipeline](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/176b21e4-7c34-4e95-b865-21097d4fdffb/topic-image.png)

FBX Content Pipeline

Information on using the FBX content import pipeline for meshes, animations, materials, and textures.](/documentation/en-us/unreal-engine/fbx-content-pipeline)
[![Hair Rendering and Simulation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b7e1c73-0fbf-4534-9876-4d8e6bb08d17/placeholder_topic.png)

Hair Rendering and Simulation

Information on rendering, simulation, creation, and editing of hair grooms in Unreal Engine.](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine)
[![Interchange Framework](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efd751a3-b2c1-4aaf-bf27-91b075d25509/topic-image.png)

Interchange Framework

Information on importing and exporting content using the Interchange Framework](/documentation/en-us/unreal-engine/interchange-framework-in-unreal-engine)
[![Static Meshes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24048c81-1ff6-405b-87f4-9946ba053cb2/topic-image.png)

Static Meshes

Information on importing and working with Static Mesh assets in Unreal Engine.](/documentation/en-us/unreal-engine/static-meshes)
[![Mutable Skeletal Mesh Generation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69d51d45-a9a8-497c-bb49-8b98a28bc4ff/topic-image.png)

Mutable Skeletal Mesh Generation

An introduction to Mutable, a toolset that generates dynamic skeletal meshes, materials, and textures at runtime.](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine)
[![GL Transmission Format (glTF)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7afcdaec-8c74-443d-abf4-acfee4cef104/placeholder_topic.png)

GL Transmission Format (glTF)

Importing and Exporting Unreal Engine Content using the glTF file format](/documentation/en-us/unreal-engine/the-gl-transmission-format-gltf-in-unreal-engine)
[![Universal Scene Description (USD)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/33f251f4-0aaf-4cf6-8613-6915e9181a6b/5-0-usd-landing-page-topic.png)

Universal Scene Description (USD)

Importing and Editing Content using Universal Scene Description (USD) in Unreal Engine](/documentation/en-us/unreal-engine/universal-scene-description-usd-in-unreal-engine)
[![LiDAR Point Cloud Plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d144371a-ca4c-411a-9289-025226750410/topic-image.png)

LiDAR Point Cloud Plugin

Use the LiDAR Point Cloud Plugin to import LiDAR point clouds into Unreal Engine.](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-for-unreal-engine)
[![Modeling and Geometry Scripting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/349ebb48-a2dd-4f82-adf6-2933557e45f3/topic-image.png)

Modeling and Geometry Scripting

Tools for modeling in-engine.](/documentation/en-us/unreal-engine/modeling-and-geometry-scripting-in-unreal-engine)
[![Working with Scene Variants](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1462929-6738-44ae-813f-e355823b5cd6/variants-topic.png)

Working with Scene Variants

The Variant Manager can help you switch between different representations of your scene.](/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine)
[![SpeedTree](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8a242ad-3e0e-4705-bbf5-8845c7ed0830/placeholder_topic.png)

SpeedTree

The landing page for using SpeedTree with Unreal Engine.](/documentation/en-us/unreal-engine/using-speedtree-in-unreal-engine)
[![Localization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/629130aa-b00b-46ab-a47b-f31e187efa72/placeholder_topic.png)

Localization

Information about how to localize your project for different regions and cultures.](/documentation/en-us/unreal-engine/localizing-content-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Starting Out](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine?application_version=5.7#startingout)
* [Content Guides](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine?application_version=5.7#contentguides)
