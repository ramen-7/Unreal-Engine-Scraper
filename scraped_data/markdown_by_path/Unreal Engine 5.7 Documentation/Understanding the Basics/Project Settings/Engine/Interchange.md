<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/interchange-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Interchange

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine "Project Settings")
7. [Engine](/documentation/en-us/unreal-engine/engine-settings-in-the-unreal-engine-project-settings "Engine")
8. Interchange

# Interchange

Interchange Settings section of the Unreal Engine Project Settings.

On this page

## Interchange

Interchange is a new import system that you can use to import Assets directly into the Level. Currently, this system is in development and will be refined in the next versions of Unreal Engine.

### Interchange

| **Section** | **Description** |
| --- | --- |
| **Pipeline Stacks** | All the available pipeline stacks you want to use to import with Interchange.  The chosen pipeline stack executes all the pipelines in order, from top to bottom.  You can reorder the pipelines by clicking and dragging the grip on the left of any pipelines. |
| **Default Pipeline Stack** | This tells Interchange which pipeline to select when importing Assets. |
| **Pipeline Configuration Dialog Class** | This tells Interchange which pipeline to pop up when you need to configure the pipelines.  You can choose from the following options:   * **None** * **InterchangePipelineConfigurationBase** * **InterchangePipelineConfigurationGeneric** |
| **Show Pipeline Stacks Configuration Dialog** | If enabled, the pipeline stacks configuration dialog will show every time Interchange must choose a pipeline to import or re-import.  If disabled, Interchange will use the `DefaultPipelineStack`. |

### Interchange (Experimental)

| **Section** | **Description** |
| --- | --- |
| **Use Interchange when Importing Into Level** | If enabled, will use Interchange when importing Assets into the Level. |
| **Default Scene Pipeline Stack** | This tells Interchange which pipeline to select when importing scenes. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Interchange](/documentation/en-us/unreal-engine/interchange-settings-in-the-unreal-engine-project-settings?application_version=5.7#interchange)
* [Interchange](/documentation/en-us/unreal-engine/interchange-settings-in-the-unreal-engine-project-settings?application_version=5.7#interchange-2)
* [Interchange (Experimental)](/documentation/en-us/unreal-engine/interchange-settings-in-the-unreal-engine-project-settings?application_version=5.7#interchange(experimental))
