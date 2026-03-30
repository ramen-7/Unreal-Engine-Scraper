<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/localizing-plist-and-nslocalizedstring-in-an-ios-project-in-unreal-engine?application_version=5.7 -->

# Localizing plist and NSLocalizedString

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [iOS, iPadOS, and tvOS](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine "iOS, iPadOS, and tvOS")
7. [iOS and tvOS Development Guides](/documentation/en-us/unreal-engine/developing-on-ios-tvos-and-ipados-in-unreal-engine "iOS and tvOS Development Guides")
8. Localizing plist and NSLocalizedString

# Localizing plist and NSLocalizedString

Identify strings in your project code that need to be translated.

![Localizing plist and NSLocalizedString](https://dev.epicgames.com/community/api/documentation/image/bfa7a4f6-db9d-401f-b1de-4b8f050fc5b9?resizing_type=fill&width=1920&height=335)

 On this page

Localization files can be added to Unreal Engine to identify and translate strings in an iOS projects code.

This document describes how to set up string translation through the creation of localization files and folders.

Developers are required to add localization files for at least one language prior to submitting their iOS project.

## Steps

1. Create a Localizations folder in the Unreal Engine project directory (if one does not already exist) under the following path: `{UEProjectDir}/Build/IOS/Resources/Localizations/`.
2. Navigate to the `Localizations` folder and create one folder per language. These folders must be named according to the following format: `{LanguageCode}.lproj`. For example, an English language localization folder should be named `EN.lproj`, where `EN` is the language code for English.

   Localization folders must be named using the language's two-character code as listed in the [ISO 639-2 standard](http://www.loc.gov/standards/iso639-2/php/code_list.php).
3. In each language folder create a text file named `InfoPlist.strings`. This file is used to translate strings listed in the `info.plist` file of your iOS project.
4. In each language folder create a text file named `Localizable.strings`. This file is used to translate strings from all the code files of your iOS project.

For example, for an application named "Lovely Game", your Objective-C code could contain the following lines:

```
	NSString* allRightText = NSLocalizedString(@"All right", @"All right");
	NSString* cancelText = NSLocalizedString(@"Cancel", @"Cancel");

Copy full snippet
```

The following table shows some examples of how you modify the `InfoPlist.strings` file and `Localizable.strings` file for various languages.

| Language | InfoPlist.strings File Code | Localizable.strings File Code |
| --- | --- | --- |
| English | `"CFBundleDisplayName" = "Lovely Game";` `"NSCameraUsageDescription" = "The camera is needed to take a picture";` | `/* All right */` `"All right" = "All right";`  `/* Cancel */` `"Cancel" = "Cancel";` |
| Chinese | `"CFBundleDisplayName" = "可爱的游戏";` `"NSCameraUsageDescription" = "需要摄像头用于拍照";` | `/* OK */`  `"OK" = "确定";` `/* Cancel */` `"Cancel" = "取消";` |
| French | `"CFBundleDisplayName" = "Beau Jeu";` `"NSCameraUsageDescription" = "L'appareil photo est nécessaire pour prendre une photo";` | `/* All right */` `"All right" = "D'accord";` `/* Cancel */` `"Cancel" = "Annuler";` |

## End Result

The newly-created Localizations folder will be copied any time Unreal Engine packages your iOS project.

Once packaged, your iOS project will have all of its strings translated and will be ready to submit to Apple.

* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/localizing-plist-and-nslocalizedstring-in-an-ios-project-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/localizing-plist-and-nslocalizedstring-in-an-ios-project-in-unreal-engine?application_version=5.7#endresult)
