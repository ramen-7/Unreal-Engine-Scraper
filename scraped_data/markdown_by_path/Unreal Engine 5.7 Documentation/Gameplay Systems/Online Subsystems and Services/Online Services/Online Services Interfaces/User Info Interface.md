<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7 -->

# User Info Interface

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
9. User Info Interface

# User Info Interface

Access a player's display name and avatar for use in your game.

![User Info Interface](https://dev.epicgames.com/community/api/documentation/image/03bab417-248b-47b8-a3cb-dbca2ff08811?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services User Info Interface** provides you with tools to retrieve user information from an online service such as Steam or Epic Online Services for display in your game. This includes a player's:

* Platform Profile.
* Display Name.
* Avatar.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the User Info Interface:

| Function | Description |
| --- | --- |
| **User Information** |  |
| [QueryUserInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserInfo/QueryUserInfo?application_version=5.5) | Query user info for the list of account IDs. |
| [GetUserInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserInfo/GetUserInfo?application_version=5.5) | Retrieve the user info for the account ID previously cached by `QueryUserInfo`. |
| **User Avatar** |  |
| [QueryUserAvatar](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserInfo/QueryUserAvatar?application_version=5.5) | Query user avatars for the list of account IDs. |
| [GetUserAvatar](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserInfo/GetUserAvatar?application_version=5.5) | Retrieve the user avatar for the account ID previously cached by `QueryUserAvatar`. |
| **Platform UI** |  |
| [ShowUserProfile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserInfo/ShowUserProfile?application_version=5.5) | Show the profile UI for the provided account ID. |

## Access User Info

Accessing user information with the User Info Interface works similarly to the other [Online Services Interfaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-services-interfaces-in-unreal-engine).

`QueryUserInfo` caches the list of user display names associated with their corresponding account ID with the interface. `QueryUserInfo` requires you to provide the list of user account IDs for which you want to access display names as parameters. To access each user's display name, call `GetUserInfo` using their account ID.

## Access User Avatar

The workflow defined in the [Access User Info](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.5) section applies to accessing a user's avatar as well. `QueryUserAvatar` caches the information with the interface. `GetUserAvatar` retrieves each avatar individually.

## Platform User Profile

`ShowUserProfile` brings up the platform service's profile user interface for the provided user. Platform service profiles are specific to the platform on which the user is currently playing your game. Consult your platform service's documentation for more information on the profile user interface.

## More Information

### Header File

Consult the `UserInfo.h` header file directly for more information as needed. The User Info Interface header file `UserInfo.h` is located in the directory:

C++

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and how to process the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [user info](https://dev.epicgames.com/community/search?query=user%20info)
* [user metadata](https://dev.epicgames.com/community/search?query=user%20metadata)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#functions)
* [Access User Info](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#access-user-info)
* [Access User Avatar](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#access-user-avatar)
* [Platform User Profile](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#platform-user-profile)
* [More Information](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
