<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-user-interface-in-unreal-engine?application_version=5.7 -->

# Online User Interface

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
7. [Online Subsystem](/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine "Online Subsystem")
8. Online User Interface

# Online User Interface

Overview of the Online User Interface.

![Online User Interface](https://dev.epicgames.com/community/api/documentation/image/2957776b-e2c4-49d7-964c-d35038a38cfe?resizing_type=fill&width=1920&height=335)

 On this page

The **OnlineUser Interface** is the central repository for all cached information and metadata about users, both remote and local. This interface also provides reverse-lookup functionality, enabling developers to search for user IDs based on their display names or email addresses and map them back to Unreal Engine's native `FUniqueId` system.

## Retrieving and Examining User Metadata

To access user metadata, you must first request and cache that data from the online service. Call `QueryUserInfo` with a list of `FUniqueNetId` values for the users whose information you want, as well as the index of the local user making the request. This is an asynchronous process, and will call a delegate of type `OnQueryUserInfoComplete` when it finishes. After a successful query populates the cache with user information, the `GetAllUserInfo` function will return all collected data. If you have the `FUniqueNetId` of a specific user whose data you want, you can call `GetUserInfo` with that `FUniqueNetId` to get just that user's data.

## Mapping External User IDs

Most online services support searching for users by their display names or email addresses. The OnlineUser Interface mirrors this functionality with `QueryUserIdMapping`, which takes a display name or email address and attempts to map it, through the online service, to an `FUniqueNetId`. Since this procedure involves contacting the online service, it is asynchronous, and will call `FOnQueryUserMappingComplete` upon completion. Unlike most information requests, this function does not update a cache. Instead, when the operation is successful, the delegate's payload will contain the known display name or email address that was searched, and the resulting `FUniqueNetId` that the online service found.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online subsystem](https://dev.epicgames.com/community/search?query=online%20subsystem)
* [online user interface](https://dev.epicgames.com/community/search?query=online%20user%20interface)
* [userinfo](https://dev.epicgames.com/community/search?query=userinfo)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Retrieving and Examining User Metadata](/documentation/en-us/unreal-engine/online-subsystem-user-interface-in-unreal-engine?application_version=5.7#retrievingandexaminingusermetadata)
* [Mapping External User IDs](/documentation/en-us/unreal-engine/online-subsystem-user-interface-in-unreal-engine?application_version=5.7#mappingexternaluserids)
