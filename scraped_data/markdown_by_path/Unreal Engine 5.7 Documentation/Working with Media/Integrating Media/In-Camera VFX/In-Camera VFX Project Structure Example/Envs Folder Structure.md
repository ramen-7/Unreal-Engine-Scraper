<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/envs-folder-structure-in-unreal-engine?application_version=5.7 -->

# Envs Folder Structure

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
9. Envs Folder Structure

# Envs Folder Structure

A reference guide for organizing your In-Camera VFX project's environment files in the Content Browser.

![Envs Folder Structure](https://dev.epicgames.com/community/api/documentation/image/e9ee3636-3bff-4c69-ab7b-dd7284b352ce?resizing_type=fill&width=1920&height=335)

![The recommended Envs folder structure in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e0b8e1b-9668-4491-b200-7c260578dd07/cb_env.png)

The **Envs** folder contains all the assets specifically for your environments (envs).

Since source control only lets you exclusively check out binary assets, such as `.umap` files, each artist working on an environment at the same time must work on their own level. The solution to this is to divide an environment up into multiple [sublevels](/documentation/en-us/unreal-engine/managing-multiple-levels-in-unreal-engine) based on the type of Actors in each.

For example, a lighting artist would work in the lighting sublevel, and an FX artist in the FX sublevel. It is also common to have multiple GEO levels that divide the environment up into regions, each being worked on by a different artist. The number and types of sublevels used should be dependent on the needs of the production.

The files in this section are linked to the **Stages** folder files, as they will all be combined for the final In-Camera VFX persistent levels.

The following are the types of folders used for each environment in the sample project:

* **Level Asset**: Level Assets follow a (LevelName)\_(Descriptor) structure. The \_P suffix is given to the Persistent Level, which acts as a container for the sublevels. Open this Level Asset to view the full environment composed of all the sublevels.
* **SubLevels**: In this project, each Level was separated into the Caustics, FX, Geo, and Lighting sublevels.
* **Snapshots**: Level Snapshot Assets associated with the Level.

For example:

* CaveEntrance

  + CaveEntrance\_P — Main persistent level
  + SubLevels

    - CaveEntrance\_Geo\_A
    - CaveEntrance\_Lighting\_A
    - CaveEntrance\_FX\_A
    - CaveEntrance\_Anim\_A
    - CaveEntrance\_Vis\_A
  + Snapshots

    - SNAP\_CaveEntrance\_(Description)
* CavePath
* SpaceJunkyard

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d94c84cb-9dc0-4201-a1c7-2cfd37e06225/envs-chart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d94c84cb-9dc0-4201-a1c7-2cfd37e06225/envs-chart.png)

A diagram showing the recommended Envs folder structure for your project in the Content Browser.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
