<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7 -->

# Migrating Assets from Unity to Unreal Engine

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for Unity Developers](/documentation/en-us/unreal-engine/unreal-engine-for-unity-developers "Unreal Engine for Unity Developers")
7. Migrating Assets from Unity to Unreal Engine

# Migrating Assets from Unity to Unreal Engine

Import, Migrate, and Convert game assets from Unity to Unreal Engine.

![Migrating Assets from Unity to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/fc173ed0-f917-418a-bd3d-502fbf5b7ee5?resizing_type=fill&width=1920&height=335)

 On this page

### Importing and Converting Assets

**Unreal Engine 5** projects contain a variety of assets that make up the final game. Some of those asset types are specific to Unreal Engine, such as Blueprint classes, while others are universal file formats that can be imported into the engine.

This document goes over the types of assets you can import into Unreal Engine, how to import them, and links to additional information.

## Common Asset Types

Unreal Engine 5 supports the following asset types:

| Unreal Asset Type | Unity Equivalent | Supported Formats |
| --- | --- | --- |
| Static Mesh | Mesh | `.fbx, .obj` |
| Skeletal Mesh | Skinned Mesh | `.fbx, .obj, .usd` |
| Animation Sequence | Animation, Mecanim | `.fbx, .obj, .abc` |
| [Texture](https://dev.epicgames.com/documentation/en-us/unreal-engine/textures-in-unreal-engine) | Texture | `.bmp, .float, .jpeg, .jpg, .pcx, .png, .psd, .tga, .dds` (Cubemap or 2D), `.exr` (HDR), `.tif` (TIFF), `.tiff` (TIFF) |
| Audio File | Audio File | `.wav, .ogg, .flac, .aif, .opus, .mp3` |
| Video Files | Video clip | `.mov, .mp4, .wmv` |
| Fonts | Font asset | `.ttf, .otf` |
| glTF File | glTF File | `.gltf` (JSON), `.glb` |
| [SpeedTree Model](https://docs.speedtree.com/doku.php?id=ue4_introduction) | SpeedTree | `.srt` |

## Asset Considerations Before Importing to Unreal Engine

### Unreal Engine’s Coordinate System

Unreal Engine uses the [Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) to represent positions in three-dimensional [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space). The coordinate system in the Unreal Editor is left-handed and uses the **X axis** to represent the **forward / backwards** direction, the **Y axis** to represent the **right / left** directions, and **Z axis** to represent the **up / down** directions.

Unity’s coordinate system is also left-handed. However, Unity uses the **X axis** to represent **right / left**, **Y Axis** to represent **up / down**, and the **Z Axis** to represent the **forward / backwards** direction.

This has implications when directly importing assets from Unity to Unreal Engine as the asset’s orientation may be incorrect. To solve this, you can change the asset’s orientation inside a digital content creation (DCC) package such as Maya or Blender, or directly in the **Import dialogue** of Unreal Engine.

You can learn more about Unreal Engine’s coordinate system by reading the [Coordinate System and Spaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinate-system-and-spaces-in-unreal-engine) documentation.

### Units of Measurement in Unreal Engine

Unreal Engine uses the [Metric System](https://en.wikipedia.org/wiki/Metric_system) to measure object size and distance. Specifically, Unreal Engine uses the **Unreal unit (UU)** internally for measurements. **One Unreal Unit** is equivalent to **1 cm**.

Use this information to assign the correct scale when creating meshes in an external digital content creation (DCC) package.

Unity also uses the Metric System internally, with **one Unity unit** being equal to **1 meter (100 cm)**. This will affect the scale of objects imported directly from Unity into Unreal Engine.

You can learn more about Unreal Engine’s units of measurement by reading the [Units of Measurement](https://dev.epicgames.com/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine) documentation.

### FBX Content Pipeline

Unreal Engine supports a variety of file formats for importing content into your project. One of the most popular asset formats is **Autodesk FBX**.

The FBX format provides interoperability between many digital content creating (DCC) packages and offers the following advantages:

* Using a single file format for static meshes, skeletal meshes, animations, and morph targets.
* Importing multiple LODs and Morphs/Blendshapes in one import operation.
* Importing material and texture assets, and automatically applying them to static meshes.

Unreal Engine’s FBX pipeline uses **FBX 2020.2**, so we recommend using that version to avoid possible incompatibilities when importing assets.

To learn more about the FBX pipeline, read the [FBX Content Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline) documentation.

## Version Information

At the time of writing, the version of Unreal Engine and Unity engine used for screenshots and terminology are as follows:

* Unreal Engine 5.4.3
* Unity 6 (6000.0.2f1)

## Preparing to Export Assets from Unity

Before exporting assets from Unity, follow these steps to **enable** the **FBX Exporter** package:

1. In Unity, click **Window > Package Manager** to open the **Package Manager** window.

   [![Click Window - Package Manager](https://dev.epicgames.com/community/api/documentation/image/985b75d7-9bc2-4c21-8921-875359c54e44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/985b75d7-9bc2-4c21-8921-875359c54e44?resizing_type=fit)
2. Click the **Unity Registry** category on the left and search for **FBX Exporter**. Click **Install** to install the package.

   [![Search for FBX Exporter and install the package](https://dev.epicgames.com/community/api/documentation/image/b328bb41-ae5d-496d-b8be-5e2fd96707fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b328bb41-ae5d-496d-b8be-5e2fd96707fa?resizing_type=fit)
3. Once the package is installed, close the **Package Manager** window.

You can now **right-click** a prefab in the **Hierarchy** window and select **Export to FBX** to export it as an `.fbx` file.

Alternatively, you can open your Unity project’s **source folder** and directly copy certain files, such as textures directly.

## Meshes / Static Meshes

[![A static mesh in Unity](https://dev.epicgames.com/community/api/documentation/image/ed7ab102-58f1-45b5-95af-a7b905553da9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed7ab102-58f1-45b5-95af-a7b905553da9?resizing_type=fit)

**Static meshes** are 3D meshes whose geometry does not change. You can import static meshes to Unreal Engine in .**fbx** or .**obj** formats, with .fbx as the preferred format. You can learn more about static meshes in Unreal Engine by reading the [Static Meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-meshes) documentation.

This example shows you how to export the Unreal Engine **material ball** static mesh from Unity into Unreal.

This prefab has one mesh and three materials. However, your mesh prefab can contain multiple meshes in its hierarchy.

[![The Unreal Engine material ball static mesh](https://dev.epicgames.com/community/api/documentation/image/08c16494-ad73-4b62-827d-2e95900897bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08c16494-ad73-4b62-827d-2e95900897bc?resizing_type=fit)

[![This prefab has one mesh and three materials](https://dev.epicgames.com/community/api/documentation/image/31905bab-0682-4d17-ac98-98082a6f3857?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31905bab-0682-4d17-ac98-98082a6f3857?resizing_type=fit)

### Export a Static Mesh from Unity

To export a **static mesh** from Unity, follow these steps:

1. Right-click the prefab in the **Hierarchy** window and select **Export FBX…** from the menu.

   [![Right click the prefab in the Hierarchy window and select Export FBX](https://dev.epicgames.com/community/api/documentation/image/d898b1de-a091-426e-93a3-e5ea7da60a94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d898b1de-a091-426e-93a3-e5ea7da60a94?resizing_type=fit)
2. In the **Export Options** window, enter the **Export Name** and **Export Path**.

   1. Under the **Options** category, select the **ASCII Export Format**.
   2. Click the **Include** dropdown and select **Model(s) Only**.
   3. If your mesh has Levels of Detail (LODs) then select the appropriate level.
   4. **Enable** the **Embed Textures** checkbox if you want to export the mesh materials with their corresponding textures.
   5. Click **Export** to export your static mesh.

   [![Enter the correct export options for your static mesh](https://dev.epicgames.com/community/api/documentation/image/90eb3a58-b6f7-4c2f-a124-7eb218b4fc02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90eb3a58-b6f7-4c2f-a124-7eb218b4fc02?resizing_type=fit)
3. Go to the **Export Path** folder to find the static mesh .fbx file. This is the file you will import to Unreal Engine.

   [![Go to the Export Path folder to find the static mesh .fbx file](https://dev.epicgames.com/community/api/documentation/image/0a7c390d-2c5c-4e01-84d5-abefe9a126a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a7c390d-2c5c-4e01-84d5-abefe9a126a9?resizing_type=fit)

### Import a Static Mesh to Unreal Engine

To import a **static mesh** to Unreal Engine, follow these steps:

1. Open **Unreal Engine** and click the **Import** button in the **Content Browser**.

   [![Click the Import button in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/4008776f-909a-4921-824d-d840ea71744b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4008776f-909a-4921-824d-d840ea71744b?resizing_type=fit)
2. Navigate to the **Export Path folder** and **select the mesh** .fbx file, then click **Open**.

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the file from the file explorer window directly into the Unreal Engine **Content Browser** to import it.
3. The **FBX Import Options** window will open to show the **import settings** for the static mesh.

   1. Scroll to the bottom of the window to the **Fbx File Information** section to see the asset details. Notice that the **Creator Application** appears as **Unity FBX Exporter 5.1.1** and the **File Axis Direction** is **Y-UP**.

      [![Scroll down to the Fbx File Information section to see the asset details](https://dev.epicgames.com/community/api/documentation/image/65f3a45f-7614-49b4-a8fc-748e6aae74ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/65f3a45f-7614-49b4-a8fc-748e6aae74ec?resizing_type=fit)
   2. Scroll up to the **Mesh** section and **enable** the **Generate Missing Collision checkbox**.

      [![Enable the Generate Missing Collision checkbox](https://dev.epicgames.com/community/api/documentation/image/4d69cdbc-99b9-407e-ae48-bd0ab1d50756?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d69cdbc-99b9-407e-ae48-bd0ab1d50756?resizing_type=fit)
   3. Expand the **Advanced** section and **enable** the **Combine Meshes** checkbox if you want to combine several meshes into one. You can also **enable** the **Import Mesh LODs** if your mesh has LODs.

      [![Enable the Combine Meshes and Import Mesh LODs checkboxes if desired](https://dev.epicgames.com/community/api/documentation/image/96d1a5e7-a86c-4c23-86d8-3facb05874d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96d1a5e7-a86c-4c23-86d8-3facb05874d2?resizing_type=fit)
   4. Scroll down to the **Miscellaneous** section and **enable** the **Convert Scene** and the **Force Front X Axis** checkboxes.

      [![Enable the Convert Scene and the Force Front X Axis checkboxes](https://dev.epicgames.com/community/api/documentation/image/d80798c8-b786-4d4b-a412-dc44ab2e666d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d80798c8-b786-4d4b-a412-dc44ab2e666d?resizing_type=fit)
   5. Scroll down to the **Material** section, click the **Material Import Method** dropdown, and select **Create New Materials**. This will automatically create new materials for the static mesh.

      [![Click the Material Import Method dropdown and select Create New Materials](https://dev.epicgames.com/community/api/documentation/image/8dc67f04-6102-43af-aff2-b83e16632e8c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8dc67f04-6102-43af-aff2-b83e16632e8c?resizing_type=fit)

      For more information on the settings available in the FBX Importer, go to the FBX Import Options Reference page.
4. Click **Import All** to import the static mesh to Unreal Engine.

   [![Click Import All](https://dev.epicgames.com/community/api/documentation/image/51be62ca-1d74-4550-9330-ff37f06fba5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51be62ca-1d74-4550-9330-ff37f06fba5e?resizing_type=fit)
5. The **static mesh** asset along with the **materials** and **textures** are now imported to Unreal Engine.

   [![The static mesh asset is now imported to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/1544bc12-a1ee-430d-a17f-7d345f1fcaf5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1544bc12-a1ee-430d-a17f-7d345f1fcaf5?resizing_type=fit)
6. **Drag** the **static mesh** asset from the **Content Browser** to the level to see the final result.

   [![Drag the static mesh asset to the level](https://dev.epicgames.com/community/api/documentation/image/99d32f2b-4a9e-44a3-997c-ad972aa63b29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99d32f2b-4a9e-44a3-997c-ad972aa63b29?resizing_type=fit)

Learn more about the static mesh FBX pipeline by reading the [FBX Static Mesh Pipeline in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine) documentation.

## Skinned Meshes / Skeletal Meshes

[![A skeletal mesh in Unity](https://dev.epicgames.com/community/api/documentation/image/aa559769-0540-404f-a303-89923a9af353?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa559769-0540-404f-a303-89923a9af353?resizing_type=fit)

Characters in Unreal Engine are created using multiple unique assets that render the visual geometry, play animations, and construct logic that controls the character's behaviors in real time.

The foundational asset for characters in Unreal Engine is the **skeletal mesh** asset, which contains the character's **visual mesh**, or geometric model render of the character, and the character's **[skeleton](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine)** that contains bone data, which is used to animate the character.

Learn more about skeletal meshes in Unreal Engine by reading the [Skeletal Meshes](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) documentation.

This example shows you how to export Unreal Engine’s **Quinn** character from Unity to Unreal.

This prefab has a **root** component which holds several transforms for IK processing, and a **skeletal mesh** component which has the Skinned Mesh Renderer and two materials.

[![Quinn character prefab](https://dev.epicgames.com/community/api/documentation/image/0726ad67-eaae-4d26-9606-a3a7f81f38b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0726ad67-eaae-4d26-9606-a3a7f81f38b8?resizing_type=fit)

[![The skeletal mesh component which has the Skinned Mesh Renderer and 2 materials](https://dev.epicgames.com/community/api/documentation/image/e131d969-b0eb-45d0-b5e5-0da085a8d35d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e131d969-b0eb-45d0-b5e5-0da085a8d35d?resizing_type=fit)

### Export a Skeletal Mesh from Unity

To export a **Skeletal Mesh** from Unity, follow these steps:

1. Right-click the prefab in the **Hierarchy** window and select **Export FBX…** from the menu.

   [![Right click the prefab in the Hierarchy window and select Export FBX](https://dev.epicgames.com/community/api/documentation/image/818e2b15-2c87-49a6-93e4-892b3ed02648?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/818e2b15-2c87-49a6-93e4-892b3ed02648?resizing_type=fit)
2. In the **Export Options** window, enter the **Export Name** and **Export Path**.

   1. Under the **Options** category, select the **ASCII Export Format**, then click the **Include** dropdown and select **Model(s) + Animations**. This will include any animations assigned to the skeletal mesh.
   2. If your mesh has Levels of Detail (LODs), select the appropriate level.
   3. **Enable** the **Animated Skinned Mesh** checkbox.
   4. **Enable** the **Embed Textures** checkbox if you want to export the mesh materials with their corresponding textures.
   5. Click **Export** to export your static mesh.

   [![Enter the correct export options for your skeletal mesh](https://dev.epicgames.com/community/api/documentation/image/49192cdb-2377-4d02-832c-b35774073366?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49192cdb-2377-4d02-832c-b35774073366?resizing_type=fit)
3. Go to the **Export Path** folder to find the skeletal mesh `.fbx` file. This is the file you will import to Unreal Engine.

   [![Go to the Export Path folder to find the skeletal mesh .fbx file](https://dev.epicgames.com/community/api/documentation/image/4784221f-4240-477f-9d3f-acfd040eb5bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4784221f-4240-477f-9d3f-acfd040eb5bf?resizing_type=fit)

### Import a Skeletal Mesh to Unreal Engine

To import a **Skeletal Mesh** to Unreal Engine, follow these steps:

1. Open **Unreal Engine** and click the **Import** button in the **Content Browser**.

   [![Click the Import button in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/41cc4009-6347-4f51-853f-86563f143165?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41cc4009-6347-4f51-853f-86563f143165?resizing_type=fit)
2. Navigate to the **Export Path folder** and **select the skeletal mesh** `.fbx` file then click **Open**.

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the file from the file explorer window directly into the Unreal Engine **Content Browser** to import the file.
3. The **FBX Import Options** window will open to show the **import settings** for the static mesh.

   1. Scroll to the bottom of the window to the **FBX File Information** section to see the asset details. Notice that the **Creator Application** appears as **Unity FBX Exporter 5.1.1** and the **File Axis Direction** is **Y-UP**.

      [![Scroll down to the Fbx File Information section to see the asset details](https://dev.epicgames.com/community/api/documentation/image/3116b399-5f53-4e61-991f-fcf9b3599b54?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3116b399-5f53-4e61-991f-fcf9b3599b54?resizing_type=fit)
   2. Scroll up to the **Mesh** section and **enable** the **Skeletal Mesh** and **Import Mesh checkboxes**. Click the **Import Content Type** dropdown and select **Geometry and Skinning Weights**.

      [![Enable the Skeletal Mesh and Import Mesh checkboxes](https://dev.epicgames.com/community/api/documentation/image/6455dff7-f454-40c5-8f94-6c9cb97941e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6455dff7-f454-40c5-8f94-6c9cb97941e9?resizing_type=fit)

      If your Unreal Engine project already contains a skeleton asset that is compatible with the character’s skeleton that you are importing, you can optionally select the compatible skeleton from the **Skeleton** drop-down. However, unless the skeleton assets are identical, you may choose to import the skeletons as their own assets and then define the different skeleton assets as compatible. For more information, see the [Compatible Skeletons](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine#compatible-skeletons) documentation.
   3. If your skeletal mesh was exported with animations, scroll down to the **Animation** section and **enable** the **Import Animations** checkbox. For this example, the skeletal mesh does not contain any animations.

      [![If your skeletal mesh has animations, enable the Import Animations checkbox](https://dev.epicgames.com/community/api/documentation/image/8e04b016-a9a7-418e-823e-ca7fb408db5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e04b016-a9a7-418e-823e-ca7fb408db5a?resizing_type=fit)
   4. Scroll down to the **Material** section, click the **Material Import Method** dropdown and select **Create New Materials**. This will automatically create new materials for the skeletal mesh.

      [![Click the Material Import Method dropdown and select Create New Materials](https://dev.epicgames.com/community/api/documentation/image/df86f27e-2aaf-41a6-8b1c-a8be14c2f9b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df86f27e-2aaf-41a6-8b1c-a8be14c2f9b3?resizing_type=fit)

      For more information on the settings available in the FBX Importer, go to the FBX Import Options Reference page. |
4. Click **Import All** to import the skeletal mesh to Unreal Engine.

   [![Click Import All](https://dev.epicgames.com/community/api/documentation/image/f480e1b3-3c9b-4529-bdf0-71c14c926f82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f480e1b3-3c9b-4529-bdf0-71c14c926f82?resizing_type=fit)
5. The **skeletal mesh** asset along with the **materials** and **textures** are now imported to Unreal Engine. In addition, a **skeleton** and a **physics asset** are also created based on the skeletal mesh.

   [![The skeletal mesh asset is now imported to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/9c55b17c-1284-4c15-bb39-1ed463aba8d4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c55b17c-1284-4c15-bb39-1ed463aba8d4?resizing_type=fit)
6. **Drag** the **skeletal mesh** asset from the **Content Browser** to the level to see the final result.

   [![Drag the skeletal mesh asset to the level](https://dev.epicgames.com/community/api/documentation/image/fdf36915-00f9-4bff-9223-1e79275bfbc8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fdf36915-00f9-4bff-9223-1e79275bfbc8?resizing_type=fit)

Learn more about the skeletal mesh FBX pipeline by reading the [FBX Skeletal Mesh Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-skeletal-mesh-pipeline-in-unreal-engine) documentation.

## Animations

[![Character animations in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/db7e9829-3e12-43fa-a20c-e3656afba304?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db7e9829-3e12-43fa-a20c-e3656afba304?resizing_type=fit)

You can use Unreal Engine's suite of powerful **animation tools** and **editors** to create **character** and **object runtime animation systems**, **rendered cinematic content**, and author **new animation content** directly in the engine.

Character **animations** in Unreal Engine are built using the [Skeletal Mesh Animation System](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine). Animations are applied to a **skeletal mesh** and are driven by **animation assets**, such as an [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).

Unreal Engine provides a variety of animation tools to work with Skeletal Meshes to further enhance your animations.

For more information about the Skeletal Mesh Animation system and for information about the suite of Animation [Editors](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-editors-in-unreal-engine), [Assets, and Features](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-assets-and-features-in-unreal-engine) in Unreal Engine, see the [Animating Characters and Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine) documentation.

### Export Animation Clips from Unity

**Animation Clips** from Unity can be exported as `.fbx` files using the **FBX Exporter** package. These exported files can then be imported into Unreal Engine as **Animation Sequences** to be used in your project.

[![Skeletal mesh animation in unity](https://dev.epicgames.com/community/api/documentation/image/343812ee-91da-4b63-91a3-c45f905f40ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/343812ee-91da-4b63-91a3-c45f905f40ee?resizing_type=fit)

To export an Animation Clip from Unity, follow these steps:

1. Navigate in your Unity project to the **Hierarchy** panel, and select the character prefab that contains the Animation Clip you want to export.
2. **Right-click** the prefab and select the **Export to FBX…** option.

   [![Export animation clips in unity](https://dev.epicgames.com/community/api/documentation/image/9549ed52-8b4d-4a36-a07c-ffcf84947bc7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9549ed52-8b4d-4a36-a07c-ffcf84947bc7?resizing_type=fit)
3. Set the **Export Name** and **Export Path** properties to define the name of your exported file and where it will be saved on your computer.

   [![Export Name and Export Path properties](https://dev.epicgames.com/community/api/documentation/image/aca6f378-0b11-4597-9e7f-3d339065dcdb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aca6f378-0b11-4597-9e7f-3d339065dcdb?resizing_type=fit)
4. Set the **Export Format** property to **ASCII**, then set the **Include** property to **Model(s) + Animation**. You can optionally decide to include all of the character’s Level Of Detail models (LODs) using the **LOD Level** property and set the **Object(s) Position** property to set a custom transform value.

   [![Options settings](https://dev.epicgames.com/community/api/documentation/image/6d0c62e0-7bb3-46e6-b57b-8ecddc3fe811?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d0c62e0-7bb3-46e6-b57b-8ecddc3fe811?resizing_type=fit)

   Setting the Include property to **Model(s) + Animation** will export the Animation Clip and your characters Model and Skeleton Hierarchy, and store everything in one .fbx file. This can be helpful when importing your assets into Unreal Engine as all of your assets will be saved together.
5. **Enable** the **Animated Skinned Mesh** checkbox, then export the assets using the **Export** button.

   [![Enable the Animated Skinned Mesh checkbox and click Export](https://dev.epicgames.com/community/api/documentation/image/8e1d2dcd-3d35-4c98-be93-34b790dd7aa8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e1d2dcd-3d35-4c98-be93-34b790dd7aa8?resizing_type=fit)

### Import Animations to Unreal Engine

To import an animation from Unity to Unreal Engine, follow these steps:

1. In the Unreal Engine **Content Browser**, click the **Import** button.

   [![unreal engine content browser import button](https://dev.epicgames.com/community/api/documentation/image/f9259d17-aac0-4356-bf91-690fd4d7a4f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9259d17-aac0-4356-bf91-690fd4d7a4f8?resizing_type=fit)
2. Navigate to the location on your computer that you saved your exported Unity Animation Clip to, select the file, and click the **Open** button.

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the file from the file explorer window directly into the Unreal Engine **Content Browser** to import it.
3. In the **FBX Import Options** window, set the following properties:

   1. **Enable** the **Skeletal Mesh** property.
   2. If you want to import the Animation Clip and generate a new Skeletal Mesh asset with the Animation Sequence asset, **enable** the **Import Mesh** property. If you only want to import the animation as an Animation Sequence, **disable** this property. For this example, we are only importing an animation and do not want to import the mesh as well, since the skeletal mesh has already been previously imported.

      [![Set the correct options in the FBX Import Options window](https://dev.epicgames.com/community/api/documentation/image/fe378a4f-40b6-4faa-bca2-2caa718e33b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe378a4f-40b6-4faa-bca2-2caa718e33b6?resizing_type=fit)

      If you are importing the mesh, you will also need to **enable** the **Import Animations** checkbox.

      [![import animation property](https://dev.epicgames.com/community/api/documentation/image/7317bc1b-7db1-474e-95e5-80a82b448b76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7317bc1b-7db1-474e-95e5-80a82b448b76?resizing_type=fit)
   3. If you are importing a new character, and want to generate a new skeleton asset during the import process, leave the **Skeleton** property **undefined**. If you are importing an animation that you want to use with an existing character skeleton in your project, select the skeleton asset from the asset selection drop-down menu. In this example, the animation is for the Quinn skeletal mesh so the property is defined to use the **SK\_Mannequin** asset.

      [![skeleton property unreal engine](https://dev.epicgames.com/community/api/documentation/image/0ab49240-3720-4a83-adb1-c019a3843110?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ab49240-3720-4a83-adb1-c019a3843110?resizing_type=fit)

      If your Unreal Engine project already contains a skeleton asset that is compatible with the character’s skeleton that you are importing, you can optionally define this **Skeleton** property using the compatible skeleton. However, unless the skeleton assets are identical, you may choose to import the skeletons as their own assets and then define the different skeleton assets as compatible. For more information see the [Compatible Skeletons](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine#compatible-skeletons) documentation.
   4. After defining the properties for the FBX Import Option window, click **Import** to import the asset.

      When importing skeletal mesh and animation assets using the FBX Import Option window, you can select either the **Import All** or the **Import** button to initiate the import process. The **Import All** will import all associated mesh, skeleton, material and texture assets contained within the .fbx file. This option is best used when trying to import all elements of the character. If you are importing additional animations associated with a character you have already imported, select the **Import** option to only import the individual animation assets.

After the import process completes, you can now access your Animation Sequence in the Asset Editor, or by dragging the asset into a level and [playing the project in the editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine).

### Skeletal Mesh Import Troubleshooting

You may encounter some issues when importing skeletal mesh characters and objects into Unreal Engine from another digital content creation (DCC) package or game engine. For example, objects may be imported at the incorrect scale or rotation due to differences between the programs and their respective coordinate systems.

Unreal Engine's FBX Import Settings menu can correct some issues during the import process, but if your objects are not importing correctly please reference the following sections for information about how to correct your import errors.

#### Scale

Unreal Engine’s coordinate system is based on a set scale where 1 Unreal Unit is 1 centimeter. Other programs operate using different scales, which, when migrating a file between the two programs, can result in characters or objects that are larger or smaller than they are designed to be. When migrating a file from Unity, which uses 1-meter units, your characters and objects could appear smaller after importing the assets into Unreal Engine.

[![scale import error](https://dev.epicgames.com/community/api/documentation/image/50c8f47b-072a-4595-b901-6516fcc5cec8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50c8f47b-072a-4595-b901-6516fcc5cec8?resizing_type=fit)

To fix this issue, navigate in the skeletal mesh editor to the **Asset Details** panel, and use the **Import Uniform Scale** property to set a new value for the mesh. After setting this value, use the **Reimport Base Mesh** button in the editor’s toolbar.

[![scale import error fix](https://dev.epicgames.com/community/api/documentation/image/161afee7-277a-4985-8026-7c2b58277889?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/161afee7-277a-4985-8026-7c2b58277889?resizing_type=fit)

#### Rotation

If your character’s skeleton, skeletal mesh, or animation assets are not rotated properly in the viewport, you can fix this issue by opening the asset in its associated editor.

[![rotation import error](https://dev.epicgames.com/community/api/documentation/image/a7375dbf-3a09-479f-8de1-c9d0e2dbf862?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7375dbf-3a09-479f-8de1-c9d0e2dbf862?resizing_type=fit)

Use the **Asset Details** panel to set a value for the **Import Rotation** property, then use the **Reimport Base Mesh** button in the asset editor’s **toolbar**. After the process is complete, your asset should be correctly rotated in Unreal Engine.

[![rotation import error fix](https://dev.epicgames.com/community/api/documentation/image/49a7fbb7-2c24-4c98-aedf-a327a03f0542?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49a7fbb7-2c24-4c98-aedf-a327a03f0542?resizing_type=fit)

Due to the coordinate system differences between Unity and Unreal Engine, a value of **90.0** on the **X-Axis** should correct any rotation issues for your skeletal mesh or Animation Sequence assets.

#### Convert Scene Properties

In the **Asset Details** panel of your asset, you can **enable** the **Convert Scene**, **Force Front Axis**, and **Convert Scene Unity** properties to correct any broken or irregular meshes during playback. After enabling any of these properties, click the **Reimport Base Mesh** button in the asset editor’s toolbar to apply the changes.

[![convert scene properties](https://dev.epicgames.com/community/api/documentation/image/8a7e87ec-1ac4-4394-900a-15bcf2d0ecb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a7e87ec-1ac4-4394-900a-15bcf2d0ecb3?resizing_type=fit)

#### Simultaneously Editing Multiple Assets

When importing Assets into Unreal Engine, it is possible that multiple assets will need the same correction to a setting, such as the import rotation or import scale. Rather than editing each asset individually, you can use bulk editing to apply the same setting or property value to multiple assets at the same time.

To edit multiple assets at once, use the following steps:

1. Select each asset you want to edit in the **Content Browser** using **Shift + Click**.
2. **Right-click** the selected assets and select the **Asset Actions** > **Edit Selection in Property Matrix** option in the context menu.

   [![bulk edit setting](https://dev.epicgames.com/community/api/documentation/image/33da2e5e-73b6-4661-ae83-010bb3b21760?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/33da2e5e-73b6-4661-ae83-010bb3b21760?resizing_type=fit)
3. Each asset’s property will now be accessible in the **Asset Details** panel, where you can search or navigate to a specific property to apply a setting to all assets at once.

### Animation Blueprints

After importing your skeletal mesh character and its Animation Sequence assets, you can use an **Animation Blueprint** to drive animation playback and logic at runtime. Use these graphs to select animations to be played, blend between animations, and layer animations. For more information about using Animation Blueprints to drive animations in your project, see the [Animation Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) documentation.

[![animation blueprint graph overview](https://dev.epicgames.com/community/api/documentation/image/1bf0fb01-bd73-49bb-9b94-3058bb6908b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1bf0fb01-bd73-49bb-9b94-3058bb6908b2?resizing_type=fit)

## Textures

[![A cube with a material that uses a brick texture in Unity](https://dev.epicgames.com/community/api/documentation/image/5d60533a-49d7-4381-8d9d-0787c999b13b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d60533a-49d7-4381-8d9d-0787c999b13b?resizing_type=fit)

**Textures** are image assets primarily used in Materials and applied to objects. They can also be used directly for other purposes, such as a heads up display (HUD).

Unreal Engine renders textures using [texture streaming](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-overview-for-unreal-engine) to optimize loading textures into the scene. The texture streaming system uses texture **mipmaps**. These are a pre-calculated sequence of images of the same texture at different resolutions.

You can learn more about textures in Unreal Engine by reading the [Textures](https://dev.epicgames.com/documentation/en-us/unreal-engine/textures-in-unreal-engine) documentation.

### Export a Texture from Unity

Unity keeps texture files saved in their original format inside the project directory, so there is no need to export a texture from Unity. Instead, you can copy the files directly from the project directory.

To find a texture file in Unity’s project directory, follow these steps:

1. **Right-click** on the texture file inside the **Project** window and click **Show in Explorer**.
2. You can now see the files inside the project directory. You can copy the files directly from here, or use this folder location to find the files from Unreal Engine.

   [![You can now see the files inside the project directory](https://dev.epicgames.com/community/api/documentation/image/1c83a250-b8f7-4556-9337-2b08692eb3a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c83a250-b8f7-4556-9337-2b08692eb3a3?resizing_type=fit)

### Import a Texture to Unreal Engine

To import a **texture** to Unreal Engine, follow these steps:

1. Open **Unreal Engine** and click the **Import** button in the **Content Browser**.

   [![Click the Import button in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/3323f928-0794-46de-a586-2ae0bd2c6084?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3323f928-0794-46de-a586-2ae0bd2c6084?resizing_type=fit)
2. Navigate to the **Unity project folder** where the textures are located, **select the texture** files, and click **Open**.

   [![Select the texture files and click Open](https://dev.epicgames.com/community/api/documentation/image/88d68257-29e9-4907-b892-fa77b60265c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88d68257-29e9-4907-b892-fa77b60265c4?resizing_type=fit)

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the files from the file explorer window directly into the Unreal Engine **Content Browser** to import them.
3. The **textures** are now imported to Unreal Engine.

   [![The textures are now imported to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/804f435f-f8ce-4c61-ab5c-4eda332ff267?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/804f435f-f8ce-4c61-ab5c-4eda332ff267?resizing_type=fit)

To learn how to use the textures in a material, see the **Shaders / Materials** section below.

## Shaders / Materials

[![A cube with a brick material in Unity](https://dev.epicgames.com/community/api/documentation/image/aed2727c-113f-497c-9505-78b97c7e2c86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aed2727c-113f-497c-9505-78b97c7e2c86?resizing_type=fit)

**Materials** in Unreal Engine define the surface properties of the objects in your scene. In the broadest sense, you can think of a Material as the "paint" that is applied to a mesh to control its visual appearance.

In more technical terms, Materials tell the render engine exactly how a surface should interact with the light in your scene. Materials define every aspect of the surface including color, reflectivity, bumpiness, transparency, and so on. These calculations are done using data that is input to the material from a variety of **images (textures)** and node-based **Material Expressions**, as well as from various [property settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-properties) inherent to the material itself.

You can learn more about materials in Unreal Engine by reading the [Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials) documentation.

### Export a Material from Unity

Unity’s **Shader Graph** is used to build shaders visually. Unity also has **materials**, which can reference a Shader Graph asset and are applied to GameObjects directly.

Unreal Engine’s materials are converted to shaders internally and are built using the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide), which also uses a node-based approach to building materials.

A Shader Graph asset cannot be directly exported from Unity and converted to a Material graph in Unreal Engine. However, you can export all relevant **textures** from Unity into Unreal Engine and rebuild the Shader Graph node network inside Unreal Engine’s Material Editor.

This example shows a **Lit Shader Graph** that contains a texture applied to the **base color** and another texture applied as the **normal map**.

[![Lit Shader Graph that uses 2 textures](https://dev.epicgames.com/community/api/documentation/image/b800b3a8-308f-49dc-b335-df69603cdc6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b800b3a8-308f-49dc-b335-df69603cdc6f?resizing_type=fit)

Export both of those textures from Unity by following the steps described in the **Textures** section of this document.

### Import a Material to Unreal Engine

Since you cannot directly import a material from Unity, you will rebuild the Shader Graph shown above in Unreal Engine’s Material Editor.

Follow these steps to build the material:

1. Import the textures to Unreal by following the steps described in the **Textures** section of this guide.

   [![The textures are now imported to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/7a292148-2e40-4b8e-9073-ffc2bab6d523?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a292148-2e40-4b8e-9073-ffc2bab6d523?resizing_type=fit)
2. Right click in the **Content Browser** and click **Material** to create a new material. Name the asset **M\_Bricks**.

   [![Create a new material and name it M_Bricks](https://dev.epicgames.com/community/api/documentation/image/54f70ea3-7e49-45d9-8ded-5d324214a213?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54f70ea3-7e49-45d9-8ded-5d324214a213?resizing_type=fit)

   [![The material asset is now created](https://dev.epicgames.com/community/api/documentation/image/ac6724a1-3893-4e34-98f7-2759ad9b19a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac6724a1-3893-4e34-98f7-2759ad9b19a5?resizing_type=fit)
3. Double click **M\_Bricks** to open the Material Editor.

   [![Double click M_Bricks to open the Material Editor](https://dev.epicgames.com/community/api/documentation/image/8c331c23-8401-4aa6-8860-3df89b51cd7e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c331c23-8401-4aa6-8860-3df89b51cd7e?resizing_type=fit)
4. Select the **textures** in the **Content Browser** and drag them inside the **Material Editor** to create two **Texture Sample nodes**.

   [![Select the textures and drag them inside the Material Editor](https://dev.epicgames.com/community/api/documentation/image/7afc0bd7-b88a-478f-935e-71230bb09079?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7afc0bd7-b88a-478f-935e-71230bb09079?resizing_type=fit)
5. Connect the **Texture Sample** node that references the **diffuse** texture to the **Base Color** pin of the material node. Then, connect the **Texture Sample** node that references the **normal map** texture to the **Normal** pin of the material node.

   [![Connect the Texture Sample nodes to the Base Color and Normal pins of the material node](https://dev.epicgames.com/community/api/documentation/image/100c9e3d-5a7b-486e-ad16-83cd1b086732?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/100c9e3d-5a7b-486e-ad16-83cd1b086732?resizing_type=fit)
6. On the material node, enter the values **0.2** for **Specular** and **0.8** for **Roughness**. Click the **Save** button to compile and save the material.

   [![On the material node, enter the values 0.2 for Specular and 0.8 for Roughness](https://dev.epicgames.com/community/api/documentation/image/0c844b09-a220-4cd0-be15-ff7664e92220?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c844b09-a220-4cd0-be15-ff7664e92220?resizing_type=fit)
7. In the viewport, click **Add + > Shapes > Cube** to add a Cube static mesh to the level.

   [![In the viewport click Add + - Shapes - Cube](https://dev.epicgames.com/community/api/documentation/image/f3b6ee2f-b88a-4872-ac03-95a75c8626d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3b6ee2f-b88a-4872-ac03-95a75c8626d2?resizing_type=fit)

   [![A cube is added to the level](https://dev.epicgames.com/community/api/documentation/image/28f0312b-eb10-4472-b38b-423b75ae1f43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28f0312b-eb10-4472-b38b-423b75ae1f43?resizing_type=fit)
8. Select **M\_Bricks** in the **Content Browser** and **drag it** to the **cube** static mesh in the level to apply the material.

   [![Select M_Bricks and drag it to the cube static mesh](https://dev.epicgames.com/community/api/documentation/image/0174fa89-3468-43f4-9fe9-f7c4b67e1450?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0174fa89-3468-43f4-9fe9-f7c4b67e1450?resizing_type=fit)

Learn more about the material FBX pipeline by reading the [FBX Material Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-material-pipeline-in-unreal-engine) documentation.

## Particle Effects

[![Niagara Visual Effects System in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/7c9ea9a1-e2db-4108-9902-fa0084b140ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c9ea9a1-e2db-4108-9902-fa0084b140ee?resizing_type=fit)

Unity’s Visual Effects Graph is used to create GPU particle simulations. The system uses a node-based interface to create the effects and can simulate a large number of particles during gameplay.

The **Niagara VFX System** is Unreal Engine's next-generation VFX system. Niagara offers full control to its users. It is programmable and customizable on every axis and provides advanced tools for debugging, visualization, and performance measurement.

Niagara **Systems** contain one or more **emitters** that can combine to create complex effects. Emitters can spawn **CPU** or **GPU particles** independently and can render their particles as **sprites**, **meshes**, **decals**, **lights**, and **ribbons**. In addition, Niagara Systems have **inheritance**, which means that you can create a master Niagara System and derive several child systems from it.

Advanced users can create **custom modules** directly in the system for complete control over the emitter’s behavior. Niagara also comes with **pre-built templates**, including a full suite of [fluid simulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-fluids-in-unreal-engine) examples for **2D** and **3D gasses**, **liquids**, and **shallow water**.

Niagara particles can interact with the environment by using mesh distance fields, collision, and the NeighborGrid3D module that allows for complex particle BOID behavior, such as flocking.

Niagara supports input data from other systems in Unreal Engine such as physics, animations, and Blueprint code. It also supports input data from external sources.

A Unity Visual Effects Graph cannot be directly exported out and imported to Unreal, so you will have to recreate your effects within Niagara. Many effects use materials and textures, which can be exported. To learn how to export textures from Unity, see the **Textures** section of this document.

Learn more about Niagara by reading the [Creating Visual Effects](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) documentation.

## Audio

Unity’s audio system can import and play a variety of audio file formats in 3D space. The system can also apply many optional effects at runtime, such as reverb.

The **Unreal Audio Engine** is a robust audio engine that supports a wide variety of features across all platforms supported by Unreal Engine.

The audio engine comes with a multi-platform [audio mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-mixer-overview-in-unreal-engine) that enables audio digital signal processing (DSP), procedural synthesis, a customizable submix graph, and a flexible C++ API.

Next-generation features, such as [MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine), [audio modulation](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-modulation-in-unreal-engine), [audio analysis](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-analysis-and-visualization-in-unreal-engine) and the ability to support custom interactive and [procedural music systems](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-procedural-music-with-metasounds) means that there is no need to use audio middleware such as FMOD or Wwise when creating rich, interactive audio for your games.

Learn more about audio in Unreal Engine by reading the [Audio in Unreal Engine 5](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-in-unreal-engine-5) documentation.

### Export an Audio File from Unity

Unity keeps audio files saved in their original format inside the project directory, so there is no need to export audio files from Unity. Instead, you can copy the file directly from the project directory.

To find an audio file in Unity’s project directory, follow these steps:

1. Right click your audio file in the **Project** window and click **Show in Explorer**.
2. You can now see the audio file inside the project directory. You can copy the file directly from here, or use this folder location to find the file from Unreal Engine.

   [![You can now see the audio file inside the project directory](https://dev.epicgames.com/community/api/documentation/image/71158ff4-522d-4fe7-b399-65b2cfcff8b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/71158ff4-522d-4fe7-b399-65b2cfcff8b0?resizing_type=fit)

### Import an Audio file to Unreal Engine

To import an **audio file** to Unreal Engine, follow these steps:

1. Open **Unreal Engine** and click the **Import** button in the **Content Browser**.

   [![Click the Import button in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/b9e7ec70-dd51-4c42-983d-829c85786bac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9e7ec70-dd51-4c42-983d-829c85786bac?resizing_type=fit)
2. Navigate to the **Unity project folder** where the audio file is located, **select the audio** file and click **Open**.

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the file from the file explorer window directly into the Unreal Engine **Content Browser** to import it.
3. The **audio file** is now imported to Unreal Engine.

   [![The audio file** **is now imported to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/c63fac7e-2e29-40db-9d68-7f62a4dff6ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c63fac7e-2e29-40db-9d68-7f62a4dff6ff?resizing_type=fit)
4. Right click the **audio file** in the **Content Browser** and click **Create Cue** to create a sound cue asset. This is the standard audio asset in the engine used to play sounds in-game.

   [![A Sound Cue is now created in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/4fec07ec-ab98-4a8a-b62c-ace49235171f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fec07ec-ab98-4a8a-b62c-ace49235171f?resizing_type=fit)

Learn more about sound cues by reading the [Sound Cues](https://dev.epicgames.com/documentation/en-us/unreal-engine/sound-cues-in-unreal-engine) documentation. We also recommend you learn about [MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine), as they provide more advanced features compared to Sound Cues.

## Video

Unity’s Video Player component attaches video files to GameObjects and provides several options to play video files in the scene.

Unreal Engine comes with a fully-featured [Media Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-technical-reference-for-unreal-engine) that provides similar functionality. The framework supports a variety of video file formats, comes with playback optimization, and supports audio/video capture hardware on Windows and Android devices.

Learn more about playing a video file in Unreal Engine by reading the [Play a Video File](https://dev.epicgames.com/documentation/en-us/unreal-engine/play-a-video-file-in-unreal-engine) documentation.

### Export a Video File from Unity

Unity keeps video files saved in their original format inside the project directory, so there is no need to export a video from Unity. Instead, you can copy the file directly from the project directory.

To find the video file in Unity’s project directory, follow these steps:

1. **Right-click** on the video file inside the **Project** window and click **Show in Explorer**.
2. You can now see the file inside the project directory. You can copy the file directly from here, or use this folder location to find the file from Unreal Engine.

   [![You can now see video file inside the project directory](https://dev.epicgames.com/community/api/documentation/image/2e973f60-160f-4d75-8e03-b50c8a9113f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e973f60-160f-4d75-8e03-b50c8a9113f6?resizing_type=fit)

### Import a Video File to Unreal Engine

To import a **video file** to Unreal Engine, follow these steps:

1. Open **Unreal Engine** and click the **Import** button in the **Content Browser**.

   [![Click the Import button in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/0b447048-ff84-4ec2-b1f7-bf9547bc4fc4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b447048-ff84-4ec2-b1f7-bf9547bc4fc4?resizing_type=fit)
2. Navigate to the **Unity project folder** where the video is located, **select the video** file and click **Open**.

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the file from the file explorer window directly into the Unreal Engine **Content Browser** to import it.
3. The **video file** is now imported to Unreal Engine. A **Media Plate actor** is automatically created in the **Content Browser** which can be dragged into the level to play the video file directly.

   [![The video file** **is now imported to Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/3e29bf61-1096-4804-88bd-1ddee26bde20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e29bf61-1096-4804-88bd-1ddee26bde20?resizing_type=fit)
4. Select the **video file** in the **Content Browser** and drag it into the level.

   [![Select the video file** **and drag it into the level](https://dev.epicgames.com/community/api/documentation/image/daa390da-9c3c-44f3-9107-01c6809d3a9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/daa390da-9c3c-44f3-9107-01c6809d3a9a?resizing_type=fit)
5. With the **Media Plate actor** selected, go to the **Details** panel and scroll down to the **Control** section.

   1. **Enable** the **Play on Open**, **Auto Play**, and **Enable Audio** checkboxes.
   2. If desired, **enable** the **Loop** checkbox to have the video loop indefinitely.

   [![With the Media Plate actor selected, go to the Details panel and set your desired options](https://dev.epicgames.com/community/api/documentation/image/5d9eba33-0423-418e-a1ed-56d7917567c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d9eba33-0423-418e-a1ed-56d7917567c2?resizing_type=fit)
6. Optionally, you can scroll down to the **Geometry** section and adjust the **geometry** used to display the video (Plane, Sphere, or Custom), the **Aspect Ratio**, and **Letterbox Aspect Ratio**. For this example, we will leave the **Auto Aspect Ratio** checkbox **enabled** so the shape conforms to the video file’s native aspect ratio when playing.

   [![You can scroll down to the Geometry section to adjust the geometry used and aspect ratio](https://dev.epicgames.com/community/api/documentation/image/eb35b6c3-9b80-4815-b493-e980f78246e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eb35b6c3-9b80-4815-b493-e980f78246e9?resizing_type=fit)
7. Click **Simulate** to see the video play inside the level.

   [![Click Simulate to see the video play inside the level](https://dev.epicgames.com/community/api/documentation/image/d98fb072-ce53-4652-bed2-62b8b0ec342f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d98fb072-ce53-4652-bed2-62b8b0ec342f?resizing_type=fit)

You can learn more about the **Media Plate actor** by reading the [Media Plate Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/the-media-plate-actor-in-unreal-engine?application_version=5.5) documentation.

## Camera Control and Cinematic Sequences

[![A cinematic sequence created in Sequencer](https://dev.epicgames.com/community/api/documentation/image/82020c26-68af-42de-8274-ab19611b2ff7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82020c26-68af-42de-8274-ab19611b2ff7?resizing_type=fit)

Unity comes with several tools to create cinematic content. The Timeline tool is used to create cinematic sequences in the editor and Cinemachine is a set of tools for controlling the camera.

When used together, these tools provide developers the ability to create dynamic cinematic sequences at runtime.

**Sequencer** is Unreal Engine's multi-track editor used for creating and previewing cinematic sequences in real time.

The editor contains robust cinematic tools that you can use to create animated and cinematic sequences. You can pilot cameras to create level fly-throughs, animate lights, move objects, animate characters, render output sequences, and more.

Camera animations and behaviors created in Timeline and Cinemachine cannot be directly exported from Unity and into Unreal Engine. For this use case, you will have to recreate that behavior by using Sequencer.

Learn more about Sequencer by reading the [Cinematics and Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine) documentation.

## Code and Visual Scripting

[![Code comparison between Unity and Unreal](https://dev.epicgames.com/community/api/documentation/image/29d12d85-4e2a-4c7c-98d7-f9cb2d755ea9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29d12d85-4e2a-4c7c-98d7-f9cb2d755ea9?resizing_type=fit)

Unity’s default programming language is C#, while Unreal uses [C++](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-cplusplus-in-unreal-engine) as its native programming language. Unity also has Bolt Visual Scripting, which is similar to Unreal Engine’s [Blueprint Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) language.

Unity C# scripts and Bolt scripting files cannot be directly exported from Unity and imported to Unreal Engine. You will have to build your functionality using C++ or Blueprints.

To learn about common Unreal Engine programming patterns and best practices, read the [Creating Gameplay in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-gameplay-in-unreal-engine-for-unity-developers) documentation.

## 2D Assets

[![sprite paper 2d asset](https://dev.epicgames.com/community/api/documentation/image/bec4eb72-4eb4-454b-a065-209928ea8f39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bec4eb72-4eb4-454b-a065-209928ea8f39?resizing_type=fit)

**Paper 2D** is a sprite-based system for creating 2D and 2D/3D hybrid games in Unreal Engine. The Paper 2D system uses texture files mapped to planer game objects to represent 2D characters, objects and backgrounds in your Unreal Engine project.

For more information about Paper 2D, and creating 2D projects in Unreal Engine, see the [Paper 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine) documentation.

### Export 2D Assets from Unity

To export 2D assets from Unity, following these steps:

1. **Right-click** the asset in your **Project** window, and select the **Show In Explorer** option to open the asset’s location on your computer.

   [![Export a sprite from Unity](https://dev.epicgames.com/community/api/documentation/image/8bcf3c3a-d3fe-405b-a0c2-434f7bfbc824?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8bcf3c3a-d3fe-405b-a0c2-434f7bfbc824?resizing_type=fit)
2. You can now see the file inside the project directory. You can copy the file directly from here, or use this folder location to find the file from Unreal Engine.

   [![unity asset in file explorer](https://dev.epicgames.com/community/api/documentation/image/026a696c-9d70-436a-b492-ad33646c5cd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/026a696c-9d70-436a-b492-ad33646c5cd1?resizing_type=fit)

### Import 2D Assets to Unreal Engine

To import a **2D asset** to Unreal Engine, follow these steps:

1. Open **Unreal Engine** and click the **Import** button in the **Content Browser**.

   [![import button unreal engine content browser](https://dev.epicgames.com/community/api/documentation/image/616a54d2-1f47-4de8-998a-feb970dcac20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/616a54d2-1f47-4de8-998a-feb970dcac20?resizing_type=fit)
2. Navigate to the **Unity project folder** where the 2D file is located, select the 2D file and click **Open** to import the asset.

   Alternatively, after using the **Show in Explorer** setting in Unity, you can **drag** the file from the file explorer window directly into the Unreal Engine **Content Browser**, to import the file.

   [![import sprite to unreal](https://dev.epicgames.com/community/api/documentation/image/d9063cb9-84d7-4a7b-9837-888008bc038b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9063cb9-84d7-4a7b-9837-888008bc038b?resizing_type=fit)
3. The 2D asset is now imported to Unreal Engine

   [![sprite imported in unreal engine content browser](https://dev.epicgames.com/community/api/documentation/image/98444c6f-731f-4c3c-8c14-eede46f4c2d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98444c6f-731f-4c3c-8c14-eede46f4c2d8?resizing_type=fit)
4. Now that your file is imported, you can use it to create 2D assets or animations using Paper 2D.

For information about importing assets, creating Sprites, and Flipbook Animations, see the [Paper 2D](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine) documentation.

## SpeedTree Assets

[![SpeedTree foliage](https://dev.epicgames.com/community/api/documentation/image/448fe9be-432d-41ef-b4e7-79a5a56a2e2a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/448fe9be-432d-41ef-b4e7-79a5a56a2e2a?resizing_type=fit)

SpeedTree is a suite of products focused on creating foliage for real time and linear content. The product includes a tree modeler and prebuilt assets you can purchase and import directly into Unreal Engine.

Learn more about using SpeedTree in Unreal Engine by reading [Introduction to SpeedTree for Unreal Engine](https://docs.speedtree.com/doku.php?id=ue4_introduction) in the SpeedTree documentation.

* [unity](https://dev.epicgames.com/community/search?query=unity)
* [unreal editor](https://dev.epicgames.com/community/search?query=unreal%20editor)
* [unity to unreal](https://dev.epicgames.com/community/search?query=unity%20to%20unreal)
* [unity editor to unreal editor](https://dev.epicgames.com/community/search?query=unity%20editor%20to%20unreal%20editor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Importing and Converting Assets](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#importing-and-converting-assets)
* [Common Asset Types](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#common-asset-types)
* [Asset Considerations Before Importing to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#asset-considerations-before-importing-to-unreal-engine)
* [Unreal Engine’s Coordinate System](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#unreal-engine-s-coordinate-system)
* [Units of Measurement in Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#units-of-measurement-in-unreal-engine)
* [FBX Content Pipeline](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#fbx-content-pipeline)
* [Version Information](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#version-information)
* [Preparing to Export Assets from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#preparing-to-export-assets-from-unity)
* [Meshes / Static Meshes](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#meshes-static-meshes)
* [Export a Static Mesh from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-a-static-mesh-from-unity)
* [Import a Static Mesh to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-a-static-mesh-to-unreal-engine)
* [Skinned Meshes / Skeletal Meshes](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#skinned-meshes-skeletal-meshes)
* [Export a Skeletal Mesh from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-a-skeletal-mesh-from-unity)
* [Import a Skeletal Mesh to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-a-skeletal-mesh-to-unreal-engine)
* [Animations](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#animations)
* [Export Animation Clips from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-animation-clips-from-unity)
* [Import Animations to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-animations-to-unreal-engine)
* [Skeletal Mesh Import Troubleshooting](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#skeletal-mesh-import-troubleshooting)
* [Scale](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#scale)
* [Rotation](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#rotation)
* [Convert Scene Properties](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#convert-scene-properties)
* [Simultaneously Editing Multiple Assets](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#simultaneously-editing-multiple-assets)
* [Animation Blueprints](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#animation-blueprints)
* [Textures](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#textures)
* [Export a Texture from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-a-texture-from-unity)
* [Import a Texture to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-a-texture-to-unreal-engine)
* [Shaders / Materials](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#shaders-materials)
* [Export a Material from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-a-material-from-unity)
* [Import a Material to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-a-material-to-unreal-engine)
* [Particle Effects](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#particle-effects)
* [Audio](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#audio)
* [Export an Audio File from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-an-audio-file-from-unity)
* [Import an Audio file to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-an-audio-file-to-unreal-engine)
* [Video](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#video)
* [Export a Video File from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-a-video-file-from-unity)
* [Import a Video File to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-a-video-file-to-unreal-engine)
* [Camera Control and Cinematic Sequences](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#camera-control-and-cinematic-sequences)
* [Code and Visual Scripting](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#code-and-visual-scripting)
* [2D Assets](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#2-d-assets)
* [Export 2D Assets from Unity](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#export-2-d-assets-from-unity)
* [Import 2D Assets to Unreal Engine](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#import-2-d-assets-to-unreal-engine)
* [SpeedTree Assets](/documentation/en-us/unreal-engine/migrating-assets-from-unity-to-unreal-engine?application_version=5.7#speed-tree-assets)
