<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/file-logging-analytics-provider-for-unreal-engine?application_version=5.7 -->

# File Logging Analytics Provider

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
7. [In-Game Analytics](/documentation/en-us/unreal-engine/in-game-analytics-for-unreal-engine "In-Game Analytics")
8. File Logging Analytics Provider

# File Logging Analytics Provider

The file logging provider can be used to debug your analytics process during development.

![File Logging Analytics Provider](https://dev.epicgames.com/community/api/documentation/image/aa2d0d57-e92d-4456-84a8-5019520dbfc3?resizing_type=fill&width=1920&height=335)

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a516355a-76ac-4d3c-8cba-1df99fe8f9b3/image00.png)

This provider is used to write analytics API calls to disk in JSON format. The reason to use this provider is for debugging the analytics process. It writes the data to the
`Saved/Analytic`s folder giving each file a unique name that ends in `.analytics`. You can then compare the data saved in that file to the events on your analytics provider's dashboard to
make sure all of the data is being processed. There aren't any special configuration settings for this provider.

This provider writes each session's data to disk which will cause ever-growing data in a released game or app. We recommend that you only use this provider for development and
don't include it in your released product.

The image below shows files created when testing the 4.8 API additions.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be69b647-635a-437e-b95e-8a54ccde7608/image01.png)

* [analytics](https://dev.epicgames.com/community/search?query=analytics)
* [file logging](https://dev.epicgames.com/community/search?query=file%20logging)
* [file logging analytics](https://dev.epicgames.com/community/search?query=file%20logging%20analytics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
