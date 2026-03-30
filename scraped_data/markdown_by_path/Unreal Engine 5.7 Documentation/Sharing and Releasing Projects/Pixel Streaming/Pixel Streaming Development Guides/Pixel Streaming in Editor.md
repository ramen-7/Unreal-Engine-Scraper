<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7 -->

# Pixel Streaming in Editor

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [Pixel Streaming](/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine "Pixel Streaming")
7. [Pixel Streaming Development Guides](/documentation/en-us/unreal-engine/development-guides-for-pixel-streaming-in-unreal-engine "Pixel Streaming Development Guides")
8. Pixel Streaming in Editor

# Pixel Streaming in Editor

Editor streaming is an experimental feature that leverages the power of Pixel Streaming to allow users to stream and interact with the Unreal Editor remotely. Additionally, there is now a new toolbar specifically for Pixel Streaming functions within the editor.

![Pixel Streaming in Editor](https://dev.epicgames.com/community/api/documentation/image/8f9e9998-3b39-497e-9ce4-65a67d50a7dc?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## Pixel Streaming Toolbar

The Pixel Streaming Toolbar is your primary means for controlling Pixel Streaming within the editor.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6c9c93b-eb2e-41c9-8527-8b1fe4eba9c4/pstoolbarexpandedfull.jpg)


To access the Pixel Streaming toolbar, make sure you have the Pixel Streaming plugin enabled.

#### Use Remote Signalling Server

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96882eb8-ff49-4dfc-8d91-1cb1d68ca798/remotesignalling.jpg)

Toggling this option stops the editor from creating an embedded signalling server when you use the Level and Full editor streaming options. You must manually launch a signalling server external to the editor and specify its URL. The default values should be sufficient in most use cases however.

#### Embedded Signalling Server Options

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7eafeeb5-ee60-417a-86c0-04db1598ff78/ssembedoptions.jpg)

These values specify the ports of the embedded signalling server created when you use the editor streaming functions. Unless you specifically need to change these, the default values should cover most use cases.

Due to Unreal Editor not running as sudo on Linux, it cannot create port bindings below 1000. As port 80 is the default viewer port for streaming, we've changed the default editor streaming viewer port to 8080 on Linux. You must specify this port in your browser URL when connecting to the stream.

This only applies to the embedded signaling server. An external signaling server will still use port 80, which does not need to be specified in the browser.

#### Virtual Camera

The virtual camera is a new experimental feature added to Pixel Streaming. For more detail on how to use this feature, please refer to the [Virtual Camera](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features) page.

#### Codecs

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52dbe792-230e-4b80-a992-5c63702bb755/codecs.jpg)

These options specify what encoder your stream will use. For more information about each codec as well as comparisons, please refer to the [Support Codecs](/documentation/en-us/unreal-engine/unreal-engine-pixel-streaming-reference#supportedencoders)  page.

## Editor Streaming

Editor streaming streams the Unreal Editor to web browsers, including browsers on mobile devices. This opens new potential for remote interaction with the editor as well as providing security benefits and enabling a new way for users to collaborate. Furthermore, eliminating the need to run the application on local hardware can open up new, efficient work pipelines.

Editor streaming leverages the base Pixel Streaming module, meaning users who are familiar with Pixel Streaming their applications will feel right at home with editor streaming.

### How do I use it?

Editor streaming is designed to be as easy to use as possible. To start editor streaming:

1. Make sure you have the Pixel Streaming plugin enabled.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f6ca97e-66fd-46dc-a529-37fabbfdd968/pspluginenabled.jpg)
2. Once the editor restarts, locate the new **Pixel Streaming** menu on your toolbar.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/175d4eaa-a5b8-4f8a-be50-a3133bb2975d/pstoolbarexpandedfull.jpg)
3. Open the Pixel Streaming menu and click **Stream Full Editor**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f8846bf-5b27-4c69-bf3e-babf7cbdf366/streamfulleditor.jpg)
4. Your editor is now being streamed. Open a browser and navigate to your public IP (127.0.0.1 works for testing a local stream).

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9ea5957-0714-4de6-ab28-5b3eb0e7d101/fullbrowserstream.jpg)
5. Open the toolbar again and you will see several IP addresses that you may be able to access your stream from, depending on your network configuration.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab79121d-9d16-48c2-b3ba-d0378c51793c/connectoptions.jpg)

The above steps will launch a signaling server that is embedded within Unreal Editor. If you prefer a workflow that uses the signaling server found in the **PixelStreamingInfrastructure** repo, check the **Use Remote Signaling Server** check box and enter the IP address of this signaling server before beginning streaming.

### How do I stream my editor in the cloud?

Streaming the editor from a cloud instance can be achieved in much the same manner as streaming your regular pixel streamed applications, albeit with a few minor modifications:

* If your application launch args contain: `-res=1920x1080` or similar, you'll want to replace this with `-EditorPixelStreamingRes=1920x1080`
* If your application launch args contain: `-resx=1920 -resy=1080` or similar, you'll want to replace this with `-EditorPixelStreamingResX=1920 -EditorPixelStreamingResY=1080`
* If your application launch args contain: `-renderoffscreen`, you'll want to add `-EditorPixelStreamingStartOnLaunch=true` to start streaming without needing to interact with the toolbar
* If you want to use a signaling server that isn't the server embedded within the engine, you'll want to add `-EditorPixelStreamingUseRemoteSignallingServer=true`
* An example of what your final command will look like is: `Engine\Binaries\Win64\UnrealEditor-Cmd.exe -project Path\To\Your\Project.uproject -RenderOffscreen -EditorPixelStreamingRes=1920x1080 -EditorPixelStreamingStartOnLaunch=true -PixelStreamingURL=ws://127.0.0.1:8888`

Editor streaming when rendering off screen is currently experimental and may be unstable.

### Stream Level Editor

Alongside full editor streaming, there is an option to exclusively stream the editor's level viewport. With only the level viewport streamed, connected peers will not see any surrounding elements, including but not limited to the outliner, content browser, and any and all pop-up menus.

To use level streaming, select **Stream Level Editor** from the toolbar option instead of **Stream Full Editor**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68f1d448-4afa-4f0e-8881-e9ea0e4a0dc3/streamleveleditor.jpg)

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [guide](https://dev.epicgames.com/community/search?query=guide)
* [pixel streaming](https://dev.epicgames.com/community/search?query=pixel%20streaming)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Pixel Streaming Toolbar](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#pixelstreamingtoolbar)
* [Use Remote Signalling Server](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#useremotesignallingserver)
* [Embedded Signalling Server Options](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#embeddedsignallingserveroptions)
* [Virtual Camera](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#virtualcamera)
* [Codecs](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#codecs)
* [Editor Streaming](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#editorstreaming)
* [How do I use it?](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#howdoiuseit?)
* [How do I stream my editor in the cloud?](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#howdoistreammyeditorinthecloud?)
* [Stream Level Editor](/documentation/en-us/unreal-engine/pixel-streaming-in-editor?application_version=5.7#streamleveleditor)
