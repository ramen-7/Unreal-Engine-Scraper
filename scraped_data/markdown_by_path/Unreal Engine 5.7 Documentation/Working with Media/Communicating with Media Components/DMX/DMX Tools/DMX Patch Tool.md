<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-patch-tool-in-unreal-engine?application_version=5.7 -->

# DMX Patch Tool

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
6. [Communicating with Media Components](/documentation/en-us/unreal-engine/communicating-with-media-components-from-unreal-engine "Communicating with Media Components")
7. [DMX](/documentation/en-us/unreal-engine/dmx-in-unreal-engine "DMX")
8. [DMX Tools](/documentation/en-us/unreal-engine/dmx-tools-in-unreal-engine "DMX Tools")
9. DMX Patch Tool

# DMX Patch Tool

Use the DMX Patch Tool to quickly apply DMX Libraries and Patches.

![DMX Patch Tool](https://dev.epicgames.com/community/api/documentation/image/7c90fcc7-3123-4a81-86d8-fbfc2d875f4c?resizing_type=fill&width=1920&height=335)

 On this page

The **DMX Patch tool** provides you a way to quickly set the DMX library and patch of a given selection of actors within the **World Outliner**.

A DMX library is the main data structure that holds information in regards to:

* Controllers
* Fixture types
* Fixture patches

A DMX patch tracks DMX addresses, and assigns the patching of DMX-enabled fixtures.

The DMX Patch tool offers 3 functionalities:

* Address incremental
* Address same
* Address and rename

![The three options available for the patch tool.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dfad63fd-1d28-44a3-bd27-c6c40fc691e2/quick-patch-options.png)

## Address incremental

* Applies the selected DMX library to all selected actors.
* Applies patches incrementally starting from the provided fixture patch.

![Using the address incremental option.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1d7293c-735c-46c2-a48f-d3ba4b40a175/address-incremental.png)

## Address same

* Applies the selected DMX library to all selected actors.
* Applies the same patch to all selected actors.

![Using the address same option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8e7cc19-6fc6-438e-81f6-8fff4a6cbf01/address-same.png)

## Address and rename

* Applies the selected DMX library to all selected actors.
* Applies the same patch to all selected actors.
* Also renames the selected actors so they match the provided patch names.

For more information on DMX patches and libraries, see the [DMX Overview](/documentation/en-us/unreal-engine/dmx-overview).

* [dmx](https://dev.epicgames.com/community/search?query=dmx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Address incremental](/documentation/en-us/unreal-engine/dmx-patch-tool-in-unreal-engine?application_version=5.7#addressincremental)
* [Address same](/documentation/en-us/unreal-engine/dmx-patch-tool-in-unreal-engine?application_version=5.7#addresssame)
* [Address and rename](/documentation/en-us/unreal-engine/dmx-patch-tool-in-unreal-engine?application_version=5.7#addressandrename)
