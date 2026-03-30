<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-requirements-for-the-collab-viewer-in-unreal-engine?application_version=5.7 -->

# Networking Requirements for the Collab Viewer

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
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Getting Started with XR Development](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine "Getting Started with XR Development")
8. [Collab Viewer Templates](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine "Collab Viewer Templates")
9. Networking Requirements for the Collab Viewer

# Networking Requirements for the Collab Viewer

Describes requirements and considerations that apply when you connect multiple computers together into a design review experience.

![Networking Requirements for the Collab Viewer](https://dev.epicgames.com/community/api/documentation/image/04908352-ecb4-4031-9fcd-c4e4fa7615d5?resizing_type=fill&width=1920&height=335)

 On this page

This page describes some of the network requirements and considerations involved in getting multiple computers to connect together into the same runtime design review session using the Collab Viewer Template.

## Connecting over a Local Area Network

The instructions in the [Quick Start](/documentation/en-us/unreal-engine/collab-viewer-template-quick-start-in-unreal-engine) page show how to connect multiple computers that are running within a simple local area network. You should have no problems connecting in this scenario as long as:

1. All computers are connected to the same network.
2. All computers have the standard Unreal Engine networking port **7777** open for communication within that network.
3. No intermediate network components, such as routers or network address traversal (NAT) services, are set up to block the connection.

If you have problems connecting, please contact your network administrator.

## Connecting Across Networks

If you need to have computers join a session across multiple sub-nets or over the open Internet, you will almost certainly need to do some extra network configuration. The exact steps you'll need to follow depend on your network configuration. However, in general:

* Your server host needs to be visible to all clients from a specific IP address. This may involve setting up NAT traversal rules on your router and opening your firewall to external communications on port 7777.
* Do not expect automatic server detection to work outside of the same network. Clients will need to manually specify the IP address of the server they want to connect to.

To avoid latency and lags, the Collab Viewer is best used locally within the same network.

## Bandwidth Requirements

Because the Collab Viewer Template only replicates lightweight data across the network, such as the 3D transforms of the users in the session and their laser pointers, network bandwidth usage should be relatively low. If you need exact measurements, you can profile how the template performs on your network using the [Network Profiler](/documentation/en-us/unreal-engine/using-the-network-profiler-in-unreal-engine).

## Other Resources

For additional information on how networking works in the Unreal Engine, see the documentation in the [Networking and Multiplayer](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine) section.

* [collaboration](https://dev.epicgames.com/community/search?query=collaboration)
* [templates](https://dev.epicgames.com/community/search?query=templates)
* [collab viewer](https://dev.epicgames.com/community/search?query=collab%20viewer)
* [design review](https://dev.epicgames.com/community/search?query=design%20review)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Connecting over a Local Area Network](/documentation/en-us/unreal-engine/networking-requirements-for-the-collab-viewer-in-unreal-engine?application_version=5.7#connectingoveralocalareanetwork)
* [Connecting Across Networks](/documentation/en-us/unreal-engine/networking-requirements-for-the-collab-viewer-in-unreal-engine?application_version=5.7#connectingacrossnetworks)
* [Bandwidth Requirements](/documentation/en-us/unreal-engine/networking-requirements-for-the-collab-viewer-in-unreal-engine?application_version=5.7#bandwidthrequirements)
* [Other Resources](/documentation/en-us/unreal-engine/networking-requirements-for-the-collab-viewer-in-unreal-engine?application_version=5.7#otherresources)
