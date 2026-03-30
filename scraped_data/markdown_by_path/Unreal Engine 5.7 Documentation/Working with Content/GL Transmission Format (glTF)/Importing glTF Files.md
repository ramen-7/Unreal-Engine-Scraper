<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-gltf-files-into-unreal-engine?application_version=5.7 -->

# Importing glTF Files

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
7. Importing glTF Files

# Importing glTF Files

How to import glTF files into Unreal Engine

![Importing glTF Files](https://dev.epicgames.com/community/api/documentation/image/df30db30-883a-4f52-aa2c-5434c4a9eb31?resizing_type=fill&width=1920&height=335)

 On this page

You import **glTF** content into Unreal Engine the same way you import other types of content. You can import an entire scene, or specific Assets.

You can import the following glTF formats:

| Format | Description |
| --- | --- |
| JSON `.gltf` | Includes the following elements, saved separately in a directory you specify:   * **Full scene description:** saved as a JSON-formatted, human-readable UTF-8 text file with the `.gltf` extension. * **Texture files:** saved to the format you specify, `.png`, `.jpeg`, and so on. * **Binary data files:** saved separate files with a `.bin` file extension. |
| Binary `.glb` | Combines the full scene description, all binary data, and all textures into a single self-contained binary file. |

## Import Individual Assets from glTF Files

You can import glTF Assets into Unreal Engine the same way you import other Assets.

1. In the **Content Browser**, do one of the following:
   * In the **+Add** menu, use the **Import to** command. For detailed instructions see [Importing from the Content Browser](/documentation/en-us/unreal-engine/importing-assets-directly-into-unreal-engine#importingfromthecontentbrowser).
   * Drag and drop a glTF Asset into the Content Browser. For detailed instructions see [Importing Using Drag and Drop](/documentation/en-us/unreal-engine/importing-assets-directly-into-unreal-engine#importingusingdraganddrop).
     Whichever workflow you use opens the **The Interchange Pipeline Configuration (Import Content)** dialog box.
2. Set the import options as needed, and click **Import**.

## Import a glTF Scene Into an Unreal Engine Level

You can import full glTF scenes into Unreal Engine using the same scene import workflow you use for other scene formats such as FBX.

1. From the main menu, choose **File > Import Into Level**.
2. Select the `.gtlf` or `.glb` file that contains the scene you want to import, and click Open.

   The **Choose location for importing scene content** dialog opens.
3. Choose the destination folder in your Unreal Engine project, and click OK.

   The **Interchange Pipeline Configuration (Import Content)** dialog box opens.
4. Set the import options as needed, and click **Import**.

* [gltf](https://dev.epicgames.com/community/search?query=gltf)
* [gl transmission format](https://dev.epicgames.com/community/search?query=gl%20transmission%20format)
* [import / export](https://dev.epicgames.com/community/search?query=import%20%2F%20export)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Import Individual Assets from glTF Files](/documentation/en-us/unreal-engine/importing-gltf-files-into-unreal-engine?application_version=5.7#importindividualassetsfromgltffiles)
* [Import a glTF Scene Into an Unreal Engine Level](/documentation/en-us/unreal-engine/importing-gltf-files-into-unreal-engine?application_version=5.7#importagltfsceneintoanunrealenginelevel)
