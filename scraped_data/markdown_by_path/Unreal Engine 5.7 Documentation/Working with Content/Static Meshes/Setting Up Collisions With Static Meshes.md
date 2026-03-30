<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine?application_version=5.7 -->

# Setting Up Collisions With Static Meshes

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
6. [Static Meshes](/documentation/en-us/unreal-engine/static-meshes "Static Meshes")
7. Setting Up Collisions With Static Meshes

# Setting Up Collisions With Static Meshes

How To Set Up Collision

![Setting Up Collisions With Static Meshes](https://dev.epicgames.com/community/api/documentation/image/c3167b9c-dbb4-4516-a1bf-d0709e4f775f?resizing_type=fill&width=1920&height=335)

 On this page

In **Unreal Engine**, you can have **Static Meshes** do many things, such as change its **Texture** or **Material** during gameplay, or move throughout your **Level** using **Sequencer**. It is likely, whatever you have your Static Mesh do in your Level, you do not want to have the player be able to walk or shoot through the mesh. That is where setting up collision on your Static Mesh is useful.

## Set Up

To start, create a new project using the **First Person Game** template and enable **Starter Content.** For more information on creating new projects in Unreal Engine, refer to [Creating a New Project.](/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine)

You may already have a level and Static Meshes of your own to work with. If you do, you can skip this step. However, with the template, you can fire projectiles to demonstrate a point later discussed, so using this template may help you follow along.

[![New Project With Starter Content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc823b69-ad6c-49ac-b9bc-19bdce0c27e7/01-new-project-with-starter-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc823b69-ad6c-49ac-b9bc-19bdce0c27e7/01-new-project-with-starter-content.png)

Click image for full size.

Once the project is open, in the **Content Browser** you can use the search bar or navigate to **Content > Starter Content > Props** to open the **Static Mesh** named **SM\_Door**.

[![Content Browser With Starter Content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1256e87-3c85-4a76-9840-c037853a5fc2/02-content-browser-with-starter-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1256e87-3c85-4a76-9840-c037853a5fc2/02-content-browser-with-starter-content.png)

Click image for full size.

[![Door In Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b282d69b-2a80-455c-9b75-030601c9195f/03-door-in-content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b282d69b-2a80-455c-9b75-030601c9195f/03-door-in-content-browser.png)

Click image for full size.

**SM** in **SM\_Door** stands for Static Mesh and follows the standard naming convention recommended by Unreal Engine. Following a consistent naming convention helps maintain an organized project. To learn more about naming files in Unreal Engine, refer to [Recommended Asset Naming Conventions](/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects).

  

Once you have found **SM\_Door**, go ahead and open up the **Static Mesh Editor** by either:

* **Double-clicking** on the asset.
* **Right-clicking** on the asset and selecting **Edit** from the context menu.

When the editor opens, you will see something similar to what is shown below:

[![Default Door](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f40f1df8-410d-4152-ad90-6c697fdb6b21/04-default-door.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f40f1df8-410d-4152-ad90-6c697fdb6b21/04-default-door.png)

Click image for full size.

## Collision On a Simple Shaped Mesh

By default, there is no collision mesh set on the door. Without collision, the player can walk through the door.

You can test this by placing the door into your Level before setting up collision, then play the Level.

![No Collision on Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2a842013-d97c-4db8-a9be-f24a95e60201/no-collision-on-static-mesh.gif "No Collision with Door Mesh")

Also, if you want the door to blow away when you shoot it or fall to the ground when placed in the sky, you will need to set **Simulate Physics** to *true* from the **Details** panel. However, this option is not available by default if the Static Mesh does not have a collision.

[![Physics Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5372a1b8-3acc-4b47-8817-9017490311f9/simulate-physics-details-panel-not-active.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5372a1b8-3acc-4b47-8817-9017490311f9/simulate-physics-details-panel-not-active.png)

Click image for full size.

These effects are undesirable in most cases, so go ahead and set up collision for this Static Mesh.

In the menu bar at the top of the Static Mesh Editor, there is a **Collision** dropdown menu. Click it to see the options for adding collision to your mesh. You can also access these options by clicking the **Collision** dropdown menu in the toolbar (![Collision Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7afee584-df86-4839-b28a-cec5ff7f4440/13-collision-button.png "Collision Button")) . To learn more about the layout of the Static Mesh Editor, refer to [Static Mesh Editor UI](/documentation/en-us/unreal-engine/static-mesh-editor-ui-in-unreal-engine).

[![Collision Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f223a11-4ed8-478f-9f60-7c263ee827b7/collision_menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f223a11-4ed8-478f-9f60-7c263ee827b7/collision_menu.png)

Click image for full size.

The door mesh is a rather simple shape. This makes things easy when trying to set up collision for your Static Mesh.

The top three options in the **Collision** menu surround your Static Mesh with a simple collision shape used as the bounds of what can and cannot be blocked or overlapped with your mesh. Below are examples of the door mesh with these collision meshes.

|  |  |  |
| --- | --- | --- |
| Sphere 1 | Capsule 1 | Box 1 |
| Sphere 2 | Capsule 2 | Box 2 |
| Sphere Simplified Collision | Capsule Simplified Collision | Box Simplified Collision |

If you already have a Simplified Collision on a mesh and you add another, the new collision does not replace the other collision, but adds to it.

Adding all three of the Simplified Collisions from above gives you something that looks like the image below.

[![All Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b69348bd-329d-49b9-8f36-89600f5bb81c/14-all-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b69348bd-329d-49b9-8f36-89600f5bb81c/14-all-collision.png)

Click image for full size.

To solve this, you can do one of the following:

* Select one of the collisions and press the **delete** key.
* Select **Delete Selected Collision** from the **Collision** dropdown menu to remove them one by one.
* In the **Collision** menu, select **Remove Collision** to remove all collisions on the Static Mesh.

[![Remove Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/716c4d28-c4d4-4648-9ab0-21bc8eb49b78/15-remove-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/716c4d28-c4d4-4648-9ab0-21bc8eb49b78/15-remove-collision.png)

Click image for full size.

After applying the collision, click the collision mesh to notice a translation widget. You can translate, rotate, and scale the collision mesh like you would with any other object within the engine.

## Collision On a More Complex Mesh

Using the simple collision mesh you set up in the last section will work fine for:

* A Static Mesh that can easily fit into a capsule or box.
* A Static Mesh where having precise collision does not matter.

However, you may have a Static Mesh with a more complex shape requiring a precise collision. This section will go over how to set that up.

Back in the **Props** folder, within the **Starter Content**, browse to the Static Mesh **SM\_Chair**. **Double-click** on the thumbnail to open it up in the Static Mesh Editor.

As you can see, this mesh already has collision on it, and looks similar to what is shown below:

[![Chair Default Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c21b2373-49c1-4019-8ce9-89ed6e07482a/16-chair-default-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c21b2373-49c1-4019-8ce9-89ed6e07482a/16-chair-default-collision.png)

Click image for full size.

Let's assume you want the player to be able to sit on the cushion of the chair. The default collision mesh of the chair has an invisible barrier that would prevent the player from sitting.

When the player is playing the game, they only see the Static Mesh itself, not the collision mesh. The player would try to sit on the chair and not know why something is blocking their way.

Remove the collision mesh by selecting **Remove Collision** from the **Collision** dropdown menu. You can try to use the primitive shapes you used in the previous section, but as you can see in the images below, none look quite right.

|  |  |  |
| --- | --- | --- |
| Chair Sphere | Chair Capsule | Chair Box |
| Sphere Simplified Collision | Capsule Simplified Collision | Box Simplified Collision |

It seems none of the primitive shapes quite achieve the precise collision needed. However, you can get closer with the other options within the **Collision** dropdown menu. These options are called the **K-DOP** Simplified Collision generators.

K-DOP is a type of bounding volume, which stands for K discrete oriented polytope (where K is the number of axis-aligned planes). Basically, it takes K axis-aligned planes and pushes them as close to the Static Mesh as possible. You use the resulting shape as a collision hull.

In the Static Mesh Editor K can be:

* **10** - Box with 4 edges beveled - you can choose X- Y- or Z-aligned edges.
* **18** - Box with all edges beveled.
* **26** - Box with all edges and corners beveled.

[![K-DOP Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9f8cf26-0194-48c0-a0c3-d8f6713f5a3e/20-k-dop-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9f8cf26-0194-48c0-a0c3-d8f6713f5a3e/20-k-dop-options.png)

Click image for full size.

Here is what your chair mesh looks like with 10-DOP, 18-DOP, and 26-DOP respectively.

|  |  |  |
| --- | --- | --- |
| 10-DOP | 18-DOP | 26-DOP |
| 10DOP | 18DOP | 26DOP |

These collision options are closer to the precision needed, but there is still a gap between the cushions that might prevent the player from sitting down in the chair.

Select **Remove Collision** one more time. Next, select **Auto Convex Collision** from the **Collision** dropdown menu.

[![Auto Convex Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8011e58c-20e9-46f3-9adf-361d6c6e0236/24-auto-convex-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8011e58c-20e9-46f3-9adf-361d6c6e0236/24-auto-convex-collision.png)

Click image for full size.

The **Convex Decomposition** panel, pictured below, will then appear in the **Details** panel.

[![Convex Decomposition](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba40e4a3-0d7f-4c1c-8af7-21123f5968c2/25-convex-decomposition.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba40e4a3-0d7f-4c1c-8af7-21123f5968c2/25-convex-decomposition.png)

Click image for full size.

The table below describes each option in the **Convex Decomposition** panel.

| Option | Description |
| --- | --- |
| **Hull Count** | Determines the number of primitives to represent the collision mesh. |
| **Max Hull Verts** | Increases or decreases the number of vertices your collision mesh has. |
| **Hull Precision** | Number of voxels to use when generating the collision mesh. |

The higher these values, the more precise your collision mesh will be, but also the more complex. Clicking **Apply** applies these settings to your Static Mesh and makes the collision mesh visible.

|  |  |
| --- | --- |
| Auto Convex Collision | Auto Convex Collision |
| Default Settings | Max Accuracy and Max Hull Verts |

Another way to set up a precise collision is by using multiple Simplified Collision meshes. If you remember from earlier, creating another Simplified Collision mesh does not replace the original one but adds to it. Also, each collision mesh has its own transform widget allowing you to translate, rotate, and scale individually. You can use this to create a custom collision mesh for your Static Mesh.

To get started select **Add Box Simplified Collision** from the **Collision** dropdown menu. **Click** the collision mesh to bring up its transform widget.

Next, translate, rotate, and scale the collision mesh so that it fits along the arm of the chair down to the ground.

![Custom Box Collision Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a206304-a397-4960-8373-300e6262af0f/box-collision-mesh-around-arm.gif "Collision Mesh Around Arm")

With the collision mesh still selected, duplicate the collision mesh by either selecting **Duplicate Selected Collision** from the Collision dropdown menu or by pressing **Ctrl + D**.

Next, move this collision mesh so that it fits along the other arm of the chair.

[![Custom Box Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e21c2e9b-00ec-4eef-8a59-9f2cfebd7c8c/custom-collison-mesh-arm.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e21c2e9b-00ec-4eef-8a59-9f2cfebd7c8c/custom-collison-mesh-arm.png)

Click image for full size.

Duplicate the collision mesh again. With this new mesh selected, move, scale, and rotate the mesh to fit along the bottom of the chair.

[![Custom Box Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a422e60-488a-4adf-ad55-9ab3df570ccc/custom-collison-mesh-bottom-chair.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a422e60-488a-4adf-ad55-9ab3df570ccc/custom-collison-mesh-bottom-chair.png)

Click image for full size.

Duplicate that collision mesh and move it up, so it fits along the chair's seat.

[![Custom Box Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4cc1cfd-1933-4a56-97fb-c304045b94a5/custom-collison-mesh-seat.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4cc1cfd-1933-4a56-97fb-c304045b94a5/custom-collison-mesh-seat.png)

Click image for full size.

Duplicate the collision mesh one more time and rotate it, so it fits along the back of the chair.

When you are done, you will have something that looks similar to this:

[![Composite Box Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/264a8c31-d639-462e-8974-1d355f2e7baa/28-composite-box-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/264a8c31-d639-462e-8974-1d355f2e7baa/28-composite-box-collision.png)

Click image for full size.

You could go back and follow the shape of the chair more closely, but for now the current collision mesh will allow a player to sit on the cushion.

## Simulating Physics and Collision Presets

With collision applied to your Static Mesh, it can now simulate physics. Save your chair mesh by clicking the **Save** button on the left of the Toolbar within the Static Mesh Editor.

Next find **SM\_Chair** inside your **Content Browser** and drag it into the level. With it still selected, look at the **Details** panel.

In the **Physics** section of the **Details** panel, the **Simulate Physics** option is now available and will be *false* by default. If you play the Level now with Simulate Physics set to *false*, walking into the chair or shooting projectiles at it has no effect. However, your character can not walk through the chair as it now has a collision.

To shoot projectiles at the chair using the First Person Shooter template, you need to walk your character into the weapon to collect it, then **Click** to shoot.

[![Physics Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abbc2259-c37e-4195-a9ec-b682bfd96cc1/simulate-physics-false.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abbc2259-c37e-4195-a9ec-b682bfd96cc1/simulate-physics-false.png)

Click image for full size.

Stop playing the Level and set **Simulate Physics** to *true*. Now when you play, notice the chair moves when the player walks into it. The Static Mesh also gets shot across the level and into the air when you shoot at it.

![Simulate Physics Active for Static Mesh Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba097032-a1cf-4d44-896b-6a1bf456d72f/simulate-physics-active.gif "Simulate Physics Active")

This is not only because the Static Mesh is simulating physics, but also because the mesh is set to **Physics Actor** by default under **Collision Preset**.

Go back to the **Details** panel for the chair and in the **Collision** section, there is a dropdown menu labeled **Collision Presets**. The way this instance of the Static Mesh reacts to other objects in the world depends on what its **Collision Presets** are. Take a look at the options you have, which are shown below.

[![Collision Presets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4dd64da-ac90-4729-979d-558fefee699b/collision-preset-physics-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4dd64da-ac90-4729-979d-558fefee699b/collision-preset-physics-actor.png)

Click image for full size.

If you switch it to **Overlap All**, as soon as play begins, you see the Static Mesh fall right through the level. There is also a custom preset, which allows you to manually set how the mesh responds to different objects in your level.

You may want it to block Pawns, but overlap Projectiles, and ignore everything else. In the custom preset, you can tell the Static Mesh to do that.

When selecting a **Static Mesh Actor** in the level editor, or any **Static Mesh Component** such as those in the Blueprint Editor, the **Details Panel > Collision Category > Collision Presets** will show **Default**. This indicates there has been no change to the Collision Preset from what it was initially set to. If something else is listed here, such as **BlockAll**, that indicates the selected Static Mesh Actor / Component has had its Collision Preset overridden.

[![Default Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29fef2f9-0f0a-4ff3-a07f-092f2dfdcc2c/31-default-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29fef2f9-0f0a-4ff3-a07f-092f2dfdcc2c/31-default-collision.png)

Click image for full size.

Now that you have collision set up on your mesh, you are ready to place it in your Level and use its collision to set up how it affects and can be affected by other objects.

To continue learning about collisions in Unreal Engine, refer to the [Collision](/documentation/en-us/unreal-engine/collision-in-unreal-engine) documentation.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Set Up](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine?application_version=5.7#setup)
* [Collision On a Simple Shaped Mesh](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine?application_version=5.7#collisiononasimpleshapedmesh)
* [Collision On a More Complex Mesh](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine?application_version=5.7#collisiononamorecomplexmesh)
* [Simulating Physics and Collision Presets](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine?application_version=5.7#simulatingphysicsandcollisionpresets)
