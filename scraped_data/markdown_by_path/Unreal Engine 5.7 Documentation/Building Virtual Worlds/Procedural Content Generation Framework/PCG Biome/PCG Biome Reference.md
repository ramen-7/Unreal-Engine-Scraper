<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7 -->

# PCG Biome Reference

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
4. PCG Biome Reference

# PCG Biome Reference

Learn how to use the PCG framework with the PCG Biome Core and Sample Plugins.

![PCG Biome Reference](https://dev.epicgames.com/community/api/documentation/image/d95f023c-8e23-4a1f-bc8e-1cc827121e1e?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## Reference

### Core Graphs Overview

The PCG Biome Core plugin uses two main graphs: a local Biome Core graph and a global Biome Core graph. Point data is defined and generated locally for each Biome Actor. The local Biome Core PCG graph executes and produces point data per biome actor. These points are then used in the global Biome Core, which applies the differences between all incoming points then only updates and spawns modified point data.

#### Local Biome Core Graph

The local Biome Core graph is responsible to generate and output all point data locally for each individual biome actor. The data produced will then be used in the global Biome Core graph for spawning.

The local Biome Core graph performs these main processing steps:

1. Compute the Local Biome Cache using a specific cache graph based on the biome actor type (volume, spline, texture).
2. The Local Root Asset Table combines all biome assets references and local biome assets on self into an attribute set table.
3. Process the generator graphs, referenced by Biome Assets and Local Assets on self, are processed and bound by the local biome cache, which produces a unique root point data per generator used. The biome definition is also directly applied during this step.
4. Assign the Root Asset Table attributes, such as the Mesh to spawn, to each point based on the generator type, subtype, and weighting.
5. Apply filters using the PCG graphs provided by the Root Points Filters parameter of the Local Biome Core PCG Component.
6. Apply recursive transforms per asset using their transform graph and child asset reference. Through this hierarchy of asset reference, child points data can be created for each root point and limited with the maximum depth parameter.
7. Load the assemblies instancer step, which copies assembly points on each generated points with an assembly assigned, and applies transformation to each point.
8. Send the output data to the global Biome Core.

### Global Biome Core Graph

The global Biome Core graph is the brain of the biome creation tool and where all processing is made using the PCG Framework.

The global Biome Core graph performs the following processing steps:

1. Get all local biome core data from all overlapping biome actors and apply sorting based on priority.
2. Perform a priority-based difference operation between each point data set is performed from all biomes. The **Biome Priority** and then **Generator Priority** property determines the order of operation and can be bypassed optionally.
3. Spawn static meshes and actors, including support for property overrides, assemblies, and collision presets.
4. Output the data to Biome Core runtime, which can be enabled in the global parameters.

### High Level Concepts

#### Biome and Asset Mapping

Each biome actor is unique and generated locally with its own definition and assets. When biome actors share the same data assets, changes applied to these assets trigger updates for each biome actor referencing them. Local assets and the local **Default Definition** on each actor can be used to build unique biomes without any data assets associated with them.

You can create child Blueprint classes of pre-configured biome volumes, splines, and textures for a project. Child Blueprint classes can be reused for instancing biomes in the same level or across multiple worlds. Then, by updating these child classes, you can adjust all of these biomes at the same time.

#### Biome Cache (Local Biome Core)

[![A preview of the Local Biome Cache point data.](https://dev.epicgames.com/community/api/documentation/image/7778856e-2aa7-4ae8-8a3b-88c04bf4eedd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7778856e-2aa7-4ae8-8a3b-88c04bf4eedd?resizing_type=fit)

The l**ocal biome cache** is point data computed locally for each biome actor and is used as the bounding shape for generators used in the biome. The local cache is also used to apply biome definition onto the produced points.

Biome definition colors associated with biome volumes, biome splines, and biome textures are used when previewing the cache, and to find matching colors when using the biome texture actor class.rThe local biome cache is a 3D point data, so you can place biomes anywhere in 3D space, such as stacking biomes on top of each other, or creating underground caves. To use the local biome cache in 2D, provide tall, column-like points using the Z Extents properties on the biome actor.

The cache resolution is controlled by the **Local Cache Size** properties on spline and texture biome actors. Volumes produce a single point matching the volume bounds.

When generating points using surface samplers in generator graphs, the local biome cache is used as a bounding shape to avoid sampling the landscape or other surfaces in parts of the world where the biomes are not using the generators.

#### Root Asset Table (Local Biome Core)

[![The root asset table.](https://dev.epicgames.com/community/api/documentation/image/bb4f68fa-b882-44d7-8262-ccd9fe30e195?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb4f68fa-b882-44d7-8262-ccd9fe30e195?resizing_type=fit)

**Root assets** are at the top level of the asset hierarchies. They are provided by data assets assigned to biome setups, volumes, or splines and contain properties such as generator, mesh, transform, bounds, rendering and collision options.

These assets properties are stored in a PCG Attribute Set table called the **root asset table**. Each entry in the table is identified using its unique **AssetID** attribute.

Once generated, points produced by generator graphs are given an **AssetID** attribute corresponding to their entry in the local root asset table.

The local root asset table simplifies and optimizes the point attributes layout by not directly assigning all properties from an asset to each generated point. Each point only needs an **AssetID**. Other attributes can be accessed from the root asset table as needed.

#### Generators (Local Biome Core)

[![The Blueprint graph of a generator.](https://dev.epicgames.com/community/api/documentation/image/862f319f-1640-4c5a-bbcc-cf5bcc5a1f8d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/862f319f-1640-4c5a-bbcc-cf5bcc5a1f8d?resizing_type=fit)

[![PCG Biome Reference](https://dev.epicgames.com/community/api/documentation/image/f5bd698a-cbda-41c2-acd9-7bae1898b9a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5bd698a-cbda-41c2-acd9-7bae1898b9a6?resizing_type=fit)

PCG Biome Reference

Generators are the root points providers and mandatory for the system to work.

**Biome generator data assets** are required to provide the following:

* a Generator Type as a unique name identifier
* Generator Graphs, which are run by the Biome Core to output points on which Biome Assets will be assigned to
* a **Generator Priority**

Generator graphs are standalone PCG graphs built for any kind of needs with any custom logic. Use PCG graph instances of Generator Graphs to customize the graph parameters without having to build new custom graphs for each similar case. You can start from the provided template **TPL\_BiomeCore\_Generator** through the new graph template selection, or copy the graph in the following folder: `/Script/PCG.PCGGraph'/PCGBiomeCore/GraphTemplates/TPL_BiomeCore_Generator.TPL_BiomeCore_Generator'`

The **Generator Priority** property is used for layering. It is used when applying the priority-based difference to order the layering of multiple generators against each other. Lower priority values indicate a higher priority. The difference by priority between generated point data is performed after assets have been assigned to each point, allowing access to the mesh bounds during these difference operations. Optionally, you can bypass difference by priority in the biome generator asset by enabling the GeneratorAllowOverlap option.

Each entry in the **Biome Assets** array has a reference to a generator. This link is necessary to define which point data the asset is assigned to. Biome assets can also be mapped to generator subtypes, which is covered in the advanced setup section. Here are some examples of how you can map biome assets to generator subtypes:

* Generate points for trees and rocks from landscape sampling with different graph instance parameter values while sharing the same source graph. The rocks generator is set with priority 0 and trees with priority 1. The trees will be automatically removed when their bounds overlap with rocks.
* Generate points for spawning POI assemblies in flat areas over static meshes by sampling the geometry surface using World Ray Hit Query.
* Produce points near the border of a lake or river spline and reproject them onto the landscape.
* Create points for Niagara systems or Sounds volumes matching the biome.

#### Filtering (Local Biome Core)

In addition to the layering performed during the priority-based difference, both root and child points can be filtered from a customizable list of compute graphs or texture projections. By default, the Biome Core actor is configured with **Height** and **Density**filters. **Biome Assets Filter Options** include ranges for each of these default filters.

The Density filter is based on density set from generator, transform or filter graphs on the points’ `$Density` property, so you can use any computation that writes to `$Density`. The Height filter uses the points' `$Position.z` property.

The filtering steps for root and child points in the Biome Core use the dynamic graph feature. The graph being executed can then be parameterized with an array of dynamic subgraphs. For information on how to define the filters array, create filter graphs, and customize filter options structure, see [Filters](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine#filters).

The Biome Sample example is set up with extra texture projection filters and custom Filter Options. The two provided textures, Flow and Sun Exposure, are both 2D texture arrays, which are projected per-tile and then filtered from their respective minimum and maximum values.

[![](https://dev.epicgames.com/community/api/documentation/image/bb8e74d9-da5c-4a85-a469-bcaf96b7dc5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb8e74d9-da5c-4a85-a469-bcaf96b7dc5e?resizing_type=fit)

Debug display of the flow map projection.

[![](https://dev.epicgames.com/community/api/documentation/image/12759610-96cf-40ea-a384-06d694091470?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12759610-96cf-40ea-a384-06d694091470?resizing_type=fit)

Filtering an asset from 0 to 0.33 from the flow map projection.

[![](https://dev.epicgames.com/community/api/documentation/image/d7b49ba9-beff-4411-b7c8-ca328a1e79cb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7b49ba9-beff-4411-b7c8-ca328a1e79cb?resizing_type=fit)

Filtering an asset from 0.66 to 1 from the flow map projection.

#### Recursion and Transform (Local Biome Core)

[![](https://dev.epicgames.com/community/api/documentation/image/40b5625d-8f02-4a12-9eeb-81b50b2a63ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40b5625d-8f02-4a12-9eeb-81b50b2a63ad?resizing_type=fit)

The BiomeCore\_ChildTransformLoop subgraph calling itself.

Root assets can have child assets. Child assets share the same asset type as their parents and can themselves have children, forming a hierarchy of assets. Unlike root assets, child assets are not generated using generator graphs. They use their parent points as input and generate their final points using transform graphs.

All assets of all hierarchy levels, including the root assets, can have their input points changed by transform graphs.

Transform graphs are PCG graphs assigned to assets. These graphs take point data from their parent as input, either from the generator graph of a root asset, or from the transform graph output of a parent asset.

Starting from their input points, transform graphs can do any operation provided by the PCG framework, like duplicate, copy points, sampling and project points. This is particularly useful when placing child assets.

To place all child assets in a hierarchy, use the recursive subgraph feature of PCG. For any given set of point, by asset, the process is as follows:

* Run the transform graph over the set of points to duplicate or change their position (the child placement pattern)
* Apply scale and bounds
* (Optional) Apply self pruning
* Assign mesh, material, mesh property overrides, assembly, and actor attributes for final asset spawning
* Output the points for spawning
* Resolve potential child assets from the current asset
* Feed resulting points and child assets to the same subgraph. This process will run recursively until no child asset and no input or parent point is found, or until the **Max Child Asset Depth** property of the local Biome Core graph is reached.

To control the performance of the recursive generation, there is a limit to the number of parent points allowed to emit child points. This limit is controlled by the **Child Input Points Rate Multiplier** property of the local Biome Core graph in each biome actor.

An asset can emit multiple child assets at the same level of recursion. When sharing the same parent, child assets distribution is weighted using the weight property of each child asset.

#### Priority-Based Difference (Global Biome Core)

The difference operation uses the **Biome Priority** in the biome definition and the **Generator Priority** priority in the generator asset to layer together the points generated for each biome, recursive transforms loop, and assembly instancing. The layering occurs when each point data is processed in the **Biome Core Difference By Priority** feedback loop. The data is ordered from the most important (smallest biome and generator priority value) to the least important (highest biome and generator priority value).

[![The priority-based difference section of the global Biome Core graph.](https://dev.epicgames.com/community/api/documentation/image/50ed24b8-5f63-4307-8b49-33d665676bdd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50ed24b8-5f63-4307-8b49-33d665676bdd?resizing_type=fit)

In the feedback loop graph, a binary difference is applied sequentially between the incoming data of the current iteration and the remaining points from previous loop iterations. After the loop completes, no points will overlap, unless the generators had identical priority values, or the **Generator Allow Overlap** property was enabled. Input point bounds are matching the assigned asset mesh or assembly bounds, and can be overridden in the asset options for better control.

[![](https://dev.epicgames.com/community/api/documentation/image/7e783912-d2dc-4565-8454-c585ba618347?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e783912-d2dc-4565-8454-c585ba618347?resizing_type=fit)

The layering between the higher generator priority Rocks (in red) removes overlapping Trees.

[![](https://dev.epicgames.com/community/api/documentation/image/bc8584b8-8b45-4945-ba51-c35e5c03e837?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc8584b8-8b45-4945-ba51-c35e5c03e837?resizing_type=fit)

The layering has been bypassed using the GeneratorAllowOverlap option, resulting in overlapping rocks and trees.

#### Spawning (Global Biome Core)

After the points have their final transforms and mesh, actor, and assembly attributes, they are ready for the actor and mesh spawning step.

The spawning step includes the 3 following methods that can be used non-exclusively:

1. An actor is spawned for each point, using a **SoftClassPath** point attribute to indicate which actor class to spawn.
2. For static meshes**,** the mesh **SoftObjectPath** attribute is used to specify the mesh to be spawned by each point using ISM Components. A list of property overrides is used to apply various static mesh component properties per point, including the following:

   * bUseDefaultCollision
   * bCastShadow
   * bCastHiddenShadow
   * DetailMode
   * InstanceStartCullDistance and InstanceEndCullDistance
   * WorldPositionOffsetDisableDistance
   * bIncludeInHLOD
   * bVisible
   * bAffectDistanceFieldLighting
3. For assemblies, each assembly is resolved as point data in each local Biome Core and spawned using ISM Components. Apply hierarchy and tag overrides are available for all instances in a PCG data asset assembly, to match the overrides for static meshes

#### Output to Biome Core Runtime (Global Biome Core)

The **output to runtime generation** is an optional step that outputs data from the global Biome Core graph, which the Biome Core runtime graph uses for runtime generation of detailed assets around the camera.

[![A scene that uses runtime generation to show detailed assets around the camera.](https://dev.epicgames.com/community/api/documentation/image/4a40b249-da20-4c12-a531-9d9482cc21a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a40b249-da20-4c12-a531-9d9482cc21a0?resizing_type=fit)

This feature showcases the **graph to graph** communication capabilities of PCG and can be described as follows:

* PCG Data from the graph is passed through the **Output** node to be serialized into the global Biome Core PCG component.
* Other graphs can access this data using a **Get PCG Component Data** node.
* The Biome Core runtime accesses and uses the data from the global Biome Core graph and component at runtime.
* Multiple data sets can be exported and serialized simultaneously by a graph, using multiple named pins. When accessing the data from a different graph using the **Get PCG Component Data** node, an **Expected Pins** array must be provided, with pin names matching the **Output** pin names of the graph providing the data.

[![](https://dev.epicgames.com/community/api/documentation/image/16dc4c7e-d783-4ab4-934b-d2af184ab14a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16dc4c7e-d783-4ab4-934b-d2af184ab14a?resizing_type=fit)

Data exported from BiomeCore using multiple pins.

[![](https://dev.epicgames.com/community/api/documentation/image/98e3fc62-9813-4495-b523-b81ef5954263?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98e3fc62-9813-4495-b523-b81ef5954263?resizing_type=fit)

The corresponding Get PCG Component Data node in the Biome Core runtime.

The Biome Core runtime has the following main features:

* Spawning points on the landscape or RVT through GPU runtime custom HLSL kernel
* Spawning points on meshes spawned by the global Biome Core
* Using global Biome Core points as influences to attract or repulse runtime-generated points
* Layering, blending and weighting runtime assets

The runtime generation of detailed assets using this data is described in the [Biome Core Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine#biome-core-runtime) section.

For more information on the runtime hierarchical generation feature of the PCG Framework, see [Using Runtime Generation](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine#using-runtime-generation).

#### Injected Data

Injected data in the Biome Core is a term defining external data sent to the system at different key steps to add manual and more artistic control. The main injected data types are **exclusions** and **custom biome** data. All injected data inputs are contained in the blue comment boxes in the LocalBiomeCore and BiomeCore PCG graphs. Exclusions have premade blueprint classes next to **Biome Actors** and the **BiomeCore** BP class.

##### Exclusions (Local Biome Core)

Binary exclusions from a volume, primitives or spline to remove generated points overlapping those exclusion data. Use these to isolate an area for manual placement such as POIs or buildings, or for specific art and gameplay needs.

The exclusion searches for actors with tags "PCG\_BiomeExclusion" using components tagged with "BiomeExclusion" for volumes, primitives, and closed splines. For an open spline, use components tagged with "BiomePath".

For example, in the image below, a pre-configured **BP\_PCGBiomeExclusionVolume** and 
BP\_PCGBiomeExclusion**Spline** were added in the lower right quadrant, resulting in empty space. The yellow open spline path removes trees along the spline volume, based on its control points scale property.

[![An example of using exclusions for biomes.](https://dev.epicgames.com/community/api/documentation/image/a9ba6d7b-3ef5-4e08-bd14-f6af892db20b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9ba6d7b-3ef5-4e08-bd14-f6af892db20b?resizing_type=fit)

##### Custom Biome Data (Global Biome Core)

The custom biome data is standalone with its own independent custom logic and output. Its point data output is injected near the very end of the pipeline just before spawning and output to the Biome Core runtime. Custom biome data can produce artifacts on its own like spawning meshes, while outputting data to the Biome Core to benefit from global spawning. It can also output data for any other graphs not related to the global Biome Core. When passing its output the global Biome Core for spawning its points, the custom biome points must have the attributes required for spawning, mainly the **Mesh** soft object path.

Here are some examples of how to use custom biome data:

* A custom cavern tool is built from PCG graph logic, Blueprints, and a set of variables. The cavern actor must hold its own trigger box, gameplay actors and spawners while all meshes can be spawned by the global Biome Core.
* A level instance actor containing a manually-created cabin is both an exclusion data for the biome and custom data, as it generates surroundings from a set of meshes and actors to be spawned by the global Biome Core.

## Inputs

### Biome Volume, Spline, and Texture Actors

Biome actors are used to set up biomes in a world. The actors are made from Blueprint classes available with the Biome Core. This includes biome volumes, biome splines, and biome texture actors.

Blueprint classes can be found in the following folders:

* `/Script/Engine.Blueprint'/PCGBiomeCore/Blueprints/BP_PCGBiomeVolume.BP_PCGBiomeVolume'`
* `/Script/Engine.Blueprint'/PCGBiomeCore/Blueprints/BP_PCGBiomeSpline.BP_PCGBiomeSpline'`
* `/Script/Engine.Blueprint'/PCGBiomeCore/Blueprints/BP_PCGBiomeTexture.BP_PCGBiomeSetup'`

Biome volume, spline, and texture actors are the way to define biomes in the world. Once set up they can be scaled or reshaped, duplicated, instanced throughout the world, and exported as child blueprint classes to re-use in multiple worlds while having a single source class to work on.

Biome volume, spline, and texture actors have the following properties:

* **Actor transforms and components**: Actor transforms include position, rotation, and scale. The spline shape can be customized and new control points can be added in the world directly, but the spline must remain a closed spline. For volumes, the box collision component can be modified.
* **Definition**: A reference to the Biome Definition data asset to identify the biome this actor represents with a color, a name, and a priority.
* **Assets array**: A reference to the biome asset. This array is a list of assets to process and spawn within this biome actor local cache bounds. This property is an array so that multiple Biome Assets can be added for categorization or for sharing the same asset in different biomes.
* **Default definition and local assets**: Each biome actor can store its own local default definition and a list of local assets. If a definition is referenced, it will be prioritized over the default definition. If assets and local assets are used, all of them are combined internally as a single attribute table local to that biome actor.
* **Local Cache Size** and **ZExtents**: These define the resolution and height of the biome when using a Biome Spline and Texture actors. A very large size value would mean this biome is applied in 2D across the Biome Core volume height, while a small value would require the spline to be adjusted against the surface. Start with default settings, or use bigger values to reduce the impact of building the local biome cache. The values can also be adjusted per biome actor depending on the level of precision you want.
* **Runtime Assets**: A reference to the biome assets to use for this biome in the Biome Core runtime generation. These are optional and are only needed when using the Biome Core runtime.
* **Controls**: Generic functions that can be used to ease workflows when working on a specific biome.

### Biome Definition

Biome definition templates are **PrimaryDataAsset** classes inheriting from **BiomeDefinitionTemplate**.

Examples of biome definition template and their corresponding structure are located in the following folders:

* `/Script/Engine.Blueprint'/PCGBiomeCore/BiomeDefinitions/Setup/BiomeDefinitionTemplate.BiomeDefinitionTemplate'`
* `/Script/Engine.UserDefinedStruct'/PCGBiomeCore/BiomeDefinitions/Setup/BiomeDefinition.BiomeDefinition'`

A biome definition structure includes the following base properties:

[![PCG Biome Reference](https://dev.epicgames.com/community/api/documentation/image/94dec730-452f-4265-add6-64f3ec35ab77?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94dec730-452f-4265-add6-64f3ec35ab77?resizing_type=fit)

* **BiomeName**: Used to identify the biome when debugging and inspecting the Biome Core. Has no actual impact on generation.
* **BiomeColor**: A unique color (RGB) to identify the biome and match generated points to assets entries in the root asset table. Biomes must have a unique color.
* **BiomePriority**: The priority specific to the biome when overlapping biomes are inserted into the biome cache. Lower values mean higher priority.

### Biome Assets and Structures

Biome asset templates are **PrimaryDataAsset** classes inheriting from BiomeAssetBaseTemplate. To be compatible with Biome Core, subclasses of **BiomeAssetBaseTemplate** must provide an array of structures named **BiomeAssets**.

Examples of BiomeAssetBaseTemplate and their corresponding structures are located in the following folders:

* `/Script/Engine.Blueprint'/PCGBiomeCore/BiomeAssets/Setup/BiomeAssetTemplate.BiomeAssetTemplate'`
* `/Script/Engine.UserDefinedStruct'/PCGBiomeCore/BiomeAssets/Setup/BiomeAsset.BiomeAsset'`
* `/Script/Engine.Blueprint'/PCGBiomeCore/Runtime/BiomeRuntimeAssetTemplate.BiomeRuntimeAssetTemplate'`
* `/Script/Engine.UserDefinedStruct'/PCGBiomeCore/Runtime/BiomeRuntimeAsset.BiomeRuntimeAsset'`
* `/Script/Engine.Blueprint'/PCGBiomeSample/BiomeAssets/Setup/BiomeSample_BiomeAssetTemplate.BiomeSample_BiomeAssetTemplate'` 
  (Biome Sample Plugin)
* `/Script/Engine.UserDefinedStruct'/PCGBiomeSample/BiomeAssets/Setup/BiomeSample_BiomeAsset.BiomeSample_BiomeAsset'`
  (Biome Sample Plugin)

Biome asset structures generally have several substructures used to categorize properties. You can create different types of biome asset templates, sharing one or more substructures, based on project needs.

A biome asset structure has the following base properties:,

[![PCG Biome Reference](https://dev.epicgames.com/community/api/documentation/image/edf52048-1b2f-44ea-94fc-e2f71d64fc7d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/edf52048-1b2f-44ea-94fc-e2f71d64fc7d?resizing_type=fit)

* **Enabled**: Used to disable an asset without removing it from the assets array.
* **Weight**: When assets sharing a common generator graph are assigned to the generated points, the weight property is used to affect the probability of the asset being chosen.
* **Generator**: A reference to a biome generator asset, used to provide a PCG graph responsible for producing PCG points.
* **GeneratorSubType**: Optional. A comma separated list of generator subtypes used to select the generator outputs to be used.
* **TransformGraph**: Optional. A reference to a PCG graph consuming the points from the generator and transforming them before spawning the asset.
* **Mesh**: A reference to a static mesh asset.
* **Assembly**: A reference to a PCG data asset.
* **Actor**: A reference to an actor class.
* **ChildAssets**: An array of biome assets to be spawned as children of this asset. Each child asset uses their transform graph to generate their relative position to the parent.
* **DebugOptions**: A **BiomeAsset\_DebugOptions** sub-structure.

  + **Isolate**: When true, only assets that are isolated are spawned.
  + **ShowBounds**: Draws wireframe bounds of the points associated with the asset.
* **AssetOptions**: A **BiomeAsset\_AssetOptions** sub-structure.

  + **OverlapWithChildren**: When false, the point bounds are used as difference to remove the child assets overlapped by the current asset.
  + **ForceAssetScale**: Applies the scale property to the points regardless of the scale applied by the transform graph. When false, the transform graphs control the scale.
  + **ExtentsMultiplier**: By default, the points bounds are computed from the composed bounds of the asset's mesh, actor, or assembly. This property acts as a multiplier over the computed bounds and affects the results of the differences with points from other generators, child assets, and self pruning operations. Useful for tree assets when the canopy bounds are too large compared to the trunk.
  + **Translation/Rotation/Scale**: Applies an offset to the mesh, actor, or assembly. Used to compensate for pivot placement. Useful in cases where assets of different size or orientation share the same generator.
  + **OrientUpward**: Progressively blends asset orientation from the generator to Z up, the landscape normal for surface sample-based generators.
  + **SelfPrune**: Applies a self pruning operation over the generated points, using the asset computed bounds with the **Extents** multiplier factor applied, to clean up overlapping points.
  + **SelfPruningExtentsMultiplier**: An extra multiplier applied to the points extents for self pruning exclusively. Allows for control over the bounds used during the self pruning without affecting other operations using the asset bounds.
* **MeshOptions**: A **BiomeAsset\_MeshOptions** sub-structure.

  + **Material**: Optional. A single material applied as an override to the static mesh material.
  + **AllowCollision**: When true, the asset uses the collision preset from the static mesh. When false, the **NoCollision** preset is used.
  + **Visible**: Translates to the similarly-named property of the static mesh component.
  + **CastShadow**: Translates to the similarly-named property of the static mesh component.
  + **CastHiddenShadow**: Translates to the similarly-named property of the static mesh component.
  + **AffectDistanceFieldLighting**: Translates to the similarly-named property of the static mesh component.
  + **DetailMode**: Translates to the similarly-named property of the static mesh component. 0 to 3 map to Low to Epic.
  + **StartCullDistance/EndCullDistance**: Translates to the similarly-named properties of the static mesh component.
  + **WorldPositionOffsetDisableDistance**: Translates to the similarly-named property of the static mesh component.
  + **IncludeInHLOD**: Translates to the similarly-named property of the static mesh component.
* **AssemblyOptions**: A **BiomeAsset\_AssemblyOptions** substructure.

  + **AllowCollision**: When true, the asset uses the collision presets from the assembly or PCG data asset static meshes. When false, the **NoCollision** preset is used.
* **FilterOptions**: A **BiomeAsset\_FilterOptions** substructure.

  + **DensityMin/Max**: Discards points with Density values outside this range.
  + **HeightMin/Max**: Discards points with **Position.Z** values outside this range.
  + **WaterDistanceMin/Max**: Points Below the water level configured in **BiomeFilter\_WaterDistance\_Level\_Inst** are considered below the water. A **Distance** node computes the 3D distance of the points above the water to the closest point below the water. Points within the **WaterDistanceMin/Max** range are kept.
* **RuntimeOptions**: A **BiomeAsset\_RunTimeOptions** substructure.

  + **ExportPoints**: Enables sampling of the asset's static mesh, and exports the assets locations in world space to generate points at runtime for additional details covering the static mesh.
  + **MeshSamplingRadius**: Controls the number of points generated by the mesh sampler.
  + **NormalOffset**: Used to remove points generated by the mesh sampler based on their normal orientation.
  + **ScaleMultiplier**: Used to scale points generated by the mesh sampler.
  + **ZMin/ZMax**: Controls the minimum and maximum height range of points generated by the mesh sampler.
  + **InfluenceType**: Controls whether the asset adds or removes runtime generated details around them.
  + **InfluenceRadius**: Radius around the asset points within which the **InfluenceType** is applied.

### Generator

Biome generator templates are **PrimaryDataAsset** classes inheriting from **BiomeGeneratorTemplate**.

Examples of BiomeGeneratorTemplate and their corresponding structure are located in the following folders:

* `/Script/Engine.Blueprint'/PCGBiomeCore/BiomeGenerators/Setup/BiomeGeneratorTemplate.BiomeGeneratorTemplate'`
* `/Script/Engine.UserDefinedStruct'/PCGBiomeCore/BiomeGenerators/Setup/BiomeGenerator.BiomeGenerator'`

It is mandatory to refer to a Biome Generator asset in each Biome Asset entry to define which root point data they belong to. Child assets do not require generator reference unless they are used as both root and child assets.

A biome generator structure includes the following base properties:

[![PCG Biome Reference](https://dev.epicgames.com/community/api/documentation/image/244592ad-df09-45bf-a628-909ac1f24108?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/244592ad-df09-45bf-a628-909ac1f24108?resizing_type=fit)

* **GeneratorType**: A unique name used to identify the generator. All generators must have a unique name and can be reused in multiple assets of multiple biomes.
* **GeneratorPriority**: The priority used when layering the point data through the priority-based difference feedback loop. Lower values mean higher priority. Generators with identical values do not impact each other if overlapping.
* **GeneratorAllowOverlap**: When enabled, the layering process through the priority-based difference operation is completely bypassed. All points produced by the generator are kept and do not impact any other generator points data during this process.
* **GeneratorGraph**: A PCG graph or PCG graph instance reference, which is executed to produce the root points.
* **GeneratorSpatialNoiseSettings**: Optional. A **SpatialNoiseSettings** asset reference exported from a spatial noise PCG node through the PCG graph. When present, this spatial noise setting controls the weighted distribution of assets instead of using the random point seed.

### Transform

Transform graphs get either points from a generator or parent-transformed points as input, and then modify them before the spawning step.

These graphs are optional for root assets but most of the time are mandatory for child assets, since without a transform graph, a child will spawn at the same location as its parent. Usage of graph instances to parameterize and control the behavior of transform graphs per asset is recommended, but using graphs directly works as well.

A few simple transform graphs are provided by Biome Core. Two examples are the **BasicSecondaries** and **DuplicatePattern**graphs, which are located in the following folders:

* `/Script/PCG.PCGGraph'/PCGBiomeCore/Transforms/BasicSecondaries.BasicSecondaries'`
* `/Script/PCG.PCGGraph'/PCGBiomeCore/Transforms/DuplicatePattern.DuplicatePattern'`

The **BasicSecondaries** graph creates a few points around each input point and projects them onto the landscape. The process works as follows:

1. Get the Input Points.
2. Build a 2D grid of points using a CreatePointsGrid node.
3. Remove the corner points of the grid to make it more circular.
4. Copy the grid to each of the input points using CopyPoints.
5. Randomly remove 50 percent of the copied points.
6. Apply Random transformations to the points.
7. Scale the points based on their distance from the center of each grid.
8. Project the result on the landscape.

[![](https://dev.epicgames.com/community/api/documentation/image/ceb5a0c6-6c90-4e12-ab64-663c04186b94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ceb5a0c6-6c90-4e12-ab64-663c04186b94?resizing_type=fit)

The BasicSecondaries transform graph.

[![](https://dev.epicgames.com/community/api/documentation/image/4beb0000-d561-495d-a84b-affcf4e85c19?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4beb0000-d561-495d-a84b-affcf4e85c19?resizing_type=fit)

The BasicSecondaries transform graph applied to 2 generations of child assets shown in red and green.)

The **DuplicatePattern** graph uses the **Duplicate Point** node to achieve a rotating star shape through the following process:

1. Reset the input points rotation.
2. Duplicate the input points 9 times, and rotate each copy by 36 degrees around the z axis.
3. Duplicate each of the 9 copies 10 times. For each copy, rotate by 10 degrees around Z, translate along the local X axis, and scale down the point by 80 percent.
4. Project to the landscape.

[![](https://dev.epicgames.com/community/api/documentation/image/57926dfc-51b2-436f-a2b5-bacbbc981f08?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/57926dfc-51b2-436f-a2b5-bacbbc981f08?resizing_type=fit)

The DuplicatePattern transform graph.

[![](https://dev.epicgames.com/community/api/documentation/image/7f07a3e5-5406-4f20-a613-fdd17c7f16e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7f07a3e5-5406-4f20-a613-fdd17c7f16e3?resizing_type=fit)

The DuplicatePattern transform graph applied to 2 generations of child assets shown in red and green.

[![](https://dev.epicgames.com/community/api/documentation/image/134b0a04-cfd9-458b-a3b7-94b4424acc30?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/134b0a04-cfd9-458b-a3b7-94b4424acc30?resizing_type=fit)

The DuplicatePattern transform graph applied to the 1st generation of child assets (red). The BasicSecondaries graph is applied to the second generation (Green).

### Filters

Root and child points can be filtered from a customizable list of filters in the **BiomeCore\_Filters** PCG graph or an instance of it. Each filter entry in the filters array has **FilterGraph**, **FilterAttribute**, **FilterRangeMinAttribute**, and **FilterRangeMaxAttribute** properties. Each filter graph is processed sequentially from the order they appear in the **Filters** list through a feedback loop during the local Biome Core execution.

The filter graphs are set globally in the Biome Core graph parameters: **Root Points Filters** and **Child Points Filters**. By default, the Biome Core is set up to use **BiomeCore\_Filters\_Inst**, which filters by Height and Density.

[![](https://dev.epicgames.com/community/api/documentation/image/6cc8a8fe-6a2a-405f-81ef-7afeb762ccab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cc8a8fe-6a2a-405f-81ef-7afeb762ccab?resizing_type=fit)

The Root Points Filters and Child Points Filters properties.

[![](https://dev.epicgames.com/community/api/documentation/image/fefbee1b-198c-452b-8d88-8c93bbf40f5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fefbee1b-198c-452b-8d88-8c93bbf40f5a?resizing_type=fit)

The BiomeCore\_Filters\_Inst list, showing properties for each entry.

The Biome Core filter graphs are located in the following folders:

* `/Script/PCG.PCGGraph'/PCGBiomeCore/Core/BiomeCore_Filters.BiomeCore_Filters'`
* `/Script/PCG.PCGGraphInstance'/PCGBiomeCore/Core/BiomeCore_Filters_Inst.BiomeCore_Filters_Inst'`

The Biome Sample filters are extended to showcase how to customize the list and include texture projection filters. The files are located in the following folders:

* `/Script/PCG.PCGGraphInstance'/PCGBiomeSample/Setup/BiomeSample_Filters_Inst.BiomeSample_Filters_Inst'`
* `/Script/PCG.PCGGraphInstance'/PCGBiomeSample/Filters/BiomeFilter_Flow_Projection.BiomeFilter_Flow_Projection'`
* `/Script/PCG.PCGGraphInstance'/PCGBiomeSample/Filters/BiomeFilter_SunExposure_Projection.BiomeFilter_SunExposure_Projection'`

The dynamic feedback loop processes all incoming root and child points data by iterating over the filter graphs set in the **Filters** array. The remaining points left from the current iteration becomes the input of the next, progressively culling points based on asset filter options.

[![](https://dev.epicgames.com/community/api/documentation/image/e9ec8c3a-425e-46c6-a90b-45049bee0957?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9ec8c3a-425e-46c6-a90b-45049bee0957?resizing_type=fit)

The processing steps for filtering

The processing steps for filtering are as follows:

1. The point data is brought in for the current loop iteration. The first iteration starts with all points, then each next iteration receives points remaining from the previous one until all filters have been processed.
2. The dynamic filter graph, set in the **Filters** array entries, processes and writes to the set **FilterAttribute** on all points. This graph is optional when filtering simple point properties such as **$Density** or **$Position,**but a filter graph can also override these properties if needed (for example, apply a spatial noise as a multiplication over incoming point **$Density**).
3. Filters points by range using the **FilterAttribute** within the **FilterRangeMinAttribute** and **FilterRangeMaxAttribute** values set in each asset filter options.
4. Outputs all remaining points left after the filtering to the feedback **Points** output pin. These will be the next iteration's incoming points to work on, or the final output of the filtering process after all iterations have been completed.

## Advanced Setup

### Local Biome Core Graph Parameters

This section describes the global parameters exposed as **Parameter Overrides** on the local Biome Core PCG component.

[![The global parameters exposed as Parameter Overrides on the local Biome Core PCG component](https://dev.epicgames.com/community/api/documentation/image/f210c3bd-70e8-4fe7-a82b-e6609e86f3d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f210c3bd-70e8-4fe7-a82b-e6609e86f3d0?resizing_type=fit)

#### Biome Blending Range

Expands the bounds of the local biome cache.

[![](https://dev.epicgames.com/community/api/documentation/image/8d0f645d-637f-46c8-9476-c12040f21e60?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d0f645d-637f-46c8-9476-c12040f21e60?resizing_type=fit)

Biome Blending Range value of 0.

[![](https://dev.epicgames.com/community/api/documentation/image/58fc5bcf-5232-4b43-aea8-b90021b67c00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58fc5bcf-5232-4b43-aea8-b90021b67c00?resizing_type=fit)

Biome Blending Range value of 6400cm.

### Biome Blending Noise and Density

Adjusts the amount of points kept within blending range.

[![](https://dev.epicgames.com/community/api/documentation/image/305d606c-5787-4586-9fd0-ab484825b2ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/305d606c-5787-4586-9fd0-ab484825b2ac?resizing_type=fit)

Biome Blending Noise value of 0 and Density of 1.

[![](https://dev.epicgames.com/community/api/documentation/image/bf779246-42cb-4587-aaa1-37fbb3571d43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf779246-42cb-4587-aaa1-37fbb3571d43?resizing_type=fit)

Biome Blending Noise value of 1 and Density of 0.5.

### Max Child Asset Depth

Controls the maximum level of recursion to reach when spawning child assets.

* A value of 0 will disable child assets spawning entirely.
* Can be used to trade off between performance and detail when iterating on biome placement, or for producing optimized content for different platforms.
* Child assets can refer to themselves, potentially creating infinite recursion. The **Max Child Asset Depth** parameter prevents this situation from happening.
* More details in the [Recursion and Transform](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine) section.

[![](https://dev.epicgames.com/community/api/documentation/image/87df475e-4750-4343-87d6-991c542b7f27?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87df475e-4750-4343-87d6-991c542b7f27?resizing_type=fit)

Max Child Assets Depth value of 0.

[![](https://dev.epicgames.com/community/api/documentation/image/ee15f166-49b1-4e18-be65-c310047914b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee15f166-49b1-4e18-be65-c310047914b3?resizing_type=fit)

Max Child Assets Depth value of 1.

[![](https://dev.epicgames.com/community/api/documentation/image/e4214cfa-1e98-4cf2-8941-d3b9d4f88acc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4214cfa-1e98-4cf2-8941-d3b9d4f88acc?resizing_type=fit)

Max Child Assets Depth value of 2.

#### Child Input Points Rate Multiplier

Limits the number of points allowed to emit child assets.

[![](https://dev.epicgames.com/community/api/documentation/image/87216fd1-b499-47d9-8e4f-24ec1a9a2e80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87216fd1-b499-47d9-8e4f-24ec1a9a2e80?resizing_type=fit)

Child Input Points Rate Multiplier value of 1.

[![](https://dev.epicgames.com/community/api/documentation/image/6bb79cdb-54dc-4183-ba8a-be8faa684282?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bb79cdb-54dc-4183-ba8a-be8faa684282?resizing_type=fit)

Child Input Points Rate Multiplier value of 10.

[![](https://dev.epicgames.com/community/api/documentation/image/4e2c4f43-92dd-40e2-8cf9-225260589887?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e2c4f43-92dd-40e2-8cf9-225260589887?resizing_type=fit)

Child Input Points Rate Multiplier value of 100.

#### Local Preview

Spawns meshes and actors on self instead of serializing the generated points into the local Biome Core component. This mode allows quick previewing of the local biome without the need of biome core BP and without triggering refresh of it if present. This is ideal to work in isolation on one specific biome configuration as a fast preview mode.

#### Bypass Filters

Skips the point filtering step. For more information, see the [Filters](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine#filters) section of this document.

#### Debug Display Local Biome Cache

Displays a visual representation of the local biome cache.

[![The debug display of the local biome cache.](https://dev.epicgames.com/community/api/documentation/image/de6e729c-849f-43af-89be-ff3abf36d49c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de6e729c-849f-43af-89be-ff3abf36d49c?resizing_type=fit)

### Global Biome Core Graph Parameters

#### Debug Display Global Biome Cache

Displays a visual representation of all combined local biome caches within the global Biome Core bounds.

[![](https://dev.epicgames.com/community/api/documentation/image/af39dc4c-0c58-432d-8650-00a28200ba3c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af39dc4c-0c58-432d-8650-00a28200ba3c?resizing_type=fit)

The debug display for the global biome cache.

#### Output Data for Runtime Generation

Enables serialization of Biome Core graph output data to the global Biome Core PCG component, for use by the biome core runtime PCG Graph. Also enables sampling of asset meshes used by the biome core runtime.

For more information, see the [Spawning](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine#spawning) section of this document.

### Generator Subtypes

Generators have a unique **generator type** that is used to map the assets to the generated points per biome. Generator graphs can optionally output multiple point data as **generator subtypes**.

Subtypes have multiple use cases and can greatly reduce the amount of generator graphs needed to create a complex biome. Any advanced interaction between the points of different assets is best handled by generator subtypes, as the BiomeCore pipeline does not allow access to points from other generators during the process. The only interaction between different generators point data happens during the priority-based difference layering step.

Here are some example use cases for generator subtypes:

[![A biome full of trees.](https://dev.epicgames.com/community/api/documentation/image/86ed50f6-0cc7-46d0-b4cd-8bfe30e1d291?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86ed50f6-0cc7-46d0-b4cd-8bfe30e1d291?resizing_type=fit)

[![The same biome, but with a landscape paint layer applied. There is now a strip of sand and bushes drawn through the middle of the trees.](https://dev.epicgames.com/community/api/documentation/image/cb9d00a0-c817-4975-81b4-25f98d6f2088?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb9d00a0-c817-4975-81b4-25f98d6f2088?resizing_type=fit)

* Generate points on landscape for trees and create subtypes based on the landscape layer weights, as seen in the images above. This allows landscape paint layers to impact the biome result while using a single generator by distributing assets based on the painting to add overall visual complexity while maintaining simple inputs and less processing.
* Separate points from a single generator to be used by different assemblies or meshes depending on the slope angle.
* Duplicating points in the generator to apply a specific transform to spawn actors such as Niagara systems, sound, decals, or gameplay items.

To help create generator subtypes in generator graphs, a pre-made PCG subgraph is available in the Biome Core. This subgraph filters data based on an attribute and produces two separate outputs. This subgraph can also be chained or used in loops to create more than two separate subtypes.

The pre-made PCG subgraph is located at the following path: `/Script/PCG.PCGGraph'/PCGBiomeCore/BiomeGenerators/Graphs/BiomeGenerator_SubGeneratorSetup.BiomeGenerator_SubGeneratorSetup'`

In the following image, the landscape surface is sampled with its layer weights, then subtypes are created for each layer (**Land**, **Mountain**, **Shore**) using the subgraph.

[![The pre-made generator subtype subgraph](https://dev.epicgames.com/community/api/documentation/image/b56f3d38-da09-4011-8277-a8fcb2983364?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b56f3d38-da09-4011-8277-a8fcb2983364?resizing_type=fit)

After the generator graph is outputting subtypes, it is mandatory to specify to which generator subtypes the Assets should be assigned using their **GeneratorSubType** property. An asset can be assigned to multiple subtypes at once using a comma separated list. In the case of the landscape painting example displayed above, the **Broadleaf Forest** assets in Biome Sample are assigned different subtypes based on each landscape paint layer. The spruce trees spawn on **Shore** and **Mountain** layers while all other assets spawn on **Shore** and **Land**, resulting in spruce trees appearing only where the **Mountain** layer was painted using a single generator.

[![The Broadleaf Forest assets assigned to generator subtypes](https://dev.epicgames.com/community/api/documentation/image/590975c6-696a-4f1f-87dc-7d617d51b2cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/590975c6-696a-4f1f-87dc-7d617d51b2cd?resizing_type=fit)

### Hierarchical Generation

The Biome Core PCG component is non-partitioned by default, but the Biome Core Graph has been built with partitioning and hierarchical generation in mind.

To enable hierarchical generation, follow these steps:

1. Enable the **Is Partitioned** property on the BiomeCore PCG Component. By default, the generation will be partitioned in chunks of 256x256 meters, according to the PCG World Actor's **Partition Grid Size** setting.

   [![The Is Partitioned property](https://dev.epicgames.com/community/api/documentation/image/fb616f6c-17be-4e00-88f1-af317bf5eb7e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb616f6c-17be-4e00-88f1-af317bf5eb7e?resizing_type=fit)
2. Enable the **Use Hierarchical Generation** property in the BiomeCore PCG Graph settings. By enabling both, the generation is partitioned in chunks of 256x256 meters, using Grid Size nodes at multiple points in the graph. Then, at the unbounded level, the generation uses the data from all the local Biome Core graphs of each overlapping Biome Actor.

   [![The Use Hierarchical Generation property](https://dev.epicgames.com/community/api/documentation/image/e7f588e3-56a7-4929-add6-c35f86868fb4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e7f588e3-56a7-4929-add6-c35f86868fb4?resizing_type=fit)

In editor, enabling partitioning or hierarchical generation increases the time needed for a full regeneration, but it makes partial updates of the biomes faster, such as when manipulating biome volumes or biome splines in the world.

Partitioning the PCG component is also recommended when using Biome Core for producing games using World Partition levels, to enable streaming of PCG partition actors at runtime.

## Biome Core Runtime

[![](https://dev.epicgames.com/community/api/documentation/image/c1df0c14-3c2f-4ff2-9ab9-dfc9a69e2a51?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c1df0c14-3c2f-4ff2-9ab9-dfc9a69e2a51?resizing_type=fit)

The Biome Core runtime debug display, showing points from the biome cache sampled by Biome Core runtime.

### Overview

Biome Core runtime includes a Blueprint actor and PCG graph, used for runtime generation of detailed assets around the camera. It consumes data that has been pre-generated by local Biome Core actors, and leverages Runtime Hierarchical Generation and PCG GPU nodes to generate a large quantity of PCG points at runtime.

#### Enabling Runtime Generation

To preview runtime generation in editor, enable the **Treat Editor Viewport as Generation Source** option on the **PCGWorldActor**:

[![The Treat Editor Viewport as Generation Source option of the PCGWorldActor](https://dev.epicgames.com/community/api/documentation/image/ab00774d-e1f2-4d28-b935-566c612bb5d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab00774d-e1f2-4d28-b935-566c612bb5d3?resizing_type=fit)

Enabling this option generate points and spawn assets around the camera. When in a Play-In-Editor (PIE) session or cooked build, the player location is automatically used as a runtime generation source.

#### Runtime Assets

Assets used by the runtime generation are a type of biome asset, assigned to the biome actors such as setups, splines, and volumes. Multiple runtime assets can be added per biome actor. Each runtime asset contains a reference to a Runtime Hierarchical Generation-enabled PCG graph and an array of weighted biome assets.

The graph includes nodes that run on the GPU to generate sets of points shared by the assets in the array. Each asset in the **Runtime Assets** array can be considered as a layer of points that shares a PCG graph and a list of meshes.

[![](https://dev.epicgames.com/community/api/documentation/image/67e1ef72-4c01-4ad6-b22d-d80746f5399a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67e1ef72-4c01-4ad6-b22d-d80746f5399a?resizing_type=fit)

A Desert runtime asset assigned to the Desert biome setup actor.

[![](https://dev.epicgames.com/community/api/documentation/image/1f376861-14d1-40ec-859a-fd23c9306012?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1f376861-14d1-40ec-859a-fd23c9306012?resizing_type=fit)

The properties of the Desert runtime asset.

#### Runtime Hierarchical Generation Setup

Runtime Hierarchical Generation is enabled using the following settings:

1. In the Biome Core runtime component settings, set Generation Trigger to **Generate at Runtime**, and set Is Partitioned to **True**.

   [![The Biome Core runtime component settings](https://dev.epicgames.com/community/api/documentation/image/5e0044b7-19ea-4535-a9c3-a0bc3db82287?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e0044b7-19ea-4535-a9c3-a0bc3db82287?resizing_type=fit)
2. In the Biome Core runtime graph settings, set **Use Hierarchical Generation** to **True** and set **Higen Default Grid Size** to **Unbounded**. This means that any node placed before a grid size node will execute only once, and at the unbounded grid level.

   [![The Biome Core runtime graph settings](https://dev.epicgames.com/community/api/documentation/image/f3b2afb7-f992-435c-b595-f04f56d24746?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3b2afb7-f992-435c-b595-f04f56d24746?resizing_type=fit)
3. Also in the runtime graph settings, the radius parameter used to control the generation distance is defined per grid size:

   * Grid size 3200, which has its **Generation Radius** set at 4800cm.
   * Grid size 6400, which has its **Generation Radius** set at 9600 cm.

   Increasing these radius values will generate details farther away, increasing the number of runtime partition actors and PCG points to process.

   [![The Generation Radius properties](https://dev.epicgames.com/community/api/documentation/image/f9c2225b-8a06-42f5-8834-b8d31a9ef9d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9c2225b-8a06-42f5-8834-b8d31a9ef9d0?resizing_type=fit)

The hierarchical generation of Biome Core runtime operates at the following levels:

* The **Unbounded**level, for operations that need to happen once for the entire level.
* A grid of runtime partition actors at the **3200** grid size level, for scattering points over Meshes around the camera.
* A grid of runtime partition actors at the **6400** grid size level, for scattering points over the **Landscape** or **World Height RVT** around the camera.

### Graph Parameters

[![The graph parameters on the Biome Core runtime](https://dev.epicgames.com/community/api/documentation/image/025f8a59-9974-4b7a-aff1-be9119ed2763?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/025f8a59-9974-4b7a-aff1-be9119ed2763?resizing_type=fit)

The following properties are exposed as graph parameters on the Biome Core runtime graph:

* **Display Biome Points**: Displays points sampled from the biome cache colored using their individual biome color.
* **Biome Search Distance**: Biome Core runtime supports linear blending of runtime assets. The blending distance is controlled by this parameter.
* **Mesh Scattering**: Enables spawning of pre-generated point clouds over meshes spawned by Biome Core.
* **Ground Scattering**: Enables scattering of runtime assets over the ground.
* **Use Height RVT**: Uses a World Height runtime virtual texture to resolve the points height in the world. When off (default) the landscape is sampled to get the point height.
* **Height RVT Priming**: When sampling from the Height RVT, PCG needs to inform the Runtime Virtual Texture system of the location in the world where the RVT data (pages) are requested, and which RVT asset will be accessed.

### Graph Overview

This section includes an overview of the Biome Core runtime graph. The description of the data exported by Biome Core and used as inputs by Biome Core runtime is located in the [Output to Biome Core Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine#output-to-biome-core-runtime) section of this document.

The Biome Core runtime graph is located at the following path: 
`/Script/PCG.PCGGraph'/PCGBiomeCore/Runtime/BiomeCoreRuntime_Graph.BiomeCoreRuntime_Graph'`

#### Inputs

The Biome Core runtime graph uses the following inputs:

* **Mesh Scatter: Asset Paths**: Contains soft objects paths to pre-generated point clouds and mesh attributes to instantiate over meshes.
* **Mesh Scatter: World Transforms**: Locations in the world where to instantiate the point clouds.
* **Ground Scatter: Biomes:** Biome cache point data generated by local Biome Core actors, representing the space occupied by each biome.
* **Ground Scatter: Influence Points**: Points used to locally increase or decrease the density of points spawned on the ground.
* **Ground Scatter: Weighted Assets**: Lists of assets and their properties to spawn on the ground (Landscape or RVT).

#### Sampled Meshes Points Placement in Worlds

[![The Mesh Scattering Assemblies section of the Biome Core runtime graph.](https://dev.epicgames.com/community/api/documentation/image/d31f7404-6329-428c-8a9e-99222804e5c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d31f7404-6329-428c-8a9e-99222804e5c5?resizing_type=fit)

In the **Mesh Scattering Assemblies** section of the Biome Core runtime graph, pre-generated PCG point cloud assets are copied at their corresponding locations in the world, represented by the **Mesh Scatter Locations** points. The point clouds are uploaded in GPU memory by the empty **Point Processor GPU** node all at once at the **Unbounded** grid size level. The point clouds are then copied at their locations in the world and spawned using **GPU Copy Points** and **GPU Static Mesh Spawner** nodes. This process is executed in a grid of partition actors, at the 800 cm Grid Size level.

[![](https://dev.epicgames.com/community/api/documentation/image/231b8d4b-7833-4a88-90c6-ca2c491f3599?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/231b8d4b-7833-4a88-90c6-ca2c491f3599?resizing_type=fit)

The orange wireframe boxes represent 3200 cm partition actors, which contain point clouds copied at their locations in the world.

#### Landscape or RVT Ground Scattering

[![The ground scattering section of the Biome Core runtime graph](https://dev.epicgames.com/community/api/documentation/image/c9d12f1d-1627-4ca3-ac78-cae8220861a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9d12f1d-1627-4ca3-ac78-cae8220861a0?resizing_type=fit)

This section of the Biome Core runtime graph prepares the Biome and Influence points, uploads them to the 6400cm grid, and loops over the assets (partitioned by the generator graph) to spawn meshes on the ground using custom HLSL nodes executed on the GPU.

#### Generator Graph Dynamic Selection and Execution

This subgraph is located at the following path: 
`/Script/PCG.PCGGraph'/PCGBiomeCore/Runtime/GroundScatter/GroundScatterRunGenerators.GroundScatterRunGenerators'`

[![The generator graph dynamic selection subgraph](https://dev.epicgames.com/community/api/documentation/image/d5dcf2cb-5bd0-4dc7-9f5a-36bb71118665?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5dcf2cb-5bd0-4dc7-9f5a-36bb71118665?resizing_type=fit)

This subgraph’s role is to select the generator graph in the assets attributes and launch it dynamically using the **Subgraph Override** pin.

#### Points Generation on GPU

Points generation occurs in one of the following subgraphs, depending on the type of ground scattering used:

* `/Script/PCG.PCGGraph'/PCGBiomeCore/Runtime/GroundScatter/PointGeneratorRVT.PointGeneratorRVT'` (for RVT)
* `/Script/PCG.PCGGraph'/PCGBiomeCore/Runtime/GroundScatter/PointGeneratorRVT.PointGeneratorLS'` (for Landscape)

[![The RVT point generator subgraph](https://dev.epicgames.com/community/api/documentation/image/2b259abf-83d5-4d8c-abaf-99850cbddb0f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b259abf-83d5-4d8c-abaf-99850cbddb0f?resizing_type=fit)

A point generator node with custom HLSL code produces and filters the points, using the asset properties and the following steps:

1. A 2D grid of points is created within the XY bounds of the current partition actor.
2. The points are randomly filtered out.
3. A random lateral offset is applied.
4. The RVT is sampled at that position, to get the point’s height.
5. A normal vector is rebuilt from 2 additional RVT samples.
6. The point rotation is created as a random rotation around the normal vector.
7. The points scale is set from the asset properties.
8. A spatial noise pattern is applied to the density value.
9. Additive/subtractive influences are applied to the density value.
10. Points with a density value of 0 are removed.
11. Density value is applied to the remaining points scale.

#### Biome Selection, Assets Selection by Weight, and Spawning on GPU

This subgraph is located at the following path: 
`/Script/PCG.PCGGraph'/PCGBiomeCore/Runtime/GroundScatter/GroundScatterGeneratorGraphGPU.GroundScatterGeneratorGraphGPU'`

[![The biome selection subgraph](https://dev.epicgames.com/community/api/documentation/image/bfdc9c2a-e3d1-4252-8759-1eabfa850a76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bfdc9c2a-e3d1-4252-8759-1eabfa850a76?resizing_type=fit)

The point processor custom HLSL node assigns meshes to the points, based on their **Biome** and **Weight** properties.

After the meshes are selected, the GPU static mesh spawner spawns them directly in the GPU scene.

#### Final Output of Biome Core Runtime

After all the steps in the Biome Core runtime graph are complete, the final output looks like the following image.

[![The final output of the Biome Core runtime graph.](https://dev.epicgames.com/community/api/documentation/image/b2a4b4ec-9840-468e-b315-98b35bc22dc4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2a4b4ec-9840-468e-b315-98b35bc22dc4?resizing_type=fit)

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [procedural generation](https://dev.epicgames.com/community/search?query=procedural%20generation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Reference](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#reference)
* [Core Graphs Overview](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#core-graph-overview)
* [Local Biome Core Graph](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#localbiomecoregraph)
* [Global Biome Core Graph](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#globalbiomecoregraph)
* [High Level Concepts](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#high-level-concepts)
* [Biome and Asset Mapping](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biomeandassetmapping)
* [Biome Cache (Local Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-cache)
* [Root Asset Table (Local Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#root-asset-table)
* [Generators (Local Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#generators)
* [Filtering (Local Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#filtering(localbiomecore))
* [Recursion and Transform (Local Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#recursionandtransform(localbiomecore))
* [Priority-Based Difference (Global Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#priority-based-difference)
* [Spawning (Global Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#spawning)
* [Output to Biome Core Runtime (Global Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#output-to-biome-core-runtime)
* [Injected Data](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#injected-data)
* [Exclusions (Local Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#exclusions)
* [Custom Biome Data (Global Biome Core)](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#custom-biome-data)
* [Inputs](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#inputs)
* [Biome Volume, Spline, and Texture Actors](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-actors-and-setup)
* [Biome Definition](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-definition)
* [Biome Assets and Structures](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-assets-and-structures)
* [Generator](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#generator)
* [Transform](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#transform)
* [Filters](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#filters)
* [Advanced Setup](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#advanced-setup)
* [Local Biome Core Graph Parameters](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-core-graph-parameters)
* [Biome Blending Range](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-blending-range)
* [Biome Blending Noise and Density](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biomeblendingnoiseanddensity)
* [Max Child Asset Depth](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#maxchildassetdepth)
* [Child Input Points Rate Multiplier](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#childinputpointsratemultiplier)
* [Local Preview](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#localpreview)
* [Bypass Filters](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#bypassfilters)
* [Debug Display Local Biome Cache](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#debug-display-biome-cache)
* [Global Biome Core Graph Parameters](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#globalbiomecoregraphparameters)
* [Debug Display Global Biome Cache](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#debugdisplayglobalbiomecache)
* [Output Data for Runtime Generation](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#outputdataforruntimegeneration)
* [Generator Subtypes](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#generatorsubtypes)
* [Hierarchical Generation](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#hierarchicalgeneration)
* [Biome Core Runtime](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biome-core-runtime)
* [Overview](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#overview)
* [Enabling Runtime Generation](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#enabling-runtime-generation)
* [Runtime Assets](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#runtime-assets)
* [Runtime Hierarchical Generation Setup](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#runtime-hierarchical-generation-setup)
* [Graph Parameters](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#graph-parameters)
* [Graph Overview](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#graph-overview)
* [Inputs](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#inputs)
* [Sampled Meshes Points Placement in Worlds](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#sampled-meshes-points-placement-in-worlds)
* [Landscape or RVT Ground Scattering](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#landscape-surface-sampler-and-biome-assets-influence)
* [Generator Graph Dynamic Selection and Execution](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#generatorgraphdynamicselectionandexecution)
* [Points Generation on GPU](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#pointsgenerationongpu)
* [Biome Selection, Assets Selection by Weight, and Spawning on GPU](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#biomeselection,assetsselectionbyweight,andspawningongpu)
* [Final Output of Biome Core Runtime](/documentation/en-us/unreal-engine/procedural-content-generation-pcg-biome-core-and-sample-plugins-reference-guide-in-unreal-engine?application_version=5.7#finaloutputofbiomecoreruntime)
