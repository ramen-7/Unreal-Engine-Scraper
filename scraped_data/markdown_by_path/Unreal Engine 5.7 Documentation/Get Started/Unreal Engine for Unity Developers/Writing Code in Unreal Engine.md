<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7 -->

# Writing Code in Unreal Engine

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
7. Writing Code in Unreal Engine

# Writing Code in Unreal Engine

Overview and examples of writing code in Unreal Engine, demonstrating equivalence between C#, C++, and Blueprint.

![Writing Code in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/cb24e784-ccbc-4160-b006-a94ba4e3261b?resizing_type=fill&width=1920&height=335)

 On this page

## Setup

### C++

To write C++ code in Unreal Engine (UE), download [Visual Studio](https://visualstudio.microsoft.com/downloads/) on Windows, or [install Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) on macOS. When you create a new C++ project, UE will automatically create Visual Studio project files for you.

There are two ways to access Visual Studio from your UE project:

* In the **Content Browser**, **double-click** a C++ class to open it in Visual Studio.
* From the main menu, go to **Tools** **>** **Open Visual Studio**. This option only appears if your project contains at least one C++ class.

A critical difference in UE: You will sometimes have to manually refresh your Visual Studio project files (for example, after downloading a new version of UE, or when manually making changes to source file locations on disk.) You can do this in two ways:

* From UE's main menu, go to **Tools > Refresh Visual Studio Project**.
* **Right-click** the **.uproject** file in your project's directory and select **Generate Visual Studio project files**.

See [Development Setup](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine) for more detailed information.

### Blueprint

You only need UE to use Blueprint scripting. All the features you need are built into Unreal Editor.

## Writing Event Functions

If you previously worked with MonoBehaviors, you are familiar with the `Start`, `Update`, and `OnDestroy` methods. Below is a comparison between a Unity behavior and its equivalent for UE: Actors and Components.

In Unity, you might have a simple component that looks like this:

C#

```
|  |  |
| --- | --- |
|  | public class MyComponent : MonoBehaviour |
|  | { |
|  | void Start() {} |
|  | void OnDestroy() {} |
|  | void Update() {} |
|  | } |
```

public class MyComponent : MonoBehaviour
{
void Start() {}
void OnDestroy() {}
void Update() {}
}

Copy full snippet(6 lines long)

### AActor

In UE, you can write code on the Actor itself rather than only coding new component types.

Additionally, Actors have similar methods to Unity's `Start`, `OnDestroy`, and `Update` methods.

#### C++

C++

```
UCLASS()
class AMyActor : public AActor
{
	GENERATED_BODY()

	// Called at start of game.
	void BeginPlay();

	// Called when destroyed.
	void EndPlay(const EEndPlayReason::Type EndPlayReason);
```

Expand code  Copy full snippet(14 lines long)

#### Blueprint

[![](https://dev.epicgames.com/community/api/documentation/image/90216cf5-0993-428e-b4d0-80903e1899f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90216cf5-0993-428e-b4d0-80903e1899f3?resizing_type=fit)

### UActorComponent

Components in UE are conceptually similar to MonoBehaviors but contain different methods.

#### C++

C++

```
UCLASS()
class UMyComponent : public UActorComponent
{
	GENERATED_BODY()

	// Called after the owning Actor was created
	void InitializeComponent();

	// Called when the component or the owning Actor is being destroyed
	void UninitializeComponent();
```

Expand code  Copy full snippet(14 lines long)

#### Blueprint

[![](https://dev.epicgames.com/community/api/documentation/image/9d35c8a7-d6fe-4bb5-bd1c-dc74d3f1fab2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d35c8a7-d6fe-4bb5-bd1c-dc74d3f1fab2?resizing_type=fit)

## Additional Notes

* In UE, you must explicitly call the parent's method within a child's method. For example, in Unity C# this would be `base.Update()`, but in UE C++ you will use `Super::Tick()` for Actors or `Super::TickComponent()` for Components.
* In UE C++, classes use various prefixes, such as `U` for `UObject` subclasses and `A` for Actor subclasses. See [Coding Standard](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) for more detailed information.
* For gameplay coding examples, see [Creating Gameplay in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-gameplay-in-unreal-engine-for-unity-developers).

* [unity](https://dev.epicgames.com/community/search?query=unity)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#setup)
* [C++](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#c)
* [Blueprint](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#blueprint)
* [Writing Event Functions](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#writing-event-functions)
* [AActor](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#a-actor)
* [C++](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#c++)
* [Blueprint](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#blueprint)
* [UActorComponent](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#u-actor-component)
* [C++](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#c++-2)
* [Blueprint](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#blueprint)
* [Additional Notes](/documentation/en-us/unreal-engine/writing-code-in-unreal-engine-for-unity-developers?application_version=5.7#additional-notes)
