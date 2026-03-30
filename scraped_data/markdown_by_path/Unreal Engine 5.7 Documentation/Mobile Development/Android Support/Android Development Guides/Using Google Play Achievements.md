<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects?application_version=5.7 -->

# Using Google Play Achievements

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
8. Using Google Play Achievements

# Using Google Play Achievements

Using Google Play Achievements to increase player engagement.

![Using Google Play Achievements](https://dev.epicgames.com/community/api/documentation/image/0bfb379c-8331-43e6-a230-077ad36626f7?resizing_type=fill&width=1920&height=335)

 On this page

![Banner Image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/602d06a2-61e2-4fd8-8cb6-56e9e27e7c6c/achievements-banner.png "Banner Image")

## Configuration

Please see [Achievements | Play Games Services | Google Developers](https://developers.google.com/games/services/common/concepts/achievements) for information on setting up the Google Play Game Services for your application.

For your Unreal Project:

1. In the **Edit** menu in **Unreal Editor**, select **Project Settings** to view the configuration options for your project.

   ![Open Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cede3c85-8c7a-46e5-b86e-f3ce32f97f1c/ue5_1-01-open-project-settings.png "Open Project Settings")
2. On the left, Select the **Platforms: Android** tab. Navigate to the **Google Play Services** section and configure project for Google Play services platform.

   [![Configure project for Google Play services](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5490ef50-daed-4bff-a230-b44308a93588/ue5_1-02-configure-project-for-google-play.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5490ef50-daed-4bff-a230-b44308a93588/ue5_1-02-configure-project-for-google-play.png)

   Click to full view
3. In the **Google Play Services** section, check the **Enable Google Play Support** option.
4. Enter the App ID for your game in the **Games App ID** field.
5. Enter your Google Play License Key in the **Google Play License Key** field.
6. Add an element to the **Achievement Map**.
7. In the **Achievement Map** you'll need to enter a **Name** that is only used within your Unreal Project and the **Achievement ID** you set up in your Google Play Services.

   [![Set other options in the Google Play Services section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c586f660-b034-4840-9f2f-d1b5d72cac34/ue5_1-03-set-options-for-google-play.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c586f660-b034-4840-9f2f-d1b5d72cac34/ue5_1-03-set-options-for-google-play.png)

   Click to full view

   All of these values are available in the Google Play Developer Console for your App and Game Services.

Since the **Name** value in the achievement map is only a mapping for the Google Play Services **Achievement ID**, and iOS is directly referred to by their **Achievement Reference**, and if you are releasing on both Android and iOS platforms, enter the Achievement Reference from your iOS Game Center settings as your **Name** so you only have to call one node regardless of platform.

## Caching your Achievements

**Cache Achievements** will request from the platform's game service the list of achievements and the values the current player has for said achievements. You'll be able to use the **Get Cached Achievement Value** if this node returns successfully.

Note that it is a **latent** node, and thusly has a number of execution output pins. The top most is a "pass through," that works like any other execution output pin. The other two pins (**On Success**, and **On Failure**) will execute when the online service returns (or fails to return) a value. When the execution returns a success

**In Blueprints:**

The example below is from the **Global Game Instance** Blueprint in the Unreal Match 3 sample game. After the user logs into the device's game platform (Game Center, Google Play), we run the **Cache Achievements** node and actually halt execution (by not having anything execute off the top output execution pin) at this point to give the service time to return all the achievements:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d417e742-f29d-4b47-a696-54d68b552dc2/cacheachievements.png)

## Reading Values from your Achievements

The **Get Cached Achievement Progress** will return the progress of a given **Achievement ID** for the provided **Player Controller**, and only work if a **Cache Achievements** node was run earlier and returned successfully.

For iOS Game Center, this value is actually a floored float, as they store it as an integer. A float is received for Google Play Services.

**In Blueprints:**

The example below is from the **Global Game Instance** Blueprint in the Unreal Match 3 sample game. Once the achievements are cached, we run through a loop pulling achievement names, as well as their target scores, from arrays, and do a quick comparison to any offline values found. We then accept the higher value of the service or the local values:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8537d173-5f1c-41dd-bbf9-f7262fa6c8f7/readachievement.png)

## Writing Values to your Achievements

The **Write Achievement Progress** will send a message up to the platform's achievement system to write a percentage (0.0% - 100.0%) based **Progress** to the provided achievement for the given user (**Player Controller** and **User Tag**). For "one off" achievements you will always pass in `100.0` for **Progress**, while for incremental achievements, you'll be passing in some lesser percentage until the user reaches `100.0` for that achievement.

For iOS Game Center, this value is actually sent as an integer, as they only have 1-100 incremental achievements. A float is sent for Google Play Services.

Note that it is a **latent** node, and thusly has a number of execution output pins. The top most is a "pass through," that works like any other execution output pin. The other two pins (**On Success**, and **On Failure**) will execute when the online service returns (or fails to return) a value. When the execution returns a success the **Written Achievement Name**, **Written Progress**, and **Written User Tag** will return non-null values equal to what you passed into the node.

**In Blueprints:**

The example below is from the **Global Game Instance** Blueprint in the Unreal Match 3 sample game. There's a loop that compares the current achievement value to the metrics required to increase that achievement, and if progress has been made, the **Write Achievement** event is called:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5aaafac6-48f6-493e-a2c1-871bb3dd000a/writeachievement.png)


This was done because latent nodes can't be used in Functions.

## Showing the Platform Specific Achievement Screen

The **Show Platform Specific Achievement Screen** will show the achievements of the provided **Player Controller** for the current platform.

**In Blueprints:**

The example below is from the **GameOverButtons** Blueprint Widget in the Unreal Match 3 sample game. When the **ShowAchievements** button is pressed, the game will attempt to show the achievement screen for the current platform.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/71d220d8-6490-411a-9440-def2a0a3d433/showachievements.png)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [achievements](https://dev.epicgames.com/community/search?query=achievements)
* [android](https://dev.epicgames.com/community/search?query=android)
* [services](https://dev.epicgames.com/community/search?query=services)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuration](/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects?application_version=5.7#configuration)
* [Caching your Achievements](/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects?application_version=5.7#cachingyourachievements)
* [Reading Values from your Achievements](/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects?application_version=5.7#readingvaluesfromyourachievements)
* [Writing Values to your Achievements](/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects?application_version=5.7#writingvaluestoyourachievements)
* [Showing the Platform Specific Achievement Screen](/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects?application_version=5.7#showingtheplatformspecificachievementscreen)
