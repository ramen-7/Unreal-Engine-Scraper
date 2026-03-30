<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7 -->

# Experimental Pixel Streaming Features

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
8. Experimental Pixel Streaming Features

# Experimental Pixel Streaming Features

New and exciting features in Pixel Streaming that are still in development, but ready for play!

![Experimental Pixel Streaming Features](https://dev.epicgames.com/community/api/documentation/image/dbca2678-6a92-4ab7-b4c3-df4e92f21e8d?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

The below features are exciting new tools we've implemented into Pixel Streaming. Though they provide new possibilities, it's important to note that these are unstable and should be used with caution.
We recommend you do not build critical components of your product on them as they may change or be removed in subsequent releases of Unreal Engine.

## VCam

VCam is a new feature that allows you to use the new VCam actor to stream the video content of the Level Viewport to an output provider.

At this stage, VCam is mostly intended for virtual production use cases. It can be paired with the Live Link VCam iOS application and used for ARKit tracking. This is useful for piloting virtual cameras in Unreal Engine, with Pixel Streaming handling touch events and streaming the Level Viewport as real-time video feedback to the iOS device. For more information on Live Link VCam, please head to this site here: [iOS Live Link VCam](https://apps.apple.com/us/app/live-link-vcam/id1547309663)

### How to use VCam

1. Ensure you have the Virtual Camera plugin enabled.

   [![](https://dev.epicgames.com/community/api/documentation/image/be995dc9-c964-462f-af93-76b7b9d85919?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be995dc9-c964-462f-af93-76b7b9d85919?resizing_type=fit)
2. Add the VCam actor, found under Virtual Production.

   [![](https://dev.epicgames.com/community/api/documentation/image/fcf3e385-31c1-42d1-8bcd-2ffbbea005db?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fcf3e385-31c1-42d1-8bcd-2ffbbea005db?resizing_type=fit)
3. As soon as you add the actor, you'll be presented with the view of the VCam as shown below:

   [![](https://dev.epicgames.com/community/api/documentation/image/6e51b8a5-429f-45e6-9a70-41a3f17ff729?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e51b8a5-429f-45e6-9a70-41a3f17ff729?resizing_type=fit)
4. As soon as the actor is added, it will start streaming. You can start and stop this via the Pixel Streaming Toolbar.

   [![](https://dev.epicgames.com/community/api/documentation/image/caecdaf2-0ce5-4ea8-91ff-238bcb46a58d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/caecdaf2-0ce5-4ea8-91ff-238bcb46a58d?resizing_type=fit)
5. Once started, open a local browser and navigate to 127.0.0.1 to see your streamed display, or open the Live Link iOS application and navigate to your computer's IP address and press connect.

   [![](https://dev.epicgames.com/community/api/documentation/image/75e85f07-03f3-452a-8fee-08776354923b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75e85f07-03f3-452a-8fee-08776354923b?resizing_type=fit)

If you want to interact with the stream through the browser, open the control panel in-browser and change the Control Scheme to Hovering.

## Use Microphone

With Pixel Streaming, you can now allow in-engine playback of a particular peer / player microphone using WebRTC audio through the web browser.

### Setting up Use Microphone in Project

Making your project microphone compatible is simple and only requires a single addition to your project.

1. Enable the Pixel Streaming Plugin.
2. On any Actor in scene, add the `PixelStreamingAudio` component. You can leave its settings as the default.

   [![](https://dev.epicgames.com/community/api/documentation/image/d99bc5e0-b864-4fde-8b51-6025026a236e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d99bc5e0-b864-4fde-8b51-6025026a236e?resizing_type=fit)

Each audio component associates itself with a particular Pixel Streaming player/peer (using the the Pixel Streaming Player ID)

### Using Microphone in Stream

1. Once your project is set up with the `PixelStreamingAudio` component, run your application as per usual for Pixel Streaming (packaged or standalone with Pixel Streaming launch args) and launch your signalling server.
2. Connect to your signalling server via web browser.
3. Open the frontend settings panel and set `Use Mic` to `true`. Click **Restart** at the bottom to reconnect.

   [![](https://dev.epicgames.com/community/api/documentation/image/e3d9a0a8-b11e-423c-b079-9683c6faa955?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3d9a0a8-b11e-423c-b079-9683c6faa955?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/2fcd3bc1-3e40-484a-8300-069bcbffb984?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2fcd3bc1-3e40-484a-8300-069bcbffb984?resizing_type=fit)
4. Your browser may ask permission to use your microphone, ensure you allow access.

   [![](https://dev.epicgames.com/community/api/documentation/image/be908424-d59a-41aa-bc01-4407b92ea8da?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be908424-d59a-41aa-bc01-4407b92ea8da?resizing_type=fit)
5. Speak into your microphone, you should hear your voice played back through the stream!

For cloud streaming you’ll need HTTPS set up for this to work, see steps to create a HTTPS certificate in the VR guide below. Additionally, Firefox requires HTTPS for successful microphone capture in both local and cloud deployments.

## Pixel Streaming in Virtual Reality

Virtual Reality (VR) Pixel Streaming is a new feature that provides users with the means to connect to a VR-compatible application using Pixel Streaming. This allows users to enjoy a VR experience with their own headsets, without running a local application.

### Setting Up the Project

For this example, we'll use the Virtual Reality template project.

1. **Create** a new project using the Virtual Reality template.

   [![](https://dev.epicgames.com/community/api/documentation/image/e10ac845-a6a2-4c3e-ad14-84b58c671105?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e10ac845-a6a2-4c3e-ad14-84b58c671105?resizing_type=fit)
2. Enable the **Pixel Streaming 2** plugin and disable the **OpenXR** plugin. **Restart** the editor.

   [![Disable-OpenXR-plugin](https://dev.epicgames.com/community/api/documentation/image/505666dd-69ed-4d3d-bc25-a8f61ff78b41?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/505666dd-69ed-4d3d-bc25-a8f61ff78b41?resizing_type=fit)

   [![Enable-pixel-streaming-2-plugin](https://dev.epicgames.com/community/api/documentation/image/a9eb7b02-8ae6-4f8c-b461-60a7d91e0023?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9eb7b02-8ae6-4f8c-b461-60a7d91e0023?resizing_type=fit)
3. In the Content Browser, search for `Asset_Guideline` and delete `BP_AssetGuideline`. When prompted, click **Force Delete**.

   [![Asset-guideline-in-search-bar](https://dev.epicgames.com/community/api/documentation/image/93aa00c8-e8f8-4a49-94be-8f7fa2fabb68?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93aa00c8-e8f8-4a49-94be-8f7fa2fabb68?resizing_type=fit)

   [![BP-asset-guideline-in-search-bar](https://dev.epicgames.com/community/api/documentation/image/d15fe2e2-d87e-447b-b889-56d33d0305bd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d15fe2e2-d87e-447b-b889-56d33d0305bd?resizing_type=fit)
4. Now search for **VRPawn** in the Content Browser. Double-click the VRPawn to open it, then compile the Blueprint. If working properly it should compile successfully. **Save** and **close** this Blueprint.

   [![](https://dev.epicgames.com/community/api/documentation/image/e835c632-86e6-4a3b-a48e-0991e0ac303f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e835c632-86e6-4a3b-a48e-0991e0ac303f?resizing_type=fit)
5. Open **Editor Preferences > Level Editor > Play** and add `-PixelStreamingURL=ws://127.0.0.1:8888 -PixelStreamingEnableHMD -ResY=1080`.

   [![](https://dev.epicgames.com/community/api/documentation/image/a28fa414-3e31-4a23-bd2c-69435875185b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a28fa414-3e31-4a23-bd2c-69435875185b?resizing_type=fit)

If you’re using Pixel Streaming 2, you can also **EnableHMD** in the PixelStreaming2 plugin settings. Doing so will remove the need to run `-PixelStreamingEnableHMD`.

[![Enable-HMD-in-plugin](https://dev.epicgames.com/community/api/documentation/image/432f3bd7-2c5a-4f38-b184-e966b6c2b031?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/432f3bd7-2c5a-4f38-b184-e966b6c2b031?resizing_type=fit)

You only need to specify the vertical resolution, as the horizontal resolution automatically adjusts to suit the device's aspect ratio. Set the best resolution for your performance-to-quality ratio.

### Creating the Required Certificates

You need a HTTPS certificate to use VR with Pixel Streaming. This is due to the fact that the standard for WebXR requires that the API is only available to sites loaded over a secure connection (HTTPS). For production use, you will need to use a secure origin to support WebXR. You can find extra information on these requirements here: <https://developer.oculus.com/documentation/web/port-vr-xr/#https-is-required>.

For this example, we'll be setting up a basic certificate via Gitbash. If you don't have Gitbash installed prior, head to this page here for steps on how to install Gitbash: <https://www.atlassian.com/git/tutorials/git-bash>.

1. Create a `certificates` folder inside the `SignallingWebServer` directory, as shown below:

   [![](https://dev.epicgames.com/community/api/documentation/image/70c30adc-4f99-4fc3-b8e3-583e0c0f4ab9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70c30adc-4f99-4fc3-b8e3-583e0c0f4ab9?resizing_type=fit)
2. Right click inside the `certificates` directory and open Gitbash. Type in `openssl req -x509 -newkey rsa:4096 -keyout client-key.pem -out client-cert.pem -sha256 -nodes`.

   [![](https://dev.epicgames.com/community/api/documentation/image/75099afe-1f70-4ab7-9831-03ee1f7b03ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75099afe-1f70-4ab7-9831-03ee1f7b03ee?resizing_type=fit)
3. Press Enter multiple times, until the command is complete. You'll know it's done when done as it will have created 2 `.pem` files in the certificates folder.

   [![](https://dev.epicgames.com/community/api/documentation/image/c67a8d7a-f82e-4732-8072-a4c1a93328a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c67a8d7a-f82e-4732-8072-a4c1a93328a7?resizing_type=fit)
4. Open the `config.json` file found in the `SignallingWebServer` folder, set the `https` value to `true`. If the `config.json` file is missing, runt he signalling server once.

   [![](https://dev.epicgames.com/community/api/documentation/image/5e00edf2-9d48-44c0-a536-dec85d4f4907?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e00edf2-9d48-44c0-a536-dec85d4f4907?resizing_type=fit)

You should now be ready to run and test your VR application!

The certificate created above is only for testing purposes. For full cloud deployment, you will need to organize a proper certificate.

### Joining the VR Stream

For this example, we'll be using the Meta Quest 2.

1. Start the `start_with_stun.bat` script found in `\SignallingWebServer\platform_scripts\cmd`
2. Going back to the editor, run the application standalone. As you added the launch args in previous steps, it should connect to the signalling server once it's fully started up.
3. Now using your VR headset, open the web browser and enter your computer's IP address. You'll be presented with a "Connection not secure" page, open the "Advanced" tab and click "Proceed to IP"

   [![](https://dev.epicgames.com/community/api/documentation/image/8ba196c3-6afe-4dab-9955-88ba7796f322?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8ba196c3-6afe-4dab-9955-88ba7796f322?resizing_type=fit)
4. You should see the application streamed to two views in the browser window. Click the XR button on the left to switch to VR.

   [![](https://dev.epicgames.com/community/api/documentation/image/9b500174-436a-4de6-8cb4-c8a4ea37d8ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b500174-436a-4de6-8cb4-c8a4ea37d8ec?resizing_type=fit)
5. Done! You should now be in your Pixel Streamed VR project!

   [![](https://dev.epicgames.com/community/api/documentation/image/ec07cd81-81b2-4c61-9231-1967062a5492?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec07cd81-81b2-4c61-9231-1967062a5492?resizing_type=fit)

## Pixel Streaming Player

The Pixel Streaming Player allows you to display active Pixel Streams within your Unreal Engine project on a display within 3D space. With this, you can display cloud-hosted content as a media source within local applications.

The Pixel Streaming Player is an experimental feature with an API currently under development. As of 5.4, the Pixel Streaming Player is compatible with H264, VPX, and AV1 encoders.

Setting up the Pixel Streaming Player has changed in Pixel Streaming 2. For more information, please refer to [Pixel Streaming 2 Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-2-overview-in-unreal-engine).

### Setting up your Pixel Streaming Player

1. Enable the Pixel Streaming 2 plugin.
2. Create a new **Blueprint** class (Actor). Save and name this anything you like.
3. Open the new Blueprint class and add the **PixelStreaming2Peer**component.

   [![Pixel-streaming-2-peer-in-components](https://dev.epicgames.com/community/api/documentation/image/4a3fe62d-8ad9-4e71-9a81-54947c941d60?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a3fe62d-8ad9-4e71-9a81-54947c941d60?resizing_type=fit)
4. Drag the **PixelStreamingSignalling** component into the event graph. Drag off from this node and create a **Connect** node. Connect **BeginPlay** to the input of the new node and enter "ws://127.0.0.1:80" into the URL value. Adding the port to the URL field is importing, as the Pixel Streaming Player may not automatically connect to the right port. For Windows, the port is 80, but for Linux, use port 8080.

   [![](https://dev.epicgames.com/community/api/documentation/image/3b8a7030-85ca-49aa-a1e5-6afe21c77f8d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3b8a7030-85ca-49aa-a1e5-6afe21c77f8d?resizing_type=fit)
5. Select the PixelStreaming2Peer component and add the **OnStreamerList** event from the details panel.

   [![On-streamer-list-event-node](https://dev.epicgames.com/community/api/documentation/image/c30b013f-fe57-4527-9057-62308af6bc0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c30b013f-fe57-4527-9057-62308af6bc0a?resizing_type=fit)
6. From the new On Streamer List node; drag from the output and create a **Branch** node. From the true output, drag and create a **Subscribe** node. From the Streamer List array output, drag out and create a **Length** node. Do this again and create a **Get (a ref)** node. Plug your Get (a ref) node into your “Subscribe” nodes streamer **id input**. Lastly, create a **Greater (>)** node from your Length node, ensure the value is **0**, and plug this into your branch condition input. You can see the finished blueprint below:

   [![](https://dev.epicgames.com/community/api/documentation/image/01feddb0-ea39-4c1c-a9b1-a6ee8a14507d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01feddb0-ea39-4c1c-a9b1-a6ee8a14507d?resizing_type=fit)
7. Select the PixelStreaming2Peer component in the Components window on the left. In the Details window under Properties, you should see Pixel Streaming Video Consumer. Select the dropdown and choose Pixel Streaming Media Texture. Name and save it accordingly.

   [![Pixel-streaming-2-texture-component](https://dev.epicgames.com/community/api/documentation/image/0fc8facd-0c99-4f55-9591-ad8cc17f47f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0fc8facd-0c99-4f55-9591-ad8cc17f47f9?resizing_type=fit)
8. Drag your blueprint actor into the scene. Create a simple plane object and then resize and shape it into a suitable display.
9. Drag your saved Pixel Streaming media texture directly from the Content Browser onto the plane in the scene. This will automatically create a material and apply it to the object.

   [![Drag-material-to-the-plane](https://dev.epicgames.com/community/api/documentation/image/0efa7871-e7a1-47b9-bb21-c2f154a56ea7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0efa7871-e7a1-47b9-bb21-c2f154a56ea7?resizing_type=fit)
10. Play in editor. You should now see your PiE stream displayed on the plane. This will work with any active stream, such as an editor stream, an external packaged project or a remote stream. Simply update the connect node to suit the IP and port of the stream.

    [![Play-in-editor-stream](https://dev.epicgames.com/community/api/documentation/image/a155ee62-edad-4fe6-9d3e-5a7fe2fc6317?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a155ee62-edad-4fe6-9d3e-5a7fe2fc6317?resizing_type=fit)

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [guide](https://dev.epicgames.com/community/search?query=guide)
* [pixel streaming](https://dev.epicgames.com/community/search?query=pixel%20streaming)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [VCam](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#v-cam)
* [How to use VCam](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#how-to-use-v-cam)
* [Use Microphone](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#use-microphone)
* [Setting up Use Microphone in Project](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#setting-up-use-microphone-in-project)
* [Using Microphone in Stream](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#using-microphone-in-stream)
* [Pixel Streaming in Virtual Reality](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#pixel-streaming-in-virtual-reality)
* [Setting Up the Project](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#setting-up-the-project)
* [Creating the Required Certificates](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#creating-the-required-certificates)
* [Joining the VR Stream](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#joining-the-vr-stream)
* [Pixel Streaming Player](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#pixel-streaming-player)
* [Setting up your Pixel Streaming Player](/documentation/en-us/unreal-engine/experimental-pixel-streaming-features?application_version=5.7#setting-up-your-pixel-streaming-player)
