<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-assigning-fonts-in-unreal-engine-user-interface?application_version=5.7 -->

# Creating and Assigning Fonts

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
5. [Creating User Interfaces](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine "Creating User Interfaces")
6. [Text Formatting, Localization, and Fonts](/documentation/en-us/unreal-engine/text-formatting-localization-and-fonts-in-unreal-engine "Text Formatting, Localization, and Fonts")
7. [Fonts](/documentation/en-us/unreal-engine/using-fonts-in-unreal-engine "Fonts")
8. Creating and Assigning Fonts

# Creating and Assigning Fonts

Explains how to create Font assets that can be used with the UMG UI designer tools.

![Creating and Assigning Fonts](https://dev.epicgames.com/community/api/documentation/image/746dcf91-0aa0-4ac3-ad76-c432c563e9e2?resizing_type=fill&width=1920&height=335)

 On this page

In this guide, you'll learn how to create an empty Font asset to which you can then assign a Font Face asset or import a new TTF or OTF font file directly using the Font Editor.

![Banner Image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bad4b56-e29f-43b0-bb47-f5d94e07db3a/ue5_1-creating-fonts-banner.png)

## Steps

Follow the steps below to create your own Font asset and then learn how to assign one of your Font Face assets using the Font Editor.

For this how-to guide, we are using the **Blank Template** project, using no **Starter Content**, with default **Target Hardware** and **Project Settings**.

### Creating a Font Asset

1. Click the **Add** button inside the **Content Browser**, then select **User Interface > Font**.

   ![Create a Font Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea8b4868-279f-489e-9e0a-6c9f0ead2f6a/ue5_1-01-add-font-asset.png "Create a Font Asset")
2. A new Composite Font asset will be created, prompting you to give it a **Name**.

   ![Name a Font Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca01e5e8-0d6c-42d9-80f5-01dbacddd44f/ue5_1-02-name-font-asset.png "Name a Font Asset")
3. Once you enter a name, you will notice an asterisk appears on the asset, this indicates that the asset has not be saved. Click the **Save All** button to save your asset, then confirm the save in the pop-up menu that appears.

   ![Click the Save All button to save your asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a1abe72-81d7-4d54-b88e-4c802c6639b8/ue5_1-03-save-font-asset.png "Click the Save All button to save your asset")

### Assign a Font Face Asset

1. Now that you've created your empty Font asset, you will have to assign your Font Face(s) to be used. To do this, double-click to open your Font in the Font Editor.

   ![Open created Font Asset in Font Editor Window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c7fe777-1c52-4b07-9ecc-ac7fdc24513d/ue5_1-04-font-editor-window.png "Open created Font Asset in Font Editor Window")
2. In the Font Editor, click on the **Add Font** button to add a new Font slot.

   ![In the Font Editor add a new Font slot](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0a26c6f-c2f4-4b1a-93bd-dce89df35532/ue5_1-05-click-add-font.png "In the Font Editor add a new Font slot")
3. Name added Font slot in the Font Editor.

   ![Name added Font slot](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f999a421-c37b-4d24-8910-46a5b831cd13/ue5_1-06-name-font-slot.png "Name added Font slot")
4. Now, use the dropdown selection under the Font Name to select an existing Font Face asset that was already imported into your project.

   ![Use the dropdown selection to select an existing Font Face asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99e36c9f-ed89-4300-bcc6-ece52aaec470/ue5_1-07-assign-font-face.png "Use the dropdown selection to select an existing Font Face asset")


   If you do not have any Font Face assets, you can use the Folder icon next to the dropdown selection box to navigate and import your own TrueType Font (TTF) or OpenType Font (OTF) font file.

## End Result

Now that you've seen how to create your own Font assets and assign an already imported Font Face asset using the Font Editor, you should be able to create your own Font assets that can be used with the UMG UI Designer.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)
* [fonts](https://dev.epicgames.com/community/search?query=fonts)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/creating-and-assigning-fonts-in-unreal-engine-user-interface?application_version=5.7#steps)
* [Creating a Font Asset](/documentation/en-us/unreal-engine/creating-and-assigning-fonts-in-unreal-engine-user-interface?application_version=5.7#creatingafontasset)
* [Assign a Font Face Asset](/documentation/en-us/unreal-engine/creating-and-assigning-fonts-in-unreal-engine-user-interface?application_version=5.7#assignafontfaceasset)
* [End Result](/documentation/en-us/unreal-engine/creating-and-assigning-fonts-in-unreal-engine-user-interface?application_version=5.7#endresult)
