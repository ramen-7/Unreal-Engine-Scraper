<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine?application_version=5.7 -->

# Working with Levels

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
6. [Levels](/documentation/en-us/unreal-engine/levels-in-unreal-engine "Levels")
7. Working with Levels

# Working with Levels

How to create, save, and open level assets.

![Working with Levels](https://dev.epicgames.com/community/api/documentation/image/16a1981e-827a-4d96-8f5f-8dc7ddbaa159?resizing_type=fill&width=1920&height=335)

 On this page

Like many other kinds of Unreal Engine data, **Levels** are stored in individual Asset files. You can perform many of the common Asset operations on Level Assets. However, there are some special considerations that you need to keep in mind. These will be detailed below.

This page covers the following workflows:

* Creating Levels
* Saving Levels
* Opening Levels

## Creating Levels

To create a new Level in Unreal Engine, you can use any of the following methods:

* From the **main menu**, go to **File**, then select **New Level.**
* Right-click in the **Content Browser**. Then, under **Create Basic Asset**, select **Level**.
* Use the **Ctrl + N** (Windows) or **Cmd + N** (Mac) keyboard shortcut.

Any of these actions opens the **New Level** window shown below.

![New Level window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d775200d-9d97-4857-a038-e968128c619e/new-level-window.png)

The **New Level** window displays all the Level templates available. You can choose from the following templates:

* **Open World**: A Level with sample content that uses the [World Partition](https://docs.unrealengine.com/5.0/en-US/building-virtual-worlds/world-partition) feature to create a large, streamable open world.
* **Empty Open World**: A Level that uses World Partition but does not contain any content.
* **Basic**: A Level with a floor plane, lighting, atmosphere, and exponential fog.
* **Empty Level**: A Level with nothing in it.

Select the level you want to use from this window, then click **Create**. The new Level will open automatically.

When connected to source control, new Levels that you create and save will be automatically added to source control.

## Saving Levels

Like any Asset, you need to save a Level to keep your changes when you close Unreal Engine or switch to another Level.

To save a Level, you can use any of the following methods:

* From the **main menu**, go to **File**, then select **Save Current Level.**
* Use the **Ctrl + S** (Windows) or **Cmd + S** (Mac) keyboard shortcut.

The first time you save a Level is slightly different. You need to specify where you want to save the Level Asset, and what to name it.

![Save Level As dialog window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7183c14e-c487-4375-a517-03d5f5fe18e5/save-level-as.png)

The Save Level As window behaves the same as any other file save dialog. Give your Level Asset a name, select the folder where you want to save it, and click Save.

To save a copy of a Level under a different name, you can use any of the following methods:

* From the **main menu**, go to **File**, then select **Save Current Level As.**
* Use the **Ctrl + Alt + S** (Windows) or **Cmd + Option + S** (Mac) keyboard shortcut.

Changing Levels will prompt you to save your current Level(s) with the **Save Content** dialog.

## Opening Levels

To open a Level, you can use any of the following methods:

* From the **main menu**, go to **File**, then select **Open Level** and choose the Level to open**.**
* Use the **Ctrl + O** (Windows) or **Cmd + O** (Mac) keyboard shortcut.

* [levels](https://dev.epicgames.com/community/search?query=levels)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Levels](/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine?application_version=5.7#creatinglevels)
* [Saving Levels](/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine?application_version=5.7#savinglevels)
* [Opening Levels](/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine?application_version=5.7#openinglevels)
