<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine?application_version=5.7 -->

# Supporting Multiple Media Configurations

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
7. [Professional Video I/O](/documentation/en-us/unreal-engine/professional-video-io-in-unreal-engine "Professional Video I/O")
8. Supporting Multiple Media Configurations

# Supporting Multiple Media Configurations

The Media Profile gathers input, output, timecode and genlock settings into one place for easy configuration. Proxies help route input and output.

![Supporting Multiple Media Configurations](https://dev.epicgames.com/community/api/documentation/image/eaaca1b1-12d9-4230-845e-d2574ef8dc04?resizing_type=fill&width=1920&height=335)

 On this page

If you've followed the Quick Start guide for working with [AJA Media](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine) or [Blackmagic Design](/documentation/en-us/unreal-engine/blackmagic-video-io-quick-start-for-unreal-engine) hardware, you've seen one possible way to set up Media Input and Media Capture Assets to get SDI video feeds in and out of your Project.

However, you often need a single Project to work with multiple different media configurations. For example:

* You may need to work with the Project on different computers, each of which has different hardware or a different wiring setup. For example, one computer might have an AJA card while another has a Blackmagic card; or the video feed that is connected to port 1 on one computer might be wired to port 2 on the other computer.
* You may need to be able to switch your Project on one computer between different kinds of sources and outputs. For example, you may want to work with live feeds coming in over the SDI connections, but switch to using pre-recorded files on disk as inputs when the feed is offline.
* You may also need to change the way the Unreal Engine reads timecode and genlocks its frame rate, especially when you change to different sources or inputs. For example, you may want to lock the Unreal Engine's frame rate only when using input feeds coming in over SDI connections.

In cases like these, you don't want to have to make deep changes in your media setup and Project content every time you switch setups. Instead, you can set up multiple Media Profiles, each of which gathers together all configuration settings related to media inputs, outputs, timecode providers, and genlock providers. By simply switching to a different Media Profile, you can immediately change your entire media I/O setup.

## How Media Profiles and Proxies Work

Media Profiles rely on *proxy* Assets to make the connection between two different points:

* On one hand, the input and output configurations that you set up in the Media Profile.
* On the other hand, the places that those inputs and outputs are consumed or generated in your Project content.

[![Media Profile Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3136533a-e452-49d5-b046-6a26cbfa3139/01-profile-proxy-work_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3136533a-e452-49d5-b046-6a26cbfa3139/01-profile-proxy-work_ue5.png)

The following list illustrates the numbered sections in the image above:

1. You set up multiple Media Profiles in your Project: one for each usage scenario that your Project needs to support. Each profile contains a list of media sources and a list of media outputs. You set up these lists to determine where your Project will get video input from, and where it will send captures to.
   For example, you could set up one Profile to get inputs from an AJA Media card, another to get inputs from a Blackmagic Design card, and a third to get inputs from files on disk.
   You can also mix and match within a single Media Profile. For example, a single Media Profile could get inputs from both files and SDI feeds.
2. When you have the **Media Framework Utilities Plugin** installed, the **Project Settings** panel for your Project contains similar lists of inputs and outputs. Each numbered entry in the input list of the Media Profile matches up with the same number in the input list of the Project Settings, and the same goes for the output lists.
   You set up each of these list entries in the Project Settings to point to a Proxy Media Source or Proxy Media Asset that you create in your Project.
3. You then refer to these same Proxy Media Assets anytime you need to set up a Media Source or a Media Output in your Project content. For example:
   1. When you set up a Media Bundle or Media Player, you point it to one of those Media Proxy Assets instead of pointing it to a Media Source that directly represents a file, stream, or SDI input.
   2. Similarly, when you set up a Media Capture, you send the output to a Proxy Media Output instead of directly to an AJA or Blackmagic Media Output. You can do this in the **Media Capture** panel in the Unreal Editor as shown above, or when you invoke the **Create Media Capture** Blueprint node at runtime. If you've set up the output list in your Project Settings to contain a reference to the same Proxy Media Output, the capture is then forwarded on to the output with the matching index that you have configured in the Media Profile.

The Proxy Media Source and Proxy Media Output Assets don't contain any important configuration properties themselves. They only act as a channel — a way to connect the input and output configurations set in the Media Profile with the places that those inputs and outputs are actually used or generated by other Assets elsewhere in the Project.

## Selecting and Saving the Active Media Profile

Whenever your Project is loaded in the Unreal Engine or the Unreal Editor, it can have only one Media Profile active (or none at all).

When you have your Project open in the Unreal Editor, you select the active Media Profile using the Media Profile menu in the Toolbar of the main Level Editor:

![Selecting the active Media Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ef13624e-7386-4a0c-b7c3-9f88f4168e39/02-select-media-profile_ue5.png "Selecting the active Media Profile")

Media Profiles are Assets that are always saved in the Unreal Engine Project. However, the choice of which Media Profile is active is saved on each computer, not within the Project. That means that once you've set a Media Profile for a given Project on a given computer, you never have to change it again (unless your media hardware or configuration changes).

On the other hand, when you run a packaged version of your Project, the choice of which Media Profile is active is always determined by the **Startup Media Profile** setting, which you'll find in the **Project Settings** window under **Plugins > Media Profile**.

[![Startup Media Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3522dfe-e345-4ec1-953e-5ac36e7b2eae/03-startup-media-profile_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3522dfe-e345-4ec1-953e-5ac36e7b2eae/03-startup-media-profile_ue5.png)

Click image to expand.

## Getting Started with Media Profiles and Proxies

In this procedure, we'll set up two Media Profiles: one that plays input from local movie files, and one that plays live video feeds from an SDI card. We'll set up two separate Media Bundles to play the videos in the Level. Finally, we'll use Proxy Media Sources to redirect the inputs from the sources configured in the Media Profiles on to the Media Bundles.

**Prerequisites**:

* Media Profiles and Proxy Assets are provided by the **Media Framework Utilities** Plugin. You'll need to have this Plugin installed.
* You'll also need to have followed the Quick Start Guide for either [AJA Media](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine) or [Blackmagic Design](/documentation/en-us/unreal-engine/blackmagic-video-io-quick-start-for-unreal-engine) hardware.



To see a working example of a setup very similar to the one described below, see the [**Virtual Studio showcase**](/documentation/en-us/unreal-engine/virtual-studio-sample-project-in-unreal-engine), available in the **Samples** tab of the Epic Games Launcher.

1. Start by creating a Proxy Media Source Asset. Right-click in the **Content Browser** and select **Media > Proxy Media Source** from the context menu.

   [![Create a Proxy Media Source](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a12d3233-0391-4d17-9b10-a09170945fcb/04-create-proxy-media-source_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a12d3233-0391-4d17-9b10-a09170945fcb/04-create-proxy-media-source_ue5.png)

   Click image to expand.

   Name the new Asset **VideoProxyInA**.
2. Repeat the previous step to create another Proxy Media Source, but name it **VideoProxyInB**.
3. Create a new Media Bundle Asset. Right-click in the **Content Browser** and select **Media > Media Bundle**.

   [![Create a Media Bundle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51152ff4-a2d5-49d0-9e55-e496d73e501e/05-create-media-bundle_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51152ff4-a2d5-49d0-9e55-e496d73e501e/05-create-media-bundle_ue5.png)

   Click image to expand.

   Name the new Asset **MediaBundleA**.
4. Double-click the new Media Bundle Asset to edit it.
5. In the **Details** panel, find the **Media Source** setting and select **Proxy Media Source** from the drop-down list.

   [![Select Proxy Media Source](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f170b6e-f7c3-46c4-98a1-0f55511dc8ef/06-select-proxy-media-source_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f170b6e-f7c3-46c4-98a1-0f55511dc8ef/06-select-proxy-media-source_ue5.png)

   Click image to expand.
6. Expand the **Source** category, and set the **Proxy** to refer to the **VideoProxyInA** Asset that you created earlier.

   [![Set the Proxy Media Source Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93369a0f-db50-4fbe-bca9-6784226e1a61/07-details-proxy_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93369a0f-db50-4fbe-bca9-6784226e1a61/07-details-proxy_ue5.png)

   Click image to expand.
7. Repeat the previous steps to create another Media Bundle. This time, name it **MediaBundleB**, and set its source proxy to refer to **VideoProxyInB**.

   The Asset names recommended here, like VideoProxyInA and MediaProfileA, are intended to help make the relationships between the various Assets clear. However, in your own Project, we recommend using names that are more descriptive of the kind of content that the Media Proxy and Media Bundle need to handle. These Asset names are visible in your configurations, and in places like the **Media Capture** window, so ideally they should be meaningful to the whole team working on your Project.
8. From the main menu, select **Edit > Project Settings**. Find the **Plugins > Media Profile** section, and expand the advanced options.

   [![Media Profile settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59f10d9c-3154-487d-a9a8-b4bcc2b258bf/08-project-setting-media-source_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59f10d9c-3154-487d-a9a8-b4bcc2b258bf/08-project-setting-media-source_ue5.png)

   Click image to expand.
9. Add two entries to the **Media Source Proxy** list. Set one to refer to **VideoProxyInA**, and one to refer to **VideoProxyInB**.

   [![Add the Proxy Media Source Assets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11a2f9a9-a3ff-4ed6-ba1f-981e56fa946e/09-add-media-source-proxy_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11a2f9a9-a3ff-4ed6-ba1f-981e56fa946e/09-add-media-source-proxy_ue5.png)

   Click image to expand.
10. Now, we'll create a new Media Profile named **FileProfile** that plays videos from files on disk. You can do this in either of two ways:
    \* Right-click in the **Content Browser** and select **Media > Media Profile** from the context menu, then rename the Asset.

    [![Right-click to create the new Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b9abb19-c089-4cfe-9184-340af0a0bf99/10-create-new-media-profile_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b9abb19-c089-4cfe-9184-340af0a0bf99/10-create-new-media-profile_ue5.png)

    Click image to expand.

\* From the profile selection button in the Toolbar, select **New Empty Media Profile** and set the path and name for the new Asset.

![Create the new Asset from the Toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8886c783-1ef3-40c4-a900-2fc5b061cd4a/11-second-option-media-profile_ue5.png "Create the new Asset from the Toolbar")

1. Double-click the new Media Profile to edit it, if it doesn't open for editing automatically.

Find the **Media Sources** setting, and add two new elements to the list. Set each entry in the list to be a **File Media Source**, and set a different **File Path** for each.

[![File Media Source paths](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/984c49f8-13b9-41d5-b72d-53b462c6031a/12-select-media-sources_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/984c49f8-13b9-41d5-b72d-53b462c6031a/12-select-media-sources_ue5.png)

Click image to expand.

If you need some sample videos to test with, you can use these: [Video1](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/30d9065d-bc72-4736-921e-63f0e68ddffc/samplevideo.mp4) | [Video2](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/938d00eb-2f4b-488b-8b37-9f7c12718908/infiltrator_demo.mp4)

1. Repeat the previous steps to create a second Media Profile, named **LiveFeedProfile**, that brings video in from the AJA or Blackmagic device connected your computer. For example:

[![Media Profile for live feeds](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5dd720e-bab5-46c6-983c-966c9379f87c/13-black-magic-media-source_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5dd720e-bab5-46c6-983c-966c9379f87c/13-black-magic-media-source_ue5.png)

Click image to expand.

Each Media Profile also offers you the ability to set a Timecode Provider and a Genlock Provider:

![Timecode and Genlock settings in the Media Profile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/936c8a70-1ca8-4557-9697-f82dfd87498f/14-blackmagic-timecode-port_ue5.png "Timecode and Genlock settings in the Media Profile")

These have exactly the same effect as the **TimecodeProvider** and **Custom TimeStep** settings offered in the **Project Settings** panel. However, when you set these values in a Media Profile, they override the **Project Settings** only when that Media Profile is active. For more information, see [Timecode and Genlock](/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine).

1. Use the profile selection button in the Toolbar to select the **FileMediaProfile** that you created above.

![Activate the FileMediaProfile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05a56b7d-d356-4a49-b27c-36fd275da054/15-change-media-profile_ue5.png "Activate the FileMediaProfile")

1. Drag and drop your two Media Bundles into your Level Viewport. You should see them begin showing the videos loaded from the files or incoming over the SDI connections.

[![Drag and drop the Media Bundles](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44ceee91-ed4d-408b-9140-8edbb100b0b1/16-add-media-profile-viewport_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44ceee91-ed4d-408b-9140-8edbb100b0b1/16-add-media-profile-viewport_ue5.png)

Click image to expand.

1. Now you can use the Media Profile selection tool in the Toolbar to switch between your two Media Profiles easily, changing your Media Sources (and, optionally, your timecode and genlock settings) in one click.

![Switch Media Profiles](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad1063c9-be8e-438c-a214-4fdd7a7806da/17-live-feed-profile_ue5.png "Switch Media Profiles")

### Using Proxy Media Outputs

In this procedure, we'll extend the Media Profile setup we created in the previous section. We'll capture a video feed in the Unreal Editor (or the Unreal Engine at runtime), and route that feed through a Proxy Media Output to an output configuration that we define in the Media Profile. The overall process is very similar to setting up media sources: you create a Proxy Asset, update the Project Settings to refer to the Proxy, and configure the actual output device in the Media Profile.

1. Start by creating a Proxy Media Output Asset. Right-click in the **Content Browser** and select **Media > Proxy Media Output** from the context menu.

   [![Create a new Proxy Media Output](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cd55fc7-2958-4d4f-958b-ae96ca53186f/18-create-proxy-media-output_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cd55fc7-2958-4d4f-958b-ae96ca53186f/18-create-proxy-media-output_ue5.png)

   Click image to expand.

   Name the new Asset **VideoProxyOut**.
2. From the main menu, select **Edit > Project Settings**. Find the **Plugins > Media Profile** section, and expand the advanced options.

   ![Project Settings for Media Profiles](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3890d237-9398-45d7-aa1d-74497a31bc84/19-add-ouput-proxy_ue5.png "Project Settings for Media Profiles")
3. Add an entry to the **Media Output Proxy** list, and set its output proxy to point to **VideoProxyOut**.

   ![Set the Media Output Proxy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/770ad3a1-f7ea-4fba-9d9d-cdb037023675/20-video-proxy-out_ue5.png "Set the Media Output Proxy")
4. Double-click the **LiveFeedProfile** you created in the previous section, and add a new entry to the **Media Outputs** list. Set it up to send the video feed to a port on the AJA or Blackmagic device connected to your computer.

   [![New Entry](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c8db82d-4d63-4934-a1d2-12bf70ec915f/21-add-new-entry_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c8db82d-4d63-4934-a1d2-12bf70ec915f/21-add-new-entry_ue5.png)

   Click image to expand.
5. From the main menu, choose **Window > Media Capture**.
6. Add a new entry to the **Viewport Captures** list if needed, and set its **Media Output** setting to point to your **VideoProxyOut** Asset.

   ![Set the Proxy in the Media Capture22-new-entry-viewport-captures\_ue5.png "Set the Proxy in the Media Capture")
7. Click **Capture** to start capturing the feed and sending it through the proxy to your AJA or Blackmagic device.

   ![Start capturing from the Unreal Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/356238f2-af89-4aa0-a278-1916e3fcc1b0/23-capture-button_ue5.png "Start capturing from the Unreal Editor")

   If you switch the current Media Profile at this point to the **FileVideoProfile**, the capture stops, because the **FileVideoProfile** does not have an output configured for entry 0 in its **Media Outputs** list.
8. To capture the video feed at runtime and send it through the Proxy, you do it exactly as instructed in the Quick Start Guide for [AJA Media](/documentation/en-us/unreal-engine/aja-video-io-quick-start-for-unreal-engine) or [Blackmagic Design](/documentation/en-us/unreal-engine/blackmagic-video-io-quick-start-for-unreal-engine) hardware.
   The only difference is that instead of using a variable that is an Object Reference to an **AjaMediaOutput** or **BlackmagicMediaOutput**, you use an Object Reference to the **ProxyMediaOutput** that you want to send the captures to. You then use this **ProxyMediaOutput** variable as the input to the **Create Media Capture** node. For example:

   [![Create the Media Capture from the Proxy Media Output](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31e949da-76da-4515-8681-0bbc2cb4ba86/24-blueprint-setting_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31e949da-76da-4515-8681-0bbc2cb4ba86/24-blueprint-setting_ue5.png)

   Click image to expand.

### End Result

You now have two different Media Profiles set up, each with its own configuration of input and output feeds. Each uses Media Proxy Assets to map those input and output configurations to the other Media Framework Assets that consume or produce those video feeds. This example configuration might not match your exact usage scenario. However, having walked through the steps to set it up, you should have a good idea of how to extend the same basic functionality to meet your own needs.

* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [professional video](https://dev.epicgames.com/community/search?query=professional%20video)
* [guide](https://dev.epicgames.com/community/search?query=guide)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How Media Profiles and Proxies Work](/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine?application_version=5.7#howmediaprofilesandproxieswork)
* [Selecting and Saving the Active Media Profile](/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine?application_version=5.7#selectingandsavingtheactivemediaprofile)
* [Getting Started with Media Profiles and Proxies](/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine?application_version=5.7#gettingstartedwithmediaprofilesandproxies)
* [Using Proxy Media Outputs](/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine?application_version=5.7#usingproxymediaoutputs)
* [End Result](/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine?application_version=5.7#endresult)
