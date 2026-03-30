<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7 -->

# Using In-App Purchases on Android

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
6. [Android Support](/documentation/en-us/unreal-engine/android-support-for-unreal-engine "Android Support")
7. [Android Development Guides](/documentation/en-us/unreal-engine/developing-guides-for-android-in-unreal-engine "Android Development Guides")
8. Using In-App Purchases on Android

# Using In-App Purchases on Android

Using in-app purchases to offer additional paid content for your Android game.

![Using In-App Purchases on Android](https://dev.epicgames.com/community/api/documentation/image/a44e20f3-ada9-49d2-867d-8c0f97bf9359?resizing_type=fill&width=1920&height=335)

 On this page

In-app purchases enable you to offer additional content and features to
users. You can use this as a means to monetize a free application or to
provide additional paid content for your application. This page provides
iOS-specific information, but you must be familiar with the general
in-app purchases information described in the [Using In-App Purchases](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-inapp-purchases-in-unreal-engine-projects-for-mobile-devices) documentation.

## Google Play Details

The information below is vague in some cases. Please check the [Google Play documentation](https://developer.android.com/distribute) for additional details.

### Querying Product Information

In-app purchase products are identified by the string-based product ID you configure for each product on the Google Play console for your application.

Subscription types in Google Play are identified by a product ID, a plan ID, and an optional offer ID. A given subscription product identified by a product ID might be configured with different plans. Different plans can define different subscription periods, auto renewal, and some other details. Each plan might define offers which can modify the renewal price under some conditions. You can find specific details for subscription management in [Google Billing library official documentation](https://developer.android.com/google/play/billing/subscriptions).

Regarding `OnlineSubsystemGooglePlay` and Blueprint implementation, the product IDs used for subscriptions in any query should be prefixed with 
`s-`. For example, when querying for product information for a subscription with product ID 
`test_subscription_1`
in the store you should instead use `s-test_subscription_1`
 as the product ID.

C++

```
// null checks ommited for simplicity

FUniqueNetIdRepl PlayerNetId = ...;
TArray<FString>& ProductIDs = {TEXT("test_product_1"), // Product ID in the store is test_product_1. 
                                                       // It is not a subscription
                               TEXT("s-test_subscription_1"}; // Product ID in the store is test_subscription_1
                                                              // It is a subscription

IOnlineSubsystem* OnlineSub = IOnlineSubsystem::Get();
IOnlineStoreV2Ptr StoreInterface = OnlineSub->GetStoreV2Interface();
```

Expand code  Copy full snippet(18 lines long)

Because there are several methods to purchase a subscription, the query for a product ID regarding a subscription may generate several entries describing all possible ways to purchase the product.

As an example, consider a subscription with a product ID `test_subscription_id` that has 2 base plans named `base-plan-1` and `base-plan-2`, with `base-plan-1` having 2 offers named 
`offer-1`
 and 
`offer-2`. `offer-1` has an initial Free trial, a discounted period and then auto renewals are done at the base-plan-1 regular price

The following images show how the configuration for that product would look like in the Google Play Console:

[![A test product in the Google Play console.](https://dev.epicgames.com/community/api/documentation/image/10639421-552d-498e-b34c-91761393e2c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10639421-552d-498e-b34c-91761393e2c4?resizing_type=fit)

[![Editing a test product in Google Play console](https://dev.epicgames.com/community/api/documentation/image/9aa82916-c0cc-4988-b881-50c8c259ee63?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9aa82916-c0cc-4988-b881-50c8c259ee63?resizing_type=fit)

This example generates product information entries with the following product IDs in the response:

|  |  |
| --- | --- |
| `s-test_subscription_1:base-plan1` | * Product ID to purchase `test_subscription_1` subscription with    `base-plan-1`    conditions. * No offer applied. * Price point reported is the regular `base-plan-1` price. |
| `s-test_subscription_1:base-plan1:offer-1` | * Product ID to purchase    `test_subscription_1`    subscription with    `base-plan-1`    conditions and applying `offer-1`. * Price point reported is the regular `base-plan-1` price (which is the last price point for an offer). |
| `s-test_subscription_1:base-plan1:offer-1:0` | * Product ID equivalent to `s-test_subscription_1:base-plan-1:offer-1`. * Price point reported for this entry is the price for the first block of renewal periods (free in this example). |
| `s-test_subscription_1:base-plan1:offer-1:1` | * Product ID equivalent to `s-test_subscription_1:base-plan-1:offer-1`. * Price point reported for this entry is the price for the second block of renewal periods (discounted price in this example). |
| `s-test_subscription_1:base-plan1:offer-1:2` | * Product ID equivalent to `s-test_subscription_1:base-plan-1:offer-1.` * Price point reported for this entry is the regular `base-plan-1`   price (which is the price for additional renewals). |
| `s-test_subscription_1:base-plan1:offer-2` | * Product ID to purchase    `test_subscription_1`    subscription with    `base-plan-1`    conditions and applying `offer-2` . * Price point reported is that of the first block of renewals. |
| `s-test_subscription_1:base-plan2` | * Product ID to purchase    `test_subscription_1`    subscription with `base-plan-2`  conditions. No offer applied. * Price point reported is the regular base-plan-1 price. |

Entries with Product IDs in the form `s-[product ID]:[plan]:[offer]:[number]` are meant to contain different price points for a given subscription so they are available to show to the user if needed.

### Validation

Google documentation recommends you validate your transactions using server-to-server calls before granting any benefit to the users:

[Google Play documentation: Fight fraud and abuse](https://developer.android.com/google/play/billing/security)

[Google Play documentation: Integrate Google Play with your server backend](https://developer.android.com/google/play/billing/backend)

They also recommend acknowledging or consuming the transaction from your backend servers using Google Play Developer API calls.

[Method: purchases.products.consume](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/acknowledge)

[Method: purchases.subscriptions.acknowledge](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/consume)

[Method: purchases.products.acknowledge](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge)

If you are not using a backend server or you want your implementation to work seamlessly on both iOS and Android, remember to call `IOnlinePurchase::FinalizePurchase` or use the **Finalize In-App Purchase Transaction** Blueprint node on the completed receipt. When using backend acknowledge or consumption remember to set `bDisableLocalAcknowledgeAndConsume` to true.

Remember that any kind of on-device validation is not safe and subscription expiration data is not available on a device. The only way to know a subscription is still active on a device is if a receipt for it exists, and that receipt must be validated to know it is legitimate.

### Product Types

The Google Play Billing library differentiates between subscriptions and in-app products. Transactions for those products should be finalized by acknowledging subscriptions and non consumable products and by consuming consumable products. Consuming implies acknowledgement. The store does not have any knowledge about products being consumable or not. Is the way you finalize them that defines what is a consumable. Subscription automatic renewal does not generate any new receipt on device.

In that sense, by default, `IOnlinePurchase::FinalizePurchase` from C++ and the **Finalize In-App Purchase Transaction** Blueprint node acknowledge subscriptions and consume in-app products locally from the device.

In case you want to support non-consumable products, you can do the finalization server-side and it is under your server control when to communicate with Google servers to consume or acknowledge an in-app product transaction. To disable local acknowledge and consume you can set the following in `[ProjectName]/Config/Android/AndroidEngine.ini`:

Config

```
|  |  |
| --- | --- |
|  | [OnlineSubsystemGooglePlay.Store] |
|  | bDisableLocalAcknowledgeAndConsume=True |
```

[OnlineSubsystemGooglePlay.Store]
bDisableLocalAcknowledgeAndConsume=True

Copy full snippet(2 lines long)

Remember that non-acknowledged transactions are refunded after a period of time (some days in production; some minutes in a sandbox environment).

## Receipts and Receipt Persistence

Receipts for transactions can be gathered while a product is not consumed and not expired. That means that the receipts gathered when querying for owned products will always contain receipts for active subscriptions, owned non-consumed in-app products, and non-acknowledged transactions at the moment the query was made. Be careful about not granting the same benefit twice in case of subscriptions and non-consumable products. Receipts for consumed in-app products will not appear. A non-consumed in-app product cannot be purchased again until consumed (the billing library will have an “already owned” error).

ValidationInfo contained in the receipt for each line item contains a FString containing a JSON with the Base64 encoded JSON receipt, its base64 signature, and a `isSubscription` field set to true in case the purchase is for a subscription product

## Subscription Expiration Management

Subscription status and expiration times are not available on device. The only information regarding a possible active subscription is the presence of a receipt for its product ID. You can check subscription state and expiration times server-side by using the same Google Play Developer API endpoints used for validation:

[Method: purchases.subscriptionsv2.get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get)

[Method: purchases.subscriptions.get (deprecated)](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get)

The Google billing library does not notify devices in any way for subscription expiration, cancellation, or refund. Google Play Developer API offers [real-time server notifications](https://developer.android.com/google/play/billing/rtdn-reference) to detect those events server side.

Take into account that enabling those notifications may incur additional charges.

## Testing In-app Purchases

Google provides an environment to test in-app purchases on devices without any charge by using a license tester account. Refer to the [Google Play official documentation](https://developer.android.com/google/play/billing/test) for more information:

There is no need to sign your APK with the release key in order to test purchases if you are using a license tester.

### Configuration

1. Set up your in-app purchase in Google Play:

   Google Play requires the ID to be all lowercase, and it's best to have the ID for iOS and Android match as far as possible for ease of Blueprint setup.

   [![Set the ID in Google Play](https://dev.epicgames.com/community/api/documentation/image/0f9f08da-775a-4b42-9dde-5718127012be?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f9f08da-775a-4b42-9dde-5718127012be?resizing_type=fit)
2. Make a note of the ID you use, as well as the product type: in-app product or subscription.

   1. Google Play does not differentiate between consumable and non-consumable products.

      1. A product is consumable if its transaction is consumed.
      2. A product is non-consumable if its transaction is only acknowledged.

      If local consume and acknowledge is enabled, all non-subscription products are treated as consumable when invoking `FinalizePurchase`.
   2. When you use the product ID for a subscription in Unreal Engine you should prefix it with `s-`.
3. If you have not already set up your project to use online subsystems, enable it through the Plugins dialog or add the following block to your project's Build.cs file:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | if (Target.Platform == UnrealTargetPlatform.Android) |
   |  | { |
   |  | PrivateDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "OnlineSubsystem" }); |
   |  | DynamicallyLoadedModuleNames.Add("OnlineSubsystemGooglePlay"); |
   |  | } |
   ```

   if (Target.Platform == UnrealTargetPlatform.Android)
   {
   PrivateDependencyModuleNames.AddRange(new string[] { &quot;Core&quot;, &quot;CoreUObject&quot;, &quot;Engine&quot;, &quot;OnlineSubsystem&quot; });
   DynamicallyLoadedModuleNames.Add(&quot;OnlineSubsystemGooglePlay&quot;);
   }

   Copy full snippet(5 lines long)
4. In **Project Settings > Platforms > Android**, find the A**dvanced APKPackaging** section.
5. Add an element to **Extra Permissions** called `com.android.vending.BILLING`.

   [![Add an element to the Extra Permissions](https://dev.epicgames.com/community/api/documentation/image/8c34aa63-4e1f-4c0c-8782-ea61431eef2e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c34aa63-4e1f-4c0c-8782-ea61431eef2e?resizing_type=fit)
6. Blueprint nodes need the `OnlineIdentity` to be properly enabled.

   * You may need to also add `android.permission.USE_CREDENTIALS` to log into Google Play with existing accounts on the device.
7. Edit `[ProjectName]/Config/Android/AndroidEngine.ini`:

   Config

   ```
   |  |  |
   | --- | --- |
   |  | [OnlineSubsystem] |
   |  | DefaultPlatformService=GooglePlay |
   |  |  |
   |  | [OnlineSubsystemGooglePlay.Store] |
   |  | bEnableGooglePlaySupport=True |
   |  | bSupportsInAppPurchasing=True |
   ```

   [OnlineSubsystem]
   DefaultPlatformService=GooglePlay
   [OnlineSubsystemGooglePlay.Store]
   bEnableGooglePlaySupport=True
   bSupportsInAppPurchasing=True

   Copy full snippet(6 lines long)
8. If you will implement your in-app purchases validation using a validation server then edit `[ProjectName]/Config/Android/AndroidEngine.ini`. This avoids acknowledge and consume of transactions on the local device. Do those steps on the validation server after granting the purchased product through server to Google Play.

   Config

   ```
   |  |  |
   | --- | --- |
   |  | [OnlineSubsystemGooglePlay.Store] |
   |  | bDisableLocalAcknowledgeAndConsume=True |
   ```

   [OnlineSubsystemGooglePlay.Store]
   bDisableLocalAcknowledgeAndConsume=True

   Copy full snippet(2 lines long)

If you are having difficulty configuring your in-app purchases, refer to the [Troubleshoot section](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-inapp-purchases-in-unreal-engine-projects-for-mobile-devices#troubleshoot) of the main in app purchases documentation.

* [development](https://dev.epicgames.com/community/search?query=development)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [services](https://dev.epicgames.com/community/search?query=services)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Google Play Details](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#googleplaydetails)
* [Querying Product Information](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#queryingproductinformation)
* [Validation](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#validation)
* [Product Types](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#producttypes)
* [Receipts and Receipt Persistence](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#receiptsandreceiptpersistence)
* [Subscription Expiration Management](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#subscriptionexpirationmanagement)
* [Testing In-app Purchases](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#testingin-apppurchases)
* [Configuration](/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android?application_version=5.7#configuration)
