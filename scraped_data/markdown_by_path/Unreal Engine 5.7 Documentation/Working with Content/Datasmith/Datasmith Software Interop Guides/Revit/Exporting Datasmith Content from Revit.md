<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/exporting-datasmith-content-from-revit-to-unreal-engine?application_version=5.7 -->

# Exporting Datasmith Content from Revit

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
9. Exporting Datasmith Content from Revit

# Exporting Datasmith Content from Revit

Describes how to export a Revit scene into a Datasmith file that you can then import into the Unreal Editor.

![Exporting Datasmith Content from Revit](https://dev.epicgames.com/community/api/documentation/image/5e3b9e34-e1e8-4443-8d85-331f30ca5b88?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

Once you've installed the Datasmith Exporter plugin for Revit, you'll have a **Datasmith** ribbon that you can use to export a selected 3D view to a `.udatasmith` file.

![Datasmith ribbon in Revit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/75b6237e-ace9-431f-88d9-6192be4efe00/datasmith-ribbon-revit.png)

Follow the steps below in Revit to export your scene using this file type.

1. In the **Project Browser**, select and open the 3D View that you want to export.

   ![Select a 3D View](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36e56e6a-6fea-4949-8410-754a2c3cd4cb/revit-select-3d-view.png "Select a 3D View")

   The Datasmith Exporter plugin uses the visibility settings defined for the current 3D View to determine what parts of the scene it should export. For details, see [Revit](/documentation/en-us/unreal-engine/using-datasmith-with-revit-in-unreal-engine).
2. Open the **Datasmith** ribbon, then click **Export 3D View**.

   ![Export 3D View button on the Datasmith toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/573488f9-d2cc-4c4b-8eaf-5301eee13bda/revit-toolbar.png "Export 3D View button on the Datasmith toolbar")
3. In the **Export 3D View to Unreal Datasmith** window, browse to the location you want to save your .udatasmith file, and use the **File Name box** to give your new file a name.

   ![Set the location and file name](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2fbb9a13-4b2e-4809-9249-f7acb2ef0cb2/revit-ds-export-location.png "Set the location and file name")
4. Click **Save**.

### End Result

You should now be ready to try importing your new `.udatasmith` file into the Unreal Editor. See [Importing Datasmith Content into Unreal Engine](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine) and [Reimporting Datasmith Content](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine).

Along with your new `.udatasmith` file, you'll see a folder that has the same name but with the suffix `_Assets`. If you move your `.udatasmith` file to a new location, make sure that you also move this folder to the same location.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [revit](https://dev.epicgames.com/community/search?query=revit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [End Result](/documentation/en-us/unreal-engine/exporting-datasmith-content-from-revit-to-unreal-engine?application_version=5.7#endresult)
