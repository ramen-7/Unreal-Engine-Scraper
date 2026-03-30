<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7 -->

# Frequently Asked Questions

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
7. Frequently Asked Questions

# Frequently Asked Questions

Frequently Asked Questions (FAQ) for developers moving from Unity to Unreal Engine.

![Frequently Asked Questions](https://dev.epicgames.com/community/api/documentation/image/64e5990a-4dff-414d-9767-a7528d6815d7?resizing_type=fill&width=1920&height=335)

 On this page

### How do I load my last project automatically?

You can configure Unreal Engine to load the last project you were working on automatically on startup. When you open a project from the Epic Launcher, enable the **Always Load Last Project on Startup** option on the Unreal Engine start screen.

[![](https://dev.epicgames.com/community/api/documentation/image/f657b1ca-6fdd-4841-a32b-77c130e7ca92?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f657b1ca-6fdd-4841-a32b-77c130e7ca92?resizing_type=fit)

### Where do I set input bindings for my game?

In Unity, you used the Input Manager settings for your project to set up default bindings.

In Unreal Engine, you configure input bindings from the **Project Settings** window, in the **Input** category. In this window, you can add various buttons (actions) and analog controls (axes). Give each control a name and default binding. Once you do that, you can get callbacks to your game's Pawn when input events are triggered.

To learn more about how to set up input for your Unreal Engine project, refer to the [Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine) page.

If your project requires more advanced input features, like complex input handling or runtime control remapping, consider using the **Enhanced Input** plugin. For more information, see [Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine).

### How do I change the starting scene of my project?

By default, Unreal Engine loads the default Level of your project when you open it. You can change this behavior in the **Editor Preferences** window (main menu: **Edit > Editor Preferences**), in the **General > Loading & Saving** category.

### How do I run my game?

There are several ways to play-test (run) your game:

* Directly in the Unreal Editor, by clicking the **Play** button on the **Main Toolbar**.
* As a standalone process, by clicking the **Platforms** button on the **Main Toolbar**, then selecting your machine from the drop-down list. Note that this will first build an executable for your platform; for example, if you are working on a Windows machine, this will build a Windows executable.
* On a different platform (for example, a mobile device or web browser), by clicking the **Platforms** button on the **Main Toolbar**, then selecting the platform you want to run your game on. Note that you will need to install all required dependencies first.

To learn more about running your Unreal Engine game on different platforms, refer to the following pages:

* [Playing and Simulating](https://dev.epicgames.com/documentation/en-us/unreal-engine/playing-and-simulating-in-unreal-engine)
* [Managing Platforms in Unreal Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-platforms-dropdown-in-unreal-editor)

### What units are these?

In Unity, the primary unit of measurement is one meter. In Unreal Engine, the primary unit of measurement is one centimeter.

So, if you move something 1 unit (meter) in Unity, that is equivalent to moving something 100 units (centimeters) in Unreal Engine.

If you want to move something 2 feet in Unity, that would be 0.61units (meters). In Unreal Engine, the equivalent is 61 units (centimeters).

### Which way is up in Unreal Engine's coordinate system?

Both Unity and Unreal Engine use a left-handed coordinate system, but the axes are named differently. In Unreal Engine, positive X is "forward", positive Y is "right" and positive Z is "up".

For more information, see [Coordinate System and Spaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinate-system-and-spaces-in-unreal-engine).

### How do I see Log Output from my game?

Click the **Output Log** button in the **bottom toolbar**.

### How do I throw exceptions?

Unlike Unity, Unreal Engine does not use exception handling. Instead, use the `check()` function to trigger a critical assertion error. You can pass in an error message. If you want to report an error but not halt the program, use `ensure()` instead. This will log an error with a full call stack, but program execution will continue. If you had a debugger attached, both functions will break into the debugger.

### Where is the .NET Framework?

Unlike Unity, Unreal Engine does not use the .NET framework. Unreal Engine has its own set of container classes and libraries. Below is a list of common container comparisons:

| .Net Framework | Unreal Engine |
| --- | --- |
| String | [FString](https://docs.unrealengine.com/latest/INT/API/API/Runtime/Core/Containers/FString), [FText](https://docs.unrealengine.com/latest/INT/API/API/Runtime/Core/Internationalization/FText) |
| List | [TArray](https://docs.unrealengine.com/latest/INT/API/API/Runtime/Core/Containers/TArray) |
| Dictionary | [TMap](https://docs.unrealengine.com/latest/INT/API/API/Runtime/Core/Containers/TMap) |
| HashSet | [TSet](https://docs.unrealengine.com/latest/INT/API/API/Runtime/Core/Containers/TSet) |

You can learn more about other Unreal Engine containers [here](https://dev.epicgames.com/documentation/en-us/unreal-engine/containers-in-unreal-engine).

### Does Unreal Engine automatically reload code changes?

Yes! You can leave the editor open while you write code. Start a compile from Visual Studio after you have finished editing code, and the editor will "hot reload" your changes automatically.

* [unity](https://dev.epicgames.com/community/search?query=unity)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How do I load my last project automatically?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#how-do-i-load-my-last-project-automatically)
* [Where do I set input bindings for my game?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#where-do-i-set-input-bindings-for-my-game)
* [How do I change the starting scene of my project?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#how-do-i-change-the-starting-scene-of-my-project)
* [How do I run my game?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#how-do-i-run-my-game)
* [What units are these?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#what-units-are-these)
* [Which way is up in Unreal Engine's coordinate system?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#which-way-is-up-in-unreal-engine-s-coordinate-system)
* [How do I see Log Output from my game?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#how-do-i-see-log-output-from-my-game)
* [How do I throw exceptions?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#how-do-i-throw-exceptions)
* [Where is the .NET Framework?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#where-is-the-net-framework)
* [Does Unreal Engine automatically reload code changes?](/documentation/en-us/unreal-engine/unity-to-unreal-engine-frequently-asked-questions-faq?application_version=5.7#does-unreal-engine-automatically-reload-code-changes)
