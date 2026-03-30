<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-sdk-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Android SDK

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
7. [Platforms](/documentation/en-us/unreal-engine/platforms-section-of-the-unreal-engine-project-settings "Platforms")
8. Android SDK

# Android SDK

Reference for the Android SDK section of the Unreal Engine Project Settings.

![Android SDK](https://dev.epicgames.com/community/api/documentation/image/47a7731e-549e-49f7-a320-d0597968525f?resizing_type=fill&width=1920&height=335)

 On this page

## Android SDK

### SDK Config

| **Setting** | **Description** |
| --- | --- |
| **Location of Android SDK** | The on-disk location of Android SDK (falls back to the `ANDROID_HOME` environment variable if this field is blank).  The directory usually contains `android-sdk-`. |
| **Location of Android NDK** | The on-disk location of Android NDK (falls back to the `NDKROOT` environment variable if this field is blank).  The directory usually contains `android-ndk-`. |
| **Location of JAVA** | The on-disk location of Java (falls back to the `JAVA_HOME` environment variable if this field is left blank).  The directory usually contains `jdk`. |
| **SDK API Level** | Define which SDK to package and compile Java with.  You can use:   * A specific version. * `latest` for latest version on disk. * `matchndk` to match the NDK API Level. |
| **NDK API Level** | Define which NDK to compile with (a specific version or `latest` for latest version on disk).  Choosing `android-21` or any later version will result in the app not running on pre-5.0 devices. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Android SDK](/documentation/en-us/unreal-engine/android-sdk-settings-in-the-unreal-engine-project-settings?application_version=5.7#androidsdk)
* [SDK Config](/documentation/en-us/unreal-engine/android-sdk-settings-in-the-unreal-engine-project-settings?application_version=5.7#sdkconfig)
