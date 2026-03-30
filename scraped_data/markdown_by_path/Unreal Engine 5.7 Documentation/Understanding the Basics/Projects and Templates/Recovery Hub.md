<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/recovery-hub-in-unreal-engine?application_version=5.7 -->

# Recovery Hub

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Projects and Templates](/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine "Projects and Templates")
7. Recovery Hub

# Recovery Hub

Plugin to help recover an Unreal Engine session after a crash or abnormal exit.

![Recovery Hub](https://dev.epicgames.com/community/api/documentation/image/a9ba8eff-a3b9-49ed-9bba-88fa42a4e5e9?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

**Recovery Hub** is an Unreal Engine plugin that helps with the recovery of an engine session after a crash or abnormal exit. In Unreal Engine 4, this plugin was named Disaster Recovery.

The Recovery Hub plugin isn't enabled by default. To use it, you must first [enable it](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).

If you work with Assets larger than 2GB, Recovery Hub will consume a large amount of disk space as it records each transaction. You should disable the system temporarily if you start to run out of disk space. To do this, in the **Plugins > Recovery Hub** section of the [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine) window, disable the **Is Enabled** option.

## How Recovery Hub Works

When the Editor launches, Disaster Recovery automatically checks to see if the last sessions ended abnormally. If it did, the Editor retrieves the previously recorded list of transactions and offers to replay them for you. You can choose to replay some or all of the transactions to help recover work that may have been lost when the last Editor session crashed.

Recovery Hub reads each change to an Actor or Asset as a **transaction** and maintains a list of the most recent transactions. If the Editor crashes, you can roll back your project to a previous transaction to restore any lost work.

Because Recovery Hub only supports Level editing and Sequencer, it works best in conjunction with autosave files and it's not intended as a replacement for autosave. Each save and autosave counts as a transaction in Recovery Hub.

Enable **Autosave** from the **General > Saving & Loading** section of the [Editor Preferences](/documentation/en-us/unreal-engine/unreal-editor-preferences).

## Recovery Hub Interface

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/587606ea-fdd4-4a54-a059-f91c953bded6/ue5_1-recovery-hub-ui.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/587606ea-fdd4-4a54-a059-f91c953bded6/ue5_1-recovery-hub-ui.png)

Click the image for full size.

The Recovery Hub window consist of the following areas:

| **Number** | **Name** | **Description** |
| --- | --- | --- |
| 1 | **Main Toolbar** | Contains two buttons:   * **Import**: Import a crash data dump in `.json` format. * **Delete**: Delete the currently selected session. |
| 2 | **Sessions** panel | Displays a list of saved sessions. |
| 3 | **Configurations** button | Click this button to open the Recovery Hub plugin settings in Project Settings. |
| 4 | Session details | Displays a list of transactions for the currently selected session. |

## Recovering a Session

To recover an Unreal Editor session after a crash, follow these steps:

1. Open Recovery Hub. From the main menu, go to **Tools > Recovery Hub**.
2. From the **Sessions** panel, select a session to recover.
3. Click **Recover All**. This button appears after an Editor crash.

## Deleting a Session

If you want to free up disk space, you can delete old Recovery Hub sessions you no longer need. To do this, follow these steps:

1. Open Recovery Hub. From the main menu, go to **Tools > Recovery Hub**.
2. From the **Sessions** panel, select a session to recover.
3. Click the **Delete** button.

* [beta](https://dev.epicgames.com/community/search?query=beta)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How Recovery Hub Works](/documentation/en-us/unreal-engine/recovery-hub-in-unreal-engine?application_version=5.7#howrecoveryhubworks)
* [Recovery Hub Interface](/documentation/en-us/unreal-engine/recovery-hub-in-unreal-engine?application_version=5.7#recoveryhubinterface)
* [Recovering a Session](/documentation/en-us/unreal-engine/recovery-hub-in-unreal-engine?application_version=5.7#recoveringasession)
* [Deleting a Session](/documentation/en-us/unreal-engine/recovery-hub-in-unreal-engine?application_version=5.7#deletingasession)
