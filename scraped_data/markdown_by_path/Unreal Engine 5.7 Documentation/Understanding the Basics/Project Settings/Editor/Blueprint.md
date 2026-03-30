<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-project-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Blueprint

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
7. [Editor](/documentation/en-us/unreal-engine/editor-section-of-the-unreal-engine-project-settings "Editor")
8. Blueprint

# Blueprint

Reference for the Blueprint Project Settings section of the Unreal Engine Project Settings.

![Blueprint](https://dev.epicgames.com/community/api/documentation/image/179cdc98-77b1-4202-a485-d09caeda36a1?resizing_type=fill&width=1920&height=335)

 On this page

## Blueprint Project Settings

### Blueprints

| **Section** | **Description** |
| --- | --- |
| **Force All Dependencies to Recompile (deprecated)** | Disables faster compiles for individual Blueprints if they have no function signature changes.  This setting has been deprecated and should not be used. You can't force all dependencies to compile when no changes are detected. |
| **Compiler Messages Disabled Except in Editor** | List of compiler messages that have been suppressed outside of full, interactive editor sessions for the current project. This is useful for silencing warnings that were added to the engine after the project was created and are going to be addressed as they are found by content authors. |
| **Compiler Messages Disabled Entirely** | List of compiler messages that have been suppressed completely. You should only supress compiler messages when using blueprints that you can't update and are raising non-critical warnings. |

### Actors

| **Section** | **Description** |
| --- | --- |
| **Validate Unloaded Soft Actor References** | If enabled, the editor will load packages to look for soft references to Actors when deleting or renaming Actors. This can be slow in large projects.  Disable this option to improve performance, but note that this will increase the chance of breaking Blueprints and sequences that use soft Actor references. |

### Experimental

| **Section** | **Description** |
| --- | --- |
| **Enable Child Actor Expansion in Tree View** | Enable the option to expand Child Actor components within component tree views. |
| **Default Child Actor Tree View Mode** | Default view mode to use for child Actor components in a Blueprint Actor's component tree hierarchy.  You can choose from the following options:   * **Component Only:** Show only the outer component as a single component node. * **Component with Child Actor:** Include the child Actor hierarchy attached to the outer component as the root node. * **Child Actor Only:** Show only as a child Actor hierarchy (do not show the outer component node as the root). |
| **Namespaces to Always Include** | The list of namespaces to always expose in any Blueprint for all project users.  This setting requires Blueprint namespace to be enabled in **Editor Preferences**. |

### Play

| **Section** | **Description** |
| --- | --- |
| **Base Classes to Allow Recompiling During Play in Editor** | Any Blueprint deriving from one of these base classes will be allowed to recompile during Play-in-Editor (PIE). This setting exists both as an editor preference and project setting, and will take effect if enabled from either one of these panels. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Blueprint Project Settings](/documentation/en-us/unreal-engine/blueprint-project-settings-in-the-unreal-engine-project-settings?application_version=5.7#blueprintprojectsettings)
* [Blueprints](/documentation/en-us/unreal-engine/blueprint-project-settings-in-the-unreal-engine-project-settings?application_version=5.7#blueprints)
* [Actors](/documentation/en-us/unreal-engine/blueprint-project-settings-in-the-unreal-engine-project-settings?application_version=5.7#actors)
* [Experimental](/documentation/en-us/unreal-engine/blueprint-project-settings-in-the-unreal-engine-project-settings?application_version=5.7#experimental)
* [Play](/documentation/en-us/unreal-engine/blueprint-project-settings-in-the-unreal-engine-project-settings?application_version=5.7#play)
