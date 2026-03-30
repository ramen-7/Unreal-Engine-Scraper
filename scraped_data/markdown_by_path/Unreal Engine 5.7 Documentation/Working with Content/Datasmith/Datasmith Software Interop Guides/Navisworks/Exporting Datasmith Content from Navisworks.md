<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/exporting-datasmith-content-from-navisworks-to-unreal-engine?application_version=5.7 -->

# Exporting Datasmith Content from Navisworks

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
8. [Navisworks](/documentation/en-us/unreal-engine/using-datasmith-with-navisworks-in-unreal-engine "Navisworks")
9. Exporting Datasmith Content from Navisworks

# Exporting Datasmith Content from Navisworks

How to Export Datasmith Content from Autodesk Navisworks

![Exporting Datasmith Content from Navisworks](https://dev.epicgames.com/community/api/documentation/image/1ca88c9d-891f-4d20-a2e3-7724a54afe0f?resizing_type=fill&width=1920&height=335)

 On this page

## Exporting From the Ribbon Menu

Once you installed the **Datasmith Exporter Plugin for Navisworks**, you will have an **Unreal Datasmith** tab added to the ribbon menu at the top of the screen:

![Unreal Datasmith tab added to the ribbon menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb5646ae-3676-4766-8ac4-5e99b232fb16/datasmithnavisexport1.png "Unreal Datasmith tab added to the ribbon menu")

Once you have hidden the elements that you do not want to export, follow the steps below to export your scene for Datasmith using the (`*.udatasmith`) filetype:

From the ribbon menu, click the Datasmith Export button to open the export panel:

![Datasmith exporter dialog box inside Navisworks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/07ea4d32-ee7e-4402-9b4d-1bc299be2e39/datasmithnavisorigin2.png "Datasmith exporter dialog box inside Navisworks")

| Name | Description |
| --- | --- |
| Merge | Allows you to select the level of an object's tree at which elements are merged to create static meshes. See [Navisworks](/documentation/en-us/unreal-engine/using-datasmith-with-navisworks-in-unreal-engine) for more information. |
| Origin | Specify the origin point for the scene. This will become 0,0,0 inside Unreal. |

Set the level of object merging and the origin point in the Export panel and then click the **Export** button.

![Saving the file](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9457f8e3-3024-4f09-a4af-b89f3bed4e74/datasmithnavisexport3.png "Saving the file")

Browse to the location where you want to save your exported file, set the File name, and click Save.

## Exporting With a Python Script

You can use a Python script to bulk export Datasmith content from Naviswork. You can try the example

```
        import sys

        import clr

        # Add location of Navisworks assembly dlls
        sys.path.append(r'C:\Program Files\Autodesk\Navisworks Manage 2022')

        # Add Navisworks assemblies
        clr.AddReference('Autodesk.Navisworks.Api')
        clr.AddReference('Autodesk.Navisworks.Automation')

        from Autodesk.Navisworks.Api import *
        from Autodesk.Navisworks.Api.Automation import *

        navisworks_app = NavisworksApplication()  # Create an app instance

        try:
            source_fpath = r'C:\Program Files\Autodesk\Navisworks Manage 2022\Samples\snowmobile.nwd'

            navisworks_app.OpenFile(source_fpath, [])

            print(f'Exporting {source_fpath}...', end='')
            if 0 == navisworks_app.ExecuteAddInPlugin('DatasmithNavisworksExporter.EpicGames', [
                r'C:\temp\test.udatasmith',
                'Merge=8',  # merge hierarchies up to depth 8
                'Origin=10, 20.0, 300.0',  # origin location
                'Hello=world',  # invalid option
            ]):
                print("DONE")
            else:
                print("FAILED")
        finally:
            navisworks_app.Dispose()  # Exit app
            # You can also keep open (e.g. if you need to review app console output for debugging)
            # navisworks_app.StayOpen()

Copy full snippet
```

## End Result

Your `.udatasmith` file should now be ready to try importing into Unreal. See [Importing Datasmith Content into Unreal Engine](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine). If your data needs additional cleaning, merging, or other modifications during the import process, see [Dataprep Import Customization](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine).

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [navisworks](https://dev.epicgames.com/community/search?query=navisworks)
* [how-to](https://dev.epicgames.com/community/search?query=how-to)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Exporting From the Ribbon Menu](/documentation/en-us/unreal-engine/exporting-datasmith-content-from-navisworks-to-unreal-engine?application_version=5.7#exportingfromtheribbonmenu)
* [Exporting With a Python Script](/documentation/en-us/unreal-engine/exporting-datasmith-content-from-navisworks-to-unreal-engine?application_version=5.7#exportingwithapythonscript)
* [End Result](/documentation/en-us/unreal-engine/exporting-datasmith-content-from-navisworks-to-unreal-engine?application_version=5.7#endresult)

Related documents

[Datasmith Import Process

![Datasmith Import Process](https://dev.epicgames.com/community/api/documentation/image/40b9aadb-1a94-4f37-b1d4-f0f60955ae8e?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine)
