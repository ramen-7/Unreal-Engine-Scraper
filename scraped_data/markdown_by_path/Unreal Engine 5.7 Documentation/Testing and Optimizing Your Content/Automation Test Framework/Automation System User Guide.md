<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7 -->

# Automation System User Guide

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
7. Automation System User Guide

# Automation System User Guide

A guide to using the Automation System for Running Tests.

![Automation System User Guide](https://dev.epicgames.com/community/api/documentation/image/adf6d408-f1fd-481c-9707-853764592c79?resizing_type=fill&width=1920&height=335)

 On this page

![Banner Image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff3be0a1-6659-4861-bb6b-486574e1bdf6/automation-banner.png "Banner Image")

Session Frontend with the Automation tab in focus.

The **Automation** tab is part of the **Unreal (Session) Frontend** of **Unreal Engine**. It is located here because it enables you to run automation tests on any other devices that are connected to your machine or are on your local network.

There are two ways you can access the frontend suite:

* **Session Frontend** - Opens the local Editor as an automation worker to run automation on external devices.

  + Navigate to **Tools > Session Frontend**
* **Unreal Frontend** - Opens a standalone version of the Frontend that includes the **Session Frontend**, **Device Manager**, and **Project Launcher**.

  + Navigate to your **[Unreal Engine Root Directory]** > **Engine** > **Binaries** > **Win64** > **UnrealFrontend.exe**

## Enabling Plugins

In the latest versions of Unreal Engine, all the **Automation Tests** have been moved from the **Engine Content** folder to their plugins that must be enabled before they will be visible in the **Automation** tab.

|  |  |
| --- | --- |
| Open Plugins | [Enable Plugins](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/807cf070-418f-4897-9a57-6d28dbd82a35/ue5_1-02-enable-plugins.png) |
| To enable the plugins, select **Edit > Plugins > Testing**. | Plugins Browser with Automation Tests |

If you are using the standalone **Unreal Frontend**, all the automation tests will be available without any additional steps to enable it.

## User Interface

When you open the **Session Frontend**, you will have access to a few tabs, such as the **Console**, **Automation**, **Screenshot Comparison**, and **Profiler**. For all your automation testing needs, the **Automation** tab will house all of the functionality you need with some additional functionality falling under the [Screenshot Comparison](/documentation/en-us/unreal-engine/screenshot-comparison-tool-in-unreal-engine) tab for rendering functionality comparison.

[![Automation tab demonstration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fde01af3-0efd-4f1a-aa23-07f9cd34301f/ue5_1-03-automation-tab.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fde01af3-0efd-4f1a-aa23-07f9cd34301f/ue5_1-03-automation-tab.png)

Click image for full view.

If you do not see anything listed in the **Automation** tab window, select an active session from the **Session Browse** on the left. For example, under **This Application** the machine named **PC-xxx** is selected.

### Session Browser

The **Sessions Browser** enables you to connect to specific instances of the Editor. You will only see the Automation window populate with the available automation tests once a session has been selected.

![Sessions Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f6bbbfd-a512-4831-88a4-19c67390cd58/ue5_1-04-session-browser.png "Sessions Browser")

### Toolbar

The **toolbar** in the **Automation** tab enables you to control how you start, refresh, and filter errors and warnings for your automation tests.

[![Automation Toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/731505b1-3c06-4aba-b3c7-af0f1d6fab3c/ue5_1-05-automation-toolbar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/731505b1-3c06-4aba-b3c7-af0f1d6fab3c/ue5_1-05-automation-toolbar.png)

Click image for full view.

| Icon | Title | Description |
| --- | --- | --- |
| Start Test button | **Start Tests** | Starts and stops the currently selected automation test(s) that are enabled. The number of tests that will be run is also listed under the button for reference. |
| Run Level Test button | **Run Level Test** | If the currently loaded level is a test map, you can click this button to select the tests and run it immediately. |
| Refresh Test button | **Refresh Tests** | This will refresh the Test Name list for any test that is added to the project. |
| Find Workers button | **Find Workers** | This will find local workers that can be used to perform the tests. |
| Errors button | **Errors** | Toggles a filter for the Test window that displays any tests that ran into an error while attempting to complete. |
| Warnings button | **Warnings** | Toggles a filter for the Test window that displays any tests that ran into a warning while attempting to complete. |
| Dev Content button | **Dev Content** | When enabled, developer directories will be included for automation tests. |
| Device Group button | **Device Groups** | Enables you to group the tests based on a series of options, such as the machine name, platform, operating system version, and much more. |
| Excluded Tests button | **Excluded Tests** | Toggle Excluded Tests only. |
| Presets panel | **Preset** | Enables you to add your own presets for automation tests with the selected tests and settings so that you can use them again at a later date. |

### Tests Window and Results

In the **Automation Tests Window** and the **Automation Test Results** panel, you'll find information relevant to the tests that have been run, such as the Machine that it was completed, number of tests that were run, the number of fails, and much more.

[![Test and Result panel]](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7cc6d504-56e3-4818-a5d3-006572c12b55/ue5_1-16-test-result-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7cc6d504-56e3-4818-a5d3-006572c12b55/ue5_1-16-test-result-panel.png)

Click image for full view.

You can use the **Device Groups** button to determine how information should be grouped in the results panel when starting a new run of automation tests.

[![Device grups drop-down menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2d00065-55ab-4ed4-995e-35d7a42b2f7f/ue5_1-17-device-grups-dropdow.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2d00065-55ab-4ed4-995e-35d7a42b2f7f/ue5_1-17-device-grups-dropdow.png)

Click image for full view.

When looking at the results, use the **Display** selection to show the **Name** of the test or the **Time** the test took to complete.

[![Display selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2cee64b-c50a-4424-8215-f75143adca6d/ue5_1-18-display-name-time.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2cee64b-c50a-4424-8215-f75143adca6d/ue5_1-18-display-name-time.png)

Click image for full view.

### Export

Once the tests have been completed, it is possible to export the results to a **CSV** file via the **Export** drop-down.

[![Export drop-down menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d060bedf-566a-4ad2-8efe-6b70337f9573/ue5_1-19-export-tests.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d060bedf-566a-4ad2-8efe-6b70337f9573/ue5_1-19-export-tests.png)

Click image for full view.

Choose from the available filters that you'd like to export and then select the **Export Data** button.

![Export Data button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63052160-9651-4eec-a3fa-ab52a2137116/ue5_1-20-export-data.png "Export Data button")

When your data is exported, a pop-up will indicate if it was successful and the save location of the **CSV** file.

![Export Data success message](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b510d91a-2b58-46d1-847f-e77a7fa4f67c/ue5_1-21-export-data-success-message.png "Export Data success message")


The **Export** drop-down will only be active once reports have been generated, and the **Export Data** button will only become active if there are reports that meet the filter criteria.

### Copy

Once the tests have been completed, you can select any lines that appear in the **Automation Test Results** panel and click the **Copy** button to copy them to your clipboard and paste elsewhere.

[![Copy Test result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c950df6d-7308-482f-885c-72e18f2cfcd7/ue5_1-22-copy-test-result.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c950df6d-7308-482f-885c-72e18f2cfcd7/ue5_1-22-copy-test-result.png)

Click image for full view.

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling Plugins](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#enablingplugins)
* [User Interface](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#userinterface)
* [Session Browser](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#sessionbrowser)
* [Toolbar](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#toolbar)
* [Tests Window and Results](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#testswindowandresults)
* [Export](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#export)
* [Copy](/documentation/en-us/unreal-engine/automation-system-user-guide-in-unreal-engine?application_version=5.7#copy)
