<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7 -->

# Hosting and Networking Guide

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
8. Hosting and Networking Guide

# Hosting and Networking Guide

Advanced networking configuration and other considerations for hosting the Pixel Streaming system.

![Hosting and Networking Guide](https://dev.epicgames.com/community/api/documentation/image/1720d9cb-8dd1-44b3-820e-e908cab6040a?resizing_type=fill&width=1920&height=335)

 On this page

Even without prior experience developing or deploying web services, you should be able to get the Pixel Streaming setup described in the [Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-pixel-streaming-in-unreal-engine) and [Quickstart Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-pixel-streaming-in-unreal-engine) pages to work within a simple local area network. However, if you try to deploy your service over more complex networks or over the open Internet, or if you want to redesign the user experience and connection flow, you might need to rethink your setup.

The signalling server, web server, and matchmaker server that accompany Pixel Streaming are a reference implementation only. We do not view them as being a complete solution for all cases, rather, we encourage you to modify them for your own purposes. To this end, we provide the signalling server and web server in the newly made [Pixel Streaming Infrastructure (external website)](https://github.com/EpicGamesExt/PixelStreamingInfrastructure/) so they can be freely distributed as per the Unreal Engine [EULA](https://www.unrealengine.com/en-US/eula/publishing) (see Distribution and sublicensing of Examples).

For more information regarding the Pixel Streaming front end and web servers, please refer to the [Pixel Streaming Infrastructure](https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-infrastructure) page.

## STUN and TURN Servers

In order for the Signaling and Web Server to be able to negotiate a direct connection between the Unreal Engine application and the browser, each party needs to send the other its own IP address. The browser needs to be able to access the IP address sent by the UE5 application, and vice-versa.

Within a simple local area network, each endpoint can usually assume that the other party can access it using the private IP address known to its own network card. Over the open Internet, across subnets, or when network address translation (NAT) services intervene between the browser and the UE5 application, this is not usually the case. Instead, each party needs to find out its own publicly visible IP address by querying a server that implements the STUN (Session Traversal Utilities for NAT) protocol. After the STUN server tells each endpoint its publicly visible IP address, the Signaling and Web Server can continue brokering their direct connection.

[![Pixel Streaming with STUN and TURN servers](https://dev.epicgames.com/community/api/documentation/image/4750a345-3b66-49c7-9eaa-109340b3f70d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4750a345-3b66-49c7-9eaa-109340b3f70d?resizing_type=fit)

Alternatively, you can use a TURN server to relay the media stream between the UE5 application and the browser. With the TURN protocol, the TURN server connects to both the UE5 application and to the browser. The UE5 application sends all of its streamed data to the TURN server, which forwards the data on to the browser. In this case, there is no direct connection between the UE5 application and the browser. If you need to support mobile devices over wireless carrier networks or clients on secured enterprise networks, you may have no choice but to use a TURN server. Mobile and enterprise networks often prevent clients from successfully connecting using the WebRTC protocol.

The STUN and TURN protocols together, along with the ability to fall back from one server to another, make up the ICE (Interactive Connectivity Establishment) framework.

You can find several [open-source implementations](https://github.com/coturn/coturn) of STUN and TURN servers on the Internet. There are even [public STUN servers](https://gist.github.com/mondain/b0ec1cf5f60ae726202e) that you can use for free instead of hosting your own, although you should exercise caution when using a service that you are not hosting yourself. Because of the throughput and bandwidth involved in relaying media through the TURN protocol, public TURN services are rarely available for free.

For convenience, the `SignallingWebServer/platform_scripts/` folder contains scripts to run **CoTURN** on Windows, Linux, and Mac. CoTURN is a free and open source STUN / TURN server that is production ready. We have removed the STUN and TURN reference servers we shipped in the past as these were not production-grade.

To set up Pixel Streaming to use ICE connections, you need to set the host names of the STUN and TURN servers you want to use in the **peerConnectionOptions** configuration parameter for the Signaling and Web Server. For details on how to format this parameter, and how to supply it, see the [Pixel Streaming Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-pixel-streaming-reference).

In addition, if you're hosting your own STUN or TURN server, you must make sure that the IP address and port you specify for it in the **peerConnectionOptions** parameter are visible on the open Internet.

## Multiple Player Endpoints

You may want all users to be in the same Unreal Engine session, but not have exactly the same ability to control that session.

For example, you might want to create an experience like a presentation, where the presenter has full control over the Unreal Engine from their browser, but other users are only able to view the stream. Or, you may want to create customized sets of controls for different users, so that they can cooperate to control different aspects of the experience in real time.

For these kinds of scenarios, you can have one Unreal Engine instance running with one stack of web services, but create different player HTML pages on the Signaling and Web Server:

[![Multiple player pages](https://dev.epicgames.com/community/api/documentation/image/df8e3ca9-82a2-4bef-bcaf-b968cb931b13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df8e3ca9-82a2-4bef-bcaf-b968cb931b13?resizing_type=fit)

In this scenario, you could customize each different HTML player page and its JavaScript environment to expose only the controls you want. Then, each class of users would need to request a different URL from the Signaling and Web Server. For example, maybe the presenter loads `http://yourhostname/presenter.html` and other users load `http://yourhostname/attendee.html`.

For more details on how to customize the player page, see [Customizing the Player Web Page](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-pixel-streaming-reference).

## Scaling on Demand

For a production Pixel Streaming deployment, we recommend a dynamic scaling solution. While running a fixed number of Unreal Engine applications may be viable for small-scale deployments, a more dynamic approach is necessary for larger or on-demand scaling. Without it, you risk either wasting resources on idle servers or forcing users to wait for a free connection. Ideally, your scaling solution should provision a new Unreal Engine instance instantly whenever a user connects.

In the past we provided a simple matchmaking server for use with the Pixel Streaming infrastructure that would match unused Unreal Engine instances with users wanting a Pixel Streaming experience. However, this matchmaking was not a dynamic scaling solution and was not a good foundation for building such a solution so we deprecated it in Unreal Engine 5.5. While a complete, ready-made scaling solution is outside the scope of what we provide, the Pixel Streaming repository contains all the essential components and libraries to build your own. We encourage you to extend these libraries with your own business logic to create a solution that is perfectly suited to your needs.

Alternatively, there are a number of cloud-based solutions and service providers who offer dynamic scaling solutions for Pixel Streaming. We recommend researching the market to find an option that aligns with the goals and business constraints of your project.

## What is the SFU?

A Selective Forwarding Unit (SFU) is a server which intelligently routes media streams between participants. In Pixel Streaming the role of the SFU is to receive stream data from the Unreal Engine application and deliver it to the recipient's peers (typically connected web browsers), optionally subsetting the data to adapt to the prevailing network conditions of each recipient peer.

When using the SFU Pixel Streaming, it implements the simulcast strategy for adapting stream bandwidth. In the simulcast strategy, the Unreal Instance generates multiple streams at different resolutions. The SFU then selects which quality variant of the stream to transmit to the recipient based on the recipient's network conditions.

At this time the SFU feature of Pixel Streaming is experimental.

[![SFUSetup](https://dev.epicgames.com/community/api/documentation/image/0c22fe96-b096-4753-9b77-9730ad809da2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c22fe96-b096-4753-9b77-9730ad809da2?resizing_type=fit)

## When to Use an SFU

An SFU enables a one-to-many stream where there can be more peers connected than would be typically available if all the peers were connected to the Pixel Streaming application in a peer-to-peer fashion. The use of an SFU is often appropriate when your Pixel Streaming application requires multiple connected recipients and those recipients are in varying network conditions that call for different quality stream quality levels (for example, lower bitrates, resolutions, or framerates).

## SFU Configuration

Configuration of the SFU can be achieved by modifying the `config.js` file found in `PixelStreamingInfrastructure/SFU/`.

The SFU is configured by default to provide three quality levels: one full, one half, and one quarter resolution streams. This configuration can be changed using `-PixelStreamingEncoderEnableSimulcast` (See the Pixel Streaming reference for details).

If you create more than eight simulcast streams you may hit up against limits when using the H.264 hardware encoders on consumer GPUs that often have a limit of eight encoding sessions. In Pixel Streaming 2, any streams beyond the 8th will automatically switch to software encoders. This is unique to Nvidia hardware.

## Host Machine Hardware Capabilities

If you choose to use a service provider such as Amazon (AWS) or Microsoft Azure to host your Unreal Engine application and Pixel Streaming web services, you may have a choice between multiple different tiers of hosts with different hardware capabilities. Keep in mind that the capabilities of the host may affect the quality of the stream that you can offer.

For example, if you opt for hosts with less powerful GPUs or less memory, you may not be able to get the maximum video quality possible in your streams.

* [guide](https://dev.epicgames.com/community/search?query=guide)
* [pixel streaming](https://dev.epicgames.com/community/search?query=pixel%20streaming)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [STUN and TURN Servers](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#stun-and-turn-servers)
* [Multiple Player Endpoints](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#multiple-player-endpoints)
* [Scaling on Demand](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#scaling-on-demand)
* [What is the SFU?](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#what-is-the-sfu)
* [When to Use an SFU](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#when-to-use-an-sfu)
* [SFU Configuration](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#sfu-configuration)
* [Host Machine Hardware Capabilities](/documentation/en-us/unreal-engine/hosting-and-networking-guide-for-pixel-streaming-in-unreal-engine?application_version=5.7#host-machine-hardware-capabilities)

Related documents

[Pixel Streaming Overview

![Pixel Streaming Overview](https://dev.epicgames.com/community/api/documentation/image/33434115-f4d2-44bd-8eed-00084dec6d15?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/overview-of-pixel-streaming-in-unreal-engine)

[Getting Started with Pixel Streaming in Unreal Engine

![Getting Started with Pixel Streaming in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/ddf40a17-c317-461e-9f5f-cf8ffc1c05a8?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/getting-started-with-pixel-streaming-in-unreal-engine)
