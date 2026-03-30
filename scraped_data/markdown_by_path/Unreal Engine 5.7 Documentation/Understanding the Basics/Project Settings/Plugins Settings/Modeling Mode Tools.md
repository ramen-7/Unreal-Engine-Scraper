<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-tools-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Modeling Mode Tools

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
7. [Plugins Settings](/documentation/en-us/unreal-engine/plugins-section-of-the-unreal-engine-project-settings "Plugins Settings")
8. Modeling Mode Tools

# Modeling Mode Tools

Reference for the Modeling Mode Tools section of the Unreal Engine Project Settings.

![Modeling Mode Tools](https://dev.epicgames.com/community/api/documentation/image/780c6386-3a7e-4cde-b1f1-616f11a97e1f?resizing_type=fill&width=1920&height=335)

 On this page

## Modeling Mode Tools

### Modeling Tools

| **Setting** | **Description** |
| --- | --- |
| **Rendering** |  |
| **Enable Ray Tracing While Editing** | Enable real-time ray tracing support for Mesh Editing Tools.  This will impact performance of tools with real-time feedback like 3D sculpting. |
| **New Mesh Objects** |  |
| **Enable Ray Tracing** | Enable ray tracing support for new mesh objects created by Modeling Tools, if support is optional (for example, `DynamicMeshActors`). |
| **Enable Collision** | Enable collision support for new mesh objects created by Modeling Tools. |
| **Collision Mode** | Default collision mode set on new mesh objects created by Modeling Tools.  You can choose from the following options:   * **Project Default:** Use project physics settings (`DefaultShapeComplexity`). * **Simple and Complex:** Create both simple and complex shapes. Simple shapes are used for regular scene queries and collision tests. Complex shapes (per poly) are used for complex scene queries. * **Use Simple Collision as Complex:** Create only simple shapes. Use simple shapes for all scene queries and collision tests. * **Use Complex Collision as Simple:** Create only complex shapes (per poly). Use complex shapes for all scene queries and collision tests. Can be used in simulation for static shapes only (that is, can be collided against but not moved through forces of velocity). |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Modeling Mode Tools](/documentation/en-us/unreal-engine/modeling-mode-tools-settings-in-the-unreal-engine-project-settings?application_version=5.7#modelingmodetools)
* [Modeling Tools](/documentation/en-us/unreal-engine/modeling-mode-tools-settings-in-the-unreal-engine-project-settings?application_version=5.7#modelingtools)
