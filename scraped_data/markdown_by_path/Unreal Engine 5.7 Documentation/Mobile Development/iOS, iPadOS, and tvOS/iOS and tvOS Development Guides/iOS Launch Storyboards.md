<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7 -->

# iOS Launch Storyboards

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
8. iOS Launch Storyboards

# iOS Launch Storyboards

Setting up launch screen storyboards in your Unreal Engine projects for iOS

![iOS Launch Storyboards](https://dev.epicgames.com/community/api/documentation/image/504387dc-5c8c-49dd-9520-625c13932c52?resizing_type=fill&width=1920&height=335)

 On this page

**Launch Storyboards** are launch screens for iOS applications. Unlike traditional launch screens, which are static images, storyboards support animation, and are capable of scaling to fit the resolution and DPI of the user's device. Developers can use this to create highly polished launch screens with relative ease that fit a wide range of devices. This how-to will walk you through implementing storyboards in your own **Unreal Engine (UE)** projects.

Storyboards are mandatory for all apps for both the App Store and Apple Arcade. Apple no longer accept submissions featuring static launch screens.

## Simple Launch Storyboards

It is recommended that you create a fully featured custom storyboard using the sections below. UE provides a method for creating simple, single-image storyboards for placeholder and testing purposes, ensuring that you always have a way of packaging a valid iOS project. This workflow can be used in any operating system, regardless of whether you are creating a C++ project or not.

To configure a simple storyboard, open **Project Settings** and navigate to the **Platforms** > **iOS** > **Launch Screen** section.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9979b1f9-b8e9-4ad6-81cd-0d68226ec878/launchscreenimage.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9979b1f9-b8e9-4ad6-81cd-0d68226ec878/launchscreenimage.png)

If you leave **Custom Launch Storyboard** unchecked, the image provided in **Launch Screen Image** will be converted into a storyboard when you build your project. An image with the Unreal Engine logo is provided by default as a fallback.

### Guidelines for Images

Launch screen images must be PNG files with no alpha channel. It is a good idea to make the dimensions square (for example, 2048x2048) so that they can scale and crop to the largest number of devices as easily as possible.

## Creating a Custom Launch Storyboard in Xcode

To create a custom storyboard, you will need a Mac with Xcode. You do not need to create a C++ project in Unreal to follow these steps, but you will need Xcode to generate the storyboard.

## Setting Up an Xcode Project

If you are creating a C++ project, you can create your launch screen directly in the Xcode project for your UE game. Alternatively, you can create your launch screen in any valid Xcode project outside of your UE project and move it into UE later. This is useful if you want to keep your storyboard project separate for organizational reasons, or if you are creating a Blueprint project.

Follow these steps to create a stand-alone Xcode project:

1. Open **Xcode** and click **File** > **New** > **Project**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b7f7a368-9b61-48f9-8873-1f70d4ec7a04/xcode_newproject.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b7f7a368-9b61-48f9-8873-1f70d4ec7a04/xcode_newproject.png)

   Click to enlarge image.
2. In the templates menu, make sure you are creating an **iOS** project, then click **Single View App**, then **Next**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7642979e-0f8f-4bf7-a5c3-b9136daea26e/xcode_newapp.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7642979e-0f8f-4bf7-a5c3-b9136daea26e/xcode_newapp.png)

   Click to enlarge image.
3. In the options menu, fill in your product name, organization name, and organization identifier. In this example, this results in a **Bundle Identifier** of *com.EpicGames.TestLaunchStoryboard*.
4. In the **User Interface** dropdown, click **Storyboard**. Once you have filled out all necessary information, click **Next**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e08e2796-6f50-45dd-a210-066d3186aff5/xcode_appoptions.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e08e2796-6f50-45dd-a210-066d3186aff5/xcode_appoptions.png)

   Click to enlarge image.
5. Place your new project in a folder that is convenient. In this example, it will be in `Users/UserName/Xcode Projects`.

You will not need to compile this project. You are only making this project for the sake of creating the storyboard, which we will manually move to our UE project.

## Creating the Launch Storyboard

Now that we have a project set up, follow these steps to create the storyboard that you will use for your launch screen:

1. In the **Project Navigator**, right-click your **Project**, click **New Group**, and create a new group called **Storyboard**.

   ![Storyboard Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77b300bc-a31f-4cef-b893-01886f6b9d85/storyboardgroup.png)
2. Click **File** > **New File...**

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/375c3c68-bae6-4342-b759-45916dbe5f19/newfile.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/375c3c68-bae6-4342-b759-45916dbe5f19/newfile.png)

   Click to enlarge image.
3. In the file template menu, navigate to the **User Interface** section, select **Launch Screen**, then click **Next**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/18a1924e-ac5c-42d9-8120-8f431e9e625e/xcode_launchscreen.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/18a1924e-ac5c-42d9-8120-8f431e9e625e/xcode_launchscreen.png)

   Click to enlarge image.
4. Save the file when prompted. Place it in the **Storyboard** folder, making sure it is in the group of the same name, and change the name of the file to **LaunchScreen**, with no spaces.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1bccb5bc-db36-4233-9d95-f01cffebd1a9/setlaunchscreenname.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1bccb5bc-db36-4233-9d95-f01cffebd1a9/setlaunchscreenname.png)

   Click to enlarge image.
5. Click the **Create** button to finish creating the storyboard. A file called LaunchScreen.storyboard will appear in your **Storyboard Group**, with a simple text label and a copyright notice.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb2017fe-3a93-43fd-8208-df66e82a21d8/section1_result.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb2017fe-3a93-43fd-8208-df66e82a21d8/section1_result.png)

   Click to enlarge image.
6. Select the **View Controller**. In the Identity Inspector, set the **Storyboard ID** to "LaunchScreen." Under the **Restoration ID** section, check the **Use Storyboard ID** checkbox.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce7e284b-5754-4599-ab1b-d5c697ba5876/setstoryboardid.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce7e284b-5754-4599-ab1b-d5c697ba5876/setstoryboardid.png)

   Click to enlarge image.

Setting the Storyboard and Restoration IDs for the View Controller is necessary for the storyboard to be recognized on startup. If you skip this step, the application will hang on a black screen before displaying the storyboard.

## Adding an Image to the Launch Storyboard

The storyboard created in the previous section is functional enough that it could be used in your project as is. In this section, we will add an image to the storyboard so that you know how to integrate outside assets into your Xcode project.

1. Create an image to serve as the background for the storyboard. This image should be a PNG with no transparency.
2. In the **Project Navigator**, right-click the **Storyboard** group, click **New Group**, and call your new group **Assets**.
3. In **Finder**, make sure there is an **Assets** folder inside the **Storyboard** folder, and place your PNG in the **Assets** folder.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d194e11-e565-4126-a05d-e699c17e8970/assetsfolder_storyboardimage.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d194e11-e565-4126-a05d-e699c17e8970/assetsfolder_storyboardimage.png)

   Click to enlarge image.
4. Drag your PNG into the **Assets** group in the **Project Navigator** to add it to the Xcode project.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d2af53b-89f9-4eeb-a758-53cae787e86d/assetfolder_withimage.png)
5. Click the **+** (plus) button at the top of the Xcode window to open the **library**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/daeb03e8-49f7-4f26-a951-155678888f63/clickplusbutton.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/daeb03e8-49f7-4f26-a951-155678888f63/clickplusbutton.png)

   Click to enlarge image.
6. In the **library**, locate the **Image View** object, then drag it into your **Storyboard**. It will replace the default **View** and all of the text populating it.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca612bf0-1df8-4607-adfd-aa906fcd75be/createnewimageview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca612bf0-1df8-4607-adfd-aa906fcd75be/createnewimageview.png)

   Click to enlarge image.
7. Select **Image View**, then in the **Attributes panel**, click the source **Image** dropdown and select your PNG. If the Attributes panel is not shown, click the icon that looks like a chevron with a line through it, next to the **Ruler** icon.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d0e38a2-a80f-41c3-aa01-3d8239d42e6a/selectimageforimageview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d0e38a2-a80f-41c3-aa01-3d8239d42e6a/selectimageforimageview.png)

   Click to enlarge image.
8. In the **Attributes panel**, set the **Content Mode** to **Aspect Fill**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b4e3405-9120-4590-83aa-c025fdd32742/aspectfill.png)
9. Select the **Size Inspector** by clicking the **Ruler** icon. Click all four **Constraints** in the **Autoresizing** section. This will ensure that the Image View resizes based on all four directions.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8dc801a-1a18-46c5-8ffe-a3303b3f1c7d/setautoresizing.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8dc801a-1a18-46c5-8ffe-a3303b3f1c7d/setautoresizing.png)

   Click to enlarge image.

As long as the image is located somewhere in your Xcode project, your Image View will be able to utilize it. However, we recommend keeping the image in an Assets folder for the purpose of adding it to your Unreal Engine project per the next section.

### Image Guidelines

We recommend using square images for launch storyboards for the sake of maximizing compatibility with a wide range of aspect ratios. However, if you are targeting a specific device or a specific aspect ratio, you can tailor your images to fit that aspect ratio safely.

## Adding the Custom Storyboard

To add your storyboard to the UE project:

1. Create a folder in your engine install directory called `Project/Build/IOS/Resources/Interface`.
2. Locate the **Storyboard** folder for your Xcode project in **Finder**.
3. Copy both **LaunchScreen.storyboard** and the accompanying **Assets** folder into `Project/Build/IOS/Resources/Interface`.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/025e7a70-1057-408b-84a1-7736b25a7412/movestoryboardtoproject.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/025e7a70-1057-408b-84a1-7736b25a7412/movestoryboardtoproject.png)

   Click to enlarge image.

   If you do not have the required files in the Project folder, the system will fall back to the Engine directory to look for them instead.
4. In the **Unreal Editor**, open **Project Settings** and navigate to **Platforms** > **iOS** > **Launch Screen**.
5. Enable the **Custom Launch Storyboard** checkbox.

   ![Enable Custom Storyboard](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/911bd856-49e6-4692-9bd9-1aceb4ee67b2/enablecustomstoryboard.png)

Now when you package your iOS project, instead of using the default launch storyboard, the project will use the custom storyboard you placed in the `IOS/Resources/Graphics` folder. While the Xcode project does not depend on a specific folder structure for referencing the image file, the UE project requires it to be located in an Assets folder alongside the LaunchScreen.storyboard file.

## Further Reading

After following this guide, you should have everything you need to implement a basic launch storyboard in your UE project. For additional information about configuring and editing storyboards for iOS, refer to Apple's documentation for [launch screens](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/launch-screen/) and [storyboards](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/DesigningwithStoryboards.html).

* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [storyboards](https://dev.epicgames.com/community/search?query=storyboards)
* [launch screen](https://dev.epicgames.com/community/search?query=launch%20screen)
* [setupsetup](https://dev.epicgames.com/community/search?query=setupsetup)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Simple Launch Storyboards](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#simplelaunchstoryboards)
* [Guidelines for Images](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#guidelinesforimages)
* [Creating a Custom Launch Storyboard in Xcode](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#creatingacustomlaunchstoryboardinxcode)
* [Setting Up an Xcode Project](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#settingupanxcodeproject)
* [Creating the Launch Storyboard](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#creatingthelaunchstoryboard)
* [Adding an Image to the Launch Storyboard](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#addinganimagetothelaunchstoryboard)
* [Image Guidelines](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#imageguidelines)
* [Adding the Custom Storyboard](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#addingthecustomstoryboard)
* [Further Reading](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects?application_version=5.7#furtherreading)
