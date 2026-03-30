<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7 -->

# Blueprint Header View

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Blueprint Editor Reference](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine "Blueprint Editor Reference")
7. Blueprint Header View

# Blueprint Header View

The Blueprint Header View is an editor tool to provide you a method to convert Unreal Engine Blueprint Classes,Components and Variables.

![Blueprint Header View](https://dev.epicgames.com/community/api/documentation/image/af644527-73cb-42ac-b0a1-e7a646b3b53a?resizing_type=fill&width=1920&height=335)

 On this page

The **Blueprint Header View** converts Unreal Engine [Blueprint Classes](/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine) and [Blueprint Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine) to C++ code.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86fef725-4966-4193-abe4-872729b83afc/blueprintheaderview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86fef725-4966-4193-abe4-872729b83afc/blueprintheaderview.png)

During the conversion process, the Blueprint Header View creates C++-style declarations for the following elements of your Blueprint:

* [Variables](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine)
* [Functions](/documentation/en-us/unreal-engine/functions-in-unreal-engine)
* [Actor components](/documentation/en-us/unreal-engine/basic-components-in-unreal-engine)
* [Event dispatchers](/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine)

## Use the Blueprint Header View

To use the Blueprint Header View in your project, do the following:

1. Right-click a Blueprint **Class** or **Struct** in the **Content Browser**.
2. From the context menu, select **Preview Equivalent C++ Header**.

![preview-cpp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d3de1a84-08f7-47b2-bebd-70fc7a9d2709/previewcpp.png)

### C++ Header Preview

When you select **Preview Equivalent C++ Header** from the menu, the **C++ Header Preview** window opens. The window displays your Blueprint's Variables, Functions, Actor Components, and Event Dispatchers.

![cpp-header-preview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c566a9bb-3d55-4465-b39f-a03c8b00f1b7/cppheaderpreview.jpg)

### Settings

Click the **Settings** button to open a drop-down list of **style** and **sort** options.

![settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f80fbe5b-7454-41f5-82fe-442f1cc150a5/settings.png)

#### Sort Method

The **Sort Method** provides options to sort the display of your Blueprint Classes and Properties in the C++ Header Preview window. Select from the following Sort Method values:

| Sort Method | Description |
| --- | --- |
| None | Properties appear in the same order as they appear in the Blueprint class. |
| Sort By Access Specifier | Properties are grouped together by Access Specifiers in order of visibility(public, protected, private.) |
| Sort For Optimal Padding | Properties are sorted to minimize padding in the compiled class layout. |

#### Style

**Style** is similar to syntax highlighting. You can adjust the **Font Size** and **Color RGB** of the **syntax** and **selection color**, in the C++ Header preview window. You can configure the following syntax elements:

* Comment
* Error
* Macro
* Typename
* Identifier
* Keyword

![syntax-colors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06410ef4-bdca-43ca-b7c4-9b31e25e8432/syntaxcolors.png)

#### Selection Color

Changing the **Selection Color** controls the selection highlighting when using your mouse in the C++ Header Preview.

![highlight-selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e941bd0-ec83-4a5a-92dd-658a41542615/highlightcolors.png)

In the image above we set the Selection Color value to the RGB color of purple.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [header view](https://dev.epicgames.com/community/search?query=header%20view)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Use the Blueprint Header View](/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7#usetheblueprintheaderview)
* [C++ Header Preview](/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7#c++headerpreview)
* [Settings](/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7#settings)
* [Sort Method](/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7#sortmethod)
* [Style](/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7#style)
* [Selection Color](/documentation/en-us/unreal-engine/an-overview-of-the-blueprint-header-view-in-unreal-engine?application_version=5.7#selectioncolor)
