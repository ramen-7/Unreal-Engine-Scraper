<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine?application_version=5.7 -->

# Packaging iOS Projects

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
7. [Packaging and Publishing for iOS, tvOS, and iPadOS](/documentation/en-us/unreal-engine/building-packaging-and-publishing-unreal-engine-projects-for-ios-tvos-and-ipados "Packaging and Publishing for iOS, tvOS, and iPadOS")
8. Packaging iOS Projects

# Packaging iOS Projects

Learn how to package iOS Projects in Unreal Engine

![Packaging iOS Projects](https://dev.epicgames.com/community/api/documentation/image/1916794f-4345-4e9e-b574-40c9c56bc87d?resizing_type=fill&width=1920&height=335)

 On this page

Choose your operating system

Windows
macOS
Linux


## Steps

In the following section, we will take a look at using the UE Editor to create an **.IPA** of your project, which can be installed later without the need for the Editor.

If you are localizing your iOS project, you will need to also translate strings in your code. See the [Localize 'plist' and 'NSLocalizedString' in an iOS Project](/documentation/en-us/unreal-engine/localizing-plist-and-nslocalizedstring-in-an-ios-project-in-unreal-engine) page for instructions on how to do this.

1. Connect your device to your computer if it is not already connected.
2. Open your project in Unreal Editor.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2fd865fe-f6e6-4c08-8620-c2b464c510d9/open_project.png)
3. In the **File** menu, select **Package Project > iOS**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/150c7b9a-e498-4355-acaa-0c4a3d097e6c/package_menu.png)
4. In the directory dialog, select a location for the `.ipa` file to be saved.
5. A packaging message will appear in the bottom right corner of the editor while the game is being packaged.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/091f2123-b950-4315-84f4-30090eb768c1/project_package.png)
6. A message is displayed when the project is successfully packaged.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32c9c4fb-8315-4280-9612-a7af618bf908/package_complete.png)



## End Result

When completed you will now have an .IPA that is ready to be deployed to your iOS device.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/663edc41-c600-4f24-a611-533ae87ccde6/app_install_xcode_6.png)



## Steps

In the following section, we will take a look at creating a **.IPA** of your project that can be installed without the need for **Unreal Editor**.

1. Connect your device to your computer if it is not already connected.
2. Open your project in Unreal Editor.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/434ff326-40f3-4d05-9b60-18bb1abafe0d/open_project.png)
3. In the **File** menu, select **Package Project > iOS**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/643c3985-ff74-4bfc-9b40-7fda262ca48c/package_menu.png)
4. In the directory dialog, select your project's directory as this is where the packaged project (`.ipa` file) will be located.
5. A packaging message will appear in the bottom right corner of the Editor while the game is being packaged.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/468ae203-c67d-478d-8877-65bc21207b21/project_package.png)
6. A message is displayed when the project is successfully packaged.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c2916ef-9293-40ae-87e7-8271e5c057b4/package_complete.png)
7. From Xcode go to **Window** and then select **Devices and Simulators**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0beeb500-3500-48c8-905d-710a05db9bc7/app_install_xcode_1.png)
8. In the **Devices** section, press the **Plus** sign icon to start the app install process.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56c1c161-7b9f-413d-ac4e-668f2a45b21a/app_install_xcode_2.png "app_Install_xCode_2.png")
9. Locate and select the **.ipa** file that UE4 created and then press the **Open** button to begin the install process.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdac607d-25fe-4625-a0fb-3f7243cc251c/app_install_xcode_3.png)
10. The progress of the install will be displayed across the top of the **Devices** window.



## End Result

When completed you will see the IPA added to your iOS device.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e6d76c6-57f7-407a-9e0b-1ea38dfddbb1/app_install_xcode_5.png)

* [guides](https://dev.epicgames.com/community/search?query=guides)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine?application_version=5.7#endresult)
* [Steps](/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine?application_version=5.7#steps-2)
* [End Result](/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine?application_version=5.7#endresult-2)
