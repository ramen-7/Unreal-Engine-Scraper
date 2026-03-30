<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7 -->

# Coding in UE: Blueprint vs. C++

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for Unity Developers](/documentation/en-us/unreal-engine/unreal-engine-for-unity-developers "Unreal Engine for Unity Developers")
7. Coding in UE: Blueprint vs. C++

# Coding in UE: Blueprint vs. C++

Learn the differences between Blueprint and C++ and how to combine them in your project.

![Coding in UE: Blueprint vs. C++](https://dev.epicgames.com/community/api/documentation/image/d5fa44ff-d3b2-4655-9b4d-c89a45277448?resizing_type=fill&width=1920&height=335)

 On this page

You can make an Unreal Engine (UE) project using only Blueprint or C++, but most projects benefit from using a mix of the two. So, how do you decide on the best mix of Blueprint and C++ for your project? This document provides guidance on how to answer that question.

## Programming vs. Scripting

To best know when to use Blueprint or C++, you must first understand the difference between programming and scripting.

* **Programming**: Instructions that define systems.
* **Scripting**: Instructions that define behaviors by interfacing with existing systems.

For example, you might use programming to define a vehicle system that handles the base functionality, such as acceleration and steering, and use scripting to define specific vehicle types, such as cars or boats.

In this context, C++ is a programming language, and Blueprint is a scripting language. However, it's not a clear distinction, as you can use C++ to define behaviors or use Blueprint to define systems. Additionally, there are times in projects where the lines between programming and scripting are blurred, and the best split between the two depends on the scenario.

Blueprint functions as a scripting language by interfacing with exposed UE functionality. Likewise, you can expose your custom functionality to Blueprints. For more information, see [Combining Blueprints and C++](https://dev.epicgames.com/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus).

## Comparing Blueprint and C++

Because every project and team is unique, there is no "right choice" when deciding to use Blueprint or C++, but we recommend considering their strengths before you use them.

### Blueprint Strengths

* **Scripting**: Blueprint can more easily define behaviors.
* **Faster Iteration**: Blueprint is excellent for prototyping as it is quicker to create, modify, compile, and test Blueprint classes.
* **Broader Accessibility**: Blueprint's visual flow representation is easier to understand and use, making it accessible to visually-oriented programmers or non-programmers like designers and artists.
* **Greater Discoverability**: With Blueprint, it's easier to find and include API and asset references.
* **Safer Memory Model**: We designed Blueprints to have a safe memory model to avoid crashes.

### C++ Strengths

* **Programming**: C++ can more easily build new systems.
* **Faster Runtime Performance**: C++ is more performant, but the significance depends on context. See the Performance Concerns section below for more detailed information.
* **Broader Access**: C++ has access to lower-level UE functionality.
* **Broader Extensibility**: With C++, you can create and interface with external systems and libraries.
* **Greater Control**: C++ grants low-level control over systems, resources, and complex algorithms.
* **Smoother Collaboration**: C++ is stored as text, making it easier to diff, merge, and share between projects. However, you can use the [Unreal Diff Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/ue-diff-tool-in-unreal-engine) with Blueprints.
* **Better Scalability**: Large C++ files are easier to modify than large Blueprint graphs.
* **Better Debugging**: There are more powerful debugging tools for C++ than the [Blueprint Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-debugger-in-unreal-engine).

### Performance Concerns

Fundamentally, C++ is more performant than Blueprint because:

* C++ compiles into machine code that executes directly on the CPU.
* Blueprints compile into bytecode that executes on a virtual machine.

This means that Blueprint has additional script execution overhead. However, Blueprint and C++ performance differences are usually insignificant and depend on context. The following examples are contexts where you can expect the most impact:

* Core, low-level infrastructure.
* Tight loops that heavily use I/O or processing resources.
* Systems that process large data sets.
* Tick-dependent classes with many instances.
* Scenarios that benefit from multi-threading, as Blueprint does not support it.

To improve performance, use timers or delegates to schedule work in Blueprints instead of using Tick.

If you use Blueprint and have performance issues, profile your project with [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) and optimize the most significant bottlenecks before considering [converting your Blueprint to C++](https://dev.epicgames.com/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus).

## Combining Blueprint and C++

The best approach to combine Blueprint and C++ is to use C++ as the foundation and build Blueprint classes on top of it. In practice, this means exposing your C++ to be usable from Blueprints.

You can expose C++ to Blueprint with the following methods:

* Create a Blueprint class that extends a C++ class and use [Metadata Specifiers](https://dev.epicgames.com/documentation/en-us/unreal-engine/metadata-specifiers-in-unreal-engine), like `UPROPERTY(BlueprintReadWrite)` or `UFUNCTION(BlueprintCallable)`, to expose specific elements.
* Create a C++ class that extends `UBlueprintFunctionLibrary` to expose the class's static functions.

In some less common cases, you may want to expose Blueprint to C++, which you may do with the following methods:

* Use the `UFUNCTION(BlueprintImplementableEvent)` specifier to define a pure virtual function you must implement in Blueprint.
* Use the `UFUNCTION(BlueprintNativeEvent)` specifier to define a virtual function you can optionally override in Blueprint.
* When creating a user interface, you can access a UserWidget created in Blueprint by using `UPROPERTY(meta=(BindWidget))`.

For more information on these methods, see the following pages:

* [C++ and Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/cpp-and-blueprints-example): A detailed example on creating a Blueprint-extendable C++ class.
* [Exposing C++ to Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/exposing-cplusplus-to-blueprints-visual-scripting-in-unreal-engine): Tips and tricks on writing Blueprint-friendly API.
* [Exposing Gameplay Elements to Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/exposing-gameplay-elements-to-blueprints-visual-scripting-in-unreal-engine): A technical guide for gameplay programmers on exposing gameplay elements to Blueprints.
* [Blueprint Function Library](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-function-libraries-in-unreal-engine): Learn how to use `UBlueprintFunctionLibrary`.
* [Lyra Sample Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine): Learn about the Lyra project, which has examples of each of the methods discussed above.

## Converting Blueprint to C++

If you want to convert your Blueprint to C++, you can start by using [Blueprint Header View](https://dev.epicgames.com/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine) to generate a C++ header file for a Blueprint class or struct. The generated `.h` file contains all the variable and function declarations from your Blueprint, but you must convert your function implementation manually into the matching `.cpp` file.

After converting a Blueprint to C++, you may need to update references to use the new C++ class. If this results in many required updates, consider using [Core Redirects](https://dev.epicgames.com/documentation/en-us/unreal-engine/core-redirects-in-unreal-engine) to remap those references automatically.

* [c++](https://dev.epicgames.com/community/search?query=c++)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Programming vs. Scripting](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#programming-vs-scripting)
* [Comparing Blueprint and C++](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#comparing-blueprint-and-c)
* [Blueprint Strengths](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#blueprint-strengths)
* [C++ Strengths](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#c-strengths)
* [Performance Concerns](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#performance-concerns)
* [Combining Blueprint and C++](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#combining-blueprint-and-c)
* [Converting Blueprint to C++](/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus?application_version=5.7#converting-blueprint-to-c)
