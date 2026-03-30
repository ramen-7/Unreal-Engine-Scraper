<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-gltf-exports-in-unreal-engine?application_version=5.7 -->

# Scripting glTF Exports

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
6. [GL Transmission Format (glTF)](/documentation/en-us/unreal-engine/the-gl-transmission-format-gltf-in-unreal-engine "GL Transmission Format (glTF)")
7. Scripting glTF Exports

# Scripting glTF Exports

How to use scripting, and Blueprint, to export to glTF from the Unreal Editor, and at runtime

![Scripting glTF Exports](https://dev.epicgames.com/community/api/documentation/image/68c28a54-4895-4a66-8b73-fc4711a81474?resizing_type=fill&width=1920&height=335)

 On this page

This page explains how to use the **Export to glTF** function to export Levels or supported Assets from the Unreal Editor using **Blueprint** or **Python**, and how to export them at runtime.

## The Export to glTF Function

The Export to GLTF function takes the following inputs:

* **An object to export:** this can be any supported Asset. For more information about supported Assets, see How the glTF Exporter Handles Unreal Engine Content.  
  To export the current Level, you can pass an empty (null) reference.
* **Selected actors:** specifies the subset of the scene to export.
  + When you export using Blueprint or Python, you must provide this set, even if it is empty.
  + When you export a Level, provide an empty set to export all Actors in the Level.
* **A destination path:** the name, path, and format (file extension) of the exported glTF file. You can specify the following formats:

  | Format | Description |
  | --- | --- |
  | JSON `.gltf` | Includes the following elements, saved separately in a directory you specify:  + **Full scene description:** saved as a JSON-formatted, human-readable UTF-8 text file with the `.gltf` extension. + **Texture files:** saved to the format you specify, `.png`, `.jpeg`, and so on. + **Binary data files:** saved separate files with a `.bin` file extension. |
  | Binary `.glb` | Combines the full scene description, all binary data, and all textures into a single self-contained binary file. |
* The export options. For more information, see [glTF Export Options Reference](/documentation/en-us/unreal-engine/exporting-unreal-engine-content-to-gltf#gltfexportoptionsreference).

The **Export to GLTF** function produces the following outputs:

* **OutMessage:** The log messages from the export.
* **Return value:** Returns `true` if the export was successful, `false` otherwise.

## Exporting with Blueprint

You can add the **Export to GLTF** action to a Blueprint graph from the context menu (**Miscellaneous > Export to GLTF**).

![Export to glTF Blueprint function configured to export a simple cube to glTF.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17111bc8-4c51-41bf-9ad3-67a409b57a61/ue5_2-bp-export-to-gltf.png)

Export to glTF Blueprint function configured to export a simple cube to glTF

| Input | Description |
| --- | --- |
| **Object** | The object to export (supported types are UMaterialInterface, UStaticMesh, USkeletalMesh, UWorld, UAnimSequence, ULevelSequence, ULevelVariantSets).Will default to the currently active world if null. |
| **File Path** | The filename on disk to save as. Associated textures and binary files will be saved in the same folder, unless the file extension is `.glb`, which results in a self-contained binary file. |
| **Options** | The various options to use during export. Will default to the project's user-specific editor settings if null. |
| **Selected Actors** | The set of Actors to export. This is only applicable if the object to export is a UWorld. An empty set results in the export of all actors. |

## Exporting with Python

The following code sample exports all Assets in the `/game/models/` subfolder as individual glTF files.

```
    import unreal

    assetPath = '/game/models/'
    outputDir = 'c:/Temp/glTFExport/'
    exportOptions = unreal.GLTFExportOptions()
    selectedActors = set()

    staticMestPaths = unreal.EditorAssetLibrary.list_assets(assetPath)
    for smp in staticMestPaths:
        sm = unreal.EditorAssetLibrary.load_asset(smp)
        if unreal.MathLibrary.class_is_child_of(sm.get_class(), unreal.StaticMesh):
            exportPath = outputDir+sm.get_name()+'/'+sm.get_name()+'.gltf'
            unreal.GLTFExporter.export_to_gltf(sm,exportPath,exportOptions,selectedActors)

Copy full snippet
```

## Exporting at Runtime

You can use the Export to GLTF function to export glTF files at runtime. However, neither [Material baking](/documentation/en-us/unreal-engine/how-the-gltf-exporter-handles-unreal-engine-content#materialbaking) nor [Material expression matching](/documentation/en-us/unreal-engine/how-the-gltf-exporter-handles-unreal-engine-content#materialexpressionmatching) is possible at runtime, so you need to do one of the following to handle most materials:

* **Pre-bake materials:** in the editor, create glTF proxy Materials. The glTF exporter uses the proxy materials for runtime glTF exports. Proxy Materials automatically ship with your application because they are referenced in the User Data for your Unreal Engine Materials. For more information about creating proxy Materials, see [glTF Proxy Materials](/documentation/en-us/unreal-engine/gltf-proxy-materials-in-unreal-engine).
* In C++, use the **GLTFBuilder** API at runtime to modify the content of the glTF file before it is exported.

* [gltf](https://dev.epicgames.com/community/search?query=gltf)
* [gl transmission format](https://dev.epicgames.com/community/search?query=gl%20transmission%20format)
* [import / export](https://dev.epicgames.com/community/search?query=import%20%2F%20export)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [The Export to glTF Function](/documentation/en-us/unreal-engine/scripting-gltf-exports-in-unreal-engine?application_version=5.7#theexporttogltffunction)
* [Exporting with Blueprint](/documentation/en-us/unreal-engine/scripting-gltf-exports-in-unreal-engine?application_version=5.7#exportingwithblueprint)
* [Exporting with Python](/documentation/en-us/unreal-engine/scripting-gltf-exports-in-unreal-engine?application_version=5.7#exportingwithpython)
* [Exporting at Runtime](/documentation/en-us/unreal-engine/scripting-gltf-exports-in-unreal-engine?application_version=5.7#exportingatruntime)
