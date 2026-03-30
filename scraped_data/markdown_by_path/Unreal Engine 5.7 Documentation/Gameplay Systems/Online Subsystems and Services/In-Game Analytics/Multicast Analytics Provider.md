<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/multicast-analytics-provider-for-unreal-engine?application_version=5.7 -->

# Multicast Analytics Provider

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
8. Multicast Analytics Provider

# Multicast Analytics Provider

A set of Blueprint nodes provided to allow you to communicate with analytics services.

![Multicast Analytics Provider](https://dev.epicgames.com/community/api/documentation/image/c29dfe20-ec22-4460-bbb3-2eee08f7bec0?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d5b2369-8384-40e6-8097-9d10a69e74be/image00.png)

The multicast provider sends analytics events to multiple providers. This allows you to use multiple analytics providers easily, since it will take the calls and hand them to each
registered analytics providers in turn without you having to manually do this dispatching work. Having multiple analytics providers is desirable since each provider has different
strengths and weaknesses. By using multiple providers, you can get all of the features that you need to run your app business.

## Configuration

Configuring the provider is straightforward. It just needs to know the list of providers that you want data sent to. This list is provided as a comma-delimited list of the module
names for the providers. In the example below, the AnalyticsMulticast provider is specified as the default provider for the application. Then, the list of providers that it sends
the data to is specified using a comma-delimited list as mentioned before. As with all analytics providers, the configuration data goes in your `DefaultEngine.ini` file.

[Analytics]
ProviderModuleName=AnalyticsMulticast
ProviderModuleNames=FileLogging,IOSFlurry,IOSApsalar

* [analytics](https://dev.epicgames.com/community/search?query=analytics)
* [multicast](https://dev.epicgames.com/community/search?query=multicast)
* [multicast analytics](https://dev.epicgames.com/community/search?query=multicast%20analytics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuration](/documentation/en-us/unreal-engine/multicast-analytics-provider-for-unreal-engine?application_version=5.7#configuration)
