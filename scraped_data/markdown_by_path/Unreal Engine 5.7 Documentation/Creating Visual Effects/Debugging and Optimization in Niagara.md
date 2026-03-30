<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-and-optimization-in-niagara-effects-for-unreal-engine?application_version=5.7 -->

# Debugging and Optimization in Niagara

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
6. Debugging and Optimization in Niagara

# Debugging and Optimization in Niagara

Learn how to debug and optimize your Niagara simulations.

![Debugging and Optimization in Niagara](https://dev.epicgames.com/community/api/documentation/image/9ed4e098-7189-4d09-b029-849256dac740?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine provides several different tools you can use to help debug what's going on in your simulations.

## Optimizing your Niagara System

[![Optimizing Niagara](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05e05782-3238-4f65-896e-a4fe5dd92b07/niagara-measure-perf-topic.png)

Optimizing Niagara

Learn how to optimize your Niagara systems in Unreal Engine.](/documentation/en-us/unreal-engine/optimizing-niagara)

## Niagara Debugger

If you need to further debug Niagara simulations after they've been added to your level, then you can use the **Niagara Debugger**. This lets you turn on a heads-up display (HUD) that outputs detailed information about the simulations in your level, such as the number of particles being generated, the amount of memory being used, and more. You can also capture a snapshot of information and then analyze that output.

[![Niagara Debugger](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba6361bb-664a-4f39-b94d-f2679d271042/topic-image.png)

Niagara Debugger

Use the Niagara Debugger to analyze your Niagara systems in a level.](/documentation/en-us/unreal-engine/niagara-debugger-for-unreal-engine)

## Performance Budgeting Using Effect Types

Create a new type of asset called a Niagara Effect Type to configure a variety of settings to help you manage budgeting in your level. Any Niagara Systems that use this Effect Type will inherit the rules you set. This way, you can improve performance by, for example, culling systems that are a certain distance away.

[![Performance Budgeting Using Effect Types](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0855f9ad-ea16-4263-bc62-56990301cbe4/performance-budgeting-topic-image.png)

Performance Budgeting Using Effect Types

Use Effect Types to set up ways to improve the performance of your Niagara systems.](/documentation/en-us/unreal-engine/performance-budgeting-using-effect-types-in-niagara-for-unreal-engine)

## How to Fix a GPU Crash

As some Niagara simulations can be graphically intensive, working in those scenes in Windows could cause a GPU crash. Visit this page to find out more about how to resolve it.

[![Dealing with a GPU Crash](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cebe7a8b-0645-435f-9aea-a22de532be8c/fix-a-gpu-crash-topic.png)

Dealing with a GPU Crash

An overview of investigating, resolving, and reporting GPU Crashes in Unreal Engine.](/documentation/en-us/unreal-engine/dealing-with-a-gpu-crash-when-using-unreal-engine)

* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Optimizing your Niagara System](/documentation/en-us/unreal-engine/debugging-and-optimization-in-niagara-effects-for-unreal-engine?application_version=5.7#optimizingyourniagarasystem)
* [Niagara Debugger](/documentation/en-us/unreal-engine/debugging-and-optimization-in-niagara-effects-for-unreal-engine?application_version=5.7#niagaradebugger)
* [Performance Budgeting Using Effect Types](/documentation/en-us/unreal-engine/debugging-and-optimization-in-niagara-effects-for-unreal-engine?application_version=5.7#performancebudgetingusingeffecttypes)
* [How to Fix a GPU Crash](/documentation/en-us/unreal-engine/debugging-and-optimization-in-niagara-effects-for-unreal-engine?application_version=5.7#howtofixagpucrash)
