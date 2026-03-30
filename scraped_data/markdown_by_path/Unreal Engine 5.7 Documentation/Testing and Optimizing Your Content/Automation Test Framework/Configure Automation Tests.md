<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/configure-automation-tests-in-unreal-engine?application_version=5.7 -->

# Configure Automation Tests

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
7. Configure Automation Tests

# Configure Automation Tests

Learn about test groups and how to exclude tests from your project

![Configure Automation Tests](https://dev.epicgames.com/community/api/documentation/image/bd90e65c-12eb-4855-b69a-bd46712fe0ab?resizing_type=fill&width=1920&height=335)

 On this page

## Test Groups

Test groups are sets of tests collected from a list of filters based on test names.

You can refer to them through the command line argument `-ExecCmds="Automation RunTest"` or through the **Test Automation** window filter. This is useful to collect tests that belong to different sections.

You can define a test group by editing the `DefaultEngine.ini` config file and adding the following line:.

```
|  |  |
| --- | --- |
|  | +Groups=(Name="Group1", Filters=((Contains=".Some String."))) |
|  | +Groups=(Name="Group2", Filters=((Contains="Group2.", MatchFromStart=true),(Contains=".Group2."))) |

Copy full snippet
```

Afterward, you can reference a test group with `Group:<GroupName>` in the `ExecCmds` argument and in [Gauntlet](/documentation/en-us/unreal-engine/gauntlet-automation-framework-overview-in-unreal-engine).

## Excluding Tests

During project development, you may need to exclude tests temporarily.

To exclude a test, edit the `DefaultEngine.ini` or the corresponding platform config file with the following line:

```
+ExcludeTest=(Test="<test or section name>",Reason="<a reason>",Warn=False)
Copy full snippet
```



You can exclude all tests that start with a string by inputting a partial name.

You can exclude by Rendering Hardware Interface (RHI) by adding the following line:

```
+ExcludeTest=(Test="<test or section name>",Reason="<a reason>", RHIs=("Vulkan", "DirectX 11"),Warn=False)
Copy full snippet
```

The RHI name must match the syntax from `Engine\Source\Runtime\AutomationTest\Public\AutomationTestExcludelist.h`

Excluded tests will show as "Skipped" with the reason attached as an info event.

You can also exclude tests in the Editor from the **Test Automation** window by selecting the **Exclude** button next to the test's selection checkbox.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [automation test framework](https://dev.epicgames.com/community/search?query=automation%20test%20framework)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Test Groups](/documentation/en-us/unreal-engine/configure-automation-tests-in-unreal-engine?application_version=5.7#testgroups)
* [Excluding Tests](/documentation/en-us/unreal-engine/configure-automation-tests-in-unreal-engine?application_version=5.7#excludingtests)
