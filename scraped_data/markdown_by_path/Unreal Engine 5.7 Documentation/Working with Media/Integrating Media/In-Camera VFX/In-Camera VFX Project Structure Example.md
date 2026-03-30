<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-project-structure-example-in-unreal-engine?application_version=5.7 -->

# In-Camera VFX Project Structure Example

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [In-Camera VFX](/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine "In-Camera VFX")
8. In-Camera VFX Project Structure Example

# In-Camera VFX Project Structure Example

A reference guide for organizing your In-Camera VFX project's file structure in the Content Browser.

![In-Camera VFX Project Structure Example](https://dev.epicgames.com/community/api/documentation/image/113efade-25d4-4bc4-867a-2fb317c35474?resizing_type=fill&width=1920&height=335)

 On this page

The **In-Camera VFX Production Structure Example** is intended to provide a clean sample organizational structure for a Virtual Production project. You can duplicate this structure and modify it as necessary to meet the requirements of your own project. The structure described is based on the structure of the [In-Camera VFX Production Test](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine), expanded to cover additional common use cases.

### Content Browser Folders

Inside the **Content** folder of the **Content Browser**, create a folder named based on your Project Name, to hold any content specifically for your project. If required, create a folder named Common, which will contain any content that is shared with other projects.

Don't confuse the Project folder created by UE when the project was created (the root folder of the entire project) with the folder with your Project Name you create inside the Content Browser. We recommend varying the names so as not to confuse them.

![Recommended project structure top level in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48ec8182-cf2a-4d52-836b-3e213483e328/cb_content_top.png)

**Content/(Project Name)/[Assets](/documentation/en-us/unreal-engine/assets-folder-structure-in-unreal-engine)**

All assets for creating Characters, Environments, and visual effects. Level Assets are not included here.

**Content/(Project Name)/[Envs](/documentation/en-us/unreal-engine/envs-folder-structure-in-unreal-engine)**

Contains all levels, snapshots, and sublevels. Does not contain any Stage actors.

**Content/(Project Name)/[Media](/documentation/en-us/unreal-engine/media-folder-structure-in-unreal-engine)**

Any media framework content such as EXRs and Movie Render Queue Outputs and Profiles.

**Content/(Project Name)/[Sequences](/documentation/en-us/unreal-engine/sequences-folder-structure-in-unreal-engine)**

All level sequences, edits, animations, and related snapshots.

**Content/(Project Name)/[Stages](/documentation/en-us/unreal-engine/stages-folder-structure)**

Stage-specific files like mocap layouts, green screen stages, and LED stages such as nDisplay Configurations which describe the topology of the LED volumes.

**Content/(Project Name)/[StageLevels](/documentation/en-us/unreal-engine/stage-levels-folder-structure-in-unreal-engine)**

All the Level Assets that have both environment and stage Actors.

**Content/(Project Name)/[Tools](/documentation/en-us/unreal-engine/tools-folder-structure-in-unreal-engine)**

Custom Blueprints including utilities and widgets, controls, Level Snapshot Filters and Presets, and Remote Control Presets. Also includes any related Blueprint Actors — structures, enums, and so on.

We recommend using an organized naming convention for your Assets to help make it easy to find them in the Content Browser. Refer to the [Recommended Asset Naming Convention](/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects) for a best-practices example.

Refer to the individual pages for the details of the recommended project structure inside each folder.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc2cb3db-cd50-451f-b087-30652ee1be2c/top-level-chart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc2cb3db-cd50-451f-b087-30652ee1be2c/top-level-chart.png)

A diagram showing the recommended top-level folder structure for your project in the Content Browser.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Content Browser Folders](/documentation/en-us/unreal-engine/in-camera-vfx-project-structure-example-in-unreal-engine?application_version=5.7#contentbrowserfolders)
