<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/adding-ndisplay-to-an-existing-project-in-unreal-engine?application_version=5.7 -->

# Adding nDisplay to an Existing Project

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. Adding nDisplay to an Existing Project

# Adding nDisplay to an Existing Project

Describes how to set up any existing Project to be ready for nDisplay.

![Adding nDisplay to an Existing Project](https://dev.epicgames.com/community/api/documentation/image/7e053fd5-7ff0-45f6-a31b-8572a1032bf3?resizing_type=fill&width=1920&height=335)

You don't have to use the nDisplay Template Project in order to render through nDisplay. If you already have a different Project set up with your content, you can adjust that Project so that it can take advantage of nDisplay.

To set up an existing Project to use nDisplay:

1. Enable the nDisplay plugin.  
   In the Unreal Editor, choose **Edit > Plugins** from the main menu. Search for "nDisplay", and check the **Enabled** checkbox.

   [![Enable the nDisplay Plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47ac9a22-abd8-4e68-8f67-64d2ad6db3a9/01-ndisplay-plugin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47ac9a22-abd8-4e68-8f67-64d2ad6db3a9/01-ndisplay-plugin.png)
2. Enable nDisplay for your Project.  
   Choose **Edit > Project Settings** from the main menu, and find the **Plugins > nDisplay** section. Check the **Enabled** checkbox.

   [![nDisplay Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ba0ce54-11b7-4ea6-87d7-3c42627393fb/02-ndisplay-enabled.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ba0ce54-11b7-4ea6-87d7-3c42627393fb/02-ndisplay-enabled.png)
3. Restart the Unreal Editor and reopen your Project.
4. Drag and drop the previously-generated config file (.cfg or .ndisplay) into your **Content Browser**. It will be automatically converted to a **UAsset**. Alternatively, add a new **nDisplay Config** UAsset, found in the **nDisplay** media category in the Content Browser
5. Continue on with the rest of the setup instructions in the [Quick Start Guide](/documentation/en-us/unreal-engine/ndisplay-quick-start-for-unreal-engine).

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [graphics](https://dev.epicgames.com/community/search?query=graphics)
* [guide](https://dev.epicgames.com/community/search?query=guide)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
