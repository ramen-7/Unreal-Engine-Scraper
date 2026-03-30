<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-store-interface-in-unreal-engine?application_version=5.7 -->

# Store Interface

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
8. Store Interface

# Store Interface

Online subsystems for describing and filtering offers for in-game purchases.

![Store Interface](https://dev.epicgames.com/community/api/documentation/image/1288f3f9-e8f9-41de-978c-ec747c1a4dd9?resizing_type=fill&width=1920&height=335)

 On this page

Two interfaces power your game's ability to support user purchases: The **Store Interface**, which provides the ability to make offers to your users, and the **Purchase Interface**, which enables users to accept these offers.
With the Store Interface, the game can retrieve offers from the online service, place them into categories, filter them, and manage them on an individual basis.
To execute a purchase, use the [Purchase Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-purchase-interface-in-unreal-engine).

An offer (class [FOnlineStoreOffer](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineSubsystem/Interfaces/FOnlineStoreOffer?application_version=5.5)) contains all necessary data about anything a user can purchase through the game.
This includes information like the description, the price, and the release and expiration dates.
Categories (class [FOnlineStoreCategory](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineSubsystem/Interfaces/FOnlineStoreCategory?application_version=5.5)) hold much simpler data, containing only a name and a list of subcategories.
The online services themselves handle setup and management of offers, while the Store Interface takes care of retrieval and filtration.

## Offers and Categories

The Store Interface retrieves offer and category data from the online service's servers.
Because this operation involves contacting a remote machine, it is broken into two phases: Retrieval and caching of data, which is asynchronous, and accessing that locally-cached data.
The Store Interface itself will automatically update the cache whenever a request completes, keeping only the results of the most recent query.

### Retrieving Offers and Categories

The first step in retrieving offer information is to retrieve the list of categories that the store contains.
The `QueryCategories` function handles this, and calls a provided delegate of type `FOnQueryOnlineStoreCategoriesComplete` when it finishes.
If successful, the Store Interface will have a cache containing all available category IDs.
At this point, the developer can begin querying for offers by making a filter (of type `FOnlineStoreFilter`) that includes certain categories, and excludes others.
With a filter, `QueryOffersByFilter` can retrieve offer IDs based on their category membership.
Once the Store Interface has retrieved and cached the offer IDs, developers can make queries for information about specific offers with the `QueryOffersById` function.
Both `QueryOffersByFilter` and `QueryOffersById` will use a provided delegate of type `FOnQueryOnlineStoreOffersComplete` to indicate success or failure, and the Store Interface's cache of offers will update following either operation completing successfully.

### Examining Offer Data

The "query" functions retrieve data about categories and offers into the Store Interface's cache.
To access this data, call `GetCategories` for the category cache, or `GetOffers` for the offer cache.
If you have a known offer ID, the `GetOffer` function will return information about the corresponding (cached) offer.

These functions all act on the local cache, so they do not have a callback.
However, they will only be useful if the cache has been populated.
These functions will not update the cache, so any live changes to categories or offers on the online service's store will not be reflected.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online subsystem](https://dev.epicgames.com/community/search?query=online%20subsystem)
* [store interface](https://dev.epicgames.com/community/search?query=store%20interface)
* [in-game purchases](https://dev.epicgames.com/community/search?query=in-game%20purchases)
* [store](https://dev.epicgames.com/community/search?query=store)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Offers and Categories](/documentation/en-us/unreal-engine/online-subsystem-store-interface-in-unreal-engine?application_version=5.7#offers-and-categories)
* [Retrieving Offers and Categories](/documentation/en-us/unreal-engine/online-subsystem-store-interface-in-unreal-engine?application_version=5.7#retrieving-offers-and-categories)
* [Examining Offer Data](/documentation/en-us/unreal-engine/online-subsystem-store-interface-in-unreal-engine?application_version=5.7#examining-offer-data)
