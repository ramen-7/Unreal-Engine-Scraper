<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-multi-user-technical-reference-in-unreal-engine?application_version=5.7 -->

# nDisplay Multi-User Technical Reference

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
8. [nDisplay Quick Launch Local Tool](/documentation/en-us/unreal-engine/ndisplay-quick-launch-local-tool-in-unreal-engine "nDisplay Quick Launch Local Tool")
9. nDisplay Multi-User Technical Reference

# nDisplay Multi-User Technical Reference

A reference guide for the nDisplay multi-user editing session connection logic.

![nDisplay Multi-User Technical Reference](https://dev.epicgames.com/community/api/documentation/image/7527dd1f-8f7c-4384-887b-c290d0946194?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

When launching [multi-user editing sessions](/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) using [nDisplay](/documentation/en-us/unreal-engine/ndisplay-overview-for-unreal-engine), **Unreal Engine** automatically creates a local server to host multiple editor users simultaneously.

In the following document you can read about the multi-user server connection logic for launching virtual production projects using **nDisplay** in Unreal Engine.

## Multi-User Connection Logic

When launching a virtual production project using nDisplay for the first time, you can use the [Quick Launch tool](/documentation/en-us/unreal-engine/ndisplay-quick-launch-local-tool-in-unreal-engine) to automatically launch a local server multiple users can connect to.

When launching your project using nDisplay for a second time, Unreal Engine automatically reconnects to the existing local server and reuses the existing multi-user editing session if the editor is already operating in a session. If the editor is not operating in an nDisplay multi-user editing session, Unreal Engine creates a new multi-user editing session on the local server.

You can also build your own custom multi-user server to host an nDisplay multi-user editing session, that multiple users can connect to locally or using a network connection.

When attempting to join a network-based multi-user server, Unreal Engine checks if the editor is already in a multi-user editing session. If the editor is operating in an editing session, Unreal Engine joins the generated multi-user server and session. If the editor is not already operating within an nDisplay multi-user editing session, Unreal Engine closes the local multi-user server, ignores the network-based multi-user server, and launches a new server locally.

You can use the following diagram to better understand the Unreal Engine Multi-User (**MU**) connection behavior:

![flowchart showing a visual diagram of how unreal engine connects to servers and m u editing sessions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da777fd8-98ba-4683-983c-11bed3be2e66/flowchart.png)

For more information about getting started using multi-user editing sessions, refer to the [Multi-User](/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) documentation.

For more information about launching virtual projects using nDisplay, see the [nDisplay](/documentation/en-us/unreal-engine/ndisplay-overview-for-unreal-engine) documentation.

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [virtual camera](https://dev.epicgames.com/community/search?query=virtual%20camera)
* [multi-user](https://dev.epicgames.com/community/search?query=multi-user)
* [working with media](https://dev.epicgames.com/community/search?query=working%20with%20media)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Multi-User Connection Logic](/documentation/en-us/unreal-engine/ndisplay-multi-user-technical-reference-in-unreal-engine?application_version=5.7#multi-userconnectionlogic)

Related documents

[Multi-User Editing in Unreal Engine

![Multi-User Editing in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/2b6f163b-4521-4112-a24e-0ccfdcc6906e?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine)
