<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/gauntlet-controller-in-unreal-engine?application_version=5.7 -->

# Gauntlet Controller

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
5. [Testing and Optimizing Your Content](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content "Testing and Optimizing Your Content")
6. [Automation Test Framework](/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine "Automation Test Framework")
7. [Gauntlet Automation Framework](/documentation/en-us/unreal-engine/gauntlet-automation-framework-in-unreal-engine "Gauntlet Automation Framework")
8. Gauntlet Controller

# Gauntlet Controller

Learn how to drive runtime functional tests.

![Gauntlet Controller](https://dev.epicgames.com/community/api/documentation/image/dd7dd542-e746-4361-b45f-3ef6371a28ae?resizing_type=fill&width=1920&height=335)

 On this page

**Gauntlet Controllers** are C++ objects that drive automated tasks outside the Automation Test Framework. They are intended for runtime functional tests, especially when networking is involved.

You can create a Gauntlet Controller by reimplementing the class `UGauntletTestController`, typically in a custom plugin.

`UGauntletTestController` has several methods you can reimplement to control the flow of the test, including:

* `OnInit()` - Called when the controller initializes.
* `OnPreMapChange()` - Called before a map change.
* `OnPostMapChange(UWorld* World)` - Called after a map change. `GetCurrentMap()` returns the new map.
* `OnTick(float TimeDelta)` - Called periodically to let the controller check and control state.
* `OnStateChange(FName OldState, FName NewState)` - Called when a module's state changes. States are game-driven.

Call `EndTest(ExitCode)` when the test finishes to pass its state to the Game instance. The UAT Gauntlet picks up the result of the controller and promotes it to the test.

## Gauntlet Roles

For a Gauntlet test to use a Gauntlet Controller, the controller's name needs to be attached to the Gauntlet Role. You can do this with the following code, assuming the name `UMyControllerName:

```
UnrealTestRole ClientRole = Config.RequireRole(UnrealTargetRole.Client);
ClientRole.Controllers.Add("MyControllerName");
Copy full snippet
```



Several Roles can have different controllers.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [gauntlet](https://dev.epicgames.com/community/search?query=gauntlet)
* [automation test framework](https://dev.epicgames.com/community/search?query=automation%20test%20framework)
* [gauntlet controller](https://dev.epicgames.com/community/search?query=gauntlet%20controller)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Gauntlet Roles](/documentation/en-us/unreal-engine/gauntlet-controller-in-unreal-engine?application_version=5.7#gauntletroles)
