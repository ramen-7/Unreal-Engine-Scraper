<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-utility-widgets-in-unreal-engine?application_version=5.7 -->

# Editor Utility Widgets

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Scripting and Automating the Unreal Editor](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor "Scripting and Automating the Unreal Editor")
7. [Scripting the Unreal Editor using Blueprints](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints "Scripting the Unreal Editor using Blueprints")
8. Editor Utility Widgets

# Editor Utility Widgets

An overview and usage instructions for Editor Utility Widgets.

![Editor Utility Widgets](https://dev.epicgames.com/community/api/documentation/image/62836839-5635-4a77-aa5f-b8c4baa573bb?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

If you want to modify the User Interface (UI) of the **Unreal Editor**, you can use **Editor Utility Widgets** to add new UI elements. Editor Utility Widgets are based on **Unreal Motion Graphics** (UMG), so you can set up Widgets in a Blueprint like you would for any other UMG Widget Blueprint.

These Widgets are specifically for the Editor UI, and you can use them to create custom Editor tabs. You can then select these custom tabs from the Windows menu, like you would select existing Editor tabs.

## Create an Editor Utility Widget

1. Right-click in the **Content Browser** and select **Editor Utilities > Editor Utility Widget**.

   ![Add Editor Utility Widget asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a65d26f-7c6d-4ba1-bbc1-c38d83315395/ue5_1-01-add-asset.png "Add Editor Utility Widget asset")
2. Name your Editor Utility Widget Asset. In this example, the Asset is named **TestEditorUtility**. Double-click the **Editor Utility Widget Asset** to open the Widget Blueprint for editing.

   ![Name your Editor Utility Widget Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bff14ee9-2a4e-44f9-a6cd-7c1eb03cdfb1/ue5_1-02-name-asset.png "Name your Editor Utility Widget Asset")
3. Edit your Widget Blueprint as needed.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0fb050e6-17c5-4962-b68b-d52fe45e0bd4/ue5_1-03-edit-widget-blueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0fb050e6-17c5-4962-b68b-d52fe45e0bd4/ue5_1-03-edit-widget-blueprint.png)
4. Right-click the **Editor Utility Widget Asset** and select **Run Editor Utility Widget** to open an Editor tab with your Editor Utility displayed. The tab is only dockable with Level Editor tabs.

   ![Run Editor Utility Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc4a3195-88a9-4d5e-af10-e62e8cfe84f0/ue5_1-04-run-editor-utility-widget.png "Run Editor Utility Widget")
5. Once you have run the Editor Utility Widget, it appears in the Level Editor's **Tools** dropdown, under the **Editor Utility Widgets** category.

   ![Test Editor Utility](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6375cbf4-2555-4116-bf7a-c0d3b380f67a/ue5_1-05-enable-test.png "Test Editor Utility")

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)
* [blutilities](https://dev.epicgames.com/community/search?query=blutilities)
* [editor utility](https://dev.epicgames.com/community/search?query=editor%20utility)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create an Editor Utility Widget](/documentation/en-us/unreal-engine/editor-utility-widgets-in-unreal-engine?application_version=5.7#createaneditorutilitywidget)
