<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine?application_version=5.7 -->

# One File Per Actor

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
6. One File Per Actor

# One File Per Actor

An introduction to the One File Per Actor System and how it can be used in your projects.

![One File Per Actor](https://dev.epicgames.com/community/api/documentation/image/d72a85b8-0824-4e80-8747-2e225a90baa4?resizing_type=fill&width=1920&height=335)

 On this page

In previous versions of Unreal Engine, when you wanted to make changes to one or more Actors inside a Level, you needed to check the file out of source control. This locked other team members out of that file until your work was complete, slowing down the development process since only one person could work on a file at a time.

**One File Per Actor (OFPA)** reduces overlap between users by saving data for instances of Actors in external files, removing the need to save the main Level file when making changes to its Actors.

The One File Per Actor feature is only available in the Editor. All Actors are embedded in their respective Level files when cooked.

## Enabling One File Per Actor

The One File Per Actor feature is enabled by default when using [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine). To enable OFPA in a non-partitioned world, follow the steps below:

[![Enabling OFPA for a Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c22c055-fcba-47b8-b9e2-73ddba2ec173/ofpa-world-enable.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c22c055-fcba-47b8-b9e2-73ddba2ec173/ofpa-world-enable.png)

Enabling OFPA for a Level.

1. Open the **World Settings** panel. From the main menu, go to **Window > World Settings**.
2. Navigate to the **World** section of the panel and click the checkbox next to **Use External Actors**.
3. You will be asked if you want to convert all Actors to external packaging. Click **Yes** to complete the conversion to OFPA.

   [![OFPA Convert All Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05a032eb-6b74-400c-8073-e0ff21b0472e/ofpa-convert-all.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05a032eb-6b74-400c-8073-e0ff21b0472e/ofpa-convert-all.png)

   Click Yes to convert all the Actors in the Level.
4. Save your Level.

## Converting Sublevels

It is important to note that only the current Level will be converted to OFPA when you activate the **Use External Actors** option for your Level. To convert any of your sublevels, you must load them and enable the **Use External Actors** for each of them, as described above. Since this may be an issue if your Level contains several sublevels, you can use a commandlet to convert a Level and its sublevels automatically.

[![OFPA Commandlet](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/315d0faf-326b-4dfc-b10d-02980a36248a/ofpa-commandlet.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/315d0faf-326b-4dfc-b10d-02980a36248a/ofpa-commandlet.png)

A breakdown of the commandlet.

Follow the steps below to use the commandlet:

1. Open a Command Prompt window.

   [![Open the Command Prompt](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c81deaf-d6e6-4017-abf5-ad6a151b99fa/ofpa-commandlet-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c81deaf-d6e6-4017-abf5-ad6a151b99fa/ofpa-commandlet-1.png)
2. At the prompt, navigate to the location of the **UnrealEditor.exe** file. For example: `C:\Builds\Home_UE5_Engine\Engine\Binaries\Win64`.

   [![Navigate to the .EXE File](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efb34d12-aaa8-4bbc-9c88-dee274e32494/ofpa-commandlet-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efb34d12-aaa8-4bbc-9c88-dee274e32494/ofpa-commandlet-2.png)
3. Next, begin typing the command. Start with the name of the `.exe` file that will run the commandlet, `UnrealEditor.exe`.
4. Add the name of the commandlet and the following arguments:

   * `-run="ConvertLevelsToExternalActorsCommandlet"` is the name of the commandlet.
   * `-nosourcecontrol` tells the commandlet to not use source control.
   * `-convertsublevels` tells the commandlet to convert any sublevels the map may have.

     [![Add the Name of the Commandlet and Arguments](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92d415b9-ce1e-4144-89c4-d5626dce7f6c/ofpa-commandlet-3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92d415b9-ce1e-4144-89c4-d5626dce7f6c/ofpa-commandlet-3.png)
5. Finish the command with the location of the Level: `"/Game/Maps/TestMaps/ExternalActors/MasterMap"` In this example, **Game** is the name of your project and **MainMap** is the name of the map you wish to convert.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d8b49dd-51bd-467b-af0a-c3a16d15d99f/ofpa-commandlet-4.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d8b49dd-51bd-467b-af0a-c3a16d15d99f/ofpa-commandlet-4.png)
6. Press **Enter** to run the commandlet. It will then convert the Level and any sublevels to OFPA.

## Using OFPA With Source Control

While working in your source control application, you will notice that external Actor file names are encoded. To address this issue, you can view and validate the contents of a changelist before you submit it using the **View Changelist** window.

[![OFPA in Source Control](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03d2997c-83f3-4083-bfc4-00990852aaab/ofpa-source-control.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03d2997c-83f3-4083-bfc4-00990852aaab/ofpa-source-control.png)

An existing changelist for a level that uses OFPA.

This window displays existing changelists and the files they contain. For external Actors, you can see the Actor names, Level paths and Asset types, rather than the encoded filenames.

With changelist support built into the Editor, you can validate the contents of your changelists before you submit them to source control. This is required due to the added complexity that OFPA brings to your projects. For example, a user can check out multiple files and only submit some of them, possibly leaving dangling references.

For more information on using source control in Unreal Engine, see In-Editor Source Control.

When using OFPA, content and Actor files should be submitted to source control from within the Editor.



Changelist support is only available when using Perforce as your source control provider.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [world partition](https://dev.epicgames.com/community/search?query=world%20partition)
* [one file per actor](https://dev.epicgames.com/community/search?query=one%20file%20per%20actor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling One File Per Actor](/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine?application_version=5.7#enablingonefileperactor)
* [Converting Sublevels](/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine?application_version=5.7#convertingsublevels)
* [Using OFPA With Source Control](/documentation/en-us/unreal-engine/one-file-per-actor-in-unreal-engine?application_version=5.7#usingofpawithsourcecontrol)
