<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-encoding-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Texture Encoding

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
8. Texture Encoding

# Texture Encoding

Reference for the Texture Encoding section of the Unreal Engine Project Settings.

On this page

## Texture Encoding

### Encode Speed Settings

| **Section** | **Description** |
| --- | --- |
| **Final Uses RDO** | If true, the speed of texture encoding when saving textures to disk in compressed formats enables Rate-Distortion Optimization (RDO) on supported encoders to decrease on-disc size of textures in compressed package files.  This rate-distortion tradeoff is controlled by a parameter called [lambda](/documentation/en-us/unreal-engine/using-oodle-in-unreal-engine#understandinglambda).  The `LossyCompressionAmount` parameter on textures is used to control lambda.`  Specific `LossyCompressionAmount` values correspond to RDO lambdas of:   * None - Disable RDO for this texture. * Lowest - 1 (Least distortion) * Low - 10 * Medium - 20 * High - 30 * Highest - 40   If this is set to Default, the `LossyCompressionAmount` in the LODGroup (Texture Group) for the texture is used instead. If `LossyCompressionAmount` is also Default, then the **Final RDO Lambda** setting described on this page is used.  Note that any distortion introduced is on top of, and likely less than, any introduced by the format itself. |
| **Final RDO Lambda** | Ignored if **Final Uses RDO** is false.  This value is used if a given texture's `LossyCompressionAmount` is set to Default.  Otherwise, the value of `LossyCompressionAmount` is translated into a fixed lambda (see **Final Uses RDO** on this page).  Low values lead to higher quality results. A value of 1 amounts to the least distortion. |
| **Final Effort Level** | Specifies how much time to take trying for better encoding results.  You can choose from the following options:   * **Default:** Let the encoder decide what's best. * **Low:** Faster encoding, lower quality. This quality level is not recommended for your final packaged project. * **Normal:** Offers a balanced output between encoding time and quality. * **High:** Takes the longest time for the highest quality. This is the recommended setting for nightly builds and unattended cooks. |
| **Final Universal Tiling** | Optimizes texture encoding for tiled texture layouts on disk.  This only applies to Oodle with RDO (**Fast Uses RDO** or **Final Uses RDO**) enabled.  256 KB is the recommended value for the majority of use cases.  Enabling this option decreases the on-disk sizes of textures for platforms with exposed texture tiling (console platforms), but slightly increases texture sizes for platforms with opaque tiling (desktop platforms).  You can choose from the following options:   * **Disabled** * **Enabled 256 KB** * **Enabled 64 KB** |
| **Fast Uses RDO** | If enabled, final encode speed enables rate-distortion optimization on supported encoders to decrease on-disk size of textures in compressed package files.  This rate-distortion tradeoff is controlled by a parameter called [lambda](/documentation/en-us/unreal-engine/using-oodle-in-unreal-engine#understandinglambda).  The `LossyCompressionAmount` parameter on textures is used to control lambda.  Specific `LossyCompressionAmount` values correspond to RDO lambdas of:   * None - Disable RDO for this texture. * Lowest - 1 (least distortion) * Low - 10 * Medium - 20 * High - 30 * Highest - 40   If this is set to Default, the `LossyCompressionAmount` in the LODGroup for the texture is used. If that is also set to Default, then the **RDOLambda** setting described on this page is used.  Note that any distortion introduced is on top of, and likely less than, any introduced by the format itself. |
| **Fast RDO Lambda** | Ignored if **UsesRDO** is false.  This value is used if a given texture's `LossyCompressionAmount` is set to Default.  Otherwise, the value of `LossyCompressionAmount` is translated into a fixed lambda (see **Uses RDO** settings on this page).  Low values lead to higher quality results. A value of 1 amounts to the least distortion. |
| **Fast Effort Level** | Specifies how much time to take trying for better encoding results.  You can choose from the following options:   * **Default:** Let the encoder decide what's best. * **Low:** Faster encoding, lower quality. This quality level is not recommended for your final packaged project. * **Normal:** Offers a balanced output between encoding time and quality. * **High:** Takes the longest time for the highest quality. This is the recommended setting for nightly builds and unattended cooks. |
| **Fast Universal Tiling** | Optimizes texture encoding for tiled texture layouts on disk.  This only applies to Oodle with RDO enabled.  256 KB is the recommended value for the majority of use cases.  Enabling this option decreases the on-disk sizes of textures for platforms with exposed texture tiling (console platforms), but slightly increases texture sizes for platforms with opaque tiling (desktop platforms). |

### Encode Speeds

| **Section** | **Description** |
| --- | --- |
| **Cook Uses Speed** | Defines which encode speed non-interactive editor sessions (commandlets) will use.  You can choose from the following options:   * **Final:** Use the Final encode speed settings in `UTextureEncodingProjectSettings`. * **Final if Available:** Try and fetch the final encode speed settings. If they don't exist, encode with Fast. * **Fast:** Use the Fast"encode speed settings in `UTextureEncodingProjectSettings`. |
| **Editor Uses Speed** | Defines which encode speed everything else uses.  You can choose from the following options:   * **Final:** Use the Final encode speed settings in `UTextureEncodingProjectSettings`. * **Final if Available:** Try and fetch the final encode speed settings. If they don't exist, encode with Fast. * **Fast:** Use the Fast"encode speed settings in `UTextureEncodingProjectSettings`. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Texture Encoding](/documentation/en-us/unreal-engine/texture-encoding-settings-in-the-unreal-engine-project-settings?application_version=5.7#textureencoding)
* [Encode Speed Settings](/documentation/en-us/unreal-engine/texture-encoding-settings-in-the-unreal-engine-project-settings?application_version=5.7#encodespeedsettings)
* [Encode Speeds](/documentation/en-us/unreal-engine/texture-encoding-settings-in-the-unreal-engine-project-settings?application_version=5.7#encodespeeds)
