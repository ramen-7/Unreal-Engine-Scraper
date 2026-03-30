<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Animation

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
8. Animation

# Animation

Reference for the Animation Settings section of the Unreal Engine Project Settings.

On this page

## Animation

### Compression

| **Section** | **Description** |
| --- | --- |
| **Compress Commandlet Version** | The compression version for the recompress commandlet.  Increase this value if you want to trigger a full recompression of all animations. Otherwise, only newly imported animations will be recompressed. |
| **Key End Effectors Match Name Array** | List of bone names to treat with higher precision, in addition to any bones with sockets. |
| **Force Recompression** | If enabled, this setting will forcibly recompress every animation.  Disable this setting before checking in your project, otherwise the Engine will recompress all animations each time the project is opened, affecting the performance negatively for all users of this project. |

### Performance

| **Section** | **Description** |
| --- | --- |
| **Enable Performance Log** | If true, recompression will log performance information. |
| **Strip Animation Data on Dedicated Server** | If true, animation track data will be stripped from dedicated server cooked data. |
| **Tick Animation on Skeletal Mesh Init** | When this property is enabled, an Animation-Tick will occur upon the initialization of a Skeletal Mesh, which is a behavior known as Zero-Ticking.  This property is disabled by default.  Zero-Ticking Animations during a Skeletal Mesh initialization was the default behavior for all versions of Unreal Engine before 4.19. |

### Custom Attributes

| **Section** | **Description** |
| --- | --- |
| **Bone Timecode Custom Attribute Name Settings** | Names that identify bone custom attributes representing the individual components of a timecode and a subframe along with a take name.  These will be included in the list of bone custom attribute names to import. |
| **Bone Custom Attributes Names** | List of custom attributes to import directly on their corresponding bone.  The meaning field is used to contextualize the attribute name and customize tooling for it. |
| **Bone Names With Custom Attributes** | List of bone names for which all custom attributes are directly imported on the bone. |
| **Attribute Blend Modes** | Custom Attribute-specific blend types (by name).  You can choose from the following options:   * **Override** * **Blend** |
| **Default Attribute Blend Mode** | Default Custom Attribute blend type. |
| **Transform Attribute Names** | Names to match against when importing FBX node transform curves as attributes (can use `?` and `*` wildcards). |

### Mirroring

| **Section** | **Description** |
| --- | --- |
| **Mirror Find Replace Expressions** | Find and Replace Expressions used for mirroring. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Animation](/documentation/en-us/unreal-engine/animation-settings-in-the-unreal-engine-project-settings?application_version=5.7#animation)
* [Compression](/documentation/en-us/unreal-engine/animation-settings-in-the-unreal-engine-project-settings?application_version=5.7#compression)
* [Performance](/documentation/en-us/unreal-engine/animation-settings-in-the-unreal-engine-project-settings?application_version=5.7#performance)
* [Custom Attributes](/documentation/en-us/unreal-engine/animation-settings-in-the-unreal-engine-project-settings?application_version=5.7#customattributes)
* [Mirroring](/documentation/en-us/unreal-engine/animation-settings-in-the-unreal-engine-project-settings?application_version=5.7#mirroring)
