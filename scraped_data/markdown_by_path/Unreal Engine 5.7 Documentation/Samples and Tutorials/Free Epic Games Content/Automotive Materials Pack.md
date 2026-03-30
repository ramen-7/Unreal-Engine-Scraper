<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7 -->

# Automotive Materials Pack

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Free Epic Games Content](/documentation/en-us/unreal-engine/free-epic-games-content-for-unreal-engine "Free Epic Games Content")
7. Automotive Materials Pack

# Automotive Materials Pack

A breakdown of what assets the Automotive Materials pack contains and how to use them

![Automotive Materials Pack](https://dev.epicgames.com/community/api/documentation/image/9df8d1ec-eeef-49c2-84c5-cece1d3a4e52?resizing_type=fill&width=1920&height=335)

 On this page

The [Automotive Materials Pack](https://www.fab.com/listings/5dd132fe-ee32-4e8c-9cd3-7496547dfb29), available on Fab, is a collection of automotive-themed [physically based Materials](/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine) ready for use in Unreal Engine (UE). The pack is designed to be an out-of-the-box solution for professional rendering of automotive finishes, featuring:

* 164 Materials Instances, driven by 10 Master Materials. All materials utilize PBR best practices.
* High-quality 4K Textures, using the Quixel Megascans library of hand scanned 2D and 3D assets.
* Support for both Object UVs and Triplanar mapping to work even when models have imperfect UV mapping.
* Full support for all lighting methods, including ray tracing.

## Overview

The Automotive Materials Pack is a state-of-the-art collection of Master Materials and example content created to provide 3D visualization professionals with a high-quality solution for creating exceptional automotive Materials.These Materials follow Physically-based Rendering (PBR) best practices and are designed for ease of use. 4K textures from the Quixel Megascans library are used to achieve stunning visual fidelity. Additionally, all materials are set up to use Triplanar Mapping to minimize texture stretching and seams. Finally, every Material is optimized for a variety of lighting solutions and is ray tracing ready.

[![View of the smaple materials available](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e90d429-826c-4d7e-a2ee-71d17b5f0b14/automotive_overview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e90d429-826c-4d7e-a2ee-71d17b5f0b14/automotive_overview.png)



The vehicles meshes used in the examples below **are not included** in the Automotive Materials Pack.

### Master Materials and Material Instances

In **Unreal Engine** (UE), an instance of a Material can be used to change the look and properties of that Material without requiring an expensive recompile. These Material Instances are created from a Master Material, which contains several properties that have been designated as parameters. The Material Instance can see these parameters and you can use them to create multiple variations of a Master Material quickly.

Creating and using Master Materials in UE4 is an advanced workflow. For more information on Materials and their use, read the following documentation:

* [Material Inputs](/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine)
* [Material Tutorials](/documentation/en-us/unreal-engine/unreal-engine-materials-tutorials)
* [Instanced Materials](/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine)

Inside of the Automotive Material Pack you will find the following Materials types:

* [Additive](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#additive)
* [Brake Rotor](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#brakerotor)
* [Car Paint](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#carpaint)
* [Decal](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#decal)
* [Emissive](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#emissive)
* [Glass](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#glass)
* [Masked](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#masked)
* [Opaque](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#opaque)
* [Textile](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#textile)
* [Tint](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine#tint)

### Physically Based Rendering

All Master Materials in the Automotive Material Pack have been designed from scratch to achieve the most realistic and accurate results possible with Unreal's [physically based rendering system](/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine). This means, for example:

* In the real world, almost all surfaces behave either as a metal or as a non-metal (dielectric). Similarly, all Materials in the pack are either fully metallic or fully non-metallic. This is determined by a node in the Master Material, exposed to Material Instances as a single **IsMetallic** checkbox. This ensures that all surfaces reflect a physically accurate proportion of specular and diffuse light.
* The Specular input is not used in any Materials. This avoids introducing any reflections that do not accurately match the behavior of light in the real world. The Specular value is typically left at the default value of 0.5.
* The Roughness map controls the glossiness of the surface. Smoother surfaces, where the roughness map is closer to black, have sharper, more focused reflections. Rougher surfaces, where the roughness map is closer to white, have blurrier, less distinct reflections.

For a more in-depth explanation of what physically based rendering is and how to use it in UE4, see the [Physically-Based Materials](/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine).

### Triplanar Mapping

The pack includes a Material Function that performs efficient triplanar mapping. Triplanar mapping is a way of applying texture maps to an object that does not use UV mappings to map the object's 3D surfaces to 2D texture space. Instead, triplanar mapping applies the texture map to three orthogonal planes, then projects these three planes to the surface of the object.

This is the default behavior for all Materials in the pack. This means that you can use all Materials successfully on objects that do not have UVs, as is often the case for parts that come from CAD applications.

This triplanar mapping function has several useful features:

* Uses local space positions to avoid textures appearing to slide across the surfaces of the objects.
* Materials keep the same texel ratio when objects are scaled.

The image below illustrates how triplanar mapping uses planar maps projected along the X (red), Y (green), and Z (blue) axis to create a complete procedural UV projection with minimal seams or stretching:

![Illustration of how Triplanar Mapping works](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9696a58-8ee4-4bff-b3ca-fda28c8e1e12/automotive_triplanar.png "Triplanar Mapping illustrated")

However, because the calculations use local space positions, the triplanar UVs are dependent on the original geometry and rotation of the object's geometry relative to its pivot. For best results applying textures, author your objects so that flat surfaces lie close to the XY, XZ, and YZ planes of the objects' local space. If your Static Meshes do have UVs, and you want to use these UVs for texture mapping, enable the **Use Object UVs** option on your Material Instance.

### Ray Tracing Support

All Master Materials are set up to optimize performance for ray tracing by using the **RayTracingQualitySwitchReplace** node to execute a different branch of the Material graph on the second bounce.

![The RayTracingQualitySwitchReplace node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdc43700-b35c-4946-8858-4f78e33c160c/automotive_raytracingqualityswitchreplace.png "The RayTracingQualitySwitchReplace node")

For the second bounce, all surface normals are considered flat, and the surface roughness is considered either fully rough or fully reflective.

## Common Exposed Parameters

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Contains options for Color (RGBA), Color Maps, and Tinting options. |
| **Metalness** | Contains options for Metallic settings. Turning on IsMetallic applies a uniform texture to control the Metallic attribute of the material. Different Metallic Maps can be applied to differentiate between metallic and non-metallic surfaces on the same object. |
| **Roughness** | Contains settings for adjusting the Roughness of your Material. A Roughness Map can be applied to create specific wear patterns. The amount of Roughness can be randomized using Min and Max values. Roughness can be used to determine the glossiness of the Material. |
| **Normal** | Applies the chosen Normal Map to the material. Normal Intensity uses a value to control the effect. |
| **Imperfections** | Allows for the adding of Stains, Fingerprints, and Dust to a Material. A mask texture can be used to apply specific patterns. |
| **UVs** | Allows for the use of an object's own UV map. Triplanar Mapping is enabled by default. |

If you are unsure what a particular parameter is or how it is used, hovering your mouse over it will display additional information.

![Many of the parameters in the pack have informative tooltips](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c729fa2b-e0c0-46ab-8955-790056686358/ap-param-description.png "Many of the parameters in the pack have informative tooltips")

## Master Materials

Inside the **Masters** folder, you will find several types of Master Materials.

### Additive

Useful for creating LCD screens, clocks, HUDs, and other forms of display, the Additive Material features an Intensity setting that makes the display brighter when the camera is facing it and less intense when viewed from the side.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Controls what is displayed on the screen. Facing Intensity affects the brightness when viewing near the center. Edge Intensity affects the brightness when viewing closer to the edges. |

In the example below, the Base Color texture map has been changed to represent a GPS unit:

[![Additive Master Material being used to simulate the screen of a GPS unit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13473072-2623-4bbb-a67a-438d4b85881f/automotive_additive.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13473072-2623-4bbb-a67a-438d4b85881f/automotive_additive.png)

### Brake Rotor

Created to use radial UV mapping, the Brake Rotor Material contains settings for Imperfections such as cracks and stains, as well as the ability to use a Metallic map to add rust. Perfect for creating any Material that requires a radial finish.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Applies a Color Map or color tint to the Material. |
| **Metalness** | Controls whether the Material is meant to be metallic. |
| **Roughness** | Used to apply wear patterns. Also determines the glossiness of the Material. |
| **Cracks** | Applies crack patterns to the Material. Can control both scale and intensity. |
| **Imperfections** | Supports stain imperfections. |

Below, you can see a brake rotor that uses the Material. Metal wear lines have been added, along with stains:

[![A steel brake rotor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6724068-3028-4a5a-92f5-f01ab2383f88/automotive_brakerotor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6724068-3028-4a5a-92f5-f01ab2383f88/automotive_brakerotor.png)

### Car Paint

Designed for car exteriors and brake calipers, the Car Paint Material features support for Flakes, Orange Peel, Chameleon effects, Clear Coat, and Imperfections.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Basic** | Applies a Color Map or color tint to the Material. Contains the setting for the Chameleon effect, which allows for a second color to be chosen. The first color will fade into the second color based on viewing angle. |
| **Clear Coat** | Applies a clear coat to the Material that affects glossiness. The intensity of this effect can be adjusted. |
| **Flakes** | Applies a flake effect to the paint's undercoat. |
| **Imperfections** | Supports fingerprint and dust imperfections. Can control both scale and intensity. |
| **Orange Peel** | Applies the dimple effect that is often seen in car paint. |

The Chameleon effect blends the primary paint color with a secondary color based on the viewing angle:

![Use Chameleon parameter off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6099b07-3175-4ef7-8809-26345960f84e/automotive_chameleonoff.png "Chameleon paramter turned off")

![Use Chameleon parameter on](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d63d997-c9e9-45b3-8492-c2817c756760/automotive_chameleonon.png "Chameleon paramter turned on")

Use Chameleon parameter off

Use Chameleon parameter on

You can see an example of the Clear Coat feature below:

![A Clear Coat Intensity value of 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a33e73d-b2bd-4dde-99a3-8dfbfc04d4be/automotive_clearcoat0.png "Clear Coat Intensity value of 0")

![A Clear Coat Intensity value of 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c38bcd7f-b7a5-49b9-bdf0-98dc4da4a900/automotive_clearcoat1.png "Clear Coat Intensity value of 1")

A Clear Coat Intensity value of 0

A Clear Coat Intensity value of 1

The Flake parameter simulates metal flakes suspended in the paint undercoat and is used to achieve a variety of different finishes:

![Use Flakes off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12d1e5d0-951a-4a96-9e68-c68337e29d75/automotive_flakeoff.png "Use Flakes off]")

![Use Flakes on](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3866aaf9-edea-4eeb-b4bb-f3f5c2e15103/automotive_flakeon.png "Use Flakes on")

Use Flakes off

Use Flakes on

The Orange Peel parameter represents the imperfections that can happen during the automitve paint process:

![Use Orange Peel off](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59cfc13f-96f9-438f-a76d-0cf2b45aa656/automotive_orangepeeloff.png "Use Orange Peel off")

![Use Orange Peel on](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6eef7b1-13aa-47e1-aa0d-677113b2fb4b/automotive_orangepeelon.png "Use Orange Peel on")

Use Orange Peel off

Use Orange Peel on

### Decal

The Decal Material is projected onto a surface and will adjust to follow its contours, manking it perfect for adding logos, stripes, and other decals to the vehicle.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Color Map controls the decal that is displayed. Tint options control the final color of the decal. |

Below you can see the Unreal Engine logo applied as a decal to the hood of the car:

[![The Unreal Engine logo applied as a Decal](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80438887-fd9a-4314-aafe-ee429a02e80d/automotive_decal.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80438887-fd9a-4314-aafe-ee429a02e80d/automotive_decal.png)

### Emissive

Useful for headlights, tail lights, and LED lights, the Emissive Material features color tint and intensity settings that vary depending on the viewing angle.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Light** | Color Tint determines the final color of the Material. Facing Intensity affects the brightness when viewing near the center. Edge Intensity affects the brightness when viewing closer to the edges. |

Here you can see the Emissive Material applied to the brake light:

[![An Emissive Material applied to a brake light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a501d3c4-5f5a-42de-849d-ab427c9a3330/automotive_emissive.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a501d3c4-5f5a-42de-849d-ab427c9a3330/automotive_emissive.png)

### Glass

The Glass Material can be used to create windows, transparent light covers, and windshields.
Windshields require a bit of setup and are made of 2 meshes: one interior and one exterior:

[![Setting up the car windshield using two meshes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1adb5649-1841-48a4-b570-0249cf1e4666/automotive_glass.png "Setting up the car windshield using two meshes")

| **Number** | **Description** |
| --- | --- |
| **1** | Interior Static Mesh using interior glass Material. Translucency Sort Priority property is set to 0. |
| **2** | Exterior Static Mesh using exterior glass Material. Translucency Sort Priority property is set to 1. |

The interior mesh uses the interior windshield Material and hasTranslucency Sort Priority set to 0. While the exterior mesh uses the exterior windshield Material and has Translucency Sort Priority set to 1.

You can see the technique used below. The exterior windshield mesh is reflecting the environment.

[![The exterior windshield relfects the environment](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d29c0061-b708-4c22-84bd-69b17de46d27/automotive_glassexterior.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d29c0061-b708-4c22-84bd-69b17de46d27/automotive_glassexterior.png)

| **Parameter Category** | **Settings** |
| --- | --- |
| **Glass** | Contains options for glass color, roughness, and darkening towards the edges. |
| **Transparency** | Contains options to apply a sun cover around the edge of the windshield. |
| **Imperfections** | Supports dust, fingerprints or stain imperfections. |

### Masked

The Masked Material is used to create perforation or grill patterns for plastics and metals. This is great for components such as speaker covers, and supports clear coat and imperfections in the form of dust and fingerprints.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Applies a Color Map or color tint to the Material. The color map contains your masked texture. |
| **Metalness** | Controls whether the Material is meant to be metallic. |
| **Roughness** | Applies roughness. Can be used to control the glossiness of the Material. |
| **Clear Coat** | Applies a shiny clear coat. |
| **Imperfections** | Supports dust and fingerprint imperfections. |

[![An example of a speaker grill Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a41852da-9b12-4455-91ce-e86dc8a2ae4a/automotive_masked.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a41852da-9b12-4455-91ce-e86dc8a2ae4a/automotive_masked.png)

### Opaque

A flexible Master Material, the Opaque Material is used to make anything that is opaque or has a coating such as metal, carbon fiber, leather, plastic, wood, rubber, or reflectors. It features clear coat and imperfection options, along with a range of color and roughness options.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Applies a Color Map or color tint to the Material. |
| **Metalness** | Controls whether the Material is meant to be metallic. |
| **Roughness** | Applies roughness. Can be used to control the glossiness of the Material. |
| **Clear Coat** | Applies a shiny clear coat. |
| **Imperfections** | Supports dust and fingerprint imperfections. |

Below is an example of the flexibility of this Master Material. The leather of the seats, nylon straps of the seatbelts, and plastic of the interior paneling are all created using the Opaque Master Material:

[![The versatility of the Opaque Master Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/67f7bd5e-d9db-4d80-be76-59c9acc17360/automotive_opaque.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/67f7bd5e-d9db-4d80-be76-59c9acc17360/automotive_opaque.png)

### Textile

Designed to create carpet, headliners, suede, perforated leather or anything with textile properties, the Textile Material features perforation, softness, and imperfection settings.

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Applies a Color Map or color tint to the Material. |
| **Roughness** | Applies roughness. Can be used to control the glossiness of the Material. |
| **Softness** | Applies a softness effect to the Material in the form of core darkness, brightness at the edges, and subsurface color. |
| **Wear** | Applies a wear pattern to the Material. |
| **Perforation** | Applies a mask that simulates perforation. A color tint can be added to the holes. Depth and size can also be controlled. |

In the example below, we can see the Textile Master Material used to create a brown suede:

[![Textile Master Material used to create a brown suede](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69900b17-e90d-40d2-b5fc-6e632a843ba4/automotive_textile.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69900b17-e90d-40d2-b5fc-6e632a843ba4/automotive_textile.png)

### Tint

Used in the setup of taillights, the Tint Material is used to modulate and tint the vehicle lights. Similar to the windshield, taillights can be setup using 3 meshes:

[![Using the Tint Master Material to setup a taillight](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad2192fd-4d72-4808-83d8-2bf1e2e7b4a3/automotive_tint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad2192fd-4d72-4808-83d8-2bf1e2e7b4a3/automotive_tint.png)

| **Number** | **Description** |
| --- | --- |
| **1** | Glass Material |
| **2** | Tint Material |
| **3** | Emissive Material |

| **Parameter Category** | **Settings** |
| --- | --- |
| **Base Color** | Controls the tint color. Can have an additional edge tint that blends to when the viewing angle changes. |

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [automotive](https://dev.epicgames.com/community/search?query=automotive)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#overview)
* [Master Materials and Material Instances](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#mastermaterialsandmaterialinstances)
* [Physically Based Rendering](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#physicallybasedrendering)
* [Triplanar Mapping](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#triplanarmapping)
* [Ray Tracing Support](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#raytracingsupport)
* [Common Exposed Parameters](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#commonexposedparameters)
* [Master Materials](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#mastermaterials)
* [Additive](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#additive)
* [Brake Rotor](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#brakerotor)
* [Car Paint](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#carpaint)
* [Decal](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#decal)
* [Emissive](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#emissive)
* [Glass](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#glass)
* [Masked](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#masked)
* [Opaque](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#opaque)
* [Textile](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#textile)
* [Tint](/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine?application_version=5.7#tint)
