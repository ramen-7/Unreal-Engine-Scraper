<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/assets-folder-structure-in-unreal-engine?application_version=5.7 -->

# Assets Folder Structure

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
9. Assets Folder Structure

# Assets Folder Structure

A reference guide for organizing your In-Camera VFX project's Asset files in the Content Browser.

![Assets Folder Structure](https://dev.epicgames.com/community/api/documentation/image/20fb1679-b0c0-48ea-92d8-69b10b1dc749?resizing_type=fill&width=1920&height=335)

![The recommended Assets folder structure in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a040f757-9210-4b38-9ca9-b69a508a8270/cb_assets.png)

The **Assets** folder typically contains all Assets for creating Characters, Environments, and FX - Meshes, like Materials, Textures, Blueprints, and other source files. Level Assets are not included here.

Each subfolder contains the appropriate source files for that Asset. For example, the Chr folder contains Character Asset subfolders, one per Character used. Each contains that Character's source Assets, that is, Blueprints, Skeletal Meshes, Skeletons, Animations, Materials, and so on.

The following list is how the Assets were categorized for the [In-Camera VFX Production Test](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine) project, expanded to include a few Asset types that were not used in that project. It's unlikely for any given project to use all possible Asset types.

* Vegetation

  + Tree\_A

    - SM\_Tree\_A
    - MI\_Tree\_A
    - T\_Tree\_A\_BaseColor
* Rocks

  + Rock\_A

    - BP\_Rock\_A
    - SM\_Rock\_A
    - MI\_Rock\_A
    - T\_Rock\_A\_BaseColor
  + Rock\_B
  + Pebble\_A
* Chr

  + Backpacker\_A

    - BP\_Backpacker\_A
    - SK\_Backpacker\_A
    - SKEL\_Backpacker\_A
    - MI\_Backpacker\_A
    - T\_Backpacker\_A\_BaseColor
    - ABP\_Backpacker\_A\_Livelink
    - ABP\_Backpacker\_A\_Game
    - Animations

      * A\_Backpacker\_A\_Run
      * A\_Backpacker\_A\_Idle

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ed6f028-81a1-44c6-a61e-e3b6732042c4/assets-chart-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ed6f028-81a1-44c6-a61e-e3b6732042c4/assets-chart-1.png)

A diagram showing the first part of the recommended Asset folder structure for your project in the Content Browser.

* FX

  + Birds\_A

    - BP\_Birds\_A
    - FXS\_Birds\_A\_(DescA)\_A
    - FXS\_Birds\_A\_(DescB)\_A
    - Emitters

      * FXE\_Birds\_A\_(DescA)\_A
* Decals

  + MI\_Caustic\_A\_Decal
  + T\_Caustic\_A\_M
* HDRs

  + HDR\_NightSky\_A
  + HDR\_CitySky\_D
* IES

  + TLP\_Arri750Plus\_A
  + TLP\_Arri750Plus\_B
* OCIO

  + (Stage Name)

    - OCIO\_(Stage)\_A
    - OCIO\_(Stage)\_B
    - LUTS

      * (Description).spi1d (file explorer only)

      OpenColorIO `.spi1d` files do not show in the Content Browser, only in the File Explorer. Refer to the [OpenColorIO](/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine) documentation for more information.
* MasterMaterials

  + Ground\_A

    - M\_Ground\_A
    - T\_Ground\_A\_BaseColor
    - MI\_WetGround\_A
  + Textures
* Props\*
* Landscapes\*
* Vehicles\*
* Other\*

\* Not used for the In-Camera VFX Production Test.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc0832e1-7908-4db5-83af-07fb289edaa9/assets-chart-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc0832e1-7908-4db5-83af-07fb289edaa9/assets-chart-2.png)

A diagram showing the rest of the recommended Asset folder structure for your project in the Content Browser. It links back to the first part at the top.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [asset](https://dev.epicgames.com/community/search?query=asset)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
