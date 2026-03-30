<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor?application_version=5.7 -->

# Scripting and Automating the Unreal Editor

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
6. Scripting and Automating the Unreal Editor

# Scripting and Automating the Unreal Editor

Introduction to using Blueprints and Python to control the Unreal Editor programmatically.

![Scripting and Automating the Unreal Editor](https://dev.epicgames.com/community/api/documentation/image/d91da222-f636-4632-a4f1-4d9ebf3cf78a?resizing_type=fill&width=1920&height=335)

 On this page

In the Unreal Editor user interface, you have access to a vast range of visual tools for setting up your Project, designing and building Levels, creating gameplay interactions, and more. But sometimes, once you've figured out what you need the Editor to do, you might want to invoke its tools and commands programmatically — either in a reusable script, or by constructing your own interfaces to drive the Editor.

This can help you:

* Minimize or eliminate the need to repeat the same series of tasks over and over,
* Automate or randomize the placement, layout and settings of Actors in your Levels,
* Create your own Asset import and management pipelines,
* Interoperate with other third-party applications and pipeline scripts,
* Extend the Editor with additional tools, and even UIs, that you customize specifically for the needs of your Project or content.

The pages in this section show how you can run these kinds of in-Editor scripts using [Blueprints](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints), [Python](/documentation/404), and [remote control ol](/documentation/en-us/unreal-engine/remote-control-for-unreal-engine).

## Installing the Editor Scripting Utilities Plugin

If you're planning to do any Editor automation, regardless of the language or system you plan to use, you will almost certainly want to install the **Editor Scripting Utilities** plugin. This plugin simplifies many of the most common operations you'll need to do in the Editor, handling uncommon edge cases so that you don't have to understand all the internal details of how the Editor works in order to do something conceptually simple.

To install the plug-in:

1. From the main menu, choose **Edit > Plugins** to open the **Plugins** window.

   ![Open Plugins window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bbf3aa7-4047-418f-b1df-136b956ef4e5/01-edit-plugins_ue5.png "Open Plugins window")
2. Under the **Scripting** category, find the entry for the **Editor Scripting Utilities** and check its **Enabled** box.

   ![Enable the Editor Scripting Utilities plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7cdeb529-a768-4bcc-8c57-9f08f121466b/02-enable-editor-scripting-plugin_ue5.png "Enable the Editor Scripting Utilities plugin")
3. If you're interested in using Python, you can also check the **Enabled** box for the Python plugin while you're here. For more, see [Scripting the Editor using Python](/documentation/404).
4. Restart the Editor and reload your Project.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [python](https://dev.epicgames.com/community/search?query=python)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [scripting](https://dev.epicgames.com/community/search?query=scripting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Installing the Editor Scripting Utilities Plugin](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor?application_version=5.7#installingtheeditorscriptingutilitiesplugin)
