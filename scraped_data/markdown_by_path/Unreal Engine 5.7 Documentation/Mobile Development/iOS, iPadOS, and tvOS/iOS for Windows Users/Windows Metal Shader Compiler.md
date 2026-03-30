<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-windows-metal-shader-compiler-for-ios-in-unreal-engine?application_version=5.7 -->

# Windows Metal Shader Compiler

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
7. [iOS for Windows Users](/documentation/en-us/unreal-engine/working-on-ios-projects-using-a-windows-machine-in-unreal-engine "iOS for Windows Users")
8. Windows Metal Shader Compiler

# Windows Metal Shader Compiler

Use the Windows Metal Shader Compiler for iOS

![Windows Metal Shader Compiler](https://dev.epicgames.com/community/api/documentation/image/b42f2e68-4f8f-4618-ad60-0396cb2f7613?resizing_type=fill&width=1920&height=335)

 On this page

The Windows Metal shader compiler currently does not work in UE 5.1 through UE 5.4.

**Unreal Engine** can compile shaders for Apple's **Metal** API on a Windows machine, greatly simplifying the workflow for iOS applications. To enable this functionality, you need to install Apple's **Metal Developer Tools for Windows**. Unreal Engine will automatically use this toolset once it is set up.

## Steps

To install Metal Developer Tools for Windows, follow these steps:

1. Sign in to your **Apple Developer Account** in your web browser, then navigate to the **Downloads** section.
2. In the tabs on the upper-right of the Downloads page, click the **Release** tab.

   [![The Beta Downloads page](https://dev.epicgames.com/community/api/documentation/image/385c3bcb-ed64-4dee-ba13-9163e8448b78?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/385c3bcb-ed64-4dee-ba13-9163e8448b78?resizing_type=fit)
3. In the Software Downloads page, click the **Applications** button.

   [![The Applications button](https://dev.epicgames.com/community/api/documentation/image/30d12aaf-0ed3-4dbf-ad67-654685b31077?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30d12aaf-0ed3-4dbf-ad67-654685b31077?resizing_type=fit)
4. Scroll down the page until you find the entry for **Metal Developer Tools for Windows**, then click the **Download** button to download the installer.

   [![The entry for Metal Developer Tools for Windows](https://dev.epicgames.com/community/api/documentation/image/2fab47ec-dd4e-45f7-bd3d-096dc23b5124?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2fab47ec-dd4e-45f7-bd3d-096dc23b5124?resizing_type=fit)

   The download entry for the Metal Developer Tools for Windows. Click to enlarge image.

   Different versions of UE require different versions of the Metal Developer Tools.

   * UE 5.5: As shown.
   * UE 5.6: Use version 4.4
   * UE 5.7: Use version 5.3
5. Run the installer to install the Metal Developer Tools.

## Final Result

Once you have completed setup for the Metal Developer Tools for Windows, your Windows installation of Unreal Engine will be able to compile shaders for Metal 2.0. No additional setup is required.

* [shaders](https://dev.epicgames.com/community/search?query=shaders)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [tvos](https://dev.epicgames.com/community/search?query=tvos)
* [ipados](https://dev.epicgames.com/community/search?query=ipados)
* [metal](https://dev.epicgames.com/community/search?query=metal)
* [shader compiler](https://dev.epicgames.com/community/search?query=shader%20compiler)
* [metal shader compiler](https://dev.epicgames.com/community/search?query=metal%20shader%20compiler)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-the-windows-metal-shader-compiler-for-ios-in-unreal-engine?application_version=5.7#steps)
* [Final Result](/documentation/en-us/unreal-engine/using-the-windows-metal-shader-compiler-for-ios-in-unreal-engine?application_version=5.7#final-result)
