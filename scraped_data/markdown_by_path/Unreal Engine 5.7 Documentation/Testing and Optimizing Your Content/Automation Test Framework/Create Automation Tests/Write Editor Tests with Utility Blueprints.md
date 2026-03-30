<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/write-editor-tests-with-utility-blueprints-in-unreal-engine?application_version=5.7 -->

# Write Editor Tests with Utility Blueprints

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
7. [Create Automation Tests](/documentation/en-us/unreal-engine/create-automation-tests-in-unreal-engine "Create Automation Tests")
8. Write Editor Tests with Utility Blueprints

# Write Editor Tests with Utility Blueprints

Learn how to create Editor Tests with Blueprint.

![Write Editor Tests with Utility Blueprints](https://dev.epicgames.com/community/api/documentation/image/ab1825a7-9b11-46fa-9f54-937c3419372a?resizing_type=fill&width=1920&height=335)

 On this page

The **EditorTests** plugin is required. To enable it, follow these steps:

1. Select **Edit > Plugins** to open the **Plugin** panel.
2. Use the search bar to find the plugin.
3. Enable the corresponding checkbox.
4. Restart Unreal Editor.

You can create scripts for automated tests in the Editor with [Editor Utility Blueprint](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints).

## Creating Editor Utility Blueprint Tests

You can create an Editor Utility Blueprint by clicking the **Add** button in the **Content Browser**, selecting **Editor Utilities > Editor Utility Blueprint**, then searching for "EditorUtilityTest" in the **Pick Parent Class** window.

Name the asset appropriately as its path will be used to name the test using the following pattern: `Project.Blueprints.EditorUtilities.<content path>.<asset name>`.

## Implementing Editor Utility Blueprint Tests

Editor Utility Blueprints have two event suggestions by default:

* **Prepare Test** - Use this to perform any setup required before starting the test and then call **Finish Prepare Test**. If this event fails or times out, the **Start Test** event will not be called.
* **Start Test** - The main event. After calling this, you can use normal utility Blueprint nodes before calling **Finish Test** to finish the test.

You must call **Finish Test**, or the test will timeout. You can set up additional instructions on test completion by overriding the **Finished Test** function. The code execution must be blocking.

You can set timeouts and metadata in the asset's **Details** panel.

## Testing Editor Utility Blueprint with Editor Utility Test

To automate testing, you can create an Editor Utility Test Blueprint that instantiates a corresponding Editor Utility Blueprint.

In the Blueprint graph, add the **Construct** node and set the **Class** to the relevant Editor Utility class. Afterward, you can call any class function.

You can store the **Construct** node's return value in a variable to use multiple calls without re-instantiation.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [automation test framework](https://dev.epicgames.com/community/search?query=automation%20test%20framework)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Editor Utility Blueprint Tests](/documentation/en-us/unreal-engine/write-editor-tests-with-utility-blueprints-in-unreal-engine?application_version=5.7#creatingeditorutilityblueprinttests)
* [Implementing Editor Utility Blueprint Tests](/documentation/en-us/unreal-engine/write-editor-tests-with-utility-blueprints-in-unreal-engine?application_version=5.7#implementingeditorutilityblueprinttests)
* [Testing Editor Utility Blueprint with Editor Utility Test](/documentation/en-us/unreal-engine/write-editor-tests-with-utility-blueprints-in-unreal-engine?application_version=5.7#testingeditorutilityblueprintwitheditorutilitytest)
