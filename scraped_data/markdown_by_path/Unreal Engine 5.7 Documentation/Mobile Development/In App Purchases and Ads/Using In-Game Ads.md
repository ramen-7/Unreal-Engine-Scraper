<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-in-game-ads-in-unreal-engine-projects-on-mobile-platforms?application_version=5.7 -->

# Using In-Game Ads

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
6. [In App Purchases and Ads](/documentation/en-us/unreal-engine/in-app-purchases-and-ads-in-unreal-engine-projects "In App Purchases and Ads")
7. Using In-Game Ads

# Using In-Game Ads

Using in-game advertisements to monetize your game.

![Using In-Game Ads](https://dev.epicgames.com/community/api/documentation/image/8f39a10f-a49d-4e69-a281-574cf69aab0c?resizing_type=fill&width=1920&height=335)

 On this page

In-game advertisements enable you to display ads to players of your game on mobile platforms. This provides a means of monetizing your game while allowing it to remain completsharing-and-releasing-projects/general-mobile-development/supporting-mobile-services

![Banner Image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/466479f4-ac6f-4eaf-b95c-f82eec6657c6/ads-banner.png "Banner Image")

## Configuration

See the appropriate platform-specific page below for details on configuring in-game advertisements for each platform:

* [Using Ad Mob In-Game Ads on Android](/documentation/en-us/unreal-engine/using-ad-mob-for-in-game-ads-on-android-with-unreal-engine)

## Showing the Ad Banner

The **Show Ad Banner** function is used to display an ad banner in your game. Call it somewhere in the logic where you want to show an ad, such as when the main menu is shown.

**In Blueprints:**

The example below is from the Unreal Match 3 sample game, which displays an ad banner when the victory/defeat screen is shown using the **Construct** event of that Widget Blueprint:

![Blueprint script for showing ad banner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9e9a09e-1fcd-419b-a55f-5179da84cb27/ue5_1-01-bp-script-show-ad.png "Blueprint script for showing ad banner")

See the [Show Ad Banner](https://docs.unrealengine.com/BlueprintAPI/Utilities/Platform/ShowAdBanner) reference for more information on the node.

## Hiding the Ad Banner

The **Hide Ad Banner** functions hides the visible ad banner. Call it when you no longer want the ad to be displayed, such as when you exit the main menu.

**In Blueprints:**

The example below is from the Unreal Match 3 sample game, which hides the ad banner when the victory/defeat screen is exited using the **Destruct** event of that Widget Blueprint:

![Blueprint script for hiding ad banner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa373c76-07ac-432b-b765-c1b9f4e66bd7/ue5_1-02-bp-script-hide-ad.png "Blueprint script for hiding ad banner")

See the [Hide Ad Banner](https://docs.unrealengine.com/BlueprintAPI/Utilities/Platform/HideAdBanner) reference for more information on the node.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [services](https://dev.epicgames.com/community/search?query=services)
* [ads](https://dev.epicgames.com/community/search?query=ads)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuration](/documentation/en-us/unreal-engine/using-in-game-ads-in-unreal-engine-projects-on-mobile-platforms?application_version=5.7#configuration)
* [Showing the Ad Banner](/documentation/en-us/unreal-engine/using-in-game-ads-in-unreal-engine-projects-on-mobile-platforms?application_version=5.7#showingtheadbanner)
* [Hiding the Ad Banner](/documentation/en-us/unreal-engine/using-in-game-ads-in-unreal-engine-projects-on-mobile-platforms?application_version=5.7#hidingtheadbanner)
