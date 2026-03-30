<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde Analytics Tutorial

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine "Horde")
7. [Horde Tutorials](/documentation/en-us/unreal-engine/horde-tutorials-for-unreal-engine "Horde Tutorials")
8. Horde Analytics Tutorial

# Horde Analytics Tutorial

A tutorial for using Horde analytics with Unreal Engine.

![Horde Analytics Tutorial](https://dev.epicgames.com/community/api/documentation/image/5956be9f-b6b5-4910-b05f-66f8a1983f6a?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

**Horde** implements a telemetry collector which can receive and process events sent by the Unreal Editor.

Horde aggregates telemetry events into **metrics** for discrete time intervals, which can then be charted by the Horde dashboard to give valuable insights into the bottlenecks experienced by your team.

![Analytics](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b3f576fd-ab23-4400-b312-07ed449281c4/analytics-main.png)

## Prerequisites

* Horde Server installation (see [Getting Started: Install Horde](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine)).
* An Unreal Engine project targetting Unreal Engine 5.5 or later.

## Steps

1. Open your project in the Unreal Editor and go to the `Edit > Plugins` menu. Search for the `Studio Telemetry` plugin and make sure it is enabled. It should be enabled by default.
2. Open your project's `DefaultEngine.ini` file (in the `Config` folder next to your `.uproject` file) and add the following lines:

   ```
        [StudioTelemetry.Provider.HordeAnalytics]
        Name=HordeAnalytics
        ProviderModule=AnalyticsET
        UsageType=EditorAndClient
        APIKeyET=HordeAnalytics.Dev
        APIServerET="http://localhost:13340/"
        APIEndpointET="api/v1/telemetry/engine"
   Copy full snippet
   ```

   Make sure to replace the value for `APIServerET` with the address of your Horde Server.
3. Configure a telemetry store to aggregate metrics from your telemetry events. There are some default metrics and charts included with the Horde installation, which can be added by adding the following snippet to your [globals.json](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine) file:

   ```
            // Define the 'Engine' telemetry store and create some standard metrics within it.
            "telemetryStores": [
                {
                    "id": "engine",
                    "include": [
                        {
                            "path": "$(HordeDir)/Defaults/default-metrics.telemetry.json"
                        }
                    ]
                }
            ],
   		
            // Configure a default dashboard to render them
            "dashboard": {
                "include": [
                    {
                        "path": "$(HordeDir)/Defaults/default-analytics.dashboard.json"
                    }
                ]
            },
   Copy full snippet
   ```

## See Also

* [Configuration > Analytics](/documentation/en-us/unreal-engine/horde-analytics-for-unreal-engine)

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Prerequisites](/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine?application_version=5.7#prerequisites)
* [Steps](/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine?application_version=5.7#steps)
* [See Also](/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine?application_version=5.7#seealso)
