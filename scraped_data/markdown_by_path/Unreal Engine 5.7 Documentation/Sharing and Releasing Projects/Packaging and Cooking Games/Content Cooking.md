<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cooking-content-in-unreal-engine?application_version=5.7 -->

# Content Cooking

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
4. Content Cooking

# Content Cooking

Generating platform-specific content for assets used in the game.

![Content Cooking](https://dev.epicgames.com/community/api/documentation/image/b8aed717-06f6-4df9-9931-d6c066d8c5e6?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine stores content assets in particular formats which it uses internally, such as PNG for texture data or WAV for audio. However, this content needs to be converted to different formats for the various platforms, either because the platform uses a proprietary format, does not support the format Unreal uses to store the asset, or a more memory- or performance-effective format exists. The process of converting content from the internal format to the platform-specific format is referred to as **cooking**.

## Cooking Content from the Command Line

To cook data for your game, you need to use the Cook commandlet.

The basic cook is performed using the following:

```
	UnrealEditor.exe <GameName or uproject> -run=cook -targetplatform=<Plat1>+<Plat2> [-cookonthefly] [-map=<Map1>+<Map2>]
Copy full snippet
```

Or

```
	UnrealEditor-Cmd.exe <GameName> -run=cook -targetplatform=<Plat1>+<Plat2> [-cookonthefly] [-map=<Map1>+<Map2>] 
Copy full snippet
```

The commandlet must be specified via `-run=cook` and a platform to cook must also be specified. This will generate cooked data for the platform specified and saved it to the location below:

```
	<Game>/Saved/Sandboxes/Cooked-<Platform>
Copy full snippet
```

## Options

| Option | Description |
| --- | --- |
| `-targetplatform=<Plat1>+<Plat2>` | Specifies the platform(s) to be cooked. The list of available platforms are WindowsNoEditor, WindowsServer, LinuxServer, IOS, and Android. |
| `-iterate` | Specifies the cooker only cook items that are out of date. Without this option, the sandbox directory is deleted and everything is recooked. |
| `-Map=<Map1>+<Map2>+...` | Specifies the map(s) to build. |
| `-cookonthefly` | Specifies that the cooker be started in server mode. This will launch a server which waits for a game to connect and then serves the cooked data as needed. When this option is used, the game requires `-filehostip=<Server IP>` specified on its command line so it can connect with the server. |
| `-MapIniSection=<ini file section>` | Specifies a section from the ini files which contains map names. The cooker will cook all maps specified in the section specified. |
| `-UnVersioned` | Saves all of the cooked packages without versions. These are then assumed to be the current version on load. |
| `-cookall` | Cooks everything. |
| `-Compressed` | Tells the cooker to compress the cooked packages. |
| `-MAPSONLY` | Cooks only maps. |
| `-NODEV` | Excludes dev content. |
| `-NoGameAlwaysCook` | Don't include packages specified by the game in the cook. This cook will probably be missing content unless you are certain of what you are doing. |
| `-NoDefaultMaps` | Don't include default maps. This cook will probably be missing content unless you are certain of what you are doing. |
| `-CookSkipRequests` | Don't include packages loaded by engine startup. This cook will probably be missing content unless you are certain of what you are doing. |
| `-SkipSoftReferences` | Don't follow soft references when cooking. Usually not viable for a real cook and the results probably won't load correctly, but can be useful for debugging. |
| `-SkipHardReferences` | Don't follow hard references when cooking. Not viable for a real cook, only useful for debugging. |
| `-CookAgainstFixedBase` | If cooking DLC, assume the base content can't be modified. |
| `-DlcLoadMainAssetRegistry` | If cooking DLC, populate the main game asset registry. |
| `-DlcReevaluateUncookedAssets` | If cooking DLC, ignore uncooked assets in the base asset registry that are not cooked, so that this cook has an opportunity to cook the assets. |
| `-RunAssetValidation` | Run asset validation (`EditorValidatorSubsystem`) on assets loaded during cook. |
| `-RunMapValidation` | Run map validation (`MapCheck`) on maps loaded during cook. |
| `-ValidationErrorsAreFatal` | Consider validation errors (from `EditorValidatorSubsystem` or `MapCheck`) as fatal, preventing the package from being cooked. |
| `-EDITOROPTIONAL` | Produce editor optional package output when cooking. |
| `-MANIFESTS` | Generate manifests for building streaming install packages. |
| `-SKIPEDITORCONTENT` | Do not save out any packages in Engine/Content/Editor. |
| `-ERRORONENGINECONTENTUSE` | Generates an error if the cook accesses engine content (useful for DLC). |
| `-cooksinglepackagenorefs` | Only cook packages specified on commandline options (for debugging). |
| `-cooksinglepackage` | A modification to `bCookSinglePackage` - cook transitive hard references in addition to the packages on the commandline. |
| `-verbosecookerwarnings` | Output additional verbose cooking warnings. |
| `-Partialgc` | Only clean up objects which are not in use by the cooker during gc (false will enable full gc). |
| `-IgnoreIniSettingsOutOfDate` | Ignore ini settings out of date. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Cooking Content from the Command Line](/documentation/en-us/unreal-engine/cooking-content-in-unreal-engine?application_version=5.7#cookingcontentfromthecommandline)
* [Options](/documentation/en-us/unreal-engine/cooking-content-in-unreal-engine?application_version=5.7#options)
