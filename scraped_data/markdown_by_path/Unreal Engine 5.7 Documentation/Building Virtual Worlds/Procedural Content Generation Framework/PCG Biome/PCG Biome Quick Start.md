<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7 -->

# PCG Biome Quick Start

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
6. [Procedural Content Generation Framework](/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine "Procedural Content Generation Framework")
7. [PCG Biome](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-in-unreal-engine "PCG Biome")
8. PCG Biome Quick Start

# PCG Biome Quick Start

Learn how to use the PCG framework with the PCG Biome Core and Sample Plugins.

![PCG Biome Quick Start](https://dev.epicgames.com/community/api/documentation/image/d6d570da-f150-475d-8ec8-ec00cde526ad?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

The PCG Biome Core and Sample Plugins are examples of how to use the  [PCG Framework](building-virtual-worlds/procedural-generation/procedural-content-generation-overview) with features like Attribute Set Tables, Feedback loops, Recursive Sub-graphs and [Runtime Hierarchical Generation](building-virtual-worlds/procedural-generation/pcg-development-guides/using-pcg-generation-modes).

This quick start guide explains how to use the biome creation tool from scratch, followed by instructions on how to add new biomes and assets.

## Requirements

This section covers the requirements and steps required to get the PCG Biome Core working in a world.

## Enabling Plugins

The PCG Biome Core and PCG Biome Sample are two distinct plugins:

* **PCG Biome Core**: A standalone plugin that contains only what is required for the biome creation tool to work. This plugin has a dependency on the **PCG Framework** and **PCG Geometry Script Interop** plugins.
* **PCG Biome Sample**: A content example showcasing the biome creation tool, which can be enabled in any project. This plugin has a dependency on the **PCG Biome Core** plugin.

To enable the plugins, open the Plugins settings. Enable **PCG Biome Core** to access the tool, and enable the **PCG Biome Sample** to access the content example. For more information on enabling plugins, see [Working with Plugins](understanding-the-basics/customizing-unreal-engine/working-with-plugins).

[![The PCG Biome Core and PCG Biome Sample plugins in the Plugin settings.](https://dev.epicgames.com/community/api/documentation/image/a956a151-e3a2-4d69-8411-b5ff39cdc6c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a956a151-e3a2-4d69-8411-b5ff39cdc6c4?resizing_type=fit)

## Resources

To access all the content related to both the PCG Biome Core and Sample plugins, the **Show Engine Content** and **Show Plugin Content** content browser settings must be enabled. Open the **Settings** menu in the **Content Browser** and click the checkbox next to both options.

[![The Show Engine Content and Show Plugin Content checkboxes.](https://dev.epicgames.com/community/api/documentation/image/7acbcba2-4f41-4758-80c1-efcf33c06377?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7acbcba2-4f41-4758-80c1-efcf33c06377?resizing_type=fit)

[![The PCG Biome Core and Sample plugin content visible in the Content Browser.](https://dev.epicgames.com/community/api/documentation/image/3785b1db-8fba-4f63-82a2-87cb5ca055bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3785b1db-8fba-4f63-82a2-87cb5ca055bb?resizing_type=fit)

Content Browser paths:

* `/All/EngineData/Plugins/PCGBiomeCore`
* `/All/EngineData/Plugins/PCGBiomeSample`

Disk paths:

* `..\Engine\Plugins\Experimental\PCGBiomeCore\`
* `..\Engine\Plugins\Experimental\PCGBiomeSample\`

## PCG Biome Core Content

All the base blueprint classes are located in the following folder: `/All/EngineData/Plugins/PCGBiomeCore/Blueprints`

[![The Blueprints folder.](https://dev.epicgames.com/community/api/documentation/image/46bf2e8b-69b2-4194-9514-e3b3176b9d85?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46bf2e8b-69b2-4194-9514-e3b3176b9d85?resizing_type=fit)

The **BP\_PCGBiomeCore** is the main blueprint class. It is pre-configured with a PCG component that refers to the Biome Core PCG graph and holds a box collision component as its volume.

The Biome Core PCG graph located at the plugin's root is the source and main graph to execute all logic for the Biome Core to work. It contains multiple subgraphs with their own nested subgraphs. All of these separate subgraphs are stored under the `Core` folder.

The Biome Core graph is located at the following path: `/Script/PCG.PCGGraph'/PCGBiomeCore/BiomeCore.BiomeCore'`

The tool relies on multiple data assets made from pre-made classes with specific structures to generate content. These assets are **BiomeDefinitions**, **BiomeAssets** and **BiomeGenerators**. They are located in their respective folders and `../Setup` sub-folders. The default assets of each type are also available for testing and debugging.

### PCG Biome Sample Content

The **BiomeSampleLevel** world is located in the following folder: `/All/EngineData/Plugins/PCGBiomeSample/Maps`

[![The BiomeSampleLevel in the Maps folder.](https://dev.epicgames.com/community/api/documentation/image/505918e9-582c-4ffb-89dc-5ef56e86506b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/505918e9-582c-4ffb-89dc-5ef56e86506b?resizing_type=fit)

The world contains the pre-configured **BP\_PCGBiomeCore**, biome textures, volume, and spline actors. Use this as a starting point to learn how to set up the tool and understand it.

The sample contains multiple biomes, generators, and assets as well as custom structures and data assets classes that inherit from the base Biome Core classes. These assets are located in their respective `BiomeSample` folders and `../Setup` sub-folders.

The PCG Biome Sample plugin contains additional data, including a BiomeMaptexture, a tiled Flow, and a SunExposure texture2Darray, located in the Tiles folder. The Sample plugin also includes example PCG assemblies, meshes, and filter graph instances.

## World Setup

To set up a world and start using the PCG Biome Core, follow these steps:

1. Create a new level or open an existing world. The PCG Biome Core works with both [World Partitioned](building-virtual-worlds/world-partition) and non-partitioned levels.
2. Add a new Landscape and set the world scale through the Landscape Editor mode. If you are starting from the Open World template or any existing level with an existing landscape, this step is not required.

   The presence of a landscape is **optional** when working with the PCG Biome Core.
3. Add or drag a **BP\_PCGBiomeCore** actor into the level. The provided BP\_PCGBiomeCore blueprint class is located in the following folder: `/Script/Engine.Blueprint'/PCGBiomeCore/Blueprints/BP_PCGBiomeCore.BP_PCGBiomeCore'`
4. Adjust the BP\_PCGBiomeCore actor's **Volume** component scale to change the world coverage. The tool uses this volume to constrain its generation and output.

The next section explains how to place a Biome actor that generates and spawns assets in the Biome Core volume.

## Biomes, Generators, and Assets Setup

After the original world setup is done and validated, you can create a new biome with its definition and assets.

To create a new biome, add or drag a new **BP\_PCGBiomeVolume** or **BP\_PCGBiomeSpline** actor into the world. The actor must be added within the Biome Core actor volume, and must be overlapping the landscape surface.

The blueprint classes are available in the following folders:

* `/Script/Engine.Blueprint'/PCGBiomeCore/Blueprints/BP_PCGBiomeVolume.BP_PCGBiomeVolume'`
* `/Script/Engine.Blueprint'/PCGBiomeCore/Blueprints/BP_PCGBiomeSpline.BP_PCGBiomeSpline'`

[![The volume and spline Blueprint classes.](https://dev.epicgames.com/community/api/documentation/image/10161d56-443c-4a1c-a7d9-45baad8fd2fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10161d56-443c-4a1c-a7d9-45baad8fd2fd?resizing_type=fit)

Next, you need to create a set of data assets for the biome definition, generators, and assets. Data assets can be added from the Content Browser, from the right-click menu, or by duplicating existing assets of the same class.

In Unreal Engine 5.6 and later, biome actors support local biome assets and a local default biome definition that is saved in the actor directly. This removes the need for separate data assets for biome definitions and biome assets. Having separate assets is still supported, and can be used for sharing and maintenance when working with multiple levels or instances.

### Set the Biome Definition

To set the Biome definition, open the **BP\_PCGBiomeVolume** asset and set the **BiomeName**, **BiomeColor**, and **BiomePriority** properties. This sets the default definition for the biome.

[![The default definition for a Biome volume asset.](https://dev.epicgames.com/community/api/documentation/image/af86c0c4-4438-4b09-b014-b5039745e0c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af86c0c4-4438-4b09-b014-b5039745e0c0?resizing_type=fit)

Optionally, you can overwrite the default definition by creating a separate data asset, following these steps:

1. Add a data asset of class **BiomeDefinitionTemplate** to the project’s content folder.
2. Open the data asset and set the **BiomeName**, **BiomeColor**, and **BiomePriority** properties.
3. Open the **BP\_PCGBiomeVolume** asset and set the **Definition** property to refer to the definition data asset you created in step 1. This overwrites the default definition of the volume asset.

The definition asset can be shared and re-used in multiple biome volumes, splines, and worlds.

For more information about biome definitions, see [Biome Definition](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine#biome-definition).

### Create a Biome Generator

To create a biome generator, add a new data asset of class **BiomeGeneratorTemplate** in the project’s content folder, and set its **GeneratorType**, **GeneratorPriority**, and **GeneratorGraph** properties.

[![The properties of a Biome generator.](https://dev.epicgames.com/community/api/documentation/image/b1075b05-448a-42bc-8c6c-cb6af8aee627?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1075b05-448a-42bc-8c6c-cb6af8aee627?resizing_type=fit)

These properties define your generator. The generator asset can and should be shared and re-used in multiple assets, as it provides the initial point data from a linked **GeneratorGraph** on which to assign and spawn assets.

The **GeneratorGraph** is a PCG graph or PCG graph instance, which creates and outputs point data created by sampling the world through world ray hit or raycasts.

To set the **GeneratorGraph** property, create a new PCG graph using the **TPL\_BiomeCore\_Generator** template, or copy it from the following folder:

`/Script/PCG.PCGGraph'/PCGBiomeCore/GraphTemplates/TPL_BiomeCore_Generator.TPL_BiomeCore_Generator'`

[![The generator graph template.](https://dev.epicgames.com/community/api/documentation/image/6493d1f7-ce27-4e4a-adcc-7db29deacd44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6493d1f7-ce27-4e4a-adcc-7db29deacd44?resizing_type=fit)

For more information about Biome generators, see [Biome Generator](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.6#generators).

### Create a Biome Asset

To create a Biome asset, open the **BP\_PCGBiomeVolume** asset and add an entry to the **Local Assets** array property. Set the asset's **Generator** property, a mandatory reference to the biome generator data asset created above, and set the **Mesh** property, a reference to the visual to spawn.

Optionally, you can create and add a separate data asset, following these steps:

1. Add a new separate data asset of class **BiomeAssetTemplate** in the project’s content folder.
2. Open the data asset.
3. Add an entry to the **Biome Assets** array property and set its **Generator** and **Mesh** properties.
4. Open the **BP\_PCGBiomeVolume** asset.
5. Refer to the data asset as a new entry to the **Assets** array property.

All local assets and assets references are combined together when generating the local biome.

In the data asset, the **Biome Assets** array is the collection of assets to process and spawn. Each entry contains multiple properties to configure. Assets sharing the same generator reference use the same point data to spawn on and will be distributed randomly onto the generated points according to their weight value. The biome assets can be shared and re-used easily across any biomes.

[![The Generator and Mesh properties in a Biome Assets array entry.](https://dev.epicgames.com/community/api/documentation/image/83c694c8-ef1d-4314-9628-de3fe9b38378?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/83c694c8-ef1d-4314-9628-de3fe9b38378?resizing_type=fit)

For more information about biome assets, see [Biome Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.6#biome-assets-and-structures).

### Biome Generation

After setting up a biome definition, biome generator, and biome asset, an automatic refresh occurs. A new biome is created by spawning the defined assets constrained within the BP\_PCGBiomeVolume and the Biome Core volume.

You can now extend the biome with more generators and assets. Any number of biomes can be created using the same process and exist in the same world or across multiple worlds. See the **BiomeSampleLevel** in the **PCGBiomeSample** plugin for a complete setup.

For reference, in the following image, a biome volume actor has been configured with multiple assets referencing and sharing only 2 custom generators, one for trees and one for rocks.

[![Screenshot of a single biome filled with rocks and trees.](https://dev.epicgames.com/community/api/documentation/image/d7f9bae1-2956-403f-a5da-a810ce3479fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7f9bae1-2956-403f-a5da-a810ce3479fd?resizing_type=fit)

In the following example, several biome spline actors with their respective assets and priorities are overlapping and fades out using a 64m blending range.

[![Screenshot of five overlapping biomes filled with various levels of trees and rocks.](https://dev.epicgames.com/community/api/documentation/image/4e669c42-9261-40a9-bb42-83030b7f9471?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e669c42-9261-40a9-bb42-83030b7f9471?resizing_type=fit)

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [procedural generation](https://dev.epicgames.com/community/search?query=procedural%20generation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Requirements](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#requirements)
* [Enabling Plugins](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#enablingplugins)
* [Resources](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#resources)
* [PCG Biome Core Content](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#pcgbiomecorecontent)
* [PCG Biome Sample Content](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#pcgbiomesamplecontent)
* [World Setup](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#worldsetup)
* [Biomes, Generators, and Assets Setup](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#biomes,generators,andassetssetup)
* [Set the Biome Definition](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#setthebiomedefinition)
* [Create a Biome Generator](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#createabiomegenerator)
* [Create a Biome Asset](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#createabiomeasset)
* [Biome Generation](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-quick-start-guide-in-unreal-engine?application_version=5.7#biomegeneration)
