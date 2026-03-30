<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7 -->

# Importing and Exporting Landscape Heightmaps

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
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. [Creating Landscapes](/documentation/en-us/unreal-engine/creating-landscapes-in-unreal-engine "Creating Landscapes")
8. Importing and Exporting Landscape Heightmaps

# Importing and Exporting Landscape Heightmaps

How to import and export your custom Landscape heightmaps using Unreal Engine

![Importing and Exporting Landscape Heightmaps](https://dev.epicgames.com/community/api/documentation/image/26a3766a-b0d0-475f-9132-7b9e544c813a?resizing_type=fill&width=1920&height=335)

 On this page

The Unreal Engine Landscape system stores height data in a heightmap, a grayscale image that uses black and white color values to store terrain elevations. In a heightmap, a value of pure black (0 in all RGB color channels) represents the lowest point and a value of pure white (255 in all RGB color channels) represents the highest point.

[![An example of a grayscale heightmap exported from Gaea showing mountains](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88d90d6d-29c5-45de-8bc7-34f6d305aa31/heightmap-example.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88d90d6d-29c5-45de-8bc7-34f6d305aa31/heightmap-example.png)

An example of a grayscale heightmap exported from Gaea.

Unreal Engine supports heightmaps created using terrain generation applications (such as Gaea, World Machine, Terragen, or Houdini) or handpainted in image editing applications using the following formats:

* 16-bit grayscale PNG
* 8-bit grayscale r8
* 16-bit grayscale r16

Unreal Engine also supports RAW format heightmaps using a JSON sidecar file. For more information, see [Landscape Technical Guide](/documentation/en-us/unreal-engine/landscape-technical-guide-in-unreal-engine#importingrawformatheightmaps).

## Importing a Custom Heightmap

Imported Heightmaps can be used when creating a landscape or applied to an existing landscape using the **Import** tool. Unreal Engine also supports large world creation using [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine) and the ability to import tiled heightmaps.

### Import Heightmap for New Landscape

To import a heightmap during landscape creation:

[![Settings menu for importing a heightmap on to a new landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97081543-f939-49f2-93fb-b61620042e66/new-import-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97081543-f939-49f2-93fb-b61620042e66/new-import-settings.png)

Settings menu for importing a heightmap on to a new landscape.

1. Enter **Landscape** mode.
2. Click **Import from File**. If using [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine), adjust the following additional settings.
   1. Adjust the **World Partition Grid Size**.
   2. Adjust the **World Partition Region Size**.
3. Click the button next to **Heightmap File** and select your heightmap.
   1. If your heightmap is tiled, Unreal asks if you would like to use the tiled image path.
   2. Click **Yes** to continue.
4. Calculate the Z scale for your heightmap.
   1. The Z scale equation is (Max height of your heightmap in meters) x (100 to convert to centimeters) x 0.001953125. For more information on calculating Z scale, see [Landscape Technical Guide](/documentation/en-us/unreal-engine/landscape-technical-guide-in-unreal-engine).

      You may be required to adjust the X and Y scale of your heightmap based on the application used to generate it. Refer to the application's documentation for details.
5. Click **Import**.

### Import Heightmap for Existing Landscape

To import a heightmap onto an existing landscape:

[![Settings menu for importing a heightmap on to an exisiting landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/444e96f8-13d0-4e2b-8a0c-b41d9d531d7d/existing-import-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/444e96f8-13d0-4e2b-8a0c-b41d9d531d7d/existing-import-settings.png)

Settings menu for importing a heightmap on to an exisiting landscape.

1. Enter **Landscape** mode.
2. In **Manage** mode, click the **Import** tool.
3. Click the button next to **Heightmap File** and select your heightmap.
   1. If your heightmap is tiled, Unreal will ask if you would like to use the tiled image path.
   2. Click **Yes** to continue.
4. Adjust the settings as needed. For more information, see [Landscape Import Settings](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine#landscapeimportsettings).
5. Adjust the **Import Type**. If you are using [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine), select **Subregion**.
6. Adjust the **Mode** option to **All**.
7. Click **Import**.

## Landscape Import Settings

### Import Settings - New Landscape

| **Option** | **Description** |
| --- | --- |
| **Enable Edit Layers** | Toggles support for [Landscape Edit Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine). |
| **Flip Y Axis** | Flips the Y coordinate of the imported file. This is used to resolve issues where tiled heightmaps do not fit together properly when imported. |
| **World Partition Grid Size** | Defines the number of Landscape Streaming Proxies per landscape component used along the X and Y axis. Requires [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine). |
| **World Partition Region Size** | Defines the number of landscape components per World Partition Region on each axis. Requires [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine). |
| **Heightmap File** | Selects which heightmap file to import. |
| **Heightmap Resolution** | Defines the heightmap resolution. Unreal Engine reads this from your heightmap file and auto populates it with the correct value. |
| **Material** | Defines the landscape material initially applied to the landscape. |
| **Layer Alphamap Type** | Defines whether the new landscape layers that are created are **Additive** or **Layered** (weight blended). Only available when you have selected a default material. |
| **Layers** | Shows the landscape layers that will be created on import. Only available when you have selected a default material. |
| **Location** | Defines the location of the new landscape. |
| **Rotation** | Defines the rotation of the new landscape. |
| **Scale** | Defines the distance between each vertex on the new landscape. For more information on calculating landscape scale, see [Landscape Technical Guide](/documentation/en-us/unreal-engine/landscape-technical-guide-in-unreal-engine). |
| **Section Size** | Defines the number of quads in a landscape section. One section is the unit of LOD transition during landscape rendering. |
| **Sections Per Component** | Defines the number of sections in each landscape component.This value and Section Size determine the size of each landscape component. For more information on landscape components, see [Landscape Technical Guide](/documentation/en-us/unreal-engine/landscape-technical-guide-in-unreal-engine). |
| **Number of Components** | Determines the number of components in the X and Y axis. This value determines the overall size of the landscape. |
| **Overall Resolution** | Displays the final overall resolution of the landscape. |
| **Total Components** | Displays the total number of components in the landscape. |
| **Edit Layers** | Displays the edit layers that will be created on the new landscape. |
| **Edit Layer Blueprint Brushes** | Displays the edit layer blueprint brushes that will be created on the new landscape. |

### Import Settings - Existing Landscape

| **Option** | **Description** |
| --- | --- |
| **Heightmap File** | Selects which heightmap file to import. |
| **Import Type** | Determines the handling of the imported height data. This drop down has the following options:   * **Original**: Imports the heightmap data at the gizmo location and at the original size. * **Expand**: Imports the data at the gizmo location and expands the data to fit the landscape. * **Resample**: Resamples the imported data to fit the landscape. * **Subregion**: Imports the heightmap data at the gizmo location without resolution checks. |
| **Flip Y Axis** | Flips the Y coordinate of the imported file. This is used to resolve issues where tiled heightmaps do not fit together properly when imported. |
| **Import Resolution** | Defines the imported heightmap resolution. Unreal Engine reads this from your heightmap file and auto populates it with the correct value. |
| **Layers** | Shows the landscape layers that will be created on import. Only available when you have selected a default material. |
| **Mode** | Determines whether to import only the loaded regions or all regions. |
| **Snap Gizmo to Landscape grid** | Determines the handling of the imported height data. This drop down has the following options:   * **None**: No snapping. * **Texel**: Snap using texel size. * **Component**: Snaps using landscape component size. |
| **Edit Layers** | Displays the edit layers that will be created on the landscape. |
| **Edit Blueprint Layers** | Displays the edit layer blueprint brushes that will be created on the landscape. |

## Exporting a Heightmap

Unreal Engine can export your heightmap file as a 16-bit grayscale .png or a 16-bit grayscale .r16 file with a variety of supported options.

### Export Heightmap

To export your heightmap:

[![Settings menu for exporting a heightmap on from an exisiting landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcbe8381-5230-489a-8003-f789211e7012/export-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcbe8381-5230-489a-8003-f789211e7012/export-settings.png)

Settings menu for exporting a heightmap on from an exisiting landscape.

1. Enter **Landscape** mode.
2. In **Manage** mode, click the **Import** tool.
3. Click **Export**.
4. Click the checkbox button next to **Heightmap File** and then click the button next to the text box to select your heightmap.
5. Name your file and select the **Save as type**. Once done, click the **Save** button.
6. Adjust the settings as needed. For more information, see [Landscape Export Settings](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine#landscapeexportsettings).
7. Click **Export**.

## Landscape Export Settings

| **Option** | **Description** |
| --- | --- |
| **Heightmap File** | Selects the file name and file location of the new exported heightmap file. |
| **Flip Y Axis** | Flips the Y coordinate of the exported file. |
| **Export Single File** | Exports the heightmap as a single file. Exports the heightmap as a tiled heightmap, if false. Requires [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine). |
| **Export Selected Edit Layer** | Exports the selected edit layer. If false, exports the blended result of all edit layers layers. |
| **Layers** | Shows the landscape layers that will be exported. |
| **Mode** | Determines whether to export only the loaded regions or all regions. |
| **Snap Gizmo to Landscape grid** | Determines the handling of the imported height data. This drop down has the following options:   * **None**: No snapping. * **Texel**: Snap using texel size. * **Component**: Snaps using landscape component size. |
| **Edit Layers** | Displays the edit layers that will be exported with the landscape. |
| **Edit Layer Blueprint Brushes** | Displays the edit layer blueprint brushes that will be exported with the landscape. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Importing a Custom Heightmap](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#importingacustomheightmap)
* [Import Heightmap for New Landscape](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#importheightmapfornewlandscape)
* [Import Heightmap for Existing Landscape](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#importheightmapforexistinglandscape)
* [Landscape Import Settings](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#landscapeimportsettings)
* [Import Settings - New Landscape](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#importsettings-newlandscape)
* [Import Settings - Existing Landscape](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#importsettings-existinglandscape)
* [Exporting a Heightmap](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#exportingaheightmap)
* [Export Heightmap](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#exportheightmap)
* [Landscape Export Settings](/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine?application_version=5.7#landscapeexportsettings)
