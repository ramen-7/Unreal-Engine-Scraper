<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7 -->

# Animation Budget Allocator

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Animation Debugging and Optimization](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine "Animation Debugging and Optimization")
8. Animation Budget Allocator

# Animation Budget Allocator

System for constraining the time taken for animation data by dynamically throttling Skeletal Mesh Component ticking.

![Animation Budget Allocator](https://dev.epicgames.com/community/api/documentation/image/cfd96006-6638-46f0-85fa-8cb85b428a3e?resizing_type=fill&width=1920&height=335)

 On this page

The **Animation Budget Allocator** is a plugin, you can use in **Unreal Engine**, to constrain the computation time allotted for animation data running on specified skeletal meshes. You can use the Animation Budget allocator to reduce the cost of many animating characters, by setting a processing budget, that the Budget Allocator will dynamically throttle Skeletal Mesh Component animation ticking. By setting a fixed CPU budget for animation data, you can maximizing perceived animation quality with minimal system overhead when animating many characters at once.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e77d7cb4-01ec-4de8-a163-a98d489369e7/bademo.gif)

The Animation Budget Allocator determines a fixed budget, that can be adjusted on a per-platform basis, in milliseconds of work to perform on the **game thread**. The Budget Allocator then determines if it can update all necessary animation updates, or if optimiziation are needed. If optimizations are required, the Budget Allocator determines the Significance of the requested updates, and identifies targets, based on several criteria, with the goal of dynamically adjusting the load to fit within the fixed **game thread** budget.

The following are targeted areas the Budget Allocator makes optimizations to reduce the performance load:

* Stop ticking on individual skeletal mesh components, and favors any present Leader Pose Component.
* Performs animation updates at a lower rate.
* Chooses whether or not to **Interpolate** between updates.

#### Prerequisites

* Enable the Animation Budget Allocator [Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine). Navigate in the **Menu Bar** to **Edit** > **Plugins** and locate the **Animation Budget Allocator**, listed under the **Animation** section, or by using the Search Bar. Enable the Plugin and restart the editor.
* ![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23ec16c4-8135-49df-ab0b-887ea1534809/enableplugin.png)
* A Skeletal Mesh character with a character blueprint.
* An animation to play on the character.

## Set Up the Animation Budget Allocator

In order to take advantage of the Animation Blueprint Allocator, you must set the character blueprint's mesh component's **Component Class** to use the **SkeletalMeshComponentBudgeted** class.

To set the character's component class, navigate in the character's blueprint to the **Components** panel and select the Mesh component to open the **Details** panel. Set the **Component Class** property to the **SkeletalMeshComponentBudgeted** option from the drop-down menu.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcd85dd9-9cc4-4a0e-860b-a207c444f7af/setclass.png)


Alternativly, you can also add the following C++ code to your `ACharacter` subclass constructor:

`: Super(ObjectInitializer.SetDefaultSubobjectClass<USkeletalMeshComponentBudgeted>(ACharacter::MeshComponentName))`

In the Budgeting section enable **Auto Calculate Significance** and ensure **Auto Register with Budget Allocator** is enabled.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8b16d6b-1753-4047-81ee-5e878efa712b/extras.png)

Create and connect the **Enable Animation Budget** node to the **Event Begin Play** node in the Character's Blueprint Event Graph, and check the **Enabled** property.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/835d8757-6eff-4a0c-9355-c983be52e090/node.png)

You can now add the character blueprint to the level, by dragging the asset from the **Content Browser** into the level **viewport**, or by spawning the character using blueprints. The Budget Allocator will be enabled by default when beginning the simulation. You can observe the processing load, using the graph that is rendered over the scene in the viewport.

Both the Enable Animation Blueprint Budget node and the feature must be enabled for the budget allocator to operate. By default the feature is enabled, but can be toggled using the `a.Budget.Enabled` console command during simulation. You can enter a console command using the backtik (`) key, and input the command in the field.

You can toggle the Animation Budget Allocator's debug overlay, to observe its operations in real-time during your project's simulation with the `a.Budget.Debug.Enabled` console command.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e22f346-84ee-4f51-8b7f-ddb9fe666b7f/overview.png)

## Using the Animation Budget Allocator

The Animation Budget Allocator impliments optimizations to being the total animation processing load within the budget, while retaining the maximize animation quality that the system can produce. It will favor the closest, most significant meshes, running their animations at the highest framerate it can while reducing the framerate and quality of less significant meshes.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/67ee917f-6836-48a1-8e41-7bd528b13b23/graphoverview.png)

The Animation Budget Allocator's debug graph observes the project's processing load, along the y-axis, over time, along the graph's x-axis, and updates in real-time. The project's budget for the total animation system is rendered as the dotted line and is labeled **Budget**, along the right side of the graph.

The solid line represents the **Performance** of the animation system at the individual moments along the graphs observed time.

The performance will vary based on the amount of work that needs to be done, when factoring in the Animation Budget Allocator's chosen optimizations.

You can view additional information about the processes of the Budget Allocator by enabling the **stat overlay**. To enable the stat overlay, navigate in the viewport menu to **Stat** > **Advanced** and toggle the **AnimationBudgetAllocator** option.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7fa169e-152f-4d6c-8949-6f6b1ca6539d/openstatoverlay.png)

You can now view additional information when beginning the project simulation.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb1f0b22-1406-44b3-9d66-1d347bea19db/stats.png)

Here you can reference a list of the information present the Animation Budget Allocator's stat overlay:

| Statistic | Description |
| --- | --- |
| **Initial Tick** | You can use the Initial Tick to observe the initial tick stats when the budget allocator is activated. Using this category you can observe the initial tick's Inclusive Average, Inclusive Max, Exclusive Average and Exclusive Max times in milliseconds (ms). |
| **Demand** | Here you can observe the demand the Budget Allocator is being operated with. You can observe the Average, Maximum (Max) and Minimum (Min) number of objects that the Budget Allocator is processing. |
| **Num Registered Components** | Here you can observe the number of registered skeletal mesh components the Budget Allocator is processing, including the multiple skeletal mesh components that comprise [modular characters](/documentation/en-us/unreal-engine/working-with-modular-characters-in-unreal-engine). You can observe the Average, Maximum (Max) and Minimum (Min) number of skeletal mesh objects. |
| **Throttled** | Here you can observe the number of throttled skeletal mesh objects the Budget Allocator is optimizing. You can observe the Average, Maximum (Max) and Minimum (Min) number of skeletal mesh objects. |
| **Num Ticked Components** | Here you can observe the number of skeletal mesh objects the Budget Allocator is optimizing per tick. You can observe the Average, Maximum (Max) and Minimum (Min) number of skeletal mesh objects. |
| **Budget** | Here you can observe the number of skeletal mesh objects the Budget Allocator is able to optimize per tick. You can observe the Average, Maximum (Max) and Minimum (Min) number of skeletal mesh objects. |
| **Interpolated** | Here you can observe the number of skeletal mesh objects the Budget Allocator is choosing to interpolate rather than render actual animation frames. You can observe the Average, Maximum (Max) and Minimum (Min) number of skeletal mesh objects. |
| **SmoothedBudgetPressure** | Here you can observe the Budget Allocator's smoothing budget pressure, or the amount of pressure to choose interpolation over animation frame selection. |
| **Always Tick** | Here you can observe the Always Tick's status, and fall off times. Always Tick bypasses the budget allocators processing to allow the mesh to always update its animation data. |
| **Average Work Units (ms)** | Here you can observe the time each process cycle takes to complete in milliseconds (ms). You can observe the Average, Maximum (Max) and Minimum (Min) clock times. |

Each Skeletal Meshes that is being optimized with the Animation Budget Allocator will be rendered with a unique overlay containing debug information.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf36f685-0410-483a-8531-982b6f587f67/uniquecharoverlay.png)

The number value indicates the rate at which the mesh is being updated. A value of one means that the mesh is being updated and ticking every frame. A value of five would mean that the mesh is updated and tick every five frames.

The other present information indicates at what fidelity the animation data is being processed. The following are the options the Animation Budget Allocator will process animation data:

* **Hi** (high detail) - the Skeletal Mesh components and running more expensive logic.
* **Lo** (low detail) - that expensive logic (such as extra character parts or more expensive work that can be skipped at a distance) is not running.
* **I** (interpolating) - the Skeletal Mesh is interpolating between frames.

When using [Modular Characters](/documentation/en-us/unreal-engine/working-with-modular-characters-in-unreal-engine), you can view individual groups of debug information for each skeletal mesh component that comprises the modular character.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7893f5ee-3009-4c68-a5fb-6d22283b19f6/budgetedchar.png)

### Platform Scaling

When developing Unreal Engine projects for multiple platforms, you can control the Animation Budget Allocator's settings on a per-platform basis.

In most cases, it is recommended to set the `cvar` inputs to the system from the [scalability settings](/documentation/404) for the specific platforms that you are targeting.

For example, you can add a `DefaultScalability.ini` file to set the budget for the Animation Budget Allocator's target budget, based on the **View Distance Quality** setting:

```
	[ViewDistanceQuality@0]
	a.Budget.BudgetMs=1.0
Copy full snippet
```

```
	[ViewDistanceQuality@1]
	a.Budget.BudgetMs=1.5
Copy full snippet
```

```
	[ViewDistanceQuality@2]
	a.Budget.BudgetMs=2.0
Copy full snippet
```

```
	[ViewDistanceQuality@3]
	a.Budget.BudgetMs=2.5

Copy full snippet
```

You can then override these values within the platform specific scalability settings.

For more information about creating profiles for specific platforms see the [Customizing Device Profiles and Scalability for Android](/documentation/en-us/unreal-engine/customizing-device-profiles-and-scalability-in-unreal-engine-projects-for-android) for an example of building a profile for android devices.

## Animation Budget Allocator C++ API

You can access the C++ files for Animation Budget Allocator within your project `Engine` installation folder under:

`Engine\Plugins\Runtime\AnimationBudgetAllocator\Source\AnimationBudgetAllocator\Public\`

Here you can reference the `IAnimationBudgetAllocator.h` file:

```
	// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.

	#pragma once

	class USkeletalMeshComponentBudgeted;

	class UWorld;

	struct FAnimationBudgetAllocatorParameters;

	/**

	* Dynamically manages skeletal mesh component tick rates to try to maintain a specified budget.

	*/

	class IAnimationBudgetAllocator

	{

	public:

		/** Get the budgeter for the specified world */

		static ANIMATIONBUDGETALLOCATOR_API IAnimationBudgetAllocator* Get(UWorld* InWorld);

		/**

		* Register a component with the budgeter system. If the component is already registered this function does nothing.

		* Once this is called:

		* - Default tick function will be disabled

		* - URO will be disabled

		* - Parallel anim tasks will be re-routed to the budgeter

		*/

		virtual void RegisterComponent(USkeletalMeshComponentBudgeted* InComponent) = 0;

		/**

		* Unregister a component from the budgeter system. If the component is not registered this function does nothing.

		* Once this is called:

		* - Default tick function will be re-enabled

		* - URO will be re-enabled

		* - Parallel anim tasks will be re-routed back to internal functions

		*/

		virtual void UnregisterComponent(USkeletalMeshComponentBudgeted* InComponent) = 0;

		/**

		* Update the prerequisites of this component. Should be called when prerequisites may have changed externally.

		*/

		virtual void UpdateComponentTickPrerequsites(USkeletalMeshComponentBudgeted* InComponent) = 0;

		/**

		* Set the significance and other flags for the specified component.

		* This information is used to dynamically control the tick rate of the component.

		*/

		virtual void SetComponentSignificance(USkeletalMeshComponentBudgeted* Component, float Significance, bool bNeverSkip = false, bool bTickEvenIfNotRendered = false, bool bAllowReducedWork = true, bool bForceInterpolate = false) = 0;

		/** Set the specified component to tick or not. If the budgeter is disabled then this calls Component->SetComponentTickEnabled(bShouldTick). */

		virtual void SetComponentTickEnabled(USkeletalMeshComponentBudgeted* Component, bool bShouldTick) = 0;

		/** Get whether the specified component is set to tick or not */

		virtual bool IsComponentTickEnabled(USkeletalMeshComponentBudgeted* Component) const = 0;

		/** Inform that we reduced work for a component */

		virtual void SetIsRunningReducedWork(USkeletalMeshComponentBudgeted* Component, bool bInReducedWork) = 0;

		/** Set the tick time */

		virtual void SetGameThreadLastTickTimeMs(int32 InManagerHandle, float InGameThreadLastTickTimeMs) = 0;

		/** Set the completion task time */

		virtual void SetGameThreadLastCompletionTimeMs(int32 InManagerHandle, float InGameThreadLastCompletionTimeMs) = 0;

		/** Tick the system per-frame */

		virtual void Update(float DeltaSeconds) = 0;

		/** Set whether this budget allocator is enabled */

		virtual void SetEnabled(bool bInEnabled) = 0;

		/** Get whether this budget allocator is enabled */

		virtual bool GetEnabled() const = 0;

		/** Set the various parameters */

		virtual void SetParameters(const FAnimationBudgetAllocatorParameters& InParameters) = 0;

		};

Copy full snippet
```

## Additional Console Commands

Here you can reference a list of the available console commands you can use when working with the Animation Budget Allocator, and a description of their functionality:

| Command | Values | Description |
| --- | --- | --- |
| `a.Budget.AlwaysTickFalloffAggression` | Range [0.1, 0.9], Default = 0.8 | Controls the rate at which `always ticked' components fall off under load. Higher values mean that we reduce the number of always ticking components by a larger amount when the allocated time budget is exceeded. |

|  |  |  |
| --- | --- | --- |
| `a.Budget.BudgetFactorBeforeAggressiveReducedWork` | Range > 1, Default = 2.0 | Reduced work will be applied more rapidly when budget pressure goes over this amount. |
| `a.Budget.BudgetFactorBeforeReduceWork` | Range > 1, Default = 1.5 | Reduced work will be delayed until budget pressure goes over this amount. |
| `a.Budget.BudgetFactorBeforeReducedWorkEpsilon` | Range > 0.0, Default = 0.25 | Increased work will be delayed until budget pressure goes under `a.Budget.BudgetFactorBeforeReducedWork`'s value minus this command's value. |
| `a.Budget.BudgetMs` | Values > 0.1, Default = 1.0 | The time in milliseconds that we allocate for Skeletal Mesh work to be performed. When over budget, various other console variables come into play, such as `a.Budget.AlwaysTickFalloffAggression` and `a.Budget.InterpolationFalloffAggression`. |
| `a.Budget.BudgetPressureSmoothingSpeed` | Range > 0.0, Default = 3.0 | How much to smooth the budget pressure value that is used to throttle reduced work. |
| `a.Budget.Debug.Enabled` | Values: 0/1 | Controls whether to render the Animation Budget Allocator's debug graph in the viewport, in builds that it is supported. |
| `a.Budget.Debug.Force` | Values: 0/1 | Enables overriding the budget settings on all meshes to specific values. |
| `a.Budget.Debug.Force.Interp` | Values: 0/1 | Toggle interpolation, when `a.Budget.Debug.Force` is enabled. A value of 1 will enable interpolation, and a value of 0 will disable interpolation. |
| `a.Budget.Debug.Force.Rate` | Values: > 0 | Overides the number of frames per animation tick, when `a.Budget.Debug.Force` is enabled. For example, a vaule of 5 means animations will be updated once every 5 frames. |
| `a.Budget.BudgetMs` | Values: > 0.0 | Lowers the threshold for the budgeter to take effect on your animation system, when `a.Budget.Debug.Force` is enabled. For example, a value of 0.1 will greatly reduce the threshold of when the budgeter will take effect. |
| `a.Budget.Debug.ShowAddresses` | Values: 0/1 | Controls whether the debug render also displays addresses of component data. |
| `a.Budget.Enabled` | Values: 0/1 | Controls whether the Skeletal Mesh batching system is enabled. Should be set when there are no running Skeletal Meshes. |
| `a.Budget.GBudgetPressureBeforeEmergencyReducedWork` | Range: > 0.0, Default = 2.5 | Controls the budget pressure where emergency reduced work (applied to all components except those that are bAlwaysTick). |
| `a.Budget.InitialEstimatedWorkUnitTime` | Values: > 0.0, Default = 0.08 | Controls the time in milliseconds we expect, on average, for a Skeletal Mesh component to execute.The value only applies for the first tick of a component, after which we use the real time the tick takes. |
| `a.Budget.InterpolationFalloffAggression` | Range [0.1, 0.9], Default = 0.4 | Controls the rate at which interpolated components falloff under load. Higher values mean that we reduce the number of interpolated components by a larger amount when the allocated time budget is exceeded. Components are only interpolated when the time budget is exceeded. |
| `a.Budget.InterpolationMaxRate` | Values > 1, Default = 6 | Controls the rate at which ticks happen when interpolating. |
| `a.Budget.InterpolationTickMultiplier` | Range [0.1, 0.9], Default = 0.75 | Controls the expected value an amortized interpolated tick will take compared to a 'normal' tick. |
| `a.Budget.MaxInterpolatedComponents` | Range >= 0, Default = 16 | Max number of components to interpolate before we start throttling. |
| `a.Budget.MaxTickedOffsreen` | Values >= 1, Default = 4 | The maximum number of off screen components we tick (most significant first). |
| `a.Budget.MaxTickRate` | Values >= 1, Default = 10 | The maximum tick rate we allow. If this is set then we can potentially go over budget but keep the quality of individual meshes to a reasonable level. |
| `a.Budget.MinQuality` | Values [0.0, 1.0], Default = 0.0 | The minimum quality metric allowed. Quality is determined simply by NumComponentsTickingThisFrame / NumComponentsThatWeNeedToTick. If this is anything other than 0.0 then we can potentially go over our time budget. |
| `a.Budget.ReducedWorkThrottleMaxInFrames` | Range [1, 255], Default = 20 | Prevents reduced work from changing too often due to system and load noise. Max value used when under budget pressure. |
| `a.Budget.ReducedWorkThrottleMaxPerFrame` | Range [1, 255], Default = 4 | Controls the max number of components that are switched to/from reduced work per tick. |
| `a.Budget.ReducedWorkThrottleMinInFrames` | Range [1, 255], Default = 2 | Prevents reduced work from changing too often due to system and load noise. Min value used when over budget pressure (for example: aggressive reduction). |
| `a.Budget.StateChangeThrottleInFrames` | Range [1, 128], Default = 30 | Prevents throttle values from changing too often due to system and load noise. |
| `a.Budget.WorkUnitSmoothingSpeed` | Values > 0.1, Default = 5.0 | The speed at which the average work unit converges on the measured amount. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7#prerequisites)
* [Set Up the Animation Budget Allocator](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7#setuptheanimationbudgetallocator)
* [Using the Animation Budget Allocator](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7#usingtheanimationbudgetallocator)
* [Platform Scaling](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7#platformscaling)
* [Animation Budget Allocator C++ API](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7#animationbudgetallocatorc++api)
* [Additional Console Commands](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine?application_version=5.7#additionalconsolecommands)
