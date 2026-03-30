<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/media-folder-structure-in-unreal-engine?application_version=5.7 -->

# Media Folder Structure

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
9. Media Folder Structure

# Media Folder Structure

A reference guide for organizing your In-Camera VFX project's Media files in the Content Browser.

![Media Folder Structure](https://dev.epicgames.com/community/api/documentation/image/0ceba3d5-0d10-4913-9cff-3f3df31fc6fc?resizing_type=fill&width=1920&height=335)

![The recommended Media folder structure in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6673d10-a73e-4138-a54d-716291c1efb2/cb_media.png)

The **Media** folder includes all the files associated with using media in your production. Some of the files in this section will be automatically populated at the Root level of the Content Browser by the [Media Framework](/documentation/en-us/unreal-engine/media-framework-in-unreal-engine) plugin. The folders here are used in the background by the Media Profiles, but you should almost never have reason to work with them directly.

* Bundles - Auto populated at the Content Root level by the Media Framework plugin.
* Proxies - Auto populated at the Content Root level by the Media Framework plugin.
* MediaOutputs
* MediaProfiles

  + MPR\_(Description1)
  + MPR\_(Description2)
* MediaSources - All Actors related to media content, with separate folders for each Media Source.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35a56298-ad66-441e-ac20-8e3eb37a9d87/media-chart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35a56298-ad66-441e-ac20-8e3eb37a9d87/media-chart.png)

A diagram showing the recommended Media folder structure for your project in the Content Browser.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
