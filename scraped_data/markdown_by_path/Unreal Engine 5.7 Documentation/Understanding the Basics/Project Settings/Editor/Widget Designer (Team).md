<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/widget-designer-team-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Widget Designer (Team)

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
8. Widget Designer (Team)

# Widget Designer (Team)

Reference for the Widget Designer (Team) section of the Unreal Engine Project Settings.

![Widget Designer (Team)](https://dev.epicgames.com/community/api/documentation/image/336f076f-60cb-4389-85a5-553116e1c0c0?resizing_type=fill&width=1920&height=335)

 On this page

## Widget Designer (Team)

Widgets are classes that represent individual menus or on-screen elements. You can define them in the Content Browser and build them in UMG, which has both a WYSIWYG (What You See Is What You Get) designer and a Blueprint graph.

### Compiler

| **Section** | **Description** |
| --- | --- |
| **Allow Blueprint Tick** | If disabled, widgets that these compiler options apply to will not be allowed to respond to the **Event Tick** event. |
| **Allow Blueprint Paint** | If disabled, widgets that these compiler options apply to will not be allowed to override the **On Paint** function. |
| **Property Binding Rule** | This setting controls whether to let the engine use property bindings in widgets.  Using property bindings can have a large performance impact.  You can choose from the following options:   * **Allow:** Allows the free use of property binding. * **Prevent:** Prevents any new property bindings, but you can still edit widgets with property bindings. The buttons will be missing on all existing widgets that don't have bindings. * **Prevent and Warn:** Prevents any new property bindings and gives a warning when the engine compiles any existing binding. * **Prevent and Error:** Prevents any new property bindings and gives an error when the engine compiles any existing binding. |
| **Rules** | Custom widget compiler rule classes that you can write in C++. You can make these by extending the `UWidgetCompilerRule` class, which is in `WidgetCompilerRule.h`. These classes will have an `ExecuteRule` function that runs when you compile a widget blueprint.  You can use this rules list to execute some custom code before the widget is finalized and compiled. |
| **Directory Compiler Options** | Allow Blueprint Tick, Allow Blueprint Paint, Property Binding Rule, and custom Rules, which you can set in specific project directories in a selective way. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Widget Designer (Team)](/documentation/en-us/unreal-engine/widget-designer-team-settings-in-the-unreal-engine-project-settings?application_version=5.7#widgetdesigner(team))
* [Compiler](/documentation/en-us/unreal-engine/widget-designer-team-settings-in-the-unreal-engine-project-settings?application_version=5.7#compiler)
