<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/emitter-settings-reference-for-niagara-effects-in-unreal-engine?application_version=5.7 -->

# Emitter Settings

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Reference](/documentation/en-us/unreal-engine/reference-for-niagara-effects-in-unreal-engine "Niagara Reference")
7. [Niagara System and Emitter Module Reference](/documentation/en-us/unreal-engine/system-and-emitter-module-reference-for-niagara-effects-in-unreal-engine "Niagara System and Emitter Module Reference")
8. Emitter Settings

# Emitter Settings

This page contains reference information for the Emitter Settings group in a Niagara emitter.

![Emitter Settings](https://dev.epicgames.com/community/api/documentation/image/bca6d2fc-2904-412e-b109-76178af8028b?resizing_type=fill&width=1920&height=335)

 On this page

## Emitter Properties Item

![Emitter Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/148b0331-5037-466c-ac4a-45c543f1d110/01-emitter-properties-item.png)

By default, the **Emitter Properties** item is included in every created emitter, even if you create an empty one. The Emitter Properties item contains the following base parameters.

| Parameter | Description |
| --- | --- |
| Emitter |  |
| **Local Space** | This setting toggles whether the particles within this emitter are relative to this emitter or to the global space. |
| **Determinism** | This setting toggles whether the random number generator (RNG) will be deterministic or non-deterministic globally. Any random calculation that is set to the emitter defaults will inherit this setting. You can still set individual random numbers to be deterministic or non-deterministic. In this case, deterministic means that the RNG will return results for the same configuration of the emitter, as long as the delta time is not variable. Any changes to the emitter's individual scripts will adjust the results. |
| **Random Seed** | If the **Determinism** setting is enabled, this is an emitter-based seed for the deterministic random number generator. |
| **Sim Target** | This determines whether the simulation is performed on the CPU or the GPU. |
| **Fixed Bounds** | This setting determines whether the fixed bounds can be edited. If it is enabled, there are Minimum and Maximum X, Y, and Z settings that can be adjusted. |
| **Interpolated Spawning** | When this setting is enabled, this emitter will spawn using interpolated parameter values, and it will perform a partial update at spawn time. This has a significant additional cost for spawning, but it will produce much smoother spawning for high spawn rates, erratic frame rates, and fast moving emitters. |
| **Requires Persistent ID** | When this is enabled, all particles emitted will be assigned a persistent ID. |
| **Combine Event Spawn** | This setting allows event based spawning to be combined into a single spawn. |
| Scalability |  |
| Scalability Settings For Scalability, there are five general settings: **Low**, **Medium**, **High**, **Epic**, and **Cinematic**. You can click to enable or disable a category for a particular emitter. Each category also has a dropdown menu listing various platforms that can display graphics at a particular level. You can include or exclude specific platforms in a category, instead of just enabling or disabling that category.  Consoles and some mobile platforms will not be displayed unless you set up the appropriate configuration and device profiles. |  |
| **Setting** | **Platforms to Include or Exclude** |
| **Low** | * Windows * Mac * Linux * Android |
| **Medium** | * Windows * iOS * Mac * Linux * Android |
| **High** | * Windows * Mac * Linux |
| **Epic** | * Windows * TVOS * Mac * Linux |
| **Cinematic** | * Windows * Mac * Linux |
| Asset Options |  |
| Asset Options |  |
| **Library Visibility** | This setting allows you to change if this emitter is exposed to the library , or should be explicitly hidden. |
| **Template Specification** | This setting toggles whether this emitter is a standart parent emitter, a template or a behaviour example. |
| **Template Asset Description** | If you identify this emitter as a Template Asset, you can click the icon on the right to find additional settings for **Inline Text** and **Referenced Text**. |
| **Category** | You can add the category to collate this emitter into for 'add new emotter dialogs'. |
|  |  |

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [module](https://dev.epicgames.com/community/search?query=module)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)
* [emitter](https://dev.epicgames.com/community/search?query=emitter)
* [system](https://dev.epicgames.com/community/search?query=system)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Emitter Properties Item](/documentation/en-us/unreal-engine/emitter-settings-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#emitterpropertiesitem)
