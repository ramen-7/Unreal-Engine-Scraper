<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine?application_version=5.7 -->

# iOS Packaged Game Size

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [Debugging and Optimization for Mobile](/documentation/en-us/unreal-engine/debugging-and-optimization-for-mobile-in-unreal-engine "Debugging and Optimization for Mobile")
7. [iOS and tvOS Debugging and Optimization](/documentation/en-us/unreal-engine/ios-and-tvos-debugging-and-optimization-in-unreal-engine "iOS and tvOS Debugging and Optimization")
8. iOS Packaged Game Size

# iOS Packaged Game Size

Factors that affect the size of a packaged iOS game.

![iOS Packaged Game Size](https://dev.epicgames.com/community/api/documentation/image/ea3c6e1c-9c19-4b2e-be91-5a71980c219b?resizing_type=fill&width=1920&height=335)

 On this page

There are a number of things that affect the size of a packaged iOS game, from the content it references to the build configuration you choose.

## Target Configuration

One of the biggest changes comes from targeting the Shipping configuration instead of Development, which saves about 31 MB. The Shipping configuration uses higher optimization settings, and removes debugging symbols and much of the logging and profiling code, resulting in much smaller executable sizes.

## Game Content References

It is important to understand that any content referenced in your game will get cooked; some common gotchas are referring to huge otherwise unused textures as the default for a texture sample in a material function or material, or referencing unused content in an disconnected node or unused variable in your Blueprint. These count as referenced even if all of your material instances replace them with something else. You can look in the cooked asset folder and if you spot any unexpected assets, use the  [Reference Viewer](/documentation/en-us/unreal-engine/reference-viewer-in-unreal-engine) to track down who refers to it.

If you cook via the [Launch](/documentation/en-us/unreal-engine/launching-unreal-engine-projects-on-devices) button on the toolbar, only the content referenced by your chosen maps will be cooked, but if you [package your project](/documentation/404), all of the content in your game will be cooked, even unreferenced content.

## Disabling Slate

Content-only projects have a larger executable since they cannot make any assumptions about which plugins and libraries you are using. You can usually shrink your executable a little bit by switching to C++, and disabling unnecessary plugins and libraries at compile time (via `EnabledPlugins` and the `Project.Build.cs` and `Project.Target.cs` files). However, we have an optimization to remove more than 30 MB of Slate assets in content-only games since they cannot use Slate. If you make a C++ project that does not use Slate, you can save this space by setting `bUsesSlate = false` in the constructor of your `TargetRules` class in `Project.Target.cs`.

## Obj List

The **Obj List** command can be used to better understand which types of assets are consuming the most memory in your project.  When the Obj List command is entered into the UE4 console it will return list like in the following image.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30301092-22fd-4008-84d3-f5e46d52adf4/packagedgamesize_objlist.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30301092-22fd-4008-84d3-f5e46d52adf4/packagedgamesize_objlist.png)

Click for full image.

You can then use this list to figure out which items are using the most memory and make optimizations accordlying.

## Low-Level Memory Tracker

The Low-Level Memory Tracker, or **LLM**, is a tool that tracks memory usage in Unreal Engine projects. LLM uses a scoped-tag system to keep an account of all memory allocated by the Unreal Engine and the operating system (OS). You can use LLM to help figure out where your memory is going. To read more about using LLM check out the following document that goes over using the LLM in your UE4 project.

* [Low-Level Memory Tracker](/documentation/en-us/unreal-engine/using-the-low-level-memory-tracker-in-unreal-engine)

* [reference](https://dev.epicgames.com/community/search?query=reference)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Target Configuration](/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine?application_version=5.7#targetconfiguration)
* [Game Content References](/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine?application_version=5.7#gamecontentreferences)
* [Disabling Slate](/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine?application_version=5.7#disablingslate)
* [Obj List](/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine?application_version=5.7#objlist)
* [Low-Level Memory Tracker](/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine?application_version=5.7#low-levelmemorytracker)
