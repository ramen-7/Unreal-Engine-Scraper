<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7 -->

# Animation Debugging and Optimization

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
7. Animation Debugging and Optimization

# Animation Debugging and Optimization

Explore documentation about Unreal Engine's tools and techniques you can use to debug and optimize your animation system.

![Animation Debugging and Optimization](https://dev.epicgames.com/community/api/documentation/image/406c913e-3e6c-4713-8679-66f4362bdf35?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** features a suite of debugging and optimizations tools and techniques you can use to streamline your project's animation system, to increase performance and reduce file sizes. In the following document you can read about tools and features you can use to polish and refine your animation system in Unreal Engine.

## Debugging Tools

Unreal Engine features a few debugging tools you can use to analyze your animation system in a controlled environment to make adjustments and find solutions to problems.

### Rewind Debugger

With the [Rewind Debugger](/documentation/en-us/unreal-engine/animation-rewind-debugger-in-unreal-engine) you can record segments of your project's **Play In Editor** (**PIE**) gameplay, then using the visual timeline-based interface, scrub through the recording in real time to observe transition behaviors, variable values, pose blends and more. Recorded gameplay provides a more stable working than traditional simulation, and can preserve incorrect animation behavior for easier collaboration and debugging.

For more information on debugging animation systems with the **Rewind Debugger**, see the following documentation:

[![Rewind Debugger](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36d20a20-1277-48ac-81aa-682c6c8baa6b/topicimage.png)

Rewind Debugger

With the Rewind Debugger you can record real-time segments of projects and preserve the data for debugging workflows.](/documentation/en-us/unreal-engine/animation-rewind-debugger-in-unreal-engine)

### Animation Insights

You can use the [Animation Insights](/documentation/en-us/unreal-engine/animation-insights-in-unreal-engine) [Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) to profile your project's animation system, to see a visual graph of all operations over time. You can use this graph to determine what animation processes are being evaluated, how much performance budget they use, and when, to make informed optimization choices to achieve your project's desired performance quality.

For more information about profiling animation systems with **Animation Insights**, see the following documentation:

[![Animation Insights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9402c03d-2549-4e05-aaa2-cd5127154219/topicimage.png)

Animation Insights

Use the Animation Insights to observe and profile your project's gameplay and animation performance during runtime.](/documentation/en-us/unreal-engine/animation-insights-in-unreal-engine)

### Pose Watch

You can use [Pose Watching](/documentation/en-us/unreal-engine/animation-shortcuts-and-tips-unreal-engine#posewatch) to toggle dynamic visual debug renders in the viewport during project simulation of individual animation data sources, when working with complex Animation Blueprints and layered animation systems. When rendering individual animation sources you can visually isolate each node's or layer's influence on the final output pose, to determine the source of bugs or irregular animation behavior in your animation system.

For more information about debugging animation systems with **Pose Watching**, refer to the following documentation:

[![Animation Shortcuts and Tips](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55219fe2-b36b-494f-8cfd-ad4dab4b6125/topicimage.png)

Animation Shortcuts and Tips

Workflow shortcuts and tips for animators and animation programmers in Unreal Engine.](/documentation/en-us/unreal-engine/animation-shortcuts-and-tips-unreal-engine)

## Animation Optimization

You can use [Animation Optimization](/documentation/en-us/unreal-engine/animation-optimization-in-unreal-engine) techniques and features to improve your animation system's performance and quality, as well as reduce file sizes.

For more information about **Animation Optimization** in Unreal Engine, see the following documentation:

[![Animation Optimization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdda0a1c-2467-4d64-89b6-d7d1f36a2c23/topicimage.png)

Animation Optimization

Use a variety of methods and techniques to optimize Animation Blueprint's performance and stability.](/documentation/en-us/unreal-engine/animation-optimization-in-unreal-engine)

### Animation Budget Allocator

The [Animation Budget Allocator](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine) is a [Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) for Unreal Engine, that you can use to throttle animation evaluation and quality, on multiple characters to reduce the performance cost of your projects entire animation system.

For more information about optimizing animation systems with the **Animation Budget Allocator**, see the following documentation:

[![Animation Budget Allocator](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b966ca08-3511-431b-905f-76271fc106c3/topicimage.png)

Animation Budget Allocator

System for constraining the time taken for animation data by dynamically throttling Skeletal Mesh Component ticking.](/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [debugging](https://dev.epicgames.com/community/search?query=debugging)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Debugging Tools](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7#debuggingtools)
* [Rewind Debugger](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7#rewinddebugger)
* [Animation Insights](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7#animationinsights)
* [Pose Watch](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7#posewatch)
* [Animation Optimization](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7#animationoptimization)
* [Animation Budget Allocator](/documentation/en-us/unreal-engine/animation-debugging-and-optimization-in-unreal-engine?application_version=5.7#animationbudgetallocator)

Related documents

[Unreal Insights

![Unreal Insights](https://dev.epicgames.com/community/api/documentation/image/b6bb65f0-31be-40d7-8592-c8e0dedb4909?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine)
