<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/batch-exporting-revit-views-with-dynamo-to-a-datasmith-scene?application_version=5.7 -->

# Batch Exporting Revit Views with Dynamo

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
8. [Revit](/documentation/en-us/unreal-engine/using-datasmith-with-revit-in-unreal-engine "Revit")
9. Batch Exporting Revit Views with Dynamo

# Batch Exporting Revit Views with Dynamo

How to use the Dynamo scripting language to export from Revit.

![Batch Exporting Revit Views with Dynamo](https://dev.epicgames.com/community/api/documentation/image/1cc6493b-068c-489b-a428-13b6d6446142?resizing_type=fill&width=1920&height=335)

 On this page

Similar to the Blueprint scripting system in **Unreal Engine**, Dynamo for Revit is a visual programming language that gives access to the Revit API and is used to easily automate many repetitive tasks. In addition to being accessible from the add-ins Ribbon toolbar, the Autodesk Revit Exporter for Datasmith uses Dynamo to automate the process of exporting your Revit 3D views as `.udatasmith` files for use in Unreal Engine.

## Installing the Plugin

Begin by downloading and installing the [Autodesk Revit Exporter for Datasmith](https://www.unrealengine.com/en-US/datasmith/plugins) plugin available from Epic Games. This will update any previous version of the plugin that has been installed, as well as add some additional hooks for the Dynamo visual scripting language.

The plugin requires your Dynamo to be version 2.0 or higher. Check this by clicking the **Help** menu in the Dynamo UI and selecting the **About** option.

After installing the plugin, launch the Dynamo interface:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1948cb1-cff7-4c85-bc52-b784bcb630b2/rb_dynamolaunch.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1948cb1-cff7-4c85-bc52-b784bcb630b2/rb_dynamolaunch.png)

Next, you need to import the DatasmithDynamoNode.dll file. In the Dynamo UI, click the File menu and select the Import Library option. You will find the library in one of the following locations:

| **Revit Version** | **Location** |
| --- | --- |
| **2018.3** | C:\ProgramData\Autodesk\Revit\Addins\2018\DatasmithRevit2018\DatasmithDynamoNode.dll |
| **2019** | C:\ProgramData\Autodesk\Revit\Addins\2019\DatasmithRevit2019\DatasmithDynamoNode.dll |
| **2020** | C:\ProgramData\Autodesk\Revit\Addins\2020\DatasmithRevit2020\DatasmithDynamoNode.dll |

To confirm that the installation of the library is successful, you should see a **DatasmithDynamoNode** entry in the Add-Ons section of the Dynamo Library.

## How It Works

Importing the library installs the Datasmith Dynamo node, which is designed to take in data from your Revit document and export the requested views with a specific level of tessellation:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d42c3243-9bf2-4395-b0a4-fb9b9379d759/rb_dynamonode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d42c3243-9bf2-4395-b0a4-fb9b9379d759/rb_dynamonode.png)

| **Number** | **Description** |
| --- | --- |
| **1** | Current Revit document |
| **2** | Output path |
| **3** | List of Views as ID's |
| **4** | Level of tessellation (integer value 1-15, default 8) |

Using the current Revit file as the document, the node outputs a `.udatasmith` file, and a folder of objects in the 3D view as `.udsmesh` files that are ready for Datasmith.

To demonstrate the use of the Datasmith Dynamo node, the plugin contains a sample Dynamo script file that shows how to use the node to create a batch exporter:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/781f7560-1d4b-48d1-b0ce-48a22f388502/rb_batchlogic2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/781f7560-1d4b-48d1-b0ce-48a22f388502/rb_batchlogic2.png)

The script goes through the following steps:

1. Using the Get 3D Views node, the script finds all the 3D views in the current Revit document and adds them to a list.
2. It then filters the list, looking for either a prefix added to the view name (using the format Prefix\_ViewName) or views that are given a specific name. In the example, the prefix default is set to Datasmith, while the Instance Parameter Name default is DatasmithExport.
3. Next, the script looks at two boolean values to determine whether you want to export all the views or only the views found in the filtered list.
4. Finally, the chosen views are exported to the chosen folder with an amount of detail defined by the Mesh Tessellation Amount.

To avoid dependencies on the Dynamo API, this version of the batch exporter requires the use of a python node to fetch information about the current document:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29f75fc8-21de-4b7b-bf79-1315c8e39db6/rb_python2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29f75fc8-21de-4b7b-bf79-1315c8e39db6/rb_python2.png)

Similarly, getting the 3D Views and extracting the ElementID of a given view relies on python nodes:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57373f3a-4b7b-4748-a43e-fafd296be86d/rb_python1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57373f3a-4b7b-4748-a43e-fafd296be86d/rb_python1.png)

## Using the Batch Exporter

The supplied Dynamo example can be executed and used as a basic batch exporter:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f31d31a7-2e8c-4a31-8002-554892b4b453/rb_dynamoplayer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f31d31a7-2e8c-4a31-8002-554892b4b453/rb_dynamoplayer.png)

| **Property** | **Description** |
| --- | --- |
| **Export To:** | Allows you to browse to a folder and specify where you want your Datasmith files. |
| **Mesh Tessellation Amount:** | Specify the level of tessellation used during the export as defined by the Revit API. Level 8 is the default. This produces the same mesh resolution as the Revit FBX Exporter.  Tesselation Level 8  Tesselation Level 2 |
| **Export All 3D Views:** | If ON, this will export every 3D view found in the current Revit document. If OFF, this will find the 3D views in the current Revit document that use a custom name or prefix and export those for Datasmith. |
| **By View Name Prefix / By View Instance Parameter:** | Exports only the views that match either a prefix name or a project parameter assigned to a view instance.   * If TRUE: Filter by parameter. * If FALSE: Filter by View Name Prefix. |
| **View Instance Parameter Name:** | Defines the view name that will be exported. |
| **Export 3D Views Prefixed With:** | Defines the view name prefix that will be exported. |

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [revit](https://dev.epicgames.com/community/search?query=revit)
* [export](https://dev.epicgames.com/community/search?query=export)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Installing the Plugin](/documentation/en-us/unreal-engine/batch-exporting-revit-views-with-dynamo-to-a-datasmith-scene?application_version=5.7#installingtheplugin)
* [How It Works](/documentation/en-us/unreal-engine/batch-exporting-revit-views-with-dynamo-to-a-datasmith-scene?application_version=5.7#howitworks)
* [Using the Batch Exporter](/documentation/en-us/unreal-engine/batch-exporting-revit-views-with-dynamo-to-a-datasmith-scene?application_version=5.7#usingthebatchexporter)
