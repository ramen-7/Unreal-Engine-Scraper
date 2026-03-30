<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7 -->

# Unreal Engine 5.7 Release Notes

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
5. [What's New](/documentation/en-us/unreal-engine/whats-new "What's New")
6. Unreal Engine 5.7 Release Notes

# Unreal Engine 5.7 Release Notes

Overview of new and updated features in Unreal Engine 5.7

![Unreal Engine 5.7 Release Notes](https://dev.epicgames.com/community/api/documentation/image/9a5467f6-4ed5-4f95-9d1a-0967d85fea26?resizing_type=fill&width=1920&height=335)

 On this page

## What's New?

The release of Unreal Engine 5.7 brings further improvements to the UE5 toolset. This release delivers improvements in a wide variety of areas, including Rendering, Character and Animation, Worldbuilding, PCG, and more.

This release includes improvements submitted by our community of Unreal Engine developers on GitHub. Thank you to each of these contributors to Unreal Engine 5.7:

AlexanderVeselov-arm, AlexBlackfrost, Almax27, andreibazi, az6667, Bit-Rot, Brian-PD, brpendle-ti, bturner, chrysos8201, ckendal3, ColinGulliver, CookiePLMonster, Darcy3000s, dasherman-ea, davidbaack, dmergele, DoubleDeez, DrewWeth, DTG-Will-Marshall, dyanikoglu, erebel55, Eric2-Praxinos, Erlandys, faisa-believer, foobit, gamethread, geordiemhall, glecko, GreenLightning, guansdu, H3mul, IngSubstance, iniside, jamesfAnet, jamespark-unreal, JasonCoombs, jdamdami, jerobarraco, jeysym, Jiboo, JohnJFarrow, Jordonbc, jorge-axiomvfx, jorgenpt, jpritchard1010, KaosSpectrum, KarimLUCCIN, KeithRare, kimkun07-k, kissSimple, klukule, KXOC, laurencei, lclara-BARB, LHG-JonAnderJimenez, ligazetom, LightKL, lsandersljungberg, LucaFranzo98, Maigo, MarcusSvensson92, Mario-Azcona, MartinWickhamFB, Mattiwatti, melku, michael-buschbeck-ms, Minus4-44, moumee, nickdarnell, phochstrasser, PICO-XR, QRare, r457-Ao2, rdunnington, reduf, redxdev, RiotJDebern, rohyunsang, sareali, serhanio, SilverWinter0511, slonopotamus, SoulSharer, sportbikerr1, ssutherland-riot, SukenderDontNod, Sythenz, teddemunnik, tioez326, tokyocplusplus, Tt-Wes, tustanivsky, Vaei, vladbelousoff, vogoltsov, WangKan, Wizzard033, wmiller, x157, yangskyboxlabs, yoonbigbear, zachlute-arenanet, ZeroEightSix, ZeroErrors, zhou-

## Rendering

### MegaLights (Beta)

[![MegaLights Beta](https://dev.epicgames.com/community/api/documentation/image/058f0ddf-8962-4d66-b974-59696f91cc07?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/058f0ddf-8962-4d66-b974-59696f91cc07?resizing_type=fit)

**MegaLights** is now in Beta, with improvements to noise reduction and overall performance. This also brings support for the following features:

* Directional Light
* Niagara Particle Lights
* Translucency
* Hair Strands

### Niagara Heterogeneous Volumes

**Heterogeneous Volumes** is now in Beta. This update focuses on improvements to shadow-casting with the following new features:

* Cascade shadows for the directional light.
* Beer Shadow Map support for Epic scalability, which provides:

  + Drastically improved shadow creation time.
  + Constant-time shadow query.
* Shadow Mask pre-pass, which removes added VGPR pressure in Deferred Lighting.
* Enabling shadow casting no longer requires an editor restart and shader compilation.

### Substrate

![Substrate materials](https://dev.epicgames.com/community/api/documentation/image/fec5e9d2-ba48-4c89-8d3d-c4499d2d9e51?resizing_type=fit)

**Substrate materials**, which are production-ready and enabled by default as of UE 5.7, represent a modular, physically grounded material framework that replaces the fixed shading models with a system designed for expressive control, scalable performance, and long-term flexibility.

It supports two rendering paths:

* The **Adaptive GBuffer**, which enables advanced features like per-pixel topology and layered closures on modern hardware.
* The **Blendable GBuffer**, a simplified fallback that ensures broad platform compatibility.

### Nanite Foliage and Skinning (Experimental)

![Nanite Foliage](https://dev.epicgames.com/community/api/documentation/image/864e19a2-1bec-4b3b-a332-12e5a62cfb0c?resizing_type=fit)

**Nanite Foliage** is an industry-leading rendering path, which at its core is comprised of three integral systems:

* **Nanite Assemblies**, which manage the foliage part instances into one cohesive unit.
* **Nanite Skinning**, which determines the dynamic behavior it will have with systems like wind.
* **Nanite Voxels**, which are pixel sized voxels that are able to retain details, animation and material characteristics based on the distance from the camera, all at a fraction of the original cost.

When combined, this allows for more robust worlds to be imagined with lifelike and animated foliage that can be delivered within a 60fps budget on current generation hardware.

New Features:

* Nanite Assemblies, for building foliage assets using instanced parts to keep asset sizes small.

  + Blueprint API for building Nanite Assemblies.
  + As well as in-editor tooling to facilitate Nanite Assembly creation from selections.
  + Importer support for USD. Exposed USD schemas to use in DCC tools to mark up scenes to import as assemblies.
* Skeletal Mesh-driven dynamic wind; trees are skeletal meshes and the new Dynamic Wind plugin enables procedural wind to affect their bones.
* Nanite Voxels, for efficiently rendering foliage geometry in the distance.
* TSR Thin Geometry detection to better handle foliage.

### SMAA (Experimental)

Mobile and desktop renderers now support **Subpixel Morphological Anti-Aliasing (SMAA)**. You can enable it with the mobile renderer using the CVar `r.Mobile.AntiAliasing=5`, and with the desktop renderer using the CVar 
`r.AntiAliasingMethod=5`.

This feature improves visual fidelity by providing high-quality edge smoothing with minimal performance impact, it is an efficient technique for mobile games.

* SMAA anti-aliasing is enabled on all platforms.
* Adjust quality settings using `r.SMAA.Quality`
* Adjust edge detection between color or luminance using `r.SMAA.EdgeMode`
* Improve edge smoothness without heavy GPU cost.

Currently an experimental feature. The quality settings provide for tuning tradeoffs between performance or visual fidelity.

## Character and Animation

### Motion Matching Chooser Integration (Experimental)

In UE 5.7, we've brought our first iteration of **Motion Matching** integrated into **Choosers**! We're doing this because it gives users control over what assets are valid for selection in Motion Matching, something that in previous releases was only possible at the database level, not at the individual asset level.

This means you can search for the best pose, but also filter the per asset results based on extra conditions like game logic through the Chooser.

A new Pose Search field in the Choosers manages this complexity, along with integrated debugging from Motion Matching into Choosers.

This feature is Experimental.

### Blendshapes and Sculpting Tools

[![Blendshapes and Sculpting Tools](https://dev.epicgames.com/community/api/documentation/image/af36a345-b993-4cec-b75a-24d9d291797f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af36a345-b993-4cec-b75a-24d9d291797f?resizing_type=fit)

Bring the flexibility of industry-standard sculpting workflows into Unreal Engine. This is an update on the Skeletal Editor tools that now provides the ability to create and edit morph shapes, bones, and skin weights seamlessly.

* Instantly move between placing bones, painting weights, and sculpting blendshapes on a Skeletal Mesh.
* New **Morph Target Viewer**.
* Shapes adapt to changes in mesh topology .
* Equip animators with expressive tools for studio-quality performances.

### World Collisions for Control Rig Physics

![World Collisions for Control Rig Physics](https://dev.epicgames.com/community/api/documentation/image/f97c5a25-e5a2-4963-a0d8-5008a3f97b32?resizing_type=fit)

Bring level collisions into your Control Rig Physics simulations. Use existing world geometry and physics bodies to create believable contacts, pushes, and interactions.

* World collision support in Control Rig physics with one-way interactions.
* Use level meshes and physics bodies as colliders.
* Drive contact with props, floors, and environment during sim and playback.

### Control Rig Dependency View

![Control Rig Dependency View](https://dev.epicgames.com/community/api/documentation/image/063c4de8-913c-4c35-8a0c-7ef18dc2a37b?resizing_type=fit)

Understand how rig elements connect and update over time with a dedicated Dependency View. Visualize relationships between controls, bones, and modules to simplify debugging.

* Explore parent-child and metadata relationships at a glance.
* Debug rigs and modules with clearer visibility into data flow.
* Familiar dependency structure visualization.

### FBIK and Retargeting Performance

[![FBIK and Retargeting Performance](https://dev.epicgames.com/community/api/documentation/image/2014353d-92d7-4b03-b416-701dcfd75e58?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2014353d-92d7-4b03-b416-701dcfd75e58?resizing_type=fit)

We added performance improvements and control in Full Body IK and IK Retargeter. This provides a way for you to have performant retargeting at runtime.

* Improve posing with FBIK without a heavy performance cost (~20% speed increase).
* Use the stretch limb solver in IK Rig for performant runtime retargets.
* Use the FK rotation mode **Copy Local** for faster rotation transfer per chain.
* Enable performance profiling on the retarget stack.
* Add a LOD threshold per retarget operator.

### Better Foot Contact and Proportioned Retargeting

![Better Foot Contact and Proportioned Retargeting](https://dev.epicgames.com/community/api/documentation/image/3aa5e368-1f24-490c-b408-9d59fbbf880b?resizing_type=fit)

We improved the IK Retargeter for better handling of ground contact and vast proportioned characters.

This provides a better transfer of animation across a large variety of characters, so you can do faster art direction. You can now do all the following:

* Define crotch height to prevent the pelvis from crashing to the ground, and maintain vertical motion.
* Add the floor constraint to feet to maintain vertical position when close to the floor.
* Use the FK translation mode **Orient and Scale** to transfer bone translation data.
* Add the **Stretch Chain** operator to match the source retarget chain or scale it.
* Use the **Stretch Limb** solver to control squash and stretch of limbs.
* Change the pivot of the **Source Scale** to a different bone for motion capture or gameplay.
* Add the **Filter Bones** operator to remove high frequency noise while retargeting on larger characters.

### Spatially Aware Retargeting (Experimental)

![Spatially Aware Retargeting (Experimental)](https://dev.epicgames.com/community/api/documentation/image/7663d6ad-8c8d-4c1a-908d-2955e0d1bcba?resizing_type=fit)

**Spatially Aware Retargeting** provides a way for artists to transfer animations between different characters without having to worry about self collision.

This reduces the need to clean up the animation after a retarget.

* We added a **Body Interactions** operator to push IK goals out using physics to prevent self collision.
* We added a **Relative IK** operator to move IK goals relative to contact lengths from the source to the target.

### Sequence Validator (Experimental)

[![Sequence Validator (Experimental)](https://dev.epicgames.com/community/api/documentation/image/b65fcd33-ae61-4071-b5b0-286fd0964eb6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b65fcd33-ae61-4071-b5b0-286fd0964eb6?resizing_type=fit)

The **Sequence Validator** provides a way for cinematic artists to check if there are any content errors in their sequences. This reduces the amount of potential issues that can happen during a production while working in Sequencer.

Using it, you can:

* Queue multiple sequences and their sequence hierarchies for potential issues.
* Check if sections in a sequence are off from the camera cut or playback range.
* Check if there are any unassigned bindings or assets on sections.
* Check if sections start and/or end on whole frames.
* Review results and navigate directly to where the problem is in each sequence.

### Ease Curve (Beta) and UX Improvements

[![Ease Curve (Beta) and UX Improvements](https://dev.epicgames.com/community/api/documentation/image/4d7f7b9b-af72-47fc-8f19-fcc586ac17cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d7f7b9b-af72-47fc-8f19-fcc586ac17cd?resizing_type=fit)

You can now use the **Ease Curve** tool from Motion Design in Sequencer. You can enable it using the Ease Curve plugin

Additionally, this update brings more cohesive behaviors for better usability so you can iterate faster.

* Use the Ease Curve tool to apply and save different Ease Curve presets in Sequencer, Curve Editor, and UMG.
* Adjust scale similar to the Details panel in the Sequencer tree using scale lock.
* Improved timeline display of sequence hierarchies to display both current and parent sequence time.
* Expand Blueprint and Python capabilities for accessing track states (Solo, Mute, Deactivate, Lock, and Pin).
* Improved transform baking to include time warp.
* Added new **Binding ID** and **Sequence ID** columns to the navigation tool.

The Ease Curve Tool is currently in Beta.

### Dataless Mutable (Experimental)

[![Dataless Mutable (Experimental)](https://dev.epicgames.com/community/api/documentation/image/4fa976ba-2611-4b95-ba7d-bd7b7907a2a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fa976ba-2611-4b95-ba7d-bd7b7907a2a7?resizing_type=fit)

Speed up iteration and streamline your workflow with dataless Customizable Objects. Parameter inputs are handled at runtime instead of compile time, giving you faster compiles, better encryption, and smaller packages.

* Convert any Customizable Object to dataless.
* Enjoy faster compile times with runtime parameter handling.
* Use encryption and packaging just like any other UE asset.

### Selection Sets

[![Selection Sets](https://dev.epicgames.com/community/api/documentation/image/c84ba3d4-3cc3-4931-91b1-325b9ef5cefb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c84ba3d4-3cc3-4931-91b1-325b9ef5cefb?resizing_type=fit)

Animators need quick access to multiple selections throughout their process. This may be multiple controls within one rig, but may also be multiple controls and/or transforms across various assets. Currently animators rely on custom tools like Gui Pickers to do this, so we wanted to build a more native version, similar to popular plugins in other tools.

### Animation Mode UX and QOL

We made improvements to **Animation Mode**.

Our **Constraints**, **Space Switching**, and **Snapper** tools are now consolidated into one new **Constraint** window..

Also related to Constraints, we added a few new options to the creation process.

* **Current Frame**: This is the previous standard functionality. It makes an ON key at the current frame and compensates all keys forward.
* **From Start (new)**: Takes the current frame's offset and keys it on the first frame of your shot instead of the current frame.
* **Infinite (new)**: Doesn't add keys. Instead, it applies the current frame's offset to the entire sequence.

Pose Library, Tween Tools, Constraints, Selection Sets (new) and Animation Layers now toggle their corresponding windows on or off based on their icon state. Their position and size within your layout is also saved.

You can assign toggling these windows to hotkeys.

## MetaHuman

### MetaHuman Creator

MetaHuman Creator in Unreal Engine is now available on Linux and macOS, bringing powerful, integrated digital human creation to your preferred platform. If you haven’t already migrated from the MetaHuman Creator web application, follow [our migration guide](https://dev.epicgames.com/documentation/en-us/metahuman/metahuman-creator-migration-guide?application_version=5.6) for instructions on how to bring your existing MetaHuman character into Unreal Engine to continue authoring!

[![](https://dev.epicgames.com/community/api/documentation/image/4312e68d-0c2d-47a2-9fb3-bb450bade256?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4312e68d-0c2d-47a2-9fb3-bb450bade256?resizing_type=fit)

We’ve enhanced the [body mesh conformation process](https://dev.epicgames.com/documentation/en-us/metahuman/body-conform-controls) with support for varied poses, and introduced UV-space vertex correspondence between the conform template and model meshes – enabling more accurate results with less effort. The parametric body controls are also now more intuitive, making it easier to stay within human proportions with increased precision and control.

With this release you can automate and batch process nearly all editing and assembly operations for MetaHuman character assets [using Python](https://dev.epicgames.com/documentation/en-us/metahuman/python-scripting-for-metahuman-creator) or Blueprints. For the first time, more deeply integrate MetaHuman Creator into your pipeline and creative workflow with an API that supports sculpting, conforming, wardrobe, rigging, and textures, streamlining full character assembly.  Preview edits live in MetaHuman Creator, run them interactively in Unreal Editor or a compute farm for offline processing.

### MetaHumans in Unreal Engine

![](https://dev.epicgames.com/community/api/documentation/image/ab987bf8-a6d1-4df9-801b-a3045cda52f9?resizing_type=fit)

The Unreal Engine Groom Plugin now enables finer control in [shaping and animating hair strands](https://dev.epicgames.com/documentation/en-us/metahuman/hair-art-directability) with a joint-based workflow. You can now blend simulations with art-directed motion, access full use of skeletal mesh animation workflows, and achieve greater artistic freedom with enhanced selection sets and paint tools. The toolset offers full compatibility for MetaHuman grooms originally created in Houdini.

### MetaHuman Animator

Real-time animation from MetaHuman Live Link sources can now be accessed via a Blueprint interface, with [an example graph](https://dev.epicgames.com/documentation/en-us/metahuman/blueprint-examples) provided in our documentation.

|  |  |
| --- | --- |
|  |  |

The workflow for [generating calibration data](https://dev.epicgames.com/documentation/en-us/metahuman/generate-calibration) from the checkerboard take – captured using a stereo camera pair – has been improved to provide better automatic frame selection, visualization to aid manual frame selection, and repeatable configurations across multiple takes.

Combined with the new [MetaHuman Animator Calibration Diagnostics plugin](https://dev.epicgames.com/documentation/en-us/metahuman/calibration-diagnostics-tool) (experimental) to validate calibration against performance footage to more easily determine if it is the best calibration to use.

### MetaHuman Capture

We’ve improved the real-time animation options in the Live Link Face [iOS](https://apps.apple.com/us/app/live-link-face/id1495370836) and [Android](https://play.google.com/store/apps/details?id=com.epicgames.facelink) applications by extending the range of supported cameras.

With Live Link Face, you can now generate real-time facial animation using an external camera on supported Android devices or iPads (Note: Apple's iOS does not support external cameras at this time).  Video can be recorded from an external camera on iPad only.

You can also generate animation in realtime by selecting from any on-device camera using Live Link Face on iOS & Android.  Video can be recorded from the on-device camera on iOS only.

### MetaHuman for Houdini

The latest [MetaHuman for Houdini](https://www.fab.com/listings/7bbdfbb5-5eaf-4aa6-b32b-b8b048ebea25) update brings [parametric groom tools](https://dev.epicgames.com/documentation/en-us/metahuman/parametric-hairstyle-generator), a guide-driven workflow for creating hairstyles using pre-authored data. The toolset includes a follicle generator to handle density and positioning around the hairline that generates guides based on flow, length, and volume parameters, as well as hair strand interpolation and styling for advanced detailing such as clumpiness.  This is a fast and approachable way to block and iterate new hairstyles.

Meanwhile, for those wanting to learn how to create more advanced hairstyles, we’ve published the new [MetaHuman Groom Advanced Kit for Houdini](https://www.fab.com/listings/165c4244-482f-4e37-9200-dd782972cdde) on Fab as an extra learning resource.

[MetaHuman for Houdini](https://www.fab.com/listings/7bbdfbb5-5eaf-4aa6-b32b-b8b048ebea25) is now available for Linux.

### MetaHuman for Maya

The latest update to [MetaHuman for Maya](https://www.fab.com/listings/9e3bf55e-d4c3-44fc-a3d4-ec4cb772ec29) is available on Linux and introduces support for Maya 2026.

## Worldbuilding

### Custom HLODs

[![Custom HLODs](https://dev.epicgames.com/community/api/documentation/image/74d604f2-8453-41e5-8a0a-dce03d7a35a4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74d604f2-8453-41e5-8a0a-dce03d7a35a4?resizing_type=fit)

When using the provided automatic HLOD generation methods, the output may not always meet the project's requirements and is bound to mesh components.

**Custom HLODs** **support** addresses this limitation by giving you the ability to provide your own custom HLOD representations for individual actors or groups of actors.

You can use the new World Partition Custom HLOD actor class in two ways:

* **Inject custom representation directly**: You can inject the custom representation as-is into the HLOD runtime partition and optionally use it as input for parent HLOD Layers.
* **Provide a custom source only**: You can use the custom representation as input to the HLOD generation process without adding it to the world itself.

### HLODs Setup UX

[![HLODs Setup UX](https://dev.epicgames.com/community/api/documentation/image/cd130b57-a597-4ee4-8339-4138a2f39fb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd130b57-a597-4ee4-8339-4138a2f39fb1?resizing_type=fit)

We reworked **World Settings > World Partition**'s HLODs layers configuration and HLODs layers assets to improve usability when creating or editing a setup.

## Procedural Content Generation (PCG)

### PCG Framework is Production Ready

[![PCG Framework is Production Ready!](https://dev.epicgames.com/community/api/documentation/image/c4b2d3f4-88c2-4d92-a86c-109f29ba1b89?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c4b2d3f4-88c2-4d92-a86c-109f29ba1b89?resizing_type=fit)

The **Procedural Content Generation Framework (PCG)** is now Production Ready with the release of UE 5.7.

While the framework is in continuous development and continues to evolve, we are committed to support a stable environment so all productions can build and rely on this fast and iterative procedural content generation toolset for both runtime and in-editor use cases.

### PCG Editor Mode

![PCG Editor Mode](https://dev.epicgames.com/community/api/documentation/image/1af90ed6-327f-49df-ae70-7b1ba479472c?resizing_type=fit)

A new PCG-specific editor tool mode in Unreal Engine is now available. It offers a library of customizable tools leveraging the PCG framework such as draw spline, paint, or create volume, each with an associated PCG Graph and its parameters available for live editing.

You can use the provided tool-specific PCG graphs as-is or as examples to create and expand the library for your own needs.

If you used the UE 5.7 preview, your PCG Editor Mode settings might not have the default setup. If your PCG Editor Mode window does not open and instead shows an error, open the **Plugins - PCG Editor Mode Settings** in the **Editor Preferences**, then click **Reset to Defaults** in the upper right corner.

### Procedural Vegetation Editor

The **Procedural Vegetation Editor** is a new experimental plugin to create and edit vegetation meshes, supporting Nanite foliage, directly within Unreal Engine.

In this initial release, procedural vegetation assets you create are edited through the Vegetation Editor, a PCG-based node graph editor. Using the provided importer node and skeletal presets distributed in the plugin's content folder, you can:

* Modify the trees' shape through gravity, carve, and scale operators.
* Adjust leaves and branches distribution.
* Assign different leaf models.
* Export to skeletal mesh or static mesh, including support for Nanite foliage assemblies.

Create multiple variants through a single node graph or multiple node graphs in order to build a library of unique vegetation meshes for your project.

### Assets Workflows

![Assets Workflows](https://dev.epicgames.com/community/api/documentation/image/60b901b5-6abf-45e5-9ce5-5d3d0a87bcf7?resizing_type=fit)

You can now execute PCG graphs as standalone graphs, removing the need for the world context and for the graph to be generated from a PCG component.

This change adds support for :

* **Assets Creation workflows**, such as creating meshes using the geometry operations, textures with GPU operations or even generate PCG Data Assets such as attribute set tables by only running a standalone PCG Graph.
* **Assets Creation tools and plugins built on the PCG framework core**, like the new Procedural Vegetation Editor, benefit from its full feature set and future updates.

To enable PCG graph standalone execution, you can enable a new **Is Standalone Graph** option is available in each graph's settings. When this option is enabled, you have access to a right click menu **Generate Standalone Graph(s)** function as well as the possibility to generate, inspect, and debug from the graph editor using a Standalone Graph debug object.

### Custom Data Types

[![Custom Data Types](https://dev.epicgames.com/community/api/documentation/image/e13a1f9c-4d88-4dd0-a616-75e432df5b18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e13a1f9c-4d88-4dd0-a616-75e432df5b18?resizing_type=fit)

Since initial release, we hardcoded the list of supported data types in the PCG framework, preventing easy addition and support of new data types when extending the framework or creating interoperations with external plugins.

In UE 5.7, you can now add support for any custom data type within the types hierarchy and expand the framework, or use the framework core and feature set to build your own tool on top.

We upgraded the type selector as well to better indicate type relationships and provide for multi-selection.

### Polygon2D Data Type and Operators

[![Polygon2D Data Type and Operators](https://dev.epicgames.com/community/api/documentation/image/7b62a031-7df1-4f07-9126-b32b285d966f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b62a031-7df1-4f07-9126-b32b285d966f?resizing_type=fit)

We added a new **Polygon2D** data type to the list of supported data types in the PCG Framework.

Polygon2D data is useful to represent areas as a closed shape which can be converted to surfaces or splines data, for sampling or for specific operations.

We added a set of new operators to support this new data type:

* **Create Polygon 2D**: Takes as input point or spline data and converts them into polygon 2D.
* **Polygon Operations**: Allows for polygon-to-polygon operations such
  as intersection, union, and differences. Additionally, polygon 2D can
  be cut with paths, using splines, to subdivide or isolate shapes. For
  example, slicing a larger area using spline data in a grid pattern to
  create individual city blocks in a city generator graph.
* **Clip Paths**: allows to intersect or difference splines with polygon 2d shapes.
* **Offset Polygon**: applies an offset to the polygon 2d to make them larger or smaller with proper handling of overlaps.
* **Create Surface From Polygon2D**: will turn the polygon 2D into a surface that can be sampled using the Surface Sampler node to create points over its area.

### GPU Fast Geo Interop

![GPU Fast Geo Interop](https://dev.epicgames.com/community/api/documentation/image/492f3844-b167-4d9d-badb-b8041a39c59a?resizing_type=fit)

PCG GPU now leverages FastGeometry components to further improve on game thread performances when using the framework to generate and spawn a high density of static meshes, such as ground scatter and grass. It removes the need for any partition actors and creates local PCG components on the fly.

To benefit from the improvement, enable the PCG FastGeo Interop plugin in your project and set the CVAR `pcg.RuntimeGeneration.ISM.ComponentlessPrimitives` to 1.

### GPU Operators and Improvements

![GPU Operators and Improvements](https://dev.epicgames.com/community/api/documentation/image/2424bed6-535f-4a4a-b1fa-65de1d14b91a?resizing_type=fit)

New additions to the the PCG Framework GPU compute features set:

* **Scene Capture**: A new node for performing scene captures from the component origin to get and sample the scene color or depth for scattering.
* **Save Texture to Asset**: A new node for baking a PCGTextureData into a UTexture2D asset.
* **Support for Overrides**: parameters overrides are now supported on GPU nodes, including Num Elements counts for custom HLSL nodes.

Existing native operators upgraded with GPU compute support:

* **Cull Points Outside Actor Bounds**
* **Transform Points**

### UX Improvements

[![UX Improvements](https://dev.epicgames.com/community/api/documentation/image/a6fc5335-a851-4c0a-b9ae-0a450c50a9fb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a6fc5335-a851-4c0a-b9ae-0a450c50a9fb?resizing_type=fit)

As continued UX improvements when working with PCG, these are latest changes:

* **Parameters and Overrides type coloring and validation**: Params, override pins, constant output pins and their edges are  all now colored based on their type, matching the Blueprints types colors visual language. When an input can be of any type or is undefined, the pin and edge use white as its display color.
* **Parameters Min, Max, Units values**: You can now configure graph parameters with min/max values and units to display.
* **Data Viewports Controls**: We added additional in-graph editor data viewport controls and options to help preview data in specific contexts.

### Nodes and Operators

[![Nodes and Operators](https://dev.epicgames.com/community/api/documentation/image/ce3257c2-d984-4d53-83ee-ae00c666b349?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce3257c2-d984-4d53-83ee-ae00c666b349?resizing_type=fit)

Unreal Engine 5.7 introduces multiple native PCG elements and new options including:

* **Spline Intersection**: Finds intersecting splines in 3D and adds control points at intersection or returns the intersection points.
* **Split Splines**: Divides splines into multiple splines based on alpha, distance, key, or control points predicates.
* **Get Segment**: Returns a segment index point or spline from a point, spline, or polygon2D.
* **Spawn Spline Mesh Component Overrides**: Component class is now
  respected when spawning the spline mesh, and component property
  overrides in the Spawn Spline Mesh node are supported.
* **New PCG Blueprint Element Classes**: added new PCG elements classes
  including range-based overridable functions to support Structure of
  Array format changes introduced in native nodes in 5.6. Using the new
  elements prevents extra data transformation and improves performance
  when working with BP PCG Elements.
* **Get Execution Context**: Updated with Is Listen Server, Has Authority, and Is Builder context support.
* **Extract Attribute**: Retrieves a specific attribute at the given index and outputs it as a new attribute set.
* **Export Selected Attributes**: Exports data as Binary or JSON format for external use cases such as ML applications.
* **Attribute Remap**: Can now be driven by a curve.
* **Bitwise Operators**: Added shift left and shift right.
* **Boolean Operators**: Added NAND, NOR, XNOR, IMPLY, NIMPLY and automatic casting to Boolean from bitwise.
* **Math Operators**: New Add Modulo operation was added, useful to offset and re-order with indices.
* **Bounds from Mesh and Points from Mesh**: Added support for Skeletal Meshes.

### Python Interop Plugin

[![Python Interop Plugin](https://dev.epicgames.com/community/api/documentation/image/f38c4059-4332-46c8-b060-54c4b1d15adb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f38c4059-4332-46c8-b060-54c4b1d15adb?resizing_type=fit)

We added a new PCG plugin, which provides a new Execute Python Script node so you can run Python scripts while executing the graphs. You can provide the Python script directly as an input, or run it from a file on disk; you can set the path to the file dynamically through an override soft object path attribute or parameter.

## Developer Iteration

### Incremental Cooking (Beta)

**Incremental Cooking** is now beta in UE 5.7.

Incremental Cooking enables you to iterate faster on your target devices by reducing overall cooking time. Cook processes automatically analyze asset changes against output stored in Zen Server, and only cooks new updates made to your project's assets. This works across all native engine assets including Blueprints and World Partition tiles.

### CPP Tools - MSVC 14.44 Support

In Unreal Engine 5.7, we updated the default Microsoft Visual C++ compiler to MSVC 14.44.

### Build Health Tracking and Visualization (Experimental)

[![Build Health Tracking and Visualization (Experimental)](https://dev.epicgames.com/community/api/documentation/image/7a3307ca-81a8-42b0-ae1d-2500533774cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a3307ca-81a8-42b0-ae1d-2500533774cf?resizing_type=fit)

As part of the Horde analytics tooling, we've introduced a new **Build Health dashboard** experimental feature that gives teams a way to monitor and inspect which BuildGraph steps across the projects change lists are completing as expected, and/or reporting errors.

This is part of an ongoing development to provide built-in functionality in Horde to help teams better understand the most common cause of build failures, monitor pressure on agent pools and other useful build performance metrics that impede your iteration times.

## Audio

### Audio Insights (Beta)

![Audio Insights (Beta)](https://dev.epicgames.com/community/api/documentation/image/98c1d942-dec2-478b-8dd4-c0214f18f2be?resizing_type=fit)

**Audio Insights** is our primary tool for profiling and debugging audio. This targets everyone using audio in Unreal Engine. In this release, in addition to stabilizing the API and architecture, we are shipping a Beta version of Audio Insights. It includes the following additional core features:

**Monitoring**

* Start a live monitoring session without writing data to disk.
* Sound designers can observe the operation of a project, both in standalone and editor sessions, for longer periods of time without concern for having enough disk space.

**Editor Support**

* Use Audio Insights for in-editor use-cases in addition to PIE.
* Audio Insights now react to any audio interaction in the editor.

**Snapshots and Tail Recording**

* Writes the last live session data to disk on demand, up to 32 MB.
* Audio Insights can detect if a Live session has started, to connect to it

**Live Loudness Metering (UX Design)**

* Provides audio metering in Standalone, specifically for Loudness compliance.

**Scrollable Event History**

* Visualize a chronological text list of audio events such as sound start and stop with timestamps.
* Selecting a specific event moves the plot and other visualizations to the same timestamp in the data.

### MetaSound Node Configuration

**MetaSound Node Configuration** brings a new layer of expressibility to MetaSounds by making it possible for a node to alter its inputs and outputs. Node Configuration takes advantage of the MetaSound Editor Details panel to provide a pathway for modifying node interfaces and serializing sidecar data usable when a node renders audio.

In addition to giving sound designers and developers a way to create more nuanced and interactive nodes, Node Configuration provides improved UX. For instance, by cleaning up the node palette and by reducing the number of steps and rewiring complexity for many common MetaSound design tasks.

## Audio Subtitle Plugin

![Audio Subtitle Plugin](https://dev.epicgames.com/community/api/documentation/image/bbbe6a69-edda-477f-8777-614d04692e12?resizing_type=fit)

Audio subtitles are required for accessibility – dialogue systems, closed captioning, and voice chat. In Unreal Engine 5.7 we are further improving the Subtitle Plugin with the following additions:

* Subtitles can now be driven by other SoundBase types in addition to the original SoundWave and independent-timing support in 5.6.  Thus, subtitles can now base their time with respect to SoundCues or the top level of a MetaSound.
* By default, subtitles attached to `USoundWave` asset userdata are automatically played and stopped using the time the audio starts and stops.  However, there is a use case for using the subtitle duration property. We added an enum to provide a method for users to choose which duration to use.
* Multiple subtitles are now supported in the userdata asset.  Rather than using multiple assets for multiple subtitles associated with a given SFX, you now instead have all the subtitles in one asset.
* You can now enable or disable subtitles globally using `UEngine::bSubtitlesEnabled`.

## Audio Waveform Editor

![Audio Waveform Editor](https://dev.epicgames.com/community/api/documentation/image/3273165c-57be-4949-85c9-2930e3be6345?resizing_type=fit)

Often sound designers need to go back and forth from UE to an external tool when working with audio assets. To help their workflow in Unreal Engine 5.7, we added the display of markers and loop regions from imported sound files to the **Audio Waveform Editor**.

This includes additional quality of life improvements to expand the wave editor to be sufficiently featured so that sound designers can stay within UE for common audio editing tasks.

### Format / Channel Agnostic Types (CAT)

Sound designers often need to send and receive multichannel audio data between specific MetaSound nodes of varying formats and channel counts. In UE 5.7, audio programmers can code custom nodes containing input and output references using **Channel Agnostic Types (CAT)**:

* The new audio-rate data type provides a way for audio buffers to support multiple channels in one pin type.
* Nodes can now support multiple configurations for audio channel formats.
* Reduces clutter and complexity in MetaSound Graphs.

### Tech Audio Tools Sample

Tech Audio’s experience and usage of editor utility can be extremely beneficial to the game audio community. This initiative is to help onboard new developers to UE Audio, make working at scale less daunting, and serve as a starting point for developers to fork from in building their own project-specific tooling.

* A set of blueprint scripting utilities, tools, and graphs to help with working with Unreal Audio technology.
* Tech Audio would like to build an exemplar collection of editor utilities and workflows to use internally and showcase externally.

## Platform

### Android Platform Support

We improved workflows for developers building, packaging, and deploying Unreal Engine projects to Android devices.

* Deploy on Android 15 with 16kb page support
* Skip manual SDK setup adjustments on macOS.
* `bDontBundleLibrariesInAPK` setting is now enabled by default, ensures libraries are kept external for improved package size and deployment flexibility.

### Mobile Renderer

Unreal Engine 5.7 brings improvements and new features to the **Mobile Renderer**.

You can now use the Multipass deferred rendering mode which enables contact shadows and inset shadows.

In addition, SSAO, SSR and DFAO are now scalability options, which you can toggle at runtime, not needing to be set as project options and re-packaging anymore.

### Stereo Layer

Stereo layer components are now visible when the X axis points toward the camera. To enable legacy behavior (visible when X points away from the camera) use the console variable: ``` XR``.StereoLayers.UseLegacyFacing true ```.

Emulated stereo layers now support depth and are OpenXR compliant in how they render. You can turn off the new rendering using the console variable: ``` XR``.StereoLayers.RenderEmulatedLayerDepth false ```.

### OpenXR Application SpaceWarp

Application SpaceWarp is Meta's developer-driven optimization technology that can unlock extra computation power for suitable content. In UE 5.7, we implemented support not only for Meta's `XR_FB_space_warp` extension, but also for OpenXR runtimes that support 
`XR_EXT_frame_synthesis`
. This technology forces the application to render at half framerate, and synthesize every other frame with an updated head orientation - greatly reducing the load on the GPU.

Frame synthesis (and SpaceWarp) is controlled with `xr.OpenXRFrameSynthesis`. You can enable it at runtime, but it requires `r.Velocity.DirectlyRenderOpenXRMotionVectors=1`.

### OpenXR User Presence

We can now return events when a head mounted display is donned or doffed for OpenXR runtimes that support the OpenXR extension `XR_EXT_user_presence`. While this has been exposed through the **VRNotificationsComponent** in the past, the new method is more accurate and behaves the same between runtimes.

## Motion Design

### Motion Design Production Ready

![Motion Design Production Ready](https://dev.epicgames.com/community/api/documentation/image/e81e8e66-3059-4985-8234-17e755934f71?resizing_type=fit)

As customers begin to implement Motion Design into their core workflows, the Motion Design team will continue to survey customer feedback and focus on further performance optimization opportunities for the toolset.

Getting Motion Design to a Production Ready state required the following:

* Harden packaging support.
* Refactor Text3D to support rich text and masking capability.
* Transition Logic stability and increased ease of use and setup.
* Enhance Remote Control functionality by adding interface organizational tools and refactor general UX for accelerated setup time.
* Upgrade Scene State based on client feedback.
* Create communication between Scene State and Transition Logic.
* Ensure Material Designer reliability.

### Text3D — Rich Text

[![Text3D — Rich Text](https://dev.epicgames.com/community/api/documentation/image/c3223087-c392-40fe-bd42-d7d30aa0fbb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c3223087-c392-40fe-bd42-d7d30aa0fbb3?resizing_type=fit)

Give your text layouts a dynamic edge with both pre-configured or dynamically customizable text. Create a Text3D style set using our new dedicated asset where you can create a consistent configuration you can use across your project on any Text3D actor.

Previously, this sort of layout would require several Text3D actors and an Auto-Follow modifier. In Unreal 5.7, these can be edited in-line, reducing the actor count and even providing a way for you to remote-control the individual text sections.

* Supports assigning fonts, colors, sizing,
* Flexible styling tools adapt to any art direction.
* Ideal for designs with dynamic UI.
* Exposes each section of the text line to remote control for further customization.

  + This is useful when you want to break apart something like "Brand New Enriched Text" into three separate controllers while retaining the style of each word.

### Transition Logic Quality of Life

[![Transition Logic Quality of Life](https://dev.epicgames.com/community/api/documentation/image/7d432986-6c5d-47bb-a4fa-1d33ba89cce6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d432986-6c5d-47bb-a4fa-1d33ba89cce6?resizing_type=fit)

**Transition Logic** is critical to the broadcast workflow and, based on customer feedback, we reevaluated the steps required to create a level and set up Transition Logic. You can now accomplish all of the steps in the image above by creating a new level and making sure that the **Create Transition Logic Default Scene** option is enabled, as seen in the top left corner of the image.

Below are the setup steps that Transition Logic automates when you enable Create Transition Logic Default Scene:

* Create pre-labeled In and Out sequences.
* Create pre-labeled Layer Change sequences.

  + You can add additional (and pre assigned) Layer Change sequences with new entries in the Sequencer options panel.
* Pre-set the sequence settings on those sequences for immediate compatibility.
* Create a default layer so that you can get to work immediately and test your design.
* Add the Transition Logic Sublayer Modifier to a null actor in your Motion Design Outliner and pre-assign it to the generated In and Out sequences.

All that is required of you beyond that is to actually animate your content using the generated In, Out, and Change sequences.

### Remote Control UX

[![Remote Control UX](https://dev.epicgames.com/community/api/documentation/image/4aa2614b-f35e-4752-85c6-7c5c412d3394?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4aa2614b-f35e-4752-85c6-7c5c412d3394?resizing_type=fit)

We added or improved several features that save you time while rigging your designs.

**New Controllers**

* Category

  + Add categories to separate your controllers into groups.
  + Single select or multi-select your controllers and drag them into the categories.
* String List

  + Curate a named dropdown list that you can link to your conditional behaviors to enhance the end-user experience.
  + Previously, solving this would require entering integers where "1 = Blue, 2= Red, 3= Yellow," now you can name the dropdown entries Red, Blue, Yellow.
* Events

  + Create a button that can play Motion Design sequences, trigger an On Modify property, or trigger a broadcast event.

**Path Behavior**

* Previously, each Path Behavior entry could only address a single actor. There is now a list that appears under the Actions panel where you can add as many actors as you want to effect, reducing the need for multiple Path Behaviors and making it easier to troubleshoot your setup.
* Reordering the path list was previously not possible; now, you can use the left side drag handle to reorder as necessary.
* The Path Preview now informs you if the path that you're routing to is valid or not with a green checkmark.

**UI Enhancement**

* We added a link icon to the left-side properties panel to show whether an exposed property is assigned to a controller.

### Scene State

![](https://dev.epicgames.com/community/api/documentation/image/181a0970-ad86-41d6-a59e-fd9b6ec958e6?resizing_type=fit)

**Scene State** in UE 5.7 received several new features and UX improvements that greatly improve user control.

* State Machine Organization

  + Reorder State Machines by dragging and dropping.
  + Add categories.
* Added Setter Tasks as part of property references.

  + Datatypes include: Boolean, Float, Int, String, Text.

    - Each datatype has unique functionality.
* Property Functions

  + Concatenate String
  + Text to String
  + Name to String
  + Integer to String
  + Float to String
* Spawn Actors and Spawn Actors to Tickers.

### Data Link

**Data Link** received two much-requested updates:

* Push Functionality, providing a method for constant detection of changing values from feeds to trigger updates.
* Interaction with with Scene State to provide a method for scrolling tickers and other living elements.

## Production Rendering Pipeline

### Material Parameter Collection Modifier

[![Material Parameter Collection Modifier](https://dev.epicgames.com/community/api/documentation/image/ed6055ab-461f-48ba-ba4f-316ee9a104a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed6055ab-461f-48ba-ba4f-316ee9a104a0?resizing_type=fit)

**Material parameter collections** are powerful assets that can drive multiple properties on multiple materials at once. Creative looks and effects within a scene are often driven dynamically by material parameter collections.

The **Material Parameter Collection Modifier** provides a way for you to set and override parameter values on a per-render layer basis in **Movie Render Graph**. Using the same level and level sequence, you can render shots with different parameter values on each render layer. You can also make parameters into graph variables and expose them as overrides in both the **Quick Render** and the **Movie Render Queue** windows.

### Burn In Per-Output Type

[![Burn In Per-Output Type](https://dev.epicgames.com/community/api/documentation/image/088892bb-64ac-44df-83f8-6b81863d01a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/088892bb-64ac-44df-83f8-6b81863d01a8?resizing_type=fit)

The ability to render multiple output types in the same job means Movie Render Graph can provide both final and review media simultaneously. Typically, Burn In is desirable for some but not all of the output types in a job. To account for this, Movie Render Graph now sets **Burn In Per-Output Type** instead of by using a separate node in a branch. This makes it much simpler to, for example, have clean EXR renders but include Burn In on MP4s.

### File Naming Control

[![File Naming Control](https://dev.epicgames.com/community/api/documentation/image/5447ba21-8fe8-47c6-acec-8c2a49216299?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5447ba21-8fe8-47c6-acec-8c2a49216299?resizing_type=fit)

Strong naming conventions on render output are a foundational building block of efficient pipelines in all industries. With this in mind, Movie Render Graph offers much more robust **File Naming Control** to better support studios' specific naming requirements natively, without the need for additional pipeline scripting. Key improvements include:

* **Custom Naming Tokens** defined in the Cinematic Assembly tools are supported in all name fields.
* You can customize {renderer\_name} (for example, "Deferred") and {renderer\_sub\_name} (for example, "beauty"), and conflicts are resolved per-branch rather than for the entire graph, offering more flexibility.
* **Burn In** no longer forces {renderer\_name} on the beauty render when it is not composited.
* **Post Process Material** passes can use a separate naming convention from the beauty render if desired.

### EXR Metadata Per Render Layer

[![EXR Metadata Per Render Layer](https://dev.epicgames.com/community/api/documentation/image/befb0db0-740b-4615-b953-b16f27b80fa8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/befb0db0-740b-4615-b953-b16f27b80fa8?resizing_type=fit)

**EXR Metadata** now follows a convention that reliably separates key/value pairs on a per-render layer basis and avoids naming conflicts. Based on this convention, metadata from Unreal Engine renders can be queried directly in post-compositing applications such as Nuke without the need for additional pipeline tooling.

## Content Pipeline

### Customize USD Asset Import with Interchange (Experimental)

[![Customize USD Asset Import with Interchange (Experimental)](https://dev.epicgames.com/community/api/documentation/image/adeab5cc-c991-4d9c-a8ea-71329b503275?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/adeab5cc-c991-4d9c-a8ea-71329b503275?resizing_type=fit)

USD is a versatile scene description file format with a growing adoption across the 3D industry.

We added USD to the list of file formats supported by the Interchange framework in UE 5.5. Content Creators benefit from more control over the import process and are now able to add custom processing steps for asset import of USD files, similar to the Interchange capabilities already available with other formats such as FBX.

The support for USD through Interchange is considered Experimental and limited to import of assets. In UE 5.7 we added support for:

* Groom
* Dome Lights (not the DomeLight\_1 schema)
* Audio (UsdMediaSpatialAudio)
* Point Instance

### FBX Level Import with Interchange

[![FBX Level Import with Interchange](https://dev.epicgames.com/community/api/documentation/image/b1a46672-e749-4c82-92f3-d37700f88bd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1a46672-e749-4c82-92f3-d37700f88bd1?resizing_type=fit)

In an effort to align the UI/UX for importing different file formats into the engine, the FBX level import process is available through the Interchange Framework. This is now the default path to import an FBX into a level. You can still fall back to the legacy behavior with the help of a CVar.

The main change comes from the use of the same import dialog as for import in the content folder. Legacy functionalities such as removing assets or actors from import, or using a different set of options to import, can now be performed through custom Interchange pipelines.

## Editor and UI Systems

### AI Assistant (Experimental)

![AI Assistant (Experimental)](https://dev.epicgames.com/community/api/documentation/image/4ce4c1e5-8bab-4d2b-9802-bf4d69a9d4c5?resizing_type=fit)

The **AI Assistant** gives you a faster way to get answers without leaving Unreal Engine. By sliding out a dedicated panel in the Editor, you can ask questions, generate code, or follow step-by-step guidance, all without switching to a browser.

You save time and stay in flow. Instead of breaking concentration to search online, you can get instant help, examples, and troubleshooting tips right inside the editor.

**What you can do:**

* Offer step-by-step instructions for tasks.
* Get guidance and tips directly in context.
* Troubleshoot development topics with AI help.
* Generate code examples to accelerate workflows.
* Reference past exchanges with chat history.
* Copy and paste answers into your project.

The AI Assistant is powered by the same specially-trained AI already available in UEFN and on the Developer Community—tailored to understand Unreal Engine and help you move faster.

### Home Screen

[![Unreal Engine Home Screen](https://dev.epicgames.com/community/api/documentation/image/784b0f86-4a84-4eb2-afcf-4bc373e1e006?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/784b0f86-4a84-4eb2-afcf-4bc373e1e006?resizing_type=fit)

The **Home Screen** helps you get oriented in Unreal Engine by providing a welcoming starting point. It highlights essential resources such as tutorials, documentation, and forums.

You get an easier, more guided onboarding experience. Instead of facing an empty editor, you have clear navigation to learning resources, news, and support, all in one place—helping you start projects with confidence and direction.

**What you can do:**

* Access the latest news and updates.
* Navigate directly to Getting Started resources.
* Open tutorials and documentation.
* Visit the forums and release notes.
* Launch links externally in Chrome.
* Turn off the Home Screen if you prefer not to see it every time.

The Home Screen serves as a one-stop onboarding hub, making Unreal Engine more approachable from the very first launch.

### Orthographic Clipping Interactions

![Orthographic Clipping Interactions](https://dev.epicgames.com/community/api/documentation/image/2e5f454f-2fee-4882-ad48-d1635770e749?resizing_type=fit)

Orthographic viewports now provide more reliable and flexible control. In earlier versions, clipping planes were often unusable, making it difficult to adjust what was visible in the scene.

You gain precise control over what you see in orthographic views, making it easier to focus on exactly the geometry you need.

**What you can do:**

* Adjust near and far clipping planes with greater accuracy.
* Use new visual controls directly in the viewport.
* Customize visibility in orthographic views to match your workflow.

This improvement, fixed in UE 5.7, makes orthographic workflows more practical and predictable.

### Improved Save and Delete Dialog Boxes

[![Improved Save and Delete Dialog Boxes](https://dev.epicgames.com/community/api/documentation/image/fe818cc4-3a97-4455-819a-1c95218b7e23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe818cc4-3a97-4455-819a-1c95218b7e23?resizing_type=fit)

We improved the **Save** and **Delete** dialog boxes in Unreal Engine to make asset management smoother. Common actions now work as expected, reducing unnecessary clicks and interruptions to your workflow.

You spend less time wrestling with repetitive prompts and more time focusing on your project.

**What you can do:**

* Use the Enter key in the Asset Deletion popup (previously unavailable).
* Delete multiple assets without repeatedly clicking Accept with the mouse.
* Rely on more consistent and intuitive dialog box interactions.

These improvements arrive in UE 5.7 and streamline everyday workflows by fixing long-standing pain points.

### Improved Window Dragging Interactions

![Improved Window Dragging Interactions](https://dev.epicgames.com/community/api/documentation/image/610fc139-afb8-402f-ba35-d3641a897467?resizing_type=fit)

Dragging windows inside the editor is now more intuitive and less disruptive. In previous versions, clicking and dragging on any header bar would undock the entire Level Editor from fullscreen, often by accident.

You avoid frustrating misclicks and keep your workspace stable, so you can stay focused on building.

**What you can do:**

* Drag windows and panels without undocking the full Level Editor.
* Prevent accidental breaks in fullscreen workflows.
* Enjoy more predictable and user-friendly window interactions.

This improvement, fixed in UE 5.7, addresses a common frustration and makes window management more reliable.

### Improved Blueprint Editor Duplicate Interactions

![Improved Blueprint Editor Duplicate Interactions](https://dev.epicgames.com/community/api/documentation/image/940f5768-67c5-480f-b047-522f7f5c28a1?resizing_type=fit)

Duplicating items in the Blueprint Editor is now smoother and less disruptive. In previous versions, duplicating would clear your selection, forcing you to manually reselect items in the tree view.

You keep momentum while editing, avoiding extra clicks and rework when duplicating elements.

**What you can do:**

* Duplicate items in the Blueprint Editor without losing selection.
* Maintain active selections when working in the tree view.
* Reduce repetitive steps when duplicating multiple items.

This improvement, fixed in UE 5.7, makes Blueprint editing more efficient and frustration-free.

### Geometry Inspection Viewport Modes

![Geometry Inspection Viewport Modes](https://dev.epicgames.com/community/api/documentation/image/0f83f10e-23e4-4219-acb7-b82f24dac15d?resizing_type=fit)

The new **Model Inspection Viewport Modes** in Unreal Engine provide simplified, non-photorealistic visualization options. These modes prioritize geometric clarity over realism, removing lighting and shadows when inspecting mechanical or complex 3D models:

* **Clay**
* **Zebra**
* **Front/Back Face**
* **Random Color**

### User Asset Tags

[![User Asset Tags](https://dev.epicgames.com/community/api/documentation/image/e7bcdf07-b951-4e43-ba6d-c5ffd4dc747f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e7bcdf07-b951-4e43-ba6d-c5ffd4dc747f?resizing_type=fit)

The **User Asset Tags** system provides a way to add arbitrary tags to your assets. It supports local favorites as well as project-wide tags, and you can extend it to suggest additional tags. These tags serve as the foundation for additional systems such as the **Tagged Asset Browser** used in Niagara. Select assets you want to tag, and use Ctrl + T or select **Manage Tags** in the context menu.

### Tagged Asset Browser (Niagara)

[![Tagged Asset Browser (Niagara) 1](https://dev.epicgames.com/community/api/documentation/image/617aef02-fc21-4706-bb3b-b67a247bda5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/617aef02-fc21-4706-bb3b-b67a247bda5f?resizing_type=fit)

[![Tagged Asset Browser (Niagara) 2](https://dev.epicgames.com/community/api/documentation/image/0d51dcd7-060b-495f-862c-04b55e6e8ce1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d51dcd7-060b-495f-862c-04b55e6e8ce1?resizing_type=fit)

An update of the previous revamp of the **Niagara Asset Browser**. Now generalized, it lays the foundation for asset factories that want to adopt the same browser. You can extend it by creating a new **Tagged Asset Browser Configuration** asset, defining your own sections and listed tags. This way it becomes possible for your projects to have their own sections and tags, or swap out the main configuration asset entirely in the Project Settings under Niagara Editor.

For help upgrading existing Niagara systems and emitters to use the new Tagged Asset Browser Configuration asset, see [Upgrading Niagara Tags](https://dev.epicgames.com/documentation/en-us/unreal-engine/upgrading-niagara-tags-in-unreal-engine).

## Framework

### State Tree: Rewind Debugger

[![State Tree: Rewind Debugger](https://dev.epicgames.com/community/api/documentation/image/212f9a88-54f3-41c4-9574-fa901043abe8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/212f9a88-54f3-41c4-9574-fa901043abe8?resizing_type=fit)

We’re introducing a new **Rewind Debugger track** for State Tree that brings an enhanced, owner- and instance-oriented debugging experience directly into the Rewind Debugger. This integration provides deeper context around when and how behavior logic is executed, all while aligned with gameplay and animation timelines.

The new track includes a dedicated Details panel with a compact tree view, making it easier to visualize and navigate complex logic setups, including nested subtrees and linked assets. This improves usability when working with larger or modular State Trees.

While this integration marks a shift toward a more unified debugging workflow, the original State Tree debugger remains available as an option. You can continue using the legacy interface if you prefer it for some use cases.

### State Tree Runtime

[![State Tree Runtime](https://dev.epicgames.com/community/api/documentation/image/ff962086-24a6-49a2-a196-cbd3751766ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff962086-24a6-49a2-a196-cbd3751766ac?resizing_type=fit)

This update brings a range of runtime-level enhancements that improve the correctness and performance of State Tree-based logic.

* **Live Property Binding**: Nodes can now push value updates to bound outputs dynamically during execution using Output Properties, resolving issues with outdated or static data in tick workflows.
* **ExecutionRuntimeData**: Nodes can now declare optional, long-lived data that persists for the life of the State Tree instance, useful for holding execution state across transitions or ticks without relying on static globals.
* **Memory Optimization for Static Bindings**: Delegate dispatchers, listeners, and property references are now stored outside of instance data, reducing per-node memory overhead.

We implemented the following features but did not enable them by default to avoid disrupting existing data and default behaviors. However, you can opt in to use them if desired.

* **Re-Enter State Behavior**: Added support for re-entering the same state and restarting tasks, providing you with a way to implement restarting logic more easily.
* **Instance Data Refactor**: Conditions and transitions now use scoped instanced data, preventing data leakage between sessions and making possible both temporary and persistent usage patterns.

### Mass Debugger

[![Mass Debugger](https://dev.epicgames.com/community/api/documentation/image/c22d5186-0b55-44a8-95a7-129e963e084f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c22d5186-0b55-44a8-95a7-129e963e084f?resizing_type=fit)

We’ve introduced a powerful new **entity search system** integrated directly into the Mass debugger, giving developers a new UI for crafting and executing MassEntity queries. The interface mirrors Mass's C++ query API 1:1, allowing for precise filtering of entities using the same criteria and requirements as hard-coded queries.

You can now create, save, load, and share custom queries, and immediately view the results in the **Entities tab**. This improves how fast and efficiently developers inspect and validate Mass state at runtime.

Additionally, we substantially upgraded the **breakpoint system**, offering more control and visibility when debugging Mass processors and fragment writes.

### Autogen NavLink Multiple Jump Config

[![Autogen NavLink Multiple Jump Config](https://dev.epicgames.com/community/api/documentation/image/81a2caf5-4e5a-4303-a36f-4fe62b041b22?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81a2caf5-4e5a-4303-a36f-4fe62b041b22?resizing_type=fit)

We’ve expanded automatic navigation link generation to support **multiple jump configurations** per navmesh generation pass. Previously, you could only use a single jump configuration, which often required overly broad tolerances to handle diverse link types (for example. jump ups, downs, and across). This also meant that all generated links shared the same area class and link proxy class, limiting flexibility.

With this update, you can now define multiple distinct configurations, each processed in its own validation pass. This enables more targeted and meaningful control. As an example, generating jump-downs and jump-overs separately, each with different distance thresholds, area types, or proxy behavior. It makes possible more nuanced movement setups while reducing overgeneration or unintended overlaps.

To ensure backward compatibility, we migrated any existing single jump configuration as the first entry in the new multi-configuration setup.pState Tree Usability

[![State Tree Usability 1](https://dev.epicgames.com/community/api/documentation/image/d22a1b1e-52e6-4eed-a01b-900f52f7c151?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d22a1b1e-52e6-4eed-a01b-900f52f7c151?resizing_type=fit)

[![State Tree Usability 2](https://dev.epicgames.com/community/api/documentation/image/0567b2f8-7ffa-4bc5-9413-5c85460fcae8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0567b2f8-7ffa-4bc5-9413-5c85460fcae8?resizing_type=fit)

We're continuing to enhance the State Tree editor experience with several quality-of-life upgrades aimed at improving clarity and usability:

* You can now **copy and paste tasks, conditions, and transitions** between states, even across different State Tree assets. This makes it much easier to reuse logic and maintain consistent behavior across large behaviors.
* We've also added the ability to **copy and paste individual property bindings**. Bound and unbound properties are handled intelligently:

  + Bound properties replace their bindings if compatible.
  + Unbound properties carry over values if a value is pasted, or carry over the binding if a compatible binding is pasted.
  + Pasting a value onto a bound property is disabled.
  + Pasting an incompatible type, or if the source data is inaccessible, will trigger a validation error.
* You can **hide properties within nodes and instance data based on schema**, reducing visual noise and improving focus.

### Mass Runtime

[![Mass Runtime](https://dev.epicgames.com/community/api/documentation/image/3dc031b5-39a0-4a3c-8023-2bb3a269983b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3dc031b5-39a0-4a3c-8023-2bb3a269983b?resizing_type=fit)

This update includes a series of low-level optimizations and architectural refinements to the Mass framework, aimed at improving overall performance, memory efficiency, and system stability in real-time scenarios.

The most notable addition is **Processor Time-Slicing**, which means long-running processors can be split across multiple frames. This helps reduce performance spikes and enables better distribution of heavy workloads, particularly useful in large-scale or simulation-heavy environments.

### Iris (Beta)

With Iris moving out of Experimental and into Beta, we’ve focused on solidifying key APIs and improving usability, maintainability, and performance across the networking stack. This release includes several internal design changes and quality-of-life improvements for developers working directly with Iris replication systems.

* **Actor Factory Overrides**: Actors can now specify custom `NetActorFactory` implementations using `StartReplicationParams`, providing more flexibility in replication behavior at runtime. This enables advanced replication setups without relying on global overrides.
* **Cleaner API Boundaries**: We removed the Iris `UReplicationBridge` base class to reduce virtual call overhead and simplify code navigation. Most Iris systems already depend on `UObjectReplicationBridge` directly, so this change streamlines the inheritance model and avoids unnecessary indirection.
* **Improved Replication Lifecycle Naming**: We clarified the `BeginReplication` API:

  + The non-virtual function is now `StartActorReplication`, clearly indicating its purpose as the entry point to start replication.
  + We renamed the virtual callback to `OnBeginReplication`, separating lifecycle behavior from system calls.
* **Better Consistency Across Iris and Legacy Networking**: `OnBeginReplication` and `EndReplication` are now consistently called regardless of whether Iris is enabled, ensuring behavior parity and making the transition between networking systems more seamless.
* **Seamless Travel Support**: Iris now supports Unreal Engine’s seamless travel feature, ensuring that replicated actors and states are handled correctly across world transitions. This is a key requirement for shipping game features that rely on persistent player data or transitions between large streaming worlds.

## Media

### Media Viewer (Beta)

![Media Viewer (Beta)](https://dev.epicgames.com/community/api/documentation/image/9765fd5f-d4ab-4f8c-ac27-6a42159ffa5d?resizing_type=fit)

Often animators need to align their animations against existing reference footage. In 5.6 we added the capability to dock media (images, media textures, video files, live viewports) next to where animation work is done. Two AB banks in either horizontal or vertical configurations help compare two sets of assets. Zoom and pan controls can be used to further align content. In UE 5.7, the **Media Viewer** plugin is now in Beta as it includes the following workflow and usability improvements:

* Enhanced controls such as rotation and zoom controls using ALT + RMB.
* Ability to bookmark and quickly recall asset configurations with hot keys.
* The lock button now also mirrors the playback controls and timeline while in dual Player mode.

## Simulation and VFX

### Chaos Destruction

![Chaos Destruction](https://dev.epicgames.com/community/api/documentation/image/1bfac456-0d5a-42c2-8259-c6722ec80730?resizing_type=fit)

The **Chaos Destruction** system is a suite of tools designed to achieve cinematic-quality levels of destruction in real-time. In addition to its great-looking visuals, the system is optimized for performance, granting artists and designers more control over content creation and the fracturing process through an intuitive, non-linear workflow.

**UE 5.7 updates include:**

* **Reset State**: You can now reset the state of the geometry collection component using C++, Blueprint, or live in the editor while simulating.
* **Export to Skeletal Mesh**: You can now export geometry collection assets to a skeletal mesh asset.
* **Leaf Sub-trace**: After tracing against a geometry collection, you can now get the exact leaf cone from a line trace. When unbroken, the original line trace against the component returns the root bone. With this new function, you can now get the exact bone the trace is hitting. This makes possible things like setting decals on the right bones or even anchoring individual pieces at runtime.

### Chaos Dataflow Editor

The **Dataflow** graph makes possible the procedural generation of assets within a node-based environment. The implementation of the graph uses a pull-based evaluation, where the nodes of the graph generate a cached output state based on the evaluation of its inputs. Dataflow assets are used to assist in the procedural authoring and setup of simulation systems.

Chaos Cloth, Destruction, Flesh, and Hair use the unified Dataflow node-based toolset.

**UE 5.7 updates include:**

* New timeline and simulation controls.
* A new toolbar.
* A redesigned Paint Weight Map tool (to match the Skeletal Mesh Editor).
* A new Edit Skin Weight tool (to match the Skeletal Mesh Editor).
* A new Edit Skeleton Bones tool.
* Many quality of life Improvements.

### Chaos Visual Debugger

![Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/8ea085fd-d82e-45cf-947c-a80b39b6a91c?resizing_type=fit)

The **Chaos Visual Debugger (CVD)** is a versatile tool designed to record and play back the state of a physics simulation during gameplay. It supports recording of all active Rigid and RBAN solvers, including particle states and collision data. CVD is accessible as an editor tool in Unreal Engine and offers extensive customization options, such as choosing specific data channels to record, either through the UI or using console commands.

The tool also features live debugging capabilities, giving you real-time inspection of physics data during simulation. Additionally, CVD includes a variety of visualization options, such as particle state, collision data, and scene queries, to assist you in analyzing and troubleshooting physics simulations effectively.

**UE 5.7 updates include:**

* **Object Name Improvements** : In this release, we introduced a new feature called **particle metadata**.

  + This new metadata replaces the old long "Debug Name" string.
  + CVD now shows the name of the actor owning the physics body name, and breaks it down in different fields (Level, Component, and Bone index).
  + In addition, we introduced a **Find in Content Browser** button that leverages this new metadata and provides a way for you to find the Blueprint a specific body comes from in a single click.
* **Performance improvements**: In this release, we continued working on improving CVD's performance.

  + CVD files with a large amount of data (specifically over 2 GB of collision geometry data) now loads up to 30% faster.
  + Reduced a stall of +10 seconds that could happen while loading the first frame of complex scenes (+93.000 objects),to ~3 seconds.
* This release also includes bug fixes and QoL improvements.

### Chaos Cloth

As cloth simulation and complex clothing become more widely requested in-engine, our legacy skeletal mesh cloth editor and workflow cannot easily adjust to future upgrades necessary to support those needs. Fashion and most character work has almost exclusively pivoted to using DCCs which specialize in panel-based clothing construction. In order to grow with these external DCC's we continue to develop our cloth editor in order to ingest and edit panel setups while refining the cloth setup workflow.

Chaos Cloth for Unreal Engine 5.7 includes the continued development of a Beta Cloth Editor.

**UE 5.7 updates include:**

* **Skeletal mesh clothing data integration:**

  + You can now add cloth assets and outfit assets as skeletal mesh clothing data.
  + The skeletal mesh render sections can then be deformed by the cloth simulation setup inside these assets dataflow graph, removing the need for an additional cloth component.
* **New reference space options:**

  + Use the new ReferenceBone dataflow node to explicitly set the ReferenceBone rather than use the auto-computed one.
  + Use the new Local Damping space option to solve in ReferenceBone space instead of using center of mass.
* **Optimizations**: We implemented optimizations to the cloth game thread and interactor tick.
* **Accessory meshes (Experimental):**

  + We added additional accessory meshes and updated the backstop constraint to be able to use this accessory mesh.
  + Currently, you can create accessory meshes by converting an existing sim mesh collection into an accessory mesh. If Imported Vertex IDs exist on both the source and target collections, you can use these to match up vertex indices that were reordered as part of a SKM import.

### Chaos Core

[![Chaos Core](https://dev.epicgames.com/community/api/documentation/image/04f0626c-e927-4cf5-9e9c-12f98b7ea326?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04f0626c-e927-4cf5-9e9c-12f98b7ea326?resizing_type=fit)

**Chaos Physics** is continually undergoing updates and optimizations in order to give artists, developers, and programmers better simulation results. Rigid Body dynamics is the core technology that most game physics rely upon. As we make progress towards bigger and bigger physics-enabled and physics-based worlds, we need to make sure this core system scales and can handle those use cases. Like rigid body dynamics, queries are a core technology that is relied upon by a wide range of systems inside Unreal Engine, and like rigid body dynamics, we need to make sure that query performance scales to very large dynamic worlds.

**UE 5.7 updates include:**

* **Simulation performance improvements:**

  + More parallel simulation stages.
  + We added the Experimental Partial Sleeping feature for improved performance of large unstructured piles.
* **Query performance improvements:**

  + Improvements to sphere and capsule narrow-phase.
  + Improvements to the general query layer transform and scale handling.
* **Chaos Visual Debugger (CVD):**

  + Improved loading speed for scenes with large actor counts and complex geometry.
  + QoL changes and runtime-debugger consistency improvements.
* **Dataflow physics assets:**

  + Initial support for the creation of physics assets using dataflow graphs.
* Many QoL changes and fixes across the simulation featureset.

### Chaos Caching

![Chaos Caching](https://dev.epicgames.com/community/api/documentation/image/103174f9-ca16-4c44-923e-3daae4d6f323?resizing_type=fit)

In Unreal Engine, **Chaos Cache** is a system within the Chaos Destruction framework that records and reuses complex destruction simulations, significantly improving performance and enabling consistent, predictable results for features like short films. You manage caching using a **Chaos Cache Manager**, which records physics data into a **Chaos Cache Collection** asset.

This cached data can then be played back at runtime to display the destruction without recalculating the entire simulation, making complex scenes more efficient and less demanding on hardware.

**UE 5.7 updates include:**

* **Geometry Collection Root Proxy Mesh Support:** Chaos cache now properly supports root proxy meshes and will switch to use them depending on the state of destruction of the geometry collection asset being cached and replayed.
* **Automatic Increment of Cache Assets:** Chaos cache manager now has an option to automatically create a new asset each time it starts a new recording session.
* **Session Start/Stop Controls:** You can now control when the caching session starts and stops. By default, the cache session starts when the Begin Play event is triggered for the cache actor (usually when starting PIE or Simulation). An option to disable this behaviour is available, requiring you to trigger the start of the session using the start and stop Blueprint functions.
* **Observed Component Functions:** Blueprint functions are now available to add, update, remove, or clear observed components of a specific ChaosActorManager.
* **Major Bug Fixes:**

  + When recording a cached Geometry Collection twice during the same session, events now always record properly the second time.
  + When replaying a cache in Play Mode, the Niagara Data Interface for Chaos Destruction now always triggers trailing events during the replay as intended.

### Chaos Hair

The **Hair and Groom** initiative focuses on building a robust simulation pipeline for realistic hair behavior using Dataflow, skeletal meshes, and guide splines. The system allows for animation-driven simulations, blending between kinematic and simulated strands, and advanced authoring features like guide deformers and painting tools.

Groom Asset procedural workflows benefit from the UE 5.7 update to the general Dataflow Editor improvement. We improved the corresponding nodes to provide for a more flexible setup:

* **Selection-aware nodes:**

  + Most nodes do take a selection, which results in a more controlled and targeted setup.
  + You can use existing selection nodes for other assets (Destruction, Flesh) to create selection sets and manipulate them procedurally.
* **Performance:**

  + Groom assets with complex geometry generate the geometry for the construction viewport faster, and now cache the information to avoid recomputing it.
  + This applies to other collection-based nodes across Dataflow Editors.

**UE 5.7 updates include:**

* Simulate hair with guide splines driven by animation and physics.
* Blend between animated and simulated states for realism and control.
* Support for painting attributes, skin weighting, and guide swapping.

### Chaos Fluids

![Chaos Fluids](https://dev.epicgames.com/community/api/documentation/image/eb9bee35-2ff6-4831-9735-2f16dfabb925?resizing_type=fit)

The **Fluids** project continues to expand Unreal Engine’s water simulation capabilities, with targeted efforts in UE 5.7 aimed at the Advanced Water plugin, mainly improvements for baked river simulations.

**UE 5.7 updates include:**

* Now supports virtual textures.
* Improved surface quality (less spikes artifacts).
* Various bug fixes and performance improvements.

## Virtual Production

### Live Link — Data Preview

![Live Link Data Preview](https://dev.epicgames.com/community/api/documentation/image/61e274a4-cbd1-4335-b173-d7fbe808c854?resizing_type=fit)

You can now preview Live Link data in the editor viewport without needing to prepare any actors or skeletal meshes. The **Live Link Data Preview** actor visualizes all your Animation, Transform, Camera, and Marker role data in one convenient actor.

We also provided actor components for custom editor utility tooling. **Mocap Manager** uses these to visualize your Live Link data.

### Live Link Hub — Robust Recording

[![Live Link Hub Robust Recording](https://dev.epicgames.com/community/api/documentation/image/6096ec0e-933c-4942-9afb-8d52f197911c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6096ec0e-933c-4942-9afb-8d52f197911c?resizing_type=fit)

We improved recording robustness in Live Link Hub to cope with subject data changing size over time — for example when losing a subject's tracking then recovering it during a recording.

You can upgrade recordings from previous versions to the new format using a right-click menu option in the recording list.

### Live Link — Broadcast Component

![Live Link Broadcast Component](https://dev.epicgames.com/community/api/documentation/image/64897646-c86a-4d8b-8784-ff8783b9daef?resizing_type=fit)

You can add the new **Live Link Broadcast** **component** to actors in your level and turn them into Live Link subjects for other machines on the local network to receive animation from. The Broadcast component supports the Transform, Camera, and Animation roles.

This new component enables workflows where you can use a lightweight Unreal Engine project for skeletal retargeting, then you can broadcast the resulting retarget pose to other Unreal Editor projects on the network, making UE the retarget DCC software. The framerate of the broadcast animation is equal to the game thread framerate.

### Live Link — Pauseable Data Stream

![Live Link Pauseable Data Stream](https://dev.epicgames.com/community/api/documentation/image/8cebc6c8-cb01-4383-a0d1-860286a36735?resizing_type=fit)

You can now pause and unpause data from Live Link subjects in the Live Link panel and in Live Link Hub. You can pause subjects individually or in groups.

There are also Blueprint scripting functions to control pausing from your custom editor tooling. Mocap Manager now uses this API to control pausing of subjects.

### Live Link Hub — Unreal Editor Device

[![Live Link Hub Unreal Editor Device](https://dev.epicgames.com/community/api/documentation/image/c819bc70-598a-4992-8611-86641306bcb7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c819bc70-598a-4992-8611-86641306bcb7?resizing_type=fit)

In future releases, the recording device functionality of Switchboard will be migrated to Live Link Hub for multi-user motion capture setups. For UE 5.7, in Live Link Hub you can now control the slate and record stop-start of Take Recorder on connected Unreal Editor clients, using a new plugin called **Live Link Unreal Device**, which is experimental.

This new approach improves robustness of multi-client Take Recording, replacing the legacy OSC message system used by Switchboard, and provides user-controlled authority over what each client should record and which clients should be allowed to record.

### Mocap Manager — Dynamic Prop Attachment

![Mocap Manager Dynamic Prop Attachment](https://dev.epicgames.com/community/api/documentation/image/3a6fdb59-c9d3-40ab-a785-37b7870241a1?resizing_type=fit)

When retargeting mocap there are often offsets between a performer's hands and the hands of your mocap character. This presents a problem when attempting to align tracked props with your character.

The new **Dynamic prop attachment** component provides a way for you to drive a prop with motion capture data but add a dynamic offset to keep it in your character's hands.

The **PCapProp** component now has a Blueprint-overridable function to let users write their own dynamic attachment logic. An example implementation is provided in Mocap Manager that should work for a majority of single handed props.

### Mocap Manager — Improved Performer Mesh Creation

[![Mocap Manager Improved Performer Mesh Creation](https://dev.epicgames.com/community/api/documentation/image/e4038d1c-81f1-4ca3-ad49-c23574750c98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4038d1c-81f1-4ca3-ad49-c23574750c98?resizing_type=fit)

For the most accurate retarget result a skeletal mesh scaled to the proportions of the performer's Live Link data is considered best-practice.

We improved the workflow in Mocap Manager for creating this asset to work with stages where the stage origin may not be conveniently placed and for systems that use right-handed coordinate systems.

### Composure

![Composure](https://dev.epicgames.com/community/api/documentation/image/13655506-c53e-4975-a882-ef5767f8eb0d?resizing_type=fit)

Unreal Engine 5.7 reintroduces **Composure** as a modern system for real-time compositing with both live video input as well as file/image media plates. The new Composure is a layer-based tool with numerous improvements over the legacy system, including:

* A redesigned **User Experience** and streamlined workflow.
* Performant **Shadow** and **Reflection** integration for live-action footage using **Custom Render Passes**.
* An improved **Keyer**.

### Media Profile

[![Media Profile](https://dev.epicgames.com/community/api/documentation/image/0b4ee201-36ab-4e7d-915a-f1d968a7177a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b4ee201-36ab-4e7d-915a-f1d968a7177a?resizing_type=fit)

Historically, the management of live video input and output in Unreal Engine required multiple assets (Media Source, Media Player, Media Texture, and so on) to get from point A to point B. The **Media Profile** seeks to consolidate these into a single configuration asset for a given machine setup and provide numerous workflow enhancements, such as:

* Dynamically add multiple Media Sources and Media Outputs and select the desired hardware option (for example, AJA, Blackmagic, NDI).
* Simultaneously preview multiple IO feeds.
* Capture Media Output.
* Configure Timecode and Genlock with immediate feedback.
* Conveniently access video IO functionality in related tools such as Composure with a single click.

### Take Recorder — Hitch Protection (Experimental)

[![Take Recorder Hitch Protection (Experimental)](https://dev.epicgames.com/community/api/documentation/image/88ee631c-ee71-4a4f-beb0-90bd77005c69?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88ee631c-ee71-4a4f-beb0-90bd77005c69?resizing_type=fit)

The UE 5.7 update adds support for **hitch protection** during take recording. You can now configure Take Recorder to dilate the recording speed to protect against data loss. If a frame would otherwise be dropped, Take Recorder can adjust the engine evaluation to allow time for the data to be recorded before catching up.

* More reliably record complete data.
* Visualize areas of concern where data integrity might be lost.
* Make informed decisions in the moment about the quality of your recordings.

### Naming Tokens — Editable Text Widget

![Naming Tokens Editable Text Widget](https://dev.epicgames.com/community/api/documentation/image/c61648cc-ace8-4f78-afd9-b3b631fbdd90?resizing_type=fit)

We added a new slate and UMG **Naming Tokens Editable Text** widget with direct support for naming tokens. You can now easily build pipeline tools with naming tokens support. When focused, the text box will display the unevaluated {token} string. When committed, the text box will show the evaluated result text.

* Search and autocomplete {tokens} directly from the text box
* Immediately see the evaluated token value directly in the text box

Available with the **Naming Tokens** plugin.

### Timeline Templates for Cinematic Assembly Schemas

[![Timeline Templates for Cinematic Assembly Schemas](https://dev.epicgames.com/community/api/documentation/image/3cb81a9f-533d-413b-af65-918e2db9fbc2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3cb81a9f-533d-413b-af65-918e2db9fbc2?resizing_type=fit)

**Cinematic assembly schemas** can now reference existing level sequences and cinematic assemblies as templates for the sequencer timeline. You can specify a target template and have that timeline recreated every time you create a new cinematic assembly using the schema.

* Design your base timeline in advance.
* Reduce repetition and error when creating shots, scenes, lighting sequences, and more!

Available when using the **Cinematic Assembly Tools (CAT)** plugin.

### Duplicate Assemblies with Reference Replacement

![Duplicate Assemblies with Reference Replacement](https://dev.epicgames.com/community/api/documentation/image/e7058df9-1cad-43f8-8243-f42e3d09b6a2?resizing_type=fit)

You can now duplicate assemblies to a new location with reference replacement. You no longer need to manually create, rename, and re-reference subsequences when duplicating an assembly.

* Duplicate to a new location and rename automatically based on assembly metadata and tokens.
* Subsequences are procedurally duplicated, renamed, and re-referenced to ensure no references are left behind, changing all of your old shots.
* Accessible easily from a clean and simple wizard.

### SMPTE 2110 — Nvidia Rivermax BlueField-3 Support

[![SMPTE 2110 Nvidia Rivermax BlueField-3 Support](https://dev.epicgames.com/community/api/documentation/image/7274259f-f01b-4948-95db-dd7b8ccb9124?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7274259f-f01b-4948-95db-dd7b8ccb9124?resizing_type=fit)

The Nvidia Rivermax plugin in Unreal Engine 5.7 supports both BlueField-2 and BlueField-3 DPUs with validated functionality in nDisplay for In-Camera VFX.

## Platform SDK Upgrades

[![Unreal Engine supported platforms](https://dev.epicgames.com/community/api/documentation/image/26e25af6-a2b5-41b1-b3ca-6b9f2bbaffd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/26e25af6-a2b5-41b1-b3ca-6b9f2bbaffd3?resizing_type=fit)

* Windows

  + Visual Studio 2022 v17.14 or newer
  + Windows SDK 10.0.22621.0 or newer
  + LLVM Clang

    - Minimum: 18.1.8
    - Preferred: 20.1.8
  + Intel OneAPI

    - Minimum: 2025.2.0
    - Preferred: 2025.2.0
  + .NET 8.0
* IDE Version the Build farm compiles against

  + Visual Studio 2022 17.14 14.44.35207 toolchain and Windows 10 SDK (10.0.22621.0)
  + Xcode 15.4
* GDK

  + Minimum Windows SDK: 10.0.22000.0
  + GDK: April 2025
  + Latest recovery version
  + Supported IDE: Visual Studio 2022
* Linux

  + Native Linux Development
  + Recommended OS: Ubuntu 22.04, Rocky Linux 8 or newer, Redhat Linux 8 or newer
  + Compiler: clang 20.1.8
  + Cross-Compile Toolchain: v26 clang-20.1.8-based
  + Note: Unreal Engine on Linux users must update their OS to use SDL3. For more information, see [Updating Unreal Engine on Linux to SDL3](https://dev.epicgames.com/documentation/en-us/unreal-engine/updating-unreal-engine-on-linux-to-sdl3)
* macOS

  + Recommended OS: Latest macOS Sonoma 14
  + Minimum OS: macOS Sonoma 14.0
  + Recommended Xcode: 15.4 or newer
  + Minimum Xcode: 15.2
  + Supported macOS SDK: 14 and newer
  + Note: Supported Xcode versions were downgraded from UE 5.6  due to some issues with compiling and linking when using the latest versions.
* iOS / tvOS / iPadOS / visionOS

  + Recommended OS: Latest macOS 14 Sonoma
  + Minimum OS: macOS Sonoma 14.5
  + Recommended Xcode: 16.1 or newer
  + Minimum Xcode: 15.4
  + Supported Target SDK versions:
  + iOS SDK version: 15 or later
  + iPadOS SDK version: 15 or later
  + tvOS SDK version: 15 or later
  + visionOS 2.4 with Xcode 16.3 recommended

    - Note: v2.5 and x16.4 passed a very limited test and are likely good. Versions down to v2 and x16 are likely to work.
  + iOS Graphics API: Metal 2.4 - 3.1
  + Other Notes

    - Shader Model 6 (SM6) requires macOS 15. This support is in Beta, and we do not recommend it for production at this time.
* Android

  + Android Studio Koala 2024.1.2 August 29, 2024
  + Android NDK r27c
  + Android SDK

    - Recommended: SDK 34
    - Minimum for compiling UE: SDK 34
    - Default target SDK for shipping: SDK 34
    - Minimum install SDK level: SDK 26
    - AGDE v23.2.91+ is recommended if you are using AGDE debugging, as this version contains a fix for a SIGBUS error.
  + Build-tools: 34.0.0

    - If you try to use 35.0.0, you may have issues if using aidl on Windows. This is fixed with 35.0.1.
  + Java runtime:

    - OpenJDK 21.0.3 2024-04-16
    - OpenJDK Runtime Environment (build 21.0.3+-12282718-b509.11)
    - OpenJDK 64-Bit Server VM (build 21.0.3+-12282718-b509.11, mixed mode)
  + Other Notes

    - UE has been updated to use Gradle 8.7, and the Android Gradle Plugin (AGP) version we use has been updated to version 8.5.2. If you are using Android Studio for debugging, we recommend using Android Studio Koala. Ladybug also works, but does not update Gradle or AGP from the above versions.
    - When you choose your NDK level, you should target android-26, which supports Android 8.0+.
* EOS

  + 1.18.1.2-47370208
* Steam

  + 1.57
* Switch

  + Default SDK Version: 20.5.6
  + Default Firmware Version: 20.1.0-2.2
  + Minimum SDK Version: 18.3.1
  + Minimum Firmware Version: 18.1.0-1.0
  + Nintendo Package Manager: 1.7.0
  + Supported IDE: Visual Studio 2022
* Switch 2

  + Default SDK Version: 20.5.6
  + Default Firmware Version: 20.1.0-2.2
  + Minimum SDK Version: 19.3.5
  + Minimum Firmware Version: 19.1.0-1.4
  + Nintendo Package Manager: 1.7.0
  + Supported IDE: Visual Studio 2022
* PS4

  + Default Orbis SDK 12.508.001
  + Minimum Orbis SDK 12.008.011
  + System software 12.508.001
  + Supported IDE: Visual Studio 2022
* PS5

  + Default Prospero SDK 11.00.00.40
  + Minimum Prospero SDK 10.00.00.48
  + System Software 11.00.00.43
  + Supported IDE: Visual Studio 2022
* ARCore

  + 1.48
* ARKit

  + 4.0
* OpenXR

  + 1.1.46
  + OpenXR 1.0 and 1.1 runtimes are supported, either can be disabled in project settings.

## Release Notes

### AI/ML

#### Neural Network Engine (NNE)

**New:**

* Added multi-task support to the IREE CPU backed NNE runtime.
* Upgraded IREE to version 3.5.0. for NNE plugin NNERuntimeIREE.

### Animation

#### Animating in Engine

**New:**

* Added a 'Tolerance' To the ControlRigPoseMirrorSettings Project settings that is used to match Controls also by position in rest pose. We still match by the Mirror table first, and fallback to position based matching. We also now cache the tables and reset them if a mirror table property is changed.
* Improved Anim Details

  + UX Editing multiple values no longer displays the first property value.
  + Releasing focus on multiple values no longer sets the first property value.
  + Shift clicking to the left of a property name no longer resets the property.
  + Added support for math expressions with multiple operators.
  + Removed support for =operator syntax, instead use operator =, e.g \*=3 to multiply the current value by 3.
  + No longer show parent controls of the current selection, avoiding showing too many channels when a selected control has hosted channels.
  + Now follows the same order as Sequencer for non Control Rig properties
  + Now uses meta data of Control Rig elements and Object Properties that sequencer controls, value ranges are now displayed and respected.
  + Selected Anim Details properties now navigate to their value widget when pressing tab.
* Animator Kit:

  + Added a new Locator utility rig.
  + Adding static mesh locators and materials.
* Curve Editor:

  + The Set Start Playback Range and Set End Playback Range shortcuts now work in the Curve Editor as well as Sequencer.
  + A new preference, Panning Mouse Button, allows you to choose whether right or alt-middle mouse button, or both should be used for panning the curve editor view. Also, alt-right now always zooms in/out.
  + The Next Key and Previous Key shortcuts now work in the Curve Editor as well as Sequencer.
* Ensured we load an animation instead of trying to just find the package before we "Bake To Animation" so that it doesn't try to create a new asset.

  + Updated AnimationEditorUtils.cpp

**Bug Fix:**

* Deleting a Bool channel can no longer set the key at another time if AutoKey and KeyAll is on.
* No longer adds anim layers to level sequence unless needed.
* Constraints now work with Pivot Tool.
* Fixed shift click so it always goes to the last selected object, added a hot key to toggle pivot and motion trail modes.
* Made sure to automate tangents when baking.
* Made motion trails enter/exiting undo/redoable.
* Motion trails can be selected without a focused viewport.
* Made sure Rotator/Location/Scale controls have a curve color
* Pose library can paste onto hidden control rigs
* Made the AnimSequencerExport Blueprint type
* Anim Details:

  + Properties now reset their values to the initial value of controls when clicking reset to default.
  + Now also displays properties that reside within a Shot Track.
  + Fixed navigation not working in some cases.
  + Fixed an issue in Anim Details where selecting a component in a plain location, rotation or scale control would not select the control in Curve Editor.
  + No longer shows objects if keys are selected only.
  + Fixed property value widgets are losing focus while scrubbing if a blueprint actor is controlled.
  + Fixed in some cases editing Anim Details properties creates more than one undo step.
  + Fixed Anim Details options no longer showing when reentering animation mode
  + Fixed an issue where Anim Details displayed the actor or component name instead of the track name for attributes.
* Curve Editor:

  + Fixed issues where bezier curves were not always painted correctly.
  + Fixed an issue where curves were not painted when none of its keys were visible.
  + Fixed an issue where linear pre-/post-infinity extrapolation was not always painted correctly
  + Baking keys with a value different than 1 would increase range
  + Fixed an issue where pre-/post-infinity was not painted correctly when the first or last key's tangent mode was linear and pre-/post-infinity interpolation was linear
  + Fix an issue where curves flicker hovered and unhovered while editing
* Motion Trails:

  + Made sure the Motion trail state stays on with asset reload.
  + Fixed strobing frame coloring with dashed by setting the start frame to be eval range start so it doesn't change when view range changes.
  + Fixed crash when drawing HUD since trail may not be updated due to how the hud draws. Clean pin state in UI when using modifiers.
* Fixed an issue where changing additive animation modes with root motion on causes inconsistent root position when going from an additive mode to none.
* Fixed a bug where starting an animation with a non-zero playback time (like rewind debugger can do) would cause an incorrect root position.
* When merging sections no longer see if it's in range, just extend it so we can match up how it works without the merge.
* Now only compensate from the game thread.
* Can now set or add keys when recording control rig keys, previously we would just add keys causing duplicates.
* Anim Layers:

  + Bake Fix for absolute with additives when doing per frame bakes.
  + Make Name Column not shrink when shrinking
  + Layers show up when added to sub sequence
  + Keep track of open anim layer UI on the anim layer asset data.
  + Fixed duplicate/merging control rig sections when the channel layout is different between sections.
* Made generic vector channel data display more robust for position/rotation/scale control types. This also fixes the euler curve filter not recognizing rotation keys coming from Rotator control types.
* Sequencer: When baking to control rig, the animation track is now disabled instead of the individual sections.
* Turn off throttle when mouse button is pressed not just on drag so scrub time doesn't throttle in sequencer/curve editor
* Space Switching: Remove extra keys when clicking a space key by checking to see if we are changing into the same space in which case we can delete the extra key and the space key
* Hosted channels are no longer enabled if the parent is not enabled, this breaks selection. Also fixed anim layer selection with static meshes
* Sequencer: The scrub shortcut (b) now properly works in the viewport, Sequencer and Curve Editor.
* Fix Pivot square scale in different FOV's.
* Force LOD to 1 when ticking skel meshes when baking anim sequences. Sequencer may restore state which can change the lod during the bake process.
* Pivot Tool: Pivot render works in different FOVs
* Animation Kit:

  + Added aim option for blendParent. Changed control shapes to not be solid.
  + Fixing bad root attachment when no control rig exists.
  + Fixed an issue with the recompute mesh normals kernel used by Deformer Rigs in the Animator Kit plugin causing unexpected changes to mesh normals even if they are not influenced by deformer.
* Can no longer do space compensation from nongame thread which can happen when deleting many channels, in which case we probably don't want to compensate anyway
* Pose Library fixes, use alt drag for non additive drags and for additive it goes from -1 to 2.

  + Blending and additive mode are now working on mirror.
* Space Switching: Fix for undoing space switch key deletion.
* Tools such as snapper, trails and baking now work better with spawnables in nested subsequences

#### Character Customization (Mutable)

**New:**

* Added component naming support for spawned groom components.
* Debugger improvements:

  + Added support for Dataless parameters.
  + Unified Debugger and Editor compilation options.
  + Reordered some widgets for better use of the available space.
* Minor API improvements:

  + Actor:

    - Added ACustomizableSkeletalMeshActor::GetCustomizableObjectInstance.
    - Added ACustomizableSkeletalMeshActor::GetSkeletalMeshComponent.
  + Override Materials

    - Deprecated UCustomizableObjectInstance::GetOverrideMaterials(int32).
    - Added UCustomizableObjectInstance::GetSkeletalMeshComponentOverrideMaterials(FName).
* Restricted Passthrough Mesh Component to only support Skeletal Meshes.

**Bug Fix:**

* Fixed Material Parameter assert.
* Fixed Default Values not exposed to Blueprint.
* Fixed Skeletal Mesh Parameter morph check.
* Fixed UpdateSkeletalMeshAsync missing parameters.
* Fixed Materials comparison for merging.
* Fixed Textures and Meshes not being properly cached, their hash was not deterministic.
* Fixed a compiled API typo.
* Fixed multiple Dataless bugs:

  + Crash with Default Material parameter.
  + Crash with Dataless Morphs having names but no data.
  + Fix Texture Parameter not cropping images with layout operations.
* Fixed issues with GenerateMutableSourceImage cache.
* Added missing COI Contains API functions.
* Fixed public API Enum Parameter functions not working with the first parameter.

  + GetEnumParameterNumValues
  + GetEnumParameterValue
* Fixed deadlock when saving an asset + compiling a CO while asset registry was loading.
* Fixed streaming crash when no indices.
* Fixed meshes incorrectly reusing poses.

**Deprecated:**

* Removed deprecated 5.6 API functions.

#### Control Rig

**New:**

* Update default hotkeys and related functionality:

  + Set Solve Mode: Construction Event - 1
  + Set Solve Mode: Forwards Solve - 2
  + Set Solve Mode: Backwards Solve - 3
  + Set Solve Mode: Backwards and Forwards - 4
  + Set Next Solve Mode - M
  + Enable profiling- P
  + Show Controls as Overlay - U
  + Display Nulls - G
  + Display Socket - H
  + Display Axes for selection - J
  + Using hotkey for Profiling (P by default) now creates an undo step.
* Function nodes from other assets now show the asset name instead of the asset path.
* Flagged Render MorphTarget MaxBlendWeight CVar as safe for render thread, in order to avoid some warning logs.
* Made the animation show flags of the control rig editor never clip off of the viewport toolbar.
* Fixed duplicated Control Rig assets not resetting the asset variant ID.
* Control Rig Hierarchy no longer reserves transform space for non transform elements (curves and connectors).
* Control Rig Physics

  + Moved to its own experimental plugin, though it still requires the Physics Control plugin as well.
  + Added ability to import collision shapes and bones
  + Support for "wind turbulence"
  + Support for colliding against world objects
  + Add various cvars under controlrig.physics
  + Numerous improvements, especially access to functionality, and fixes
* Removed top level component concept from Control Rig Hierarchy
* Added GetSocketTransform
* Modular Control Rig:

  + Adding plugin Icon for Modules
  + Improved backwards solve for Foot Module.
  + Added Module tags and Root56 module to the correct ini files.
* Dragging a rig element onto the graph now offers an option to Get Metadata and Set Metadata.
* Update default settings and remember them per editor per user:

  + Display Axes On Selection is now enabled by default.
  + Display Axes On Selection, Axis Scale, Display Nulls, Display Sockets, Gizmo Scale, Hide Control Shapes, Show Controls as Overlays, Only Select Rig Controls are now saved per editor per user.
* Control Rig now only performs one copy of the hierarchy during initialization.
* Added line trace unit nodes.
* Added icon to plugin.
* Added Damp and Critical Spring Damp nodes to Control Rig.
* The Control Rig menu now shows directly in the viewport toolbar instead of being a submenu in the Show menu (eyeball icon).
* Nodes and hierarchy elements now offers options to find nodes by name locally and globally.
* Updates to Set Initial Transform from Current and related Commands

  + Set Initial Transform from Current is now only applicable for Bones, Nulls and Connectors.
  + For Controls, Set Initial Transform from Current is now Zero Controls.
  + For Controls, Set Initial Transform from Closest Bone is now Zero Controls from Closest Bone, and no longer applicable for Bones, Nulls and Connectors.
  + Set Shape Transform from Current is now Zero Control Shape.

**Bug Fix:**

* Moved findItemsWithTag to the construction event for performance.
* Fixed Control Rig curve container undo / redo breaking the curve list
* Fixed Control Rig editor resetting on compile curve operations made on the curve container (delete, rename, and import).
* Fixed a crash in Control Rig Pose adapter when removing bones from the skeleton while having a Blueprint with a Control rig opened in the asset editor.
* Fixed AnimNode Control Rig variable mappings initialization at OnInitializeAnimInstance.
* Control Rig: Need to update Rotation Order table with modular rig updated names.
* Fixed Control Rig Hierarchy updating more transforms than needed in propagate dirty flags function.
* Modular Control Rig

  + Added twist to legs.
  + Fixed IK/FK naming.
  + Added back public function from arm to leg so it picks up changes.
  + Fixed hind legs ik fk.
  + Changed leg and arm softness to off by default.
  + Fixed socket tooltip in Spine.
  + Fixed HindLeg FK controls not rotating.
  + Fixed AnimalNeck stretch.
  + Fixed Shoulder backwards solve by parenting to chest null instead of body ctrl.
  + Fixed HindLeg to always use connectors for creation instead of parent lookup.
* The editor now retains the Rig Solve Mode after compiling.
* Fixed Control Rig control module iterator lambda parameters creating copies of some expensive objects.
* Fix for client crash in FRigUnit\_HierarchyInstantiateFromPhysicsAsset, due to Modular Control Rig object overrides getting garbage collected.
* Fixed ControlRig Hierarchy serialization not storing the previous hierarchy name map.
* Fixed crash in Control Rig editor when the preview floor mesh is not available, now it will trigger an error log and continue to load the asset.
* Avoid a crash in Control Rig when adding an empty rule to a connector.
* Fixed an editor undo redo in an AnimBPs that contains a Control Rigcrash, when performing a redo of a previously-undone SetPreviewMesh transaction.
* Anim In Engine: Rotator control keys are retained in Sequencer when the controls are changed to transform controls in the rig.
* Need to update Constraint Channels with updated Modular rig names, or constraints come in broken.
* Fixed ControlRig editor not executing post undo for the transient editor preview actor.
* Fixed undo / redo crash in Control Rig hierarchy mappings, when undoing across a construction transaction.
* Converted HandleExecutionReachedExit event to function callback, to avoid worker thread contention.
* Fixed ControlRig spawn control node details panel not generating the shape name list as a combo box.
* Fixed a crash in ControlRig when expanding a function reference from a different graph that contains a private function inside. Now the user will receive a localize request to make a local copy of the function.
* Fixed RigVM local variable customization not showing value for local variables not used in the graph and losing value after compiling.

#### Deformer Graph

**New:**

* Adding Deformer dynamically in Control Rig was changed to use Async Loading to avoid hitches when the Deformer loads.
* Enabled Compute Framework/Deformer Graph on mobile platforms.
* Fixed SkinWeightAsVertexMask Date Interface providing incorrect data when a non-default skin weight profile is used.
* Fixed skeletal meshes getting invalid tangents when using deformer graph with opengl\_es31.
* Fixed wrong category for a few deformer functions.
* Added a pre-built dual quat deformer that supports both morph and cloth.

**Bug Fix:**

* Made sure skin weight profiles are requested earlier so that we can avoid T-Pose on the frame that the deformer becomes active / LOD changes.
* Fixed copy pasting resource node with matrix3x4 type creating a node with no pin.
* Fixed an ensure related to deformer graph instance settings in packaged build caused by incorrect object name used when creating the settings object.

#### Gameplay

**New:**

* Make Motion Warping switchoff conditions and warp target direction mode experimental as these APIs will change in future.
* Added support for animation mirroring to UAF.

  + Note this is a first pass and not fully matching Animation Blueprint's capabilities yet.
* Added a new version of AddAnimationNotifyEvent() that supports blueprint exposed data from notify events.

  + This helps prevent data loss when copying/duplicating animation notify events.
* Add SmoothWalkingMode to Mover2.0

  + Added base class SimpleWalkingMode to help make writing walking modes easier.
  + Renamed AnimationMath -> SpringMath and made public Rename SpringWalkingMode -> SimpleSpringWalkingMode.
  + Added Velocity Spring functions to SpringMath Add character prediction functions to SpringMath.
  + Added documentation to SpringMath.
* Added support for PoseSearchDatabase searches returning multiple results
* Added experimental support to the motion matching node (FAnimNode\_MotionMatching) for interaction searches (multi character motion matching, to mimic FMotionMatchingTrait).
* Added a custom make bp function for FMotionWarpingTarget to ensure that the custom actor is called to calculate the target transforms when a component is passed as an input.
* The ChooserTable randomization column can now keep track of multiple recently selected entries and reduce the probability of reselecting them.
* Added new Chooser table column type (FPoseSearchColumn) to support motion matching searches within chooser evaluations.
* Add a spring walking movement mode to Mover named "SimpleSpringWalkingMode". This uses a critically damped velocity spring model to translate and rotate the character.
* Removed UE 5.5 deprecations from PoseSearch plugin.
* Exposed anim to texture editor functions as a public interface.
* Add threadsafe method for getting curve asset float & vector values.

**Bug Fix:**

* Fixed UE::PoseSearch::SDatabaseAssetListItem potentially referencing a deleted asset.
* Fixed a crash when opening the PoseSearchInteractionAsset editor.
* Fixed FSearchContext::GetSampleRotationInternal and FAssetIndexer::GetSampleRotation not properly calculating the rotation relative to their reference bone.
* Fixed motion matching tracing during throttled or skipped searches.
* Stored FBlendStackAnimPlayer::StoredAttributes as FMeshAttributeContainer instead of FHeapAttributeContainer to support animation LOD changes in blend stack.
* Fixed a pose search database indexing crash when using a UAnimNotifyState\_PoseSearchSamplingAttribute referencing a bone that is missing from any channel included in the pose search schema.
* Fixed root motion sampling in blend stack.
* Fixed the motion warping switchoff condition to use the correct target transform when component following ends.
* Fixed a crash in UPoseSearchFeatureChannel\_Phase::IndexAsset when indexing assets with a single pose, usually caused by a very short animation in a pose search database.
* Fixed UPoseSearchDatabase::SynchronizeWithExternalDependencies mistakenly synchronizing transient assets into a database, leading to reference garbage collected assets.
* Removed notify guids from Pose Search Database hash generation, otherwise the hash can be non-deterministic.
* Fixed a crash in FAsyncPoseSearchDatabasesManagement::CollectDatabasesToSynchronize with Objects with invalid Object->GetClass().
* Fixed the Alias state nodes not working with getters like GetRelevantAnimTime.

**Deprecated:**

* Deprecated UPoseSearchDatabase TArray AnimationAssets in favor of TArray DatabaseAnimationAssets.
* Deprecated UPoseSearchLibrary::UpdateMotionMatchingState.

#### ML Deformer

**New:**

* Hide certain conflicting properties (categories even) from the advanced preview scene settings tab. This was needed because the MLD asset editor has its own mesh picking and animation playback. Changing those properties inside the preview settings tab would mess things up. So we now hide those specific conflicting settings.
* Make curves work with UAF.
* Added support for copy paste between input bone and curve lists.

  + Means users can copy/paste the input lists from one model to the other.
  + You can now right click the input list widgets and choose Copy and Paste.
  + Fixed a few bugs in the tooltips as well as unique curve group name generation.
  + Improved the UX a bit by setting a minimum height for the bone, curve, bone group and curve group widgets and some context menu improvements.
  + Fixed some UI refresh issues as well when adding bones or curves. Curve group and bone group coloring did not refresh properly.
* Improved performance of the asset editor. Improved responsiveness to property changes, faster loading, faster sampling of anims.
* Added a new console command "MLDeformer.DebugDrawInputPoses" which will draw the input pose to the ML Deformer. It can be useful to quickly visually see what meshes have ML Deformers on them, and what bones are included.
* GeomCache: Some improvements to the memory management. Prevented reallocs, resulting in faster performance.

**Bug Fix:**

* Fixed a problem where training with curves would cause a failure during training.
* Fixed a bug where curves on the skeletal mesh instead of on the skeleton would cause some error checking to fail.
* Fixed a crash when adding a bone to the inputs of the ML Deformer.
* Fixed a crash on undo on morph based models. Also changed the icon of the Train button.
* Fixed python errors when launching with "-game" as argument.
* Fixed a bug when training, related to masks of input animations. Training would fail with some error right after sampling.
* Moved the tick group from pre physics to post physics.
* Fixed a VertexDeltaModel python import error. This was because an import should have been inside the Train function, but it was in global scope.
* Fixed async loading issues.
* Some fixes where it would not detect curves.

#### Physics Control

**New:**

* Now supports using a mask when invoking control profiles, which means they can be applied to a subset of the character.
* Additional support for specifying control/modifier set names in function calls.
* Kinematic targets are now specified the same way across PhysicsControlComponent, RigidBodyWIthControl and ControlRigPhysics.
* Fixed duplication of the Linear/AngularTargetVelocityMultiplier and TargetVelocityMultiplier parameters.

**Bug Fix:**

* General minor fixes/improvements to the physics control asset editor, including a fix for a potential crash.

#### Runtime

**New:**

* Added pinning and toolbar to workspace viewport and remove scene description tab.
* Now supports drag/dropping multiple bones in the abstract skeleton binding editor.
* Bone items can now be dropped onto non-set items in the abstract skeleton set binding editor.
* Added a filter for attributes to anim asset browser.
* Added Initialize as a default implemented event in the UAF module.
* State Machine: Self transitions & UX improvements:

  + Self transitions and state re-entry are now possible.
  + Re-entering a state uses inertial blending and requires an inertialization node. Old content will not use the new re-entry feature but any newly built content, when re-entering a state, will create an error if an inertialization node is not present root-wards in the graph.
  + The target state must enable bAlwaysResetOnEntry for the inertial blend to trigger.

    - To aid with managing state-reentry, a new MinTimeBeforeReentry value has been added to transitions.
  + Added 'reverse transition' context menu option that just reverses the direction of transitions.
  + Relinking transitions to other states can now be performed from the transition tail as well as the head.
  + State alias list is now sorted alphabetically to make finding states easier.
  + Look and feel of state machines has been tweaked & improved.

    - Now uses SVG brushes to better scale.
    - Different node types (states, aliases and conduits) now have different shapes.
  + Transitions now rotate to follow their direction and have been moved closer together and closer to their link line.
  + Transitions now sort in front of states.
  + Links are now further apart and scale correctly with zoom level.
  + Selection of links now scales correctly with zoom level.
  + Details panels for states now show the anim node functions for their result node and have been rearranged.
  + Added 'force transition' option to the context menu for state machines that are currently being debugged.
  + Made machine entry nodes non-deletable.
* Extended the Create Asset menu to allow non-asset menu entries for wizards that create potentially multiple assets of various types.
* Added a picker widget for animation attributes.
* Added toggle to blend layer trait to blend in mesh space.
* Added live updating blend mask weights in the profile blend node.
* Updated animation blueprint interface icon in the 'My Blueprint' tab to show as blue when the function has been implemented.
* Exposed Curve Metadata API on the Skeleton to Blueprint and Python. This includes functions to query, add, remove and rename curve metadata as well as querying and setting material and morph target flags.
* Disabled adding set bindings without a set collection set.
* Added a viewport to the workspace for UAF.
* Paused preview animation while manipulating transform widget in animation editor.
* Added an asset wizard for help authoring UAF content.
* Added foundations for the abstract skeleton runtime.
* Added editors for the abstract skeleton assets.
* Added functionality to Open in New Tab via the context menu for collapsed nodes and function nodes in UAF
* Fixed collapsed nodes and functions in UAF workspaces being opened without context of their outer, leading to loss of access to variables.
* Fixed debug only assert when opening items via double click the workspace outliner.

**Bug Fix:**

* Fixed a missing drag-drop op for adding attributes to sets in the set collection editor.
* Caught a situation where the mesh asset in InitializeAnimScriptInstance is invalid. Also dealt with possible parallel anim eval tasks being in flight.
* Fixed a crash when trying to create a new UAF Workspace instead of picking an existing one when prompted to choose a workspace after opening a newly created UAF Graph.
* Fixed slow document navigation in the workspace editor.
* Fixed a crash when attempting to add an existing curve attribute to abstract skeleton binding.
* Fixed being able to rearrange a trait onto itself.
* Fixed for animation modifiers not reverting correctly and crashing in some instances.
* Fixed a crash when re-removing a pin on a blend multi node after undoing.
* Fixed a broken root motion extraction during animation modifier evaluation.
* Fixed a regression in root motion extraction which prevented animation modifiers from reading raw uncompressed data during the compilation process, causing them to fail
* Fixed missing text localization in pose asset widget.
* SkeletonCompatibility: Fixed a problem when using compatible skeletons where we could end in a situation where the source skeleton did not have a bone of the target skeleton, which could lead to a crash.
* RBAN: Ensure RBAN doesn't write NaNs into the pose.
* Fixed visualization of what the blend weight of the animation is in Animation Insights for Random Sequence Player. Now it takes the overall blendweight of the animation into account as well.
* Fixed the look at edit mode locator gizmo not updating location when changes are made in the details panel
* Anim State Machine:

  + Fixed incorrect duplicate GUID warning when a transition rule is shared.
  + Prevented renaming states to 'None'.
  + Fixed copy-paste of transition nodes creating duplicate GUIDs/assets.
  + Fixed clamping values preventing manual entering of valid negatives.
* Anim Sequence: Fixed thumbnail scene references preventing deletion when assets contain notify states.
* Anim Assets: Fixed a crash when creating a preview scene for assets with a deleted compatible skeleton.
* Fixed the animation sequence segment length
* Fixed a button in the montage editor not working due to property access type mismatch
* SkeletalMeshComponent: Fix meshes getting ticked offscreen incorrectly when using montage-related visibility options
* Fixed pose history and trajectory history desync by delta time, causing incorrect results especially noticeable when the component transform makes large translation and rotation, e.g. a 180 pivot.

  + This fixes a bug with bad pivot selection when the capsule rotation flips
* Fixed incorrect timings on trajectory history when delta time is not constant.
* Fixed duplicate trajectory entries around t = deltatime.
* Fixed the set collection editor not updating when renaming a set, and added rename to the context menu.
* Fixed the expansion state of tree items resetting when drag/dropping a bone in the abstract skeleton binding editor.
* Fixed drag-dropping segments into composite track not matching selection order.
* Fixed window scaling issue when dragging multiple notifies in the animation editor.
* Changed check to ensure in SkeletalMeshComponent to avoid crash using rewind debugger.
* Fixed many SAssetShortcuts unnecessarily refreshing on asset opening resulting in slow ABP navigating.
* Animation Budget Allocator: Enabled component tick when unregistering.
* Updated the animation attribute functions to not allow adding an attribute with a name that already exists.
* Anim BP: Fix cook non-determinism with generated 'mutables' struct
* Anim Instance: Fix memory leak when GC-ing both mesh & anim instance in the same pass.
* Fixed an issue with tooltip names in SOverrideStatusWidgets.
* AnimSequence: Fix uninitialized pose transforms being generated in some circumstances
* PropertyAccess: Fix memory leak when calling functions via property access that return non-POD values.
* Anim Decompression: Removed usage of deprecated GetCompactPoseIndexFromSkeletonIndex.
* Fixed copying notifies when duplicating an anim sequence so the new notifies no longer reference the old sequence.
* Fixed the UAF asset wizard template assets being visible in the content browser and selectable in the workspace picker etc.
* Added more inline crash details when invalid values are found in animation poses.
* PropertyAccess: Hardened GetAccessAddress in case of unexpected data.
* SkeletalMeshComponent: Fixed a crash when calling SetAnimInstanceClass during a notify callback.
* Triggered caching of all otherwise lazily computed data when a DNA is loaded from a binary stream, which can avoid potential race conditions if the same DNA reader is utilized in a multithreaded environment.
* Fixed not being able to move nodes within newly created comment nodes in Control Rig and UAF.

**Deprecated:**

* Removed deprecated Skeleton Compatibility code from the Skeleton class.
* Removed deprecated Curve code from the Skeleton class.
* Removed deprecated Mesh Linkup Caching code from the Skeleton class.

#### Sequencer

**New:**

* Property tracks can now be renamed.

  + Note, the tooltip will still show the actual name of the property being animated.
* Added setting to always stop when going to playback start or end.
* Sequencer Navigator: There are now columns for the sequence ID and the object binding ID which are useful for debugging purposes.
* Take Recorder: Add a cvar TakeRecorder.AllowPossessablePIEObjects to bypass disallowing recording PIE objects as possessables. The default is to not allow this (no change in behavior). This can be useful when recording a player pawn.
* Added scripting to text
* Added ISequenceVisitor callbacks for when the visit enters/exists a sub-sequence
* The camera cut track now supports multiple rows. When multiple rows exist, the camera cut track does not try to auto arrange sections.
* MovieScene: Exposed FLevelSequencePlaybackContext to other modules.
* Hot key scrubbing will continue playing if Sequencer was playing.
* Preview camera cuts in simulate. This also lets users enable/disable seeing camera cuts in PIE after ejecting from the player controller.
* The colors for the playback start/end range can now be customized by user settings.
* Added support for notification callbacks when animating properties.
* The timeline in the cinematic viewport now respects the snapping behaviors of the Sequencer timeline.
* Added fixes and improvements to the time space display. The desired time space and the local time space are now both drawn.
* Bake Transform now has an option to bake with time warp applied.
* Attach sections with Preserve None now default to infinite duration.
* 'Bake Animation Sequence' and 'Create Linked Animation Sequence' actions in Sequencer now remember the last folder that was used in the current Editor run.
* Bake Transform is now available in the Template Sequence and Camera Animation Sequence Editors
* The subsequence section's Origin Override Location/Rotation now respect the default float/double spinbox incremental behaviors.
* Sequences: Add PlayReverse function to actor sequence components.
* Editing scale channels in the Sequencer Key Details now has an option to preserve the scale ratio
* Save As is now available in the Template Sequence and Camera Animation Sequence Editors.
* Added the ability to get and set Mute Nodes, Solo Nodes, Deactivated Nodes, Locked Nodes, Pinned Nodes, and Binding Tags in Blueprints/python.
* The view and working ranges are no longer saved with the asset. Every time you open a level sequence, it will be zoomed to the playback range.
* Duplicate keys are now removed on mouse release
* Update tooltip to "The interpolation type for the initial keyframe" to clarify that this is only for the first keyframe on the track/section
* UE\_API all blueprint exposed functions for Sequencer Scripting

**Bug Fix:**

* Refactored track instance bindings and added the concept of "volatile" paths to fix possible memory stomps when animating array items or instanced structs.
* Fixed an issue where when changing shots we could sometimes get one frame of t-pose on a character when using bForceCustomMode. The issue was that we were checking for custom mode too late in the frame relative to when we were potentially doing the binding to a custom anim instance.
* Fixed the color not reverting when pressing cancel on the color picker.
* Added an adjustment for an issue for capturing thumbnails for sequences. Renders at a square aspect ratio and cleans up some advanced rendering features to create the cleanest image possible like materials.
* When opening a sequence, the playback mode is now set to loop selection range if a selection range is set.
* Fixed the BakeToControlRig function. Now fetches the templateID for the sequence that we're in so that if the sequence we are working on is a nested, instance, or template sequence we can resolve objects within the function.
* Added support for indirect gizmo manipulation of sub track offsets.
* Added support for animating property bag properties.
* Fixed a possible GC leak with UMG animations. It happened when using an event track, and the widget is removed from its parent while the animation is playing, and then the inactive widgets pool is discarded and GC'ed.
* Sequencer Navigator: The marks column now properly updates when marks are changed/added/removed.
* Exporting a binding that doesn't have a valid spawnable template no longer crashes
* Fixed a GC error in restore state of skeletal mesh animation track.
* Properly implemented end-at-time feature.
* Now stores camera shake previewers as shared pointers because FGCObject classes are not relocatable.
* Fixed Material Parameter Collection track display name so that it's not set explicitly on creation. Instead, the display name is just the name of the MPC if the user hasn't changed it. This allows the user to change the MPC and the name will automatically change.
* Proxy bindings no longer allow you to mistakenly pick the same actor it is a proxy for.
* Key selection is no longer emptied when right clicking on the timeline.
* UMovieSceneSequence: Fixed nullptr crash.
* Fixed pre-roll/post-roll sometimes still evaluating sections that aren't set to evaluate there.
* No longer falls back to the double blender system when a property doesn't have blending information. Instead, it falls back to the fast path where we don't blend anything.
* Fixed broken support for ping-pong playback when we only cross the loop boundary once.
* Fixed the pre-animated state being incorrectly saved as "persistent" for root tracks.
* Deleting a muted track row now properly no longer causes other rows to lose their mute state.
* When a fixed timescale is set negative, ranges 2 levels down no longer collapse causing subscenes of subscenes not to play correctly.

  + This only fixes the case of fixed timescale. Similar issues still occur using the playrate/timescale curve.
* Copying a folder now properly copies root tracks as well.
* .MovieSceneSequenceExtensions::FindBindingByName now returns a more reliable binding because it gathers the names from FMovieScenePossessable and FMovieSceneSpawnable which are kept in sync with the actor labels.
* Fixed a regression with a deprecated code path for fetching what animation is playing for UMG Sequences.
* Fixed pause-at-frame logic, which was sometimes incorrectly pausing on the previous frame.
* Select All Keys Forward and Backward now properly select all the requested keys.
* Selecting a layer bar no longer mistakenly deselects component bindings.
* Collapse Nodes and Descendants now properly collapse after being expanded.
* Copying a folder now properly copies all bindings and their child component bindings.
* Payload objects for event keys are no longer lost.
* Disallow picking a proxy binding that's already bound to the current one.
* Remove the "Blocking Evaluation" checkbox from the advanced menu, since we can already set it from the playback options.
* Fixed ongoing focus issues in the key details. Sequencer are now committed when focus is lost and keys are not accidentally created with incorrect values.
* Fixed the time warp curve still evaluating even while muted.
* Fixed a bug where the keyable indicator would not update for the selected object in the details panel after opening a sequence. It required adding to the sequence or selecting new objects.
* Fixed pre-roll/post-roll sometimes still evaluating sections that aren't set to evaluate there.
* Removed calling Modify from SetPreRollFrames / SetPostRollFrames. The caller should be responsible for calling Modfiy().
* If you copy an event track from one sequence to another, the events in the pasted event track will point back to the blueprint director in the copied sequence. This is not allowed, so those events are now cleared.
* Fixed creating an object property track as a class property in python not properly setting the bClassProperty value which allows a class chooser to pop up instead of an object chooser.
* Fixed keys not selectable on multiple rows.
* Restored a section model expansion state to be closed if it was before, since RestoreLayout resets it to expanded.
* We now tear down the Take Recorder's Sequencer instance before we delete and GC the sequence.
* Re-added dropped support for Blocking Evaluation in UMG animations.
* Fixed a crash when reinitializing a Sequencer editor on a new sequence while the previous one had legacy tracks
* When importing cameras, now applies a uniform scale modifier to distance based parameters (Manual Focus Distance).
* No longer blends enum values, and make the byte track use the enum system when it animates an enum.
* Ensured that evaluation context buffers are flipped if an eval task is active prior to forced update.
* Added a potential fix for a memory corruption of UMG animation states.
* The topmost unmuted Cinematic Shot is now correctly evaluated.

  + Previously, if a muted Cinematic Shot was topmost, it wouldn't be skipped over.
* Fixed some properties that should appear to be animatable (i.e. FieldOfView and AspectRatio for Cine Camera Components).
* Fixed an issue that when converting to a spawnable, sometimes the original possessable meshes were still visible.
* Fixed undo of camera cut section now restoring the camera binding properly.
* Fixed regression of pre/post-roll behavior in the skeletal animation track.
* Creating the initial key for material tracks now respects the default interpolation type setting.
* Snap play time to pressed/dragged key only if snapping is enabled.
* Fixed a reference-leak in the Track Instance system.
* Setting the time of a key through the Properties menu now works properly.
* Keying specific channels of a transform through the Details Panel now properly sets the key with those current values (and not 0).
* Fixed calls to bool property custom accessors, which were using the wrong function signature.
* Better handling looping for camera cut tracks:

  + Added a new "HasLooped" flag on the evaluation context.
  + Assumes by default that looping sequences are "seamless" and do not create a straight/hard camera cut on loops.
  + Added an advanced evaluation flag to opt out of this assumption.
* Fixed undo not working when editing with control rigs.
* Now fully supports all camera and post-process properties when previewing blending camera cuts.
* Disabled ensure before cleaning up camera cut track viewport modifiers.
* Fixed regression in how skeletal animation sections behave when resized from the left edge.
* Take the first loop start offset into account when determining if a skeletal animation section needs to loop.

**Deprecated:**

* Deprecated FMovieSceneBinding::Name since it's redundant and not kept in sync with actor labels.
* Can now return multiple objects with FMovieSceneBindingResolveResult. FMovieSceneBindingResolveResult's Object is deprecated in favor of an array of Objects.
* Migrated text tracks to Movie Scene Tracks plugin (enabled by default). Deprecated MovieSceneTextTrack plugin.

#### Skeletal Editing

**New:**

* Skin weight profiles can now be switched directly in the skeletal editor viewport, if there are skin weight profiles defined for the skeletal mesh asset.
* Edit Weights Tool: Fixed removing weights from vertices weighted fully to a single bone turning them into unweighted vertices.

Bug Fix:

* Animation: Editing the text field in the curve editor of an anim montage no longer crashes.

### Editor

#### Datasmith

**Bug Fix:**

* Fixed 3dsmax plugin support for 2026.

#### Framework

**New:**

* Fixed GetOwnerPackages() for instanced structs inside non-complex properties.

  + FStructurePropertyNode::GetOwnerPackages() fails at walking up the property nodes for a specific case, and may trigger an ensure. When stumbling upon an instanced struct, GetOwnerPackages() walks up by getting the direct parent.
  + However, this parent is not necessarily a complex parent (can be a non-object/structure property type). To make sure the walk happens correctly, the case should be handled the same way GetInstancesNum() does (get complex parent of parent).
* Added a few virtuals to cosmetic SGraphNode getters.

  + Useful while adding advanced styling in custom node editors. In some cases it might be possible to avoid overriding engine methods by implementing our own variants, with different names, but not in every case.
  + Also reusing original methods makes the programmer's intent much clearer - what part of the base class was actually overridden.
* Implements experimental Capture Stealing in ITF Input Router.
* Updated MathStructCustomization metadata extraction to include InstanceMetadata

  + This change updates metadata extraction for header row to include InstanceMetadata. It is useful when assigning metadata to Vector/IntVector types via other customizations.
* UToolMenu Items will now override any parent Tool Menu Items of the same name.
* Positioned Tool Menu Items that fail to be positioned will now be inserted at the end of the section.
* Improved reliability of legacy SExtensionPanel support in the new viewport toolbar. Extensions are only enabled when there is enough information to support their existence.
* ToolMenus: Adds options for whether a Tool Menu Entry with an insert position that can't find its target should insert anyways and/or log.

  + Defaults to both inserting & logging.
  + Disables logging if the ToggleViewportToolbar and ToggleHideViewportUI commands can't find the ToggleFullscreen command in the Level Editor Window menu.

**Bug Fix:**

* Fixed an edge case Blueprint Editor crash on exit.
* Fixed an issue where top-level toggle buttons in Viewport Toolbars looked like raised buttons.
* Users can now change the derived type on default value instantiations used to initialize a base type reference member in saved instance data when using override serialization.
* Fixed the asset reference filtering not working when dropping assets on Material, Niagara Script and Texture Graphs, or on nodes and pins of any asset graph type.
* Fixed inconsistencies between drag and drop visual feedback and drop behavior in Animation State Machine, Sound Cue, and Texture Graphs.

**Deprecated:**

* The old Level Viewport Toolbar Panel Extensions are now deprecated. They will be removed in a later version.

#### Interchange

**New:**

* Reduced memory usage when importing static meshes.
* Added a SubdivisionAPI custom schema for specifying per-prim subdivision level.
* Added support for array node attributes.
* Added support for subdividing static meshes and geometry caches when importing via USD Interchange.
* Added more C++ UsdWrapper types and tweaked the Unreal.natvis file to improve how they're displayed on the debugger.
* Upgraded MaterialX version to v1.39.3.
* Textures imported with non-power-of-2 dimensions or non-multiple-of-4 dimensions were previously automatically set to NeverStream and Uncompressed. This can now be toggled with a config setting :TextureImportSettings::bDoAutomaticTextureSettingsForNonPow2Textures .

  + Also when textures initially imported as nonpow2 are re-imported as pow2, they now get their settings automatically fixed to the defaults for pow2 textures.
* Improved the performance of importing skeletal meshes with multiple morph targets via USD Interchange.
* When importing USD stages through USD Interchange, SkeletalMeshComponent prims will be spawned with AnimSequences assigned to them, if any were imported.
* Added a "Use Single Bone" option to import a static mesh as a skeletal mesh with top node as the only bone.

  + If "Force All Mesh as Type" is set to "Skeletal Mesh" and "Use Single Bone" is checked, the imported skeletal mesh will have a unique bone at its origin called "Root".
* Added a new option to the USD Export Options dialog when exporting levels to USD called "Export to Nested Sub Folders", which restores the previous behavior of exporting asset layers to a folder structure that mirrors the content folder structure
* Interchange: Added support for importing OBJ into level.
* Reduced memory usage when importing skeletal meshes.
* Upgraded OpenUSD version to v25.08.
* Interchange USD can now import groom assets and groom caches.
* Added support for dome lights via SkyLightComponents when importing via USD Interchange.
* Removed FNavigationOctree::AddNode Warnings during Level Import.
* Implemented a Nanite triangle threshold value on the Interchange generic asset pipeline, in order to enable Nanite only for meshes past a triangle count size.
* The USD Interchange translator has a new setting for collecting prim metadata as translated node user attributes. It can also specify a regex for filtering of particular metadata fields.
* Refactored the LevelSequence handling for USD imports in order to properly support subsections due to references and payload arcs.
* Importing via USD Interchange will now reuse generated assets when importing instanced prims.
* Added support for OpenUSD on Windows ARM64.
* Refactored skeleton handling in Interchange USD to not consider the skeleton prim itself as a root joint, which prevents transforms applied directly to the skeleton from being ignored in some cases.
* Interchange USD imports that preserve the pseudoroot node will now produce a top-level actor named after the root layer's display name, as opposed to being always named "/"
* Now uses the default static mesh collision profile for static meshes generated via the USD Stage Actor imports.

**Bug Fix:**

* Fixed Reimport not showing skeletal mesh conflicts.
* Fixed missing AnimSequence assets when importing animation tracks via Interchange that have a total length below MINIMUM\_ANIMATION\_LENGTH (of 1/30 seconds)
* USD: Editing keys in Sequencer now properly update back to the USD Stage.
* Fixed node name collision suffixes appending to previous suffixes, producing names like Cube12345
* Fixed actors with identity transform being imported via Interchange with the inverse transform of their parents in some cases.
* Fixed imported LevelSequences overwriting others with the same name when importing some very complex USD scenes.
* Fixed cameras imported from OpenUSD with fStop of zero so that depth of field effects are correctly disabled.
* Fixed incorrect skeletons being imported via Interchange FBX in some edge cases when TransformLinks seem to represent local transforms.
* Fixed static mesh collider transforms being incorrect in some cases when importing into level with Interchange.
* Fixed some issues with baked skinned mesh transforms when importing skeletal meshes with morph targets via USD Interchange.
* Fixed how AnimSequences seemed to have no animation data after using Actions -> Import on the USD Stage Editor.
* Fixed issues with using Material Search Location when importing scenes with Material Instances via USD Interchange.
* Fixed automated reimports still showing the options dialog when reimporting via Interchange or USD.
* Fixed metadata not making it onto actor AssetUserData when importing scenes via Interchange in some scenarios.
* Now discards empty LevelSequences when importing from USD.
* Fixed SparseVolumeTexture assets not being generated by USD Interchange when importing scenes with volumes if the exact same volume node shows up on the stage more than once.
* Fixed a crash when trying to parse USD LodSubtreeAPI schema applied to skinned meshes.
* Fixed import of UsdPreviewSurface into Material Instances for USD materials that have output connections to other shader graph or material prims.
* Fixed performance bottleneck when importing many lights via USD Interchange.
* Fixed some name-prefix-based collision meshes not being correctly used when importing via Interchange in some cases involving name collision.
* Can now generate the desired simple collision meshes even if the shape disagrees with the provided mesh data.
* Fixed morph target normals and position offsets not being skinned with geomBindTransform when importing skinned meshes via USD.
* Fixed how Interchange USD was not using timeCodesPerSecond values when baking skeletal animation tracks.
* Fixed incorrect vertex ordering of subdivision surface meshes imported from OpenUSD when their orientation is "leftHanded" and subdivision is enabled.
* Fixed a crash when parsing some USD SkelRoots configurations with multiple Mesh prims that contain normals.
* Fixed how USD asset imports were persistently disabling the "Import Into Level" option to import actors.
* Fixed OpenVDB being imported via USD stages without compensation for the stage's upAxis and metersPerUnit values.
* Fixed level exports to USD always using absolute file paths for layer references and payloads.
* Fixed Euler flipping issues when importing some USD stages with complex rotation animation.
* Fixed invalid skeletons being produced when importing some USD stages with prim names that are not globally unique.
* Fixed various issues while importing an asset containing elements named "None"
* Fixed support for UDIM textures when opening or importing USD Stages via the USD Stage Actor.
* Silence a couple warnings when trying to fetch transforms from Interchange scene nodes with none authored.
* Fixed missing actors and assets when importing scenes via USD Interchange that contain sibling prims whose names differ only by character casing.
* Fixed a crash when resaving assets imported with Interchange after deserializing them with Interchange disabled.
* Fixed HeterogeneousVolumeComponents not refreshing after their SparseVolumeTextures imported via USD Interchange were reimported.
* Fixed incorrect skeletal mesh influences when importing skeletons with multiple root bones via Interchange USD.
* Fixed various import issues related to using names that resolve to NAME\_None.
* Fixed risk of missing content when importing FBX containing assets or bones requiring name sanitization.
* Fix SparseVolumeTexture assets imported via Interchange USD ending up named as "Null" if the VDB filename itself was purely numeric.
* Fixed the handling of some skeletal mesh edge cases via Interchange USD, like nested LOD meshes.
* Fix transforms placed directly on LOD meshes being ignored when importing into level with Interchange USD.

#### Scripting

**New:**

* Exposed FullyLoadPackages/FullyLoadAssets functions to editor scripting via EditorLoadingAndSavingUtils

  + These fully load the given objects, so that UE no longer has a write lock on their on-disk files (eg, when needing to overwrite the file via an external application).
  + This is also available in the UI via Asset Actions -> Load, if you hold shift while clicking on Load.
* Added support for texture-based tool icons in Scriptable tools.
* Added support for setting a custom UUserWidget above the tool details panel of a Scriptable Tool.
* Preview Platform Blueprint Functions:

  + TogglePreviewPlatform: Toggle the Preview Platform On/Off
  + SetPreviewPlatform: Sets the Preview Platform.
  + The Preview Platform is set from a list of valid Preview Platforms, the same present in the Preview Platform Menu.
* Added a Disable Preview Platform Blueprint Node.
* Added a GetDrawableGeometryActor() BP function to fetch the actor that owns any line, point and triangle sets added by a Scriptable tool.
* Exposed FTSTicker to Python:

  + This exposes the superior and safer FTSTicker-based ticking method to Python, and existing Python scripts using the Slate-based ticking methods should consider migrating to use this new method (unless forwarding ticks to an embedded UI framework, which was the intent of the Slate-based ticking methods).
  + The new ticker callables can be registered via `unreal.register\_ticker\_callback(...)`, which takes a callable (taking a float delta time, and returning a bool where True means continue to tick), along with the delay (in seconds; default 0) that we should apply between each ticker callback. `unreal.unregister\_ticker\_callback(...)` can be used to remove a previously registered ticker callback.
  + Examples:

    - def run\_once(dt): print("run\_once") return False # stop ticking
    - unreal.register\_ticker\_callback(run\_once, 1.0) # call run\_once once after 1 second
    - def run\_many(dt): print("run\_many") return True # continue ticking
    - run\_many\_handle = unreal.register\_ticker\_callback(run\_many, 1.0) # call run\_many repeatedly after 1 second delays
    - unreal.unregister\_ticker\_callback(run\_many\_handle) # stop calling run\_many
* Exposed the ability to include or exclude editor-only references from script asset registry queries

**Bug Fix:**

* Added an encoding fix for PipInstall to force a utf-8 encoding.
* Fixed a crash in ExecutePythonScript when Python was disabled at runtime.
* Fixed a crash when re-registering Scriptable tools during mode shutdown.
* Fixed reachable garbage objects warnings when compiling ScriptableTools containing ScriptablePoint/Line/Triangle sets.
* Fixed an issue with accept/cancel/complete actions not firing in ScriptableTools mode.
* Fixed 'no world was found for object' warnings when invoking WorldContextObject functions in a Scriptable tool.
* Fixed a crash when calling DataTable RemoveRow from editor scripting.
* Fixed non-deterministic tool order in Scriptable Tools category palettes.
* Added a fix to ensure AssetTools do not call slate functions in headless.
* Fixed Python Callback attached to Dynamic Delegate
* Editor can now run even if Python is not able to load properly.

#### UI

**New:**

* Significantly improved the Content Browser column sort performance for large search results.
* Updated the Content Browser navigation bar so clicking in the empty space edits the package path if available instead of the virtual path.
* Slate drawing optimization: fixed float comparison of the alpha that could send an invisible element to the renderer, for negative or small alpha values.
* In the graph editors, right clicking to summon the node context menu now includes the hovered wires connected pins, if any. This allows, for example, insertion of a 'NOT boolean' node on a bool wire in the blueprint editor
* Made the "Show Selected" action for actors always visible in the context menu.
* SlateIM: Add support for Tab widgets
* CommonUI:

  + Updated CommonWidgetCarousel to be more consistent in its widget caching.
  + Added an option to determine whether or not to cache widgets at all
  + Old behavior was to cache widgets in the carousel's RebuildWidget, but widgets added at runtime via AddChild would never be cached.
  + Currently caching is enabled by default to match the behavior when children were added at design-time, though this could result in increased memory usage in use cases where all widgets were added dynamically.
* Added a clockwise ordering option for DynamicEntryBox.
* Updated the source control Submit dialog to display full file paths for non-asset files in the Path column.
* Waveform editor: Add icons for fade options
* Waveform:

  + Now calculates LUFS and Sample Peak values on audio import, on Waveform Editor open, and on Waveform Transformation changes.
  + Now displays LUFS and Sample Peak as meta data when hovering over a soundwave in the content browser.
* The Path column in the Asset View will now display the package or object path of the row item if available instead of the virtual path.
* Redesigned Platforms menu moved from the toolbar to the main menu.
* Can now specify a screenshot view rect via FScreenshotRequest::RequestScreenshot:The view rect will be ignored if it is invalid (empty or not within the extent of the render target), or if bShowUI=true, since that takes the slate widget screenshot pathDefault behavior remains the same (to screenshot the whole window)
* Enabled 10-bit swap chains on desktop platforms even when the feature level is ES31.
* Slate: Modified GetCachedWidget:

  + GetCachedWidget now returns the Widget returned by RebuildWidget.
  + GetWrappedWidget returns the Widget return by RebuildDesignWidget if available. Otherwise, returns the widget returned by UIComponents via RebuildWidgetWithContent.
* Added InitializeInEditor function to UserWidgetExtension and WidgetBlueprintGeneratedClassExtension to be able to support proper initialization in Editor for Extensions.
* Added utility functions to query private states in the widget.
* UMG Bindings: Added a new Conversion Function SetVectorParameter that takes a FColor and converts to FLinearColor.
* Added support for package path suggestions to the Content Browser navigation bar.
* Added support for navigating to C++ class package and object paths entered into the Content Browser navigation bar.
* Optimized the font shaping process when using complex shaping (typically for Arabic).
* Added a Python script for generating an html color palette for the FColorList class.
* Updated mouse capture and high precision mode handling on Windows to save up to .5ms on redundant API calls
* A UFont can now be a wrapper around FCoreStyle::GetDefaultFont(), for use with editor UI.
* Added a CVar `Slate.UseSharedBreakIterator` to support shared ICU Break Iterators to reduce CPU usage. False by default.
* Added new Header and ToolHeader sections to the ToolkitBuilder.
* Added support for MVVM Bindings in asset diff tool.
* Exposed world context pin on MVVMViewModelBase. This allows blueprints on a Viewmodel to access world subsystems (assuming they have an object they can use to resolve the world context).
* Add SetLazyContentWithCallback to CommonLazyWidget to improve async usage in blueprints.
* Add blueprint function, SetViewModelByClass, for setting VM by class on a widget directly to simplify usage.
* Exposed a setter for CategoryToolbarVisibility in FToolkitBuilder.

**Bug Fix:**

* Fixed a regression where Toolbar buttons with a combined options menu did not display that options menu when the toolbar button was clipped.
* Fixed an issue where Spline-related UI elements were displaying XYZ axis labels and tooltips even when the editor was running in LUF coordinate mode.

  + Details: Updated the context menu and details panel for Splines so that axis labels, tooltips, and action names now correctly reflect LUF when active.
  + This includes context menu areas like SnapAllToSelected, SnapToLastSelected, and SetLockedAxis (temporarily disabled).
  + This also includes Details panel areas for Spline settings like Selected Spline Nodes Location, Rotation, Scale, Arrive Tangent, Leave Tangent, and Up Vector Logic was added to ensure these UI elements are now dynamically aligned with the current coordinate system.
  + XYZ (FLU) remains the fallback when LUF is not enabled.
* UMG Sequencer: Fixed 2 issues.

  + When adding an event track as the first item in a widget animation, the duration of the animation would reset to 0, and notably the playback range start would be set to exclusive (range as (0,0)). This would persist after the length changed, for example to (0,500), meaning that any items placed on the 0 frame, such as events, would never evaluate.
  + When not encountering the above issue, items placed on the 0 frame would evaluate twice. This was due to a refactor to the way widget animation would playback.
* Fixed the Asset View Type column sorting by the full class path rather than the display name that is displayed.
* UMG:

  + Fixed named slot content not saving for named slot instances of widget blueprints that extend widget blueprints.
  + Fixed CDO de-sync with root widget property changes.
  + Added a fix to avoid crashes in cases of re-entrancy.
  + Various fixes for widget animations:

    - Fixed a crash caused by the runner being invalid for an unknown reason.
    - Fixed iteration of active animations that can grow during that iteration.
    - Fixed iteration of animated widgets that can grow during that iteration.
  + Fixed first and last frame evaluation of animations - Don't tick the widget on the first frame, wait until the next frame. The flag for that was lost during the animation refactor in 5.6 - Fix the evaluation time for when stopping which should indeed be the first frame of the playrange, not frame 0. This was incorrectly ported during the animation refactor.
  + Fixed how we consume the current animation time on play, to prevent events at frame 0 from firing twice.
  + Double clicking on a color key in the timeline now correctly opens the color picker.
* Fixed an inconsistency in the Viewport right-click context menu, where the Transform options were always ordered according to FLU rather than the expected LUF, even with LUF coordinate system in use. Behavior is now consistent and context-aware across coordinate systems.
* Can now pick struct type when class type picking is enabled, eg, from within the Data Table editor
* UMG Designer:

  + Fix to FWidgetBlueprintEditor::SelectObject to support UObject selection. Fixes a nullptr access when a property was changed in the detail panel on an object that is not a UWidget.
  + Fixed a crash in Drag and Drop operation. Added more checks around calls to GetCachedWidget that can return a null object during drag/drop and move operation.
  + Fixed a crash in UMG Designer Replace widget context menu operation in the Hierarchy panel. This happened when using the replace function with a User Created widget selected in the Palette panel.
* Optimized the widget editor's palette to reduce refresh cost in large projects.
* Fixed virtual texture thumbnails sometimes showing the wrong texture.
* Fixed an issue where screen-space widget components wouldn't render for players other than player 1 if splitscreen is disabled. There is now an option (ShowAllPlayerWidgetsWhenSplitscreenDisabled) to overlay the player layers, instead of culling out all player layers except for player 1.
* Fixed a regression that caused the editor to crash when attempting to place a cooked Actor-based Blueprint class via drag/drop.
* Fixed a memory leak when trying to trigger the display of a FCanvasBatchedElementRenderItem without a primitive to draw.
* Fixed an issue where SearchableComboBox couldn't be set back to the same value after resetting to default.
* Fixed an issue where SCommonButton wouldn't release when it loses focus
* Fixed a rare crash in SlateRHIRenderer due to both main thread and render thread possibly writing to the same arrays simultaneously.
* Fixed a situation where the Asset Dialog hotkeys either didn't function, or operated on the wrong widget.
* Slate: Fix SStackBox not respecting the Orientation slate arg.
* Fixed various possible crashes and bugs when importing offline fonts.
* Fixed Content Browser columns appearing as sorted after you click on their headers in the column view even when they are no longer the active primary or secondary sort columns.
* MetaSounds WaveAsset: Removed create new asset actions for unsupported assets.
* CommonUI:

  + Fixed not being able to click buttons with Virtual\_Accept while binding hold actions to Virtual\_Accept.
  + Ensure UCommonInputPlatformSettings load is done at the right time to avoid a synchronous load flushing async load request. Now PostLoad will be called as expected for all UPlatformSettings.
  + Fix persistent action bindings not always being registered as persistent actions.
* Fixed custom dialogs non-deterministically aligning their buttons.
* Fixed an issue where FQuat variables always displayed with the name "Rotation" in the details panel, regardless of DisplayName metadata or the variable's actual name. This fix ensures that the intended name is respected and shown properly in the UI.
* Fixed a typo in BoxElem.h
* Prevented Pin Value Inspector Tooltips from using global invalidation, as it can cause broken tooltips or crashes in some scenarios.
* SlateIM:

  + Fixed a case where child rows would not get removed when no longer drawn.
  + Fixed Viewport roots preventing mouse input for the whole viewport.
* Fixed an issue in the ListView Widget where OnEntriesGenerated would fire for each entry instead of firing once all entries are generated
* Fixed a crash in SObjectWidget OnFinishedPointerInput missing CanRouteEvents that causes nullptr access.
* Fixed Message Log not displaying when failing to save packages.
* PropertyPermissionList: Fixed buttons not appearing for functions marked CallInEditor details panel unless added to AllowList explicitly.
* Fixed an issue where users can't type polish letters s and a (with a tail) into the text input.
* Fixed an issue with Slate Screen Reader at initialization of the plugin.
* Add missing validation check with enabling or disabling SWindow.
* UMG Viewport: Made sure we EndPlay on the preview world during teardown.

**Deprecated:**

* Deprecated SCustomDialog VAlignButtonBox since it didn't affect the button layout, but could result in the button rendering outside the dialog if VAlign\_Center was used.

#### UX

**New:**

* StylusInput: Added MacOS support.
* Change the default of bUseLinkedOrthographicViewports to `False`.
* Simplify the camera speed settings to just expose the camera speed. Min/max values are still exposed in settings.
* Slice graph connections by alt+middle-mouse dragging in the graph editor.
* Fix a bug where viewports could control the movement of a locked actor in a different viewport.
* Added support for direct manipulation of editor viewport orthographic near & far planes.

  + Added a new Editor Viewport Depth Bar that provides visual control over those planes.
* FDateTimeStructCustomization now has a tooltip. Hovering over a DateTime property's text box in the editor provides a hint at the format.
* Disabled use of a Template SoundWave, can be re-enabled in Editor Preferences->Audio Editor Per Project Settings.
* Switched to camera-relative vertical panning by default. Add an option for world-based vertical panning.
* Waveform Editor:  Instated Waveform editor as the default SoundWave editor.
* Splits viewport panning logic so that the middle mouse button and the left+right mouse button gestures are distinct. Middle mouse can be camera relative (and continues to be so by default) while left+right mouse button always move up and down.
* Outliner: Added visibility function versions that work on the selected actor's hierarchy and set H to default to toggle selected hierarchy.
* Asset Picker Size Scaling as Editor Preference: Added the Editor Setting "Scale Asset Picker Widget Size" to allow the size of asset pickers to be scaled up or down.
* Added a new "Toggle Selected Actor Visibility" command & behavior. This command takes the default "H" binding from "Hide Selected Actors". The command:

  + Hides selected actors if any actors in the selection are visible.
  + Shows selected actors if all actors in the selection are hidden.
  + Does not affect selection.
* Show template projects from all plugins:

  + Problem:

    - New Project dialog only listed template projects from enabled plugins Users couldn't see or start from templates included in installed but disabled plugins.
    - Empty/invalid background image paths in template categories showed broken visuals
  + Solution:

    - Updated search to include template projects from all discovered plugins Added warning icon + tooltip for templates from disabled plugins.
    - Selecting a disabled plugin template shows a warning/error box that the plugin is not enabled.
    - Warning is non-blocking (no modal), project creation proceeds after user confirmation.
  + Notes:

    - Keeps behavior lightweight.
    - Surfaces risk (no additional modal asking to confirm creation) but doesn't block flow.

**Bug Fix:**

* Ensured that the "Hide Selected At Startup" action now correctly applies to all selected actors, regardless of their current visibility state. Previously, actors that were already hidden were skipped by this action. With this change, both visible and non-visible actors will be consistently marked to start hidden on load.

### Foundation

#### Build

**New:**

* AssetManager, AssetRegistry: Add Property AffectsCookRule to ManageReferences.
* Extended the AddExternalImportValidation of missing UClass imports to validate imports of all native types.
* Added support for the 'Activate' flag in PluginReferenceDescriptors. This fixes an issue where the 'Activate' flag would be deleted from plugin descriptors when running some UAT programs.
* IncrementalCook is now enabled for DLC cooks, but for DLC cooks it is still experimental and is not yet robust.
* UHT: Added support for engine version comparisons as preprocessor conditions.
* Prevented Clang builds for Windows from launching multiple link jobs simultaneously to avoid memory exhaustion.

**Bug Fix:**

* DLC Packaging: Fix missing .upluginmanifest when packaging without -DLCPakPluginFile.

  + With the plugin manifest present the output folder from a DLC package can be copied into a packaged game as-is and will load through the default plugin discovery and loading process.
* SavePackage: Fix errors in IllegalReferences diagnostic; it now more accurately finds the object and property that caused the illegal reference.

#### Core

**New:**

* Added UE::CFloatingPoint concept.
* Added value hashes and sizes to DDC replays
* RemoteObjects:

  + Transactional RPCs can be rescheduled per Actor. This means the transaction can abort and try other transactions while we wait for needed dependencies to service the RPC.
  + TimerManager now has some limited transactional support.
  + Exposed GetClass that may skip migrations when used with FRemoteObjectId.
  + Exposed GetRemoteId() on TWeakObjectPtr
  + Distinguished between Loaning out an Object and Reassigning a Borrowed Object. This helps clarify some situations, particularly where you're sending an object and maintaining ownership you can just check if you're Loaning it now, because ReassignBorrowed is now a separate case (which means another server has borrowed it, but you never owned it).
* Allow third-party crash handling to use `FAdditionalCrashContextStack`.
* Default WindowsPlatform.bClangStandaloneDebug to true. This slightly increases pdb size when compiling with clang, but improves debugging experience.
* FStateGraph and FStateGraphNode no longer timeout if -NoTimeouts is provided on the command line.
* Added [[nodiscard]] to mutex functions.
* Added [[nodiscard]] to TLess, TGreater and TEqualTo.
* Optimized TCppStructOps vtables to only include functions that will be called. This now prevents users from making UScriptStruct or TCppStructOps a friend in order to allow your class only constructible by the CoreUObject system.
* Refactored FInstancedPropertyBag's CopyMatchingValuesByID function to allow the caller to provide a matching function. Added CopyMatchingValuesByName that matches properties by name instead of ID.
* Added FRecursiveWordMutex to support very early and/or very late recursive mutex usage.
* Removed LLM dependencies on FCriticalSection and FRWLock.
* Eliminate static log records in the absence of source location and log tracing to reduce program size.
* Made mutating EnumClassFlags functions usable in constexpr contexts.
* Added UE\_LIFETIMEBOUND to TValueOrError.
* Exclude trace state when log trace is disabled and optionally compile out source location from logging to reduce program size.
* Use Yield() instead of YieldThread() when spinning in mutexes to improve performance under heavy system load.
* Optimized ParkingLot::Wait when there is no timeout.
* Added UE::CContiguousRange and CPointer concepts.
* Added CCharType concept and applied it in TStringView.
* Added Max() functions to sets and maps - and TSparseArray which is needed for sets.
* Replaced TSortedSet's O(N^2) Append with an O(N) (at best) or O(N log N) (at worst) and added tests.
* Added some basic TSet tests, based on the existing TMap tests.
* Specialized FPlatformManualResetEvent for each platform that we target.
* Added FOutputDeviceFence to support lifetime management of dynamic log records
* Updated debug visualizers for TDeque, supporting visualisation of elements when the container is set up to use a different allocator such as TInlineAllocator or TFixedAllocator.
* Add explicit nullptr constructor/equality operators to TWeakInterfacePtr Mark functions in TWeakInterfacePtr [[nodiscard]]
* Fixed overallocation for unused null terminators in TStringBuilder.
* Added TFunctionWithContext to adapt a callable into a function pointer and context
* Improve accuracy of GC time limit by setting object destroy granularity to 10 (instead of 100) and provide a way for it to be tweaked per project with gc.IncrementalBeginDestroyGranularity.
* Optimized ParkingLot callback code generation
* Updated UE::Core::Private::StringLength to use TCString::Strlen outside of a constant-evaluated context, to speed up compile times with MSVC.
* Added UE\_IF\_CONSTEVAL and UE\_IF\_NOT\_CONSTEVAL.
* Updated Oodle to 2.9.14.
* Used InitializeCriticalSectionAndSpinCount to avoid an extra function call during construction of FWindowsRecursiveMutex.
* Added CConvertibleTo concept mirroring std::convertible\_to.
* Added a configurable intrusive unfair non-recursive mutex.
* Added TInstancedStruct::NetSerialize function.
* Removed contention on root flags when pinning weakobjectptrs.
* Improved the logging backlog to minimize the number of missed log lines during the initialization.
* Added TLogTemplate and control over log template allocation.
* Added IsLocked and IsLockedShared to the mutex types.
* Add Async.ParallelFor.DisableOversubscription which if enabled will only use existing threads which can be faster when cores are saturated.
* Added support for nested $format in structured log formatting.
* Added Intel OneAPI and Microsoft Clang 19 HWPGO integration.
* Added an ExecFileOverride resource to BootstrapPackagedGame.
* Optimized FLazyName to support constant initialization.
* Deflate, gzip & lz4hc compressors now honor COMPRESS\_BiasSpeed and COMPRESS\_BiasSize
* Added TExternalStringBuilder and support for TStringBuilder<0>
* Improvements to GameFeaturesSubsystem and FPluginDescriptor:

  + Added a new hook to PluginDescriptor to allow customized loading of uplugin json data.
  + Updated GFS to ensure that, at least in the editor, we will try to use the PluginManager's copy of the plugin data rather than re-reading it and deserializing it from json ourselves. This is necessary to take advantage of the customized loading.
* Enabled custom crash handling for GPU crashes.
* Optimization for FSoftObjectPath::ResolveObjectInternal to avoid the round trip to/from string.
* Add a console command, core.ResetEnsureState, to reset the ensure state so they fire again. This will cause all non-always ensures to trigger again if they've already been suppressed.
* Reduced memory use by FOutputDeviceFile by 992 KiB in the default configuration.
* Added better error messages when TLess, TGreater and TEqualTo when used with a type without the corresponding operator.
* Now validate LinkerSave unmapped objects against the package harvester excluded object list. This removes the limitation of asserting when FindObject is called while GIsSavingPackage is set.
* FPaths:CreateStandardFilename: changed behavior to normalize paths that cannot be standardized: .. is collapsed when possible.
* Added UE::CNotCVRefTo concept.
* Removed dependencies on ParkingLot from Windows stack walking
* Made the MSVC implementations of FPlatformMath::CountLeadingZeros and FPlatformMath::CountTrailingZeros constexpr.
* Added format string validation to LowLevelFatalError.
* Added UE::CStringViewable and UE::CCompatibleStringViewable concepts.
* ThinLTO is now enabled by default for Clang based toolchains.
* Added an experimental plugin, Global Configuration Data, that can be used as a single point of access to data that may be provided from different systems.

  + Can be used to have console and config data added to blueprints without additional code.
  + Additional data routers can be registers to expand on what data sources are available to the system.
* Added UE::CArithmetic concept.
* Added UE::CCompatibleCharType concept and some usage in TStringView.
* Added UEOps.h to aid in the correct generation of all binary comparison operators based on a couple of simple member function definitions.
* Replaced the UTF8CHAR enum with C++20's char8\_t.
* Added checks for non-trivially-relocatable types being used in containers, particularly FGCObject-derived types.
* Added UE\_REWRITE, a replacement for FORCEINLINE intended to be used on macro-like functions (rather than for optimization) by 'rewriting' a function call as a different expression.
* Enabled override max printed reference chains via `gc.MaxReferenceChainsToPrint` Cvar.
* FVector2D deprecated comparison operators (from 5.2 onwards) removed.
* Remove deprecated FLinearColor methods, deprecate unused DXT block structs.
* Enabled TSharedPtr and TUniquePtr to be usable as keys in sorted containers, and TUniquePtr to be usable as keys in hashed containers.
* Added std::initializer\_list support to TSparseArray.
* Fixed UPS cooking indeterminism for TBox[2] structs on stack Make ForceInit constructor zero out padding.
* Fixed managed storage handle attempting to resolve an unmanaged file more than once after the manager becomes active.
* Added UE::CDerivedFrom concept.
* Added debug visualizers for UE::Math::TVector2<> and FDeprecateSlateVector2D.
* Extended `gc.PerformGCWhileAsyncLoading` to provide the option to garbage collect while async loading, only when low memory is detected (based on gc.LowMemory.MemoryThresholdMB).
* Package flags are now thread-safe.
* Add TargetRules.bIdenticalCodeFolding setting (--icf=all).
* Added intrusive unset optional support to TNotNull.
* Added a benchmark for mutex types.
* Added CSameAs and CDecaysTo concepts.
* Added UE::CIntegral concept.
* Added tests for Algo::StableRemoveIf.
* Added configs managing how GenericPlatformMallocCrash handles allocation requests on non-crashing threads, allowing them to permanently suspend on allocs/frees, suspend on allocs and skip frees, or process as normal.
* Removed dependency on FCriticalSection and ParkingLot in memory allocators.
* Retry in the shared mutex TryLockShared while there is not an exclusive lock.
* Added support for joining non-contiguous ranges in TStringBuilder.
* Added support for optional sub-object references in localized structured log formatting.
* Reduced codegen impact of ensure() macro.
* Added an overload of CreateLogTemplate that takes the format as FText.
* Added support for $locformat in structured log formatting.
* Added NotNullGet for retrieving the inner value from a TNotNull without an explicit cast.
* Experimental Visual Studio 2026 support.
* Added a new experimental API: SpringMath:

  + This includes some useful functions for critically based spring damping
  + Added experimental blueprint library for spring math to expose functions to BP
  + Added SpringMath::ExponentialSmoothingApproxQuat to mirror the existing function FMath::ExponentialSmoothingApprox.
* Added support for creating Property Bag Placeholder types for entity prefabs.

  + This is done via a new table added to package files: ImportTypeHierarchy table.
  + Each entry of that table contains hierarchical information for every FObjectImport entry that is a type (e.g., UClass).
  + This is the second part of a 2 part change. The first change introduced the package file header change along with the object version bump.
  + This change adds the remaining logic to save/load the new table and the change to use it when creating placeholders.
* Added support for AVX10.
* Added write helpers to RapidJsonUtilsAdded UE::Json::WriteCompact and UE::Json::WritePretty, to write a UE::Json::FDocument to a FString in either compact or pretty form.
* Added UE::Json::MakeStringRef and UE::Json::MakeStringValue to help convert a FStringView to a UE::Json::FStringRef or UE::Json::FValue when building a JSON DOM.
* Added some additional aliases to UE::Json that are needed when building a JSON DOM.
* Switched UE::Json aliases to use the UE FMemory allocator, rather than rapidjson::CrtAllocator.
* Added --prioritize-dependency-scanning SN-DBS build option.
* Added `FNonshrinkingAllocator`, which changes the shrinking policy to No by default.
* Added hidden MetaData works for base structs in Instanced Structs.
* Cooker:

  + CookPackageSplitter: Changed the return value of GetGenerateList to a struct (and changed the name to ReportGenerationManifest) so that generators can request that the package containing the generator be not saved.
  + Deprecated the ability to run the cook inside the editor process when launched from editor. The cook instead should always be executed in a separate invocation of the CookCommandlet. This has been the default since 5.3, and we are now deprecating the ability to change that default and will remove all support for it in 5.9.
  + Added the following commandline arguments:

    - -cookshowremaining
    - -cookshowpackagenames
    - -cookshowinstigators
    - These provide a clearer behavior than -dpcvars=cook.displaymode=1|2|4.
    - Each flag can be specified with a value: -cookshowremaining=1|0, or with no value, defaulting to 1: -cookshowremaining.
    - These flags override whatever value has been assigned via config or -dpcvars commandline.
* Introduced a mechanism for render asset updates to be abandoned by owning `UStreamableRenderAssets` so `UStreamableRenderAssets` can be garbage collected independently (See r.Streaming.EnableAssetUpdateAbandons). Abandoned render assets are ticked during GC or every streaming update if r.Streaming.TickAbandonedRenderAssetUpdatesOnStreamingUpdate is true (defaults to true).

**Bug Fix:**

* Changed FMonotonicTimeSpan::IsInfinity() to stop matching negative infinity.
* Fixed FMath::FindDeltaAngleDegrees and FMath::FindDeltaAngleRadians for input deltas outside [-540, 540] degrees.
* COMPILE\_WARNING reports as error when WarningsAsErrors is being used.
* Fixed a potential infinite loop in the serialization of packed ints when loading malformed values.
* Fix potential deadlock in the scheduler if a foreground task is scheduling a background one.
* Fix potential deadlock in object annotations because of 2 different locks used in different order.
* Made -VerifyGC and -NoVerifyGc take all verification cvars into account.
* Fixed invalid access to memory location error in UnrealBuildTool.
* Made sure that pinned UObject are preventing GC of clusters they are part of.
* Fixed composite EPackageFlags not being shown in the debugger, caused by non-power-of-two enumerators.
* Fixed \_GetUObjectPacked intrinsic for debug visualizers. This addresses an issue with visualizers for weak object ptrs not working in builds where UE\_ENABLE\_FUOBJECT\_ITEM\_PACKING == 1.
* Made TBox's InverseTransformBy and TransformProjectBy both check for box validity before transforming (matching TransformBy).
* Fixed issues trying to load redirected native classes using the StreamableManager (and AssetManager).
* Fixed a bug in GC timing where if it destroyed exactly 100 objects in a frame it could cause a large stall.
* Fixed many log categories having a default verbosity higher than their compile-time verbosity.
* Fixing a crash in CppStructOps caused by unloading a dll at an inopportune time resulting in a dangling pointer to a vtable.
* Fixed TMemoryWriter IndexSize to be a bit count.
* LaunchEngineLoop: Fixed a copy paste mistake in the error message, it now correctly identifies that it fails to load the Game Engine class instead of the Editor Engine class when instantiating GEngine.
* InstancedStruct: Fixed the operator= when copying from a TConstStructView.
* The loader will now flush any remaining async loads before PreExit to avoid async loading to perform operations past the exit point.
* Fixed UE\_STATIC\_ASSERT\_COMPLETE\_TYPE for zero-sized arrays.
* Enabled seeking to the end of a response body without returning CURL\_SEEKFUNC\_FAIL in the Curl implementation in DevHttp module.
* Fixed UI layout for a particular view of the crash report dialog where the screenshot preview can cover button controls.
* Fixed clang miss-leading indentation warnings.
* Checked zlib init and shutdown for errors.
* Cleaned up usages that expect nullptr\_t to be in the global namespace.
* Fixed StaticDuplicateObject when Source Object class and Destination class are different.
* Fixed crash when loading content from corrupted pak or optional segment files.
* Disabled nuget audit for the dotnet Development configuration to prevent unactionable dotnet build errors.
* Force synchronous writes on type library input files.
* Fixed pipe and task timeout calculations that generated bad code.
* Deferred invoking the class initializer on duplicated objects until after subobject instancing has occurred.
* Disable 'C4702: unreachable code' when use bUseInlining is disabled.
* Fixed potential race condition in FConfigCacheIni::ForPlatform adding plugins without holding the lock.
* Fixed text import of delegate properties with full object paths, and made FDelegateProperty consistent with FPropertyMulticastDelegate on text export.
* Added static\_asserts to TValueOrError to ensure that it's not instantiated with references.
* Fixed a FARFilter with only WithPackageFlags or WithoutPackageFlags set failing to return any assets from IAssetRegistry::GetAssets(...).
* Avoid TInstancedStruct::GetPtr/GetMutablePtr and TStructView/TConstStructView::GetPtr crashing when the underlying struct data is incompatible with BaseStructT

  + This will now ensure instead, though will still perform the bad cast in a shipping build, so any ensures need to be fixed!
* Fixed TStringView::CopyString for copying an empty range.
* Fix a missing test of MaybeWaitingFlag in FManualResetEvent before parking the thread.
* Fixed Algo::RemoveIf calling the predicate too many times in some cases, and added some tests.
* Rehashed map and set properties after instancing key subobjects in their overrides of FProperty::InstanceSubobjects.
* Disabled AutoSDK for LowLevelTests targets.
* Fix thread scheduler to properly apply the cvars TaskGraph.UseDynamicPrioritization, TaskGraph.UseDynamicThreadCreation, and TaskGraph.OversubscriptionRatio which can be used to modify thread performance.
* Adding -nocrashreports support for windows. When provided, we will log crashes/ensures/etc but will not perform more complex reporting that could risk hanging on a file pipe.
* Reimplemented TVectorRegisterType with partial specializations rather than std::conditional\_t to work around alignment issue using Clang on Windows.
* Disabled custom property lists during native struct serialization.
* Fixed a race waking threads in FSharedMutex and FSharedRecursiveMutex.
* Added workaround for getting an array reference element from an rvalue tuple under MSVC.

**Deprecated:**

* Deprecated Alignment in TStaticArray and fixed UB behavior in it's GetData. Made TArrayView and Invoke constexpr.
* Deprecated TSortedMap::GetMaxIndex, fixed TSortedSet::GetMaxIndex and correctly commented TSet::GetMaxIndex and TMap::GetMaxIndex.
* Deprecated public and protected ways of initializing TStringBuilderBase from a buffer.
* Deprecated member TFunction::CheckCallable which was never intended to be public.
* Deprecated TIsConst.
* Deprecated PLATFORM\_COMPILER\_SUPPORTS\_CONSTEXPR\_BUILTIN\_FILE\_AND\_LINE.
* Replaced bExactClass with EFindObjectFlags in the FindObject family of functions.
* Deprecated the original log template API.
* Delete FCbFieldIterator::MakeOwned() to avoid breaking the iterator.

#### Dev Tools

**New:**

* Added compile warning argument ordering.
* Wildcard support in project sections of UGS ini files.
* Improved the summary outputs of UnrealPak. The units of memory now scale with the number of bytes making it easier to read for both smaller and larger containers.
* UBT DefaultBuildSettings:

  + Build Settings V6 now applied to wundef.
  + Default Build Settings Updates for Targets - V6 - engine.
* BuildCMakeLib: Added support for building third-party projects with CMake using the Ninja build system.
* Adding capabilities to the warning defaults, cleaning up tests, adding more warning+error strings for easier long term adoption & toggling.
* UHT will flag U macros (i.e. UCLASS) found in skipped blocks of code as deprecated. This will be made a warning in a future version of UE.
* UBT Editor: Added graceful messaging for Target upgrade requirements on editor path.

  + Emit the target build settings version & build environment to target file for editor runtime consumption.
  + Consume target file metadata to improve error messaging for Target versions.

**Bug Fix:**

* Fixing a bug where UAT could hang waiting for output. We now log a warning instead.
* Shaders: Fixed the shader pipeline skipping work if the number of shaders to compile is less than the number of tasks available.
* Fixed an issue where if a TInstancedStruct is used as a function argument, Clang platforms would fail to compile.
* Fixed BuildCookRun to include base build .sig files when generating patches.
* Updating UHT to once again generate an error when a USTRUCT contains more than one base.
* Fixed an issue in UnrealVS that could cause UnrealVS.P4->History to open an empty window
* Updated UnrealVS - Includes fixes to test discovery and execution
* Corrected define usage (UE\_BUILD\_SHIPPING vs UE\_SHIPPING)
* Fixed UHT parser issue where if FArchive is forward declared when used in the Serialize function declaration, UHT would fail to generate the proper code.
* Fixed inconsistent exception logging in Gauntlet.TestExecutor. It now consistently uses Exception.ToString().
* Fixed issue in UHT where it was allowing a USTRUCT to have multiple USTRUCTs as base classes.
* Fixed a bug where presets would be added to the global sync filters if the tab with the preset had its sync filter view opened and the okay button pressed.
* Fixed UGS not showing investigations as "resolved" when using Horde's metadata endpoint.
* Fixed destination files potentially not having the correct permission during SafeCopyFile in UAT, on non-Windows platforms.

#### Horde

**New:**

* BuildHealth Server Build: Added JobSummary telemetry.
* Hashed issue handler will now automatically check for a file property in the event's structured logging, and use that data in suspect finding. This should lead to suspect changes being identified more accurately, but relies on emitted warnings and errors including file metadata.
* Analytics:

  + Added a Build Health Dashboard View that shows step outcome history for selected templates & streams.
  + Add ExternalIssueKey & Fingerprint to the telemetry payload for issues. Also includes AnalyticsIntegrationTests.
* Added example of implementing a new Secrets Provider for Azure Key Vault. This secret provider is experimental and provided as an example of how to implement a custom secret provider.
* Added Secrets plugin configuration option WithAws that controls if the AwsParameterStore provider is enabled.
* Added new Secrets API api/v1/secrets/resolve/ that resolves a string to a property value of a secret. For example the string horde:secret:SecretName.PropertyName would resolve to the value of PropertyName for the secret SecretName.
* Only commits with Code CommitTag are considered when searching for Compile issue suspects.
* Removed the unused Password property from EpicGames.Horde.Streams.IWorkspaceType.
* Added the attribute ResolveSecret that allows properties in the Global Config to be resolved to the value of a Horde secret during configuration load.

  + If the property's value is of the form horde:secret:SecretName.PropertyName then if a secret SecretName exists and has a property PropertyName it will be replaced with the value from the Horde secret.
  + This allows sensitive configuration properties to move out of the configuration files to an external secrets provider such as AWS or HashiCorp Vault.
  + New: Updated the Password and Ticket properties for the Build Config's PerforceCredentials property to use the attribute ResolveSecret allowing Perforce credentials to be moved to an external secret provider.
* Changed build graph updates where a node that is skipped but modified does not fail the whole build. This allows the build to continue with only dependent nodes being marked as skipped while non-dependent subtrees can continue to run.
* Replaced the deprecated code coverage tool JetBrains.dotCover.GlobalTool with JetBrains.dotCover.CommandLineTools.
* Added to the Stream Config a StreamTags property, which is a set of name and Boolean pairs; and to the Schedule Config a Condition property.

  + The Condition property can be used instead of the Enabled property to control if the scheduled jobs for a stream should be enabled.
  + Each stream tag will have an environment variable named after it with the UE\_HORDE\_STREAMTAG\_ prefix and a value of True or False, which can be used in BuildGraph script conditions.
* Fixed an issue where capabilities for agents was missing their RAM capacity.
* Updated Temp Storage to allow the maximum number of exports to write in a single request to be configurable from the agent settings. The new option is TempStorageMaxBatchSize and defaults to a value of 20. Modified from contrib .

**Bug Fix:**

* API encounters ".NET type System.Text.Json.JsonElement cannot be mapped to a BsonValue" on swagger API invocations.
* Fixed an issue where GetNext for ScheduledDowntime would return the previous downtime.
* Fixed an issue where the log for the Downtime Service would print the next downtime being in the past when an expired non-repeating downtime was in the global config.
* Server Tests: Fix the DatabaseIntegrationTest class to properly forward dispose calls to the mongoDBRunner.
* BuildHealth Server: Exposed DateUtc on GetCommitResponse.
* Fixed an issue where capabilities for macOS agents was missing information for:

  + CPU number of logical cores.
  + CPU performance and efficiency cores for Apple Silicon.
  + GPU name and core count.
  + User name, domain name and running as administrator.
* Fixed an issue where the Notices Get method would not return the start and finish times, and if the start and finish times are set then set the active value accordingly.

#### Insights

**New:**

* Adds pre and post state change callbacks for TraceLog channels. Allows instrumentations to deny state changes and provide a reason for the denial, as well as performing actions when a channel is enabled or disabled, such as sending initial state, resetting tracked state or activating tracking.
* Added a method of creating a TraceAnalysis session using a custom data stream.
* Added an ability to copy a tooltip value to clipboard from the bookmarks track.
* The PlatformEvents channel now uses callbacks to deny enabling channels and provide user feedback, if requirements are not fulfilled.
* Added support to save data traced via the Direct Trace mode to disk. FDirectSocketStream can now accept an optional FArchiveFileWriterGeneric used to write the data to disk.
* Added support for Frame Start and End Misc Trace events in the minimal trace API.
* Added config variables to provide variable trace log write buffer size and prevent writer sleeping. This helps prevent the write thread from getting saturated under heavy load.
* Increased version of Unreal Insights to v1.08, for the UE 5.7 Release.
* Improved management of TraceLog worker thread in various scenarios. The worker thread can now be started on demand.

**Bug Fix:**

* Fixed a startup deadlock when launching with -trace=memory without tracehost or tracefile.
* Fixed an issue where FTraceAuxiliary::Relay did not respect the Options parameter provided.
* Fixed an issue due to Trace gap detection using three sync points. Previous logic used two sync points to calculate gaps, but the engine sends out three. In some scenarios this caused an error in gap detection which meant a higher serial was chosen as the next serial. This would leave much of the trace data unprocessed.

### Framework

#### AI

**Bug Fix:**

* Fixed an issue where selecting subnodes would result in the currently-edited property value to be discarded instead of applied.

#### AI Behavior Trees

**Bug Fix:**

* Fixed reinstantiation for Blueprint-based nodes using blackboard key selector.
* Fixed Blueprint reinstantiation issues with some BehaviorTree types.
* AAIController::UseBlackboard: Fixed to correctly return the result of trying to initialize the Blackboard.
* Changed InstanceIdx to use a const int32 to prevent a need for IntCastChecked to prevent possible data truncation.

#### AI Debugging

**New:**

* Added possibility in Rewind Debugger tracks to override the default behavior to step backward and step forward commands.
* VisualLogger log entry initialization can now also assign a valid location for components. With this change, double-clicking on such an entry will bring the camera to that location instead of the world's origin.
* Fixed GameplayDebugger local-multiplayer render duplication.

**Bug Fix:**

* Fixed ever growing buffer in FVisualLoggerBinaryFileDevice when VisualLogger is not set to record to file.
* Fixed debug draw helper functions and SmartObject visualization to properly handle scaled DPI.

#### AI EQS

**New:**

* EnvQueryTest\_GameplayTags: Added searching for tags container in actor's components if actor itself doesn't implement IGameplayTagAssetInterface.
* Upgraded the description details of the UEnvQueryTest\_Pathfinding test to better reflect its behavior in EEnvTestPurpose::Score mode.

**Bug Fix:**

* Fixed blueprint reinstantiation for EQS types

#### AI Navigation

**New:**

* NavLink Generation:

  + Added a name property to generation configs, and JumpMaxDepth can now be negative.
  + Activated the "enable" property now that multiple configurations are supported.
  + Added multiple link configurations for generated navlinks.
  + Added LinkGenerationSelectedConfig to debug a specific config.
  + Improved trajectory ground sample debug display.
* GameplayDebuggerCategory\_Mass: Now draws a purple circle around entities that are LOD off.
* AsyncNavWalkingMode can use navmesh normal instead of physics hit normal.

  + Now always take the highest hit location in z when searching for ground location.
* Mass Navigation:

  + Added text to MassNavigation::Debug methods.
  + Added an option to avoid slowing down when steering.
  + Added a MassSceneComponentVelocityTranslator to copy velocity between mass entities and actors.
  + Updated NPC desired movement based on current velocity when in animate mode for root motion driven NPCs. This helps with smooth blending into animated states from steering when character is root motion driven.
  + Added navmesh path boundaries to mass gameplay debugger.
  + Added logs in the navigation flow.
* Mass Entity: Fixed an infinite loop caused by loop variable overflow ().
* NavMesh: Added a navmesh tile building optimization when using CompositeNavModifiers with lots of data.
* Mass Navmesh Navigation: Increase default corridor width used by FMassNavMeshPathFollowTask.
* Pathfind: Changed warnings to logs when InitPathfinding can't find a polygon at the start or the end location.
* Removed deprecated 5.4 navigation code.
* MassNavMeshPathFollowProcessor: Improved logging information and clamping distance on the closest segment.
* MassNavMeshPathFollowTask: Removed overlapping points when building a corridor.
* Mass Navigation and Avoidance:

  + Made a fix to apply max speed in UMassApplyForceProcessor.
  + Added debug to display standing entities in mass avoidance.
  + Pathfollow -> Made a fix to keep the steering force when near the end of a path (we want to apply the fade only on the avoidance forces).
  + Used stronger avoidance forces when getting out of environment boundaries.Added an optional tag to prevent moving backward while avoiding.
* Navigation: Added in the output log information regarding invalid pathfind requests and changed log verbosity from error to warning.
* NavigationSystem: Replaced legacy repository unregisternavrelevantobject method with UnregisterNavRelevantObjectInternal.

**Bug Fix:**

* Navigation:

  + Fixed a crash occurring when building navmesh on PIE ending.
  + Made a tentative fix for a crash occurring when navigation is being rebuilt because a navigation override is being removed when clearing world components.
  + Update SplineNavModifierComponent to apply the NavAreaToReplace to its modifier.
  + Guarded against zero DeltaTime in UPathFollowingComponent::FollowPathSegment to prevent division by zero ().
* NavLink Generation:

  + Fixed missing links on small navmesh patches.
  + Made a fix to avoid filtering overlapping links if they used different navigation areas.
  + Fixed automatically generated navlinks being created without the NavLinkFlag.
* NavMesh:

  + Made a tentative fix for a rare crash in storeWallSegment.
  + Fixed assertions occurring in UE::NavMesh::Private::CalculateMaxTilesCount().
  + Fix FindDistanceToWall returning incorrect result and finding a closest position that is not on a wall.
  + Fixed editor crash when a large number is typed in the Agent Radius value.
* ISMC: Fixed an ensure in UInstancedStaticMeshComponent::GetNavigationBounds() caused by invalid navigation bounds. CachedBounds were being invalidated and not being recomputed when instances were added individually.
* ZoneGraph: Fixed problem with converting FZoneGraphTag::None to FZoneGraphTagMask ().
* Fix for AsyncNavWalkingMode using stale normals.

#### AI Smart Objects

**New:**

* Added method to retrieve a Smart Object slot's UserData from the SlotView.
* Added basic MRU slots implementation for MassSmartObject with settings in Mass SmartObject section of the project settings:

  + MRUSlotsMaxCount: Possible values between 0 and 4 (default: 0, meaning that the feature is not used; up to 4 slots).
  + bUseCooldownForMRUSlots: to allow the most recently used slots to be considered again a given period of time.
  + MRUSlotsCooldown: period of time during which a given slot will not be considered after being used.
* Added all camera controls to the SmartObjectEditor toolbar

**Bug Fix:**

* Fixed a crash in AITask MoveTo
* Fixed an issue where the NavNodeRef was not included when requesting the slot entrance location with the option for projecting to navmesh enabled.

#### AI State Tree

**New:**

* Added a rule to remove sustained state. All reselected states are new states.
* Added Blueprint helper 'RunStateTreeRunStateTree' to execute a StateTree on an actor. Helper will use an existing StateTree component or add it if necessary.
* Added Multiply operator to the Consideration score calculation.
* Added ExecutionExtension callback when a transition is about to be applied.

**Bug Fix:**

* Fixed a Runtime Validation false positive error when changing state trees without running any.
* Fixed a transition that didn't remove the frame when a sub-frame changes root.
* Prevented a reentrant call into StartTree and Tick for StateTreeComponent and GameplayInteractionsContext.
* Fixed temporary frames not cleaned up when we run multiple transitions and did State selection more than once.
* State tree references can now change while the tree is not run.
* Fixed editor freezing when the user spams undo/redo operation inside State Tree Editor.
* State Tree Editor: Hide level actor picker in the state tree editor.
* Fixed property function node value not being retained in new nodes when copied/pasted/duplicated.
* Fixed property bindings not being retained in new nodes if the old bindings were removed before pasting.
* Fixed details view not always syncing correctly with the selected editor node.
* Fixed Delegate Listener being unable to bind to the nested Delegate Dispatcher.

#### API

**New:**

* Added DrawDebugCircleArc version accepting a quaternion for orienting the arc with an arbitrary roll.

**Bug Fix:**

* SlateIM ComboBox now properly shows its selected value when spawned.

#### Audio

**New:**

* Waveform Editor:

  + Added a noise threshold for zero crossing logic.
  + Added an inverted S fade function.
  + Streamlined the trimming workflow to have new UI handles and be enabled on opening the waveform editor.
  + Added loop, delete, and conversion options when right clicking.
  + Playback hotkey adjustments to allow move playhead to start
  + Added an icon to fade handles.
  + Made adjustments to default nudge settings.
  + Added controls to scroll left and right when zoomed using the right mouse button.
* Made memory improvements for MetaSounds in the Operator Cache.
* Added a Fade Node in MetaSound Experimental.
* Added Blueprint equality operator for MetaSound literals
* SoundWave Cue Point Origin now has improved defaults. Default origin is now the Waveform Editor Transformation Markers, unless the .wav had cue points on import.
* Added a new Virtualization Mode: Seek Restart. This mode will virtualize, but keep track of playback time and, when realized, seek to that time as if it was playing the whole time. It's a less accurate, but more performant alternative to Play When Silent.
* Performance improvements when using and destroying a large number of Quartz subscribers.
* Metasound Trigger Filter node display name is now Trigger Chance to better convey its meaning. Some of its advanced pins are now hidden by default, and the node & pins tooltips have been made clearer.
* Added "MaintainAudioSync" input to Wave Player Node as an advanced input to the Wave Player MetaSound Node.

  + "MaintainAudioSync" will compensate for latency during playback of streaming wave assets so that the playback of the audio stays in sync within the playing MetaSound.
* Added a new debug display for Audio Modulation: au.Debug.Modulation.ActiveMixes

  + This will display all currently active mixes.you can choose whether Global Control Bus Mixes are included with au.Debug.Modulation.ActiveMixes.ShowGlobalMixes
* Both experimental and legacy subtitle fields are now initialized for DialogueWaves so users can switch between them.
* Added Subharmonizer MetaSound Node to standard library.
* Added an option to only support Vorbis decoding, not encoding, for memory-constrained targets.
* Renamed the "Create Subtitle" Asset Utility action to the more-specific "Make Asset UserData from Legacy Subtitles."
* Improved extendable MetaSound node configuration editor details customization.
* Added two new features to Control Bus Mixes:

  + Control Bus Mix Timer: Set a duration on the Control Bus Mix, and it will disable itself that many seconds after activating.
  + Retrigger on Activate: Optional behavior where, when a mix is activated when it's already active, it sets the values on the CBM to its default values and starts the attack over again (like retriggering an envelope).
* Added a new Asset Action Utility that enables converting Overlay assets into subtitles in bulk.
* MetaSound presets now inherit default metadata (ex. float range/clamp) from parent graph if applicable.
* Subtitles and Closed Captions plugin:

  + Multiple Subtitles can now be added to a single SoundWave. All of them fit inside a single Asset UserData.
  + No longer queues subtitles if the engine settings for subtitles are turned off.
  + Added an Enum to Subtitle Assets to distinguish when the duration property is relevant vs when it stops automatically using a sound's length.
  + Subtitles from now have a default priority of 1.
  + Subtitles created in a SoundWave's Asset UserData will automatically estimate the length of the sound and default their duration thereto.
  + Sequences now support dragging and dropping subtitles.
  + Changed the USubtitleTextBlock class name to USubtitleWidget.
  + Added automatic subtitle playback support for DialogueWaves inside SoundCues.
  + Added a Blueprint node for queuing all the subtitles in an Asset UserData at once.
  + Added a Blueprint function for hot-swapping the Widget.
  + Added StopSubtitlesInAsset BP function.

**Bug Fix:**

* Waveform Editor:

  + Fixed an issue where selecting a loop region marks the soundwave dirty.
  + Fixed an issue where highlighting and saving with a loop region selected disables the rest of the soundwave playing.
  + Fixed SoundWave markers with incorrect position data on export to USoundWave.
  + Scrubber Undo Fixes
  + Fixed frame length resetting to default instead of min when sliding loop region size.
  + Fixed exported soundwaves not supporting undo transactions.
  + Fixed ensure on undoing loop deletion.
  + Fixed editor crashing when closing out a Sound Wave asset after canceling to Export Waveform.
  + Fixed undo markers triggering ensure
  + Made UI fixes for markers with positive frame length
  + Made fixes to popup clearing.
  + Fixed right click getting stuck when scrolling waveform.
* Subtitles in the Subtitles and Closed Captions plugin with delayed starts now respect internal/external timing choices.
* Subtitles from the Sequencer plugin now correctly update their visibility when scrubbing along PIE.
* Fixed crash with MetaSound user preset widget tab.
* Fixed shutdown crash on Audio Streaming Cache handle ref counting.
* Fixed a bug where, when a submix is deactivated, Modulators attached to it would still be active.
* Fixed a bug where submixes with modulators could not disable via the Auto-Disable setting.
* Fixed an issue with the Seek Restart Virtualization mode where it did not properly account for changes in pitch before virtualization.

  + When the sound virtualizes, it will use the last pitch it was set to to estimate where it should seek upon realization.
* Sound Attenuation: Fixed == operator on FSoundAttenuationSettings.
* Fixed MetaSound relative render cost being incorrectly reported in some cases when using the operator cache.
* Fixed a bug where some Modulation inheritance settings were not working in some cases for non-volume modulation on sound sources.
* Fixed MetaSound comment node positions not saving properly after resizing.
* Fixed a bug where projects with the Audio Modulation plugin disabled had logspam.
* Fixed crashes when using MetaSound node configuration with pages.
* Fixed a MetaSounds edge case when the on-done trigger is triggered mid-buffer.
* Fixed a MetaSound crash when clicking audition menu after closing asset editor
* Fixed a bug where the Chorus Source effect modulation settings did not respond to Modulation changes.
* Fixed Sine Curves on FVolumeFader when used outside [0,1] range. They should now follow the expected curve between any two values.
* Fixed a bug causing various ITD features to have an enormous delay.

#### Blueprint

**New:**

* By default the Blueprint editor no longer searches for references to variables when the variables type is changed via the blueprint editor

  + To re-enable this behavior, set "bSearchForReferencesWhenVariableTypeChanged" to true in your editor settings.
* Can now call BlueprintFunctionLibrary functions from classes that do not implement GetWorld or ShowWorldContextPin. It now always shows the pins if needed and will always connect invisible pins even if they are marked as optional.
* Added a SetFocusInViewport node to UScriptableInteractiveTool. This means scriptable tools can give focus to the viewport so that key bindings pass through without user interaction.
* The Blueprint Debug Draw Line / Point / etc. methods now have the option to draw with 'screen' depth priority.
* Added ToRotationVector, MakeFromRotationVector and GetShortestArcWith to the Kismet Math Library.
* Structs tagged as HasNativeMake can now still have their individual members set.
* Asset/Actor Actions in Developer folders show for everyone.

  + GetBlutilityClasses already had code to ensure that we don't list other devs' blutilities.
  + However, it didn't use the correct path format, which caused FPaths::IsUnderDirectory to always return false.
  + Similarly, UEditorUtilitySubsystem::HandleStartupAssets never had a similar filter to begin with.

**Bug Fix:**

* Fixed failure to copy instanced Blueprint component value overrides on copy/paste workflows.
* CollectionsManagerScriptingSubsystem:

  + Removed a warning from GetAssetsInCollection when an asset could not be found.
  + Fixed an issue where logs displayed as red despite actually being warnings.
* Fixed an editor crash after clicking on a deleted graph node hyperlink in the Blueprint editor's compiler results tab.
* UK2Node\_VariableGet::SetPurity erroneously removed the SetPurity function from the public API of UK2Node\_VariableGet. This fix now re-adds SetPurity, but changes its implementation to use TogglePurity.
* Fixed an editor crash after clicking on a deleted graph node hyperlink in the Blueprint editor's compiler results tab.
* Fixed a crash when editing children from a cooked Blueprint that had editor-only components.
* User defined structs with Text fields with non-trivial default values no longer alter themselves on load.
* The Blueprint diff tool now reports changes to Create Event Node's signature function.
* Fixed potential for ICH override template namespace collision after reparenting an Actor-based Blueprint.
* The engine no longer crashes when it exits while a search in Blueprints is ongoing.
* Added more crash report context to paths where we are failing to resolve a node's owning Blueprint and/or graph, while using an ensure to avoid crashing the editor as a result.

#### Blueprint Compiler

**Bug Fix:**

* Fixed crash in SerializeUnversionedProperties during cooking.
* Fixed crash when cooking blueprints with local object references set to objects in asset.
* Fixed compiler failing to find newly added functions on Blueprint interfaces, which led to implemented functions being renamed.
* Fixed one cause of 'Reachable Garbage' when recompiling Blueprints.
* Blueprint's delegate signature checking logic no longer accidently looks at local variables when matching function signatures.
* Fixed one cause of loss of Blueprint subobjects when a Blueprint that is contained in another Blueprint is compiled.
* Fixed a crash in garbage collection due to mislinked SKEL\_ classes, most frequently seen during long-running cook operations.

#### Blueprint Runtime

**Bug Fix:**

* Fixed a bug where arrays of structs with custom identical operators could fail to copy from Blueprint generated classes correctly.
* Fixed push-model blueprint array property not properly marked dirty if modified by different actor.

  + The root cause of the issue is due to incorrect function signatures on array function thunks. Several of them mark their input array as 'const', but clearly change the array.
  + When push-model support was added, this problem was discovered and worked around by adding MARK\_PROPERTY\_DIRTY calls directly in the thunks. The problem with this solution is that it doesn't work when we change an array on a different actor.
  + Additionally, the thunk doesn't have enough information to determine that easily.
  + The correct solution is to leverage the existing code in FKCHandler\_CallFunction that has sufficient context to inject MarkPropertyDirtyNode accurately.
  + In order to get array functions working, we needed to fix their signatures to use UPARAM(ref) instead of 'const'. One issue with this fix is that there might be existing Blueprint code that incorrectly uses mutable array functions with read-only data.
  + For now, we'll support this, but with a warning to fix the code as it'll become an error in 5.9. Currently, this warning is disabled until we fix affected content.
* Fixed a memory leak when using containers with types that allocate memory by default.

#### Gameplay

**New:**

* Mover:

  + Added a method of canceling movement features by matching gameplay tags.
  + Added User-Defined Struct support for Mover data collections, so Blueprint-only users can include custom data without requiring native code.
  + Now supports spring-based walking mode work in networked play.
  + Reduced potential memory operations when adding to a data collection by preferring to copy onto an existing matching struct if possible.
  + Added options for supporting root motion for non-vertical moves, which makes possible combining them with gravity-based falling.
  + Added a double buffer for cached sync state to avoid issues with reading in data that may be freed/overwritten.
  + Added Mover-Mass translators along with a Mover Integrations plugin to house various integrations between Mover and other systems.
  + NavWalking mode now sets floor results in the Mover Blackboard when projecting to level geometry is enabled.
  + Added an auto-expire policy option for rollback blackboard entries.
  + Added support for blueprintable layered moves through a new system that splits up Layered Move Logic and Data.

    - This allows Layered Move Logic to be made natively and in Blueprints in an effort to expand blueprint support in Mover.
    - These new layered moves exist alongside the old ones at the moment with the intention of these new moves eventually replacing the old ones.
  + Added options for handling out-of-band movement changes, whether to warn about it and whether to accept it as the new starting sim state. Usage is primarily for non-networked play, where an external system is allowed to move the actor around, such as during cinematics or temporary physics simulation.
  + Converted absolute timesteps to double-precision.
  + Now supports avoiding state-copying operations when the simulation state doesn't change.
  + Added AdditiveVelocity MixMode support to MultiJump Layered Move.
  + Made small adjustments to the extended Mover pawn to make sure additive velocity is respected by turning off extra jump input from CharacterMoverComponent Jump.
  + Added option for flat-bottom floor checks.
  + Added consistent angular velocity when changing movement modes.
  + Adjusted mover API to use a FVector for angular velocity instead of a FRotator. This changes some public API related to Mover.
  + Removed the gravity orientation from angular velocity calculation.
  + Added simple montage replication support for the character-focused MoverComponent.
  + Added first version of rollback-aware blackboard.
  + Added experimental option to append inputs into sync state, for cases where you want to share inputs with sim proxies that are not simulated and may not have those inputs available.
  + Made MoveInput and MoveInputType BlueprintReadOnly, so setting this input is done through specific functions only. This means we can properly apply some precision to input to make sure all clients/server have same value after NetSerialization.
* Cameras:

  + Added Blueprint getter nodes for camera rig parameters.
  + Added evaluation context to transition conditions' API.
  + Now shows the name of the camera rig on the rig prefab node.
  + Added more debug information for blend stacks.
  + Added ResolveCameraRigProxy method to Blueprint camera director.
  + Moved lens calibration camera node to the CameraCalibrationCore plugin
  + Some changes to input slots:

    - Now runs input nodes in OnRun. OnUpdateParameters is only meant for pre-blending input parameters, not running actual logic, if only because it is run in isolation on just a few nodes that opt-in.
    - Moved the revert axis options onto the base input slot class.
    - Added a speed option on the input slot class. Pre-blend that instead of pre-blending the actual player input.
    - Moved the user-exposed option for accumulation onto the axis-binding specific node, in preparation of adding an actual accumulation node for more complex input chains.
    - Moved axis-binding code to a helper class in preparation of a "raw" input action node.
  + Added raw input action and accumulator node for complex input chains.
  + Added "driven control rotation" input node:

    - This input node makes possible using a "centralized" player input system which drives control rotation on the pawn, while still enabling cameras to have different orientations, such as when using target preservation with various lateral offsets (and therefore parallax requiring converging cameras with different orientations).
    - The active camera rig uses control rotation as-is, but any blending-out camera rigs use their last control rotation driven by the "delta" control rotation each frame.
    - This seems to be a good compromise between cameras limited by a single orientation and having player input managed by camera rigs individually.
  + Added the GetPlayerController method on the Blueprint camera node evaluator.
  + Added an option on camera components to set control rotation.
  + Added the ability for the Camera Debugger panel to bind to specific camera system instances (for instance, picking which Gameplay Camera actor to debug).
  + When drag-and-dropping a camera or camera rig asset onto a level or a sequence, create the corresponding actor.
  + Camera rig parameters now default to not pre-blended.

    - Defaulting to pre-blended benefited a few cases, but also caused visual bugs in a couple of other cases, so it's not worth turning it on by default.
  + Moved persistent rig activation functions onto the camera components and the camera manager.

    - These Blueprint functions were previously global, affecting whatever camera system host was currently considered "active".
    - This turns out to be unclear and prone to errors. Now the user activates persistent rigs exactly on whatever they intend to.
  + Now auto-create camera rigs and assets when nothing is specified on a Gameplay Camera component (but log a warning).
  + Made the orientation initialization service available to 3rd parties, and added an API for overriding the target or yaw/pitch to preserve.
  + Added a Blueprint utility function to access the evaluated camera's orientation.

    - Added Teardown API for node evaluators, added layer and active camera rig information.
    - Made node evaluator and evaluation service flags inclusive by default (i.e. opt-out).
    - Added a new "initialize with ideal framing" option on screen-space framing nodes.
  + Added a "family shortcut" bar to various camera asset editors for helping navigate between related assets.
  + Users can now set variables to be pre-blended.
  + Made QoL improvements to the Blueprint camera node.
  + Added bone/socket options to the attach to player pawn node.
  + Improved advanced camera shakes (add shake instance IDs and the ability to interrupt and stop a shake), improved the internal API for implementing shake nodes, and fixed a few bugs.
  + Implemented a more proper auto-build for camera assets for PIE.
* GAS:

  + Improved logging for missing attributes in FActiveGameplayEffectHandle when using GetGameplayEffectMagnitude.
  + Gameplay Tag display ends in an ellipsis when the display is cut off rather than overflowing.
  + Gameplay Tag and Tag Container meta data "DisplayShortTagNames" will now remove the Categories filter from the beginning of the Tag chip in the details panel.
  + Gameplay Effects stacking options now have better names and comments.
  + CooldownGameplayEffectClass validation: When a GameplayAbility is configured with a cooldown GE class, validation will check whether that GE applies any tags.
  + Updated the GameplayTagCountContainer to serialize tags itself and provide for fine control of what tags should replicate where via EGameplayTagReplicationState enum.
  + Exposing common GameplayEffectSpecHandle and ActiveGameplayEffectHandle queries to Blueprint. The following Blueprint callable functions have been added to AbilitySystemBlueprintLibrary to empower Blueprint programmers when making GameplayAbilities. Since some GameplayAbilityTask callbacks only provide a GE spec handle and/or active GE handle, now you can do more with those handles:

    - GetGrantedTags: Gets gameplay tags granted by a Gameplay Effect, from the effect's spec handle.
    - GetAssetTags: Gets gameplay tags describing the GameplayEffect, from the effect's spec handle.
    - GetGameplayEffectFromSpecHandleIsDurationGameplayEffectSpecHandle: Whether a GameplayEffect is instant or non-instant.
    - IsActiveGameplayEffectHandleValid: Whether a handle for an active GameplayEffect is a valid handle or not. Applied instant GEs don't result in an active handle.
    - IsActiveGameplayEffectHandleActive: Whether a handle for an active GameplayEffect is a valid handle and it's still applied.
    - GetAbilitySystemComponentFromActiveGameplayEffectHandle: Retrieving the AbilitySystemComponent from an active GE handle.
  + Renaming a gameplay tag in the Gameplay Tag Manager now automatically renames all sub tags.
  + Added predictive gameplay effect stacking and improved stack overflow handling.
* The data validation error for when there is a null input trigger on a key mapping now includes the name of the input action which it is mapped to.
* You can now call "SetShouldConsume" on any Enhanced Input bound action handles.

  + You can also define "ENHANCED\_INPUT\_ALLOW\_LEGACY\_BINDING" in your game's .build.cs file to enable legacy key bindings onto enhanced input components, making upgrading to enhanced input easier.
* Added GetActorFilter UPROPERTY meta support to object picker (mirroring GetAssetFilter).
* Added a virtual function to UBlueprint, ShouldAutomaticallyRegisterInputOnConstruction, which can be overridden in widget blueprints.
* Added a set of deprecated input action/axis names in the project settings.
* Added "Setter=SetShowMouseCursor" to APlayerController::bShowMouseCursor.
* Added ReleaseGameFeaturePlugins for multiple plugins at once. Unloading plugins batches GC and GameplayTags tree changes together which improves performance of unloading operation
* Added an editor preference for setting a "Simulated Device Mapping Policy".

  + This can be used in the editor to change how input devices get mapped to platform users, which can be useful for testing device connection sequences for your UI, log in flows, etc.
  + Added the current device mapping policy to the output of the "Input.LogAllConnectedDevices" command.
* Added helper functions to Ability system library: HasAnyAbilitiesWithCondition and HasAnyAbilitiesWithAssetTag
* Added QueueWorkFunction and SendQueuedWork to the TaskSyncManager which can be used to queue a batch of function pointers to execute as a simple tick task. This can be used with RegisterTickGroupWorkHandle to safely schedule batched gameplay thread work from any worker thread.
* Calling GetDeviceSpecificData now uses the given input device ID. If that is invalid, it uses the platform user's most recent device.
* Added LoadGameIfExistsAsync to SaveGameSystem which combines the exists and load checks into one async call to avoid an extra frame delay. Changed GameplayStatics to use this for async loads which fixes a warning when trying to load a nonexistent save game.
* Added ensure and comments to prevent creation of registered FTickableGameObjects on worker threads which is an unsafe race condition.
* Added an option to the FTickableGameObject constructor to enable creating with a disabled tick, which is safe on a worker thread.
* Added bindable "virtual" accept and back FKeys.
* Added a OnPostUserSettingsInitialized delegate to Enhanced Input, which will fire after the Enhanced Input User Settings have been initialized on the subsystem.
* Added more ways to detect a local player subsystem when using the node which does not have an explicit player controller target pin.
* Implemented SlideAlongNavMesh option for CMC NavWalking mode. This means pawns in NavWalking mode can move along a navmesh rather than just moving towards a projected point on the navmesh.
* CineCamera: Added an option to disable dynamic exposure.

  + Previously, turning off depth-of-field with FocusMethod would also turn off exposure simulation. This was fixed recently, but also meant that CineCameraComponent would now always simulate exposure, which isn't always desirable.
  + This change adds a new ExposureMethod setting to allow disabling exposure too.
* Made sure that the key mappings "supported key profile" tag is respected, and made the OnKeyProfileChanged delegate Blueprint assignable.
* Fixed a race condition crash on shutdown of the SteamController plugin.
* Added an "Input.LogAllConnectedDevices" command to dump all the currently connected input devices and some metadata about them to the logs.
* Reduced mouse input overhead on Windows by processing raw mouse moves on a separate FRunnable thread in the WindowsApplication..
* GameplayTags and GameplayTagContainers created in Blueprint give the user a way to edit the "Categories" metadata for tag filtering in the owning Blueprint.
* Fixed a crash where UPlayerInput::SmoothMouse would assert before it would attempt to divide by zero.

**Bug Fix:**

* Mover:

  + Fixed a bug in mover angular velocity clamping where the limit was not respected when rotating off axis
  + Added CommonLegacyMovementSettings shared settings in various movement modes to avoid a crash that could happen if they were the only mode added.
  + Fixed an issue where pawns wouldn't follow a navlink off the navmesh if bSlideAlongNavMeshEdge was true.
  + Nav walking modes now force a navmesh projection if something comes along and invalidates our last floor information, such as teleportation.
  + Now initialize the Mover mode state machine earlier so it can be used in backend initialization if desired
  + Fixed NaN issue in UMovementUtils::ComputeVelocity that could happen when MoveDirectionIntent was zeroed out.
  + Fixed issue where backends could leave stale non-persistent structs in sync state between frames.
  + Fixed several cases where strict equality checks on orientations could fail due to float point imprecision.
  + Fixed an issue where a specified InputProducer could fail to have ProduceInput called on it.
  + Fixed a Blueprint editor crash during validation if there's a shared settings object set to None.
  + Fixed issues with trying to maintain the small distance off of floors in falling/flying modes where a character could get pulled towards the floor.
  + Fixed improperly calculated angular velocity for mutli-axis rotation cases, and added utility function to compute it.
  + Fixed a bug in standalone mode where the time step was being rounded down to the nearest whole millisecond.
  + Fixed floating point precision error in mover's fixed delta time calculation.
  + Finding a movement modifier by handle and by type now searches through the queued modifiers on the Mover State Machine as well. Fixes an issue where modifiers weren't found immediately after queuing them.
  + Fixed local->world root motion conversions when non-yaw rotations are involved.
  + Fixed cases where some movement modes were not respecting the setting for remaining vertical.
  + Fixed bugs where an actor can violate the min/max distance it's supposed to float above walkable floors.
  + Made sure we use BaseVisualComponentTransform to update PrimaryVisualComponent transform in FinalizeFrame so changes to BaseVisualComponentTransform apply to the visual component regardless of whether we're smoothing state or not.
  + Now properly expose Movement Mode in-out references in GenerateMove and SimulationTick to Blueprint.
  + Searching modifiers by handle with an invalid handle will return nullptr rather than active modifiers with invalid handles that haven't been fixed up yet.
  + Now passing along starting velocity in Falling modes if we didn't use any time. This fixes some velocity cancellation that sometimes causes a stutter on landing.
* Cameras:

  + Fixed main camera assets not being usable as Blueprint variables.
  + Fixed crashes and bugs with rewind debugger integration.
  + Improve debug info display with extra data, more filtering options, and a few other things.
  + Fixed single-rig updates missing some of the steps the blend stack does.
  + Fixed static initialization problems that can lead to debug blocks not saving their fields in trace files.
  + No longer freezes camera rigs during stateless evaluations.
  + No longer warns about a camera asset not using any rigs if it's using proxies, and builds any rigs in the proxy table.
  + Fixed a crash when a camera's enter or exit transitions have empty pins.
  + Fixed an incorrect reset-to-default behavior on the camera parameter editor UI.
  + Now prevents infinite recursion when there's a cyclic reference of camera rigs.
  + Fixed gameplay tag transition condition; when a tag query is specified, it should fail if there is no previous/next camera rig.
  + Normalized yaw/pitch for spline orbit node
  + Can now run the target ray-cast node when there's no player controller.
  + Can now build and run camera rigs and shakes with no root node.
  + Now prevent rig prefab nodes referencing their own camera rig.
  + No longer throws asserts or error messages when we have a camera actor without an asset specified on it
  + Fixed activating persistent rigs during director initialization, and having these rigs receive custom parameter overrides.
  + Now validates that exposed camera rig parameters have the correct type for what they're connected to.
  + Fixed possible crash in GPC camera manager when the last evaluation context is removed from the stack.
  + No longer updates dampers and interpolators when the delta-time is zero.
  + Now properly freeze blends (possibly mid-blending) when freezing a camera rig in a blend stack.
  + Fixed simple fixed-time blends not saving/restoring their current time.
  + Fixed a crash when changing the type of a camera rig parameter.
  + No longer shows byte/int types for data parameters.
  + Now resolves camera rig name conflicts when building the property bag for a camera asset.
  + Fixed camera rig parameter nodes not being added to the list of graph objects.
  + Fixed assert when adding an enum data parameter to a camera rig.
  + Fixed broken "inline" evaluation of camera shake prefabs.
  + No longer pre-blends camera variable table entries that are not flagged for it.
  + Fixed the tick group for the camera components.
  + Fixed a crash when running editor builds without an editor.
  + Added missing initialization call for blend nodes in merged camera rigs.
  + The camera reference widget is now disabled if overridden with a rig parameter.
  + Fixed a crash when connecting a camera variable reference to a camera rig parameter.
  + Fixed an issue where rigs could keep running with old data after their asset was rebuilt.
  + Fixed "Home" button in camera rig editor.
  + Deleted references to camera variables when a variable collection is deleted.
  + Fixed a possible crash when running with unbuilt or outdated rigs.
  + Fixed Blueprint breakpoints not working on GET/SET parameter nodes.
  + Fixed shake prefab node not passing shake parameter values over to the visual layer in deferred mode.
  + Fixed SET parameters nodes not setting anything if the parameter wasn't already known in the variable/data tables.
  + Fixed error messages for unexpected situations lerping/overriding variable tables.
  + Fixed variable and context data tables sometimes returning uninitialized memory, and replace assert with one-time warning.
  + No longer uses manual focus distance on the output camera component if the focus distance isn't set.
  + Fixed pin types and colors for some data parameters.
  + Fixed incorrect parameter/pin types on the Blueprint camera node for object and class pointers.
  + Camera modifier rigs added from the player camera manager should now be aware of the player controller.
  + Added fixes for the player camera manager:

    - No longer double-updates Gameplay Camera actors
    - Now run the vanilla (Blueprint-based) camera modifiers ourselves after the camera system.
    - Now sets the transform of the camera manager itself to where the final viewpoint is.
* GAS:

  + Consolidated code that checks whether an AttributeSet's FProperty represents a gameplay attribute, and improved coverage and stability:

    - FGameplayAttribute details customization dropdown will only show attribute set properties that represent GameplayAttributes. Previously it showed all properties.
    - GameplayDebugger will now also display doubles. Doubles as FGameplayAttributes remain supported for legacy reasons.
    - Fixed GameplayDebugger crash when an UAttributeSet had any int32 UPROPERTY().UAttributeSet::InitFromMetaDataTable now only processes property types that can back gameplay attributes.
  + Fixed a crash when debugging gameplay effects with aggregate by source stacks.
  + Fixed an issue where SetTagMapCount didn't call OnTagUpdated like the other tag update functions. This will now be called when Gameplay Cue tags and Loose Tags are added and removed (No change for changing values that don't add or remove the tag).
  + Fixed target data recalculating source tags and attributes when applying Effect Spec.
  + GameInstance pointer for Async Actions is correctly reset after it is un-registered.
* Network Prediction: Changed static initialization of FNetworkPredictionModelDefRegistry's singleton to avoid issues with static initialization happening out of order causing registered Network Prediction model definitions to be skipped/removed. Also, made some minor adjustments to FNetworkPredictionModelDefRegistry::FinalizeTypes to avoid potential ODR issues.
* Fixed an error in ULocalPlayerSaveGame::IsSaveInProgress where it always returned true even if one was not in progress.
* Added an ensure to protect against missing player state crashes during seamless travel.
* Map placed actor Event Dispatcher duplicates:

  + A map placed Blueprint actor's bindings to another map placed actor's multicast delegates (including Event Dispatchers) are now cleaned up when the actor is destroyed and reinstanced.
  + This fixes a bug that bindings to other actors' multicast delegates accumulate when recompiling an actor blueprint. Previously this resulted in event nodes firing multiple times, increasingly when the Blueprint is recompiled.
* Now return the playercontroller if found from the owner.
* Network Prediction: fixed crash in smoothing service that could occur after adding more simulation objects during runtime
* Fixed replication issue canceling Gameplay Abilities when destroying the ASC from the server while abilities are active.
* Fixed Multiply (Compound) modifiers not calculating correctly with stacked GameplayEffects.
* Prevented a crash in APlayerCameraManager when the owning player controller has been GC'ed.
* Input triggers and modifiers will now properly respect the priority of an input mapping context. This fixes a bug where if you had the same input modifier class on an input mapping context of a different priority, it would always use the modifier values of the one which was pushed to the stack first.
* Fixed code that removes ?listen from client URLs to work correctly with # options as well.
* Ensured that the "SlateApp.GetModifierKeys" function will return the correct values when called on platforms using GameInput to process keyboards.
* Fixed OnBlendComplete not being broadcast in Standalone (non-networked) games.
* Find-in-Blueprints: When a BP member variable is a struct, its members' default values are now searched and returned as results. Map keys are not supported yet.
* Chaos Mover: Fixed floating point precision error in ChaosMoverStateMachines's fixed delta time calculation.
* No longer restarts a camera animation blend out when reaching the blend out time if we were already stopping.
* Fixed DefaultToInstanced subobjects breaking on blueprint duplication.

  + Fixed instanced subobjects, including DefaultToInstanced classes and UPROPERTY(Instanced), breaking when a blueprint class with instanced subobjects got duplicated.
  + This fixes the following editor actions which previously resulted in data loss:

    - Duplicating blueprints with user defined instanced subobjects.
    - Duplicating blueprints with GAS attribute set DefaultSubobjects.
* Player Input: Fixed a bug where if you had an input component whose outer was a subobject of the currently controlled pawn, the input component would be processed twice.

  + One example where this could be a common issue is within the "Modular Gameplay Framework". Users would add a UInputComponent to some UActorComponent, and then call "PushInputComponent" on the owning player controller. This would result in the UInputComponent being processed twice.
  + This would happen because in "APlayerController::BuildInputStack" it calls "GetComponents" on the controlled pawn, which would return the UInputComponent which had already been pushed to the controller's input stack, thus adding it twice to the stack for processing.
* Enhanced Input: Do not load platform-specific override data on post load of the platform settings. If you are referencing an object that is in a plugin, this will just fail anyway and does not improve any sort of loading behavior.
* Fixed an incorrect Deleter being used on FGameplayAbilityTargetData when calling FilterTargetData, and exposed FGameplayAbilityTargetDataDeleter for this purpose.

  + Use this deleter when creating an FGameplayAbilityTargetData using FMalloc, such as in UAbilitySystemBlueprintLibrary::FilterTargetData.
  + When creating TSharedPtr to FGameplayAbilityTargetData which was created with FMemory::Malloc, please use the FGameplayAbilityTargetDataDeleter

**Deprecated:**

* Deprecated the "Speech Mappings". These speech mappings were originally added to support Hololens, which is no longer a supported platform and can be removed.
* Removed the deprecated functions on the camera manager, GetCameraCachePOV and GetLastFrameCameraCachePOV.
* GAS: Deprecated StackType to make it private in the future, use new accessors instead.

#### Mass

**New:**

* Added time-slicing with FMassEntityQuery::FExecutionLimiter to limit execution to a set entity count.
* Added a Mass command for grouping entities.
* Mass Debugger:

  + Added "Open In Query Editor" button to all query displays in the debugger.
  + Added handle-based sorting of entities on the Entities tab.
  + Completely overhauled breakpoints with new types, filtering, hit counters, session to session persistence, copy-paste.
  + Added query editor UI with load/save and copy/paste support for authored queries.
  + Added Fragments view tab.
  + Added new "Selected Entity" breakpoint filter to break for whichever entity is selected in the gameplay debugger or debug UI.
* FMassFragmentRequirements and FMassEntityQuery are no longer UStructs, which they were never supposed to be.
* Added observers locking to commands flushing. This change results in batching observers calls, significantly reducing the number of individual observers executions (~20 times in CitySample).
* Added MassQueryExecutor to unify the functions of MassQuery and MassProcessor and create a foundation to remove dependency on UObjects for Mass processing in the future.

  + Simplified Mass data access with templated UE::Mass:FAccessors collection.
* Added a way to fetch base-typed fragment views from Execution context while providing the actual, specific class with a UScriptStruct pointer.
* CFragment concept now checks whether types are std::is\_trivially\_copyable and if not emits errors requiring users to manually mark fragment types that are not trivially copyable.

  + The goal is to educate fragment creators about good practices and point out fragments that might accidentally violate the requirement.
* Deprecated FMassBatchedCommand::Execute as a const function and introduced non-const replacement named `Run`.

  + Unfortunately a new name had to be introduced since the constness of the function is the only thing that's changing.
  + Added a temporary construct to MassCommandBuffer to statically detect commands that still implement the deprecated virtual Execute in an attempt to make it easier for people updating their code to notice the change.
  + The construct will check at compile time all the pushed commands of known types and statically assert if the command type still overrides the deprecated `Execute` function.
* Entity Builder API extension, supporting use of an arbitrary "element" type and having the builder figure out what kind of an element that is and store it appropriately. Additional changes:

  + Fixed FEntityBuilder::AddInternal implementation to not add duplicated instances of a given element type if one is already present.
  + Added creation context to the deferred path, to ensure the fragment values are already set when the observers kick in. This was already done in the synchronous path, so this change addresses the inconsistency
* Added a couple of functions to MassEntityManager, that deal with types passed in as UScriptStruct, and pass the argument to the appropriate function, based on the type (Tag or Fragment).
* Mass Command Buffer API extension:

  + PushUniqueCommand: the function lets callers add a hand-crafted command. Use it to push commands that you don't want to get merged with other commands of the same type.
  + AddTag and RemoveTag: added versions that take an array view of entity handles.
  + DestroyEntities: Added a version with rvalue ref parameter.
* Added FMassFragmentRequirements::AddElementRequirement that can be called at runtime with UScriptStruct.

  + It will add the provided type to Fragment or Tag bitsets, depending on the type represented.
* Added FMassRepresentationParameters::Identical to implement logically-correct FMassRepresentationParameters instances comparison. The operation by design ignores CachedDefaultRepresentationType and CachedRepresentationActorManagement.
* Added a way to ask a MassCommandBuffer about its host thread.
* UMassVisualizationTrait can now be configured to not check mesh descriptions for validity which can be used to procedurally populate trait instances.

**Bug Fix:**

* Fixed inconsistencies between single and multi-threaded deferred command flushing in FMassProcessingPhase::ExecuteTick.
* Modified the occasionally failing ensure condition in UInstancedActorsData::OnInstancedActorDestroyed and provided it with more comments and a message to emit.
* Properly handle shared fragment hash collisions.
* Mass puppet actors now get destroyed immediately when the puppet is destroyed.
* Fixed configuration issues of FMassProcessingContext created in UMassSpawnerSubsystem::DoSpawning for running initializer processors.

  + The original configuration was flushing commands if any have been issued, but did so in a way that forced flushing of all the system's commands accumulated up until that point. That resulted in different behavior in entity spawning depending on whether there were initializers for a given entity available or not.
  + The new configuration results in keeping the behavior consistent, regardless of initializers presence, which is to not flush commands and if any are issued they will be appended to the main buffer when FMassProcessingContext goes out of scope.
* MassGameplay:

  + Fixed a crash when a mass representation actor is destroyed while mass simulation is active.
  + Fixed a teardown crash in MassAgentComponent.
  + Fixed a situational crash in UMassRepresentationSubsystem on world teardown.
* MassAgentComponent changes to update EntityHandle-to-actor mapping in MassActorSubsystem when dealing with a player-owned component.

  + The change fixes an issue with GameplayDebugger's Mass category not being able to display info on the player-owned entity. A tiny change to the category removes the friction when doing that (no longer requiring the transform fragment to display data).
* Fixed an issue in FMassEntityQuery::ParallelForEachEntityChunk stemming from the code not taking into consideration that ParallelForEach's workers can be moved between threads.

  + If that happened and the query was run with `bAllowParallelCommands == true`, then the command buffer would complain about being used outside of the thread of its creation. The fix is updating the thread ID of the command buffer whenever it's picked up.
* Now sorting observer processors to utilize UMassProcessor.ExecutionPriority.
* Fixed FarmTest to not crash on PIE:

  + The existing implementation is crashing since the changes to processor initialization have not been applied there.
  + This issue is limited to the farm-test, due to the custom and legacy way of setting up and running processors.
* Fixed standalone-game IA uses by properly talking to ServerInstancedActorsSpawnerSubsystem, which fixes some IA representation issues.

  + Also, ServerInstancedActorsSpawnerSubsystem has been fixed to `FinishSpawning` actors only once their IAComponent has been configured.
* Marked UMassCapsuleTransformToMassTranslator as "game-thread only" to avoid data races when the observed component is modified in game thread as the data is being accessed by the processor.

#### Networking

**New:**

* Implemented RPC state stomp detection which can detect state buffer writes between quantization and serialization. The cvar to control this is net.Iris.RPC.ServerStompDetectionEnabled which is false by default.
* Support Iris when using NMT\_JoinNoPawn and NMT\_JoinNoPawnSplit.
* Adding an FSocket::ReleaseNativeSocket for use with native socket API's (e.g. asio). Using this new function inside the TraceAnalysis' FDirectSocketStream to support cases where we want multiple connections, not just a single connection (e.g. a multi-server capture).
* Iris

  + Implemented seamless travel support. If seamless travel support is not needed for a project the cvar net.Iris.AlwaysCreateLevelFilteringGroupsForPersistentLevels can be set to false to avoid unnecessary overhead of filtering objects in the persistent level.
  + Optimized polling to only poll objects/properties that are marked dirty.
  + Added some async loading failure debugging cvars:

    - net.Iris.AsyncLoading.FailPackageName Name: fails async loading all packages containing the package name.
    - net.Iris.AsyncLoading.FailNextLoad 1: fails the next async load regardless of the name and resets the cvar.
    - net.Iris.AsyncLoading.FailAllLoads 1: fails all loads until the cvar is set to 0.
  + Gracefully handle reaching the end of the bitstream even if it's unexpected. The behavior is controlled via cvar net.Iris.ReplicationReader.GracefullyHandleReachingEndOfBitstream.
  + Added better logging when handling end of bitstream issues. Reset the read journal when deserializing huge objects.
* Added a NetDriver command for printing out all of the actors registered for replication (generic replication system only).
* NetEmulation:

  + Added netEmulation setting to simulate buffer bloat on game traffic.
  + Set PktBufferBloatInMS for outgoing packets and PktIncomingBufferBloatInMS for incoming packets.

    - Ex: 'netEmulatation.PktBufferBloatInMS 1000' will apply 1sec of buffer bloat on outgoing traffic.
  + netEmulation.BufferBloatCooldownTimeInMS can also be used to set a cooldown period between each buffer bloat occurence.

    - Ex: 'netEmulation.BufferBloatCooldownTimeInMS 2000' means buffer bloat is not applied for 2secs after a buffer flush.
  + Added a "BufferBloat" emulation profile that enables buffer bloat of 400ms (in and out) over an 'average' emulation profile.
* Added metrics to measure the performance and behavior of the multiserver proxy.
* Multithreaded Iris Polling Step:

  + FObjectPoller can now kick off multiple FReplicationPollTasks, each of which processes a subset of the ObjectsConsideredForPolling array.
  + This is set to process cache line sized Chunks in an interleaved pattern so that each task gets a roughly balanced amount of work, and we avoid false sharing the same cache line.
  + Also supports the ForcePoll flow if PushModel is disabled.
  + Added NetBitArray ForAllSetBitsInRange function to facilitate iterating over different parts of the same Array inside each task.
  + FNetTypeStats now supports threaded access through the use of ChildNetStatsContexts that are used during parallel phases and then accumulated into the parent context at the end of a frame.
  + Configuration is done at the ReplicationSystem level so that we can enable it just for GameNetDriver on the Server.
  + We define a flag called bIsInParallelPhase which is true whilst the FReplicationPollTasks are running, and is used to protect against non-thread-safe access during this time.
  + Added capability for Networking Iris Polling phase to be run in parallel. This can be enabled by adding bAllowParallelTasks=true to the ReplicationSystemConfig
* MultiServer:

  + Refactored LaunchMultiServer script. Users can now derive from it to add their own features.
  + The -ProxyGameServers command-line argument can now accept a port range. This helps with launching multiple servers on a single host, so you can just use 127.0.0.1:9001-9025 for 25 servers.
* RemoteObjects: Now reschedules aborted ServerReplicateActor calls rather than retrying them.
* Fixed an issue where UActorChannel::ReplicateActor did not account written bits in one of the paths
* Renamed RepNotifies CSV stat to Generic\_RepNotifies to better distinguish between Actor Channel based replication (generic) and Iris replication.
* Added support for closing child connections in the net driver and closing connections on the multiserver proxy.
* Added mutators to UNetworkMetricsDatabase functionality.

  + Mutators can be added to UNetworkMetricsBaseListener and get a chance to process input metrics every frame. They report an output metric to their owning listener on the listener's reporting interval.
  + Use mutators to aggregate metrics that are set more frequently than a listener's reporting interval. Basic mutators for min, max, and average are provided.
  + Added server-side network metrics for RawPing values across all client connections.
* Added support for actor replication relevancy when using the multiserver proxy.
* The multiserver proxy now shares a single NetGUID cache and objects are cached on the proxy when migrating between servers.

**Bug Fix:**

* Fixed a crash which could occur if an actor channel was removed during replay playback scrubbing.
* Iris:

  + Fixed bug with FastArraySerialzierFragment if using not replicating items.
  + Fixed bug where FGameplayAbilityTargetingLocationInfoNetSerializer would not properly call FreeDynamicState.
  + Fixed bug that could prevent a default subobject from receiving a large RPC.
  + Fix edge case with prioritization causing a crash.
  + Fixed issue where dirty status of new subobjects created from PreUpdate of objects was masked out.
  + Now resets NetBitStreamReader between batches to get correct read journal entries and clear overflow status.
  + ObjectProperty class type is now validated property when serializing object references.
  + Fixed a bug where initial state was not applied when beginplay() was dispatched for world from AGameStateBase::OnRep\_ReplicatedHasBegunPlay.
  + Fixed a bug that allowed adding subobjects to torn off root objects.
  + FScriptInterfaceNetSerializer can now handle blueprint implemented interfaces.
  + The ObjectReplicationBridge's AddDependentObject method will now prevent circular dependencies.
  + Fixed bitstream corruption that could lead to disconnects.
* Can now pass zero size to FNetBitStreamWriter's InitBytes method.
* Network:

  + Added UE\_FAST\_ARRAY\_COMPILE\_LOG\_LEVEL that enables a program to control the compile time verbosity of LogNetFastTArray logs.
  + Since this class is templated the logs in the functions are unique per implemented class so it can grow the amount of the log static strings if they are left compiled-in.
* Fixed issue with FObjectReplicator's CanSkipUpdate with net.PushModelSkipUndirtiedReplication enabled.
* Made a change in UNetDriver::IsLevelInitializedForActor to avoid iterating over net connections if the actor we are evaluating has the correct world, or if the actor it is not a player controller
* NetDriver:

  + Fixed ping updates discarding higher ping values when multiple Acks were received in one packet.
  + For example this caused ping values to stay low during BufferFloat occurrences.
  + Added RawPing metric that tracks the highest ping value received every frame.
  + RawPing will not change if no packets are received or the incoming packets contain no new Acks.
* When using Iris replication, objects that have a spatial filter set at runtime will now always use their correct location for filtering calculations.
* When using Iris replication, actors and subclasses without explicit FilterConfig overrides in ObjectReplicationBridgeConfig will now be filtered based on their relevancy flags like bAlwaysRelevant.

  + Previously these actors were treated as always relevant regardless of their bAlwaysRelevant flag.

**Deprecated:**

* Removed error prone SetConnectionFilter API from UReplicationSystem. Use exclusion groups instead.
* Deleted UNopNetObjectFilter. It's been superseded by UAlwaysRelevantNetObjectFilter which has identical functionality.
* Deprecated GetSubobjectsWithStableNamesForNetworking function

### Level Design and Art Tools

#### Geometry Core

**New:**

* We now use the fast cluster simplifier for convex decomposition's pre-pass simplifier (since the main use case is to make the decomposition faster).
* Geometry Core: Added morph target attribute as a core dynamic mesh vertex attribute.
* Added path intersection & difference.
* Added a ReparameterizedCloserToWorldFrame to the GeometryCore TOrientedBox3 class.
* Added a CreatePerVertex method to dynamic mesh overlays, as a faster alternative to the CreateFromPredicate() method in the per-vertex case.
* Added a vertex -> single triangle method to dynamic mesh, as a faster/more-convenient path (vs e.g. using a vertex->triangles iterator to get a single element).
* FDynamicMesh3 queries now optionally take an inline-allocated array for local vertex-neighborhood mesh queries.
* Added optional scale factor to DynamicMeshUVEditor::ScaleUVAreaTo3DArea utility function.
* Added option for geometrycore's MeshBoolean to report the source mesh of each result triangle.
* Added option for the Mesh Boolean to take a custom 'inside mesh' function, per mesh.
* [GeometryCore] Delaunay 2D iterative update support.
* Added a version of Expand() to FAxisAlignedBox3 and FAxisAlignedBox2 that takes a vector.
* Segment Tree: - add option to build the tree with an array of segments - make use of the filter function that's passed in as an option.

**Bug Fix:**

* We now reset the UsedCount on a moved-from RefCountVector, so it is left in a valid state (and e.g. a mesh will not fail CheckValidity after being moved from).
* Made the implicit morphology generator not hit an ensure() when passed an empty mesh (and still return an empty result).
* Fixed the dynamic mesh color transfer method handling of non-compact meshes when biasing element positions, and simplified the lerp-toward-centroid logic used.
* Fixed static mesh's LOD -> dynamic mesh conversion handling of non-compact polygon group IDs

  + We need to compact these IDs so that they correspond to static mesh section indices, which all our tools and geometry script processing expect.
* Improved performance of MeshRegionGraph operations:

  + Region merging transfers known neighbor information, rather than recomputing it.
  + Less redundant validation on internal operations.
  + Less redundant array searching when building neighbors.
* Added api exports to the OBJMeshUtil methods so they can be called from other modules.
* Made MeshConvexHull's grid sampler exit when mesh bounds are empty, to avoid ensures on grid w/ zero cell size.
* Fixed dynamic mesh CompactInPlace creating a triple-sized TriangleEdges array + add coverage for this case in CheckValidity, and guard against this kind of error breaking AppendWithOffsets.
* We now do not leave unused vertices in the cluster simplifier mesh result mesh.
* Fixed incorrect transforms on GeometryCollectionToDynamicMesh converter, and added more comments to document the expected coordinate spaces for these meshes.
* Fixed crash in implicit morphology offset operation due to offset grid dimensions overflowing int32.
* Fixed a possible crash in algorithms that use the sparse solver wrapper, by properly handling failed factorizations.

#### Geometry Script

**New:**

* Added various oriented box functions to geometry script, to create and query / test intersections and convert to meshes.
* Added an OBB containment function to geometry script (matching what simple collision fitting does, but exposing the found oriented box directly).
* Improved geometry script's CopyCollisionMeshesFromObject support for complex collision.

  + It now supports any type that implements the IInterface\_CollisionDataProvider interface, and specifically should now work better with Skeletal Mesh Components and Spline Mesh Components.
* Added a 'select occluded from outside view' jacketing method to geometry script, to have more controllable occlusion operations (e.g. from specific directions, for specific material IDs/parts of mesh, w/ transparent tris).

  + Also, cleaned up the detect exterior visibility function logic to support the new options and be a bit faster / more robust.
* Added target edge length QEM and cluster-based simplification methods in geometry script.
* We now more consistently use the term "Connected Islands" instead of "Components" when referring to connected pieces of a mesh in Geometry Script nodes.
* Filled out geometry script list conversion extract/set methods for the various list types: Scalar, UV, Vector and Color.
* FOrientedBox is now exposed to Blueprint.
* The 'debug' pins in geometry script are now hidden in the Blueprint graph
* Geometry script now supports standard MikkT tangents in the Compute Tangents node, on platforms where the MikkT library has been compiled (i.e., win/mac/linux).

**Bug Fix:**

* Added Vertex and Triangle ID validation to geometry script Mesh Query methods so users do not crash on querying an invalid element ID.
* Made dynamic mesh pools safer to use from a non-game thread.
* Fixed the output param display name for GetMaxMaterialID.
* In geometry script asset creation methods, we now test that the paths for new assets are valid before attempting to use them.
* Fixed a bug with "AppendXWithSimpleCollision" geometry script methods where repeated calls of a script could accumulate extra copies of the collision shape, because blueprint re-uses output reference objects across script invocations.
* Removed requirement that patch unwrap mesh be non-compact.
* Fixed issue where Geometry Script would maximally simplify a mesh if "Simplify to Tolerance" was run with a tolerance of 0.
* Deprecated incorrect geometry script perlin noise node, and added a corrected v2.

#### Landscape

**New:**

* No longer visualizes disabled landscape patches.
* Now sorts landscapes alphabetically when multiple landscape actors are editable in landscape mode.
* Changed the landscape Collapse Layer tool to use selective render weightmaps code instead of intermediate render code.

  + Added weightmap support for edit layer selective renders.
* Added a GrassMap RenderEveryFrame command, to debug grass map runtime generation.
* Changed landscape tools with the "Combined Layers Operation" feature to use new selective layer render code.

  + Stops using old "intermediate render" code and avoids polluting the persistent texture data with intermediate results. The new version is faster and safer.
* Moved the Landscape feature level warning (for shader modes < SM5) from a blocking notification to a simple console log.
* Landscape optimization for the editor:

  + No longer inspects materials for finding mobile layer names when generating mobile weightmap allocations while there's no weightmap allocations in a given landscape component in the first place.
* Performance optimization when undoing landscape edits.
* Added a transient landscape property to track the last selected edit layer index. Edit layer selection state is persistent when toggling between editor modes.
* Removed the ability to place Landscape Blueprint brushes from the Place Actors panel.
* Added all landscape brushes from the Landscape Manage - Blueprint Brush tool.
* Enabled dynamic Landscape Spline control point billboard size and offset in editor.

  + To change the offset and size, configure Spline Icon World ZOffset and Spline Icon Scale under the Landscape Project settings.
  + To maintain legacy spline behavior, set CVarLandscapeSplineEnableFixedSpriteIcons=True.
* Removed the Landscape Spline Deform to Landscape buttons used to update spline data for non-edit layer landscapes. With edit layer landscapes, Landscape splines automatically affect the data when a Spline Edit Layer is added.
* Added API exposure for all public BlueprintCallable Landscape Patch functions.
* Exposed landscape component's GetGrassTypes to Blueprint.
* Added generic World Partition Landscape Builder Commandlet. Builds all landscape grass maps, physical materials, and nanite components.
* Improved landscape.DumpLODs command:

  + Now it only displays the landscape LOD information by default and -detailed needs to be used to get the verbose mip-to-mip delta information.
* Added an option to align landscape grass instances with the precise triangle normal when using jittered grid mode.

  + Also fixed an issue with the triangle normal calculation.
* Added API exposure to virtual functions on landscape patch plugin UCLASSes so that they can be inherited from in other modules.
* Remove redundant and unsafe non-blocking landscape nanite build from PreSave. No longer builds Nanite at all on auto-saves.
* Added an option to Add Unassigned Blueprint Brushes in the Landscape Edit layer context menu. If a Blueprint brush does not have an assigned edit layer, the right-click context menu will include an option for re-assignment
* Added a DeleteActors helper in order to let the editor's delete actors dialog run when possible but also to let actors be safely deleted without using the UI in other cases.
* Added Landscape Edit Layer Context Menu customization system.

  + Added the ability to easily extend right-click context menu actions for custom edit layer classes.
* Moved LandscapePatch plugin out of Experimental.
* UX improvements:

  + Updated icons to landscape target layers display order methods.
  + Added sort type (ascending/descending) for this.
  + The sort/filter options have moved next to filter box within the Layers property (since they affect only the layers that are visible, these buttons should not be present when the property is collapsed).
  + Added a number of target layers in the Layers property header, in order to be similar to standard arrays and also the edit layers property above.
* Added Collapse All Edit Layers action to the Edit Layer context menu.

  + Removes all edit layers and flattens the current data into the default edit layer.
* Updated default spline edit layer selection behavior:

  + Selecting the Splines Edit Layer no longer auto-activates the Splines tool.
  + Double-Click on the Splines layer, or use the right-click context menu option, to toggle between the Splines Tool and last active tool.

**Bug Fix:**

* Fixed mobile landscape weightmaps not being taken into account by streaming.
* Fixed a crash when auto-filling target layers from material.
* Fixed height/weight alpha precision loss when merging landscape.
* Fixed grid-alignment warnings when creating a landscape with more than one region worth of components.
* Added refined Water Body underwater detection to avoid applying post-processing when the camera is underneath or outside the bounds of the collision volume
* No longer calls UpdateResource when changing texture LOD settings for render targets. This fixes the water brush breaking landscape after switching between desktop mobile preview mode and desktop renderer.
* Fixed landscape legacy weight blending potentially leaving ghost weightmaps on large landscapes.
* Turned assert about landscape physical material tasks failing to complete on save into an error, since that is something that can happen if the material fails to compile.
* Fixed a crash that happened when trying to clear a Landscape Paint Target Layer that was already empty.
* Fixed a crash when a Landscape Blueprint brush was deleted and then restored via Undo.
* Removed spurious assert when the landscape material references a texture named "Heightmap" (implicit name for heightmaps in landscape).
* Fixed determinism issue when updating landscapes with conflicts on the border of landscape components that would lead to landscape proxies getting dirty in an inconsistent way.
* Fixed an issue with World-Partition Landscape Proxy Nanite Materials not updating after using Undo/Redo with the Landscape Paint Tool.
* Fixed invalidations of landscape physical material during painting.

  + The last few frames of a paint stroke could be lost because the invalidations were ignored while a physical material task was still pending.
* Fixed several issues with ReinitializeHeight/Weights in landscape patches.
* Fixed crash with multiple patches. The render command recorder was not stopped at the right moment: both Render and Blend operations must respect the render mode (Immediate or Recorded), which could be broken in case the renderer was grouped with another one earlier.
* Fixed landscape that was not updated after having reinitialization had been executed.
* Fixed a crash when the same patch is rendered in several batches. The boolean bReinitializeHeightOnNextRender does not support this and that supposes that during reinitialization, the patch is rendered in a single batch. The fix artificially increases the batch size to the entire landscape, which is wasteful, but the best we can do until the reinitialization is replaced by a proper landscape edit layer partial merge.
* Fixed landscape batched merge not handling multiple weight patches (i.e. multiple target layers) being rendered on the same patch component (the render targets would cycle in between each, leading to invalid blending).
* Fixed landscape patches' input area (which was the size of the patch), that would lead to needlessly large batches.
* Fixed potential determinism issue with landscape patches that could theoretically render before their referenced textures are fully streamed in.
* Handle null landscape patch weight entries in the couple of places where it was not.
* Fixed invalid checks in landscape batched merge.
* Stop over-invalidating on empty landscape components. Change to invalidating only components that added or removed weightmap allocations.
* Fixed PCG refresh on undo/redo landscape painting.
* Moved creation of landscape nanite's UStaticMesh out to the game thread to remove danger of threading issues.
* Fixed improper blend of landscape edit layers with custom height/weight flags.
* Avoided a crash if saving when FLandscapeTextureStreamingManager is not available.
* Fixed a bad ensure condition when trying to cache data from an empty area in the landscape smooth/flatten/erosion tools.
* Fixed a crash with the Landscape Copy Tool when attempting to copy data from an invalid or deleted landscape.
* Fix deleted landscape spline points/segments coming back after duplicating the spline.
* Fixed a crash occurring when saving level instances that include World-Partition Landscapes.
* Fixed ctrl+alt+right click drag increasing/decreasing the landscape brush continuously even when the mouse was still.
* Fixed mobile landscape data hash being zeroed when entering PIE. That was leading to all landscape mobile data being rebuilt when entering PIE while in mobile preview mode.
* Fixed a landscape flatten tool conflict with undo.
* Fixed landscape flatten tool behavior at the edges of geometry.
* Fixed landscape painting errors when toggling "invert" during a brush stroke.
* Fixed an issue with the Landscape Resize tool clearing all heightmap/weightmap data for edit-layer based landscapes.
* Fixed an issue with Water Bodies automatically generating invalid collision boxes in the Blueprint editor when changing the Wave Source property.
* Prevented a crash when redoing an undo of a Water Zone actor deletion.
* Fixed an issue with the Landscape Resize tool using the wrong Y position offset while expanding the landscape.
* Fixed the handling of changing transforms when building landscape groups.
* Fixed additive blend mode for landscape texture patches.
* Fixed various landscape+water new cases where it was assumed that GetWorld() returns a valid world while it's not the case when a world is deleted from the content browser.
* Improved the Landscape Import/Export Exposed user experience by exposing the Landscape Gizmo location property to the Landscape details panel.
* Fixed a crash updating landscape edge snapshots when heightmaps are not readable.
* Fix landscape edit layers merge on Vulkan SM6.
* Fixed a crash when renaming a Landscape Paint Target Layer to an invalid name. Target Layer names must be unique non-empty names.
* Keep landscape patches in sync with their host landscape by upgrading them from the soft-dirty package list to regular dirty status when the landscape makes that same change.
* Enabled landscape grass culling when running MRQ.

  + Previously we would pass an array of no camera to RegenerateGrass, which prevents all landscape grass from being distance-culled.
  + Instead, we now pass nothing, which leads landscape to use the streaming manager to get the current "views", one of which is the captured camera (the other, the editor).
  + This is better handled in the new movie render graph but at least this solves a performance issue in grass-heavy scenes. The user can now override the grass cull distance (as well as grass density) via Game Overrides settings.
  + Default = override + cull distance multiplier of 50, to have (mostly) backwards compatibility with the previous MRQ captures (which prevented all grass culling) The default for grass density override is false, though, also for backwards compatibility reasons.
  + Note that the new movie render graph doesn't have these settings since it doesn't have them for ViewDistanceScale, ShadowDistanceScale, etc. so we figured it didn't need those grass settings either.
  + Also added a CVar (grass.VisualLog.ShowCameraLocation) to show the camera locations used by landscape grass in the visual logger.
* Now displays an error message instead of crashing when failing to import an image file to a landscape layer.
* Avoided a crash on opening a scene containing the legacy LandscapePatchManager when the scene was already at the max number of edit layers. Ignore the soft limit when creating the new dedicated patch layer.
* Fixed OOBB->AABB computation in landscape batched merge, which was leading to bad blend groups for landscape patches.
* Fixed an issue with landscape brushes that would sometimes modify height/weight data on the border with unloaded tiles.
* Avoided a crash when opening a map with a disconnected landscape patch manager, when the editor isn't ready to provide the current selection set.
* Fix for Nanite landscape possibly generating invalid Nanite mesh streaming data on cook.
* Added an option for landscape Blueprint brushes to tell if they require power-of-2 render targets to operate. For backwards compatibility reasons, it's set to true by default, although it's not the best option. This ensures that the water brush behaves precisely how it used to before UE 5.6
* Fixed the water brush on Vulkan SM5.
* Fixed an issue where Landscapes only generate Nanite for the first 64 components of any given landscape proxy.
* Fix missing landscape spline meshes after undo of merger of two splines.
* Now hides the landscape selector when the New tool in the Manage panel is active.
* Fixed a rare crash in the landscape texture streaming manager when landscape textures are GCed while the landscape is still active.
* Fixed missing updates to landscape physical material when using a material instance.
* Fixed a crash using Undo operation with a Landscape Patch and Patch Edit Layer.
* Landscape add component tool fixes:

  + Now properly generates extrapolated height data on each persistent edit layer, so that there's continuity on the corners on each of them.
  + No longer generates collisions on component creation because at this point, the height data is set to all zeroes (i.e. the minimum height, not the median, default height value) and doesn't correspond to what comes out of the the subsequent edit layers merge, whose readback would generate an identical heightmap hash, and would therefore not re-generate collisions. Delaying collision generation until the merge fixes this, since that's the first time the collision values would be valid anyway.
  + Now prevents existing neighboring components from being dirtied when adding a new component (previously they would get dirty by the simple act of caching/interpolating their height data).
  + Automatically apply splines after component creation, so that new components are immediately affected by the splines that overlap with them.
  + Improved visualizer for the component about to be added.
* Prevent landscape edge fixup from running on world composition maps, where heightmap sharing is still possible.
* Fixed all logs involving landscape LandcapeGroupKey and LODGroupKey.
* Fixed ensure loading old landscape data with landscape.StripLayerMipsOnLoad = false.
* Fixed a crash occurring after exiting a level instance with the Landscape Editor - Landscape Copy tool active.

**Deprecated:**

* Deprecated legacy non-edit layer landscapes:

  + Removed all editor tooling related to non-edit layer landscapes (e.g. Landscape Retopologize Tool/XY Offset data).
  + Disabled the creation of non-edit layer landscapes and the ability to toggle between edit layers and non-edit layer landscapes.
  + When non-edit layer landscapes are loaded, an automatic conversion to an edit layer based landscape occurs. During this process, all proxies copy the existing non-edit layer data to a new default edit layer. Any existing Retopologize data is removed and the proxy is flagged as "soft dirty" with an editor viewport warning.
* Removed global and local merge code and deprecated anything that was only available for this.

  + Since the console variable "landscape.EditLayersLocalMerge.Enable" is deprecated now, a new console command was added, to trigger a landscape layer full update (landscape.ForceLayersFullUpdate) :

    - With no argument: Updates all landscapes.
    - With arguments: Updates all landscapes whose display name (partially) matches the argument (e.g. with 3 landscapes named Landscape\_0 Landscape\_1 and Landscape\_2, "landscape.ForceLayersFullUpdate \_0 \_1" will trigger an update on the first 2 only)
* Changed landscape edit layers merge API from experimental to official.
* Removed landscape's "intermediate render" code path.

#### Modeling Tools

**New:**

* Added support for the tangents tool to choose the reference UV layer to use when computing tangents.
* Added BrushValue property to the AttributePaintTool to allow users to specify the target value that is painted down rather than always accumulating to 1.0f.
* Added symmetry support to the Paint Vertex tool.
* The target requirements for the Inspect tool have been relaxed to support DynamicMeshProviders rather than MeshDescriptionProviders.
* Modify UBoundarySelectionMechanic to be able to operate on either closed loops (current behavior) or open spans (new optional behavior).
* Lattice Deformer Tool:

  + Modified the FFDLattice to optionally accept an oriented bounding box rather than computing one from the input mesh. This means the lattice can operate on just a portion of the mesh. Lattice computations are now all done in local space.
  + Added an ILatticeStateStorage interface, which enables the interactive LatticeDeformerTool to store its state in when the tool ends.
* Added support for a HitBackfaces option to the MeshAttributePaintTool.
* The attribute paint tool now has the option to use a more-shaded material.
* Added an option to the Mirror tool to averaging normals along the weld.

**Bug Fix:**

* Fixed a crash on attempting to split meshes w/ invalid material IDs.
* Fixed an issue where the AttributePaintTool's stamps would be skewed for meshes with non-uniform scale.
* Fixed where modeling tools could incorrectly change material ID assignments due to the static mesh tool target 'IMeshDescriptionCommitter' interface not finding the right material ID mapping method.

  + The same function is also on the Provider, so needed to be pulled to the top level for both interfaces to find the method.
* Made vertex sculpt tool skip render decomp step if the sculpt mesh has no triangles (fixing ensure when tool is run on an empty mesh).
* Fixed a crash in the subdivide tool. We were passing in the wrong vertex count to OpenSubdiv.
* Fixed a potential crash when enabling UVLayoutPreview.
* Fixed a warning about realtime mode erroneously appearing in modeling and scriptable tools modes when the editor doesn't have focus.
* Fixed a potential crash in DisplaceMeshTool for meshes with invalid topology.
* Fixed a GC crash with mesh element selection's usage of PreviewGeometry.
* Fixed support of the 'join method' for closed curves in the Mesh Splines tool (previously always used 'square' joins).
* Fixed a crash on starting modeling mode w/ an actor selected that has null components attached.
* Fixed a crash when swapping from Modeling Mode to Animation Mode with Motion Trails active.
* Fixed a potential crash in the ISM Editor tool.
* Fixed a potential nullptr dereference crash in OnActiveViewportChanged for StylusHandling.
* Fixed the OutputType properties' display name and tooltip to SourceType in the BakeVertex tool to better reflect the function of those properties.
* Fixed an issue where tools in Modeling Mode and Scriptable Tools Mode would not tick if the viewport did not receive focus yet during the editor session.
* Fix for crash in Extrude Path tool when creating a totally straight polyline.
* Fixed a rare crash when hovering over Mesh Element Selection before viewport is focused.
* Fixed Mesh Splines tool handling of duplicate start/end points generated on looping splines, which could previously cause incorrect triangulations.
* Lattice Deformer Op: Fixed a check that fires when operating on non-compact meshes.
* Fixed an issue where the Union tool only transferred UV Channel 0 in the result mesh.
* Fixed a potential crash in TDynamicVector::TruncateBlocks for an empty vector.
* Added a workaround to prevent a crash in UVAtlas.
* Normal seams on dynamic meshes are now automatically hard edges when converted to mesh description, which can better preserve sharp features when the dynamic mesh is used for editing a static mesh or skeletal mesh asset.
* Reduced confusion during displace tool computations by adding a slight delay to the appearance of the 'in progress' material.
* Addressed a bug which displayed random gizmo orientation in local space in the PolyEdit tool.
* Fixed an error in AddSingleClickBehavior and AddDoubleClickBehavior function tooltip.
* Fixed the StaticMeshSelector only working on exactly StaticMeshComponents.

#### Procedural

**New:**

* Added "SetWorldObject" on the PCG Data Exporter for Blueprints.

  + Objects can't be cast to World in Blueprints, and when doing an utility widget, Get Selected Assets returns an array of objects.
  + Does the cast internally, returns false if the cast fails.
* Added support for skeletal meshes in BoundsFromMesh and PointFromMesh.

  + Deprecate StaticMesh property to Mesh property in PointFromMesh, with override alias
* Added a new "Extract Attribute" node to extract any attribute from any data and domain.

  + Factorized code for Get Attribute From Point Index.
  + Get Attribute From Point Index now works with data domains too.
* Added the Polygon2D data type, that represents a 2d polygon (e.g. on a plane), with an additional transform. Has some polygon specific metadata properties on both the data domain and the vertex domains.
* Added Python Interop Plugin and Execute Python Script Node.
* Stand up the Break Debugger debug feature for GPU nodes, and make the breakpoint conditional on inspection so that it is usable in partitioned/higen use cases.
* Fixed multiple performance bugs where GPU-resident data is unnecessarily read back when passing through Change Grid Size nodes.
* Added toggle to GPU nodes to trigger render captures for debugging (editor only).
* Added GPU processor node for Attribute Sets.
* Fixed runtime generation bug where changing Partition Grid Size setting on PCGWorldActor resulted in generated actors being leaked into the level.
* Added re-nameable categories for organization in Graph Parameters + Includes Drag and Drop.
* Improved priority calculation in distance and direction runtime generation policy to behave more uniformly across grid sizes and to be easier to tweak.

  + Note: May require re-tweaking if non-default weights were in use.
* Added Generate Landscape Textures node that can generate a height map as well as grass maps from the landscape. This path does not rely on virtual textures, and is significantly more efficient than the CPU path.
* Added LLM tags for tracking memory allocations.
* Added a get segment node that allows the user to retrieve a segment from a polygon 2d, spline or point data, in the form of two points or a spline containing a single segment. Support negative indices (-1 being the last segment) in all cases and hole support for polygons.
* Added 'Clip Paths' node to cut paths (points or splines) with clipping polygons. Supports either difference or intersection.
* Add new property for data that supports elements: @Data.$NumElements.

  + Useful to combine with Filter Data by Attribute.
  + Added the concept of read-only for properties in the Selector menu to not show for output.
  + Applied this concept to Polygon2D properties.
* Added support for property remap when converting back and forth between Attribute Set and Points

  + Saves adding "Copy Attribute" nodes to do the conversions.
* Added option to disable default input creation for top-level graphs. Will become default eventually.
* Improvements on Boolean and Bitwise op.

  + Boolean op now supports arithmetic types as input, still produces a bool as output.
  + Added operators NAND, NOR, XNOR, IMPLY, NIMPLY.
  + Added ShiftLeft/Right for Bitwise.
* Added "AddModulo" operation in maths node.

  + Do operation (A + B) % C .
  + Useful to get the ($Index + 1) % NumPoints.
* Added comma-separated tag list (override) to create target actor node.
* Added polygon offset functionality (offset positive or negative, open and close holes).
* Added polygon operations (intersection, difference, union, inner intersection, exclusive or, cut polygon with paths).
* Added GPU implementation of Transform Points.
* Added change detection to runtime generation state to throttle scans over grid cells, saving per-frame Game Thread cost.
* Added 'Split Spline' node to split splines based on a few criteria (key, distance, alpha) or on a predicate on control points.
* Add `IsBuilder` to Get Execution Context node.

  + Needed to know which component the builder was scheduling.
  + Added that information to the PCG Editor Module, which can be queried through IPCGEditorModule.
  + Add helper function to get the result from the IPCGEditorModule.
* Added support for attribute curve remap.

  + Added a new mode in the existing attribute remap node.
  + Added an alias for curve remap.
  + Also exposed ExternalCurve for the spline sampler (with the new PCG\_OverridableChildProperties).
* Added a 'Spline Intersection' node that computes intersections between splines (in 3d).
* Added a debug feature that repeatedly dispatches the compute graph to enable profiling, compiled out by default (PCG\_GPU\_KERNEL\_PROFILING).
* Added String Contains and Matches nodes and .Length extractor + Extractor:

  + .Length - Length of the string
  + Contains - Whether string A contains substring B
  + Matches - Whether string A matches string B exactly
* Added Cvar pcg.GPU.FuzzMemory which initializes GPU buffers to random values during execution to help catch uninitialized data bugs and other undefined or unreliable behaviour.
* Added the ability to retrieve the ray hit material with GetMaterialFromCollisionFaceIndex, instead of needing to specify a material index.
* StructUtils: Added new features to the Property Bag Details View Child Row Widget:

  + Customizable via the EPropertyBagChildRowFeatures enum (set via metadata specifier).
  + New STypeSelector widget (wrapper around SPinTypeSelector) for type selection.
  + New Access Specifier button.
  + New drop down menu.
* Added 'Get Asset List' node to get assets from a folder or from a collection. Can extract asset classes and generated classes when these are blueprints too.
* Anim - SkinnedMesh: Exposed SkinnedAsset and TransformProvider on FSoftSkinnedMeshComponentDescriptor.

  + To have parity with the non-soft version.
  + To be used for the Instanced Skinned Mesh Spawner in PCG.
* Nanite Assemblies: Initial prototype of Nanite Assemblies builder to support creating Static Meshes.

  + Interop plugin, as this is still very experimental.
* Added specific graph cache enabled and budget CVars for editor worlds vs game worlds.
* Can now override nested properties in the Static/Skinned Mesh Spawner.

**Bug Fix:**

* Fixed multiple cook warnings arising from GPU node kernels.
* Fixed bugs with CreateGrid2D and CreateGrid3D Custom HLSL helper functions where the NumRows/NumCols arguments were not used correctly.
* Fixed Filter Elements by Index node's indexing issue.
* Now supports Attribute Rename for Selectors and Data domain.
* Improvements to Spline Mesh spawning.

  + Component class is now respected when spawning the spline mesh.
  + Added override on the component itself, if users have special fields they want to fill.
* Fixed an outstanding issue in package build where the Switch and MultiSelect nodes can fail if the DisplayName is different from the real name for an EnumValue.

  + GetDisplayName won't return the display name in package build but the real name.
  + Since we use the Display name for naming the pins, we need to keep a mapping.
* Fixed Create Points Sphere crash from divide-by-zero when graph params are used to set degrees to 0.
* Fix bool attribute in Write to Niagara Data Channel.

  + Writing bool values was crashing.
* Fixed bug causing Inline Constant not to respect required pin.
* Fixed Per data CRC caching issue when there are N:N mappings, which was the case in some configurations of the Match & Set node and the Distance node.
* Added support to call Pre/PostEditChange on objects on ApplyOnObjects.

  + When overriding objects with ApplyOnObject node, we call Pre/Post Edit change to have any pre/post processing to do after a change.
* Fixed an outstanding bug in match and set attributes for attribute sets in keep unmatched mode.

  + SetAttributes metadata entry keys arguments were in the wrong order.
* Can now drag and drop in the graph any asset that is a subclass to UPCGBlueprintElement.
* Fixed the RemapMaterial not working if the target dynamic mesh didn't have any material.

  + This was breaking appending a mesh with materials to an empty dynamic mesh, for example.
* Fixed erroneous readbacks and re-uploads of arrays of GPU data items that are not placed first in the compute graph's input data collection.

#### Texturing Tools

**New:**

* Improvements to UCurveLinearColorAtlas.

  + A bug was fixed which caused nearly black negative values to become white.
  + TextureHeight of Atlas is now automatically set to the number of curves.
  + The default width of new atlases is now 64 instead of 256.
  + Interactive updates are now much faster.
  + The UV scale for sampling atlases is now fixed so that the U range of [0,1] goes from the first to last pixel center. Old atlases will automatically be updated for these changes.
* Added Virtual Texture feedback and warmup support to TextureGraph material rendering nodes.

  + Virtual texture samples will now stream to the correct mip level before the final render.
  + Added a new console variable to control the warmup length: "TG.VirtualTexture.WarmupFrames".

#### UV Editor

**Bug Fix:**

* Fixed localization issue for the "Advanced Transform" category label.
* Fixed UVEditor launch conditions to support BP actors with mesh components.Fixed an issue where the RMB context menu would not display the UV Editor option for actors with any invalid components.

#### World Building

**New:**

* Added a Save Texture to Asset node (editor only).
* Added a world partition function to insert a new runtime cell transformer.
* HLOD:

  + Support Spline Mesh Components in Approximate Mesh HLOD.
  + Added world partition validation to detect actors having a HLOD Layer which doesn't support that actor class. Rules can be specified using a config file and violations trigger a warning.
* Standalone HLOD: Added AWorldPartitionHLODOnlyLevelInstance Actor to allow users to place Standalone HLODs in the world without having to add actual Level Instance to the world

  + After adding the actor to the world users can select the level for which Standalone HLODs should be loaded.
  + The actual level is neither loaded nor cooked. It's only used by the Standalone HLOD Subsystem to pull in the corresponding Standalone HLOD levels.
* Add overridable attribute support to CustomHLSL node
* Custom HLOD support:

  + Added WorldPartitionCustomHLODActor, an actor you can place in the world to provide a custom HLOD representation (using static mesh component).
  + Added a new HLOD Layer type: "Custom HLOD Actor".
  + Custom HLOD actors assigned to "Custom HLOD Actor" layer are injected as-is into the HLOD runtime partition.
  + The "Custom HLOD Actor" layer can specify a parent layer. In that case custom HLOD actors are also used to generate parent layer's HLOD representation.
  + Custom HLOD actors can also be assigned to other (non-Custom) HLOD Layers. In that case they are used only during HLOD generation and are not pulled into the HLOD partition themselves.
  + Adds a new LinkedLayer property to UHLODLayer, visible only when LayerType is set to Custom HLOD Actor
  + LinkedLayer is used to control the visibility of Custom HLOD Actors. They become visible when actors from the LinkedLayer are unloaded.
  + If LinkedLayer is not specified, Main Partition is used to control the visibility.
* Added a SceneCapture node.
* Added GPU implementation for CullPointsOutsideActorBounds.
* Now supports overridable attributes on GPU nodes.
* Added a world partition function to check if runtime cell transformers are installed.
* Cell Transformer: Improved handling of components that can be ignored.
* FastGeo: Moved FastGeoContainer PSO Precaching from PostLoad (GameThread) to be asynchronous.
* Added grid streaming dependency mode to scheduling policy
* Move PCG GPU from Experimental to Beta.

**Bug Fix:**

* Standalone HLOD:

  + Fixed a crash when adding a standalone LI with standalone HLOD to a non-WP world.
  + Made sure that Standalone HLOD Actors are injected into appropriate containers during streaming generation.
* Fixed attached spatially loaded actors not being GCed when AttachParent exists.
* EDL: Fixed handling of EDL injection of client-only cells in cases when it happens after BeginPlay Removes irrelevant cells from cells lists during the injection.
* Foliage Editor Subsystem: OnActorMoved optimization to avoid expensive TActorIterator operations when no work is done inside the TActorIterator loop.
* HLOD: Fixed distributed HLOD builds running on non-WP worlds not doing any work.
* WPBuilderCommandlet: Fixed logging when processing additional maps.
* Standalone HLOD: Fixed logic that generates the list of Standalone HLOD levels returned by ShouldProcessAdditionalWorlds, to correctly handle cases where the number of HLOD Setups differs from the maximum HLOD hierarchy depth.
* FastGeo: Fixed a crash on mac caused by TArray relocation of FFastGeoPrimitiveComponent which contains a FRWLock.
* [Cell Transformer] Replaced references to objects that could be recreated during RerunConstructionScripts triggered from ApplyRuntimeCellsTransformerStack in Standalone Editor.
* Fixed a crash while level editing. Deleting an actor inside a level instance then pressing save in the bottom of the level viewport would crash in some situations.

### Media

#### Media Viewer (Beta)

**New:**

* Extra keybinds for videos:

  + Fixed spam of updates when offset / scale was not changing.
  + Exposed delegates to the public API so it can be used in the image viewer overlay.
* Transform lock now also duplicates media playback controls between players.
* New dragging options:

  + Revamped dragging system a little to support more zoom types.
  + Added alt+rmb to zoom (in addition to scroll wheel).
  + Added alt+mmb for panning (in addition to left click).
* Improved level editor viewport robustness:

  + Made sure all settings have default values.
  + Moved level viewport render to end of RT thread event.
  + Added cross-thread robustness to the pixel color system.
* Media track section:

  + Added a media track section that lists tracks in sequencer that have a media texture.
  + Added the refresh dynamic group button.
* Images now support yaw rotation.
* Added a clear history button.
* Added Snapshot category.

**Bug Fix:**

* Fixed controls to properly display when playing in reverse.

  + Also added keybind info to tooltip buttons.
* Media Viewer / Media Player Editor:

  + Added scrub event to IMediaPlayerSlider.
  + Integrated scrub event to allow dual scrubbing.
  + Fixed bug in file drag/drop for media viewer not allowing comparisons to current image.
* Media Stream: Fixed for packaged games.
* Fixed crash relating to viewport.
* Added texture size constraints to render calls.
* Fixed struct initial values.
* Fixed a crash with invalid library thumbnail.
* Fixed changing splitter location in single image mode.
* Media Stream:

  + Corrected the "Add Track" button for Media Sources.

    - Will now always display the button, but disable it, rather than hide it, when it is not available.
    - Added tooltip to the button explaining what it does and when it is usable.
    - It is now disabled if the Media Stream's world is not the level level sequence's world.
  + Fixed relevancy issue for Sequencer.
  + Fixed Sequencer binding issues.
* When locked scrubbing, the videos not being directly scrubbed is paused.
* Invalid assets are removed from history when the tab is opened.
* When in dual view and without an A image, the slider position now works correctly.
* Fixed pixel sampling for compressed images - All pixel samples now work via a render target.
* Fixed an issue with A-image not being displayed behind B-image when the slider was set to 0%.
* Right click asset fix: There's now a maximum parent check for material instances
* Fixed crash when 2 viewport tabs are open.
* Added cross-thread hardening for pixel sampling.
* Added more texture encoding types to the no-read-with-rhi list.
* You now must supply a unique name when saving snapshots.
* Toggling the overlay while in comparison mode no longer blocks the custom image ui (i.e. video control overlay).

### Mobile Rendering

#### Mobile Lighting

**New:**

* Translucent objects now receive CSM shadow when surface lighting.

#### Mobile Postprocessing

**New:**

* Added EUpscaleMethod::Area and swapped in for PrimaryUpscale using the mobile renderer to reduce blurriness at low screen percentages.

### Online

#### Crash Reporter

**New:**

* Apple:

  + Unified crash dump format on iOS & Mac to crashlog
  + Added commandline/ini override to enable crash dump on iOS.
* Upgrade PLCrashReporter to 1.12.0 and apply our existing modifications by diffing 1.8.1 vanilla & our modified 1.8.1

#### HTTP

**New:**

* Added an option to enable different http versions per IHttpRequest via SetOption(HttpRequestOptions::HttpVersion).
* Limit the number of concurrent HTTP requests by default. This helps avoid connection timeouts when queuing up very large numbers of HTTP requests.

**Bug Fix:**

* Fixed Blueprint compilation crash due to mismatching pin names.
* Fixed a low rate crash in HTTP requests.

#### Online Subsystem

**New:**

* OSS for GDK: Propagate the checkout failure error codes from GDK APIs into PurchaseFailure and PurchaseFailureStart errors.
* OnlineServicesCommon: Added TOnlineAsyncOp::GetWrappedHandle to transform the result of an operation to simplify cases where one operation is implemented in terms of another.
* Added OSSv2 PSN Connectivity interface.

**Bug Fix:**

* Fixed OnlineServicesNull handling FPartialUpdatePresenceFix FPartialUpdatePresence not merging RichPresenceString.
* "ENABLE\_PGO\_PROFILE 1" Shipping configuration can now disable online subsystems from the commandline.
* Fixed Push Event related issues

  + Fixed FNpPushEventWrapper::Initialize not correctly handling callbacks disposing.
  + Fixed OSSv1/2 FNpPushEventPushContextWrapper not handling TOptional value safely
* Fixed crash in FUserManagerEOS::ReadFriendsList callback when user failed to authorize.
* OnlineSubsystemIOS: Fixed a race condition that caused a purchase to fail when purchasing an offer immediately after finalizing a successful purchase of the same offer.

**Deprecated:**

* Removed deprecated GoogleSignIn support from OSSGoogle for Android.

### Platform

#### Linux

**New:**

* Upgraded toolchain to LLVM 20.1.8
* Added preliminary support for BuildCMakeLib from Linux.
* Add -NoStripSymbols to UBT to support build systems where stripping needs to happen later in the process.

**Bug Fix:**

* Re-enabled PreLoadScreens.
* Now skips chmod +x dotnet if file is already executable. This addresses permission errors if UE is run on a read-only file system on Linux.
* Fixed an issue where BuildCMakeLib can produce .so files that depend on system shared libraries.
* Fixed loss of precision when FLinearColor is requested in VulkanDynamicRHI::RHIReadSurfaceData.
* Updated FLinuxPlatformProcess::BaseDir to support -basedir=.

#### Mac

**New:**

* Inline Ray Tracing is now available for Mac platforms running with the SM6 renderer.
* Parallel translation of encoders is now enabled by default on Mac (and can be used on iOS). This gives a significant reduction in overall RHI thread time.
* Compute shaders are now executed with concurrent dispatch on iOS and Mac platforms. This provides a significant performance boost when using Nanite.
* Adding Metal-strip to lib processing to reduce metallib sizes (around 10% reduction).
* Delete iAD framework (deprecated) from Core.Build.cs.
* Mac: Included Mac MainThread in CrashContext.runtime-xml for CrashReporter.
* Added support for Aliased formats to be explicitly declared enabling optimisation on Metal platforms.

**Bug Fix:**

* Fixed tweakobjectptr debug on Mac OS.
* Fixed process reaping to be non-blocking and not leaking.
* Fixed an issue where on Mac/iOS SM5 uniform buffers were bound to indices that were unnecessarily high, which caused validation errors in the RHI.
* Stopped the submission thread getting stuck when encountering a NotPermitted GPU error.
* Fixed bug where Metal runs out of counter sample buffers.

  + Metal now longer breaks encoders by default when profiling, this can still be enabled with GMetalSampleComputeEncoderTimings and GMetalSampleBlitEncoderTimings.
* Mac:

  + Fixed Cursor offset from visual because of an outdated ScreensArray when processing OnWindowDidMove, resulting from a DPI change.
  + Fixed MainThreadChecker issue in FMacApplication::OnWindowDidMove. Move bDisplayReconfiguring from FCocoaWindow to FMacApplication since it's not dependent on FCocoaWindow
* HairStrands: Disable HairStrands rendering on Mac SM5.
* ApplePlatformFile: Refactored to use the common implementation FFileHandleRegistry to support more than the limit of read-only opened files.
* Changed Fatal log to a Warning when posix\_spawn fails in CreateProcInternal, for consistency with Windows, and to prevent unnecessary crashing.
* Fixed DPI scaling bug which could cause Mac's to render at 2x res when using PIE.
* Fixed performance issue on editor start up with mdfind taking multiple minutes due to matching incorrect types.
* Fixed potential bug where bindless handle could be null when retrieving viewport texture.

#### Online

**New:**

* Updated GooglePlay Billing library to 7.1.1 in OSSGooglePlay

**Bug Fix:**

* Pixel Streaming:

  + Fixed a crash when streaming with Pixel Streaming and a user attempts to enter text through the stream text modal on a multiline text element.
  + Fixed a crash in the editor when setting the streamID on the command line and streaming with Pixel Streaming.
* AVCodecs: Encoding frames with VP9 can now have odd pixel width or height.

#### Windows

**New:**

* Moved Win32 calls for mouse cursors off of the game thread and onto the task graph to reduce stalls on the game thread from internal lock contention that occasionally occurs.
* Moved processing of mouse inputs to a dedicated thread to reduce overhead on the game thread for Windows. This is useful for mice with high polling rates, e.g. 8000 Hz.
* Made Clang 20 the preferred version of Clang on Windows.
* Changed thread priorities for Game, Render, and RHI threads from Normal to AboveNormal on Windows.
* Increased MinimumWindowsX64TargetVersion from 0x601 (Windows 7) to 0xA00 (Windows 10) to make more functionality available directly from Windows headers.

**Bug Fix:**

* Ensured that shared resources are created as committed resources for improved compatibility.
* Changed our heap VA computation for transient resource allocations on Windows to fix D3D12 call failures on some GPUs.
* Fixed FWindowsPlatformMisc::SetEnvironmentVar to unset the variable if it is null or "", just like on Mac and Linux, and .NET 8.

#### XR

**New:**

* Added native support for the OpenXR XR\_EXT\_frame\_synthesis extension, including Application SpaceWarp (AppSW) on Meta Quest:

  + To enable, set:

    - r.Velocity.DirectlyRenderOpenXRMotionVectors=1 (read-only)
    - xr.OpenXRFrameSynthesis=1 (toggleable at runtime).
  + Currently only supported on the Vulkan mobile forward renderer, and cannot be used alongside features which require standard velocity rendering (such as TAA/TSR).
* Added Android Runtime category tag for immersive mode selection.

  + See https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#appendix-android-runtime-category
* AddedIOpenXRExtensionPlugin hook OnCreateHandTracker().
* OpenXR XR\_EXT\_user\_presence is now supported:

  + Added support for the user presence extension, which tells us whether the hmd is being worn if the platform supplies that information.
  + Removed the previous implementation which attempted to drive the worn state from other openxr state transitions. This had inconsistent and sometimes broken behavior across platforms.
* Replace xr.MobileLDRDynamicResolution with a new CVar, xr.MobilePrimaryScalingMode, which controls whether primary scaling is redirected to the HMD runtime (which will always use spatial scaling) when it would otherwise be unsupported.

  + Options are:

    - 0: Never
    - 1: DynRes Only (default)
    - 2: Always.
* Updated device profiles for standalone XR devices. They no longer inherit from each other in sequence, and the new Android\_OpenXR device profile matches the Quest 3 profile which has had its shadow quality increased for dynamic shadows to draw by default in Mobile Preview and on Device. Consider lowering this value if dynamic shadows are not required.
* Improved expose passthrough support via the editor:

  + Added a new UENUM for environment blend modes, EOpenXREnvironmentBlendModeUpdate SetEnvironmentBlendMode() node to accept EOpenXREnvironmentBlendMode.
  + Added a new GetEnvironmentBlendMode() node.
  + Added a new GetSupportedEnvironmentBlendModes() node, which returns supported blend modes in an array in order of runtime preference (highest to lowest).
  + Added a new IsCompositionLayerInvertedAlphaEnabled() node.
  + Added an xr.OpenXRInvertAlpha checkbox to the OpenXR plugin settings.
  + Added an r.Mobile.PropagateAlpha checkbox to the Engine->Rendering->Mobile settings
  + Renamed OpenXRHMDSettings to OpenXR Settings, since it controls settings for the entire module.
* OpenXR is now building for all platforms:

  + The platform specificity of the openxr plugins and modules was problematic because content derived from these would not load on non-xr platforms for projects that are meant to be cross platform.
  + OpenXR is not actually platform dependent. It can be implemented on any platform. If it is present as a fully independent openxr runtime a small amount of platform specific code is needed to implement an openxr loader.
  + It is also possible to create an unreal plugin which either acts as an openxr runtime or is able to find an openxr runtime.
  + The plugins are still disabled by default.

**Bug Fix:**

* Removed permissions not allowed by Quest App Store.
* Fixed various debug draw elements failing to render when using Instanced Stereo or Mobile Multi-View:

  + r.VisualizeOccludedPrimitives
  + ShowFlag.Bones
  + DrawDebugBox and other similar calls, excluding DrawDebugString.
* Fix a bug where late update camera movements were not accounted for when calculating scene visibility, causing smearing, latency, or other artifacts when some rendering features were used.
* Fixed GetHMDData TrackingStatus field:

  + It was only checking if the hmd device tracking handle was valid, needs to check if the hmd is actually tracked.
  + It was also attempting to use the camera position rather than the hmd tracking position.
  + Removed GetMotionControllerData and FXRMotionControllerData which were deprecated in 5.5.
* Added handtracking permissions for Quest.
* Fixed OpenXR AddProfile for input always being given true rather than the passed in bHasHaptics parameter.
* Fixed a crash when using the SteamVR runtime with Vulkan.
* Fixed MetalViewport SubmitImmersive: [IOGPUMetalCommandBuffer setProtectionOptions:]:585: failed assertion `setProtectionOptions: with uncommitted encoder'
* Fixed Visionos cp\_frame\_query\_drawable null handling:

  + We abandon the frame if the drawable is null, this indicates that the app is either being paused or exited.
  + Essentially we just continue the frame but don't call the cp\_ functions.
  + At the beginning of the next frame we handle the state change.

**Deprecated:**

* Deleted the formerly deprecated functions from 5.3 to remove references to the UPlayerMappableInputConfig type.

### Platform Mobile

#### Android

**New:**

* Added -FastIterate flag to Visual Studio/Rider/Quick Launch, to have libUnreal.so outside the APK, and made build iteration faster in general.
* Added -AndroidStudio flag to GenerateProjectFiles that generates a Gradle project that wraps around the original Gradle project that is suitable for use in Android Studio.
* The Android Vulkan detection logic now uses the same VkApplicationInfo parameters (e.g. App name, Engine version) as used by the VulkanRHI initialization, so graphics drivers that need to opt out of Vulkan for Unreal Engine apps can do so consistently.
* Implemented support for factoring screen rounded edges in computing the safe zone. The implementation means users can align the safe zone horizontally or vertically to the rounded edge excluded areas or to an average of both.

  + Additionally, cleaned up current safe zone implementation to determine size relative to the main view instead of the display as the system may reduce the main view to exclude cutout areas.
* Constrained kotlin stdlib dependencies to >= 1.8.0 to fix building issues.
* Recompiled libopenxr\_loader with 16kb page support based on NDK 27.2.
* Removed need for security token for debuggable applications when using AndroidFileServer with UnrealAndroidFileTool.
* Added warning if a library on Android is not 16kb page size compatible.
* Removed bashrc/bash\_profile related code, instead using zshrc for Mac as primary source of environment variables.
* Report resident size of "libUnreal.so+base.apk+[anon:.bss]+[anon:linker\_alloc]" as ProgramSize on Android.
* Report resident size of all memory mapped files as MMIO on Android.
* Tag all virtual memory with "UE" VMA tag on Android.
* Added the vkquality 1.2.2 library which can be used as another data point as to whether to select Vulkan or OpenGL ES.

  + The result of the vkquality check is returned in the SRC\_VKQuality that can be queried by the Android device profile selector rules.
* Updated AutoSDK "MinVersion" to NDK r27c.
* Improved AndroidFileServer (AFS) file transfer - retries and resumes for file push to device.
* Resolves potential sync issue that leaves the EditBox non responsive to text input and the keyboard in a state where it doesn't get dismissed its the 'Done' button.

  + Additionally, replaced setVisibility with add/remove View to work around an Android level spam issue when keyboard is repeatedly dismissed/invoked.
* Improved Android Camera Player with the Android Camera2 APIs and support for Vulkan frame data processing.
* Default NDK is updated to r27c, buildtools to 35.0.1, bundletool to 1.18.1.
* Recompiled libopenxr\_loader with 16kb page support based on NDK 27.2.
* Replaced libhwcpipe with C wrapped .so to avoid C++ STL ABI conflicts on Android.
* Now starts loading libUnreal dependencies early for faster startup time
* Created Android-arm64/x64 configs in Visual Studio.
* Made Quick Launch now build an x86\_64 binary when launching on x86\_64 devices, such as the emulator.
* Lowered Android SDK "MaxVersion" to NDK r28c, due to NDK r29 compiler bug.
* Update GooglePAD to 1.15.4 / 2.3.0.
* Added engine device profiles for Mali-G1-Ultra and similar devices.
* We now detect devices using the ANGLE OpenGL ES driver and use the Vulkan deviceName string for SRC\_GPUFamily. This means the device profile Vulkan selection can continue to match the same string as used when the device is in native OpenGL ES mode.

**Bug Fix:**

* Enabled desugar for older Android support.
* Filtered out AFSProject task if running it from Gradle (prevent second run).
* Ensured java sources are wiped when FirebaseEnabled is toggled off. Otherwise, source files are left behind that don't compile as the Java dependencies don't get populated by the plugin when FirebaseEnabled = false.

  + Additionally, registerBuildSettiings for the Firebase settings referenced from the plugin's UPL.
* Fixed the timing of firing the MediaOpened event in Android Camera Player.
* Fixed the issue that the Console Command input is disabled when "Show Launch Image" is off in Project Settings.
* Ensured keyboard OnTextCommitted messages are dispatched when using Android improved virtual keyboard.
* Ensured nativeKeyboardInputResult is invoked when keyboard is dismissed and keeps the reference to VirtualKeyboardWidget valid until the result is handled.
* Corrected issue with file locking in UnrealAndroidFileTool for writes.
* Fixed black screen when playing start movies.
* Added a watch for deletion complete before database close in Fetch2 (part of background downloading).
* Moved early load sync point to prevent possible crash due to an ordering issue.
* Made NDK toolchains detection for manual SDK installs more robust.
* Made JAVA\_HOME environment setting for manual SDK installs more robust.
* Added missing setting of ndkPath to Gradle property value
* Fixed generated install scripts with overflow OBBs that are broken on non-Windows
* Updated Breakpad dump\_syms with version supporting compressed symbols.
* Added catching of UnsatisfiedLinkError in GameApplication.LoadLibraries, in case some other ClassLoader has already loaded them
* Fixed the WebView freeze when switching the game to the background while loading a URL.
* Fixed VersionScriptFile not being created robustly, sometimes causing build failures.
* Worked around a Gradle bug whereby when only assets change, it attempts to patch the existing APK from previous packaging by adding asset deltas resulting in growth of the final APK payload. Workaround is detection of changes to assets and wiping the existing APK to force Gradle to repackage it correctly.
* Fixed a Java exception when closing the Camera Device during initialization.
* Fixed the "Play On Open" feature for the Android Camera Player.
* Fixed the keyboard EditBox layout on devices with cutout when the cutout area isn't used.

  + getWindowVisibleDisplayFrame returns a rectable in screen space, however, the edit box coordinates need to be provided in the main decor view's space.
  + As such, translate the results of getWindowVisibleDisplayFrame to the decor view's space by translating these by the decor view's screen position.
* libGPUCounters: Android early crash fix libGPUCounters is built with statically linked libc++, exposing a bunch of std symbols, which override those in libUnreal.so.

  + For example, it overrides std::to\_string leading to an early crash:

    - Other plugin calls to\_string (uses libGPUCounter implementation and its operator new & memory alloc).
    - That string is later destructed, using engine's operator delete.
    - Our allocator fatals on unrecognized pointer.
  + The fix is to add a linker version script to the libGPUCounters build and only expose C API related symbols as global.
* Updated Android TargetSDK Fix templates with AFS configuration.
* Updated Fetch2 3.3.0 with new version of androidx.room 2.7.1 (used for background downloading).
* Added detection of SQL lock error on enqueue (can happen after deleteAll in Fetch2 background downloading).
* Added new dump\_syms\_comp.exe supporting compressed Symbols for Android use.
* Fixed an issue with assets with starting offset other than 0.
* Made MakeApk do a clean during packaging if EnableBundle is flipped between builds.
* Fixed crash from pending JNI exception in non-Shipping builds, when skipping over checks.
* Now round rather than truncate Android getRefreshRate when converting to integer.
* Fixed the freeze of Android Media Player playback on Xiaomi 13T or devices with a similar chipset.
* Fixed TargetSDK 35 compatibility issues with background downloading.
* No longer requests WRITE\_EXTERNAL\_STORAGE permission if TargetSDK doesn't support non-scoped storage.
* Ensured that keyboard dismissed isn't called when the text input is accepted by the Virtual Keyboard's done key or a physical keyboard's enter key.

  + Additionally, ensured that on dismissal of the virtual keyboard, text entry type is Canceled so that text committal only triggers if the widget is configured with behaviour 'Text commit on Dismiss'.

#### iOS, tvOS, and iPadOS

**New:**

* IOS: Notification about network path characteristic FIOSPlatformMisc::OnNetworkConnectionCharacteristicsChanged can be used to know about network characteristic changes, e.g. knowing if a new connection is constrained or expensive.
* Re-enabled SetBytes and SetBufferOffset on iOS and enable on tvOS.
* Added support for Xcode26.
* The IOS rotation code now defers applying a new rotation until after we have rendered a new frame in the new orientation, for both auto-rotation and programmatic orientation selection.

  + This fixes the issue with a squashed aspect ratio when the user rotates the app at a time we cannot immediately render a new frame, such as during loading.
* Now ask for background time on iOS until all delegates called from applicationWillEnterBackground are invoked.
* Disallowed resolve of R32F MSAA targets as this format isn't MSAA resolvable in Metal.

  + Additionally, make the texture memoryless as we'll never be resolving to it.
* Exposed network changed delegate for iOS.
* Implemented functionality for -MetalPSOCache=use.

**Bug Fix:**

* Deferred handling of notifications if the engine isn't ready to receive.
* Occlusion Query Helpers now correct the number of frames for Metal mobile platforms.
* Ensured valid URL for pipeline cache save location.

  + The current invalid URL generated was invalid as it was constructing a file URL using the absolute string of another URL as a path parameter to the constructor, causing MTLBinaryArchive->serializeToURL to crash when used.
* Now store webauth credentials in iOS keychain using a key that does not change after uninstalls.
* Fixed some memory leaks in the iOS web browser.

### Rendering

#### Architecture

**New:**

* Virtual Texture:

  + Renamed "r.VT.Support16BitPageTable" to "r.VT.PageTableMode".

    - The setting can now be modified live at run time instead of being read only.
    - Also removed "r.VT.SplitPhysicalPoolSize" which now corresponds to setting "r.VT.PageTableMode=2".
  + Unified mip color debug display for Virtual Textures.

    - "r.VT.RVT.MipColors" is deprecated and Runtime Virtual Textures now respect "R.VT.Borders" which other Virtual Textures already use.
    - "r.VT.Borders" is no longer on/off. The value now sets the debug border texel width.
    - Also added "r.VT.Borders.Mip" which isolates the mode to a single mip level.
  + Release/Recycle Virtual Texture spaces after they are unused for some time.

    - We don't release immediately to avoid cases during loading where this might trigger unnecessary Recreate/Resize work.
    - The old behavior was to never Release/Recycle unless we ran out of space slots.
    - Added "r.VT.SpaceReleaseFrames" to control this. The default is to release after 150 frames. Setting to -1 will return to the old behavior.
  + Changed draw behavior for selected meshes which only write to Runtime Virtual Texture.

    - Previously we would fully show those meshes on selection (they are hidden in the main pass otherwise).
    - Now we only show the selection outline.
* Runtime Virtual Texture:

  + The display name of the "Virtual Texture Builder" (also sometimes previously known as "SVT") asset is now "Streaming Runtime Virtual Texture" (i.e. SRVT). This avoids confusion with Sparse Volume Texture (SVT).
  + It can now be created from the content browser.
  + Now prevent StreamingTexture from being carried over when duplicating a RVT component (Save As, copy/paste...).  This avoids the common mistake of using another map's SRVT after a Save As.
* Added optional Z-increment parameter to FPixelShaderUtils::AddRasterizeToRectsPass, in order to control the Z of the quads (Z = quad index, i.e. instance id \* ZIncrement). Combined with depth test enabled, this enables making the rasterization deterministic in case of overlapping quads.

**Bug Fix:**

* Runtime Virtual Texture preload requests now work for the adaptive page table case.
* Fixed programmatic RenderDoc captures randomly crashing.
* Fixed non DBuffer mesh decals not obeying the mesh component "Receive Decals" setting.

#### Lighting

**New:**

* Enabled VSM receiver masks for directional lights by default.

  + ~10MB memory overhead (depending on settings/scalability).
  + Often fairly significant performance improvements in uncached cases with lots of dynamic geometry.
* Disabled the selection of Virtual Textures on Rect Light components. These have never been supported in a cooked build, but were still shown in the Editor.
* Exposed Max Draw Distance and Max Distance Fade Range to Blueprint.
* Now store and propagate "cleared" flags to avoid reclearing pages we never wrote into; particularly relevant for receiver mask where we treat all dynamic pages as uncached but often don't write into them all.
* No longer allocate unnecessary receiver mask space if local light receiver masks are disabled.
* Refactored VSM ID allocation so that we can control the order more consistently. The immediate goal is to guarantee that directional lights get allocated first so that we can easily allocate receiver masks just for directional lights without the memory overhead of doing it for all local lights as well
* Added TexCreate\_3DTiling flag to volume textures in TranslucentLighting to reduce memory and boost performance on some platforms.
* Marked r.UseClusteredDeferredShading and r.Mobile.UseClusteredDeferredShading as deprecated and added notification about future removal. Clustered deferred shading will be removed in a future release due to lack of utility to reduce maintenance burden.

**Bug Fix:**

* Fixed incorrectly reported one pass projection overflow with megalights active. Only run VSM coarse page marking once when there are multiple views as it is view-independent.
* Scale the light fade range by `GLightMaxDrawDistanceScale` to avoid lights becoming too dim at lower scales.

#### Lumen

**New:**

* Enabled half res integration on High scalability (r.Lumen.ScreenProbeGather.StochasticInterpolation 2).

  + This can soften normals in indirect lighting, and make GI a bit more noisy.
  + On the other hand it saves ~0.5ms on console at 1080p, which feels like a right tradeoff for High scalability intended for 60hz on console.
* Lumen Screen Probe Gather: Bent Normal Integration improvements (r.Lumen.ScreenProbeGather.ShortRangeAO.ApplyDuringIntegration 1)

  + Implemented r.Lumen.ScreenProbeGather.ShortRangeAO.ScreenSpace.FoliageOcclusionStrength.
  + Fixed EvaluateSHIrradiance which was causing brightening in corners.
  + Removed double AO apply during bent normal integration. Now instead of applying AO for the second time we apply only the GI approximation using AOMultiBounce, as DistantIlluminationRescale was too strong.
  + Clamp decoded AO as it could be larger than 1 causing too strong indirect specular occlusion.
  + Now support ShouldApplyDuringIntegration when Screen Probe Gather Integration and Short Range AO downsample factors match.
  + Fixed artifacts when ShortRangeAO is disabled, but ShouldApplyDuringIntegration is enabled.
* Lumen HWRT path now supports split screen.
* R.LumenScene.DumpStats 3 will now dump primitive culling information. This is useful, as it merges instances into a single entry making it easier to read the log.
* Moved GBuffer tile classification out into a single pass, which is also storing opaque history for the next frame. This pass is reused across Lumen and MegaLights for better performance.
* Screen tile marking optimizations, which speed up reflections, GI, and water reflections.
* Tweaked default settings:

  + r.Lumen.TraceMeshSDFs 0 - SWRT detail traces (mesh SDF tracing) is now a deprecated path, which won't be worked on much. For scaling quality beyond SWRT global traces it is recommended to use HWRT path instead.
  + r.Lumen.ScreenProbeGather.MaxRayIntensity 10 - firefly filtering is now more aggressive by default. This removes some interesting GI features, but also reduces noise, especially from things like small bright emissives

**Bug Fix:**

* Fixed missing subsurface energy by removing extra divide by PI. Now an emissive card matches a rect light reference of the same irradiance. This bug was only affecting Epic scalability (r.Lumen.ScreenProbeGather.IrradianceFormat 0 path).
* Fixed a bug on Mac platforms when running on SM5 using R11G11B10 for Typed UAV's causing rendering corruption.
* Fix visual artifacts and out of memory reads/writes when using non power of 2 Tracing Octahedron Resolution. Now Tracing Octahedron Resolution is always clamped to valid input values.
* Nanite Skeletal Mesh now supports bHasRayTracingRepresentation, so that those primitives can be skipped from Lumen under certain conditions.
* Fixed landscape culling stealing the r.Lumen.DiffuseIndirect.Allow's on changed callback. This is not needed anymore since this CVar's callback already invalidates all components, including landscape ones.
* Fixed tile artifacts on indirect specular on cloth pixels in the same tiles as hair pixels
* Don't reset temporal history on SceneTexturesExtent change. Sometimes SceneTexturesExtent can change due to inline view rendering (like water) which causes full history reset and results in visible noise on screen until things converge again.
* Skip creating RGS when Lumen is disabled from the PPV volume.

#### Materials and Shaders

**New:**

* Added an asset registry tag to find material instances causing shader permutations.
* Enabled Virtual Texture sampling on Volume material domains.
* Changed the interpretation of the PreSkinned Local Bounds material node when used on Instanced Static Mesh. Previously it was the bounds for the entire component. Now it is the bounds for the mesh instance.
* Added platform cached ini value to determine whether to compile 128 bit base pass pixel shader variations on platforms which require them. These are infrequently needed and turning them off can save 50k shaders / 15 MiB at runtime r.128BitBPPSCompilation.Allow (default is true, for backwards compatibility).
* Improved error messages reported by shader conductor to properly identify where individual error messages begin and end (and so ensure each compile error is reported on its own).
* Disabled the ZoomToFocus behavior when creating a usage node from the declaration - No longer zooms the focus of the editor since this was visually jarring for the user.
* Optimized material instance post-load in Editor builds by directly hashing the portions of shadermap ID used to construct the unique asset name, rather than constructing the full string representation then hashing.
* Added a Base field to Material Parameter Collections, which can be used to derive one collection from another, with the derived collection inheriting the base's properties.
* Added support for overriding a material's parameter collections with derived collections in material instances.
* Material scalar parameters can now optionally select an enumeration object to use for selecting scalar values by name in the material UI.
* Added default initialization of fields of FMaterialEnumerationEntry.
* Added function APIs to MaterialEditingLibrary to manipulate the new Enumeration material parameter.
* Reworked ShaderDebugData output to unify the "worker input" and "direct compile" debug mechanisms:

  + Removed r.ShaderCompiler.DebugDumpWorkerInputs cvar; always dump a valid worker input file for all jobs whenever debug info is enabled.
  + Moved writing of this file into job completion callbacks alongside the other debug artifacts, so will be written out for cache hits if r.ShaderCompiler.DumpDebugInfoForCacheHits is true.
  + Modified these files to not include a copy of the compressed source, instead using the .usf artifacts.
  + Renamed "direct compile" mode to "debug compile" and made it use this file instead of needing to serialize extra data into the debug .usf file.
  + Removed the r.DumpShaderDebugWorkerCommandLine cvar; all jobs will export a DebugCompileArgs.txt file containing the commandline that can be used to run SCW in debug compile mode by default.
  + Modified shader pipeline compile jobs to export a single worker input file (in the first stage's debug folder).

    - Each stage of a pipeline will export their own DebugCompileArgs.txt (for convenience, so if only a single stage fails you can still navigate to that stage's debug folder and run the job from there).
    - The debug compile for any pipeline stage will run the full pipeline job (so compilation always matches what happens in the normal context) with paths modified to be relative to that specific debug folder for convenience (so when downloading debug output from another machine, only one path in the commandline needs to be fixed up to run)
* When using the Material Editing Library of functions, now always refreshes the material instance editor when changing material instance parameters.

  + This fixes a bug where you would set a MI parameter via a python script and the MI Editor wouldn't update the properties panel to show the newly updated value.
  + Automatically call UMaterialEditingLibrary::UpdateMaterialInstance() whenever a parameter on a instance is set via the library.
  + UMaterialEditingLibrary::UpdateMaterialInstance should try to find any open material instance editors and tell them that the material instance has changed.
  + FMaterialInstanceEditor::NotifyExternalMaterialChange now calls `Refresh()` which will update the whole editor, including the property window, to properly reflect any parameter changes made by the library.
* Inconsistency fixed on Comment Bubbles on Material Editor:

  + To ensure visual consistency new Comment bubbles created use the same color value as the other node editors, like Blueprints.
* Material Editor: Added two experimental custom output nodes `Motion Vector World Offset (Per-Pixel)` and `Temporal Responsiveness` to give users a way to modify per pixel motion vectors and set how responsive the temporal history is.

  + Temporal Responsiveness: Describes how temporal history will be rejected for different velocity mismatch levels.

    - Default :0
    - Medium (0,0.5]
    - Full (0.5, 1.0].
    - Now, it will be used by TSR to change rejection heuristics. Translucency material can also use it to request higher responsiveness if depth is written (r.Velocity.TemporalResponsiveness.Supported=1) or clipped away (r.Velocity.OutputTranslucentClippedDepth.Supported=1).
    - The translucency mask generated improves TSR thin geometry quality.
  + Motion Vector World Offset (Per-Pixel): Works similar to the `Previous Frame` input of `Previous Frame Switch` but in the pixel shader. Regions with invalid velocity will be approximated with the current frame's offset.

    - This function currently supports non-nanite meshes only in non-basepass velocity write and is implemented in two passes. Use r.Velocity.PixelShaderMotionVectorWorldOffset.Supported to enable it.
* Added support for customizing the file name for ShaderSymbols and ShaderTypeStats output files.
* Exposed EMaterialProperty::MP\_MaterialAttributes to Blueprints, Python, and the Editor UI.

  + This way users can use the Blueprint MaterialEditingLibrary to connect expressions to the MaterialAttributes output on the material block for materials that use MA.
* Added a MaterialEditingLibrary function called RenameMaterialParameterGroup and RenameMaterialFunctionParameterGroup which bulk renames all the Group Names on many Material Parameters at once.

  + Changed LogMaterialEditingLibrary verbosity to include `Log` messages.
  + Simply loop over all material expressions that are parameters and if the OldGroupName matches change the name to the new one.
  + Call RecompileMaterial to force the material to recompile so MIs update through the editor.
  + Unfortunately the `Group` property of material expressions is spread across many different classes. To avoid checking all the different material expression types (there are 8 different UMaterialExpression classes with their own unique Group), I've opted for a property system approach that looks for the property by name.
* Optimize pipeline cache to reduce single allocation size and improve performance by copying less data on resize.
* Modified output of shader formats using DXC (DXIL output) to keep the reflection data in the DXIL container if the r.Shaders.ExtraData cvar is enabled. This is a workaround for graphics tools which cannot correctly re-generate reflection information from external PDBs.

  + Note that this bloats runtime memory usage so should only be enabled locally if you are encountering issues seeing data formats (i.e. cbuffer layouts) in such tools.
* Can now copy/paste material errors in the PlatformStats panel.

  + Simply makes the text read-only "editable" so the user can select the text and get automatic copy/paste functionality.
* Rename the aliases for the Convert node from `Make Float4` to `Make Vector4` to match "Vector Parameter" and "Constant Vectors'.

  + This also avoids confusion with the existing Make Float 4 Engine Material functions.
* Added additional project-specific texture groups.
* Vector Parameter Expression now shows output pin display names to avoid confusion on what the first output pin is.

  + Also fixed "Convert to Constant" for vector parameters. By default the outputs are now:

    - RGB
    - R
    - G
    - B
    - RGBA
  + Users were expecting the first output pin to be RGBA, but it was RGB.
  + Now shows output name on pins by default for vector parameter.
  + Added RGBA output as the final one to match what TextureSample does.
  + Updated this behavior in the new material translator (it should really use the outputs array which is already defined).
  + If no channel names are specified show R, G, B by default.
  + No longer truncates and loses user data when using "Convert to Constant" for Vector Parameter -> Constant.
  + Gave constant 4 expression display names so the conversion code can match outputs by name when converting nodes.
* Marked deprecated virtual functions from MaterialInterface and FMaterial as final to avoid silent errors.

  + Modified all derived classes to override the right functions.
* Improved IO performance of FinishPopulateShaderLibrary.
* Added a new debug artifact (ShaderTypeStats.csv), dumped by default for all cooks to the ShaderDebugInfo folder for each shader format.

  + This CSV file contains permutation counts/code sizes for all shaders in the shader library, grouped by shader type.
  + Note that this is not directly representative of final shader memory usage since it doesn't account for potential duplication of bytecode introduced by the pak chunking step (where shaders used in multiple pakfiles will have a copy in each).
  + This is only intended to be used as a tool for tracking and comparing shader growth over time or between cooks.
* Subsurface Profile: Improved neighborhood validation for checkerboard when enabled, less bleeding into subsurface scattering region for low res.

**Bug Fix:**

* Virtual Texture Pending Mips debug view now takes screen scaling into account.
* Fixed UMaterialExpressionParticleSubUV::Compile bug that caused the node not to use the texture object connected to the Texture input pin.
* Repaired cook editor-only-data nondeterminancy in materials.
* Ensured that FDefaultMaterialInstance's CacheUniformExpression is cancelled on destroy if still pending.

  + Under certain conditions the FDefaultMaterialInstance could be destroyed and subsequent dispatch of CacheUniformExpression would result in a crash due to a dangling reference. This replicates functionality from FMaterialInstanceResource for which this guard is already implemented.
* Fixed a potential out-of-bounds read when remapping shader compile diagnostic messages; could occur if there were no digits before the end of the line in the diagnostic message after the \_\_UE\_FILENAME\_SENTINEL marker.
* Fixed material shader map not releasing compilation ID if shaders failed to compile.
* Fixed incorrect reporting of line numbers when compile errors are encountered in generated material code.

  + The code calculating the line number offset of the substituted #line directive in MaterialTemplate.ush was incorrect.
* Fixed a bug that could cause a retry loop when running with shader development mode enabled and a preprocessing failure is encountered.
* Fixed crash in SafeRenameEditorOnlyData() when EditorOnlyCurrent is null.
* Fixed a material derivative autogen crash when dealing with uints.
* Fixed a crash occurring when the material parent of an instance is changed through scripting.
* Fixed ShadingModel material expression in-node combobox to display only valid shading model entries.
* Made a minor fix for custom ShaderTypeStats customized name, needs to lookup cvar by ShaderFormat.
* Added support for Nanite Geometry Collections to Preskinned Local Bounds material node.
* Fixed an issue where the Vulkan shader pipeline cache would sometimes incorrectly produce cache misses for shaders that had already been compiled and serialized.
* Fixed shader output for preview/transient materials being cached in DDC.
* Changed UMaterialFunctionInterface to include the BlueprintType annotation.
* Removed incorrect application of the component scale to the output of World Space Vertex Normal node when used with skinned mesh.
* Fixed an uncommon crash in Lerp material expression when the alpha pin was connected to a non-primitive output.

#### MegaLights

**New:**

* Implemented MegaLights-driven VSM marking to only mark VSM pages that MegaLights has selected samples for.
* Added the r.MegaLights.DownsampleCheckerboard, which can run sampling/tracing at half res (every other pixel). It's a good middle ground between default quarter res sampling and option full resolution sampling.
* Exposed r.MegaLights.HardwareRayTracing.ForceTwoSided, which allows to flip between matching raster behavior and forcing two-sided on all geometries in order to speedup tracing.
* Now always vectorize shading samples. This saves on average 0.1-0.2ms in complex content on current gen consoles.
* Improved spatial denoiser filtering after disocclusion.
* Limited number of samples sent towards the directional lights to a specified fraction (r.MegaLights.DirectionalLightSampleFraction). This helps with noise indoors, where there's a strong directional light inside taking over the entire sampling budget.
* Now uses downsampled neighborhood for temporal accumulation. Interpolated pixels don't add much to neighborhood stats, so we can skip them, improving quality by effectively using a wider neighborhood filter. This also improves performance of the temporal accumulation pass, as it now can load less data into LDS.
* Now properly handle invalid sample upsampling. Sometimes during upsampling we can't find any valid sample and need to fallback to history (without any neighborhood clamp). This makes lighting on highly detailed or thin geometry a bit sharper and a bit more stable.
* Disabled guiding tile filtering and added stochastic bilinear sampling of guiding tiles in order to hide tile artifacts.
* Now merge identical rays in order to avoid overhead of duplicated traces. Duplicated rays happen with strong point lights, where we may send a few identical rays to the same light doing unnecessary work.
* Added screen space trace for hair (r.MegaLights.Hair.ScreenTraces). Screen space traces improve card hair quality compared to approximate RT fallback mesh, but can be noisy. In order to reduce the noise there's now extra hair only screen space trace bias (r.MegaLights.Hair.ScreenTraces.Bias).
* Merged downsample factor / checkboard CVars into a single r.MegaLights.DownsampleMode CVar.

**Bug Fix:**

* Now require ray tracing platform support, in order to skip compiling and cooking MegaLights shaders on certain platforms.
* Fixed split screen crash due to out of bounds memory reads.
* Fixed denoiser artifacts on borders between dielectrics and metals (bright outlines) caused by too aggressive material demodulation factors.

#### Nanite

**New:**

* The dithered opacity mask option is now supported for Nanite rasterization.
* Added a new culling check that can improve Nanite culling speed and reduce the amount of memory needed for candidate clusters (r.Nanite.Culling.MinLOD).
* Added support for rendering Nanite skinned meshes in the animation editor.
* Exposed NanitePixelProgrammableDistance for Nanite skinned meshes to enable forcibly disabling pixel programmable rasterization of Nanite when the mesh is further than a given distance from the camera.
* Added experimental and optional passes to prime the HZB before VisBuffer rendering if the HZB is missing (e.g., due to a camera cut), see cvar r.Nanite.PrimeHZB et al.

  + The main idea is to draw a lower resolution (HZB or lower) and lower detail (by using LOD bias and/or drawing only ray tracing far field scene geometry).
  + This new render is then used to build a HZB with some depth bias that is then used to render the full scene, greatly improving the cost in many cases.
* GeometryCollection: Added a "Nanite Minimum Residency" setting for Geometry Collection assets. This controls the number of resident nanite root pages.

  + Previously we used a single root page and this is still the default.
  + Increasing the value can avoid pop-in when a Geometry Collection is first shown.
* Added support for disabling "Render In Main Pass" on static mesh components for Nanite meshes.

**Bug Fix:**

* Fixed a bug where the World Position node would return incorrect results when used to calculate opacity in a masked material.
* Automatically disable Software VRS when Nanite is not enabled, preventing it from generating shading rate images which will not be used.
* Fixed a rare streamer crash that could occur when a streaming page is resident in the streaming pool while its root page slot gets reused a multiple of 256 times.
* Invalid page requests from the GPU are now ignored and optionally logged, instead of potentially resulting in a crash.
* Suppressed console warning spam when `r.Nanite.Visualize` is set to an invalid value.
* Fixed an incorrect conservative instance draw distance test used in the hierarchical instance culling that caused missing instances.
* Nanite: Fixed incorrect geometric normal when using r.RayTracing.Nanite.Mode=1.
* Fixed a GPU crash that could occur when Nanite was rendering to odd viewport sizes.
* Fixed a crash in Nanite primitive filtering that can happen if HLOD force-hidden primitives, or the view's ShowOnlyPrimitives/HiddenPrimitives, contain invalid primitive IDs when there are no primitives in GPU scene.
* Fixed a regression where if a static mesh has multiple mesh sections of the same material, Nanite build would merge them into a single mesh section, which could cause them to be re-ordered and cause issues. Now the multiple mesh sections remain intact, but the fallback will not have triangles in the duplicated sections.
* Fixed an issue where the sign of the TwoSidedSign node would be flipped for masked materials.
* Fixed a crash caused by enabling a Nanite visualization mode when instanced stereo rendering is enabled.
* Fixed an issue where MaxHierarchyDepth was not calculated correctly, which could under rare circumstances result in streaming not progressing beyond a certain point.
* Fixed an issue where having a non-Nanite capture in the scene can cause the Nanite streamer to not get updated and result in GPU hangs.
* Fixed an issue where scene captures and main view rendering would independently try to update residency, sometimes resulting in visual artifacts.

#### Niagara

**New:**

* CascadeToNiagaraConverter: Can now add template emitters.
* Supported read / write icons for stateless: You can now more easily see where bindings are used in LW emitters.
* Added a way to release resources from render target 2D:

  + Changed handling of null texture to set the material default to avoid dangling references.
* Removed slate dependency from emitter merging (used by python scripts), which could trip up commandlets that ran without the editor UI.
* Other distribution types can now opt into indexing / address / interpolation.
* Initialize particle add lookup value mode options:

  + Added initial look up value mode enum.
  + Enabled lookup on initial position.
  + Changed color to a distribution.
* Added getter method for Niagara parameters.
* Lazy instantiate parts of the baker to reduce memory usage:  Added a call to tick the baker world as paused, this ensures the world manager is called to process clean up functions.
* Arrays for LW distributions:

  + Made a large refactor to make reading a distribution a function call vs a structure.
  + When sampling a value needed for motion vectors pass in multiple time parameters and it will return both values to ensure random is respected.
  + Some limited space was added to pack indexing into the data, this can be controlled using meta data on the distribution property.
  + GPU storage moved to ByteAddressBuffer for LoadX operations which gave a small speed boost.
  + Perf on a large number of particles was marginally better vs before.
* LWE:

  + Added support for debug HUD particle attribute display.
  + Added support to data set readback.
* Adjusted display name for SKM / SM DIs to remove confusion between the asset types.
* Changed pin color based on Data Interface vs UObject to reduce confusion.
* LWE Shape Location Changes:

  + Added shape scale.
  + Fixed plane shape not applying rotation.
  + Added surface mode to the cylinder.
* Material Parameter Collection Data Interface: You can now push scalar / vector parameters from Niagara to MPCs.
* Removed UNiagaraEmitter from stateless emitter on cook.

  + The cooked build does not require them, various parts of the UI still make assumptions and will be cleaned up.
  + This saves ~4k per stateless emitter.
* Added rotator distribution to stateless & use in shape location to allow the rotation to be bound to an attribute.

  + Fixed the axis not properly being used on the display name for each widget.
  + Fixed the same binding being added multiple times.
* Niagara Editor Preview Actor:

  + Used for previewing and tuning Niagara Systems without the need to run PIE.
  + Has some simple default motion options which can be overridden by a derived Blueprint for more complex behavior.
* Niagara Fluids: Added vector controls for turbulence frequency and gain.
* Niagara Content: Added distribution curve dynamic inputs for float, vector, and vector2D types.
* Weighted Distribution Int Array:

  + Each entry has a value & weight.
  + The Weight is used in the random calculation, so the higher the weight the more likely it is to return that value.
* CascadeToNiagaraConverter: Added UPROPERTY() tags.
* When changing the preview platform, now invalidate the cooked status.

  + We need to make sure everything is in sync when the device profile changes to avoid crashes inside the VM.
* Added Niagara to Visuals placement menu.
* Updated Stateless Rotate Around Point module:

  + Added coordinate space / rotation / center.
  + Added a CPU path for the module.
  + Added Debug Draw support.
* Added a property to customize quick capture number of frames.
* Added ID support to Sim Cache Reader.
* Added wildcard name match exclusions to sim cache compare.
* Validation rules can now be disabled by config file.
* Added information about who is using sorting.

  + Added a marker to sort key generation.
  + Added a console variable fx.Niagara.Batcher.DumpSortedSimulations which can be used to dump to the log.
* Changed the color grad editor stop time widget to use the spin box.

  + This allows for math operations and validation of the input data.
* Dynamic Mesh Sim Cache Storage + Visualizer.
* Added all base Niagara float types to sim cache interpolation.

  + Enabled by default can be disabled by changing bInterpolateAllTypes in the creation parameters.
  + This improves MRQ renders with temporal samples.
* Added concurrent sim cache reading when no data interfaces are cached.

  + Can be disabled using "fx.Niagara.SystemSimulation.AllowASyncSimCache".
  + Enabled concurrent execution for fixed DT systems if it's a single tick.
  + Fixed a bug in the component recaching where it ran all the time in the editor.
* Stateless Curve Editor Improvements:

  + Moved the existing LW curve editor into the compact curve editor.
  + Added a new curve editor for distributions which is closer to the existing curve editor.
  + Exposed some of the common widgets shared between the editors.
  + Future change will be to wrap the DI inside the distribution adapter and share the editors, which will be useful for the compact editor also
* Made the FXSystemInterface sharable to fix world tear down reference issues.

  + In some situations an FX component can be destroyed after the world.
  + When the world is destroyed it will destroy the FX system set, which will enqueue a command to destroy the FX interfaces.
  + The render command can execute before the FX component's are destroyed leaving them with a dangling reference.
* Added a setting to enable HLSL 2021 in Niagara.

  + HLSL 2021 features will fail to compile on the VM and on some platforms, but this allows users to experiment.
* Added an enum for notify progress, none / forward / reverse.

  + Fixes issues around using negative rate scaling and allows the user to still use 0-1 when playing backwards.
* Disable Source Mode with LWE to reduce confusion.

  + We don't have a particle stack so there is no way to modify the data without binding to system / user parameters.
* Added console commands (fx.Niagara.Component.ReinitializeActive & fx.Niagara.Component.DeactivateActive) to allow a quick way to kill / restart Niagara components.

  + Cleaned up various console variables while I was here.
* Niagara: Properties (Section Start Behavior, Section Evaluate Behavior, Section End Behavior, Age Update Mode, Allow Scalability) in UMovieSceneNiagaraSystemSpawnSection can now be set in Blueprints / Python.
* Multiply the debug draw color by alpha so we can have translucent lines.
* Now send the current bounds to the GPU for the emitter properties DI.

  + This makes the result of GetBounds consistent between both paths when using fixed bounds on the emitter.
* Removed stateless emitters from compilation.

  + Previously they would still generate some HLSL data resulting in compilation when added / removed.
  + Cleaned up several areas that assumed Emitter Data would always be valid.
* Made renderer memory savings by reducing FNiagaraVariableAttributeBinding.

  + Sprites 1992 -> 1320 = 672
  + Mesh 1688 -> 1160 = 528
  + Ribbon 1888 -> 1312 = 576
  + Light 800 -> 560 = 240
* Added a rule for validating material usage in renderers.

  + This makes it possible to block content that does not have the appropriate usage flags set.
* Niagara Content:

  + Added a new dynamic input to support querying values from the new Weighted Distribution Int Array data interface.
  + Added new modules for spawning particles from simulation caches.
* Removed all the async optimize / decompression of VM byte code.

  + The new VM does not use this path so the code is dead.
* Enabled Sub UV cutouts ES3.1.
* Can now use the Niagara Data Interface to set material parameters on Material Instance Dynamic objects, from a CPU stage.
* CascadeToNiagaraConverter: Add more script input types.
* Added Shift+D to enable selected emitters (reverse of D which disables selected emitters).
* Refactored renderer widgets to share code and use small chip
* Added a menu entry when we have no stateless bindings to make it clear to the user what type we are looking for.
* Added a debug draw to renderers.

  + Implemented debug draw for light & decal renderer.
* Added column sorting to sim cache viewer.

  + Also cleaned up how we build the table data to make it less confusing.

**Bug Fix:**

* Fixed issue where ParticleSystem EPSUM\_FixedTime had no effect due to incorrect assignment.
* Fixed validation accidentally changing usage with flags on materials.

  + CheckMaterialUsage will both check and set which can result in a race with shader compilation.
* Use the component transform for local space vs the simulation one - When disabling requires current frame data (for performance) these could be out of sync, which mismatches other renderers on the RT (i.e. sprites & meshes)
* Fixed hash function in data channel to use full string data instead of just half of it.
* LWE: Set the sim target on the compiled data set to match the mode.

  + This fixes a mismatch that can cause attributes to not upload to the GPU when we are in CPU mode due to using the light / decal renderer.
* No longer call the OnSystemFinished delegate if we are constructing Blueprints.

  + The delegate might interfere with the actor / components and can cause crashes.
* Shader loading: Now prevent dereferencing potential nullptr when file is not found.
* Fixed emitter renderer tick ordering issue when combined with LWE.
* Added missing postload calls for stateless emitters.
* Guarded against using EmitterData as it can be nullptr.
* Fixed binding buffer changes causing dispatches to serialize on some RHIs.
* Fixed potential OOB reads if a binding is invalid.
* Added a lock to GPU Sort Manager AddTask to ensure no concurrent access.

  + This fixes a race between Niagara & Cascade adding tasks.
* Now calculate spawn probability per particle for spawn rate, rather than per loop.
* Fixed user variables being removed and renderers not updating correctly.

  + The variable was without namespace so failed to match.
* Added a missing null check for the graph source that can happen during undo.
* Fixed GetResourceSizeEx miscalculating for non-isotropic UTextureRenderTargetVolume.
* Niagara component renderer: now only register one object replacement delegate with the CDO to prevent races during asset loading.
* Added missing CanBind to user parameters.

  + Changed style of binding to be more consistent with other bindings.
* Now sets the world time information in the baker.

  + This fixes things like Engine.Time always being 0.0 and material based time effects not working as expected.
* Used GroupMemoryBarrierWithGroupSync with Radix Sort to fix issues on various GPUs.
* No longer load niagara system when getting asset registry tags, to prevent deadlocks during emitter merging.
* Disabled low latency when anything other than the lit view mode is active.

  + Some of the view modes short circuit rendering so the data may not be ready in time.
* Fixed a crash when copying script variable metadata.
* Handled null data interface inside Niagara Variant.

  + It is unclear how the variant DI becomes nullptr at the moment, this will at least avoid crashing the editor, but more investigation is required to understand why.
* Fixed duplicating an emitter with RunUpdateScript set for interpolation mode changing post duplication to NoInterpolation.
* Fixed single segment GPU ribbon UV calculations being incorrect.
* Fixed a potential use-after-free on world tear down.

  + If the compute interface is marked pending kill we can ignore sending the command to remove from the computer interface as it will be killed before.
* Fixed an asan issue using the component in the lambda.

  + Bring changes over for garbage references also.
* Fixed incorrect stride with FRibbonAccumulationValues when using different features.
* Fixed color curves not working inside NPCs when using GPU emitters.
* When modifying parameters in the detail panel, now use the editor setting GetResetSimulationOnParameterChange to see if we should reset the system or not.

  + Disabling reset can be useful to iterate on content live.
* Fixed editor undo crashing due to order being out of sync and the thumbnails.
* Fixed update context killing systems that are waiting for compilation.

  + When switching preview modes the update context is called multiple times.
  + The first time it's considered active.
  + The next time it's no longer active but is waiting for compilation (compontent ticking) so is now removed from the reactivate list.
  + We now check if the component tick is enabled due to waiting for compilation results.
* When setting up previous data use current if previous does not exist.

  + Current changing to a new position binding which does not have a previous value generated it would use the default position which is 0,0,0. Using the current value won't produce corrupt motion vectors, but will also not produce correct motion vectors.
* Changed default for LOD size Y to -1 to fix issue with meshes being culled incorrectly.

  + A value of -1 indicates that it will never be culled by screen size.
  + The previous value of 2 would be adjusted to 1.0 and fail the >= screen size test if bounds were large enough.
* Now uses the aliased variable when finding the default mode

  + This fixes an issue if the first time a variable was encountered it was in StackContext as we would ignore the binding.
* Fixed a bug where min instead of max distance was used as LoD parameter.

  + Fixed a nullptr and weak ptr bug in error log format.
  + Fixed a bug when an error during script merge occurs.
* Fixed memory leak in data channel object destructor.

#### Path Tracer

**New****:**

* Improved the adaptive sampling heuristic.
* Added an option to hide the planet ground surface.

  + When using reference atmosphere mode, the path tracer no longer displays a large ground sphere to represent the planet for better parity with the deferred renderer.
  + The old behavior of showing the planet ground can be accessed by the cvar r.PathTracing.EnableAtmosphereGround.
* Post-process materials can now be specialized for the path tracer.

  + This adds a permutation of the PostProcess Material that is used when the path tracer is enabled on the view.
  + This can be used to account for differences in how the path tracer creates the image. Behavior can be customized with the PathTracingQualitySwitch node.

**Bug Fix:**

* Improved shadow artifacts in transparent shadows due to double-counting of transparent hits.
* Improved startup time by moving rarely used permutations to experimental.
* Fixed a crash when enabling decal normal projection.

#### Postprocessing

**New:**

* Changed the EOTF for UI composition in HDR from sRGB to BT.1886 for improved parity between SDR and HDR appearance. A new CVar r.HDR.UI.CompositeEOTF was added to provide control over this behavior.
* TSR:

  + Added an option to allow all shading models to use TSR thin geometry detection when r.TSR.ThinGeometryDetection.Coverage.ShadingRange=2.
  + Added exposure offset (r.TSR.ShadingRejection.ExposureOffset) back so global darkening ghosting can be improved. The value behaves a little differently and is now used to adjust the exposure offset for the reject shading moire luma and guide history. Any legacy project before UE5.5 using the old CVar should consider adjusting the value.
* Updated shader selection logic for CombineLUTs to force compute shader rather than pixel shader if graphics volume rendering is guaranteed, and reduced the size of the dispatch group from 512 threads to 64 threads.

**Bug Fix:**

* Replaced usage of PF\_R32G32B32F with PF\_R32\_FLOAT for the ACES gamut table texture to make the implementation compatible with more platforms.
* Fixed alpha invert show flag on desktop if primary upscale was active.
* Fixed Bloom not working with TSR when motion blur is disabled.

  + Forced the invalidation of the low-res scenecolor for translucency after motion blur pass if motion blur is not run.

#### RHI

**New:**

* AddEnqueueCopyPass can now be used with texture arrays.
* Metal:

  + Refactored bindless to support new FeatureLevel & Platforms and include a per-project experimental Mac option to enable SM5 Bindless.
  + Upgraded Metal Developer Tools from 4.4 to 5.3
* MetalCPP: Upgraded to metal-cpp\_macOS15.2\_iOS18.2

**Bug Fix:**

* Fixed a bug in the PS4 renderer submission queue that delayed signaling occlusion query events.
* Fixed UpdateTexture2D() failure case where the source region has an offset and the texture is block compressed.

#### Substrate

**New:**

* Improved the rough diffuse shading model to minimize energy loss and improve the shaping at high roughness.
* Improved legacy conversion of cloth materials.

  + The roughness range of cloth has been adjusted for better parity with the legacy cloth BRDF.
  + The specular amount is now automatically adjusted to account for the Fuzz layer being added on top of specular in Substrate whereas it was linearly blended in the legacy model.
* Removed r.SubstrateBackCompatibility as we now rely on the Substrate Rough Diffuse option to drive that instead.
* Set Blendable GBuffer format as default for new projects. Some archvis and automotive project templates are set to Adaptive GBuffer format by default.

**Bug Fix:**

* Fixed most material properties not being added to FMaterialData::PropertySizes when baking Substrate materials on the Actor Merge -> Simplify path.

### Simulation

#### Chaos Visual Debugger

**New:**

* Improved batching of TEDS operations performed when new physics body data is loaded in the scene. This change, combined with some other improvements made in TEDS itself, resulted in ~75% reduction in the processing time when the first frame of a large CVD recording (+90.000 objects) is loaded. The stall in this particular case went down from ~12 seconds to ~3 seconds.
* Added support to enable CVD recordings in Shipping configurations.
* Added a new pop up notification to provide a cleared indication of when CVD is still processing trace data for a loaded file.
* Added a non-blocking loading bar. This bar will appear in the status bar to indicate the loading process of very large CVD files.
* Added initial experimental support for tracing smaller sections of a map instead of the entire map.

  + This can be configured from code with the CVD\_SET\_RELEVANCY\_VOLUME macro or via Blueprint with the CVD Set Trace Relevancy Volume node.
  + Note: If a recorded body moves to outside the recorded volume, CVD will show that body frozen in time. This will be addressed in the next release.
* Implemented the new view port toolbar the rest of the editor uses.
* Extension System:

  + Added support for attaching custom data to the CVD Recording instance.
  + Added support for implementing 2D visualizations via CVD's component visualizer API
* Improved tracing performance by removing the need for locks (and reduced the contention of ones we could not remove) in some heavily multi threaded paths. Mostly in collision geometry and physics body metadata serialization paths.
* Removed connection details from the Recording status message, and moved it to its own message which is sent when needed. This reduces the message bus bandwidth usage when a CVD recording is active.

**Bug Fix:**

* Added missing serialization for FChaosVDParticleDynamicMisc::MLinearEtherDrag.
* Added missing serialization for FChaosVDParticleDynamicMisc::MSleepThresholdMultiplier
* Added missing serialization for FChaosVDParticleDynamicMisc::MCollisionConstraintFlag.
* Fixed an issue where attempting to trace multiple processes at the same time could fail to playback, even if the recording was successfully started.
* Fixed a race condition when a CVD recording is started at the same time or right before PIE is started, resulting in a crash.
* Fixed an issue where CVD's sessions manager broadcasts a session discovery ping every second, even if CVD is not open in the editor.
* Fixed incorrect visualization of per particle position/velocity/projection iteration counts.

  + Moved iteration counts to FChaosVDParticleDynamicsMisc and added serialization version guards accordingly.
* Fixed an issue where trying to load the same CVD recording twice caused an ensure, and failed.
* Fixed an issue where the first frame of a recording was not automatically loaded in some scenarios, resulting in an empty scene until you scrubbed to a new frame or started playback.
* Fixed an edge case where the recording controls UI could get soft locked, blocking you from stopping a recording that was just started.
* Fixed an issue where QueryData was used instead of SimData, in the details customization used for Collision Geometry details panels.
* Fixed an error where the Network Tick sync mode was not clamping the track tick offsets to the supported limits in some scenarios.
* Fixed an issue where recorded destroyed particles were not being properly removed from the scene.
* Fixed a crash that could happen if you play a CVD recording while it is still loading.

#### Cloth

**New:**

* Added a ReferenceSpace local damping option to Chaos Cloth. This enables local damping about the reference space bone instead of the existing center of mass option.
* Updated ChaosClothAsset and ChaosOutFitAsset to use SoftObjectPaths internally to better handle renamed dependent assets such as the Physics Asset.
* Updated Chaos Cloth to internally use FNames instead of FStrings for properties. This fixes a long-standing performance regression when setting simulation properties at runtime via the cloth blueprint interactor.
* Added the ability to specify the ReferenceBone for a cloth asset.
* Added additional accessory meshes for chaos cloth.

  + Updated the backstop constraint to be able to use this accessory mesh.
  + This feature is considered experimental.
* Cloth Remesh Node: Can now transfer vertex weight layers to output cloth render mesh.
* Updated Chaos Cloth and Skeletal Mesh-based cloth to better handle non-simulating LODs.

  + Fixed a bug where chaos cloth could stop simulating if there was a non-simulating LOD sandwiched between two simulating LODs.
  + Updated Skeletal Mesh-based cloth to no longer tick cloth for non-simulating LODs when cloth is present on other LODs.
* Chaos cloth debug draw improvements: Added wind velocity and updated gravity display.

**Bug Fix:**

* Fixed an editor crash which could occur when remeshing a chaos cloth asset with Long Range Constraints.
* Fixed issues with Kinematic Collider and Skinned Triangle Mesh, these were regressions from implementing Skinned Triangle Meshes in Chaos Cloth in the last release.

  + Kinematic Collider was using previous frame's positions for its constraint Apply causing it to lag behind and not fully resolve collisions.
  + Kinematic Collider debug draw was broken due to an indexing bug.
  + Added ClothCollisionThickness parameter on the SimulationCollisionConfigNode was not setting the correct string, so it wasn't being used.
  + This fix for this will not affect existing assets (ClothCollisionThickness will be set back to 0 to retain existing behavior).
* Cloth Render Node: Now populate all UV Channels for output.
* Fixed CorrespondClothAssetIndex never set in BindToSkeletalMesh, since checks are stripped out in Shipping.
* Cloth Remesh Node: use the DynamicMesh UV layers to determine how many UV channels should be on each render vertex in the output ClothCollection (so that we don't accidentally add 4 channels when the input only has 1, for example).

#### Core Physics

**New:**

* Partial Island Sleep:

  + Added a console command to enable partial island waking when the user explicitly manipulates the transform of a rigid body ("p.Chaos.Solver.Sleep.PartialIslandSleep.PartialWakePreIntegration").
  + Added a console command to enable rigid body waking based on the velocity change introduced by the velocity collision solver ("p.Chaos.Solver.Sleep.PartialIslandSleep.PostStepWakeThreshold").
  + Added a console command to restrict partial island sleep to collision constraints only, i.e. rigid bodies connected by other constraint types will have to be both awake or asleep ("p.Chaos.Solver.Sleep.PartialIslandSleep.CollisionConstraintsOnly").
  + Added console command to enable the propagation of impact momentum though the physics constraints to determine with the purpose of waking rigid bodies in partially sleeping islands ("p.Chaos.Solver.Sleep.PartialIslandSleep.MomentumPropagation").
  + Introduced a Blueprint event to enable or disable partial island sleep for the entire island a rigid body is in ("Set Allow Partial Island Sleep").
  + Improved performance by limiting partial island waking to scenarios with any sleeping rigid bodies.
  + Added a console command to only enable partial island sleep if the decimal percentage of motionless rigid bodies is above a user-defined threshold ("p.Chaos.Solver.Sleep.PartialIslandSleep.MinimumMotionlessRatio").
* Added generic AddElem function for AggGeom and helpers to access the correct containers based on input element type.
* Added SetUseMinTimestep function in Immediate Physics API.

  + This makes it possible to avoid switching to a fixed timestep when the delta time is small, bypassing the cvar p.Chaos.ImmPhys.MinStepTime
* Added a new p.Chaos.MinParallelTaskSize cvar and CVarMinParallelTaskSize function to set a threshold of tasks to run in parallel, which can improve performance on low-core platforms.
* Enabled some p.Chaos cvars (like p.Chaos.MaxNumWorkers) in Shipping so they can be used to tweak game-specific performance.
* Enable some physics cvars (like p.Chaos.MaxNumWorkers) in Shipping so they can be used to tweak game-specific performance.
* Added support for setting CollisionEnabled per ISM body.
* Exposed functions for calculating covariance matrix of a set of points and retrieving the dominant eigenvector.
* Added a per poly collision setter function to SkeletalMeshComponent.
* Moved several shapes from Chaos to ChaosCore.
* Added an option to treat default as simulated for RBAN.

**Bug Fix:**

* Enforced drive linear force limits when non-linear joint solve is enabled.
* Fixed SphereTraceComponent not returning the hit FaceIndex when tracing against complex shapes.
* Fixed an issue where AddForce related methods did not generate wake events in some scenarios.
* Now detect and remove null constraints from CCD swept constraints prior to application.
* Fixed collision behavior when converting from probe to nonprobe.
* Optimized allocation in cable mesh building
* Chaos: Fixed wrong rotation axis when using simd for linear joint solver.
* Fixed an occasional crash when unwelding rigid bodies.
* Fixed a physics bug where unwelding via socket name failed to unweld. This could lead to a crash when the parent body was destroyed and a query was performed against the child.
* Fixed FKShapeElem copy constructor accidentally changing the CollisionEnabled flag instead of copying it.

#### Dataflow

**New:**

* Double clicking on a Dataflow variable now finds the related nodes in the Dataflow graph and sub-graphs.
* Dataflow construction views are now generally more performant for large meshes and allow render data caching.
* Added transform support to dataflow rendering geometry groups.
* Added capsule rendering support to the rendering facade.
* Updated the weight map tool in dataflow to more closely match the UI of existing painting tools.
* Dynamic mesh processor blueprint can now optionally specify that it is ok to run async.
* It is now possible to edit some of the bool / int / float non-connected input parameters inline on Dataflow nodes.
* Added a 'Cut Planes' array input to the PlaneCutter dataflow node, to support directly specifying the cutting plane(s).
* The Geometry Script based Dataflow node now exposes the Geometry script parameters out to the Dataflow node as connectable inputs.
* Added general array Dataflow nodes for getting an element or reading the size of an array.
* Dataflow can now automatically add a node to auto convert from an output type to an input type.
* Added an option for dataflow FilterPointsWithMesh node to filter by mesh min/max distances in addition to inside/outside winding number test.
* Added a general dataflow selection -> index array conversion node (so that e.g. one can iterate the selected indices).
* Added support for root proxies for Dataflow based Geometry Collection asset.
* Enabled construction view rendering for most of the geometry collection Dataflow nodes.
* Added a generic version of the math Clamp dataflow node.
* Dataflow variable nodes can now be used directly in Subgraphs.
* Added the possibility to promote a dataflow input to a variable ( right click menu ).
* Geometry Script based dataflow nodes will now open the Geometry Script blueprint when double clicked on.
* Dataflow now show an array pin icon for array types.
* Added a Dataflow node to set a string transform attribute and to select from a string pattern.
* Added dataflow nodes for conversion from an index or index array to a dataflow selection.
* Support "Only Same Parent" option for TinyGeo "Merge Geometry" mode (and corresponding dataflow node).
* Added Dataflow nodes for getting bounds from static mesh and dynamic meshes.
* Added support for setting up root proxies in Dataflow.
* Added a Dataflow node to set the dynamic state of geometry collection bones.
* Updated the Dataflow Editor to better handle Save As by reconnecting the newly created derived assets (e.g., Dataflow Asset) to the main asset.
* Added display of performance data for Dataflow subgraphs.
* Optimized the Dataflow collection spreadsheet ( up to 25x for large collections ).
* Added Box, Capsule and Convex simple builders as geometry generators for dataflow physics assets.
* Added support for manipulating bones from the Dataflow Edit Skin Weight tool.
* Added Fov and planes options to the view menu in both Dataflow simulation and construction views.

**Bug Fix:**

* Fixed crashes due to incorrect selection init for some dataflow fracture nodes.
* Expanded out fracture brick pattern bounds by a half-brick, to fix bricks not quite covering the intended bounds in many cases.
* Made the collection->mesh dataflow node take an optional selection and perform the conversion more consistently with the collection selection->meshes dataflow node.
* Changed the dataflow 'show/hide inputs' menu to use the localized display names instead of the internal source code names.
* Add correct struct handling to dataflow context cache to support nested UObject references.
* Made blueprint dataflow nodes default to evaluate on the game thread, for safety.
* Added guards against selecting invalid indices. Now returns false instead of crashing on attempting to set an invalid selection.
* Fixed Dataflow graph not re-evaluating when switching from manual to automatic evaluation mode.
* Made sure Dataflow nodes performance data is recorded per node even when the data is not shown on screen.
* Fixed the Dataflow Selection by Level Node to make sure the level attribute exists in the collection.
* Fixed "append collections" dataflow node not updating transform indices correctly.
* Fixed array support for Dataflow subgraph inputs and outputs.

#### Fluids / Smoke

**New:**

* Added default drag for accurate integration.
* Added support for landscape proxies.
* Drag model updated buoyancy tests make sure physics assets for rafts computes mass with the correct material.
* Added water, spray, foam shading improvements, translucent spray particles
* Refactored capture modules in sw emitters to handle overhangs in terrain with better controls rework summary views.

**Bug Fix:**

* Fixed spike artifacts by only advecting to wet cells. This can avoid issues where we advect into steep areas that we shouldn't be.

#### General Physics

**New:**

* Added a way to reset the state of a geometry collection (from Blueprint or live from the editor with a button in the component details).
* Added the ability to incrementally create new cache collection assets each time a Chaos cache records.
* Exposed Chaos cache observed component functions to Blueprints.
* Geometry collections can now be converted to Skeletal meshes (right click on the asset or in Dataflow).
* Added a way to start and stop a Chaos Cache from Blueprint.
* Added API for generic sweep traces (Sphere, Boxt, Capsule and Raycast) on the physics thread.
* It is now possible to query a geometry collection leaf bone using a line trace from Blueprints (FindLeafTransformByLineTrace).
* Added asset user data support to physics assets.
* Added support for override materials for geometry collection root proxies.

**Bug Fix:**

* Creating a Chaos cache from the main menu can now be undone.
* Fixed Chaos cache not recording events properly after the cache was recorded once.
* Fixed Chaos cache not properly replaying simulations of geometry collection using root proxies.
* Geometry collections with no materials are now assigned a default material. This prevents issues where the geometry collection may have weird rendering artefacts.
* Fixed spawned geometry collections not properly using the physical material set on the asset.
* Fixed a crash in the geometry collection SetLocalRestTransforms method happening when the rest of the collection is empty.
* Fixed Chaos Niagara interface not playing trailing events properly.
* Fixed Nanite based geometry collection not replaying properly from a Chaos cache.
* Fixed geometry collections not properly waking up when applying velocity.
* Fixed force based local fields not working properly when applied to a geometry collection.
* Made sure gravity settings are propagated to cluster unions or cluster group unions.
* Fixed geometry collection anchored and other attributes being stripped when using strip on cook on Nanite based geometry collection.
* Fixed Chaos cache not properly restoring Simulate Physics or notify break flags when deleted or when removing an observed component.
* Fixed geometry collection local field not properly working with partial clusters when using minimal resolution.
* Fixed an issue with geometry collection Nanite fallbacks not rendering when enabled and when Nanite is disabled in editor.

#### Modular Vehicles

**New:**

* Added an additional input quantization mechanism.

#### Networked Physics

**New:**

* Made improvements to how and when RewindData caches physics states along with fixes for KinematicTarget resimulation.
* Optimized NetworkPhysicsSettings memory footprint from padding and alignment.
* Added a NetworkPhysicsSettingsDataAsset and converted the NetworkPhysicsSettingsComponent to reference the DataAsset instead of holding all settings in memory for each actor instance.
* Added the first iteration of Iris support in the NetworkPhysicsComponent with a new base struct for inputs and states along with a new interface for custom implementations to communicate with the NetworkPhysicsComponent.
* Scheduled Physics Thread command lambdas with resimulation handling.
* Added new settings and features to balance simulated proxies and post-resimulation corrections.

  + Option to trigger a resim when receiving new inputs.
  + Option to apply input decay curve over a set time instead of over the remaining resim frames.
  + Option to decay post-resim error in render interpolation exponentially, with a half-life setting.

**Bug Fix:**

* Fixed an issue where inputs can get dropped when the server input-buffer runs empty because only the latest received input gets injected at the front of the buffer.
* Fixed an issue where input wouldn't be produced for locally controlled pawns not using a player controller.
* Fixed Geometry Collection and Cluster Union post-resimulation render interpolation issues with stuttering and rotational calculation.
* Added fixes for inputs getting lost.

### Tools

#### BuildGraph

**New:**

* Added the Boolean attribute ReportOnExecution to report diagnostics during execution of a step. The name list attribute ReportOnNodes is used to limit which nodes will report diagnostics during execution.

#### UnrealGameSync

**Bug Fix:**

* Fixed an issue where Update Settings would fallback to Horde when changing theme even though Perforce was previously selected.

### Virtual Production

#### Compositing

**New:**

* Marked HoldoutComposite plugin as hidden, since it was deprecated & renamed to CompositeCore.
* Changed the default Lens Distortion rendering mode of the Lens Component to use the Lens Distortion Scene View Extension.

#### nDisplay

**New:**

* Removed a dependency on legacy Composure.

**Bug Fix:**

* Improved stage geometry mesh generation to mitigate deformities when geometry edges are near the mesh equator.
* Fixed an issue where the ICVFX window would throw a failed assert when -rhivalidation was used.

#### Performance Capture

**New:**

* LiveLink:

  + Added a LiveLink Broadcast Component. This component currently allows streaming LiveLink data for Transform, Camera, and Skeletal Mesh data. Adding a broadcast component will create a LiveLink subject that automatically rebroadcasts data from the component.
  + You can now synchronize a Virtual Subject rebroadcast to one of its subjects.You can enable this through the "Sync Subject" option on Virtual Subjects.
* Live Link Hub:

  + Added a playback mode, which is a compact view of the playback widget. Keyboard Shortcuts for Recording Playback

    - Left / Backspace: Step back one frame (hold to scrub backward).
    - Right: Step forward one frame (hold to scrub forward)
    - Space / Enter: Toggle pause Added a "Select Recording" button when no recording is selected, which opens a pop up window with the recording list.
  + Added support for config autosave.
  + Refactored the discovery mechanism to enable seeing all clients without connecting to them automatically.
  + Added a crash recovery mechanism that attempts to restore the last autosave after launching following a crash.

    - Note: When launching multiple Live Link Hub instances, this system will only allow crash recovery for the first session that was launched.
  + Added Client filtering and filter presets support.
  + Added more information to the discovered clients list (IP, Hostname, Project, Level).
* Aja: Updated Aja SDK to 17.5.0
* Users can now choose what class of prop component to use. Default is the native version but users can override with their own derived class for uses such as building custom constraint behaviours.
* Added a delegate to emit when a Live Link subject's bool bIsEnabled is modified. Required for Performance Capture workflow to respond to subjects being modified in the Live Link client panel.
* Removed Mocap Manager requiring all spawned characters to be a ACaptureCharacter actor. All ASkeletalMeshActor classes can now be set to the CaptureCharacterClass property in a PCapCharacterDataAsset.
* Changed CaptureCharacterClass member type in UPCapCharacterDataAsset from TSoftClassPtr to TSoftClassPtr.
* Relocated the Performance Capture properties under a 'Performance Capture' details category for ACaptureCharacter actors.
* Improved PIE/SIE usability of the stage manager and the outliner.

  + Cleaned up unused nodes in mocap manager EW.
* Refactor of LiveLink data pausing:

  + Moved all calls from the individual actor components (performer, prop, retarget) to simple pausing the LiveLink data on the LiveLink client.
  + Subjects that are paused can still be recorded in Mocap Recorder.
  + Pausing a subject will update the pause state in the UI in all locations.
  + Subjects that go invalid will no longer be removed from Record Manager. Only subjects that are disabled (requires UI interaction with Live Link panel to accomplish) will be disabled from being recorded.
  + Removed tracking what's paused and what's enabled from the LiveLinkEval struct and renamed to LiveLinkVisual. The array of this struct in the viewmodel now only keeps track of what subjects are being visualised.
  + All calls to determine a subject's state or enablement go to the Live Link Blueprint function library functions.
* Introduced the functionality to calculate a dynamic prop offset via Blueprint native function (dynamic constraint).

  + Added Function library to query IK Rig and Retargeter properties at run time for calculating dynamic constraint.
  + Improved handling of spawning custom props actors from the PCap Prop data asset.
* Added runtime module for -game sessions.

  + Refactored actor, actor component and animinstance classes into new runtime module to enable running tools/actors in -game session.
  + Added redirectors to new class locations.
* Updated plugin description to aid discoverability in the plugin browser by including text referring to Mocap Manager.
* Enabled Mocap Manager retarget tuner and prop offset widgets to run in PIE/SIE.
* Added F keyboard binding to focus on Pcap UMG viewport actor.
* Mocap Manager Viewmodel now caches the initial state of Take Recorder settings and reverts them to the initial state when closing Mocap Manager.

  + Users can now select a folder for their PCap data.
  + Can now be a Content Plugin path or a game content path.
  + Now creates a session template per project as part of the first-run workflow, removing dependency away from Engine/Plugin content.
  + The session template is now unique per uproject.
* Did a full pass on all Blueprints, setting namespace to PerformanceCapture on all assets, to prevent functions leaking into the function palette when they're not wanted.

  + Added Hide actor in-game button to outliner, only visible during a multi user session.
* Added missing delegate for when a Live Link subject is added.

  + This is needed for Virtual Subjects.
  + Added OnLiveLinkSubjectAdded delete to the PerformanceCaptureSubsystem.
* Now remove illegal characters from the filename of created Skelmesh when using Live Link subject name as the basis for the new asset's name.
* Improved scaled performer mesh workflow:

  + Now uses poseable mesh component to shuttle live link transforms to the new skelmesh.
  + Added ability for user to a freeze the pelvis bone above the origin.
  + Added bone picker so users can choose which bones is the pelvis
  + Auto find the pelvis bone function executed on invoking the panel.
  + Warning if the bones in the given skelmesh do not match the Live Link data.
* Modified the bone visualizer to work with any actor containing at least one skinnned mesh component. Always defaults to the first found skinned mesh.
* Removed pausing/unpausing of render in the main level viewport when starting the custom UMG viewport. This was negatively impacting prop line up workflows when the user wants to use both viewports.
* Added exclusion list of components to the Take Recorder permission list User Asset data object and a function to audit a Take Recorded actor's components in the motion actor row of Mocap Recorder.

  + Users can now filter recording on component names.

**Bug Fix:**

* LiveLink: Added multi-select for subjects, so you can pause multiple subjects at once.
* Live Link Hub:

  + Added a column that displays the translated role for a subject (hidden by default).
  + Fixed Live Link Hub resetting timecode and genlock upon exiting, even if these options were not enabled in the Hub.
  + Can now pick an interpolation processor if transmitting evaluated data is enabled.
  + Pause subjects when pausing a recording so they appear as valid on UE clients. Dragging the playback slider will no longer pause recording on end if the recording wasn't paused.
  + Added a prompt to verify if the user intends to close the hub before closing.

    - You can turn off this behavior by changing the "Confirm Close" option in the LiveLinkHub settings.
  + Fixed a crash when launching a game in shipping configuration with Live Link Hub plugin enabled.
* Fixed potential Multiuser crash caused by emitting change to take recorder metadata during recording. Emit is now gated behind bIsRecording=false.
* Retarget character mesh will now tick and update pose on the same frame as the perforrmer source mesh.
* Prevented base mocap mesh getting set to null after creating a performer.
* Prevented character name getting set to null when creating a character data asset.
* Prevented pre-requisite cycle when SourceMesh == ControlledMesh because FComponentReference wants to set default to first skelmesh component on the owning actor.
* Fixed crash in Performer mesh creation if the chosen skelmesh has no valid skeleton assigned.
* Fixed session missing message after first-run creating the base PCap datatables.
* Fixed Motion outliner UI getting invalid information from the level when assets have been deleted which the mocap actors reference.
* Fixed bug with mesh visualizer in Performer mesh workflow not clearing the mesh from the viewport.
* Fixed bug where Live Link recording subjects aren't refreshed when subjects are removed from the record manager.
* Fixed a bug in the Mocap Manager picker widget preventing excessive calls to the asset registry during Take recording.

**Deprecated**

* Deprecated the SourcePerformer, RetargetAsset and bForceAllSkeletalMeshesToFollowLeader properties on ACaptureCharacter in favor of the same properties on URetargetComponent.
* Deprecated the AdditionalMeshes property on UPCapCharacterDataAsset.

#### Rendering

**New:**

* Exposed linear versions of the UE emulation color spaces in OpenColorIO plugin config, useful for tonecurve inversion for example.
* Fixed lens distortion material default support for packaged games.

#### Tools

**New:**

* Live Link Hub:

  + Store external plugin paths in a versioned directory that reflects the plugin ABI (e.g. "%LocalAppData%\UnrealEngine\LiveLinkHub\_5.7"). Outside of an installed build, the workspace Engine/Config directory is used instead.
  + Added "auxiliary channel" endpoint negotiation. It's now possible to register a channel type handler with ILiveLinkHubMessagingModule, and initiate a channel request to a known client using ILiveLinkHubClientsModel.
  + Fixed not properly replaying tracks that had inconsistent framerate or data.

    - A track's timestamps are now always used when seeking to frames across tracks rather than only relying on qualified frame time conversions. For efficiency we still convert the desired frame time to a track's local frame time first which often puts as at or near the desired frame.
    - Timestamps are now saved and loaded in bulk, rather than with each frame. For old recordings the file is iterated once to load the timestamps, which can be slow.
    - Added an Upgrade feature which will force load the entire recording into memory and then save it to a new file, providing users a way to convert old animations to the new format, and decrease future load times. The recording list will now specify if a version is outdated or not. If a recording is outdated a context menu option "Upgrade Recording" will be available.
    - Fixed multiple event fires when committing a scrubber change via spin boxes.
    - Fixed a crash when exiting the app while streaming frames.
* Added extendable data for Productions.

  + User defined UStructs can be registered as extended data types and are displayed in the Production Wizard.
  + This data is saved with each Production in the default engine configuration file (Engine.ini).
  + User defined customizations can be registered for the Production Wizard for registered extended data types.
  + User defined 'User Settings' tabs can be registered to the Production Wizard.
* Added a Tracking Alignment Tool into the Camera Calibration plugin. This tool aligns two tracking spaces together by calculating the aligned origin transform of one of the tracking spaces.
* Remote Control:

  + Made behaviors rearrangeable in the RC panel.
  + Added Select Source button to the action list

    - Also added icon to right click on exposed property right click menu.
  + Changed "in use" visualisation for properties to a background color similar to selection.
  + Added indication of whether a property is bound to a controller.
  + Added support for enums and additional struct types.
  + "Fill path from selected asset" now looks for selected exposed properties if there are no assets selected.
  + Added a stateless controller button.
  + Revamped path behavior.
  + Added the "controller"  category .
  + Changed entity bind numbers over to runtime objects.
  + You can now select bound action sources.
* Switchboard:

  + Updated the BP OSCListener to use the TR subsystem in all functions. Now all calls to get take metadata use the Subsystem so it can be used without take recorder being open (Mocap Manager)
  + Start and stop recording now uses the subsystem and will open a level sequence by default to keep the behaviour the same as previous when triggering start record from SB.
  + Removed some debug prints that snuck in during the dev process that don't help the end-user.
  + Added an experimental "Use Fast Sync" option to Source Control Settings.

    - This enables incremental sync functionality in sbl\_helper.py.
    - In the case where the currently synced changelist is known, and we are syncing ahead to a future changelist, we can pass a revision range to the Perforce commands involved in order to achieve a potentially dramatic speedup (reductions from >3 minutes to <30 seconds were observed in large projects internally).
  + Perforce changelist dropdown refresh now occurs asynchronously, avoiding attendant UI hitches/hangs for long-running Perforce operations.
  + sbl\_helper.py now explicitly maintains workspace sync state in JSON files in the engine/project directories; this is more reliable than the previous mechanism which relied on `p4 cstat ...#have`.

    - Additionally, if the workspace is "dirty," this will be indicated by an asterisk next to the changelist indicators in Switchboard.
  + Added a button to the progress dialog to interrupt population / refresh of the asset cache, which can take a long time in large projects.
  + Can now pass command line arguments to specify the Unreal Editor OSC server address and port.
  + Added a setting to optionally the Live Link Hub device to suppress the crash recovery dialog following an unclean shutdown.
* Take Recorder:

  + Root cinematics path can now refer to both content and plugin content.
  + Made Take Recorder Source types public. Sources that weren't already exported now are. This is for consistency since all sources were previously exposed to Blueprints.
  + Fixed custom time dilation failing when bStartAtCurrentTimecode is true and sequencer is disabled.
* Added a command line flag to bypass source control checks when joining a Multi-user session. The new command line arg is -CONCERTSKIPSOURCECONTROLCHECKS.
* Motion Design:

  + Text3D:

    - Hid the Text3DCharacterTransform from the "add component" list to avoid being added to the new Text3D.
    - The UText3DLayoutTransformEffect is the new approach to handle per character transform, and keep components to migrate properties to newer systems.
    - Adding LocationBegin in LayoutTransformEffect to adjust starting offset.
    - Recycle components instead of creating/destroying using a pool.
    - Components and renderer are no longer transient.
    - Reduced number of components needed by 2
    - Suppressed material & mesh warning when using Text3DComponent in a Blueprint.
    - Added effects section for text (layout effects) in Details panel.
    - Reworked the default text transform extension effect to support ease curve.
  + Fixed the mask material function to work fully in local space without continuous updates to adjust itself.
  + Added missing Blueprint functions to retrieve text extensions.
  + Now uses a single custom material for front, back, extrude, bevel slots.
* Naming Tokens:

  + Now supports case-insensitive namespace lookup. bForceCaseSensitive is now recognized for namespaces to force case-sensitive checks.

    - Registering namespaces is unchanged, and still requires a unique name regardless of case.
  + Added Naming Tokens Editable Text Box UMG widget for displaying token text, both as raw tokens and resolved tokens. This wraps a new slate version: SNamingTokensEditableTextBox.

    - The default behavior allows you to type in text with {tokens} through NamingTokens that are automatically resolved when committing the text.
    - An autocomplete suggestion dropdown is included which allows you to search for namespaces and tokens and automatically insert them into the text box.
  + Added EvaluateTokenList API to evaluate specific tokens and return their evaluation data.
  + Added the TokenNamespace field to FNamingTokenValueData so the namespace is always returned.
  + Added a CombineNamespaceAndTokenKey utility function in case the key and namespace need to be recombined.
* Added support for specifying additional mount points via the command line for the storm sync plugin.
* SwitchboardListener: Enabled separate handling of stdout and stderr streams.
* Template Level Sequences or Cine Assemblies can now be set for assembly and sub-assembly construction through the Cine Assembly Schema 'Content Hierarchy' tab.
* Using the take recording feature, you can now capture microphone audio sources on -game clients.
* Created a new stat category for the Take Recorder and its sources. This allows users to see what sources are assigned on a -game client.
* CineAssembly

  + Added Productions level toolbar to change the active production.
  + Added naming token support in Cine Assembly Schema metadata String fields.
  + Added Python functionality to access and set the author property of a CineAssembly(get\_author, set\_author).
  + Added Blueprint functionality to access and set the author property of a CineAssembly (GetAuthor, SetAuthor)
  + Added Python functionality to access the created data and time of a CineAssembly (get\_created\_string, get\_date\_created\_string, get\_time\_created\_string).
  + Added Blueprint functionality to access the created data and time of a CineAssembly (GetCreatedString, GetDateCreatedString, GetTimeCreatedString).
  + Added a new token to access a CineAssembly's author property ({author}).
  + Added a new token to access a CineAssembly's created date and time ({created}, {dateCreated}, {timeCreated}).
  + Exposed the author property of a CineAssembly at creation time in the CineAssembly creation window details.
  + Added a new property (bIsDataOnly) to Cine Assembly Schema's and Cine Assemblies to set schemas and assemblies as data only.
  + Data Only CineAssemblies now cannot be added as SubSequences to other Sequences or Assemblies.
* SubSequence compatibility with a parent sequence is checked by two new optional virtual functions on UMovieSceneSequence (IsCompatibleSubSequence, IsCompatibleAsSubSequence).
* Added a Shot Duplication tool to the Cinematic Assembly Tools plugin, featuring configurable options for duplicating the subsequences of a Cinematic Assembly asset.
* Added a new asset content menu entry widget to set the favourite rating of a Level Sequence or Cine Assembly.
* Added a widget to the 'Edit Properties' window of a Level Sequence and Cine Assembly to set the favorite rating.
* Added display of the favorite rating of a Level Sequence or Cine Assembly in their Content Browser asset tooltips.
* Removed reflect visibility in-game cvar for users. A new workflow is supported in the level editor where users have more explicit control over level visibility.
* When recording multiple clients in Take Recorder, we recommend that you disable remote sequencer open. An error is now displayed to enforce this condition.

**Bug Fix:**

* Fixed Remote Control Interception on function calls with constant reference parameters.
* Take Recorder:

  + Fixed not applying time dilation when Sequencer was closed.
  + Now transacts when removing a source from the subsystem, fixing MultiUser usage.
  + Fixed OnStopped event not firing in subsystem.
  + Fixed recording over an existing level sequence crashing when using the Take Recorder subsystem.
  + ActorRecordingSettings no longer creates settings objects in the constructor, improving struct validation times.
  + Fixed Take Recorder Subsystem IsReviewing() returning true for a frame when stopping a recording.
  + Fixed GetLastRecordedLevelSequence not returning the last level sequence while reviewing a recording.
  + Fixed a crash when creating a level snapshot in a multi-user session.
* Fixed a crash that occurred when a Cine Assembly Schema was created with a name whose length exceeded path limits.
* Naming Tokens:

  + Evaluation data no longer initializes datetime in the constructor, fixing an issue with CDO stability.
  + Now provides world context by default.
* Motion Design:

  + Text3D:

    - Fixed missing glyph geometry when using some fonts like Antonio, Teko... caused by the code checking if a contour is contained within another only testing a segment instead of the entire polygon or bounding box.
    - Fixed UnrealServer compilation warnings caused by FreeType and HarfBuzz macro redefinition.
    - Fixed dynamic mesh renderer crash when text gets regenerated due to update flags not triggering a complete refresh of the render proxy.
    - Added game ready player collisions for static and dynamic mesh
    - Fixed layout extension to handle RTL text.
    - Adjusted wrapping code for RTL text.
    - Fixed Text3D can be used in packaged builds.
* Switchboard:

  + Included rsync daemon in the job object to ensure it doesn't outlive the Switchboard process.
  + No longer discard keystrokes in the Add Device dialog that would otherwise cause the device name to collide with an existing device.
* SwitchboardListener:

  + Avoided leaking ETW trace sessions via PresentMon invocations in the event of unclean shutdown.
  + Prevented child processes from inheriting unintended handles. Unintentionally leaking various resources into child processes that outlive SBL is suspected to be involved in a multitude of intermittent issues, such as:

    - Inability to bind to the configured listening port when re-launching SBL.
    - NVAPI initialization failures.
    - Network performance degradation and disconnects.
* Updated OSCSwitchboard editor utility object to use new Take Recorder Subsystem events in addition to keeping the legacy TR BP delegate events.
* Mocap Record manager: Added missing calls to emit take and slate changes and to accept an externally called StartRecording event.
* Remote Control:

  + Fixed issues with deleting/renaming groups in the group context menu.
  + Fixed a crash when playing a level in PIE with embedded Remote Control preset and opening another level while PIE is running.
  + Fixed an issue where the Create Camera button would not show up for Cine Assemblies in the Sequencer editor.
  + Fixed a Web Remote Control building issue on Mac where the bin directory added to PATH in the Start script was not absolute causing the subsequent web app scripts to fail.
  + Protocol bindings now correctly mark the preset modified when changing the override mask.
* Fixed issue where the 'Add Actor Track' menu option would not show up for Cine Assembly assets.
* Live Link Hub:

  + Fixed play and reverse button tooltips not updating correctly while in playback.
  + Fixed a freeze when looping large recordings.
  + Fixed a freeze if waiting for frames to buffer where the range required was spread across different tracks, but not within a single track.
  + Fixed a possible freeze when reversing or stopping a recording immediately after looping.
  + Fixed the default selection end time possibly ending early. Recording length now goes by furthest track timestamp, not frame number.
  + Added a delay when scanning the asset registry after a directory change detection to help cases where the file system may still be locking the file after a manual move.

    - Added a recording context option to rescan the recording list manually.
    - Prevent loading or creating a config if the playback session is active.
  + Fixed recordings not always looping.

    - Improved frame time calculation and increased precision.
    - Buffer range reported should no longer report past max frames.
  + Fixed issues when jumping to a specific frame. Waiting for a frame to buffer will now properly validate the frame is ready across all tracks. Fixes several issues:

    - Previously buffered frames that were cached and pending removal would still be considered buffered even if they weren't ready, resulting in the wrong frame being displayed initially.
    - Jumping to a frame that was buffered and ready on one track, but not ready on another track that had inconsistent frames or a faster frame rate would not wait for this track's frame to be ready, displaying the wrong frame.
    - Reversing from the start to end frame, such as from a reverse play loop, would hit one or both of these issues and the animation would not always continue playing correctly.
* UDP Messaging:

  + Fixed an issue when the loopback device was not added to the multicast group; so only the first editor instance launch would receive multicast packets. We now always join the group across all instances so other editor instances can be in the same multicast group.
  + Made multiple reliability improvements to UDP Messaging.
* Fixed Media Plate's Aspect Ratio and Mesh Mode transactions to fix Multi-User operations.
* VR Editor: FVREditorModeManager now explicitly shuts down VR Editor in response to FEditorDelegates::OnEditorPreExit.
* Fixed the Render Grid crashing when passing in an empty string when setting Remote Control values
* Fixed an issue where attaching an actor to the socket of a skinned mesh actor would not transact in Multi-User or reapply the attachment as part of an undo operation.
* Multiuser: Fixed a possible crash when stopping a take record or reverting take changes.
* Capture Manager: Fixed several crashes while aborting take upload.

**Deprecated:**

* Lens Calibration no longer depends on (legacy) Composure, and all features that relied on it have been replicated using internal functionality. Opening lens file assets will no longer add a temporary Composure actor to the level.

### Templates

**New:**

* VR Template:

  + The directional light is now configured to draw shadows on standalone XR platforms. Enabled Single Sample Shadow from Stationary Lights on BP\_Pistol to reduce shadow cost (it's already enabled on all other dynamic actors in the scene).
  + Implemented an example of how Passthrough can be toggled. The option can be found in the hand menu. Note that this native Passthrough solution is currently only available on Meta Quest as the OpenXR runtime must support XR\_EXT\_composition\_layer\_inverted\_alpha.
  + VR Template content has now been moved to be a shared template resource named XRFramework. This enables the VR template content to be used in multiple templates.
  + The mannequin hands are now a shared template resource. We can now use them in multiple XR templates.
  + Renamed Blueprints to match the style guide of new templates
  + Added unique descriptions to all Input Actions and Input Mapping Contexts
* Added the Android Runtime category tag for immersive mode selection. See the OpenXR specifications appendix about the Android runtime category for more information.

**Bug Fix:**

* VR Template:

  + Now prevent VR Spectator inputs if HMD is not enabled. This fixes an issue when trying to use a mouse and keyboard pawn in the VR Template for testing.
  + Grab-logic now works even if MotionControllerSource is changed to non-default (such as Palm).
  + Fixed hand models staying hidden if switching which hand the Pistol was being held with.
  + Rebuilt lighting to get rid of shadow artifacts from Point Lights.
* Collaborative Viewer Template: Fixed default pawn not turning when moving mouse. The template used a Set Mouse Position-function hack which doesn't behave the same as it used to, and input logic had to be updated to not use that function in the same way.

## Upgrade Notes

### Animation

#### Control Rig

**Upgrade Notes:**

* Projects using Control Rig Physics, previously provided by the Physics Control plugin, will now need to enable the Control Rig Physics plugin as well.

#### Runtime

**API Change:**

* Since this code change causes some variables to become unused in a variant of UpdateHistory\_TransformHistory, it is now marked as deprecated.

  + The signature of experimental function UpdateHistory\_WorldSpace has been changed

### Editor

#### Framework

**Upgrade Notes:**

* Previously, the UEdGraphSchema performed asset reference filtering when dropping assets on graphs (but not nodes or pins). This high level assumption doesn't hold up for all types of graphs, for example, some graphs open the asset dropped on them for edit. Since the UEdGraphSchema doesn't have knowledge of what the graph represents, asset reference filtering has moved to the implementation details of the various graphs that support it.

  + Any classes that derive from UEdGraphSchema and implement DroppedAssetsOnNode should perform their own asset reference filtering if dropping an asset on the graph creates a reference from the graph asset to the dropped asset.

#### UI

**API Change:**

* Public access to UFont::CompositeFont is now deprecated.

  + Use UFont::GetCompositeFont() if you want to resolve the FCompositeFont to use at runtime (if any).
  + Use UFont::GetInternalCompositeFont() or UFont::GetMutableInternalCompositeFont() if you need to specifically access/modify UFont::CompositeFont.
* Developers should carefully review their use of GetCachedWidget. If a system depends on the outer wrapped widget being returned, use GetWrappedWidget instead. GetCachedWidget may not always return the wrapped widget as expected.

#### UX

**API Change:**

* The depth bar supports displaying custom widgets that are automatically arranged by depth. This is used in the Level Viewport Client to display selected objects along the depth bar.

  + These features can be disabled with the "r.Editor.ManualOrthoDepth 0" CVar.

### Foundation

#### Build

**Upgrade Notes:**

* For projects overriding UAssetManager's functions GetPackageManagers, ModifyCook, GetPackageCookRule, GetPackageChunkIds, or UpdateManagementDatabase, there is now an additional EDependencyProperty::CookRule on EDependencyCategory::Manage properties, and there are two types of PackageManagers reported by the UAssetManager:

  + GetPackageManagers for managers that control only chunk assignment (which pakfile/iostore container an Asset is placed into).
  + GetPackageCookRuleManagers for managers that affect both cookrule (whether an Asset gets cooked), and chunk assignment.
  + Assets that declare usedingame dependencies affect both categories of their dependencies.
  + Assets that declare editoronly, non-build dependencies affect neither.
  + Assets that declare editoronly, build dependencies affect chunk assignment but not the cookrule. This new property was added to support correct chunk assignment for platform-specific dependencies.

#### Core

**API Change:**

* MSVC v14.50 compiler bundled with Visual Studio 2026 is not currently supported.
* Developers can change the default behavior of TArray<> and related containers to behave more like traditional C++ containers, so that they will only compact when Shrink() is explicitly called. Use the `FNonshrinkingAllocator` as your array allocator to request this behavior. This can also be passed as the secondary allocator for TInlineAllocator.

**API Change:**

* Nuget packages will continue to be audited for other configurations as these are urgent issues to address, but this will prevent blocking errors for licensees and CI while they are addressed.

#### Dev Tools

**Upgrade Notes:**

* Updating Project Build Settings:

  + If your project is a code project, the following applies. This does not apply to content-only projects, as they do not contain \*Target.cs files.
  + For Launcher & Installed Engine Builds:

    - For each \*Target.cs file in your project, update the build settings to V6:DefaultBuildSettings = BuildSettingsVersion.V6
    - Note: If the project is opened from the Epic Games Launcher, you’ll see a prompt identifying which \*Target.cs file must be updated. After making this change, reopen the project.
  + For Source Engine Builds (not an installed version):

    - For each \*Target.cs file in your project, you have two options:

      1. Recommended (Upgrade): Follow the same steps as for Launcher & Installed builds and set the DefaultBuildSettings:DefaultBuildSettings = BuildSettingsVersion.V6.
      2. Stay on Current Build Settings: If you wish to remain on your existing DefaultBuildSettings, you must declare a unique build environment:BuildEnvironment = TargetBuildEnvironment.Unique.

### Framework

#### Audio

**Upgrade Notes:**

* Existing subtitles inside Asset UserData will need to be remade.
* Any classes inheriting from USubtitleTextBlock need to instead inherit from USubtitleWidget.

#### Gameplay

**API Change:**

* You can suppress the deprecation warnings with the bEnabledLegacyMappingDeprecationWarnings option in the project's input settings.
* The CVar AbilitySystem.WarnCooldownEffectWithoutTags can be used to opt-out of this, for example if your GameplayAbility subclass implements a different way of checking cooldowns.
* Trying to create a FTickableGameObject with default options from a worker thread (such as during async loading) will now ensure as this is a race condition that could crash. To fix this, use the new FTickableGameObject(ETickableTickType::Never) constructor and then call SetTickableTickType after initialization is complete.
* If you make a custom camera node evaluator, you can now opt-out of features you don't need, but you get them all by default. It avoids the situation where making a new node results on stuff not working because you didn't add the correct flag.
* This behavior is enabled by default, but you can go back to processing only on the main game thread with this console variable: [ConsoleVariables] WindowsApplication.UseWorkerThreadForRawInput=false
* Authors of custom movement modes in Mover 2.0 will need to update their code:

  + Callers must now provide an angular velocity to FMoverDefaultSyncState::SetTransforms\_WorldSpace in order to ensure that angular velocity can persist when changing mode
  + FRotator FProposedMove::AngularVelocity is now replaced by FVector FProposedMove::AngularVelocityDegrees.
  + UMovementUtils::ComputeAngularVelocity is now deprecated, callers should use ComputeAngularVelocityDegrees
* Add a way to deprecate specific "legacy" axis and action mapping names. If this flag is set to true on the project settings, then any BP references to it will have a deprecation warning. Any C++ Bind calls using these names will also emit a warning.
* Some of your camera rigs may need some parameters to be pre-blended. Backwards compatibility was not kept for this change (it was too costly and unnecessary given GameplayCameras' "Experimental" status) so you'll have to re-enable the option for these parameters.
* Added a "IsVirtual" flag to FKeys so that you check at runtime if the key is virtual.

  + Added two new virtual keys for accept and back, which are bindable and useable in Enhanced Input.
  + We need to make new keys here because FKeys are serialized via their FName, so in order to make sure that it properly serializes per-platform we need to save out the keys with unique names and then populate the key details with the "real" value at runtime.
* Check for the instigating controller on an actor.

  + For actor components, get the owning actor and check that instigating controller.

**Upgrade Notes:**

* If you are dealing with the map-placed actor duplicating bindings bug in UE 5.5 and 5.6, see the [resolution notes here](https://issues.unrealengine.com/issue/UE-273286).

#### Mass

**API Change:**

* Renamed all `FMassBatchedCommand::Execute` overrides to `Run` and made it non-constant.

### Level Design and Art Tools

#### Landscape

**API Change:**

* Example Command Line: ProjectName MapName -run=WorldPartitionBuilderCommandlet -SCCProvider=Perforce -Builder=WorldPartitionLandscapeBuilder -AllowCommandletRendering ( -IterativeCellSize=Value)
* Deprecated ULandscapeEditLayerBase::GetActions and FEditLayerAction to remove custom actions from runtime logic. Edit Layer customization classes can implement IEditLayerCustomization and register to the Landscape Editor module.

### Online

#### Crash Reporter

**Upgrade Notes:**

* Previously, the format was protobuf and needed to be converted using plcrashutil, but now the format is crashlog.

### Platform

#### Mac

**Upgrade Notes:**

* If HairStrands rendering is needed on Mac SM5, the feature can be enabled in addition to using the experimental feature bindless SM5 in project settings.

#### XR

**Upgrade Notes:**

* If your project has an xr.MobileLDRDynamicResolution setting, you should replace it with an xr.MobilePrimaryScalingMode setting:

  + xr.MobileLDRDynamicResolution=0 -> xr.MobilePrimaryScalingMode=0
  + xr.MobileLDRDynamicResolution=1 -> xr.MobilePrimaryScalingMode=1

**API Change:**

* Added FOpenXRRenderBridge::RunOnRHISubmissionThread, which should be used to wrap all OpenXR calls that can submit directly to the graphics queue (xrBeginFrame, xrEndFrame, xrAcquireSwapchainImage, xrReleaseSwapchainImage).

  + xrEndFrame in FOpenXRHMD is currently exempted because the submission thread is flushed before we present.

### Rendering

#### Lighting

**Upgrade Notes:**

* Added immediately deprecated r.LightMaxDrawDistanceScale.UseLegacyFadeBehavior\_WillBeRemoved to temporarily restore previous behavior.

#### Materials and Shaders

**API Change:**

* Cached the ShaderPlatform inside MaterialResource, derive the FeatureLevel from that ShaderPlatform.
* Cache/Find MaterialResource by QualityLevel/ShaderPlatform instead of QualityLevel/FeatureLevel.
* Deprecated all the Setter/Getter functions for MaterialResource, MaterialRelevance that take FeatureLevel and replace them with ShaderPlatform.
* Deprecated all FMaterialResource/FMaterial/UMaterial/UMaterialInstance functions that take ShaderPlatform as argument, since the ShaderPlatform should already be cached inside the MaterialResource when it was added.
* Deprecated BuildFeatureLevelWidget, LoadEditorFeatureLevel, SaveEditorFeatureLevel for BuildShaderPlatformWidget, LoadEditorShaderPlatformPreview, SaveEditorShaderPlatformPreview.
* Deprecated GetCurrentFeatureLevelPreviewText, GetCurrentFeatureLevelPreviewTextVisibility, BuildFeatureLevelWidget for GetCurrentShaderPlatformPreviewText, GetCurrentShaderPlatformPreviewTextVisibility, BuildShaderPlatformWidgetMark.
* Deprecated virtual functions from MaterialInterface and FMaterial as final to avoid silent errors.

#### MegaLights

**API Change:**

* Marking for HairStrands data is not yet implemented; it will produce a warning. "Reference mode" works the same with raytracing and will often tend to work with VSM, but could in theory miss marking some pages, so also produces a warning. This is not expected to be a useful mode though as reference mode should generally use raytracing (and perhaps should force it for all lights).

### Simulation

#### Core Physics

**API Change:**

* Added a dependency to the ChaosCore module.

#### Modular Vehicles

**API Change:**

* Added an additional input quantization mechanism.

### Virtual Production

#### Tools

**API Change:**

* GetValue and GetValueInArray of the IRemoteControlPropertyHandle now correctly take UObject\* references.
* Remove ProvidedNamespace as it was not in use anywhere. No deprecation as this is an experimental plugin.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What's New?](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#what-s-new)
* [Rendering](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#rendering)
* [MegaLights (Beta)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#megalights(beta))
* [Niagara Heterogeneous Volumes](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#niagaraheterogeneousvolumes)
* [Substrate](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#substrate)
* [Nanite Foliage and Skinning (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#nanitefoliageandskinning(experimental))
* [SMAA (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#smaa(experimental))
* [Character and Animation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#character-and-animation)
* [Motion Matching Chooser Integration (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#motionmatchingchooserintegration(experimental))
* [Blendshapes and Sculpting Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#blendshapesandsculptingtools)
* [World Collisions for Control Rig Physics](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#worldcollisionsforcontrolrigphysics)
* [Control Rig Dependency View](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#controlrigdependencyview)
* [FBIK and Retargeting Performance](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#fbikandretargetingperformance)
* [Better Foot Contact and Proportioned Retargeting](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#betterfootcontactandproportionedretargeting)
* [Spatially Aware Retargeting (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#spatiallyawareretargeting(experimental))
* [Sequence Validator (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#sequencevalidator(experimental))
* [Ease Curve (Beta) and UX Improvements](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#easecurve(beta)anduximprovements)
* [Dataless Mutable (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#datalessmutable(experimental))
* [Selection Sets](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#selectionsets)
* [Animation Mode UX and QOL](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#animationmodeuxandqol)
* [MetaHuman](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahuman)
* [MetaHuman Creator](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahumancreator)
* [MetaHumans in Unreal Engine](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahumansinunrealengine)
* [MetaHuman Animator](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahumananimator)
* [MetaHuman Capture](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahumancapture)
* [MetaHuman for Houdini](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahumanforhoudini)
* [MetaHuman for Maya](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metahumanformaya)
* [Worldbuilding](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#worldbuilding)
* [Custom HLODs](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#customhlods)
* [HLODs Setup UX](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#hlodssetupux)
* [Procedural Content Generation (PCG)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#proceduralcontentgeneration(pcg))
* [PCG Framework is Production Ready](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#pcgframeworkisproductionready)
* [PCG Editor Mode](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#pcgeditormode)
* [Procedural Vegetation Editor](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#proceduralvegetationeditor)
* [Assets Workflows](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#assetsworkflows)
* [Custom Data Types](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#customdatatypes)
* [Polygon2D Data Type and Operators](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#polygon2ddatatypeandoperators)
* [GPU Fast Geo Interop](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#gpufastgeointerop)
* [GPU Operators and Improvements](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#gpuoperatorsandimprovements)
* [UX Improvements](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#uximprovements)
* [Nodes and Operators](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#nodesandoperators)
* [Python Interop Plugin](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#pythoninteropplugin)
* [Developer Iteration](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#developeriteration)
* [Incremental Cooking (Beta)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#incrementalcooking(beta))
* [CPP Tools - MSVC 14.44 Support](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#cpptools-msvc1444support)
* [Build Health Tracking and Visualization (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#buildhealthtrackingandvisualization(experimental))
* [Audio](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#audio)
* [Audio Insights (Beta)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#audioinsights(beta))
* [MetaSound Node Configuration](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#metasoundnodeconfiguration)
* [Audio Subtitle Plugin](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#audiosubtitleplugin)
* [Audio Waveform Editor](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#audiowaveformeditor)
* [Format / Channel Agnostic Types (CAT)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#format/channelagnostictypes(cat))
* [Tech Audio Tools Sample](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#techaudiotoolssample)
* [Platform](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#platform)
* [Android Platform Support](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#androidplatformsupport)
* [Mobile Renderer](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mobilerenderer)
* [Stereo Layer](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#stereolayer)
* [OpenXR Application SpaceWarp](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#openxrapplicationspacewarp)
* [OpenXR User Presence](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#openxruserpresence)
* [Motion Design](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#motion-design)
* [Motion Design Production Ready](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#motiondesignproductionready)
* [Text3D — Rich Text](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#text3d%E2%80%94richtext)
* [Transition Logic Quality of Life](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#transitionlogicqualityoflife)
* [Remote Control UX](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#remotecontrolux)
* [Scene State](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#scenestate)
* [Data Link](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#datalink)
* [Production Rendering Pipeline](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#production-rendering-pipeline)
* [Material Parameter Collection Modifier](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#materialparametercollectionmodifier)
* [Burn In Per-Output Type](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#burninper-outputtype)
* [File Naming Control](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#filenamingcontrol)
* [EXR Metadata Per Render Layer](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#exrmetadataperrenderlayer)
* [Content Pipeline](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#content-pipeline)
* [Customize USD Asset Import with Interchange (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#customizeusdassetimportwithinterchange(experimental))
* [FBX Level Import with Interchange](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#fbxlevelimportwithinterchange)
* [Editor and UI Systems](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#editoranduisystems)
* [AI Assistant (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#aiassistant(experimental))
* [Home Screen](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#homescreen)
* [Orthographic Clipping Interactions](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#orthographicclippinginteractions)
* [Improved Save and Delete Dialog Boxes](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#improvedsaveanddeletedialogboxes)
* [Improved Window Dragging Interactions](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#improvedwindowdragginginteractions)
* [Improved Blueprint Editor Duplicate Interactions](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#improvedblueprinteditorduplicateinteractions)
* [Geometry Inspection Viewport Modes](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#geometryinspectionviewportmodes)
* [User Asset Tags](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#userassettags)
* [Tagged Asset Browser (Niagara)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#taggedassetbrowser(niagara))
* [Framework](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#framework)
* [State Tree: Rewind Debugger](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#statetree:rewinddebugger)
* [State Tree Runtime](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#statetreeruntime)
* [Mass Debugger](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#massdebugger)
* [Autogen NavLink Multiple Jump Config](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#autogennavlinkmultiplejumpconfig)
* [Mass Runtime](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#massruntime)
* [Iris (Beta)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#iris(beta))
* [Media](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#media)
* [Media Viewer (Beta)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mediaviewer(beta))
* [Simulation and VFX](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#simulation-and-vfx)
* [Chaos Destruction](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaosdestruction)
* [Chaos Dataflow Editor](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaosdatafloweditor)
* [Chaos Visual Debugger](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaosvisualdebugger)
* [Chaos Cloth](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaoscloth)
* [Chaos Core](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaoscore)
* [Chaos Caching](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaoscaching)
* [Chaos Hair](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaoshair)
* [Chaos Fluids](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaosfluids)
* [Virtual Production](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#virtualproduction)
* [Live Link — Data Preview](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#livelink%E2%80%94datapreview)
* [Live Link Hub — Robust Recording](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#livelinkhub%E2%80%94robustrecording)
* [Live Link — Broadcast Component](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#livelink%E2%80%94broadcastcomponent)
* [Live Link — Pauseable Data Stream](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#livelink%E2%80%94pauseabledatastream)
* [Live Link Hub — Unreal Editor Device](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#livelinkhub%E2%80%94unrealeditordevice)
* [Mocap Manager — Dynamic Prop Attachment](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mocapmanager%E2%80%94dynamicpropattachment)
* [Mocap Manager — Improved Performer Mesh Creation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mocapmanager%E2%80%94improvedperformermeshcreation)
* [Composure](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#composure)
* [Media Profile](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mediaprofile)
* [Take Recorder — Hitch Protection (Experimental)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#takerecorder%E2%80%94hitchprotection(experimental))
* [Naming Tokens — Editable Text Widget](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#namingtokens%E2%80%94editabletextwidget)
* [Timeline Templates for Cinematic Assembly Schemas](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#timelinetemplatesforcinematicassemblyschemas)
* [Duplicate Assemblies with Reference Replacement](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#duplicateassemblieswithreferencereplacement)
* [SMPTE 2110 — Nvidia Rivermax BlueField-3 Support](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#smpte2110%E2%80%94nvidiarivermaxbluefield-3support)
* [Platform SDK Upgrades](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#platform-sdk-upgrades)
* [Release Notes](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#release-notes)
* [AI/ML](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ai/ml)
* [Neural Network Engine (NNE)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#neuralnetworkengine(nne))
* [Animation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#animation)
* [Animating in Engine](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#animatinginengine)
* [Character Customization (Mutable)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#charactercustomization(mutable))
* [Control Rig](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#controlrig)
* [Deformer Graph](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#deformergraph)
* [Gameplay](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#gameplay)
* [ML Deformer](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mldeformer)
* [Physics Control](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#physicscontrol)
* [Runtime](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#runtime)
* [Sequencer](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#sequencer)
* [Skeletal Editing](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#skeletalediting)
* [Editor](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#editor)
* [Datasmith](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#datasmith)
* [Framework](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#framework)
* [Interchange](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#interchange)
* [Scripting](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#scripting)
* [UI](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ui)
* [UX](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ux)
* [Foundation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#foundation)
* [Build](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#build)
* [Core](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#core)
* [Dev Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#devtools)
* [Horde](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#horde)
* [Insights](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#insights)
* [Framework](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#framework-2)
* [AI](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ai)
* [AI Behavior Trees](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#aibehaviortrees)
* [AI Debugging](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#aidebugging)
* [AI EQS](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#aieqs)
* [AI Navigation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ainavigation)
* [AI Smart Objects](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#aismartobjects)
* [AI State Tree](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#aistatetree)
* [API](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#api)
* [Audio](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#audio)
* [Blueprint](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#blueprint)
* [Blueprint Compiler](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#blueprintcompiler)
* [Blueprint Runtime](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#blueprintruntime)
* [Gameplay](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#gameplay-2)
* [Mass](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mass)
* [Networking](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#networking)
* [Level Design and Art Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#leveldesignandarttools)
* [Geometry Core](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#geometrycore)
* [Geometry Script](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#geometryscript)
* [Landscape](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#landscape)
* [Modeling Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#modelingtools)
* [Procedural](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#procedural)
* [Texturing Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#texturingtools)
* [UV Editor](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#uveditor)
* [World Building](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#worldbuilding-2)
* [Media](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#media)
* [Media Viewer (Beta)](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mediaviewer(beta)-2)
* [Mobile Rendering](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mobilerendering)
* [Mobile Lighting](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mobilelighting)
* [Mobile Postprocessing](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mobilepostprocessing)
* [Online](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#online)
* [Crash Reporter](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#crashreporter)
* [HTTP](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#http)
* [Online Subsystem](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#onlinesubsystem)
* [Platform](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#platform)
* [Linux](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#linux)
* [Mac](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mac)
* [Online](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#online-2)
* [Windows](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#windows)
* [XR](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#xr)
* [Platform Mobile](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#platformmobile)
* [Android](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#android)
* [iOS, tvOS, and iPadOS](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ios,tvos,andipados)
* [Rendering](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#rendering-2)
* [Architecture](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#architecture)
* [Lighting](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#lighting)
* [Lumen](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#lumen)
* [Materials and Shaders](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#materialsandshaders)
* [MegaLights](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#megalights)
* [Nanite](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#nanite)
* [Niagara](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#niagara)
* [Path Tracer](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#pathtracer)
* [Postprocessing](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#postprocessing)
* [RHI](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#rhi)
* [Substrate](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#substrate-2)
* [Simulation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#simulation)
* [Chaos Visual Debugger](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#chaosvisualdebugger-2)
* [Cloth](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#cloth)
* [Core Physics](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#corephysics)
* [Dataflow](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#dataflow)
* [Fluids / Smoke](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#fluids/smoke)
* [General Physics](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#generalphysics)
* [Modular Vehicles](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#modularvehicles)
* [Networked Physics](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#networkedphysics)
* [Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#tools)
* [BuildGraph](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#buildgraph)
* [UnrealGameSync](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#unrealgamesync)
* [Virtual Production](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#virtualproduction-2)
* [Compositing](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#compositing)
* [nDisplay](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ndisplay)
* [Performance Capture](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#performancecapture)
* [Rendering](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#rendering-3)
* [Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#tools-2)
* [Templates](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#templates)
* [Upgrade Notes](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#upgrade-notes)
* [Animation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#animation-2)
* [Control Rig](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#controlrig-2)
* [Runtime](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#runtime-2)
* [Editor](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#editor-2)
* [Framework](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#framework-3)
* [UI](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ui-2)
* [UX](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#ux-2)
* [Foundation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#foundation-2)
* [Build](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#build-2)
* [Core](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#core-2)
* [Dev Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#devtools-2)
* [Framework](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#framework-4)
* [Audio](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#audio-2)
* [Gameplay](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#gameplay-3)
* [Mass](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mass-2)
* [Level Design and Art Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#leveldesignandarttools-2)
* [Landscape](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#landscape-2)
* [Online](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#online-3)
* [Crash Reporter](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#crashreporter-2)
* [Platform](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#platform-2)
* [Mac](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#mac-2)
* [XR](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#xr-2)
* [Rendering](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#rendering-4)
* [Lighting](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#lighting-2)
* [Materials and Shaders](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#materialsandshaders-2)
* [MegaLights](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#megalights-2)
* [Simulation](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#simulation-2)
* [Core Physics](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#corephysics-2)
* [Modular Vehicles](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#modularvehicles-2)
* [Virtual Production](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#virtualproduction-3)
* [Tools](/documentation/en-us/unreal-engine/unreal-engine-5-7-release-notes?application_version=5.7#tools-3)
