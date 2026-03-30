<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types?application_version=5.7 -->

# Datasmith Supported Software and File Types

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
4. Datasmith Supported Software and File Types

# Datasmith Supported Software and File Types

Details all the third-party software applications and data formats that Datasmith works with.

![Datasmith Supported Software and File Types](https://dev.epicgames.com/community/api/documentation/image/16092a85-de86-4269-97be-5be60fcc99ec?resizing_type=fill&width=1920&height=335)

 On this page

Datasmith currently works with the software applications and file formats listed in the following table.

For each type of software or file format listed, the **Status** column uses the following icons to indicate the level of readiness you should expect:

| Icon | Meaning |
| --- | --- |
| [Production-ready](https://dev.epicgames.com/community/api/documentation/image/afaaf1aa-cc02-4090-9637-1c430a991878?resizing_type=fit) | Production-ready. |
| [Beta or Experimental](https://dev.epicgames.com/community/api/documentation/image/400ec849-12d6-4b01-ac13-62adec8a3fb6?resizing_type=fit) | Beta or Experimental feature, shared with customers for testing and feedback. Expect changes, and we may deprecate functionality at our discretion. |

The **Workflow Type** indicates how you package the information from your design application:

* **Direct** means that the Datasmith Importer Plugin in Unreal reads the application's file format directly.
* **Export** means that you need to export the content from your application to a specific file format before Datasmith can import it into Unreal Engine. You export the content using functionality that is already built into your application.
* **Export Plugin** means that you need to install a new plugin into your application in order to export your design data into the format that Datasmith imports into Unreal.

The **Importer Plugin** column below tells you which Datasmith importer plugin you need to enable in your Unreal Engine Project to be able to import files of each type. For more information about this process, see [Importing Datasmith Content into Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine)

You can download all Datasmith exporter plugins from the [Datasmith exporter plugins](https://www.unrealengine.com/en-US/datasmith/plugins) page.

## Supported Applications

| Application | Support Level | Version | Workflow Type | Importer Plugin |
| --- | --- | --- | --- | --- |
| **3D ACIS** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/1ca5d42d-54ee-4205-8797-2e7b1105b72f?resizing_type=fit) | Up to 2023 | Direct | **CAD** |
| **3DEXCITE DELTAGEN** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/17835215-0842-4e3a-9444-6cadb8cd56c4?resizing_type=fit) | 2017–2024 | Export (FBX only) | **FBX** |
| **ArcGIS CityEngine** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/ad14ec26-24c2-483e-8406-b7227d9c90a9?resizing_type=fit) | -- | Export Plugin | **Datasmith** |
| **Autodesk 3ds Max** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/98767c42-ae80-40e7-a4cd-98d6a2df3006?resizing_type=fit) | 2016–2026 | Export Plugin | **Datasmith** |
| **Autodesk Alias** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/f27a7b43-8722-41ff-acee-366e57850ac3?resizing_type=fit) | Up to 2025 | Direct | **CAD** |
| **Autodesk AutoCAD** | [Beta or Experimental](https://dev.epicgames.com/community/api/documentation/image/5c5fc95a-d100-4bed-bec7-8ef059a8e6ee?resizing_type=fit) | -- | Direct | **CAD** |
| **Autodesk Inventor** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/a574b747-abb9-484f-83e9-268119890b30?resizing_type=fit) | Up to 2025 | Direct | **CAD** |
| **Autodesk Revit** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/81aa231e-4290-4f6c-bc06-7ece4f698522?resizing_type=fit) | 2016.3–2023\* | Export Plugin | **Datasmith** |
| **Autodesk Navisworks** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/84cc85bb-01ab-4d66-9975-330492be48a0?resizing_type=fit) | 2019–2026 | Export Plugin | **Datasmith** |
| **Autodesk VRED** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/a8c7e83d-1212-4bb8-89d3-cd4d7aa0cf0a?resizing_type=fit) | VRED Professional 2018–2026 | Export Plugin | **FBX** |
| **Dassault Systèmes CATIA V5** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/006eaf29-0143-4692-a485-cfbe45836e04?resizing_type=fit) | Up to V5\_6 R2024 | Direct | **CAD** |
| **Dassault Systèmes SOLIDWORKS** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/0e4ce760-d26b-4b80-9f37-d89371f148af?resizing_type=fit) | Up to 2025 | Export Plugin | **CAD** |
| **Dassault Systèmes SOLIDWORKS** | [Beta or Experimental](https://dev.epicgames.com/community/api/documentation/image/58292a02-2979-4f10-a977-3096023a08e0?resizing_type=fit) | 2020–2025 | Direct | **Datasmith** |
| **Graphisoft Archicad** | [Beta or Experimental](https://dev.epicgames.com/community/api/documentation/image/49f371d8-fc99-4bde-9d22-105b27d52716?resizing_type=fit) | 23–28 | Export Plugin | **Datasmith** |
| **Maxon Cinema 4D** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/357f7ac7-ac31-4336-9680-12ae8744ed6c?resizing_type=fit) | -- | Direct | **C4D** |
| **McNeel Rhinoceros** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/59f1fe0d-53fe-4541-ba39-de5da16c00e0?resizing_type=fit) | up to 8 | Export Plugin | **Datasmith** |
| **McNeel Rhinoceros** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/b145fca7-fe02-49e0-a560-05909a020285?resizing_type=fit) | up to 8 | Direct (`.3dm` files) | **Datasmith** |
| **PTC Creo (Pro/ENGINEER)** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/59b37b97-2b5e-4300-a593-943090e27bfe?resizing_type=fit) | Pro/Engineer 19.0 to Creo 11.0 | Direct | **CAD** |
| **Siemens NX** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/7678233b-70af-42d5-9c43-e4c1f69692a9?resizing_type=fit) | V11–V18, NX–NX12, NX1847–NX2412 | Direct | **CAD** |
| **Trimble SketchUp Pro** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/44c3e36a-de4b-4392-be4f-55ad0ddb151b?resizing_type=fit) | 2019–2025 | Export Plugin, DirectLink | **Datasmith** |

\* As of Unreal Engine 5.3, Autodesk now manages newer versions of the Revit exporter plugin and is shipped directly in Revit 2024+. UE still supports this plugin and you can get older versions of the plugin from the download page.

## Supported File Formats and Standards

| File Format or Standard Name | Support Level | Version | Workflow Type | Importer Plugin |
| --- | --- | --- | --- | --- |
| **3DXML** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/4e43aae1-1233-4323-8b3e-cca2aed50ec7?resizing_type=fit) | Up to V5-6 R2024 | Direct | **CAD** |
| **Industry Foundation Classes (IFC)** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/026eb6a8-1dc3-46da-b02d-12a45c3508b2?resizing_type=fit) | IFC2x Editions 2-4, 4x3 (Beta) | Direct | **CAD** |
| **Initial Graphics Exchange Specification (IGES)** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/ecfcfbe1-831a-44e0-9947-ae26132a07ba?resizing_type=fit) | 5.1, 5.2, 5.3 | Direct | **CAD** |
| **JT Open** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/0013068f-b4b9-42f1-a2b3-283a1d5a6b1c?resizing_type=fit) | Up to 10.9 | Direct | **CAD** |
| **Parasolid (x\_t)** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/c9213214-6ec2-4180-9b19-02a9f13b23f8?resizing_type=fit) | up to 37.1 | Direct | **CAD** |
| **Siemens PLM XML** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/fa524200-b387-40f5-9ebf-079c9348921d?resizing_type=fit) | 7.0.3 and later (Compatible with TeamCenter 11 or later) | Direct | **CAD** |
| **STEP** | [Production-ready](https://dev.epicgames.com/community/api/documentation/image/da01f6b7-101f-43d7-98e4-2b21d4ab930e?resizing_type=fit) | AP203, AP214, AP242 Ed2 and Ed3 | Direct | **CAD** |

### Export Plugins for macOS

Most **Export Plugins**, as well as all Datasmith importers in the Unreal Editor, are currently only available for Microsoft Windows platforms. As of Unreal Engine 4.27, we also support exporting from the following applications on macOS:

| Application | Supported Versions |
| --- | --- |
| Trimble SketchUp Pro | 2019–2025 |
| Graphisoft Archicad | 23–28 |
| McNeel Rhinoceros | 6, 7, 8 |

## Formats that Unreal Engine Supports Directly

Unreal Engine offers built-in support for importing and exporting FBX files.

These FBX-based workflows are optimized to support game requirements, which tend to be focused on working with individual objects. Datasmith, by contrast, brings in entire scenes, potentially containing thousands of objects, each with its materials, pivots, scale, hierarchy, and metadata, from a wide range of sources. However, you should feel free to use the FBX import pipeline if it suits your needs. For example, you might use it to import pieces of additional set dressing that you'll use to augment your Datasmith content in your Unreal Level.

For details, you can read about our [FBX Content Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-content-pipeline).

## Backward Compatibility

Sometimes, we may need to change the Datasmith file format and the behavior of the importer plugins in order to add new features. We do not guarantee backward compatibility between all versions of Unreal and all versions of the Datasmith export plugins. Although you may be able to import a `.udatasmith` file generated with an older version of an export plugin into a newer version of Unreal Engine, we do not recommend depending on it.

Always use the version of an export plugin that matches the Unreal Engine and Datasmith plugin versions that you need to use the exported file with. To get the most out of Datasmith, and to make sure you benefit from the latest fixes and features, we recommend always using the latest available version of Unreal Engine and the export plugins.

* [reference](https://dev.epicgames.com/community/search?query=reference)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [simulation](https://dev.epicgames.com/community/search?query=simulation)
* [architecture](https://dev.epicgames.com/community/search?query=architecture)
* [supported software](https://dev.epicgames.com/community/search?query=supported%20software)
* [file types](https://dev.epicgames.com/community/search?query=file%20types)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Supported Applications](/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types?application_version=5.7#supported-applications)
* [Supported File Formats and Standards](/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types?application_version=5.7#supported-file-formats-and-standards)
* [Export Plugins for macOS](/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types?application_version=5.7#export-plugins-for-mac-os)
* [Formats that Unreal Engine Supports Directly](/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types?application_version=5.7#formats-that-unreal-engine-supports-directly)
* [Backward Compatibility](/documentation/en-us/unreal-engine/datasmith-supported-software-and-file-types?application_version=5.7#backward-compatibility)
