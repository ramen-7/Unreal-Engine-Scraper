<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/developers-folder-in-unreal-engine?application_version=5.7 -->

# Developers Folder

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
6. [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine "Content Browser")
7. Developers Folder

# Developers Folder

Iterate and collaborate with other developers using the Developers folder.

![Developers Folder](https://dev.epicgames.com/community/api/documentation/image/41193fc5-e159-44a1-848b-3b977e6cd54d?resizing_type=fill&width=1920&height=335)

 On this page

The **Developers** folder in the **Content Browser** is where you can duplicate and work on Assets without worrying about breaking things in your project. Use the Developers folder to experiment with different things, from small-scale Asset modification to project-wide refactors.

If you work in a shared project with other developers, each developer has their own folder.

The Developers folder uses the same name as your Windows username, but without characters that aren't allowed in Unreal Engine folder names, like periods or spaces.

Because the Developers folder is meant to act as a sandbox environment, you should never reference Assets from this folder anywhere outside this folder. Doing so can cause errors when cooking the project or cause cooking to fail.

## Enabling the Developers Folder

If you don't see the Developers folder in your Content Browser, follow these steps to enable it:

1. In the **Content Browser**, click **Settings**.
2. From the Settings menu, enable the **Show Developer Content** option.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/577cd545-0075-439f-bf99-c284596ef399/ue5_1-enable-developers-folder.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/577cd545-0075-439f-bf99-c284596ef399/ue5_1-enable-developers-folder.png)

Click the image for full size.

## Collaborating with Other Developers

If you use [source control](/documentation/en-us/unreal-engine/source-control-in-unreal-engine), you can configure Unreal Engine to see Assets in other developers' folders. To do this, follow these steps:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20c98a07-b00e-4602-8dee-ae3db9588ca3/ue5_1-other-developers-filter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20c98a07-b00e-4602-8dee-ae3db9588ca3/ue5_1-other-developers-filter.png)

Click the image for full size.

1. In the **Content Browser**, click the **Filters** button.
2. From the Filters menu, select **Other Filters > Other Developers**.

## Excluding the Developers Folder from Cooked Builds

If you want to make sure that you don't accidentally package broken or in-progress Assets, you can exclude the Developers folder from cooked builds.To do this, follow these steps:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11e12369-81c0-4e91-ab31-ddb32ad318ed/ue5_1-directories-to-never-cook.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11e12369-81c0-4e91-ab31-ddb32ad318ed/ue5_1-directories-to-never-cook.png)

Click the image for full size.

1. From the main menu, go to **Edit > Project Settings** and search for the **Directories to never cook** array.

   You can find this array by using the **Search** box at the top of the section.
2. Click the **Add (+)** button to add a new item to the array.
3. Click **…** to open a list of folders in your project.
4. Click the **Developers** folder to select it.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling the Developers Folder](/documentation/en-us/unreal-engine/developers-folder-in-unreal-engine?application_version=5.7#enablingthedevelopersfolder)
* [Collaborating with Other Developers](/documentation/en-us/unreal-engine/developers-folder-in-unreal-engine?application_version=5.7#collaboratingwithotherdevelopers)
* [Excluding the Developers Folder from Cooked Builds](/documentation/en-us/unreal-engine/developers-folder-in-unreal-engine?application_version=5.7#excludingthedevelopersfolderfromcookedbuilds)
