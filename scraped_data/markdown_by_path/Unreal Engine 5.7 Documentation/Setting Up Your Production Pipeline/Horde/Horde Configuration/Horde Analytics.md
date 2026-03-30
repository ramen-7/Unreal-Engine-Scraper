<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-analytics-for-unreal-engine?application_version=5.7 -->

# Horde Analytics

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
7. [Horde Configuration](/documentation/en-us/unreal-engine/horde-configuration-for-unreal-engine "Horde Configuration")
8. Horde Analytics

# Horde Analytics

An overview of Horde Analytics.

![Horde Analytics](https://dev.epicgames.com/community/api/documentation/image/06767e0d-fcfb-4163-b7bd-b648068a5bd9?resizing_type=fill&width=1920&height=335)

 On this page

Horde implements HTTP endpoints to collect telemetry data sent by Unreal Editor. This data can provide insights into bottlenecks and workflow issues that a team and the Horde dashboard can aggregate and chart it to highlight improvements and regressions over time.

The [Getting Started > Analytics](/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine) guide explains how to configure a project to send telemetry data to Horde.

## Telemetry Stores

Horde supports multiple orthogonal telemetry stores, allowing you to group telemetry data for different projects as you see fit. Each telemetry store has its own set of metrics, and the dashboard allows switching contexts to view the same charts using data from different stores.

To send data to a particular telemetry store, include the telemetry store name in the `APIEndpointET` property in the project's `DefaultEngine.ini` file. The `engine` store uses the following URL, for example:

```
APIEndpointET="api/v1/telemetry/engine"
Copy full snippet
```

## Metrics

To provide efficient aggregation of analytics data over large time periods, Horde aggregates telemetry events into running metrics for each time interval. This aggregation is performed according to rules specified in the `Telemetry.Metrics` section of the globals.json file (see [MetricConfig](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#metricconfig)).

## Charting

The Horde dashboard render charts showing metrics collected on the server. These views are configured using the `Dashboard.Analytics` section of the globals.json file (see [TelemetryViewConfig](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#telemetryviewconfig)).

## Telemetry Sinks

Horde can collect raw telemetry data in its own database as well as forwarding it to other telemetry sinks.

You can configure telemetry sinks through the `Telemetry` property in the server's [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file. It is not necessary to configure a telemetry sink in order to compute metrics from aggregated data.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Telemetry Stores](/documentation/en-us/unreal-engine/horde-analytics-for-unreal-engine?application_version=5.7#telemetrystores)
* [Metrics](/documentation/en-us/unreal-engine/horde-analytics-for-unreal-engine?application_version=5.7#metrics)
* [Charting](/documentation/en-us/unreal-engine/horde-analytics-for-unreal-engine?application_version=5.7#charting)
* [Telemetry Sinks](/documentation/en-us/unreal-engine/horde-analytics-for-unreal-engine?application_version=5.7#telemetrysinks)
