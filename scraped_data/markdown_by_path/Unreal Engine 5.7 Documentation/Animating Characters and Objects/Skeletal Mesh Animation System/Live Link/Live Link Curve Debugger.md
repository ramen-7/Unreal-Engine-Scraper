<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-curve-debugger-in-unreal-engine?application_version=5.7 -->

# Live Link Curve Debugger

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine "Live Link")
8. Live Link Curve Debugger

# Live Link Curve Debugger

Using the Live Link Curve Debugger, you can quickly see what the output is of various Live Link curves are in an easy to debug manner.

![Live Link Curve Debugger](https://dev.epicgames.com/community/api/documentation/image/f38a389f-75e2-4883-a1d6-bbe488f96f83?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

When streaming content into Unreal Engine using the [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine) Plugin, you may want to view the various curves and values that are active. The **Live Link Curve Debugger**is a tool that enables you to quickly see what the output is of various Live Link curves are in an easy to debug manner.

## Enabling Live Link Curve Debugger

In order to use the Live Link Curve Debugger, you will first need to enable it from the **Plugins**menu:

1. From the **Edit** menu, select **Plugins**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95082820-936d-40c1-9e60-fd56e0b13317/01_pluginmenu.png "01_PluginMenu.png")
2. In the **Plugins**menu under **Animation**, enable both **Live Link**and **Live Link Curve Debug UI**options, and restart the Editor.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f26cdcd-b983-4b30-bd02-db59376f3a51/02_enablelivelinkoptions.png "02_EnableLiveLinkOptions.png")
3. From the **Window**option, under **Developer Tools**, select **Live Link Curve Debugger**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e9c3483-25ac-4cf0-ba49-1cce7da84f9c/03_debuggerwindow.png "03_DebuggerWindow.png")

   The **Live Link Curve Debugger** window will open.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de73fc33-f9d0-4077-86ae-dab1ea580455/04_debuggerwindowopen.png "04_DebuggerWindowOpen.png")

## Using Live Link Curve Debugger

Once connected to [Motion Builder with Live Link](/documentation/en-us/unreal-engine/live-link-stream-motionbuilder-to-unreal-engine), the content you have in your application will be accessible within Unreal Engine, include any animation curves. With the Live Link Curve Debugger, you can see a list of all the curves and curve values for the currently selected **Subject Name** which you can define by clicking the **Live Link Subject Name**drop-down menu and selecting your Subject.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28494e75-f152-41ea-8a1b-147a459de232/debuggerwindowsubject.png "DebuggerWindowSubject.png")

Once you select a Subject, any curves will be displayed in the window along with their values.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9617ff22-1ab3-4def-b995-a752c2ed9c73/curvedebugger-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9617ff22-1ab3-4def-b995-a752c2ed9c73/curvedebugger-1.png)

Click image for full view.

If you haven't specified a Subject Name, as soon as one connects with some curves, the debugger will switch to that one. You can change this selection by clicking the **Live Link Subject Name** drop-down (in Editor or a Desktop build) or by typing **LiveLinkDebugger Next** in the command-line to cycle through different subject names (on other client builds)

Inside a client you can also use the command-line to show the Live Link Debugger with the command: **LiveLinkDebugger Show**

Optionally you may specify a Live Link Subject Name to start with in the command-line by using the command **LiveLinkDebugger Show** *SubjectName* (the name of your Subject).

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [live link](https://dev.epicgames.com/community/search?query=live%20link)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling Live Link Curve Debugger](/documentation/en-us/unreal-engine/live-link-curve-debugger-in-unreal-engine?application_version=5.7#enablinglivelinkcurvedebugger)
* [Using Live Link Curve Debugger](/documentation/en-us/unreal-engine/live-link-curve-debugger-in-unreal-engine?application_version=5.7#usinglivelinkcurvedebugger)
