<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-cooking-insights-in-unreal-engine-5?application_version=5.7 -->

# Unreal Cooking Insights

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
5. [Testing and Optimizing Your Content](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content "Testing and Optimizing Your Content")
6. [Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine "Unreal Insights")
7. [Timing Insights](/documentation/en-us/unreal-engine/timing-insights-in-unreal-engine-5 "Timing Insights")
8. Unreal Cooking Insights

# Unreal Cooking Insights

An overview of profiling your package data using Unreal Cooking Insights

![Unreal Cooking Insights](https://dev.epicgames.com/community/api/documentation/image/5a817327-b093-4a63-b182-4f450d0a3b12?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Cooking Insights** provides you with the ability to gather and display information about the way packages are cooked in your project. Large cooking times can significantly affect the productivity of teams that are working on larger projects. By showing the times it takes to cook each package, this tool can help reduce cooking times.

### Setup

You can run a trace for cooking insights from the command line by using the command:

```
|  |  |
| --- | --- |
|  | trace=default,cook |
|  |  |

Copy full snippet
```

Alternatively, you can run the following command to target a specific host and platform:

```
|  |  |
| --- | --- |
|  | MyProject -run=cook -log -trace=default,cook -tracehost=localhost -targetplatform=Windows |
|  |  |

Copy full snippet
```

When loading a trace that contains cook data, the **Packages** table will be populated with the **load time**, **save time**, and **cooking time** for each package when the analysis is complete.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb121992-fc3b-4ed6-8360-0461501c2a92/packagesview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb121992-fc3b-4ed6-8360-0461501c2a92/packagesview.png)

### Hierarchy Sorting

When selecting the **Hierarchy** filter, you can choose from the following Grouping options.

![hierarchy-sorting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df1edd7a-4141-4924-9de7-17768f0cc88e/hierarchysorting.png)

| **Hierarchy Grouping Option** | **Description** |
| --- | --- |
| Flat (All) | Creates a single group that includes all items. |
| Unique Values - Asset Class | Creates a group for each unique value. |
| Path Breakdown - Package Name | Creates a tree hierarchy out of the path structure of string values. |

### Preset Options

When observing your package data, you can navigate to **Preset** to configure your tree view.

![preset-options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97c55397-fec8-424b-987d-ab6fb315d902/presetoptions.png)

You can choose from the following Presets:

| **Preset Option** | **Description** |
| --- | --- |
| Default | Shows the default packages info. |
| Package Path | Groups packages by the package path. |
| Asset Class | Groups packages by their most important Assets. |

### Column Sorting

Cooking Insights groups specific package data in the following columns.

| **Column Name** | **Description** |
| --- | --- |
| Hierarchy | Hierarchy of the package's tree. |
| Id | The Id of the package. |
| LoadTime | The amount of time it took to load the package. |
| SaveTime | The amount of time it took to save the package. |
| BeginCache | The total time spent in the `BeginCacheForCookedPlatformData` function for the package. |
| IsCachedCooked | The total time spent in the `IsCachedCookedPlatformDataLoaded` function for the package. |
| Asset Class | The class of the most significant Asset in the package. |

You can sort columns into the following sorting categories.

| **Sorting Option** | **Description** |
| --- | --- |
| Sort Ascending | Sort your chosen column in ascending order. |
| Sort Descending | Sort your chosen column in descending order. |
| Sort By | Sort your column by the following values:   * Package Hierarchy * Id * LoadTime * SaveTime * BeginCache * IsCachedCooked * AssetClass |

You can also customize the table by showing and hiding columns individually by using the following options.

| **Column Visibility** | **Description** |
| --- | --- |
| View Column | Hides or shows columns. |
| Show All Columns | Resets the tree view to show all columns. |
| Reset Columns to Default | Resets columns to default. |

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [profiling](https://dev.epicgames.com/community/search?query=profiling)
* [unreal insights](https://dev.epicgames.com/community/search?query=unreal%20insights)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/unreal-cooking-insights-in-unreal-engine-5?application_version=5.7#setup)
* [Hierarchy Sorting](/documentation/en-us/unreal-engine/unreal-cooking-insights-in-unreal-engine-5?application_version=5.7#hierarchysorting)
* [Preset Options](/documentation/en-us/unreal-engine/unreal-cooking-insights-in-unreal-engine-5?application_version=5.7#presetoptions)
* [Column Sorting](/documentation/en-us/unreal-engine/unreal-cooking-insights-in-unreal-engine-5?application_version=5.7#columnsorting)
