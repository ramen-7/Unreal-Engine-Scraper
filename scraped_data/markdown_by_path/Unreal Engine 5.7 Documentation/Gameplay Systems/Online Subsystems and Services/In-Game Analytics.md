<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/in-game-analytics-for-unreal-engine?application_version=5.7 -->

# In-Game Analytics

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
7. In-Game Analytics

# In-Game Analytics

Use in-game analytics to track player engagement and find balance issues.

![In-Game Analytics](https://dev.epicgames.com/community/api/documentation/image/42023fb4-e0c9-4d26-ba03-ad821be040b1?resizing_type=fill&width=1920&height=335)

 On this page

In order to get data on how your game is performing, you must use an analytics provider to capture and process the data. For those without a homegrown solution, there are plenty of
options available, from free services to paid ones. Unreal Engine provides an abstract interface for communicating with one or more analytics providers. Your game uses the interface, and analytics providers offer a backing implementation. In some cases, Epic has built the backing provider already. Previously, Epic Games provided an implementation to multicast analytics events, relaying them to multiple providers. For providers, there is support of providers that support [Swrve](http://www.swrve.com), a paid service, and support for Flurry.

More provider plugins will become available over time, and it is also feasible to add your own provider if needed.

## Implementing Game Analytics

[![Instrumenting Your Game](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c611e6c8-e38b-484c-92e8-67f3b075ed31/placeholder_topic.png)

Instrumenting Your Game

Using in-game analytics to track player engagement and find balance issues.](/documentation/en-us/unreal-engine/instrumenting-your-game-with-analytics-in-unreal-engine)
[![Blueprint Analytics Plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b6777b6-7e28-450a-bae3-124429404c6c/placeholder_topic.png)

Blueprint Analytics Plugin

A set of Blueprint nodes for communicating with analytics services.](/documentation/en-us/unreal-engine/blueprint-analytics-plugin-for-unreal-engine)

## Providers

[![File Logging Analytics Provider](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0ac3b6c-9570-40b4-af6a-7b76f82d5053/placeholder_topic.png)

File Logging Analytics Provider

The file logging provider can be used to debug your analytics process during development.](/documentation/en-us/unreal-engine/file-logging-analytics-provider-for-unreal-engine)
[![Flurry Analytics Provider](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad672d01-e6f5-490b-b612-42f7990f8943/placeholder_topic.png)

Flurry Analytics Provider

A set of Blueprint nodes provided to allow you to communicate with analytics services](/documentation/en-us/unreal-engine/flurry-analytics-provider-for-unreal-engine)
[![Multicast Analytics Provider](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11fa21cc-019c-46fc-9a01-515458c2fdc8/placeholder_topic.png)

Multicast Analytics Provider

A set of Blueprint nodes provided to allow you to communicate with analytics services.](/documentation/en-us/unreal-engine/multicast-analytics-provider-for-unreal-engine)

* [analytics](https://dev.epicgames.com/community/search?query=analytics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Implementing Game Analytics](/documentation/en-us/unreal-engine/in-game-analytics-for-unreal-engine?application_version=5.7#implementinggameanalytics)
* [Providers](/documentation/en-us/unreal-engine/in-game-analytics-for-unreal-engine?application_version=5.7#providers)
