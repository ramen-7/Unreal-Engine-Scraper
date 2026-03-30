<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-budgeting-using-effect-types-in-niagara-for-unreal-engine?application_version=5.7 -->

# Performance Budgeting Using Effect Types

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Debugging and Optimization in Niagara](/documentation/en-us/unreal-engine/debugging-and-optimization-in-niagara-effects-for-unreal-engine "Debugging and Optimization in Niagara")
7. Performance Budgeting Using Effect Types

# Performance Budgeting Using Effect Types

Use Effect Types to set up ways to improve the performance of your Niagara systems.

![Performance Budgeting Using Effect Types](https://dev.epicgames.com/community/api/documentation/image/8790e138-6dd2-4b6d-ba05-1f95bd0701ef?resizing_type=fill&width=1920&height=335)

 On this page

### When to Use Performance Budgeting

When building a game, you can have a lot of variability in the FX workload depending on the scene composition. Sometimes you may want to take actions to help manage the performance, such as culling instances outside a certain range, or instances that exceed a specified budget usage.

**Effect Type** assets allow you to configure a variety of settings once, then apply them across a collection of Niagara systems.

### How to Create an Effect Type Asset

To create an Effect Type asset, right-click in the **Content Browser** and select **FX > Niagara Effect Type**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24da3446-a6de-44f1-a1d2-e2f88e5bee54/01-create-niagara-effect-type.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24da3446-a6de-44f1-a1d2-e2f88e5bee54/01-create-niagara-effect-type.png)

Click image for full size.

### Effect Type Budgeting Options

In the Effect Type asset, you can set several different methods to cull systems that are exceeding your budget usage. These options are all available under the heading **Budget Scaling**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa4d317d-964e-4cbf-89d9-3d6d93767cec/02-0budget-scaling.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa4d317d-964e-4cbf-89d9-3d6d93767cec/02-0budget-scaling.png)

Click image for full size.

* **Max Global Budget Usage**: This option lets you set up a budget above which any system is culled. You will normally set this to a value between 0 and 1, which represents a percentage from 0-100%. You can set it to 1.5 if you want the system to be more permissive. What this means is, as soon as any system reaches this percentage of your budget, it is culled. This is the best option if you are favoring performance over visuals.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e94dcd5f-ae3c-4818-a2e5-78e60ce34f0f/03-max-global-budget-usage.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e94dcd5f-ae3c-4818-a2e5-78e60ce34f0f/03-max-global-budget-usage.png)

Click image for full size.

* **Max Distance Scale by Global Budget Use**: This option lets you set up a curve to define how the distance at which you cull systems decreases as your budget use increases. For example, if your budget use is very high, then Niagara only renders systems that are close and not those that are far away.
* **Max Instance Count Scale by Global Budget Use**: This option lets you set up a curve that defines how as your budget use increases, the number of instances in your level is scaled down. This scales down all instances of all systems that match this Effect Type.
* **Max System Instance Count Scale by Global Budget Use**: This option lets you set up a curve that defines how as your budget use increases, the number of instances in your level is scaled down. However, in this option, instead of culling all instances in all systems, you are culling a number of instances per system.

For each of those 3 options that take Start X, Start Y, End X, and End Y values, those values define a linearly interpolated curve. Anything above that curve will be culled. For an example, see the following diagram of what the curve would look like.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25b1788f-ca5d-48bf-89df-80056ed22d95/04-distance-and-instances-by-global-budget-usage.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25b1788f-ca5d-48bf-89df-80056ed22d95/04-distance-and-instances-by-global-budget-usage.png)

Click image for full size.

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [When to Use Performance Budgeting](/documentation/en-us/unreal-engine/performance-budgeting-using-effect-types-in-niagara-for-unreal-engine?application_version=5.7#whentouseperformancebudgeting)
* [How to Create an Effect Type Asset](/documentation/en-us/unreal-engine/performance-budgeting-using-effect-types-in-niagara-for-unreal-engine?application_version=5.7#howtocreateaneffecttypeasset)
* [Effect Type Budgeting Options](/documentation/en-us/unreal-engine/performance-budgeting-using-effect-types-in-niagara-for-unreal-engine?application_version=5.7#effecttypebudgetingoptions)
