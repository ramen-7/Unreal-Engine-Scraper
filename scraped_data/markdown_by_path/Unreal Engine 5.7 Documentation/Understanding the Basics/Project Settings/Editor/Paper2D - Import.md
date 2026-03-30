<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paper2d-import-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Paper2D - Import

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
8. Paper2D - Import

# Paper2D - Import

Reference for the Paper2D - Import section of the Unreal Engine Project Settings.

![Paper2D - Import](https://dev.epicgames.com/community/api/documentation/image/24832e83-d2ad-4686-af17-2ee936239303?resizing_type=fill&width=1920&height=335)

 On this page

## Paper2D - Import

### New Asset Settings

| **Section** | **Description** |
| --- | --- |
| **Pick Best Material when Creating Sprites** | Defines whether the source texture should be scanned when creating new sprites to determine the appropriate material.  If disabled, the Default Masked Material is always used. |
| **Pick Best Material when Creating Tile Maps** | Defines whether the source texture should be scanned when creating new tile maps (from a tile set or through importing) to determine the appropriate material.  If disabled, the Default Masked Material is always used. |
| **Analysis Can Use Opaque** | Defines whether opaque materials can be applied as part of the "best material" analysis. |
| **Default Pixels Per Unreal Unit** | The default scaling factor between pixels and Unreal Units (cm) to use for newly created sprite Assets (for example, 0.64 makes a 64 pixel wide sprite take up 100 cm). |

### Import Settings

| **Section** | **Description** |
| --- | --- |
| **Normal Map Texture Suffixes** | A list of default suffixes to use when looking for associated normal maps while importing sprites or creating sprites from textures. |
| **Base Map Texture Suffixes** | The default suffix to remove (if present) from a texture name before looking for an associated normal map using `NormalMapTextureSuffixes`. |
| **Default Sprite Texture Group** | The default texture group for imported sprite textures, tile sheets, and so on.  This option is typically set to **UI** for modern-style 2D assets, or **2D pixels** for retro-style 2D assets. |
| **Override Texture Compression** | Defines whether the texture compression settings should be overridden on imported sprite textures, tile sheets, and so on. |
| **Default Sprite Texture Compression** | Compression settings to use when building the texture.  The default texture group for imported sprite textures, tile sheets, and so on.  This option is typically set to **UI** for modern-style 2D assets, or **2D pixels** for retro-style 2D assets.  You can choose from the following options:   * **Default (DXT1/5, BC1/3 on DX11)** * **Normalmap (DXT5, BC5 on DX11)** * **Masks (no sRGB)** * **Grayscale (R8, RGB8 sRGB)** * **Displacementmap (8/16bit)** * **VectorDisplacementmap (RGBA8)** * **HDR (RGB, no sRGB)** * **UserInterface2D (RGBA)** * **Alpha (no sRGB, BC4 on DX11)** * **DistanceFieldFont (R8)** * **HDRCompressed (RGB, BC6H, DX11)** * **BC7 (DX11, optional A)** * **Half-Float (R16F)** |

### Material Settings

| **Section** | **Description** |
| --- | --- |
| **Unlit Default Masked Material** | The unlit default masked material for newly created sprites. "Masked" means binary opacity: things are either opaque or see-through, with nothing in-between. |
| **Unlit Default Translucent Material** | The unlit default translucent material for newly created sprites. "Translucent" means smooth opacity, which can vary continuously bewteen 0 and 1, but translucent rendering is more performance-intensive than opaque or masked rendering and has different sorting rules. |
| **Unlit Default Opaque Sprite Material** | The unlit default opaque material for newly created sprites. |
| **Lit Default Masked Material** | The lit default masked material for newly created sprites. "Masked" means binary opacity: things are either opaque or see-through, with nothing in-between. |
| **Lit Default Translucent Material Name** | The lit default translucent material for newly created sprites. "Translucent" means smooth opacity, which can vary continuously bewteen 0 and 1, but translucent rendering is more performance-intensive than opaque or masked rendering and has different sorting rules. |
| **Lit Default Opaque Material** | The lit default opaque material for newly created sprites. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Paper2D - Import](/documentation/en-us/unreal-engine/paper2d-import-settings-in-the-unreal-engine-project-settings?application_version=5.7#paper2d-import)
* [New Asset Settings](/documentation/en-us/unreal-engine/paper2d-import-settings-in-the-unreal-engine-project-settings?application_version=5.7#newassetsettings)
* [Import Settings](/documentation/en-us/unreal-engine/paper2d-import-settings-in-the-unreal-engine-project-settings?application_version=5.7#importsettings)
* [Material Settings](/documentation/en-us/unreal-engine/paper2d-import-settings-in-the-unreal-engine-project-settings?application_version=5.7#materialsettings)
