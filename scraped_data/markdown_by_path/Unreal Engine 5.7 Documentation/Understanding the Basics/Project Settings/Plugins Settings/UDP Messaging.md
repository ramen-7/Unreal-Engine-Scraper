<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/udp-messaging-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# UDP Messaging

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine "Project Settings")
7. [Plugins Settings](/documentation/en-us/unreal-engine/plugins-section-of-the-unreal-engine-project-settings "Plugins Settings")
8. UDP Messaging

# UDP Messaging

Reference for the UDP Messaging section of the Unreal Engine Project Settings.

![UDP Messaging](https://dev.epicgames.com/community/api/documentation/image/cbbc66df-de72-4188-b827-9009f62104b7?resizing_type=fill&width=1920&height=335)

 On this page

## UDP Messaging

### Availability

| **Setting** | **Description** |
| --- | --- |
| **Enabled by Default** | Defines whether UDP messaging is enabled by default.  If disabled, messaging will need to be added to the command line when running non-editor builds.  In shipping builds, `ALLOW_UDP_MESSAGING_SHIPPING=1` must also be defined in TargetRules for messaging to be available with or without this setting. |

### Transport

| **Setting** | **Description** |
| --- | --- |
| **Enable Transport** | Defines whether the UDP transport channel should be enabled.  Can be specified on the command line with `-UDPMESSAGING_TRANSPORT_ENABLE=`. |
| **Unicast Endpoint** | The IP endpoint to listen to and send packets from.  The format is `IP_ADDRESS:PORT_NUMBER`.  `0.0.0:0` will bind to the default network adapter on Windows and all available network adapters on other operating systems.  Specifying an interface IP here will use that interface for multicasting. Static endpoints might also reach this client through `<unicast ip:multicast port>`.  Specifying both the IP and Port will allow usage of static endpoint to reach this client.  Can be specified on the command line with `-UDPMESSAGING_TRANSPORT_UNICAST=`. |
| **Multicast Endpoint** | The IP endpoint to send multicast packets to.  The format is `IP_ADDRESS:PORT_NUMBER`.  The multicast IP address must be in the range `224.0.0.0` to `239.255.255.255`.  Can be specified from the command line with `-UDPMESSAGING_TRANSPORT_MULTICAST=`. |
| **Message Format** | The format used to serialize the UDP message payload.  You can choose from the following options:   * **CBOR (Platform Endianness):** UDP messages are encoded in CBOR using the platform endianness. This is the fastest and preferred option, but the CBOR data will not be readable by an external standard-compliant CBOR parser if generated from a little-endian platform. If the data needs to be consumed outside Unreal Engine, consider using `CborStandardEndianness` format instead. * **CBOR (Standard Endianness):** UDP messages are encoded in CBOR, using the CBOR standard-complinant endianness (big-endian). This performs slower on a little-endian platform, but the data will be readable by standard CBOR parsers. Useful if the UDP messages need to be analyzed or consumed outside Unreal Engine. |
| **Advanced** |  |
| **Auto-Repair** | Defines whether the UDP transport channel should try to auto-repair when in error. |
| **Max Send Rate** | Maximum sustained transmission rate in Gbit/s.  The default value is 1 Gbit/s.  This is to control transmission of larger packages over the network. Without a limit, packet data loss can occur because more data may be sent than may be supported by your network card.  Adjust this value higher or lower depending on your network capacity. |
| **Auto-Repair Attempt Limit** | The number of consecutive attempts the auto-repair routine will try to repair. |
| **Multicast Time to Live** | The time-to-live (TTL) for sent multicast packets. |
| **Static Endpoints** | The IP endpoints of static devices.  Use this setting to reach devices on other subnets, such as mobile phones on a Wi-Fi network.  The format is `IP_ADDRESS:PORT_NUMBER`. |

### Tunnel

| **Setting** | **Description** |
| --- | --- |
| **Enable Tunnel** | Defines whether the UDP tunnel is enabled. |
| **Tunnel Unicast Endpoint** | The local IP endpoint to listen to and send packets from.  The format is `IP_ADDRESS:PORT_NUMBER`. |
| **Tunnel Multicast Endpoint** | The IP endpoint to send multicast packets to.  The format is `IP_ADDRESS:PORT_NUMBER`.  The multicast IP address must be in the range `224.0.0.0` to `239.255.255.255`. |
| **Advanced** |  |
| **Remote Tunnel Endpoints** | The IP endpoints of remote tunnel nodes.  Use this setting to connect to remote tunnel services.  The format is `IP_ADDRESS:PORT_NUMBER`. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [UDP Messaging](/documentation/en-us/unreal-engine/udp-messaging-settings-in-the-unreal-engine-project-settings?application_version=5.7#udpmessaging)
* [Availability](/documentation/en-us/unreal-engine/udp-messaging-settings-in-the-unreal-engine-project-settings?application_version=5.7#availability)
* [Transport](/documentation/en-us/unreal-engine/udp-messaging-settings-in-the-unreal-engine-project-settings?application_version=5.7#transport)
* [Tunnel](/documentation/en-us/unreal-engine/udp-messaging-settings-in-the-unreal-engine-project-settings?application_version=5.7#tunnel)
