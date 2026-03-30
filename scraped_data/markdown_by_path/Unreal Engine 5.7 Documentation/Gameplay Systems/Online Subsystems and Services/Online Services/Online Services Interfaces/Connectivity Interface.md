<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7 -->

# Connectivity Interface

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Online Subsystems and Services](/documentation/en-us/unreal-engine/online-subsystems-and-services-in-unreal-engine "Online Subsystems and Services")
7. [Online Services](/documentation/en-us/unreal-engine/online-services-in-unreal-engine "Online Services")
8. [Online Services Interfaces](/documentation/en-us/unreal-engine/online-services-interfaces-in-unreal-engine "Online Services Interfaces")
9. Connectivity Interface

# Connectivity Interface

Determine whether your game is connected to your platform's online services.

![Connectivity Interface](https://dev.epicgames.com/community/api/documentation/image/e999254a-873e-4673-aba4-7dc6c50f7366?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services** **Connectivity Interface** provides you with tools to determine whether your game is connected to your platform's backend online services.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the Connectivity Interface:

| Function | Description |
| --- | --- |
| [GetConnectionStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IConnectivity/GetConnectionStatus?application_version=5.5) | Retrieve the connection status for the provided online service. |
| [OnConnectionStatusChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IConnectivity/OnConnectionStat-?application_version=5.5) | The event triggered when an online service connection status changes. |

### Enumerated Classes

Online service connection status is represented by the [EOnlineServicesConnectionStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EOnl-?application_version=5.5) enumerated class.

#### EOnlineServicesConnectionStatus

| Value | Description |
| --- | --- |
| `Connected` | Connected to the online services. |
| `NotConnected` | Not connected to the online services. |

## Connection Status

`GetConnectionStatus` returns the current connection status for the provided online service. Some online services consist of multiple underlying microservices. Use the name of one of these microservices as a parameter for `GetConnectionStatus` to determine the particular microservice's connection status. If you don't specify an online service parameter, `GetConnectionStatus` returns `EOnlineServicesConnectionStatus::Connected` only if all underlying microservices are connected.

You can bind `OnConnectionStatusChanged` to events to inform you when the connection status of an online service or one of its microservices changes.

The organization of an online service and the accessibility of its particular microservices varies by platform. Consult your platform's online services documentation for more information.

## More Information

### Header File

Consult the `Connectivity.h` header file directly for more information as needed. The Connectivity Interface header file `Connectivity.h` is located in the directory:

C++

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [status](https://dev.epicgames.com/community/search?query=status)
* [connectivity](https://dev.epicgames.com/community/search?query=connectivity)
* [connection](https://dev.epicgames.com/community/search?query=connection)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#functions)
* [Enumerated Classes](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#enumerated-classes)
* [EOnlineServicesConnectionStatus](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#e-online-services-connection-status)
* [Connection Status](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#connection-status)
* [More Information](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
