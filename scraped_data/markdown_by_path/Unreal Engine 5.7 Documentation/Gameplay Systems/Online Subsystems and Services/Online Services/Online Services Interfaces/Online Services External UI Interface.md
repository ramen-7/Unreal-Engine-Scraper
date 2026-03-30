<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine?application_version=5.7 -->

# Online Services External UI Interface

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
9. Online Services External UI Interface

# Online Services External UI Interface

Display your platform's online services external user interface.

![Online Services External UI Interface](https://dev.epicgames.com/community/api/documentation/image/c86d2db5-83b8-4378-b244-9fc1898fa771?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services External UI Interface** provides access to your platform's online services external user interface. A platform-specific External UI can be useful for:

* User login
* Friends and social interaction

## API Overview

| Function | Description |
| --- | --- |
| [ShowLoginUI](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IExternalUI/ShowLoginUI?application_version=5.5) | Display the default online service's login UI. |
| [ShowFriendsUI](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IExternalUI/ShowFriendsUI?application_version=5.5) | Display the default online service's friends UI. |
| [OnExternalUIStatusChanged](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IExternalUI/OnExternalUIStatusChanged?application_version=5.5) | Event triggered when the external UI status changes. |

Access to the External UI interface only succeeds if the Online Services platform implementation that you are using supports the External UI interface.

## Accessing the External UI Interface

Some online services have built-in, standardized user interfaces that are displayed whenever certain operations are performed. Examples of operations that display the built-in UI might include:

* Logging in to online services
* Inviting a player to a session
* Adding a friend

These operations might bring up a game-independent form, overlay, screen, or workflow that the user must navigate to access that feature. This is generally done to ensure that certain sensitive interactions are always handled the same way, and are controlled by the company that owns the online service rather than individual, third-party developers. These features are also not standard across every online service, and in some cases, may only exist on one particular service or system. To handle these disparate features, the Online Services plugin collects them and provides the External UI Interface to interact with them.

## More Information

### Header File

See the `ExternalUI.h` header file directly for more information as needed. The External UI Interface header file `ExternalUI.h` is located in the directory:

C++

```
Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online
```

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [external ui](https://dev.epicgames.com/community/search?query=external%20ui)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Accessing the External UI Interface](/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine?application_version=5.7#accessing-the-external-ui-interface)
* [More Information](/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
