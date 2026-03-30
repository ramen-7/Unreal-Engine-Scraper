<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/tools-folder-structure-in-unreal-engine?application_version=5.7 -->

# Tools Folder Structure

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
8. [In-Camera VFX Project Structure Example](/documentation/en-us/unreal-engine/in-camera-vfx-project-structure-example-in-unreal-engine "In-Camera VFX Project Structure Example")
9. Tools Folder Structure

# Tools Folder Structure

A reference guide for organizing your In-Camera VFX project's Tools files in the Content Browser.

![Tools Folder Structure](https://dev.epicgames.com/community/api/documentation/image/5a888b6b-e947-4a14-baa7-33d9a8c96895?resizing_type=fill&width=1920&height=335)

![The recommended Tools folder structure in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68da9888-29c6-40da-bb78-11f796f222e9/cb_tools.png)

The **Tools** folder contains custom [Blueprints](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) and widgets, [Level Snapshot](/documentation/en-us/unreal-engine/level-snapshots-in-unreal-engine) Filters and Presets, and [Remote Control](/documentation/en-us/unreal-engine/remote-control-for-unreal-engine) Presets. The following list describes each tool.

* Blueprint Tool A: Separate folder per-Stage blueprint used, containing it's source:

  + BP\_Tool *or* WBP\_WidgetTool — The principle Blueprint.
  + Enums - Related enumerations used in the Blueprint.

    - E\_(Description)
  + Structs - Related structures used in the Blueprint.

    - F\_(Description)
  + SubBlueprints - Only present if any sub-blueprints are used.

    - BP\_(Description)
  + SubWidgets - Only present if any sub-widget blueprints are used.

    - WBP\_(Description)
* Remote Control: Remote control presets used

  + RCP\_(Description)
* Common

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f59293ba-288d-4b45-a46f-6e189cbdd077/tools-chart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f59293ba-288d-4b45-a46f-6e189cbdd077/tools-chart.png)

A diagram showing the recommended tools folder structure for your project in the Content Browser.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [remote control](https://dev.epicgames.com/community/search?query=remote%20control)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [level snapshots](https://dev.epicgames.com/community/search?query=level%20snapshots)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
