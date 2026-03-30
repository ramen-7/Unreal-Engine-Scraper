<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/flurry-analytics-provider-for-unreal-engine?application_version=5.7 -->

# Flurry Analytics Provider

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
8. Flurry Analytics Provider

# Flurry Analytics Provider

A set of Blueprint nodes provided to allow you to communicate with analytics services

![Flurry Analytics Provider](https://dev.epicgames.com/community/api/documentation/image/1fca90ec-f2c7-43cd-b46c-e266285f89b3?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e04d1249-b8c1-4d37-a7d8-535d844ea304/flurry.png)

[Flurry](http://www.flurry.com) is a widely used free analytics service. Because it is so widely used, it can compare your app's data to other applications in the same category. This lets you quickly get a feeling of how your game is doing and areas you might need to do some work. To use their service, you must register at their site, get an application key that uniquely identifies your app, and download the libraries which get compiled into the Flurry plugin. See the plugin's corresponding `<PlatformAndName>.Build.cs` file to see where the libraries and headers are expected to be placed.

## Configuration

Once you have done the prerequisites and have successfully built the plugin for the target platform, you can configure the plugin for your game. As of 4.8, there is only one configuration property to set: the key that uniquely identifies your game. The snippet below shows a theoretical configuration for Flurry. As with all analytics providers, the configuration data goes in your `DefaultEngine.ini` file.

```
	[Analytics]
	FlurryApiKey=RANDOM34LETTERS4511
Copy full snippet
```

* [analytics](https://dev.epicgames.com/community/search?query=analytics)
* [flurry](https://dev.epicgames.com/community/search?query=flurry)
* [flurry analytics](https://dev.epicgames.com/community/search?query=flurry%20analytics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuration](/documentation/en-us/unreal-engine/flurry-analytics-provider-for-unreal-engine?application_version=5.7#configuration)
