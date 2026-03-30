<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-glossary-in-unreal-engine?application_version=5.7 -->

# PCG Biome Glossary

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
8. PCG Biome Glossary

# PCG Biome Glossary

Learn the terms used when working with the PCG Biome Core and Sample Plugins.

![PCG Biome Glossary](https://dev.epicgames.com/community/api/documentation/image/1b3d5d03-d53e-4f0f-a517-283a671f0447?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

The PCG Biome Core and Sample Plugins are examples of how to use the [PCG Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview). This page provides definitions for many of the terms used in the documentation for this project.

Assembly (PCG)
:   PCG point data created and exported from all static meshes and instanced static meshes found in a level, using the **Asset Action > Create PCG Assets from Level(s)**.

Biome
:   A volume in space defined by a biome definition and a list of biome assets.

Biome Actors
:   Blueprint actors that are used to set up biomes in a world. These include biome volumes, biome splines, and biome textures.

Biome Assets
:   Data assets that contain asset properties to be spawned by Biome Core.

Biome Core
:   A data-driven biome creation tool that provides a fixed pipeline with customizable steps. The PCG Biome Core plugin contains a collection of PCG graphs and sub-graphs used to procedurally generate biomes.

Biome Core Runtime
:   A separate PCG component and graph, used for GPU runtime generation of detailed assets spawning around the camera.

Biome Sample
:   The PCG Biome Sample plugin contains a level, data assets and custom PCG graphs used to showcase procedural biome generation using Biome Core.

Child Points
:   All points created from the recursive transform step to spawn child assets.

Filter Graph
:   A PCG Graph that processes points and writes to a defined filter attribute from its logic or texture projection.

Filters
:   A list of filter graphs.

Generator
:   A data asset with **Type**, **Priority**, and **Generator Graph** properties, referred to by biome assets entries.

Generator Graph
:   A PCG Graph that produces root points used for placing assets in the world.

Global Biome Core Graph
:   On the Biome Core BP actor, the PCG component has the Biome Core graph assigned to it. When executed, the graph gets all data produced by all local Biome Core graphs in each Biome actor. The data goes through a difference by priority step, then spawns the remaining points as static meshes, assemblies, or actors.

Global parameters
:   Graph parameters on the global Biome Core that impact its global behavior. Includes filter graphs and the debug cache display.

Hierarchical Generation
:   Subdivides the volume and processing into multiple grids of different size at which parts of a PCG graph executes. Hierarchical Generation speeds up local updates by distributing computing at different grid sizes and outputs data into separate actors that can be streamed in individually. For more information, see [Using PCG Generation Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.5).

Injected Data
:   External data injected at different stages of the Biome Core to exclude or add points. Divided in different types based on their entry point within the pipeline: exclusions and custom biome data.

Local Biome Cache
:   Point data computed locally for each biome actor and used as the bounding shape for generators used in the biome. The local cache is also used to apply the biome definition onto the produced points.

Local Biome Core Graph
:   Each biome actor has its own PCG component and a local Biome Core graph assigned to it. The local Biome Core graph generates all data locally per biome actor. The output of that local generation is then used in the global Biome Core graph.

Local parameters
:   Graph parameters in the local Biome Core that impact its local behavior. Includes preview mode, debug local cache display, and biome blending controls. Partitioning Biome Core graph parameters that impact its global behavior. Includes filter graphs and the debug cache display.

Root Points
:   All points provided by the generators and their graphs.

Runtime Assets
:   A data asset containing properties of assets to be spawned by Biome Core runtime.

Runtime Hierarchical Generation
:   Generates grid cells at runtime based on streaming source or PCG generation source components. Uses the generation radius of each grid size configured in the PCG Graph. Uses the same multi-level grid size approach as the Hierarchical Generation. For more information, see [Using PCG Generation Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.5).

Transform Graph
:   A PCG Graph that takes points from a generator or parent transformed points to change their properties. Used for generating and placing child points.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [procedural generation](https://dev.epicgames.com/community/search?query=procedural%20generation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
