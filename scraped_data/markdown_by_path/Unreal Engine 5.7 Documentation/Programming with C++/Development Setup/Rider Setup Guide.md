<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7 -->

# Rider Setup Guide

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
7. Rider Setup Guide

# Rider Setup Guide

Step through some of the basic steps when you first launch Rider.

On this page

Rider is a fast and fully-featured IDE for Unreal Engine. It delivers insights on code and Blueprints, assists with reflection specifiers, provides safe refactorings, and offers advanced code completion. Try [Rider for Unreal](https://www.jetbrains.com/lp/rider-unreal/)! Compared to Visual Studio, Rider has:

* Better code navigation and auto-completion
* Better performance (less freezing)
* Better debugging and console support

## Step-by-step guide

1. Install Rider

   1. Get the latest version from the [Jetbrains website](https://www.jetbrains.com/lp/rider-unreal/)  .
2. Visit the Jetbrains Marketplace

   1. Install the [EzArgs plugin](https://plugins.jetbrains.com/plugin/16411-ezargs).
3. Apply these setting for your RAM setup

   1. Set your RAM to 64 gb (Rider will not function with its default RAM settings).

      1. **Help > Edit Custom VM Options**
      2. Then enter `-Xmx64g`
      3. **Save** your modifications as a file

         [![Edit-custom-vm-options-command-line](https://dev.epicgames.com/community/api/documentation/image/0074e836-685b-465f-99ad-78c9807c01f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0074e836-685b-465f-99ad-78c9807c01f2?resizing_type=fit)
4. Configure your **dotnet.exe** and **MSBuild** version paths (these settings are not the default settings).

   1. Go to **Settings > Build, Execution, Deployment > Toolset and Build**
   2. Adjust your file paths (see step e for an example MSBuild file path)
   3. Under **Build**, set parallel process to **1**
   4. Under **Design Time Build**, set parallel processes to **64**

      [![Toolset-and-Build-options](https://dev.epicgames.com/community/api/documentation/image/3fe8d16c-2147-4d15-b918-f7603d416358?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3fe8d16c-2147-4d15-b918-f7603d416358?resizing_type=fit)

      Click image to expand.
   5. Select the **path** for the MSBuild version

      [![Selecting-the-MSbuild-path-file](https://dev.epicgames.com/community/api/documentation/image/a27360d8-8657-4a06-91e7-07681e1a26af?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a27360d8-8657-4a06-91e7-07681e1a26af?resizing_type=fit)

      Click image to expand.
   6. Unlike with some tools, you need to explicitly save your settings changes.  **Save to This computer** so that your settings carry over to all your work streams.

      [![Save-to-this-computer](https://dev.epicgames.com/community/api/documentation/image/e7987cd1-1e5d-4ce4-b001-4457c21f0af7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e7987cd1-1e5d-4ce4-b001-4457c21f0af7?resizing_type=fit)
   7. Enable indexing on plugins so that you get full code support (syntax, refactoring, completion, finding definitions, dependency analysis etc.) in the Harmonic and other plugins.  From **Settings > Languages & Frameworks > C++ > Unreal Engine**, under **Code Indexing**, select the checkbox for **Index plugins**.

      [![Enable-indexing-plugins](https://dev.epicgames.com/community/api/documentation/image/0c51309b-6917-4b54-9d56-0c9b43e31bb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c51309b-6917-4b54-9d56-0c9b43e31bb3?resizing_type=fit)

## Remove Warning when Editing Files in a Changelist

By default Rider will warn you about editing files that are not in the **default** changelist. You can disable it by:

* Unchecking **Highlight files with changelist conflict**. (**Settings > Version Control > Changelists**)

  [![highlight-files-with-changelists](https://dev.epicgames.com/community/api/documentation/image/64b7ae63-9298-45c0-b147-9c404bb60236?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64b7ae63-9298-45c0-b147-9c404bb60236?resizing_type=fit)
* Alternately, use the Active/Inactive changelist system in Rider.  Go to the Perforce icon in the lower left panel to see all your open changelists. Set one of them to be the “active” one, and only work within those files.

## Open Code in Rider from the Unreal Editor

When you click on a BP node in the editor or a C++ class from the Content Browser, you want it to open Rider, rather than MSVC (Microsoft Visual C+ compiler).

In the Unreal Editor, go to **Edit > Editor Preferences… > search for: source code editor**, and set the dropdown to **Rider**.

[![General-source-code-editor-in-search-bar](https://dev.epicgames.com/community/api/documentation/image/d4031f9b-dbb5-448e-b124-3a80e2b01d6d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4031f9b-dbb5-448e-b124-3a80e2b01d6d?resizing_type=fit)

## Additional Options

### Show Whitespace and Set the Color

In **Rider’**s opening dialog box, go to **Configure > Settings > Editor** to access whitespace and text settings:

* Show/hide whitespace (and other text settings):  **Color Scheme > General > Text > Whitespaces**

  [![Text-options-in-rider-menu](https://dev.epicgames.com/community/api/documentation/image/ecd079a2-2c44-43cf-8bdb-bea4c378df61?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ecd079a2-2c44-43cf-8bdb-bea4c378df61?resizing_type=fit)
* Go to **Color Scheme > Color Scheme Font** to select from a menu of color options

  [![Color-scheme-fonts](https://dev.epicgames.com/community/api/documentation/image/70d6f329-1c6b-47ac-9d1a-1e1df6d5a500?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70d6f329-1c6b-47ac-9d1a-1e1df6d5a500?resizing_type=fit)

### Show Selected in Explorer

In **Rider**, view where your currently open file is in the directory structure.

1. Select the **Folder icon** in the left side-menu for Explorer View.
2. (Usually) You can find your file in the left panel, two folders down in the file tree.

   [![Viewing-a-file-in-the-directory](https://dev.epicgames.com/community/api/documentation/image/9e3ac6cd-c8b9-4e59-a407-180827bfc169?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e3ac6cd-c8b9-4e59-a407-180827bfc169?resizing_type=fit)
3. When an editor tab is selected, you can use this setting to have the corresponding file in Project view be selected. From **Project View Options > Behavior > Always Select Opened File**, toggle the setting to **ON**.

   [![Always-select-open-file-option-toggled-on](https://dev.epicgames.com/community/api/documentation/image/c0f989f4-bc2b-4003-879d-fb88795a9742?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0f989f4-bc2b-4003-879d-fb88795a9742?resizing_type=fit)

### Highlighting

By default this is turned off, and files have minimal syntax highlighting.

In Rider’s opening dialog box, go to **Settings > Editor > Inspection Settings > Enable Code Analysis**

### Does Unreal Game Sync run into problems with Unreal Build Tool already running (while Rider is open)?

By default, Rider regenerates the project when it detects a change to the project files or configuration. This will invoke UBT at some point, and UBT will usually still be running when UGS gets to building post-sync.

**Settings > Languages & Frameworks > C/C++ > Unreal Engine**, under Project model, select/deselect (as needed) **Regenerate project properties on project files change**.

[![Regenerate-project-properties-checkbox](https://dev.epicgames.com/community/api/documentation/image/4a448052-2e22-459d-bbca-be77fe1eb462?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a448052-2e22-459d-bbca-be77fe1eb462?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Step-by-step guide](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#step-by-stepguide)
* [Remove Warning when Editing Files in a Changelist](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#removewarningwheneditingfilesinachangelist)
* [Open Code in Rider from the Unreal Editor](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#opencodeinriderfromtheunrealeditor)
* [Additional Options](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#additionaloptions)
* [Show Whitespace and Set the Color](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#showwhitespaceandsetthecolor)
* [Show Selected in Explorer](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#showselectedinexplorer)
* [Highlighting](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#highlighting)
* [Does Unreal Game Sync run into problems with Unreal Build Tool already running (while Rider is open)?](/documentation/en-us/unreal-engine/rider-setup-guide?application_version=5.7#doesunrealgamesyncrunintoproblemswithunrealbuildtoolalreadyrunning(whileriderisopen)?)
