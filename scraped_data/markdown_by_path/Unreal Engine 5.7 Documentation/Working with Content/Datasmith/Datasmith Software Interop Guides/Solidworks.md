<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7 -->

# Solidworks

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine "Datasmith")
7. [Datasmith Software Interop Guides](/documentation/en-us/unreal-engine/datasmith-software-interop-guides-for-unreal-engine "Datasmith Software Interop Guides")
8. Solidworks

# Solidworks

Describes how to install the Datasmith Solidworks Exporter plugin, how to get Solidworks content into Unreal Engine, and how Datasmith coverts Solidworks content.

![Solidworks](https://dev.epicgames.com/community/api/documentation/image/043423c1-7554-4b0b-a4e9-4185549f241d?resizing_type=fill&width=1920&height=335)

 On this page

This page describes how to install the Datasmith Solidworks Exporter plugin, how to get Solidworks content into Unreal Engine using Datasmith, and how Datasmith imports scenes from Solidworks into Unreal Engine.

## Download and install the Solidworks Exporter Plugin

To export Solidworks content with Datasmith, download and install the **Solidworks Exporter** plugin from the [Datasmith Export Plugins](https://www.unrealengine.com/en-US/datasmith/plugins) page.

Make sure to download the plugin for the version of Unreal Engine you plan to use.

To see what versions of Solidworks the plugin supports, see .

### Install the Solidworks Exporter Plugin

Before you install the Solidworks Exporter plugin:

* Uninstall any previous versions of the plugin from your machine.
* Make sure that Solidworks is not running on your machine.

To install the plugin, open the installer and follow the instructions.

If the plugin installer detects multiple versions of Solidworks on your machine, and at least one of these versions is supported, it will install the export plugin for all of the Solidworks versions it detects.

### Uninstall the Solidworks Exporter Plugin

To uninstall the plugin, locate it in the Windows **Control Panel**, and remove it as you would any other Windows application.

## Datasmith Workflows for Solidworks

You can get Solidworks content into Unreal Engine in the following ways:

* Export a Solidworks scene as a `.udatasmith` file, and import it into Unreal Engine.
* Use Direct Link to preview changes to your Solidworks scene in Unreal Engine in real time.

### Export Content From Solidworks

To export Solidworks content as a `.udatasmith` file, you need to:

1. [Install the **Solidworks Exporter** Plugin](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine#installthesolidworksexporterplugin).
2. In Solidworks, load the scene you want to export.
3. From the main toolbar, open the Save menu (floppy disk icon), and select Save As.

   ![Save As button in Solidworks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b76604f6-69aa-480c-8dc1-b09f9618b516/solidworks-saveas.png)
4. In the **Save As** window, set **Save as type** to **Unreal (`*.udatasmith`)**.

Datasmith saves your scene as a `.udatasmith` file that you can import into Unreal Engine. For details, see [Importing Datasmith Content into Unreal Engine](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine).

If you need to perform additional cleaning, merging, or other modifications to Solidworks data during the import process, you can use Dataprep. For details, see [Dataprep Import Customization](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine).

### Preview Solidworks Content with Direct Link

Instead of manually re-importing a Solidworks scene into Unreal Engine every time you make a change, you can set up a Datasmith DirectLink between Solidworks and Unreal Engine to preview changes to your scene in real time. When you set up a Direct Link, the Unreal Engine preview updates whenever you make a change to the scene in Solidworks.

For more information, see [Using Datasmith Direct Link](/documentation/en-us/unreal-engine/using-datasmith-direct-link-in-unreal-engine).

In Solidworks, Datasmith Direct Link is available from the Unreal tab of the main toolbar.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19c8373d-0359-4e30-89be-f3f10c8d4f03/datasmith-solidworks-tab.png "Datasmith tools in Solidworks")


You must [Install the **Solidworks Exporter** Plugin](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine#installthesolidworksexporterplugin) to access Datasmith features, including DirectLink, in Solidworks.

## How Datasmith Imports Content from Solidworks

This section describes what happens when you use Datasmith to convert and import objects from Solidworks scenes into elements in an Unreal Engine Project. Datasmith follows the process outlined in the [Datasmith Overview](/documentation/en-us/unreal-engine/datasmith-plugins-overview) and [About the Datasmith Import Process](/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine), but adds some special translation behavior that is specific to Solidworks.

### Solidworks Feature Support

The Datasmith Solidworks exporter supports the following features:

* Product structure
* Solid geometry
* Textures and materials
* Display states
* Configurations
* Metadata

The following features are **not** supported.

* Animations
* Lights
* Cameras
* Construction geometry: points, curves, planes

### Converted Entities

When you import a `.udatasmith` file into Unreal Engine, Datasmith converts the following Solidworks entities into their Unreal Engine counterparts:

| Solidworks | Unreal Engine |
| --- | --- |
| Sub-assembly | Actor |
| Part | Static Mesh |
| Part Instance | Static Mesh Actor |
| Configuration | Variant |
| Display State | Variant |
| Appearance | Material |

### Solidworks Data Loading Models

When you open an assembly file, Solidworks can load its active components as either **lightweight** or **fully resolved**. Depending on the selected mode, data from the model may or may not be available in Solidworks.

We recommend opening assemblies in **fully resolved** mode to guarantee that the most amount of information will be transferred through Datasmith.
For more information, see Solidworks documentation on [Components](http://help.solidworks.com/2021/english/SolidWorks/sldworks/c_lightweight_components_swassy.htm).

### Materials and UVs

Solidworks does not have data for UVs associated with parts. Unlike Unreal Engine, Solidworks stores mapping information per material. When exporting data into a `.udatasmith` file, the Datasmith exporter bakes UVs into the static meshes using the material information. So, if a part is instantiated several times in the Solidworks assembly, and each part instance uses different materials, it may end up with multiple static meshes in Unreal Engine.

### Configurations and Display States

If the Solidworks model has display states or configurations, Datasmith may create a Level Variant Set asset. This asset will hold the translated variant entity.
For more information, see Solidworks documentation on [Configurations](http://help.solidworks.com/2021/english/SolidWorks/sldworks/c_Configurations_Overview.htm).

### Metadata

When you import a SolidWorks file, Datasmith adds a minimal amount of pre-set metadata to each Static Mesh Actor it creates, to indicate the part name and assembly of that mesh in the original SolidWorks design. Datasmith does not currently carry over any custom metadata properties that you add to your parts and assemblies.

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [solidworks](https://dev.epicgames.com/community/search?query=solidworks)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Download and install the Solidworks Exporter Plugin](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#downloadandinstallthesolidworksexporterplugin)
* [Install the Solidworks Exporter Plugin](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#installthesolidworksexporterplugin)
* [Uninstall the Solidworks Exporter Plugin](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#uninstallthesolidworksexporterplugin)
* [Datasmith Workflows for Solidworks](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#datasmithworkflowsforsolidworks)
* [Export Content From Solidworks](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#exportcontentfromsolidworks)
* [Preview Solidworks Content with Direct Link](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#previewsolidworkscontentwithdirectlink)
* [How Datasmith Imports Content from Solidworks](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#howdatasmithimportscontentfromsolidworks)
* [Solidworks Feature Support](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#solidworksfeaturesupport)
* [Converted Entities](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#convertedentities)
* [Solidworks Data Loading Models](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#solidworksdataloadingmodels)
* [Materials and UVs](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#materialsanduvs)
* [Configurations and Display States](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#configurationsanddisplaystates)
* [Metadata](/documentation/en-us/unreal-engine/using-datasmith-with-solidworks-in-unreal-engine?application_version=5.7#metadata)
