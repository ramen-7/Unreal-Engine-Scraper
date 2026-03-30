<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-project-for-grooms-in-unreal-engine?application_version=5.7 -->

# Setting Up a Project to use Grooms

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
6. [Hair Rendering and Simulation](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine "Hair Rendering and Simulation")
7. Setting Up a Project to use Grooms

# Setting Up a Project to use Grooms

Setup your projects to import and render groom assets.

![Setting Up a Project to use Grooms](https://dev.epicgames.com/community/api/documentation/image/bbe0462c-961e-406d-99e6-4942c9facf4e?resizing_type=fill&width=1920&height=335)

 On this page

Before you can start using grooms in your Unreal Engine projects, you'll first need to enable some project settings and plugins that help you import and render them.

## Project Settings

When you enable grooms for your project, a basic skinning system is embedded for forwarding skin deformation to the groom system. However, this system only supports bone-based deformation. To use more advanced skin deformation, such as morph targets and deformers, you'll want to enable the [Skin Cache](/documentation/en-us/unreal-engine/skeletal-mesh-rendering-paths-in-unreal-engine) system.

In the **Project Settings** under **Rendering > Optimizations**, you can enable the Skin Cache system by checking the box for **Support Compute Skin Cache**.

This setting requires the editor to be restarted.

![Groom Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0ee3a4eb-4e36-4ff6-9669-f43f5be6f54a/grooms-project-settings.png)

## Groom Plugins

The **Plugins** browser includes required and optional plugins that support using grooms in your Unreal Engine projects. You can open it from the main menu under the **Edit** menu.

The following Groom plugins are available:

![Groom Plugins](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a55f795b-27e8-4f33-bbb4-e62f81c897e0/groom-plugins-browser.png)


Enabling these plugins requires the editor to be restarted.

| Plugin Name | Description | Default Status |
| --- | --- | --- |
| Geometry |  |  |
| **Alembic Groom Importer** | Enables you to import Alembic (\*.abc) files that contain groom data sets into Unreal Engine. | Disabled |
| **Groom** | Enables rendering and simulation of imported grooms. | Disabled |
| [Optional] **Hair Card Generator** | Enables generation of cards from strands in your groom. You can configure parameters to determine how the cards are generated from your groom, which can also be used to generate different levels of detail. To learn more about how to generate groom cards, see [Groom Cards and Meshes](/documentation/en-us/unreal-engine/setting-up-cards-and-meshes-for-grooms-in-unreal-engine) | Disabled |
| Animation |  |  |
| [Optional] **Deformer Graph** | Enables deformation graphs that you can use to perform and customize mesh deformations for any skinned mesh. To learn more about how to use this with your grooms, see [Groom Deformer](/documentation/en-us/unreal-engine/setting-up-a-groom-deformer-graph-in-unreal-engine). | Enabled |

* [plugins](https://dev.epicgames.com/community/search?query=plugins)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Project Settings](/documentation/en-us/unreal-engine/setting-up-a-project-for-grooms-in-unreal-engine?application_version=5.7#projectsettings)
* [Groom Plugins](/documentation/en-us/unreal-engine/setting-up-a-project-for-grooms-in-unreal-engine?application_version=5.7#groomplugins)
