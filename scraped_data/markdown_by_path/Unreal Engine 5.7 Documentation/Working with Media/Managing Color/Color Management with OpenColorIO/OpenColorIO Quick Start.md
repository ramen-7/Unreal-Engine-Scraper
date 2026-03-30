<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7 -->

# OpenColorIO Quick Start

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Managing Color](/documentation/en-us/unreal-engine/managing-color-in-unreal-engine "Managing Color")
7. [Color Management with OpenColorIO](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine "Color Management with OpenColorIO")
8. OpenColorIO Quick Start

# OpenColorIO Quick Start

Create OpenColorIO Configuration Assets from OpenColorIO configuration files.

![OpenColorIO Quick Start](https://dev.epicgames.com/community/api/documentation/image/0bcf491c-e98c-4400-9e33-0e0e5e1c9dc6?resizing_type=fill&width=1920&height=335)

 On this page

This page guides you through getting started with OpenColorIO (OCIO) in Unreal Engine (UE). It shows you how to create an **\*\*OpenColor Configuration Asset**\*\* from an OCIO Config.

After creating this file, you can use OCIO to apply color transformations by using [Blueprints](/documentation/en-us/unreal-engine/converting-colors-in-unreal-engine-blueprints) and in UE's [Viewport and Play in Editor modes](/documentation/en-us/unreal-engine/apply-color-conversion-to-the-level-viewport-and-play-in-editor-with-opencolorio-in-unreal-engine).

## Prerequisites

The OpenColorIO plugin is automatically enabled by UE when you create a new project.
If the OpenColorIO plugin is disabled, you must enable it to use OCIO in UE. For information about enabling plugins in UE, see [Working with Plugins](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).

## OCIO Configs

OCIO configs contain sets of color spaces, displays and views that you can use with OCIO. You can use your own OCIO config file, one of the default ACES configs provided with the OCIO plugin, or one of the ACES config files from the [Academy Software Foundation](https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES/releases/tag/v1.0.0) GitHub repo.

## Using a Built-in OCIO Config

You can use one of the built-in OCIO configs by entering one of the following strings into your OpenColorIO Configuration Asset's **Configuration File** path (see Create an OpenColorIO Configuration Asset). These config files are built into the OCIO library and do not require any external files.

* To use the [default ACES CG config](https://opencolorio.readthedocs.io/en/latest/releases/ocio_2_2.html#built-in-configs), enter this string into the **Configuration File** path: `ocio://default`
* To use the ACES CG config, enter this string into the **Configuration File** path: `ocio://cg-config-v1.0.0_aces-v1.3_ocio-v2.1`
* To use the ACES Studio config, enter this string into the **Configuration File** path: `ocio://studio-config-v1.0.0_aces-v1.3_ocio-v2.1`

## Importing an OCIO Config File

To add an OCIO config (`ocio` or `.ocioz`) file to your project, you must use your computer's file explorer to add the file to your project's Content folder. UE does not automatically recognize `.ocio` or `.ocioz` files, so you cannot add them to your project by using the Content Drawer within UE.

The OCIO plugin also supports `.ocioz` archive files. These can be useful if you want to compress a config file and its LUT texture folder into a single archive.

## Example OCIO Config File

Epic have created an example `.ocio` config file as part of the OCIO plugin. This example config file is located in your engine install folder under `Engine\Plugins\Compositing\OpenColorIO\Content\OCIO`.

When you browse to the OpenColorIO plugin's contents in the Content Browser, the Content Browser does not show these files since it only shows .uasset files. Use your computer's file explorer to browse to the files instead.

## Create an OpenColorIO Configuration Asset

The OCIO plugin uses an OpenColorIO Configuration Asset to manage the color profiles you want to use in your project. This asset references an OCIO config, which contains detailed specifications about multiple color profiles and how to transform between them.

UE currently supports OCIO v2.2. For more details on OCIO config files, refer to the [OpenColorIO v2 documentation](https://opencolorio.readthedocs.io/en/latest/index.html) and the [OCIO v2.2 release information](https://opencolorio.readthedocs.io/en/latest/releases/ocio_2_2.html).

Before using OCIO you must create an OpenColorIO Configuration Asset..

To create an OpenColorIO Configuration Asset:

1. In the [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine), right-click to open the context menu and select **Miscellaneous > OpenColorIO Configuration** to create an **OpenColorIO Configuration Asset**.

   ![Create an OpenColorIO Configuration Asset ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a404fa8-ef47-4bdf-bd58-01e9f39b229d/create-ocio-config-asset.png)
2. Double-click your **OpenColorIO Configuration Asset** to edit its settings. In this example, the Asset is named **OCIO\_Example**.

   ![Edit the OpenColorIO Configuration Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcc9d37c-c1e5-4114-87b8-e7a7ebefdd7e/ocio-config-asset-settings.png)
3. For the **Configuration File** parameter, click **Browse** to locate and select an OCIO config (`.ocio`) file on your computer or enter a URL to use one of the built-in configs. By default, new OpenColor Configuration Assets use the `ocio://default` OCIO config.

   ![Select a Configuration File](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08da7692-1383-45f2-bffa-228b5d39a5d9/set-ocio-configuration-file.png)
4. For the **Desired Color Spaces** parameter, click **Add (+)** to add a new color space entry.

   ![Add a new color space](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5609db12-dd1c-4d09-acc8-7c909e9bd259/add-new-color-space.png)
5. In the new entry, open the drop-down list and select one of the color spaces defined in the config file that you want to use in UE.

   ![Select the color space you want to use](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96950455-dc41-4c4d-b455-3b2f3133e82e/set-color-space.png)
6. Repeat the last two steps for each color space or display view you want to use, then **Save** your Asset.

   ![Add extra color spaces](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1114d195-9078-4264-83da-97ff44345c16/ocio-config-asset-with-color-spaces-added.png)

Only set up the color profiles you actually need to use in UE. This helps your configuration Asset remain as lightweight as possible.

Your OpenColorIO Configuration Asset is now set up so you can use it to apply color transformations to different systems in the engine.

## Configure the OpenColorIO Configuration Asset

![The OCIO Configuration Asset details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da190c1b-7053-401b-8c4f-3376ef31f696/generic-apply-ocio-asset.png)

While the method to set up color conversions for systems in UE may be different, the color conversion settings with OpenColorIO are the same. You'll need to specify which OpenColorIO Configuration Asset to use, and the source and destination color spaces:

* **Configuration Source:** The OpenColorIO Configuration Asset you're using.
* **Source Color Space:** The input color space you want to convert from.
* **Destination Color Space:** The output color space you want to convert to.
* **Destination Display View**: The display view that you want to convert colors in.

* [vfx](https://dev.epicgames.com/community/search?query=vfx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#prerequisites)
* [OCIO Configs](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#ocioconfigs)
* [Using a Built-in OCIO Config](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#usingabuilt-inocioconfig)
* [Importing an OCIO Config File](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#importinganocioconfigfile)
* [Example OCIO Config File](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#exampleocioconfigfile)
* [Create an OpenColorIO Configuration Asset](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#createanopencolorioconfigurationasset)
* [Configure the OpenColorIO Configuration Asset](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine?application_version=5.7#configuretheopencolorioconfigurationasset)
