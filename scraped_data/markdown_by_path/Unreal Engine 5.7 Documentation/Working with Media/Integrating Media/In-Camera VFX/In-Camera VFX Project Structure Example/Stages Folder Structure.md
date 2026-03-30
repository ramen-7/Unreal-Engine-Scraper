<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stages-folder-structure?application_version=5.7 -->

# Stages Folder Structure

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
9. Stages Folder Structure

# Stages Folder Structure

A reference guide for organizing your In-Camera VFX project's Stages files in the Content Browser.

![Stages Folder Structure](https://dev.epicgames.com/community/api/documentation/image/99de66eb-eb99-42f9-b764-93e9207314a8?resizing_type=fill&width=1920&height=335)

![The recommended Stages folder structure in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb5edce1-0553-4f69-a373-1cd4fd48f6e3/cb_stages.png)

The **Stages** folder contains the **nDisplay Configurations** which describe the topology of the LED volume or volumes used and all related files.

The files in this section are linked to the **Envs** folder files, as they will all be combined for the final In-Camera VFX persistent levels.

* EpicLA

  + EpicLAStage\_P - Main Stage persistent level
  + WarpMeshes - Meshes that make up the volume

    - EpicLA\_C1

      * SM\_EpicLA\_C1
      * MI\_EpicLA\_C1\_(Description)\_A
      * T\_EpicLA\_C1\_(Description)\_A
  + Configs

    - NPC\_EpicLA\_(Description)
    - EpicLA\_(Description).cfg - `.cfg` files are not visible in the content browser

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e6da2ce-fcd4-4dcf-810b-346cb1251eb8/stages-chart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e6da2ce-fcd4-4dcf-810b-346cb1251eb8/stages-chart.png)

A diagram showing the recommended Stages folder structure for your project in the Content Browser.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
