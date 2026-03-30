<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7 -->

# Using In-App Purchases on iOS

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [iOS, iPadOS, and tvOS](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine "iOS, iPadOS, and tvOS")
7. [iOS and tvOS Development Guides](/documentation/en-us/unreal-engine/developing-on-ios-tvos-and-ipados-in-unreal-engine "iOS and tvOS Development Guides")
8. Using In-App Purchases on iOS

# Using In-App Purchases on iOS

Using in-app purchases to offer additional paid content for your iOS game.

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Using In-App Purchases](/documentation/en-us/unreal-engine/using-inapp-purchases-in-unreal-engine-projects-for-mobile-devices)

 On this page

In-app purchases enable you to offer additional content and features to users. You can use this as a means to monetize a free application or to provide additional paid content for your application. This page provides iOS-specific information, but you must be familiar with the general in-app purchases information described in the [Using In-App Purchases](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-inapp-purchases-in-unreal-engine-projects-for-mobile-devices) documentation.

## Apple App Store Details

The information below is vague in some cases. Please check official [App Store](https://developer.apple.com/documentation/appstoreconnectapi/app-store) and [StoreKit](https://developer.apple.com/documentation/storekit) documentation for additional details

## Querying product information

In-app products are identified by the string based product ID you configure for each product on your application in `AppStoreConnect`.

StoreKit handles initiating a purchase for an in-app product or subscription the same way. Before you can initiate a purchase for a given product, you need to query its updated information at some point since some internal objects from this query are used to trigger the purchase flow. You can query for product information using the **Read In App Purchase Information2** blueprint node or `IOnlineStore::QueryOffersById` in C++.

If the methods described in this document don't function due to changes in the API, you can  check the [App Store Server APIs](https://developer.apple.com/documentation/appstoreserverapi) to find the proper API for server validation, you can check subscriptions state server-side, and/or you can use the [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications).

## Validation

You should validate your receipts to avoid fraud. Check the [official documentation about receipt validation](https://developer.apple.com/documentation/storekit/choosing-a-receipt-validation-technique) for more information.

Take into account that when using local validation, there is no way to check for subscription state and expiration times. You can gather validation information using the [Get Transaction Info endpoint](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-info), and you can gather subscription state and expiration information using the [Get All Subscription Statuses endpoint](https://developer.apple.com/documentation/appstoreserverapi/get-all-subscription-statuses).

You should finalize all transactions locally on device once validated and the product is granted. You can accomplished this by calling `IOnlinePurchase::FinalizePurchase` or use the **Finalize In-App Purchase Transaction** blueprint node on the completed receipt. Not finalizing transactions may lead to bad device performance

## Product Types

App Store differentiates between consumable in-app products, non-consumable in-app products, and subscriptions. Transactions for all of them are handled the same way and they need to be finalized when completed. Autorenewed subscriptions generate a new receipt each time they are renewed

## Receipts and Receipt Persistence

Only receipts for non-completed transactions can be gathered at any point. Once a transaction is finished, by calling `IOnlinePurchase::FinalizePurchase` or using the Finalize **In-App Purchase Transaction** Blueprint node, it won’t generate a receipt on following queries for receipts. For that reason, you must always keep a record of the user-granted products.

When a subscription is renewed it generates a new receipt. To detect those events while the game is running you can register to the `OnUnexpectedPurchaseReceipt` delegate in IOnlinePurchase. Subsequent calls to query receipts will contain the new receipt until it is handled and finalized.

Successful deferred and interrupted purchases will also be notified through `OnUnexpectedPurchaseReceipt`. Those types of transactions initially generate a failed receipt with a deferred or canceled state, and can generate a new successful transaction when they succeed.

See the [official StoreKit documentation](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox) for more information.

ValidationInfo stored in the receipt for each line item contains a FString containing the Base64 encoded AppReceipt that should be used for validation.

### Subscription Expiration Management

Subscription status and expiration times are not available on devices. After the receipt is finalized there is no information regarding a possible active subscription. You can check the subscription state and expiration times server-side using the [Get All Subscription Statuses endpoint](https://developer.apple.com/documentation/appstoreserverapi/get-all-subscription-statuses).

StoreKit does not notify devices in any way for subscription expiration, cancellation, or refund. Apple offers [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications) to detect those events server side.

### Testing In-app Purchases

You can test in-app purchases using [StoreKit testing in Xcode](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode/) or a sandbox environment. StoreKit testing in Xcode does not need in-app products to be configured in the AppStore connect application, but if they are already set up it can import the configuration to use it in a local environment. The application must be launched from Xcode and there are some tools to control transaction lifetime.

A [sandbox environment](https://developer.apple.com/documentation/storekit/in-app_purchase/testing_in-app_purchases_with_sandbox) uses real product information and you can use it to test server to server transactions. To use sandbox environments you need to setup a Sandbox Apple ID and use a development signed app properly configured in App Store connect.

### Restore Transactions

At any moment you can restore transactions using the **Restore Owned In-App Products** blueprint node or invoking `IOnlinePurchase::QueryReceipts` with the 
`bRestore`
 argument set to true. In that case a restore transactions operation is triggered, caching a receipt for each successful non-consumable or subscription transaction made in the past including subscription renewals. This can be useful to recover the full list of transactions when using the same App Store credentials in a new device.

Receipts marked as Restored do not need to be finalized.

## Configuration

1. Set up your in-app purchase in iTunes Connect:Google Play requires the id to be all lowercase, and it's best to have the ID for iOS and Android match as much as possible for ease of Blueprint setup.

   [![Sample product for testing](https://dev.epicgames.com/community/api/documentation/image/f769f309-488b-448f-8210-280b6fd7e8a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f769f309-488b-448f-8210-280b6fd7e8a5?resizing_type=fit)
2. Make a note of the ID you use, as well as if the item is consumable or non-consumable or subscription

   1. Product IDs for subscriptions can be used directly on iOS implementation while GooglePlay implementation has some specific details
3. If you have a code project and have not already set up your project to use online subsystems, add the following block to your project's `Build.cs` file:

   C#

   ```
   |  |  |
   | --- | --- |
   |  | if (Target.Platform == UnrealTargetPlatform.IOS) |
   |  | { |
   |  | PrivateDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "OnlineSubsystem" }); |
   |  | DynamicallyLoadedModuleNames.Add("OnlineSubsystemIOS"); |
   |  | } |
   ```

   if (Target.Platform == UnrealTargetPlatform.IOS)
   {
   PrivateDependencyModuleNames.AddRange(new string[] { &quot;Core&quot;, &quot;CoreUObject&quot;, &quot;Engine&quot;, &quot;OnlineSubsystem&quot; });
   DynamicallyLoadedModuleNames.Add(&quot;OnlineSubsystemIOS&quot;);
   }

   Copy full snippet(5 lines long)
4. Edit `[ProjectName]/Config/IOS/IOSEngine.ini`:

   Config

   ```
   |  |  |
   | --- | --- |
   |  | [OnlineSubsystem] |
   |  | DefaultPlatformService=IOS |
   |  |  |
   |  | [OnlineSubsystemIOS.Store] |
   |  | bSupportsInAppPurchasing=True |
   ```

   [OnlineSubsystem]
   DefaultPlatformService=IOS
   [OnlineSubsystemIOS.Store]
   bSupportsInAppPurchasing=True

   Copy full snippet(5 lines long)
5. Blueprint nodes need the 
   `OnlineIdentity`
   to be properly enabled. To use GameCenter edit `[ProjectName]/Config/DefaultEngine.ini`:

   Config

   ```
   |  |  |
   | --- | --- |
   |  | [/Script/IOSRuntimeSettings.IOSRuntimeSettings] |
   |  | bEnableGameCenterSupport=True |
   ```

   [/Script/IOSRuntimeSettings.IOSRuntimeSettings]
   bEnableGameCenterSupport=True

   Copy full snippet(2 lines long)
6. Your provisioning profile AppID must match your App Store application bundle ID and must have the In-App Purchases entitlement. In-app purchases will not work using a wildcard provisioning profile.

If you are having difficulty configuring your in-app purchases, refer to the [Troubleshoot section](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-inapp-purchases-in-unreal-engine-projects-for-mobile-devices#troubleshoot) of the main in app purchases documentation.

* [ios](https://dev.epicgames.com/community/search?query=ios)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Apple App Store Details](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#appleappstoredetails)
* [Querying product information](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#queryingproductinformation)
* [Validation](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#validation)
* [Product Types](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#producttypes)
* [Receipts and Receipt Persistence](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#receiptsandreceiptpersistence)
* [Subscription Expiration Management](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#subscriptionexpirationmanagement)
* [Testing In-app Purchases](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#testingin-apppurchases)
* [Restore Transactions](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#restoretransactions)
* [Configuration](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-ios?application_version=5.7#configuration)
