<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7 -->

# Commerce Interface

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
9. Commerce Interface

# Commerce Interface

Purchase and redeem game content outside of gameplay.

![Commerce Interface](https://dev.epicgames.com/community/api/documentation/image/6ffca624-9a46-49b1-9505-a4af335b3882?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services Commerce Interface** is Unreal Engine's foundation for any game service that provides players the ability to purchase or redeem game content outside of gameplay. The Commerce Interface consists of two primary components:

* **Transactions**: the process of purchasing store items with platform currency.

  + Once the transaction is complete, the interface will grant the player the appropriate entitlements.
* **Entitlements**: content that a player is entitled to receive or use.

  + A player may receive or use an entitlement because they purchased an item or redeemed a game code.

## API Overview

The following table provides a high-level description of the functions included in the Commerce Interface.

| Function | Description |
| --- | --- |
| **Offers** |  |
| [QueryOffers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/QueryOffers?application_version=5.5) | Fetch the list of all available offers from the store and cache them in the interface. This includes any available downloadable content (DLC), bundles, items, and so on. |
| [QueryOffersById](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/QueryOffersById?application_version=5.5) | Fetch the list of available offers from a list of supplied IDs and cache them in the interface. |
| [GetOffers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/GetOffers?application_version=5.5) | Retrieve offers from the interface cached by `QueryOffers`. |
| [GetOffersById](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/GetOffersById?application_version=5.5) | Retrieve offers from a list of supplied IDs cached with the interface. |
| **Store** |  |
| [ShowStoreUI](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/ShowStoreUI?application_version=5.5) | Show the native store UI for the user to view store information or process transactions outside of the game client. |
| **Checkout** |  |
| [Checkout](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/Checkout?application_version=5.5) | Initiate the purchase process with one or more purchase offers retrieved with `GetOffers` or `GetOffersById`. |
| **Event Listening** |  |
| [OnPurchaseCompleted](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/OnPurchaseCompleted?application_version=5.5) | Event that fires whenever a local user completes a transaction. This can be initiated either internally by `Checkout` or externally through the native store UI. |
| **Entitlements** |  |
| [QueryTransactionEntitlements](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/QueryTransactionEntitlements?application_version=5.5) | View the in-game entitlements corresponding to a successful `Checkout` call to provide these benefits to the player. |
| [QueryEntitlements](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/QueryEntitlements?application_version=5.5) | Fetch the list of already acquired entitlements for the specific user from the store and cache them in the interface. |
| [GetEntitlements](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/GetEntitlements?application_version=5.5) | Retrieve entitlements from the interface cached by `QueryEntitlements`. |
| [RedeemEntitlement](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/RedeemEntitlement?application_version=5.5) | Mark an entitlement as "redeemed". The entitlement will then have the redeemed flag when later queried. This is useful for when there is no external game service managing entitlements. |
| **Verification** |  |
| [RetrieveS2SToken](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ICommerce/RetrieveS2SToken?application_version=5.5) | Return a token that can be sent to game services backends to communicate with the platform and verify the ownership of the given entitlements. |

## Process Flow

We now provide an example process flow using the Online Services Commerce Interface that regulates the flow of a user launching a game, entering the in-game store to make a purchase, and verifying that purchase for use.

### Launch Game

After a user launches the game and successfully authenticates with their desired online service, the game calls `QueryEntitlements`. The game compares the data cached by `QueryEntitlements` against the registered entitlements in the user's save data to see which entitlements have been granted while the user was offline and appropriately applies them to the user. Simultaneously, the game uses the OnPurchaseCompleted event to listen for a message if the user completes a purchase in the future.

### Enter In-Game Store Interface

The user opens the menu for the store while in-game. The game shows a loading screen for the user opening the store while it calls QueryOffers. Once the query resolves, the game then calls GetOffers to get local copies of the data. The local copies are then passed on to the UI framework to render and display the game offers.

### Perform Transaction

Upon viewing the items on offer, the user decides to purchase a specific product, we will refer to this as `PRODUCT_A`. The user adds `PRODUCT_A` to their in-game cart (handled by the in-game UI) and confirms the transaction. After authenticating the user, the game calls `Checkout` with the ID of `PRODUCT_A`. This leads into the platform UI for final confirmation and payment handling.

Once `Checkout` successfully resolves and an `OnPurchaseCompleted` event fires, the game calls `QueryTransactionEntitlements` on the given transaction ID to obtain the in-game entitlement IDs granted to the user as part of the transaction, and applies them to the user's save game. If `PRODUCT_A` is not something that should be granted to the user's gameplay globally, the game then calls `RedeemEntitlement` to ensure that the entitlement for `PRODUCT_A` is not duplicated.

### Verify Transaction

After successfully purchasing and redeeming `PRODUCT_A`, the user decides to enter online play with their newly purchased `PRODUCT_A`. While authenticating the game server, the game notices that the local user is claiming a new entitlement and requests a verification token to ensure that the product is legitimate. The game calls `RetrieveS2SToken` on the IDs provided for verification and obtains a JSON Web Token (JWT), which the backend service then uses to connect to the platform service and verify the ownership of the product. Once this returns successfully, the user is then permitted to enter online play with their newly purchased item.

## Converting Code from the Online Subsystem

The Online Services Commerce Interface is responsible for all code owned by both the **Store** (read-only code) and **Purchase** (read / write code) interfaces from the [Online Subsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine). The following table shows the correspondence between objects from the Online Systems Commerce Interface and their counterparts from the older Online Subsystem.

| Online Services |  | Online Subsystem |  |
| --- | --- | --- | --- |
| **Interface** | **Object** | **Interface** | **Object** |
| Commerce | Offer | [Store](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-store-interface-in-unreal-engine?application_version=5.5) | Offer |
| Commerce | Entitlement | [Purchase](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-purchase-interface-in-unreal-engine) | Entitlement |

## More Information

### Header File

We welcome you to consult the `Commerce.h` header file directly for more information as needed. The Commerce Interface header file `Commerce.h` is located in the following directory:

C++

```
Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online
```

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For a step-by-step guide on how to obtain the UE source code, refer to our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [purchase](https://dev.epicgames.com/community/search?query=purchase)
* [store](https://dev.epicgames.com/community/search?query=store)
* [multiplayer](https://dev.epicgames.com/community/search?query=multiplayer)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [commerce](https://dev.epicgames.com/community/search?query=commerce)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Process Flow](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#process-flow)
* [Launch Game](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#launch-game)
* [Enter In-Game Store Interface](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#enter-in-game-store-interface)
* [Perform Transaction](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#perform-transaction)
* [Verify Transaction](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#verify-transaction)
* [Converting Code from the Online Subsystem](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#converting-code-from-the-online-subsystem)
* [More Information](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
