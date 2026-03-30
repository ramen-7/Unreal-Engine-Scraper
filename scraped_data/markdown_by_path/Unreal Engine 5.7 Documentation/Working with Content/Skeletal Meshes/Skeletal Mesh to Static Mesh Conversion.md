<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-to-static-mesh-conversion-in-unreal-engine?application_version=5.7 -->

# Skeletal Mesh to Static Mesh Conversion

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
6. [Skeletal Meshes](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine "Skeletal Meshes")
7. Skeletal Mesh to Static Mesh Conversion

# Skeletal Mesh to Static Mesh Conversion

Learn how to convert Skeletal Meshes to Static Meshes.

![Skeletal Mesh to Static Mesh Conversion](https://dev.epicgames.com/community/api/documentation/image/80e762cf-af91-4153-87c8-040acd5af226?resizing_type=fill&width=1920&height=335)

 On this page

When creating splash-screens, screenshots, or other in-game static versions characters, it can be helpful to non-destructively convert a posed [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) assets to [Static Mesh](/documentation/en-us/unreal-engine/static-meshes), in order to preserve its position and reduce the render cost of the still objects.

The following document will provide an example workflow of how to pose and convert a **Skeletal Mesh** asset to a **Static Mesh** asset in Unreal Engine.

#### Prerequisite

* Your project contains a **Skeletal Mesh** character.

## Posing Skeletal Meshes

To begin posing a Character in Unreal Engine, open the Skeletal Mesh asset in the [Skeletal Mesh Editor](/documentation/en-us/unreal-engine/skeletal-mesh-editor-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7832a4e-03bd-4264-93b8-fd08c26fa118/skelmesheditor.png)

To expose the Skeletal Mesh's bones, in order to manipulate their position, navigate in the **Viewport** panel to **Character** > **Bones** and toggle the **All Hierarchy** option.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/539390b4-d19f-4582-96c5-351f1593c46d/exposebones.png)

Select a bone to adjust by clicking on it, and then use the **Move**, **Rotate**, and **Scale** tools, to manipulate your character's pose.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7869737c-665f-4813-8c7d-a85bd8ba9f53/manipulatetools.gif)

## Saving Skeletal Mesh Poses

After Manipulating your character's pose to your desired position, you can then save the pose as a Static Mesh asset using the **Make Static Mesh** button in the Skeletal Mesh Editor's **toolbar**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64f434cb-3d9a-4019-b4ae-004a0a13e954/makestaticmesh.png)

**Name** and select a location to save the new Static Mesh asset, and then select **Save**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2cc7831e-a1d7-422a-9df6-1ed2fc47666e/save.png)

You can now use your converted Static Mesh in your project.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba0388d7-d051-4915-9d5a-025c6ef322b8/placestatic.gif)

After converting your Skeletal Mesh to a Static Mesh you can safely reposition your mesh to its reference pose by re-importing your Skeletal Mesh's `.fbx` source file using the **Reimport Base Mesh** button in the Skeletal Mesh Editor's **toolbar** or by manually reverting your manipulation edits using **Ctrl** + **Z**.

If you do not revert your bone manipulation edits, your Skeletal Mesh's Animation Sequences will not play properly.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1273300b-b1f0-4ecd-b294-0693f6942604/reimport.png)

You can also save posed Skeletal Meshes as [Animation Sequences](/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) and [Pose assets](/documentation/en-us/unreal-engine/animation-pose-assets-in-unreal-engine) for other more dynamic use cases using the Create Asset button in the Skeletal Mesh Editor's toolbar.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b383fea7-71ae-4030-aefc-eded6c24fc7a/createasset.png)

For more information about using saved Skeletal Mesh poses, see the following documentation:

[![Animation Pose Assets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/864732bd-8b40-4a56-b856-970a9bddd5e4/topicimage.png)

Animation Pose Assets

Describes the Animation Pose Asset which can be used to drive animation through weighted curve data.](/documentation/en-us/unreal-engine/animation-pose-assets-in-unreal-engine)

## Converting Multiple Skeletal & Static Meshes

You can also convert a group of Static or Skeletal mesh objects, that have been placed into a level, to a single Static Mesh asset, in order to pose multiple characters together, or combine characters with other objects such as backgrounds or weapons. After placing and positioning your objects in a level, you can multi-select each object you want to convert to a static mesh, and then navigate in the **Menu Bar** to **Actor** > **Convert Actors to Static Mesh**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8da2e746-60c0-4cf4-b679-eb77d1dc039c/convertinscene.png)

**Name** and select a location to save the new Static Mesh asset and then select **Save**. You can now use the converted Static Mesh in your project.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9ee9bf8-0b4b-4901-8de9-4d12a2e56f99/staticscene.gif)

You can also convert groups of game objects to a single Static Mesh during **Play In Editor** (**PIE**), and other simulation modes within the editor, such as recorded gameplay segments using the [Rewind Debugger](/documentation/en-us/unreal-engine/animation-rewind-debugger-in-unreal-engine) to save more dynamic gameplay snapshots.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a71bb24e-8693-48ce-8bcc-305a13d2a0e4/pie.gif)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [static mesh](https://dev.epicgames.com/community/search?query=static%20mesh)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisite](/documentation/en-us/unreal-engine/skeletal-mesh-to-static-mesh-conversion-in-unreal-engine?application_version=5.7#prerequisite)
* [Posing Skeletal Meshes](/documentation/en-us/unreal-engine/skeletal-mesh-to-static-mesh-conversion-in-unreal-engine?application_version=5.7#posingskeletalmeshes)
* [Saving Skeletal Mesh Poses](/documentation/en-us/unreal-engine/skeletal-mesh-to-static-mesh-conversion-in-unreal-engine?application_version=5.7#savingskeletalmeshposes)
* [Converting Multiple Skeletal & Static Meshes](/documentation/en-us/unreal-engine/skeletal-mesh-to-static-mesh-conversion-in-unreal-engine?application_version=5.7#convertingmultipleskeletal&staticmeshes)
