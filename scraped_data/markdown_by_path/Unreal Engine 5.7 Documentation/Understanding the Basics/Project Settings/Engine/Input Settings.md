<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Input Settings

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
8. Input Settings

# Input Settings

Input Settings section of the Unreal Engine Project Settings.

On this page

## Input

### Bindings

Action and Axis Mappings provide a mechanism to conveniently map keys and axes to input behavior and the keys that invoke it.

| **Section** | **Description** |
| --- | --- |
| **Speech Mappings** | List of Speech Mappings. |
| **Action Mappings** | List of Action Mappings for key presses and releases. |
| **Axis Mappings** | List of Axis Mappings that allow for inputs that have a continuous range. |
| **Axis Config** | List of Axis Properties. |
| **Alt+Enter Toggles Fullscreen** | If enabled, you can use **Alt** + **Enter** to toggle fullscreen at runtime. |
| **F11 Toggles Fullscreen** | If enabled, you can use **F11** to toggle fullscreen at runtime. |

### Viewport Properties

| **Section** | **Description** |
| --- | --- |
| **Capture Mouse on Launch** | Controls whether the viewport will capture the mouse on launch of the application. |
| **Default Viewport Mouse Capture Mode** | The default mouse capture mode for the game viewport.  You can choose from the following options:   * **No Capture** * **Capture Permanently** * **Capture Permanently Including Initial Mouse Down** * **Capture During Mouse Down** * **Capture During Right Mouse Down** |
| **Default Viewport Mouse Lock Mode** | The default mouse lock state behavior when the viewport acquires capture.  You can choose from the following options:   * **Do Not Lock** * **Lock on Capture** * **Lock Always** * **Lock in Fullscreen** |

### Input

| **Section** | **Description** |
| --- | --- |
| **Enable Legacy Input Scales** | Enable the use of legacy input scales on the player controller (`InputYawScale`, `InputPitchScale`, and `InputRollScale`). |

### Mobile

| **Section** | **Description** |
| --- | --- |
| **Always Show Touch Interface** | Specifies whether the touch input interface should be shown at all times or just when the platform has a touch screen. |
| **Show Console on Four-Finger Tap** | Specifies whether or not to show the console on 4-finger tap on mobile platforms. |
| **Enable Gesture Recognizer** | Specifies whether or not to use the gesture recognition system to convert touches into gestures that can be bound and queried. |
| **Default Touch Interface** | The default on-screen touch input interface for the game (can be set to `null` to disable the onscreen interface). |

### Virtual Keyboard (Mobile)

| **Section** | **Description** |
| --- | --- |
| **Use Autocorrect** | If enabled, virtual keyboards will have autocorrect enabled.  Currently only supported on mobile devices. |
| **Excluded Autocorrect OS** | Disables autocorrect for these operating systems, even if autocorrect is enabled.  Use the format `[platform] [OSversion]` (for example, "iOS 11.2" or "Android 6").  More specific versions will disable autocorrect for fewer devices ("iOS 11" will disable autocorrect for all devices running iOS 11, but "iOS 11.2.2" will not disable autocorrect for devices running 11.2.1). |
| **Excluded Autocorrect Cultures** | Disables autocorrect for these cultures, even if autocorrect is turned on.  These should be ISO-compliant language and country codes, such as "en" or "en-US". |
| **Excluded Autocorrect Device Models** | Disables autocorrect for these device models, even if autocorrect is turned on.  Model IDs listed here will match against the start of the device's model (for example, "SM-" will match all device model IDs that start with "SM-").  This is currently only supported on Android devices. |

### Default Classes

| **Section** | **Description** |
| --- | --- |
| **Default Player Input Class** | Default class type for player input object.  May be overridden by the player controller. |
| **Default Input Component Class** | Default class type for Pawn input components. |

### Console

| **Section** | **Description** |
| --- | --- |
| **Console Keys** | Keyboard shortcuts to open the console. |

### Mouse Properties

| **Section** | **Description** |
| --- | --- |
| **Use Mouse for Touch** | Allows mouse to be used for touch. |
| **Enable Mouse Smoothing** | Mouse smoothing control. |
| **Enable FOVScaling** | Scales the mouse input axes (both horizontal and vertical axes) from the player controller's input to the Player Camera Manager's field of view.  The lower the FOV value, the less sensitivity from the mouse will be in the project. |
| **FOVScale** | The scaling value to multiply the field of view by `[value]`. |
| **Double Click Time** | If a key is pressed twice in this amount of time, it is considered a "double click". |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Input](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#input)
* [Bindings](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#bindings)
* [Viewport Properties](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#viewportproperties)
* [Input](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#input-2)
* [Mobile](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#mobile)
* [Virtual Keyboard (Mobile)](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#virtualkeyboard(mobile))
* [Default Classes](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#defaultclasses)
* [Console](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#console)
* [Mouse Properties](/documentation/en-us/unreal-engine/input-settings-in-the-unreal-engine-project-settings?application_version=5.7#mouseproperties)
