<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/oodle-data?application_version=5.7 -->

# Oodle Data

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
5. [Testing and Optimizing Your Content](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content "Testing and Optimizing Your Content")
6. [Using Oodle](/documentation/en-us/unreal-engine/using-oodle-in-unreal-engine "Using Oodle")
7. Oodle Data

# Oodle Data

An overview of using Oodle Data to optimize delivering your package files to users.

![Oodle Data](https://dev.epicgames.com/community/api/documentation/image/6981ecee-6b96-4213-812e-116f074a2680?resizing_type=fill&width=1920&height=335)

 On this page

**Oodle Data** provides a compression format for `.pak` files and IOStore files. It is supplied as a plugin which should be enabled by default.

[![The Oodle Data plugin](https://dev.epicgames.com/community/api/documentation/image/3d351c36-e896-40ce-b4fa-bd08e49ba46e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d351c36-e896-40ce-b4fa-bd08e49ba46e?resizing_type=fit)

The parameters and settings for using Oodle Data with IOStore files are identical to those for .pak files in **Unreal Engine**.

When packaging, you will know you are using Oodle Data if you see a log similar to the following, with your specific settings listed for method and level:

`Oodle v2.9.0 initializing with method=Kraken, level=3=Fast`

In other contexts where you need Oodle Data to decode the packages files, you will see the following in the log:

`LogPluginManager: Mounting plugin OodleData`

## Key Concepts for Oodle Data

Oodle Data exposes two controls for managing the output: The **compression method** and the **compression level**. It is important to understand the distinction between them:

* The compression *method* trades off how small the data gets with how fast it is to decode.
* The compression *level* determines how long it takes to encode the data.

The decoder at runtime never needs to know what method was used.

### Compression Methods

There are four different compression methods available, representing different levels of compression and decode speed.

| Method | Description |
| --- | --- |
| Kraken | High compression with good decode speed, the usual default. |
| Mermaid | Less compression and faster decode speed; effective when CPU usage is limited or on platforms with less CPU power. |
| Selkie | Even less compression and faster than Mermaid. |
| Leviathan | More compression and slower to decode than Kraken. |

### Compression Level (Effort Level)

Compression Level is a number between -4 and 9, representing encoding speed. Compression level values are referred to as follows:

| Level | Name | Other Information |
| --- | --- | --- |
| -4 | HyperFast4 |  |
| -3 | HyperFast3 |  |
| -2 | HyperFast2 |  |
| -1 | HyperFast1 |  |
| 0 | None | Just copies the raw bytes. |
| 1 | SuperFast |  |
| 2 | VeryFast |  |
| 3 | Fast | Good for daily use. |
| 4 | Normal |  |
| 5 | Optimal1 |  |
| 6 | Optimal2 | Recommended baseline optimal encoder. |
| 7 | Optimal3 |  |
| 8 | Optimal4 |  |
| 9 | Optimal5 |  |

## Enabling Oodle Data

Due to various overrides, there are several different places where you need to enable and configure Oodle Data. The baseline method for enabling it is using the **Packaging** settings in the **Project Settings** window.

In the Project Packaging settings, you will have to expand the **Advanced** parameters to see these.

[![The Advanced Packaging Project settings that apply to Oodle Data](https://dev.epicgames.com/community/api/documentation/image/f41b4d20-b1fc-430d-b77c-34af90d6c778?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f41b4d20-b1fc-430d-b77c-34af90d6c778?resizing_type=fit)

These settings can also be edited directly in your `BaseGame.ini` file under the `[/Script/UnrealEd.ProjectPackagingSettings]` header.

### Properties / Settings

These are the relevant properties in the Project Packaging area, with the equivalent `.ini` file setting.

| Property | .ini File Setting | Description |
| --- | --- | --- |
| Create compressed cooked packages | bCompressed | When enabled, Unreal will compress output packages unless overridden. |
| Pak File Compression Format(s) | PakFileCompressionFormats | Sets the list of compression formats. Set it to Oodle to use Oodle Data. |
| Pak File Compression Commandline Options | PackageAdditionalCompressionOptions | Specifies additional options to pass to the compression format. For Oodle, we recommend this be set to `-compressionblocksize=256KB`. |
| Use this Compression Format not hardware override | bForceUseProjectCompressionFormatIgnoreHardwareOverride | If set, the `HardwareCompressionFormat` in the `DataDrivenPlatformInfo.ini` file will be ignored, and these settings will be used. So, you could set things up using the above settings, use `HardwareCompressionFormat` to ignore them, and then ignore THAT with this setting, getting back to where you started. |
| Pak File Compression Method | PackageCompressionMethod | Specifies the compression method as previously described (for example, Kraken). |
| Encoder Effort Level for Debug & Development | PackageCompressionLevel\_DebugDevelopment | Specifies the amount of time to spend encoding. This is a number from the previously-described Compression Level settings (3 by default). |
| Encoder Effort Level for Test & Shipping | PackageCompressionLevel\_TestShipping | Specifies the amount of time to spend encoding. This is a number from the previously-described Compression Level settings (5 by default). |
| Encoder Effort Level for Distribution | PackageCompressionLevel\_Distribution | Specifies the amount of time to spend encoding. This is a number from the previously-described Compression Level settings (7 by default). |

### Example Settings

In your `BaseGame.ini` file, this is a representative set of settings:

C++

```
|  |  |
| --- | --- |
|  | [/Script/UnrealEd.ProjectPackagingSettings] |
|  | bCompressed=True |
|  | PakFileCompressionFormats=Oodle |
|  | PackageAdditionalCompressionOptions=-compressionblocksize=256KB |
|  | PackageCompressionMethod=Kraken |
|  | PackageCompressionLevel_Distribution=7 |
|  | PackageCompressionLevel_TestShipping=5 |
|  | PackageCompressionLevel_DebugDevelopment=3 |
|  | bForceUseProjectCompressionFormatIgnoreHardwareOverride=False |
```

[/Script/UnrealEd.ProjectPackagingSettings]
bCompressed=True
PakFileCompressionFormats=Oodle
PackageAdditionalCompressionOptions=-compressionblocksize=256KB
PackageCompressionMethod=Kraken
PackageCompressionLevel\_Distribution=7
PackageCompressionLevel\_TestShipping=5
PackageCompressionLevel\_DebugDevelopment=3
bForceUseProjectCompressionFormatIgnoreHardwareOverride=False

Copy full snippet(9 lines long)

### Platform-Specific Exceptions

If a given target platform supports hardware data compression, it is likely exposed in the `DataDrivenPlatformInfo.ini` file in the platform's configuration directory, for example:

C++

```
|  |  |
| --- | --- |
|  | [DataDrivenPlatformInfo] |
|  | HardwareCompressionFormat=Zlib |
```

[DataDrivenPlatformInfo]
HardwareCompressionFormat=Zlib

Copy full snippet(2 lines long)

However, if you want to bypass the hardware data compression and use Oodle Data anyway, you can set `bForceUseProjectCompressionFormatIgnoreHardwareOverride=True` in the platform's `(Platform)Game.ini` file settings.

This will cause the packaging for the target platform to use Oodle Data, rather than the (in this example) hardware zlib.

* [compression](https://dev.epicgames.com/community/search?query=compression)
* [oodle](https://dev.epicgames.com/community/search?query=oodle)
* [packaging](https://dev.epicgames.com/community/search?query=packaging)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Key Concepts for Oodle Data](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#key-concepts-for-oodle-data)
* [Compression Methods](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#compression-methods)
* [Compression Level (Effort Level)](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#compression-level-effort-level)
* [Enabling Oodle Data](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#enabling-oodle-data)
* [Properties / Settings](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#properties-settings)
* [Example Settings](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#example-settings)
* [Platform-Specific Exceptions](/documentation/en-us/unreal-engine/oodle-data?application_version=5.7#platform-specific-exceptions)

Related documents

[Packaging Projects

![Packaging Projects](https://dev.epicgames.com/community/api/documentation/image/226adb79-9ed2-42c2-8690-1933a3519f28?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/packaging-unreal-engine-projects)
