<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine?application_version=5.7 -->

# Importing Datasmith Content into Unreal Engine

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
7. [Datasmith Tutorials](/documentation/en-us/unreal-engine/datasmith-tutorials-in-unreal-engine "Datasmith Tutorials")
8. Importing Datasmith Content into Unreal Engine

# Importing Datasmith Content into Unreal Engine

How to use Datasmith to bring files that you create in supported 3D design applications into Unreal Engine.

![Importing Datasmith Content into Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/2d1a4c16-15fa-4677-8a88-b8c066a2a92f?resizing_type=fill&width=1920&height=335)

 On this page

This page describes how to use Datasmith to import content from a supported 3D design application or file format into Unreal Engine.

## Prerequisites

Before you can import content with Datasmith, you might have to enable some Unreal Engine plugins or install additional software.

### Datasmith Plugins

To import content into Unreal Engine using Datasmith, your project must have the **Datasmith Importer** plugin enabled. If you don't enable the plugin, you won't see the Datasmith import options in Unreal Engine. Some supported file formats require additional plugins.

* For a list of supported applications, file formats, and plugin requirements, see .
* To learn how to enable plugins in Unreal Engins, see [Customizing Unreal Engine](/documentation/en-us/unreal-engine/customizing-unreal-engine).

If you start your project from one of the **Architecture** or **Automotive, Product Design, and Manufacturing** templates, some or all of the Datasmith plugins are enabled by default.

### Additional Software

To import some supported file formats, you must install additional software. The following file formats have specific software requirements:

| File Format | Requirement |
| --- | --- |
| `.wire` | Install a version of Autodesk Alias AutoStudio that is compatible with your `.wire` file. |

## Import Datasmith Content into Unreal Engine

1. In Unreal Editor, open the project that you want to import Datasmith content into.
2. If you want to bring your content into an existing Level in your project, open it now. Otherwise, create a new Level or use the default Level.
3. In the main toolbar, open the Create menu and select **Datasmith > File Import**. A file import dialog opens.

   ![The Datasmith import option in the Create menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1fc57557-b1c2-4611-9dce-2701624d7bfd/datasmith-import-menu.png "The Datasmith import option in the Create menu")
4. Select the file you want to import, and click **Open**. A file dialog opens.
5. Choose a location in your project to store the imported content, and click **OK**. The **Datasmith Import Options** dialog opens.

   To create a new top-level folder for your Datasmith content, right-click an empty area in the file dialog. To create a subfolder of an existing folder, right-click that folder.
6. In the **Datasmith Import Options** dialog, select the types of content that you want to import from your source file, and set the other import options as needed.

   ![Set import options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b85e645-e4fb-4d62-80c4-c09960dce9ae/unrealdsimportoptions-1.png "Set import options")

   The **Datasmith Import Options** dialog displays different import options for different file types. For more information about import options, see [Datasmith Import Options](/documentation/en-us/unreal-engine/datasmith-import-options-in-unreal-engine).
7. When you finish setting the import options, click **Import**. Datasmith Does the following:

   * Reads the imported file.
   * Creates new Assets in your project.
   * Places the Datasmith Scene into the current Level.

   For more information about the import process, see the [Datasmith Overview](/documentation/en-us/unreal-engine/datasmith-plugins-overview).

## Customizing the Import Process

You can customize the Datasmith import process in the following ways:

* Use Blueprints visual scripting or Python scripts to automate the import. For details, see [Customizing the Datasmith Import Process](/documentation/en-us/unreal-engine/customizing-the-datasmith-import-process-in-unreal-engine).
* Use Dataprep to perform additional operations on the data at import time. You can save and reuse Dataprep import recipes to create your own set of Asset import pipelines. For details, see [Dataprep Import Customization](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine).

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine?application_version=5.7#prerequisites)
* [Datasmith Plugins](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine?application_version=5.7#datasmithplugins)
* [Additional Software](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine?application_version=5.7#additionalsoftware)
* [Import Datasmith Content into Unreal Engine](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine?application_version=5.7#importdatasmithcontentintounrealengine)
* [Customizing the Import Process](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine?application_version=5.7#customizingtheimportprocess)

Related documents

[Datasmith Import Options

![Datasmith Import Options](https://dev.epicgames.com/community/api/documentation/image/7718326b-c2c1-491c-911b-62926a888a7a?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/datasmith-import-options-in-unreal-engine)

[Customizing the Datasmith Import Process

![Customizing the Datasmith Import Process](https://dev.epicgames.com/community/api/documentation/image/ad9d42ac-a36f-48c6-a45c-d4e2854ff300?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/customizing-the-datasmith-import-process-in-unreal-engine)

[Dataprep Import Customization

![Dataprep Import Customization](https://dev.epicgames.com/community/api/documentation/image/6a8ab477-49b4-462e-acc3-9c75f0fa08de?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine)
