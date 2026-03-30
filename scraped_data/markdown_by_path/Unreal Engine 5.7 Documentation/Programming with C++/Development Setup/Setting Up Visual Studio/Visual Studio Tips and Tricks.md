<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7 -->

# Visual Studio Tips and Tricks

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
6. [Development Setup](/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine "Development Setup")
7. [Setting Up Visual Studio](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine "Setting Up Visual Studio")
8. Visual Studio Tips and Tricks

# Visual Studio Tips and Tricks

Useful tips and tricks for working on Unreal Engine content in Visual Studio

![Visual Studio Tips and Tricks](https://dev.epicgames.com/community/api/documentation/image/6c4a31f9-880a-43d0-91d9-287bb0c75b2f?resizing_type=fill&width=1920&height=335)

 On this page

## Immediate Window

| Command | Description |
| --- | --- |
| `{,,UnrealEditor-Core}::PrintScriptCallstack()` | Blueprint callstack |
| `{,,UnrealEditor-Core}::GFrameNumber` | Current frame number (also works as breakpoint condition) |
| `{,,UnrealEditor-Core}::GPlayInEditorID` | PIE ID (useful for multiplayer, also works as breakpoint condition) |
| `UnrealEditor-Engine!GPlayInEditorContextString` | PIE window name (useful for multiplayer) |

## Quick Reference

### Disabling/Enabling Optimizations

The following macros will disable and enable compiler optimization for the file you add them to:

C++

```
|  |  |
| --- | --- |
|  | UE_DISABLE_OPTIMIZATION |
|  | UE_ENABLE_OPTIMIZATION |
```

UE\_DISABLE\_OPTIMIZATION
UE\_ENABLE\_OPTIMIZATION

Copy full snippet(2 lines long)

When optimization is disabled, code will execute exactly as you wrote it without removing temporary or debugging variables you would need during traces or step-by-step debug sessions. This is useful when you want to selectively debug files without using a full Debug build.

### Debug Lines

**Debug lines** refer to lines drawn in the viewport, usually to show the path of line traces or paths. To use them, you need to include `DrawDebugHelpers.h`. The following code illustrates how to use `DrawDebugLine`:

C++

```
|  |  |
| --- | --- |
|  | #include "DrawDebugHelpers.h" |
|  | DrawDebugLine(GetWorld(), START, END, FColor::Green); |
```

#include "DrawDebugHelpers.h"
DrawDebugLine(GetWorld(), START, END, FColor::Green);

Copy full snippet(2 lines long)

`DrawDebugHelpers` has numerous debug drawers in addition to standard debug lines. These include:

**Primitive Shapes**

C++

```
|  |  |
| --- | --- |
|  | + DrawDebugBox |
|  | + DrawDebugSphere |
|  | + DrawDebugCapsule |
|  | + DrawDebugCylinder |
|  | + DrawDebugPlane |
|  | + DrawDebugCone |
|  | + DrawDebugPoint |
```

+ DrawDebugBox
+ DrawDebugSphere
+ DrawDebugCapsule
+ DrawDebugCylinder
+ DrawDebugPlane
+ DrawDebugCone
+ DrawDebugPoint

Copy full snippet(7 lines long)

**Solid Shapes**

C++

```
|  |  |
| --- | --- |
|  | + DrawDebugSolidBox |
|  | + DrawDebugSolidPlane |
```

+ DrawDebugSolidBox
+ DrawDebugSolidPlane

Copy full snippet(2 lines long)

**Other Common Shapes**

C++

```
|  |  |
| --- | --- |
|  | + DrawDebugFrustrum |
|  | + DrawDebugCamera |
|  | + DrawDebugCrosshairs |
```

+ DrawDebugFrustrum
+ DrawDebugCamera
+ DrawDebugCrosshairs

Copy full snippet(3 lines long)

**Meshes**

C++

```
+ DrawDebugMesh
```

+ DrawDebugMesh

Copy full snippet(1 line long)

### Debug Text

The following code provides an example of how to write debug text to the screen. This mirrors the functionality in the **Print String** Blueprint node.

C++

```
|  |  |
| --- | --- |
|  | #include "Engine/Engine.h" |
|  | FString MyDebugString = FString::Printf(TEXT("MyVelocity(%s)"), *MyVelocity.ToCompactString()); |
|  | GEngine->AddOnScreenDebugMessage(INDEX_NONE, 0.f, FColor::Yellow, MyDebugString, false, FVector2D::UnitVector * 1.2f); |
```

#include "Engine/Engine.h"
FString MyDebugString = FString::Printf(TEXT("MyVelocity(%s)"), \*MyVelocity.ToCompactString());
GEngine->AddOnScreenDebugMessage(INDEX\_NONE, 0.f, FColor::Yellow, MyDebugString, false, FVector2D::UnitVector \* 1.2f);

Copy full snippet(3 lines long)

The `FString::Printf` function can take string format parameters, providing a way to quickly compose strings that include variables. You need to include `Engine.h` to gain access to `GEngine` so you can call `AddOnScreenDebugMessage`. For more information on how to use string formatting, refer to [String Handling in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/string-handling-in-unreal-engine).

### Enum to String

Enums can be converted to strings by calling `GetNameStringByValue` from a static `UEnum` and providing it with the value you want to get the name of. You must initialize the `UEnum` with a `StaticEnum` of the same type as the enum whose value you are passing in.

C++

```
|  |  |
| --- | --- |
|  | EMyEnum::Type MyVariable; |
|  | static const UEnum* Enum = StaticEnum<EMyEnum::Type>(); |
|  | Enum->GetNameStringByValue(MyVariable); |
```

EMyEnum::Type MyVariable;
static const UEnum\* Enum = StaticEnum<EMyEnum::Type>();
Enum->GetNameStringByValue(MyVariable);

Copy full snippet(3 lines long)

## Fixing the Configuration Combobox Width

The default solution configuration combobox is too small to see the full name of the option currently selected. To fix that, right-click on the **toolbar**, select **Customize**, select the **Commands** tab, select the **radio Toolbar > Standard**, scroll down to the **Solution Configurations**, click on **Modify Selection**, and put in the width you would like. A width of 200 is typically useful.

[![Fixing the configuration combobox](https://dev.epicgames.com/community/api/documentation/image/69237c88-b481-4002-8e77-1786741b503d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69237c88-b481-4002-8e77-1786741b503d?resizing_type=fit)

## Speeding up Visual Studio 2019

Visual Studio 2019 can be slow when working with Unreal projects. The following are a few strategies that might improve performance for you:

### Debugging Is Slow

Try disabling the following settings in **Option > Debugging > General**:

* Uncheck **Enable Diagnostic Tools** while debugging.
* Uncheck **Show elapsed time PerfTip** while debugging.

### Perforce Visual Studio history Shows Above Every Method

[![Showing P4VS history](https://dev.epicgames.com/community/api/documentation/image/243dbcf8-4d1f-434a-9b2b-3a1a19874fe5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/243dbcf8-4d1f-434a-9b2b-3a1a19874fe5?resizing_type=fit)

To stop the Perforce Visual Studio history from showing above every method, uncheck **Tools > Options > Text Editor\All Languages\CodeLens > Enable CodeLens**.

### Visual Studio Is Slow when Opening Solutions or Debugging

If you are using another plugin for symbol searching, such as Visual Assist, you can disable the Intellisense database to prevent it from parsing the solution. This can be done from:
**Tools** > **Options** > **Text Editor** > **C/C++** > **Advanced** > Set **Disable Database = true**.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Immediate Window](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#immediate-window)
* [Quick Reference](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#quick-reference)
* [Disabling/Enabling Optimizations](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#disabling-enabling-optimizations)
* [Debug Lines](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#debug-lines)
* [Debug Text](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#debug-text)
* [Enum to String](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#enum-to-string)
* [Fixing the Configuration Combobox Width](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#fixing-the-configuration-combobox-width)
* [Speeding up Visual Studio 2019](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#speeding-up-visual-studio-2019)
* [Debugging Is Slow](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#debugging-is-slow)
* [Perforce Visual Studio history Shows Above Every Method](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#perforce-visual-studio-history-shows-above-every-method)
* [Visual Studio Is Slow when Opening Solutions or Debugging](/documentation/en-us/unreal-engine/visual-studio-tips-and-tricks-in-unreal-engine?application_version=5.7#visual-studio-is-slow-when-opening-solutions-or-debugging)
