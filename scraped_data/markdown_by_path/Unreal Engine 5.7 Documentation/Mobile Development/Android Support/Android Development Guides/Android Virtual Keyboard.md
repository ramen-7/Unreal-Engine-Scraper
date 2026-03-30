<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-android-virtual-keyboard-in-unreal-engine-projects?application_version=5.7 -->

# Android Virtual Keyboard

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
6. [Android Support](/documentation/en-us/unreal-engine/android-support-for-unreal-engine "Android Support")
7. [Android Development Guides](/documentation/en-us/unreal-engine/developing-guides-for-android-in-unreal-engine "Android Development Guides")
8. Android Virtual Keyboard

# Android Virtual Keyboard

Going over setting up the Android Virtual Keyboard.

![Android Virtual Keyboard](https://dev.epicgames.com/community/api/documentation/image/251ea07a-2d4c-44c8-b542-0388e7adf3a3?resizing_type=fill&width=1920&height=335)

 On this page

All **Unreal Engine** (UE) Android-based projects offer support for using either the standard pop up dialog input box or the operating system's virtual keyboard. The following document shows how to set up and call either virtual keyboard in your UE projects.

![New Keyboard Input](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8ded930-32ad-416a-b1e9-2ebf5aa9cab3/virtual-keyboard-new.png)

![Old Keyboard Input](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f5efb85-f44b-4f8f-b2fe-3ec7e3b61781/virtual-keyboard-old.png)

New Keyboard Input

Old Keyboard Input

## Steps

To enable the Virtual Keyboard in your project, you will need to do the following:

1. From the **Main Menu** go to **Edit** and then click on the **Project Settings** option.

   ![Open Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31a8ac02-d89f-4079-9290-e9a1438c5175/ue5_1-01-open-project-settings.png "Open Project Settings")
2. In the **Project Settings** menu go to **Platforms > Android** and under the **APK Packaging** section look for and click on the check mark box next to the **Enable improved virtual keyboard** option to enable it.

   [![Enable improved virtual keyboard](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a1ed389-3c5b-4a85-8ecb-b09edb329cd1/ue5_1-02-enable-improved-vk.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a1ed389-3c5b-4a85-8ecb-b09edb329cd1/ue5_1-02-enable-improved-vk.png)

   Click for full image.
3. Right-click in the **Content Browser** and then go to **User Interface > Widget Blueprint** option, giving this new Blueprint a name of **InputText**.

   [![Create Widget Blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0939d2f-1cd3-4c2c-ae45-ca5e764f240b/ue5_1-03-create-widget-blueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0939d2f-1cd3-4c2c-ae45-ca5e764f240b/ue5_1-03-create-widget-blueprint.png)

   Click for full image.
4. Double - click on the **Input Text** UMG widget to open it up and from the **Palette** drag a **TextBox** into the UMG graph.

   [![Drag Text Box Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/853c1ed4-ad6b-4dc5-add9-9c334e1c0082/ue5_1-04-drag-text-box-widget.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/853c1ed4-ad6b-4dc5-add9-9c334e1c0082/ue5_1-04-drag-text-box-widget.png)

   Click for full image.
5. Position the **TextBox** so that it is in the middle of the **Canvas** panel and then press the **Compile** and **Save** buttons.

   [![Set position Text Box widget and compile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9384501e-1391-42b4-a3f2-003bb1017046/ue5_1-05-set-position-compile.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9384501e-1391-42b4-a3f2-003bb1017046/ue5_1-05-set-position-compile.png)

   Click for full image.

   Keep in mind that your application is responsible for ensuring input elements are visible and not obscured behind the virtual keyboard. You can use the supplied **OnVirtualKeyboardShown** and **OnVirtualKeyboardHidden** event handlers to make sure that UI elements do not obscure the virtual keyboard.
6. Open up the **Level Blueprint** and add the following nodes to the **Event Graph**.

   * **Event Begin Play**
   * **Create Widget**
   * **Add to Viewport**

     [![Add nodes to the Event Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8d52305-420f-470e-8392-42455bddf4c1/ue5_1-06-bp-script-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8d52305-420f-470e-8392-42455bddf4c1/ue5_1-06-bp-script-1.png)

     Click for full image.
7. Connect the **Event Begin Play** node to the **Create Widget** node and then connect the **Create Widget** node to the **Add Viewport** node. When completed your **Level Blueprint** should look like the following image.

   [![Set Blueprint Script for Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/43d07a9c-a70b-4c7d-94c5-02e0adf98247/ue5_1-07-bp-script-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/43d07a9c-a70b-4c7d-94c5-02e0adf98247/ue5_1-07-bp-script-2.png)

   Click for full image.
8. Next, in the **Create Widget Blueprint** node, in the **Class** input, add the **InputText** Widget Blueprint that was created earlier.

   [![Set Blueprint Script for Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31d1e73b-8821-49b6-9bfd-c070f322b6dd/ue5_1-08-bp-script-3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31d1e73b-8821-49b6-9bfd-c070f322b6dd/ue5_1-08-bp-script-3.png)

   Click for full image.
9. Save the level, giving it a name of **AndroidVirtualKeyboard** then open up your **Project Settings** and go to **Maps & Modes**. In the **Default Maps** input the **AndroidVirtualKeyboard** map into the **Editor Startup Map** and the **Game Default Map**.

   [![Set Default Maps options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1524b35-73ed-420f-bd2b-3a0ebbe44b58/ue5_1-09-default-maps-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1524b35-73ed-420f-bd2b-3a0ebbe44b58/ue5_1-09-default-maps-options.png)

   Click for full image.
10. Click on the **Platforms** button small and from the displayed list, select the Android device you want to deploy your UE project to.

[![Deploy Project to the Device](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e9121de-e72a-4f9d-8c89-a3853f7d0388/ue5_1-10-deploy-project.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e9121de-e72a-4f9d-8c89-a3853f7d0388/ue5_1-10-deploy-project.png)

Click for full image.

## End Result

Once your project launches on your Android device, press on the text input box and when you do, you should now be able to input the text you want using the Android system keyboard like in the following video.

You can also disable the virtual keyboard using the **Android.NewKeyboard** console variable followed by one of the following numbers. Doing this is particularly useful when the user is using a language requiring a different IME (Input Method Editor).

| Command Name | Input | Description |
| --- | --- | --- |
| **Android.NewKeyboard** | 0 | Uses the check mark box setting that was set in the UE editor. |
| **Android.NewKeyboard** | 1 | Forces the new keyboard to be used. |
| **Android.NewKeyboard** | 2 | Forces the dialog to be used. |

* [development](https://dev.epicgames.com/community/search?query=development)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [guides](https://dev.epicgames.com/community/search?query=guides)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/setting-up-android-virtual-keyboard-in-unreal-engine-projects?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/setting-up-android-virtual-keyboard-in-unreal-engine-projects?application_version=5.7#endresult)
