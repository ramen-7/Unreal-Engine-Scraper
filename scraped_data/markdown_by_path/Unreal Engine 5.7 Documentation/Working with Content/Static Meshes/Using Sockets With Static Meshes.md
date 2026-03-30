<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7 -->

# Using Sockets With Static Meshes

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
7. Using Sockets With Static Meshes

# Using Sockets With Static Meshes

How To Set Up and Use Sockets with Static Mesh Actors

![Using Sockets With Static Meshes](https://dev.epicgames.com/community/api/documentation/image/2ba7a8bb-d39c-49f1-ba9b-bc81f66f83df?resizing_type=fill&width=1920&height=335)

 On this page

While making your **Level** in **Unreal Engine**, there may come a time when you want to attach something to your **Static Mesh**. You could parent an object to the Static Mesh in the **World Outliner**. However, you still have to position it in the exact place you want it on your mesh, which can get tedious. **Sockets** are attach points you can place on your Static Mesh. Once set up, you can connect objects to the Socket. This tutorial will show you how to create a Socket for your Static Mesh and use it for your Level.

## Set Up

If you already have a project that you are working on, you can use that project to follow along. If you do not, start out by launching Unreal Engine and creating a new project with **Starter Content** enabled. For this guide the First Person Template is used, but you can use whichever template you would like. For more information on creating new projects in Unreal Engine, refer to [Creating a New Project](/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine).

Once your project is open, find the **Starter Content** folder within the **Content Browser**. Next, navigate to the **Props** folder and find the Static Mesh named **SM\_DoorFrame**.

If you are working on a project but didn't enable Starter Content, you can import the **Assets** from the Content Browser. Choose **Add Feature or Content Pack** from the **Add** dropdown menu. Refer to [Content Browser Interface](/documentation/en-us/unreal-engine/content-browser-interface-in-unreal-engine) for more information.

[![Content Browser With Starter Content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb5da766-45f4-4f13-9b0d-f20cfb1f4499/01-content-browser-with-starter-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb5da766-45f4-4f13-9b0d-f20cfb1f4499/01-content-browser-with-starter-content.png)

Click image for full size.

[![Door Frame In Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/502c8e80-bb07-4037-902c-547a71b213dd/02-door-frame-in-content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/502c8e80-bb07-4037-902c-547a71b213dd/02-door-frame-in-content-browser.png)

Click image for full size.

Open **SM\_DoorFrame** in the **Static Mesh Editor** by doing one of the following:

* **Double-clicking** the Asset.
* **Right-clicking** the Asset and selecting **Edit** from the context menu.

After, the door frame will appear in the Static Mesh Editor, as shown below.

[![Door Frame In Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4ab5846-e9bf-4655-98bb-a0a07a0c7159/03-door-frame-in-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4ab5846-e9bf-4655-98bb-a0a07a0c7159/03-door-frame-in-editor.png)

Click image for full size.

## Creating Your First Socket

With the Static Mesh opened in the Static Mesh Editor, you can create a socket to place a fire particle in the middle of the doorway.

To start, click the **Window** dropdown menu at the top of the Static Mesh Editor and select **Socket Manager**.

[![Window Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16f1bfdf-6dea-40cb-bc54-2f4b9adf24a4/04-window-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16f1bfdf-6dea-40cb-bc54-2f4b9adf24a4/04-window-menu.png)

Click image for full size.

The Socket Manager window will appear next to the **Details** panel, as shown below. Once opened, click **Create Socket** (![Create Socket Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd870907-b43c-4776-8de5-b2918fbc4284/05-creat-socket-button-1.png "Create Socket Button")).

[![Create Socket Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2020b54-2c15-4c84-8f1c-d39b7eae272e/06-create-socket-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2020b54-2c15-4c84-8f1c-d39b7eae272e/06-create-socket-button.png)

Click image for full size.

After clicking the button the Socket is created and you are prompted to rename it. In this example, **Fire** is used.

[![New Socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/951ba014-7c7c-41aa-a551-d6001ee62146/renaming-socket-fire.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/951ba014-7c7c-41aa-a551-d6001ee62146/renaming-socket-fire.png)

Click image for full size.

Looking at your Static Mesh in the Viewport, you can see a translation widget for the Socket. If not, make the Socket visible by clicking it in the Viewport or the Socket Manager panel.

[![Sockets Transform Widge](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0051c6e2-628a-41c9-8c2e-bf4361b800c5/socket-transform-widget.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0051c6e2-628a-41c9-8c2e-bf4361b800c5/socket-transform-widget.png)

Click image for full size.

Once you can see the Socket, you may notice the location is incorrect. By default, when you create a new Socket, it is located at the origin of the Static Mesh. In this case, the bottom center of the door frame.

You can use the translate widget in the Viewport to move the Socket manually to the desired location or change its relative location, rotation, and scale from within the **Socket Manager** panel. For this guide, you want the Socket in the middle of the doorway so the player will have to walk through fire as they go through the door.

Change the value of **Z** in its Relative Location from 0 to 115, as shown in the image below.

[![Fire Socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d397788e-fbf5-45e8-92cb-a8e7bdf2557f/fire-socket-relative-location.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d397788e-fbf5-45e8-92cb-a8e7bdf2557f/fire-socket-relative-location.png)

Click image for full size.

## Attaching Objects to a Static Mesh

With a Socket placed on Static Mesh, you can begin to attach objects to your Static Mesh in your Level.

Click **Save** in the Toolbar inside the Static Mesh Editor and return to the Level Editor.

Find **SM\_DoorFrame** inside your **Content Browser** and drag a copy into your Level. Next, go to the **Particles** folder inside the **Starter Content** folder and find the Asset named **P\_Fire**.

[![Fire Particle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a324fa36-05db-4a55-9a2a-891b5fbb2210/10-fire-particle.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a324fa36-05db-4a55-9a2a-891b5fbb2210/10-fire-particle.png)

Click image for full size.

Drag a copy of **P\_Fire** into your Level as well. This particle effect will serve as the fire attached to **SM\_DoorFrame**.

Once you dragged in an instance of **P\_Fire**, **right-click** the particle inside the Viewport to open the context menu.

[![Context Menu For Fire](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/587476b8-aad3-4d2e-a848-ea3c091559ee/11-context-menu-for-fire.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/587476b8-aad3-4d2e-a848-ea3c091559ee/11-context-menu-for-fire.png)

Click image for full size.

In the context menu, select **Attach To**. Inside the search box, type **Door Frame** and select **SM\_DoorFrame**.

[![Fire Attach To Frame](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eaf13609-21f7-4575-9b7f-7f5e415721c2/12-fire-attach-to-frame.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eaf13609-21f7-4575-9b7f-7f5e415721c2/12-fire-attach-to-frame.png)

Click image for full size.

Once you select **SM\_DoorFrame**, choose where you want to attach the object. The list consists of **None** and every Socket you created for your Static Mesh. Select **Fire** from the list.

[![Choose Socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/474b01a2-bd8d-47e0-b377-b8708b9f16a3/select-fire-socket.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/474b01a2-bd8d-47e0-b377-b8708b9f16a3/select-fire-socket.png)

Click image for full size.

In the Outliner, **P\_Fire** is now a child of **SM\_DoorFrame**, but you may notice the particle effect did not snap to the location of the Socket. For that to happen, you need to reset the transform location of the particle effect.

[![Socket Child of Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec14b158-6b6d-4b3e-8895-2c0a46708827/socket-child-of-static-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec14b158-6b6d-4b3e-8895-2c0a46708827/socket-child-of-static-mesh.png)

Click image for full size.

With **P\_Fire** selected go to the **Transform** section of the **Details** panel. To the far right of the **Location** bar click the reset arrow (![Reset to Default Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7732763d-4762-489b-8a3c-440425056f78/reset-to-default-button.png "Reset to Default Button")) to change the settings back to default.

As a child of **SM\_DoorFrame**, the particle effect's location is now relative to its parent. Therefore the transform values reset to 0,0,0 as it snaps to the Socket.

[![Reset Asset's Transform to Default](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed59c56e-51aa-4d98-b137-ae1bdc336c59/reset-transform-to-default.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed59c56e-51aa-4d98-b137-ae1bdc336c59/reset-transform-to-default.png)

Click image for full size.

The particle effect is now attached to your Static Mesh.

![Fire Socket Attached to Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/765b13d4-1173-4c49-a033-64d40f5b1633/walking-through-fire-socket.gif)


With the particle effect attached to the Static Mesh via its Socket, you can still move, rotate, and scale the particle effect separately from the Static Mesh. However, any transformations made to the Static Mesh also affect any objects attached.

## Detaching

Detaching an object from a Static Mesh follows similar steps as attaching an object.

**Right-click** on the object you want to detach, and select **Detach** from the context menu. The object is no longer a child of the Static Mesh.

[![Detach](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7f2d384-3270-4ac0-8b70-6f68bd0275d6/15-detach.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7f2d384-3270-4ac0-8b70-6f68bd0275d6/15-detach.png)

Click image for full size.

## Creating a Doorway With a Solid Door

Now that you have used Sockets to create a fiery doorway, it is time to create something more practical.

In the **Props** folder within the **Starter Content**, find **SM\_DoorFrame** and drag another copy of it into the Level. Next, find **SM\_Door**, and drag it into the Level.

[![Door Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/731f8b1f-26e0-4c37-bb22-0d0eadd23e98/door-static-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/731f8b1f-26e0-4c37-bb22-0d0eadd23e98/door-static-mesh.png)

Click image for full size.

You could attach the door to the door frame using the Socket already created, but there is a problem. The Static Mesh **SM\_Door** has an origin at the bottom corner, so attaching the door to the **Fire** Socket will leave the door floating in the air and bursting through the corner of the doorway. To fix this problem, you are going to make another Socket.

### Creating a New Socket

Reopen **SM\_DoorFrame** in the Static Mesh editor and add a new Socket in the **Socket Manager** panel. Name the Socket door, so later you know this is where you want to attach the door mesh.

You can manually move the Socket using the 3D widget, or you can move it by changing the relative location, rotation, and scale from within the **Socket Manager** panel. For this example, changing the Socket's relative location's value of **Y** to 42 places the Socket at the bottom corner of the door frame mesh.

[![Door Socket](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb0724e0-4d0f-4ff3-a2ae-8411c12d2db4/door-socket.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb0724e0-4d0f-4ff3-a2ae-8411c12d2db4/door-socket.png)

Click image for full size.

If you do not see the sockets, highlight the Sockets Button so that sockets are visible.

[![Sockets Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/894dad86-070c-4e4a-b29c-e5debac276f7/17-sockets-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/894dad86-070c-4e4a-b29c-e5debac276f7/17-sockets-button.png)

Click image for full size.

### Attaching the Door to the Frame

Now that you have a socket to attach the door to the frame, save your door frame mesh and return to the Level Editor.

Select the instance of the door mesh in your Level and **right-click** to bring up its context menu.

From within the context menu, select **Attach** and search for **SM\_DoorFrame**.

Find the instance of the door frame you want to attach the door to and select it. When asked which Socket to connect to to, select **Door**.

[![Door Socket Complete](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f23ad7d7-95c4-4200-991b-698542f322e6/18-door-socket-complete.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f23ad7d7-95c4-4200-991b-698542f322e6/18-door-socket-complete.png)

Click image for full size.

By default, **SM\_Door** will not have a collision set. If you play the Level now, the player can walk through the solid door, which is not very useful. Set a **Simple Box Collison** for the door inside the Static Mesh Editor. Refer to [Setting Up Collisions with Static Mesh](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine) to learn how.

After setting the collision, use Blueprints for scripting a behavior for the door to open and close. Learn how with the [Opening Doors](/documentation/en-us/unreal-engine/opening-doors-in-unreal-engine) guide.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Set Up](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#setup)
* [Creating Your First Socket](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#creatingyourfirstsocket)
* [Attaching Objects to a Static Mesh](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#attachingobjectstoastaticmesh)
* [Detaching](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#detaching)
* [Creating a Doorway With a Solid Door](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#creatingadoorwaywithasoliddoor)
* [Creating a New Socket](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#creatinganewsocket)
* [Attaching the Door to the Frame](/documentation/en-us/unreal-engine/using-sockets-with-static-meshes-in-unreal-engine?application_version=5.7#attachingthedoortotheframe)
