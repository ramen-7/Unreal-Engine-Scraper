<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# User Interface

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
8. User Interface

# User Interface

Reference for the User Interface Settings section of the Unreal Engine Project Settings.

On this page

## User Interface

### Focus

| **Section** | **Description** |
| --- | --- |
| **Render Focus Rule** | Rule to determine whether the Engine should render the Focus Brush for widgets that have user focus.  You can choose from the following options:   * **Always:** Focus Brush will always be rendered for widgets that have user focus. * **Non-Pointer:** Focus Brush will be rendered for widgets that have user focus not set based on pointer causes. * **Navigation Only:** Focus Brush will be rendered for widgets that have user focus only if the focus was set by navigation. * **Never:** Focus Brush will not be rendered. |

### Hardware Cursors

| **Section** | **Description** |
| --- | --- |
| **Hardware Cursors** | This setting overrides default cursors provided by the operating system with the raw image files that you specify. |

### Software Cursors

| **Section** | **Description** |
| --- | --- |
| **Software Cursors** | This setting overrides hardware cursors with the Unreal Motion Graphics widgets that you specify. |

### DPI Scaling

| **Section** | **Description** |
| --- | --- |
| **Application Scale** | (Optional) An application scale to apply on top of the custom scale rules.  For example, if you want to expose a property in your game title, you can modify this underlying value to scale the entire UI. |
| **DPI Scale Rule** | The rule to use when deciding what scale to apply.  You can choose from the following options:   * **Shortest Side:** Evaluates the scale curve based on the shortest side of the viewport. * **Longest Side:** Evaluates the scale curve based on the longest side of the viewport. * **Horizontal:** Evaluates the scale curve based on the X axis of the viewport. * **Vertical:** Evaluates the scale curve based on the Y axis of the viewport. * **Scale to Fit:** Doesn't use the scale curve. Emulates scale box behavior by using `DesignScreenSize` and scaling the content relatively to it. * **Custom:** Allows custom rule interpretation. |
| **Custom Scaling Rule Class** | If you set the **DPI Scale Rule** to **Custom**, select the class to use instead of any of the built-in rules. |
| **DPI Curve** | Controls how the UI is scaled at different resolutions based on the **DPI Scale Rule**. |
| **DPI Curve (External Curve)** | Select a Curve Asset from the Content Browser to use instead of the base DPI Curve setting. |
| **Allow High DPI in Game Mode** | If enabled, the game window will have high-DPI awareness enabled on desktop platforms.  We recommend that you enable this only if the game UI allows users to modify 3D resolution scaling. |
| **Design Screen Size** | Used only with the **Scale to Fit** scaling rule from the **DPI Scale Rule** options.  Defines the native resolution that the source UI textures werer created for.  DPI scaling at this screen resolution will be set to 1.0. |

### Widgets

| **Section** | **Description** |
| --- | --- |
| **Load Widgets on Dedicated Server** | If disabled, widget references will be stripped during cook for server builds and not loaded at runtime. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [User Interface](/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7#userinterface)
* [Focus](/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7#focus)
* [Hardware Cursors](/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7#hardwarecursors)
* [Software Cursors](/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7#softwarecursors)
* [DPI Scaling](/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7#dpiscaling)
* [Widgets](/documentation/en-us/unreal-engine/user-interface-settings-in-the-unreal-engine-project-settings?application_version=5.7#widgets)
