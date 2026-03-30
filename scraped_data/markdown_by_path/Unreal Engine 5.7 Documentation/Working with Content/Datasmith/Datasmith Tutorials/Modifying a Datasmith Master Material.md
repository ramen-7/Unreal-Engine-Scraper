<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/modifying-a-datasmith-master-material-in-unreal-engine?application_version=5.7 -->

# Modifying a Datasmith Master Material

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine "Datasmith")
7. [Datasmith Tutorials](/documentation/en-us/unreal-engine/datasmith-tutorials-in-unreal-engine "Datasmith Tutorials")
8. Modifying a Datasmith Master Material

# Modifying a Datasmith Master Material

Describes what to do if you need to modify the Material graph for any Material Instance created by Datasmith.

![Modifying a Datasmith Master Material](https://dev.epicgames.com/community/api/documentation/image/1f69db20-857c-4dde-a3c2-4fa942f1540f?resizing_type=fill&width=1920&height=335)

 On this page

As described in [Datasmith Overview](/documentation/en-us/unreal-engine/datasmith-plugins-overview) and [Datasmith Import Process](/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine), Datasmith creates a Material Instance in your Project to represent each different type of surface that it detects in your source scene. Each of these Material Instances exposes a pre-set list of properties, which you can modify freely in your Unreal Engine Project.

However, if you want to modify the Master Material that any of your Datasmith Material Instances are based on, always create a duplicate of the original Master Material, save that duplicate in your Project content, make your changes in the duplicate, then set the Material Instance to point to your duplicate Master Material.

The instructions below on this page provide step-by-step instructions for doing so.

* The pre-set Parent Material Assets used by Datasmith — such as the **Datasmith\_Color**, **SketchUpMaster**, and **RevitMaster** Materials — are included in the Datasmith Plugin content. If you make any changes to these Parent Materials, you'll be changing them for all your Projects, not just for your current Project. And your changes won't be saved in your Project, so if you have to distribute your Project to someone else, or upgrade to a new version of Unreal Engine, you'll lose those changes. Always make a duplicate inside your Project's content folder.
* Even when you're working with a Parent Material created by Datasmith inside your Project's content folder — typically, a Parent Material created for a custom-designed Material imported from 3ds Max or Rhino — you should always follow this same procedure to create a duplicate of the original Parent Material instead of modifying the original Parent Material directly. Changes to Parent Material graphs are not preserved as Datasmith overrides, so your changes would be lost the next time you reimport your Datasmith Scene Asset.

## Steps

To duplicate and modify the Parent Material for any Material Instance created by Datasmith:

1. Double-click the Material Instance whose Parent Material you want to modify. This opens the Material Instance in the Material Instance Editor.
2. In the **Details** panel, find the **General > Parent** setting. This identifies the Parent Material that provides the Material Graph that this Material Instance is based on.

   [![Material Instance Parent Setting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/580c489c-f3b9-4f61-8332-390c322e0aea/material-instance-parent-setting.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/580c489c-f3b9-4f61-8332-390c322e0aea/material-instance-parent-setting.png)

   Click image for full size.
3. Double-click the thumbnail image for the **Parent**.

   [![Material Instance Parent thumbnail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2563825f-63aa-43e0-8cdd-16a918cdd380/material-instance-parent-thumbnail.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2563825f-63aa-43e0-8cdd-16a918cdd380/material-instance-parent-thumbnail.png)

   Click image for full size.

   This opens the Parent Material in the Material Editor, where you can see its Material graph.

   You can also use the **Hierarchy** button in the Toolbar to choose and open the Parent Material.

   [![Material Instance Hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/edf0df96-1f59-4458-93ae-bc5416c8a8cc/material-instance-hierarchy.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/edf0df96-1f59-4458-93ae-bc5416c8a8cc/material-instance-hierarchy.png)

   Click image for full size.
4. From the main menu of the Parent's Material Editor, select **File > Save As**, and save a copy of the Parent Material anywhere in your Project's content folder.

   [![Material Parent Save As](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7830edc4-ee12-4ac2-9938-a94b38387991/material-parent-saveas.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7830edc4-ee12-4ac2-9938-a94b38387991/material-parent-saveas.png)

   Click image for full size.
5. Go back to your Material Instance, and change the **General > Parent** setting to point to your newly created Master Material.

   [![Material Instance change Parent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/041bd6c1-1f52-4cc3-ba00-7071449ad304/material-instance-change-parent.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/041bd6c1-1f52-4cc3-ba00-7071449ad304/material-instance-change-parent.png)

   Click image for full size.
6. **Save** the Material Instance.

## End Result

You've created a new Parent Material that duplicates the default Parent Material assigned by Datasmith, and you've assigned that new Parent Material to your Material Instance. Now, any changes you make to the graph and settings in your duplicated Master Material will immediately apply to your Material Instance. And, the next time you reimport your Datasmith Scene Asset, you won't lose any of the changes you made in your duplicated Parent Material.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/modifying-a-datasmith-master-material-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/modifying-a-datasmith-master-material-in-unreal-engine?application_version=5.7#endresult)

Related documents

[Material Instance Editor UI

![Material Instance Editor UI](https://dev.epicgames.com/community/api/documentation/image/6d514ff4-fd86-427c-8f64-6a30beaf3ce7?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui)
