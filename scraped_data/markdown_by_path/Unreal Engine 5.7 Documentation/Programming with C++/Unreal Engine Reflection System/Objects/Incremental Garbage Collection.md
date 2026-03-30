<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine?application_version=5.7 -->

# Incremental Garbage Collection

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
5. [Programming with C++](/documentation/en-us/unreal-engine/programming-with-cplusplus-in-unreal-engine "Programming with C++")
6. [Unreal Engine Reflection System](/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine "Unreal Engine Reflection System")
7. [Objects](/documentation/en-us/unreal-engine/objects-in-unreal-engine "Objects")
8. Incremental Garbage Collection

# Incremental Garbage Collection

Improved garbage collection system for UObjects.

![Incremental Garbage Collection](https://dev.epicgames.com/community/api/documentation/image/eccecd4f-ffcd-42e0-ade4-282789173f88?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

Unreal Engine (UE) uses a mark-and-sweep garbage collector to manage [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/objects-in-unreal-engine) memory. For soft-real-time applications, garbage collectors have historically had one major drawback; the potential to generate gameplay hitches while the garbage collector determines which objects’ memory can be reclaimed. In UE, this process is called **reachability analysis**. UE relies on this phase of garbage collection to complete within a single frame, which temporarily stops all UObject processing (in particular, gameplay). The more objects reachability analysis has to scan, the longer the pause, which can introduce visible gameplay hitches as a result. There are several ways programmers can avoid hitches, such as:

* Keeping tight UObject budgets.
* Using UObject pools.
* Disabling garbage collection during normal gameplay.

However, these workarounds tend to increase code complexity and overall project costs.

## Incremental Reachability Analysis

UE improves upon this using **incremental reachability analysis**. Users now have the ability to split the garbage collector’s reachability analysis phase across multiple frames with a configurable per-frame, soft time limit. The engine tracks UObject references between reachability iterations through `TObjectPtr` properties. This means that any assignment to a `TObjectPtr`-exposed `UPROPERTY` immediately marks the object as reachable while garbage collection is in progress. This is also known as a garbage collector **write barrier**.

The engine has already been converted to use `TObjectPtr` instead of raw C++ pointers in any place that exposes UObjects to the garbage collector, including any UObject or `FGCObject` `AddReferencedObjects` functions. To use incremental reachability analysis in projects built with Unreal Engine, it’s critical to convert all `UPROPERTY` instances to use `TObjectPtr` instead of raw C++ otherwise garbage collection might reclaim some of UObjects’ memory too early. We are initially releasing this feature as experimental, as it’s still possible that the reachability analysis phase can exceed the specified time limit.

## Enable Incremental Reachability Analysis

Incremental reachability analysis can be enabled with the following console variables when added to your project’s `DefaultEngine.ini`:

C++

```
|  |  |
| --- | --- |
|  | [ConsoleVariables] |
|  | gc.AllowIncrementalReachability=1 ; enables Incremental Reachability Analysis |
|  | gc.AllowIncrementalGather=1 ; enables Incremental Gather Unreachable Objects |
|  | gc.IncrementalReachabilityTimeLimit=0.002 ; sets the soft time limit to 2ms |
```

[ConsoleVariables]
gc.AllowIncrementalReachability=1 ; enables Incremental Reachability Analysis
gc.AllowIncrementalGather=1 ; enables Incremental Gather Unreachable Objects
gc.IncrementalReachabilityTimeLimit=0.002 ; sets the soft time limit to 2ms

Copy full snippet(4 lines long)

## Additional Console Variables

You can also use console variables for stress-testing and debugging purposes:

| Console Variable | Description | Type |
| --- | --- | --- |
| `gc.DelayReachabilityIteration` | Delay reachability analysis by the specified number of frames. Used for stress-testing the GC barrier. | `<INTEGER>`: Number of Frames (default: 10) |
| `gc.VerifyNoUnreachableObjects` | Run a test after reachability analysis is complete to make sure no reachable (valid) object is referencing an unreachable (soon to be destroyed) object. | 0: disabled, 1: enabled |
| `gc.ContinuousIncrementalGC` | Keep restarting incremental garbage collection after the previous one has completed. | 0: disabled, 1: enabled |

## Performance Comparison

Below is an [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) visualization of a sample project's performance graph with incremental reachability turned off. The blue line represents the total frame time and the orange line shows the time taken up by reachability analysis. Unreal Insights plots a continuous graph line between single events separated by multiple frames; even though it may seem like garbage collection is running throughout the entire timeline, it only actually runs for a single frame at a time.

In the first image of the following graph comparison, you can see a spike each time garbage collection runs (denoted by the **GC** labels at the top of the timeline).

![Without Incremental Reachability](https://dev.epicgames.com/community/api/documentation/image/ba2d9034-ca00-42a7-bb3d-1de8a66745fb?resizing_type=fit&width=1920&height=1080)

![With Incremental Reachability](https://dev.epicgames.com/community/api/documentation/image/4db3e889-0f33-49aa-84fd-32a1b4a62be4?resizing_type=fit&width=1920&height=1080)

Without Incremental Reachability

With Incremental Reachability

In the second image, with incremental reachability turned on, you can see that the GC lag spikes are gone, and that incremental reachability is now split across multiple frames (represented by the now wider light green bars).

## Known Limitations

Incremental reachability is not fully thread safe. Under some circumstances, an object that is being manipulated on a worker thread will not be marked as reachable while the garbage collector is scanning the UObject graph. This can result in the object being garbage collected prematurely. We recommend enabling incremental reachability in single-threaded builds only (for example, dedicated servers).

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [c++](https://dev.epicgames.com/community/search?query=c++)
* [uobject](https://dev.epicgames.com/community/search?query=uobject)
* [garbage collection](https://dev.epicgames.com/community/search?query=garbage%20collection)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Incremental Reachability Analysis](/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine?application_version=5.7#incremental-reachability-analysis)
* [Enable Incremental Reachability Analysis](/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine?application_version=5.7#enable-incremental-reachability-analysis)
* [Additional Console Variables](/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine?application_version=5.7#additional-console-variables)
* [Performance Comparison](/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine?application_version=5.7#performance-comparison)
* [Known Limitations](/documentation/en-us/unreal-engine/incremental-garbage-collection-in-unreal-engine?application_version=5.7#knownlimitations)
