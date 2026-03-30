<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-supported-platforms?application_version=5.7 -->

# Datasmith Supported Platforms

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
4. Datasmith Supported Platforms

# Datasmith Supported Platforms

Details what Datasmith features work on which different platforms.

![Datasmith Supported Platforms](https://dev.epicgames.com/community/api/documentation/image/54b9f4c7-bbe6-44ec-b1b2-4206dc70268f?resizing_type=fill&width=1920&height=335)

 On this page

This page describes which features of Datasmith work on which different platforms when you download Unreal Engine through the Epic Games Launcher, and when you build the engine yourself from its source code distribution.

## Supported File Formats by Platform

Some components used internally by the different Datasmith importers only work on selected Unreal Engine platforms.

| Source format | 64-bit Windows | Mac OS X | Linux |
| --- | --- | --- | --- |
| **.udatasmith files** | [Supported](https://dev.epicgames.com/community/api/documentation/image/0f771c6e-1cbd-447b-8dcc-e357b577a947?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/eab757b9-3a0e-4085-9524-3ee752430ad3?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/643fab5b-b4af-4717-a8be-ddada133fabf?resizing_type=fit) |
| **CAD file formats** | [Supported](https://dev.epicgames.com/community/api/documentation/image/9fef861f-391e-4732-9e55-190fa3ccf34a?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/73b24d0d-9270-4107-bd9e-5525ed846e71?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/34946cb1-c191-4842-be8e-a9811cf5b88b?resizing_type=fit) |
| **Alias .wire** | [Supported](https://dev.epicgames.com/community/api/documentation/image/28b51d09-46d5-4565-91bb-109a65f4c190?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/7293a416-13a0-4482-a198-ab0fa5aa6571?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/b769e9ab-a2ac-41e9-bd2a-794429d4fd19?resizing_type=fit) |
| **Rhino** | [Supported](https://dev.epicgames.com/community/api/documentation/image/9a332600-7c20-4080-b19d-5876507185f7?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/cd49c9b8-aac2-4740-a1fd-902b3dc70aba?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/e0a62d35-9aab-4804-a30c-9526265386ab?resizing_type=fit) |
| **Cinema 4D** | [Supported](https://dev.epicgames.com/community/api/documentation/image/7ab58086-ef48-4e23-bd93-9e8a37d955a9?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/aebceb5b-94c7-4d3f-b4b4-f5b2b2de4eaf?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/9a692a46-3080-4993-83b5-560d58cad2cc?resizing_type=fit) |
| **AxF** | [Supported](https://dev.epicgames.com/community/api/documentation/image/733e1958-8e4b-4421-8e5e-6be4361b03b3?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/d0421700-8517-487f-8497-d7456ea7c327?resizing_type=fit) | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/fbe6b4ce-e892-4aaf-81b2-dd237225f347?resizing_type=fit) |
| **MDL** | [Supported](https://dev.epicgames.com/community/api/documentation/image/251f5d8f-e117-42e7-9582-6382f6d43be8?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/a7fcf2f8-cba0-4e8b-a473-3d42f4bf5ba7?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/a85e53af-a15b-47d6-b55f-4856c2798622?resizing_type=fit) |
| **Deltagen and VRED** | [Supported](https://dev.epicgames.com/community/api/documentation/image/2ce3d818-f0ee-4491-9914-bb42a4ecd6c8?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/b0bc3df7-8674-4af8-ad2d-fdeca4ec2484?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/9bfd35a9-2e2e-4be1-b912-727aa17f3d5f?resizing_type=fit) |

## Rebuilding Unreal Engine from Source

Some components used internally by the Datasmith importers are not redistributable as part of the Unreal Engine source code. Therefore, you can't rebuild Unreal Engine yourself with support for the features provided by these components.

When you rebuild Unreal Engine yourself from its source code distribution, the Datasmith import plugins support the following formats:

| Source format | Rebuildable? |
| --- | --- |
| **.udatasmith files** | [Supported](https://dev.epicgames.com/community/api/documentation/image/e381353a-6f8f-4f08-93c5-2abe43fd6daf?resizing_type=fit) |
| **CAD file formats** | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/250830bf-b584-4c55-847b-0d17e1775bd8?resizing_type=fit) |
| **Alias .wire** | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/b5f3f50d-7e69-4252-99c4-081cfa84d30c?resizing_type=fit) |
| **Rhino** | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/47480270-9819-4216-9552-df906cdaacf1?resizing_type=fit) |
| **Cinema 4D** | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/0e013307-7af9-4e06-916d-fd1781cb509a?resizing_type=fit) |
| **AxF** | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/ec58bee9-92a9-4d4a-9b27-15e6090e53c6?resizing_type=fit) |
| **MDL** | [Unsupported](https://dev.epicgames.com/community/api/documentation/image/bfd9edf6-ebd1-4213-9ca9-ae95c0d4c803?resizing_type=fit) |
| **Deltagen and VRED** | [Supported](https://dev.epicgames.com/community/api/documentation/image/5f1bdc85-b479-41dc-a9ce-3f87ac26d328?resizing_type=fit) |

You may be able to compile Unreal Engine with some of the unsupported features listed above if you download and install the required software development kits from third parties.

Support for gITF is now native to UE.

## Datasmith Export Plugins

The pre-built versions of the Datasmith Exporter Plugins on the [Datasmith export plugins](https://www.unrealengine.com/en-US/datasmith/plugins) download page support the following platforms:

| Source application | 64-bit Windows | Mac OS X |
| --- | --- | --- |
| **SketchUp Pro** | [Supported](https://dev.epicgames.com/community/api/documentation/image/ad670bb2-6751-4a58-9694-ec6bf0eb50b9?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/3700ea2f-4c50-4592-875b-5dc1e37ccc0c?resizing_type=fit) |
| **3ds Max** | [Supported](https://dev.epicgames.com/community/api/documentation/image/21aa1c6e-f278-4f2a-9b70-8e4dfdccd7cb?resizing_type=fit) | n/a \* |
| **Revit** | [Supported](https://dev.epicgames.com/community/api/documentation/image/c51b027a-4f80-460e-aa44-2d7b46a4695b?resizing_type=fit) | n/a \* |
| **Navisworks** | [Supported](https://dev.epicgames.com/community/api/documentation/image/9415d22c-ee0d-49bc-a020-332a933e9a16?resizing_type=fit) | n/a \* |
| **Rhino** | [Supported](https://dev.epicgames.com/community/api/documentation/image/fa0cbc32-a040-40e3-9339-8113dcd7bec1?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/a87d95d3-2dce-498e-a58d-8f74bdb850cf?resizing_type=fit) |
| **Archicad** | [Supported](https://dev.epicgames.com/community/api/documentation/image/198304f5-4f03-42a6-bfee-72a9709f0928?resizing_type=fit) | [Supported](https://dev.epicgames.com/community/api/documentation/image/9a595b43-a914-4dbc-b572-e863ee253bce?resizing_type=fit) |
| **Solidworks** | [Supported](https://dev.epicgames.com/community/api/documentation/image/d4b6bc95-c428-442d-965a-3177a6bd73ea?resizing_type=fit) | n/a \* |

\* Not available on macOS.

\*\* As of Unreal Engine 5.3, Autodesk now manages newer versions of the Revit exporter plugin and is shipped directly in Revit 2024+. UE still supports this plugin and you can get older versions of the plugin from the download page.

When you rebuild Unreal Engine yourself from its source code distribution, you can rebuild the Datasmith Exporter Plugins for Windows. However, you need to download and install the SDK for your source application from [Trimble](https://extensions.sketchup.com/en/developer_center/sketchup_sdk) or [Autodesk](https://www.autodesk.com/developer-network/overview).

* [reference](https://dev.epicgames.com/community/search?query=reference)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [simulation](https://dev.epicgames.com/community/search?query=simulation)
* [architecture](https://dev.epicgames.com/community/search?query=architecture)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Supported File Formats by Platform](/documentation/en-us/unreal-engine/datasmith-supported-platforms?application_version=5.7#supported-file-formats-by-platform)
* [Rebuilding Unreal Engine from Source](/documentation/en-us/unreal-engine/datasmith-supported-platforms?application_version=5.7#rebuilding-unreal-engine-from-source)
* [Datasmith Export Plugins](/documentation/en-us/unreal-engine/datasmith-supported-platforms?application_version=5.7#datasmith-export-plugins)
