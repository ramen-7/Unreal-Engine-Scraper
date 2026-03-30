<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7 -->

# Procedural Vegetation Editor (PVE)

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
7. Procedural Vegetation Editor (PVE)

# Procedural Vegetation Editor (PVE)

Use the Procedural Vegetation Editor to generate realistic, high-quality, Nanite-ready vegetation.

On this page

The **Procedural Vegetation Editor** (**PVE**) is a powerful, graph-based tool integrated within Unreal Engine. It allows users to create high-quality, Nanite-ready vegetation assets directly within the engine environment. Unlike traditional methods, PVE leverages real-world botanical principles, simulating plant generation based on hormone distribution and adaptive responses. This innovative approach enables the generation of diverse and realistic vegetation.

In order to use the Procedural Vegetation Editor, you must enable the plugin, by navigating in the **Menu Bar** to **Edit** > **Plugins** > **Procedural Vegetation Editor (experimental)**. You must also ensure that the PCG, and Dynamic Wind plugins are also installed.

With PVE you can use the following features to build Nanite ready vegetation in your project:

* Generate Nanite-ready vegetation: Create highly optimized vegetation assets that take advantage of Unreal Engine's Nanite virtualized geometry system for incredibly detailed scenes with high performance.
* Apply real-world botanical principles: Produce vegetation that attempts to replicate natural growth patterns, leading to more authentic and believable results.
* Customize and create variations: Modify existing vegetation presets or design entirely new species using the node graph to suit specific project needs and artistic visions.
* Streamline vegetation creation: Reduce the manual effort typically involved in creating complex vegetation, allowing for quicker iteration and production.

### PVE Presets

The Procedural Vegetation Editor relies on using preset assets, called **Megaplants**, that contain data to build specific species of vegetation. These preset assets contain Skeletal Meshes, Materials and Textures, with nanite foliage support for multiple variations to create realistic vegetation in your project. Multiple preset assets can be combined using the PVE Graph, to build complex and interesting foliage in your project. You can also modify these preset assets using the PVE Graph Editor to meet the goals of your project.

You can explore the Megaplant selection of preset assets on FAB.

### Key Supported Workflows

Currently PVE supports the following key workflows:

* Using pre-built variations supplied in the presets as is - they are ready to be used immediately.
* Customizing the pre-built variations supplied in the presets or creating new ones by reusing the supplied components.
* Using custom foliage and materials to change the look and feel while retaining the foundational aspects of those species.
* Using PVE output to populate scenes by hand-placement or PCG.

The initial version of PVE focuses on providing a robust foundation for procedural vegetation creation to allow users to always start with some presets. While the full range of features will expand to allow users to grow vegetation from scratch, currently the core functionality revolves around:

* Loading Procedural Vegetation Presets:

  + Description: This feature allows users to load pre-built data for specific plant species. These presets contain foundational information and growth parameters that define a particular species of vegetation.
  + What it does: It provides a quick starting point for users, offering a library of diverse instances of vegetation species that can be further customized to create variations. This eliminates the need to build every plant from scratch.
* Customizing/Creating Variations using the Node Graph:

  + Description: PVE utilizes a node-based interface, similar to other visual scripting tools in Unreal Engine. This graph allows users to manipulate and define the parameters that control the vegetation's growth, form, and appearance using pre-built nodes.
  + What it does: Through connecting various nodes, users can:

    - Adjust parameters related to hormone simulation and adaptive growth.
    - Introduce randomness or specific conditions to influence branching, leaf distribution, and overall plant structure.
    - Control material properties, texture application, and other visual aspects of the vegetation.
    - Generate unique variations of a loaded preset or construct entirely new botanical forms, tailoring the vegetation precisely to their desired needs.

## PVE Nodes

You can use the following sections of this document as a reference for the PVE Nodes you will use when constructing graphs to generate foliage in your project. Each section will provide an overview and use case for each of the nodes as well as a breakdown of each of the nodes properties, and their associated options.

### Procedural Vegetation Preset Loader

The **Preset Loader** is your **starting point** in PVE. It loads a ready-made **plant preset** so you don’t have to build a tree or bush completely from scratch. Think of it like choosing a base recipe — once loaded, you can tweak, customize, and grow it into something unique.

**What It Does**

* Loads a **preset plant species** (like oak, pine, or bush).
* Each preset includes:

  + The plant’s **main structure** (trunk and branches).
  + **Growth rules** (how it expands or reacts to light/gravity).
  + **Branch data** (where smaller branches attach).
  + **Foliage meshes** (what leaves or needles look like).
  + **Materials** (textures for bark, leaves, etc.).

**When to Use It**

* **Quick start**: Instantly load a full plant model to begin experimenting.
* **Customization**: Use presets as a base, then add nodes to change shape, size, or foliage.

**Pro Tip for Beginners**

* Start with a preset and make small changes (like Scale or Foliage changes) to quickly see results.

| Category | Description |
| --- | --- |
| Variable Group | Preset |
| Variable | Preset |
| What it does | Loads a ready-made plant preset |
| Detailed guidance | Each preset contains all the information for a species (trunk, branches, leaves, materials, and growth rules). It’s your starting point before customizing. |

### Carve

The **Carve** node is like using pruning shears or a saw on your plant. It lets you trim away parts of the structure based on rules you set, so you can control the final shape and size of your vegetation.

**What It Does**

You can “carve” (remove) branches or parts of the trunk based on different measurements:

* **Length From Root**: Cuts branches depending on how far they are from the trunk base.

  + Example: Removes branches from the top of the plant. A value of 0 will not remove any branches, but a value of 1 will remove all branches leaving the plant as just a trunk.
* **From Bottom**: Cuts based on height from the very bottom of the plant.

  + Example: Similar to Length From Root, From Bottom trims branches, just in the opposite direction starting from the base of the plant. From Bottom first shortens the trunk and then removes the lowest branches.
* **Z Position**: Cuts based on world height (Unreal Engine’s Z axis).

  + Example: slice the plant at a specific height in the level.
* **Radius**: Removes branches depending on how thick they are.

  + Example: keep only the thickest branches, or trim away smaller twigs.

**When to Use It**

* **Shape control**: Trim a tree into a cleaner silhouette.
* **Gameplay needs**: Clear out the bottom of trees for visibility or player movement.
* **Stylization**: Chop off parts to create stylized or fantastical plant forms.
* **Optimization**: Remove fine details (thin twigs, low branches) for background vegetation.

**Pro Tip for Beginners**

* Use **From Bottom** if you want a quick way to clear the lower trunk.
* Try **Radius** to simplify a plant, keeping the main structure but getting rid of smaller clutter.
* Don’t over-carve — a few subtle trims often look more natural than drastic cuts.

| Category | Description |
| --- | --- |
| Variable Group | Carve |
| Variable | CarveBasis |
| Valid Values | LengthFromRoot, From Bottom, ZPosition, Radius |
| What it does | Sets the trimming rule. |
| Detailed guidance | **LengthFromRoot:**Trim branches based on how far they are from the trunk base.  **From Bottom**: Trim based on height from the bottom of the plant.  **ZPosition**: Trim at a specific world height.  **Radius:** Trim based on branch thickness.  Use this to clean up lower branches or thin twigs for performance. |

| Category | Description |
| --- | --- |
| Variable Group | Carve |
| Variable | Carve |
| Valid Values | 0.0–1.0 |
| What it does | Controls how much trimming happens. |
| Detailed guidance | Detailed guidance  0 = very little trimming, 1 = aggressive trimming.  Start with low values for natural results. |

### Gravity

The **Gravity** node makes your plant react to forces in nature — like how real branches bend under their own weight or grow upwards toward sunlight. It’s a way to add natural curves and direction to your vegetation so it feels alive and believable.

**What It Does**

* **Gravity Mode**

  + **Gravity**: Branches bend downward under their own weight.
* **Strength Controls**

  + Decide how much branches bend.
  + Low strength = gentle curve.
  + High strength = dramatic bending.
* **Direction Vector**

  + Modify this to Bend the plant along a custom direction.
  + Example: usually set to **world down**, but you can set a custom direction (useful for tilted plants or stylized growth).
* **Angle Correction & Bias**

  + Fine-tunes how branches balance between keeping their original angle.

**When to Use It**

* **Realism**: Make trees naturally droop under their own weight or external forces.
* **Stylization**: Exaggerate curves to give plants a fantasy or alien look.
* **Environment storytelling**:

  + Gravity-heavy: older, heavier trees with drooping branches.

**Pro Tip for Beginners**

* Start with **low strength** for subtle realism — too much bend can look unnatural.
* Mix both modes in the same scene for variety and natural diversity.

| Category | Description |
| --- | --- |
| Variable Group | Gravity |
| Variable | Mode |
| Valid Values | Gravity |
| What it does | Select the bending style. |
| Detailed guidance | Gravity: Branches bend downward under their own weight.  Gravity = heavy old trees. |

| Category | Description |
| --- | --- |
| Variable Group | Gravity |
| Variable | Gravity |
| Valid Values | 0.0–1.0 |
| What it does | Strength of bending. |
| Detailed guidance | Low = subtle curve, High = dramatic bend.  Keep low for realism, high for fantasy effects. |

| Category | Description |
| --- | --- |
| Variable Group | Gravity |
| Variable | Direction |
| Valid Values | Vector3 (e.g., World Down, custom vector). |
| What it does | Sets bending direction. |
| Detailed guidance | Usually world down, but custom vectors allow sideways growth or stylized effects. |

| Category | Description |
| --- | --- |
| Variable Group | Gravity |
| Variable | AngleCorrection |
| Valid Values | 0.0–1.0 |
| What it does | Preserves original branch angle. |
| Detailed guidance | Prevents over-bending by blending between the natural angle and new curve. |

### Scale

The **Scale** Node controls how big or small parts of your plant are. Think of it as the resize tool for vegetation — it lets you make trunks thicker, branches longer, or leaves larger (or smaller).

**What It Does**

* Scales the whole plant mesh.

**When to Use It**

* **Quick adjustments**: Make a preset tree taller, wider, or smaller to better fit your scene.
* **Variation**: Create multiple plant variations by scaling them differently (so not every tree looks the same).

**Pro Tip for Beginners**

* Use small changes (like **10–20% scale** **differences**) to quickly make believable variations of the same plant.
* For forests, mix scaled-up and scaled-down versions of the same tree to avoid repetition.

| Category | Description |
| --- | --- |
| Variable Group | Scale |
| Variable | Scale |
| What it does | Changes the size of the plant. |
| Detailed guidance | Scales trunks, branches, or leaves up or down. Works like a resize tool.  Use slight changes (10–20%) to add natural variation. |

### Remove Branches

The **Remove Branches n**ode gives you control over which branches stay and which ones get trimmed away. It’s like a digital pruning tool that helps shape your plant’s overall look, or simplify it for performance.

**What It Does**

You can remove branches based on different rules:

* **Length**: Cut off branches that are too short or too long.
* **Radius**: Remove thin or thick branches depending on your needs.
* **Light:** Remove branches that don’t get enough sunlight (helps mimic natural growth).
* **Age:** Older branches can be pruned away.
* **Generation:** Decide how many “levels” of branching should remain (e.g., trunk only, or trunk + 2 layers of branches).

**When to Use It**

* **Artistic control**: Shape the silhouette of your plant (make it fuller, sparser, or more stylized).
* **Performance**: Reduce unnecessary small branches for background trees.
* **Realism**: Mimic how trees naturally lose lower or shaded branches.

**Pro Tip for Beginners**

* **Start simple**: try adjusting Length or Generation first — these are the easiest to understand visually.
* Use Light-based removal if you want a tree that feels more realistic (like a forest tree with fewer lower branches).
* For large environments, use removal to keep distant vegetation lighter and faster to render.

| Category | Description |
| --- | --- |
| Variable Group | Remove Branches |
| Variable | BranchRemoveBasis |
| What it does | Sets the rule for pruning. |
| Detailed guidance | Branches can be removed based on length, thickness, age, generation, or light exposure. This mimics natural pruning or lets you simplify plants.  Use light-based removal for realistic forest trees (fewer shaded branches). |

### Mesh Builder

The **Mesh Builder** node is where your plant design turns into a **real 3D model** that you can see, use, and export in Unreal. Everything you set up in the earlier nodes comes together here to form the actual **mesh**.

**What It Does**

* **Generates a 3D mesh** for your plant from the structure defined by the graph.
* **Applies materials** to the mesh (textures, colors, surface details).
* **Adds detail with displacement** if you want extra surface variation (like bark bumps or leaf veins).

By default, it uses the materials from the preset you loaded, but you can swap them for your own custom materials if you want a different look.

**Settings Groups**

* **Material** – Choose or change what textures and surfaces your plant uses.

  + Example: Replace the bark material with a mossy one.
* **Mesh** – Adjust how the mesh is generated (overall shape, resolution, quality).

  + Example: Higher quality for hero plants, lower for background.
* **Displacement** – Add fine surface details by pushing/pulling the mesh surface.

  + Example: Add bark roughness without needing a super high-poly model.

**When to Use It**

* The Mesh Builder is a **required step** to actually see your plant in 3D.
* Customize materials if you want your plant to stand out (different bark, leaf colors, seasonal looks).
* Use displacement for **close-up** plants where small details will be noticed.

**Pro Tip for Beginners**

Think of the Mesh Builder like a **final bake**: it takes your plant’s structure (the recipe) and turns it into a finished dish (the model).

* Keep settings simple at first: just use the preset materials.
* Once you’re comfortable, start experimenting with custom materials and displacement for more artistic control.

| Category | Description |
| --- | --- |
| Variable Group | Mesh Builder |
| Variable | **Material**: Pick or replace textures/materials (e.g., bark, leaf surface).  **Mesh**: Defines how the plant’s structure becomes a 3D mesh.  **Displacement**: Adds surface detail like bark bumps or leaf veins. |
| What it does | Turns your plant into a real 3D model. |
| Detailed guidance | Takes the structure built by nodes and generates a mesh with materials applied. Displacement adds realism without increasing polycount.  Use default materials at first; add custom ones later for uniqueness. |

### Foliage Palette

The **Foliage Palette** node is like your leaf and branch library. It shows you what types of foliage (leaves, needles, flowers, etc.) are being used on your plant, and it lets you swap them out if you want a different look.

**What It Does**

* **Visualizes foliage meshes**: You can see the different leaves or small meshes attached to your plant.
* **Replace foliage meshes:** Swap default leaves for your own meshes (e.g., turn oak leaves into maple leaves).
* **Remove foliage meshes**: Take out certain leaf types if you want a bare or simplified plant.

  The **placement of leaves** (where they appear) comes from the preset and **cannot be changed** here — only what the leaves look like.

**When to Use It**

* **Customization**: Quickly change the look of a plant without rebuilding the whole structure.
* **Variety**: Use different leaf meshes on the same preset to make unique versions of the same tree species.
* **Optimization**: Remove high-poly foliage meshes and replace them with simpler ones for performance.

**Pro Tip for Beginners**

* Start by just **swapping leaf meshes** to create variations — it’s the fastest way to make your forest look more diverse.
* You can create a few trees with the same structure but different foliage meshes to make your environment feel natural and less repetitive.

| Category | Description |
| --- | --- |
| Variable Group | Foliage Palette |
| What it does | Lets you see and change the foliage meshes. |
| Detailed guidance | You can swap leaves or needles with your own meshes, or remove them entirely. Placement is controlled by the preset and cannot be changed here.  Quickly create variation by swapping leaf types (oak to maple). |

### Foliage Distributor

The **Foliage Distributor** node controls **how leaves and small branches are spread out** across your plant. It gives you a simple way to make a plant look **dense and bushy** or **sparse and pruned** depending on your needs.

**What It Does**

* Adjusts how many buds, leaves, and small branches stay on the plant.
* Uses a concept called **ethylene** (a plant growth hormone that causes leaves to drop as the plant ages).
* By setting an **Ethylene Threshold**, you can decide how sensitive the plant is to this process.

**Key Setting**

* **Ethylene Threshold**: Think of this as a slider that changes how “full” your plant looks:

  + **Higher Threshold** means more leaves and branches stay making plants look dense and bushy.
  + Lower Threshold means more leaves and branches fall off making plants look sparse and pruned.

**When to Use It**

* **Dense look**: Use for jungles, lush forests, or healthy plants where you want lots of greenery.
* **Sparse look**: Use for autumn scenes, dry climates, or stylized/optimized plants where fewer leaves are needed.

**Pro Tip for Beginners**

If you’re not sure where to start:

* Set a **higher threshold** for lively, fresh plants.
* Lower the threshold gradually to create natural variation (like some trees in the forest looking older or drier).
* Mixing both in one scene makes the environment feel **more natural and believable**.

| Category | Description |
| --- | --- |
| Variable Group | Foliage Distributor |
| Variable | EthyleneThreshold |
| Valid Values | Adjustable slider (0.0–1.0) |
| What it does | Controls how dense the plant looks. |
| Detailed guidance | Based on ethylene, the plant hormone that causes leaves to fall.  High threshold: dense and bushy.  Low threshold: sparse and pruned. |

### Bone Reduction

The **Bone Reduction** node helps you make your plant’s skeleton simpler. In PVE, when you export a plant as a **skeletal mesh**, the system creates bones so branches and leaves can move (for example, swaying in the wind).

Sometimes, these skeletons can have **too many bones**, which can slow down performance in a game or large scene. The Bone Reduction Node lets you **cut down the number of bones** to make things run faster.

**What It Does**

* **Keeps performance high** by lowering bone count.
* **Simplifies animations** so your plants don’t eat up too much processing power.
* **Trade-off**: fewer bones means less realistic wind movement.

**When to Use It**

* **Use Bone Reduction** if you’re creating:

  + Large forests or scenes with **hundreds/thousands** of plants (you need speed).
  + Background vegetation where **fine wind details** don’t matter.
* **Avoid too much Bone Reduction** if:

  + The plant is close to the player or camera.
  + It’s a **hero asset** (important tree/plant in a cutscene or gameplay moment).

**Pro Tip for Beginners**

Start with **default bones,** then try using Bone Reduction if your scene starts running slowly. Think of it like lowering the “detail” of movement to gain performance.

| Category | Description |
| --- | --- |
| Variable Group | Bone Reduction |
| Variable | Bone Reduction |
| What it does | Simplifies the plant’s skeleton. |
| Detailed guidance | Reduces the number of bones in a skeletal mesh. Fewer bones means better performance, but less accurate wind animation.  Use on background plants for speed; keep detail on close-up plants. |

### Output

The **Output** node is where you take everything you’ve built in your Procedural Vegetation graph and turn it into a usable asset in Unreal Engine. Think of it as the **export button** for your plant.

**What It Does**

The Output Node lets you save your plant in different formats depending on how you want to use it in your project:

* **Static Mesh**: A standard Unreal mesh with no Nanite or skeletal data. Good for simple plants or if you don’t need high detail.
* **Static Mesh with Nanite Foliage:** Same as above, but optimized with **Nanite**, Unreal Engine’s virtualized geometry system. Perfect for super-detailed vegetation with great performance.
* **Skeletal Mesh**: A mesh that has a skeleton (bones) so it can move or react to wind/physics. Great for trees or plants you want to sway or bend.
* **Skeletal Mesh with Nanite Foliage:**Best of both worlds: highly detailed + animated for wind and motion.

If your foliage doesn’t already have bones, the Output Node will **automatically generate skeletal data** for you when you pick a Skeletal Mesh option.

**When to Use Each Option**

* **Static Mesh:** For small plants, bushes, or background details where animation isn’t needed.
* **Nanite Static Mesh**: For forests, jungles, or close-up plants where detail matters.
* **Skeletal Mesh**: For vegetation that needs to move
* **Nanite Skeletal Mesh**: For dense forests with detail and wind animations in cinematic shots where you need both realism and movement.

**Pro Tip for Beginners**

If you’re just starting out:

* **Use Static Mesh with Nanite** for most cases — it’s simple and looks great.
* Move to **Skeletal Mesh options** once you’re comfortable and want to add motion like wind interaction.

| Category | Description |
| --- | --- |
| Variable Group | Output |
| Valid Export Options | * Static Mesh * Static Mesh with Nanite * Skeletal Mesh * Skeletal Mesh with Nanite |
| What it does | Exports your plant into a usable mesh. |
| Detailed guidance | * Static Mesh: Simple, no animation. * Nanite Static Mesh: High detail and performance. * Skeletal Mesh: Includes bones for movement. * Nanite Skeletal Mesh: Best of both: detail and motion.   Use Nanite Static Mesh for most cases; switch to Skeletal if you need wind animation. |

## UE Content upon Import

[![](https://dev.epicgames.com/community/api/documentation/image/cf74c666-6020-4269-b801-78c952ffb9a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf74c666-6020-4269-b801-78c952ffb9a6?resizing_type=fit)

Once the preset is loaded in UE, you get the following:

* Root Folder (Species name like: Tree\_European\_QuakingAspen\_01)

  + Instances (Sub folder)
  + Materials (Sub folder)
  + Textures (Sub folder)
  + WindSettings (Sub folder)

    - PVE Wind Simulation Data Asset
* Skeletal Mesh with Nanite Foliage for each variation
* Skeleton for each variation
* PVE Graph Editor asset
* PVE Preset Data Asset

### Example end-to-end User Flow

1. Download a Quixel Megaplants Preset pack via one of the following (not available for 5.7 Preview, only for 5.7 release onward):

   1. Fab in Launcher
   2. Fab UE Plugin
   3. Fab.com
2. Open the Asset Zoo sample scene to review the vegetation variations that come pre-built with the download.
3. Use pre-built skeletal mesh variations as-is to start placing them by hand, instancing, duplicating or using them in your PCG volumes to scatter.
4. Double-click on PVE Graph Editor asset to see the node graph for each variation
5. Edit the variations using various parameters of the nodes or duplicate the node graph to create a new variation altogether
6. Export using the Output node of the node graph of the variation you wish to export, selecting one of the desired output mesh type
7. Start placing them by hand, instancing, duplicating or using them in your PCG volumes to scatte

Required Plugins

* PVE
* PCG
* Dynamic Wind
* Nanite

Project Settings

* Nanite should be enabled
* Nanite Foliage should be enabled

Use with PCG to allow for wind animation

## Key Botanical Concepts

When using PVE to generate vegetation in your project, there are several key terms that you should familiarize yourself with:

* Phototropism: The orientation of the vegetation growth in response to light. In PVE, this plays an important role in growing the branches in a more realistic manner.
* Hormones:

  + Ethylene:

    - Ethylene acts as a plant hormone, playing a significant role in various growth and developmental processes, including seed germination, root and shoot elongation, flowering, fruit ripening, and leaf/flower senescence. It can promote or inhibit growth depending on the concentration and species.
    - In PVE, it has a major contribution in controlling the growth of the plant and where and how many new leaves/foliage will be present.
* Branch Generations:

  + This functionality specifies the hierarchical depth of branches within the plant structure. It determines how far a branch is removed from the trunk and is used to control growth, appearance, and behaviors at different structural levels.

* Generation 0: The trunk or main stem.
* Generation 1: Branches that emerge directly from the trunk.
* Generation 2: Sub-branches growing from generation 1, and so forth.

* Some settings like material can be setup differently for different generations

* Axil angle:

  + Often called the insertion angle is the angle between a lateral organ—like a leaf, flower stalk, or lateral branch—and its parent axis (the stem/branch it emerges from).

0° ≈ parallel to the parent axis (pointing along it)

90° ≈ perpendicular (sticking straight out)

>90° ≈ drooping back toward the ground relative to an upright parent

This angle affects light capture, shedding of rain/snow, and overall plant architecture. It varies by species, organ type, age, and environment.

* [experimental](https://dev.epicgames.com/community/search?query=experimental)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [PVE Presets](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#pvepresets)
* [Key Supported Workflows](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#keysupportedworkflows)
* [PVE Nodes](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#pvenodes)
* [Procedural Vegetation Preset Loader](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#proceduralvegetationpresetloader)
* [Carve](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#carve)
* [Gravity](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#gravity)
* [Scale](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#scale)
* [Remove Branches](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#removebranches)
* [Mesh Builder](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#meshbuilder)
* [Foliage Palette](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#foliagepalette)
* [Foliage Distributor](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#foliagedistributor)
* [Bone Reduction](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#bonereduction)
* [Output](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#output)
* [UE Content upon Import](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#uecontentuponimport)
* [Example end-to-end User Flow](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#exampleend-to-enduserflow)
* [Key Botanical Concepts](/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine?application_version=5.7#keybotanicalconcepts)
