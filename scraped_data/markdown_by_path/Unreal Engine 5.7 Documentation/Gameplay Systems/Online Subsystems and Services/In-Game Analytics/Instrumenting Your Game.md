<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/instrumenting-your-game-with-analytics-in-unreal-engine?application_version=5.7 -->

# Instrumenting Your Game

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
8. Instrumenting Your Game

# Instrumenting Your Game

Using in-game analytics to track player engagement and find balance issues.

![Instrumenting Your Game](https://dev.epicgames.com/community/api/documentation/image/6af9fed5-472a-4a77-9ea2-018de1082e76?resizing_type=fill&width=1920&height=335)

The instructions below are from an earlier version of Unreal Engine. iOS Apsalar is no longer available in UE5. However, these instructions should still be applicable to other analytics frameworks.

The first step in capturing player retention data is to register an analytics provider for your game. This is done via your project's `DefaultEngine.ini` file. You must register a default provider. Optionally, you can register different providers and account details for different build types of your game (development, testing, and production). The sections below are an example of configuring the Apsalar plugin:

```
|  |  |
| --- | --- |
|  | [Analytics] |
|  | ProviderModuleName=IOSApsalar |
|  | ApiKey=YourAnalyticsKey1 |
|  | ApiSecret=YourAnalyticsSecret1 |
|  | SendInterval=60 |
|  |  |
|  | [AnalyticsDevelopment] |
|  | ApiKey=YourAnalyticsKey2 |
|  | ApiSecret=YourAnalyticsSecret2 |
|  | SendInterval=60 |
|  |  |
|  | [AnalyticsTest] |
|  | ApiKey=YourAnalyticsKey3 |
|  | ApiSecret=YourAnalyticsSecret4 |
|  | SendInterval=60 |

Copy full snippet
```

The `[Analytics]` section is the default one used and is where you should set the name of the default provider module. In the case above, it is set to the IOSApsalar plugin that is part of the 4.5 release. The `ApiKey` and `ApiSecret` fields come from the Apsalar website. Once you create an account, they will give you a key and secret to use.

Once you have it configured for your project, you are ready to start recording analytics events. To get just the basic player retention data, you need to create a session when the game starts up and end it when it is no longer in the foreground. This can be done using the lines of code shown below, or by using the [Blueprint analytics plugin](/documentation/en-us/unreal-engine/blueprint-analytics-plugin-for-unreal-engine):

```
	FAnalytics::Get().GetDefaultConfiguredProvider()->StartSession();
	FAnalytics::Get().GetDefaultConfiguredProvider()->EndSession();
Copy full snippet
```

With those calls as part of your game, you will automatically start gathering player retention data. After getting basic player retention data, you can start adding more events to tell you even more about player behavior in your game.

* [analytics](https://dev.epicgames.com/community/search?query=analytics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
