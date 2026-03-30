<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7 -->

# Procedural Foliage Tool

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Open World Tools](/documentation/en-us/unreal-engine/open-world-tools-in-unreal-engine "Open World Tools")
7. Procedural Foliage Tool

# Procedural Foliage Tool

How to set up and use the Procedural Foliage tool.

![Procedural Foliage Tool](https://dev.epicgames.com/community/api/documentation/image/56e725f3-2b18-4a6d-a288-a9937cbe9b7b?resizing_type=fill&width=1920&height=335)

 On this page

In this Quick Start tutorial we will take a look at how the **Procedural Foliage Tool** works. Over the course of this Quick Start tutorial you will learn how to create, set up, and spawn an entire forest's worth of trees inside of UE5 using only the Procedural Foliage tool. You will also be introduced to key properties and settings that will help you shape your virtual forest to fit your project's needs.

![Final Product](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/febee554-d0d9-4888-9f1f-83f59fb575be/01-t-pf-qs-final-product.png "Final Product")

You will also be exposed to all of the required Assets and properties the Procedural Foliage tool requires to function correctly and deliver the results you want. When you have completed this Quick Start you will have a new level that should look similar to the image above.

### Prerequisites

Before you can use the Procedural Foliage tools in your project, you must first enable them by doing the following.

1. From the **Main Menu** open the **Edit** menu then click on **Editor Preferences**.

   [![Editor Preferences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2b7969e-45c4-42c0-b4a8-ca2a65765527/02-pfs-editor-prefs.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2b7969e-45c4-42c0-b4a8-ca2a65765527/02-pfs-editor-prefs.png)

   Click image for full size.
2. Inside of the Editor Preferences **right - click** on the **Experimental** section.
3. Enable the Procedural Foliage option by clicking on the checkmark box next to the word **Procedural Foliage**.

   [![Editor Preferences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1512b219-c8b9-48b5-b85c-a29f4ab50679/03-pfs-editor-preferences.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1512b219-c8b9-48b5-b85c-a29f4ab50679/03-pfs-editor-preferences.png)

   Click image for full size.

You will also need to download the **Open World Demo Collection** content pack from the **Unreal Engine Marketplace** as some of the content from the collection will be used in the following Quick Start. Once the Open World Demo Collection is downloaded add it to the project that you are using to follow along with this Quick Start by doing the following.

1. From the Epic Games Launcher in the Marketplace locate and then download the **Open World Demo Collection**.

   [![Open World Demo Collection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1a698e9-37e5-411b-b080-e623d7124aa4/04-t-owt-owdc.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1a698e9-37e5-411b-b080-e623d7124aa4/04-t-owt-owdc.png)

   Click image for full size.
2. Go the **Library** section of the launcher and then under **Vault** section locate the Open World Demo Collection .

   [![Open World Demo Collection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28e2db87-82aa-414d-a007-a211bdde59b7/05-t-owt-add-content-00.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28e2db87-82aa-414d-a007-a211bdde59b7/05-t-owt-add-content-00.png)

   Click image for full size.
3. Click on the button that says **Add to Project**.

   [![Add to Project](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79d0c972-d506-453f-adbd-a8b445d8907a/06-t-owt-add-to-project.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79d0c972-d506-453f-adbd-a8b445d8907a/06-t-owt-add-to-project.png)

   Click image for full size.
4. You will then be shown a list of projects that you can add this to, select the project that you are using to follow along with this Quick Start and then press the **Add to Project** button

   [![Select_Project](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d5bd82f-642e-4354-ab55-4eedc52aa48b/07-t-owt-atp.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d5bd82f-642e-4354-ab55-4eedc52aa48b/07-t-owt-atp.png)

   Click image for full size.

## 1 - Creating Foliage Type Actors

In this step you will create a new Level, Landscape Terrain, and all of the Assets the Procedural Foliage Tool requires.

1. Create a new level using the **Default Template** as a base.

   [![New Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be7712ba-14e4-4fd9-8f7b-c8deb1ebb148/08-t-new-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be7712ba-14e4-4fd9-8f7b-c8deb1ebb148/08-t-new-level.png)

   Click image for full size.
2. Add a new **Landscape Actor** to the level by first selecting **Landscape** in the **Modes** dropdown menu to open the **Landscape Panel**, and then clicking the **Create** button to add the Landscape Actor to the level.

   [![Modes Landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e587420c-5aa0-429e-98b4-7ef74cbcd8b4/09-modes-landscape.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e587420c-5aa0-429e-98b4-7ef74cbcd8b4/09-modes-landscape.png)

   Click image for full size.

   Using a Landscape Terrain Actor quickly provides you with a very large area to spawn your forest on.

   [![Placed Landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b230810e-b21d-4bf6-b1fe-b727b757b3d5/10-placed-landscape.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b230810e-b21d-4bf6-b1fe-b727b757b3d5/10-placed-landscape.png)

   Click image for full size.

   If you are not familiar with how Landscape Terrain works or would like to learn more, please refer to [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine) for more information.
3. Create a new Procedural Foliage Spawner by **right-clicking** in the **Content Browser**, expanding the **Foliage** section, and then clicking on the **Procedural Foliage Spawner**.

   [![Create Procedural Foliage Spawner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4720cac-0a5b-4a27-a2cd-b70e3dddc23c/11-t-create-pfs.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4720cac-0a5b-4a27-a2cd-b70e3dddc23c/11-t-create-pfs.png)

   Click image for full size.
4. Name the Procedural Foliage Spawner in this example **PFS\_Example** or something similar.

   [![Name Procedural Foliage Spawner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee3c531b-7932-4f7b-8fc8-cf8bfcffa361/12-t-name-pfs.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee3c531b-7932-4f7b-8fc8-cf8bfcffa361/12-t-name-pfs.png)

   Click image for full size.
5. Drag the Procedural Foliage Spawner from the **Content Browser** into the level and position it so that it is in the center of the level or at **0,0,200** in the X, Y, and Z axis.

   [![Place Procedural Foliage Spawner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac4324f4-eda3-451b-967e-6341f92774cb/13-pfs-place-pfs.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac4324f4-eda3-451b-967e-6341f92774cb/13-pfs-place-pfs.png)

   Click image for full size.
6. Scale the Procedural Foliage Spawner to **100,100,10** in the X, Y, and Z axis to create a large area to spawn your forest in.

   [![PFS Example Details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78037cbd-7b4d-4e35-ba04-0a453e2b2611/14-pfs-example-details.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78037cbd-7b4d-4e35-ba04-0a453e2b2611/14-pfs-example-details.png)

   Click image for full size.
7. Now that we have our spawner, we need to give it some Foliage to spawn. To do this, **right - click** in the **Content Browser** expanding the **Foliage** section and then click on **Static Mesh Foliage**. Name the Static Mesh Foliage **Tree\_00** or something similar.

   [![Create Static Mesh Foliage](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a07368cf-f123-43dc-833d-501e31dd16e2/15-t-create-ft.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a07368cf-f123-43dc-833d-501e31dd16e2/15-t-create-ft.png)

   Click image for full size.
8. If you have not done so already, save your work and level by pressing the **Save All** button to save all content and the **Save** button to save the level. When prompted for a level name use the name **PFT\_00**. At this point you should have something that looks similar to the image below.

   [![Save All](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58606039-a59f-472f-ab1e-96b0b121b092/16-t-save-all.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58606039-a59f-472f-ab1e-96b0b121b092/16-t-save-all.png)

   Click image for full size.

## 2 - Telling the Spawner What to Spawn

In the following section we will cover how to set up the **Foliage Type Actors** to work with the Procedural Foliage Spawner. You will continue to work with the **PFT\_00** level that was created in the last step.

1. Open up the **Procedural Foliage Spawner** by **double - clicking** in the Content Browser.

   [![Procedural Foliage Spawner Opened](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0bb355f-197a-4c11-8e87-1f68c6d3f824/17-t-pfs-opened.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0bb355f-197a-4c11-8e87-1f68c6d3f824/17-t-pfs-opened.png)

   Click image for full size.
2. Add a new item to the **Foliage Types** array by clicking the **Plus Sign** icon that is to the right of the **Foliage Types** menu option.

   [![Procedural Foliage Spawner Add Foliage Types](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aab7c320-7063-4222-9d8c-57d013491076/18-t-pfs-add-ft.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aab7c320-7063-4222-9d8c-57d013491076/18-t-pfs-add-ft.png)

   Click image for full size.
3. In the Content Browser, select the Tree\_00 Static Mesh Foliage and drag it into the **Foliage Type Object**, or press the **Arrow** icon, to load the selected Static Mesh Foliage into the Procedural Foliage Spawner.

   [![Add Foliage Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7422e9d4-0a57-4710-b4cd-86fcc1fe7fef/19-pfs-add-foliage-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7422e9d4-0a57-4710-b4cd-86fcc1fe7fef/19-pfs-add-foliage-mesh.png)

   Click image for full size.
4. Open up the Tree\_00 Static Mesh Foliage by **double - clicking** on it in the Content Browser.

   [![PFT Window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e177b35-426a-42cc-a623-f715297de0e7/20-t-pft-window.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e177b35-426a-42cc-a623-f715297de0e7/20-t-pft-window.png)

   Click image for full size.
5. At the top of the Tree\_00 Static Mesh Foliage, locate the **Mesh** section and then click on the drop down menu that says **None**.

   [![PFT Mesh Section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/575d167d-66d6-4f11-92e4-883076675bff/21-t-pft-mesh-section.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/575d167d-66d6-4f11-92e4-883076675bff/21-t-pft-mesh-section.png)

   Click image for full size.
6. Locate the **HillTree\_02** Static Mesh from the **Open World Demo Collection** either by typing "HillTree\_02" as the search term or by scrolling through the list, and load it by clicking on it.

   [![Select HillTree _02](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8f562ae-0998-4bbe-9405-495563e45f04/22-pfs-select-hill-tree-02.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8f562ae-0998-4bbe-9405-495563e45f04/22-pfs-select-hill-tree-02.png)

   Click image for full size.
7. Back in the viewport select the **Procedural Foliage Spawner** that was placed in the level and then expand the **Procedural Foliage** section under the **Details** panel.

   [![PFV Select In Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b1c3f96-0fd9-4d8c-b358-54df30c9622c/23-t-pfv-select-in-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b1c3f96-0fd9-4d8c-b358-54df30c9622c/23-t-pfv-select-in-level.png)

   Click image for full size.
8. Under the **Procedural Foliage** section click on the **Resimulate** button and you should now see the Procedural Foliage Spawner densely packed with tress like in the image below.

   [![Final Results](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4405c849-ab1e-478a-b7e7-9a932360adb6/24-t-final-results.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4405c849-ab1e-478a-b7e7-9a932360adb6/24-t-final-results.png)

   Click image for full size.

   In order to see the proper results, you will need to click on **Build** in the **Main Toolbar** to rebuild the lighting every time you use the Resimulate button to create or alter the Procedural Foliage . This can take a long time due to the large number of static meshes involved.

## 3 - Tweaking Foliage Type Object Properties

**Foliage Type Objects** (both Static Mesh Foliage and Actor Foliage) come with a number of different properties that you can adjust to control anything from how the Foliage Type Objects are placed on other objects in the level to how the Foliage Type Objects will grow and spread throughout the Foliage Spawner. In the following section we will take a look at what properties are available in **Foliage Type Objects** and how you can manipulate these properties to get the results you desire. You will continue to work with the **PFT\_00** level that was used in the last step.

1. Open up the Tree\_00 Static Mesh Foliage.
2. Expand the **Placement** section and make sure that both **Align to Normal** and **Random Yaw** are enabled.

   [![Placement Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c6caf11-4460-409f-ae39-e2c6c51dd818/25-t-placement-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c6caf11-4460-409f-ae39-e2c6c51dd818/25-t-placement-options.png)

   Click image for full size.

   The Placement section is where you can adjust how a Foliage Type Object's meshes are placed on objects in the level.
3. Under the **Procedural** section of the Static Mesh Foliage expand the **Collision** section and set the **Shade Radius** to **50**.

   [![Shade Radius](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a181940-c5fc-442b-8810-1a41242ea89f/26-t-shade-radius.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a181940-c5fc-442b-8810-1a41242ea89f/26-t-shade-radius.png)

   Click image for full size.

   The Collision section determines which Foliage Type Objects should be removed when two Foliage Type Objects are competing for the same spawn location or relative space. When a Virtual Seed's collision radius overlaps an existing collision or shade radius from another Foliage Type Object's Virtual Seed, one Virtual Seed will be replaced or killed based on which Foliage Type Object has the higher priority.
4. Select the Procedural Foliage Spawner that was placed in the level and under the Procedural Foliage section click on the Resimulate button.

   [![Press ReSimulate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09c580d5-607a-461b-b610-7d2c9ed24d83/27-t-press-resimulate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09c580d5-607a-461b-b610-7d2c9ed24d83/27-t-press-resimulate.png)

   Click image for full size.
5. Back in the Tree\_00 Static Mesh Foliage collapse the Collision section and expand the **Clustering** section, then set **Num Steps** to **0**, so that we get trees that are all the same size and age and then press the Resimulate button. When completed you should have something that looks similar to the image below.

   [![Num Steps 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5db4f58-0e30-4539-ab95-043ea65c047d/28-t-num-steps-0.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5db4f58-0e30-4539-ab95-043ea65c047d/28-t-num-steps-0.png)

   Click image for full size.

   Clustering uses a number of properties such as density, age, and proximity to help determine how the specified Foliage Type Object's mesh instances should be placed, grouped and spread around inside of the Procedural Foliage Spawner.
6. While we now have some space in between our trees, the overall density is still a little too high. To fix this, set the **Initial Seed Density** to **0.25** and then click on the Resimulate button.

   [![Num ISD 0.125](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/54779b51-018f-4190-a2b6-2b3dd5d5ee50/29-t-num-isd-0-125.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/54779b51-018f-4190-a2b6-2b3dd5d5ee50/29-t-num-isd-0-125.png)

   Click image for full size.
7. As you can see, setting the Initial Seed Density to 0.25 greatly reduced the density of our forest because we are only growing and spreading trees for a single year. To fix this set the Num Steps back to **3**, which will grow and spread the trees for 3 years, and then click on the Resimulate button.

   [![Num Steps 3](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b5de4cf-190f-49df-80f2-26e366ff8b95/30-t-num-steps-3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b5de4cf-190f-49df-80f2-26e366ff8b95/30-t-num-steps-3.png)

   Click image for full size.
8. Expand the **Growth** section then set the following parameters to the following settings.

   * **Max Age**: **20.0**
   * **Procedural Scale Max**: **10.0**

     [![Set Growth](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4768863c-d822-484f-beef-ec765da3252f/31-t-set-growth.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4768863c-d822-484f-beef-ec765da3252f/31-t-set-growth.png)

     Click image for full size.

     The Growth section allows you to adjust how a Foliage Type Object's mesh instances will grow and get bigger over time.
9. Finally in the **Instance Settings** under the **Cull Distance** option, set the **Max** value to **20,000** and then click on the Resimulate button. When completed you should have something that looks similar to the image below.

   [![Cull Distance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b698db5-7b82-40da-96af-749feaf9105e/32-t-cull-distance.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b698db5-7b82-40da-96af-749feaf9105e/32-t-cull-distance.png)

   Click image for full size.

   The Instance Settings allows you to adjust how a Foliage Type Object's mesh instances will be displayed in the level. Inside the Instance Settings you can set or adjust many different properties like Cull Distance, Shadowing, and Collision.

## 4 - Using Multiple Foliage Type Objects

Adding another species of tree to your virtual forest will greatly help to increase the realism and overall look and feel. Luckily, the **Procedural Foliage Spawner** allows for you to spawn multiple **Foliage Type Objects** resulting in one single **Procedural Foliage Spawner** being able to spawn an entire forest with a multitude of different trees. In the following section we will take a look at how you can set up a Procedural Foliage Spawner to work with multiple Foliage Types. You will be continuing to work with the **PFT\_00** level that was used in the last step.

1. Inside of the Content Browser select the Tree\_00 Static Mesh Foliage and then press **Ctrl + W** on the keyboard to duplicate it using **Tree\_01** as the name.

   [![Dup FT](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f567d45-b8ad-43c8-8537-bcf82abb303f/33-t-dup-ft.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f567d45-b8ad-43c8-8537-bcf82abb303f/33-t-dup-ft.png)

   Click image for full size.
2. Open the newly created Tree\_01 Static Mesh Foliage and under the Mesh section change the mesh to the **ScotsPineTall\_01** Static Mesh.

   [![New Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f184f40b-0b20-4e94-af15-4d930c5aae60/34-t-new-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f184f40b-0b20-4e94-af15-4d930c5aae60/34-t-new-mesh.png)

   Click image for full size.
3. Open up the Procedural Foliage Spawner from the Content Browser and expand the Foliage Types section.

   [![Expand FT](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc736de8-b405-4093-a21e-a4f2eeaf3ba2/35-t-expand-ft.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc736de8-b405-4093-a21e-a4f2eeaf3ba2/35-t-expand-ft.png)

   Click image for full size.
4. Click on the Plus sign icon to add the option to input another Foliage Type Object.

   [![Add New FT](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9f915b4-2309-4a9d-9460-6b492288b1b1/36-t-add-new-ft.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9f915b4-2309-4a9d-9460-6b492288b1b1/36-t-add-new-ft.png)

   Click image for full size.
5. In the Content Browser, select the Tree\_01 Static Mesh Foliage and drag it into the Foliage Type Object, or press the Arrow icon, to load the selected Static Mesh Foliage into the Procedural Foliage Spawner.

   [![PFS Add Foliage Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84fed898-08a8-4a30-ad1c-0d640060446c/37-pfs-add-foliage-mesh-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84fed898-08a8-4a30-ad1c-0d640060446c/37-pfs-add-foliage-mesh-2.png)

   Click image for full size.
6. Select the Procedural Foliage Spawner that was placed in the level and then click on the Resimulate button. When completed you should see something like the following image.

   [![FT In Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49625c91-380b-4a21-a7d4-493da0ba8b1a/38-t-2-ft-in-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49625c91-380b-4a21-a7d4-493da0ba8b1a/38-t-2-ft-in-level.png)

   Click image for full size.
7. To make the forest look more interesting open up the Tree\_01 Static Mesh Foliage and adjust the following parameters with the following values. The numbers and options that are listed below were selected because they will produce a forest that has interesting clustering and growth interaction with the Static Mesh Foliage instances that are already in use. However please feel free to experiment with these numbers and settings till you get something that suits your needs.

   * **Num Steps:** 4
   * **Initial Seed Density:** 0.125
   * **Average Spread Distance:** 100
   * **Can Grow in Shade:** Enabled
   * **Spawns in Shade:** Enabled
   * **Max Age:** 15
   * **Overlap Priority:** 1
   * **Procedural Scale:** Max 5.0
8. Once the settings have been adjusted click on the **Resimulate** button on the Procedural Foliage Spawner and you should now have something that looks similar to the image below.

   [![Adjust Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/178dc66a-622f-4d24-8bdb-2dcc2184d96b/39-t-ft01-adjust-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/178dc66a-622f-4d24-8bdb-2dcc2184d96b/39-t-ft01-adjust-settings.png)

   Click image for full view.

## 5 - Implementing Procedural Foliage Blocking Volumes

The **Procedural Foliage Blocking Volume** is a Volume Actor that can be placed in a level and scaled to a desired size which will prevent the Procedural Foliage Spawner from spawning any Foliage Type Objects inside of the bounds of the Procedural Foliage Blocking Volume. In the following section we will go over how you can add a **Procedural Foliage Blocking Volume** to your level and use it to prevent Foliage meshes from spawning. You will be continuing to work with the **PFT\_00** level that was used in the last step.

1. First find the **Procedural Foliage Blocking Volume** by searching for it in the **Place Actors** panel using **Proc** as the search term.

   [![Find Procedural Foliage Blocking Volume](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36e9b80c-4491-43fd-b315-bfc928012143/40-t-find-procf-blocking-volume.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36e9b80c-4491-43fd-b315-bfc928012143/40-t-find-procf-blocking-volume.png)

   Click image for full size.
2. Select the Procedural Foliage Blocking Volume and then drag it from the Place Actors panel into the level.

   [![Procedural Foliage Blocking Volume](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26d5b94c-e03f-43f7-8286-9924768bdc7e/41-pfs-blocking-volume.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26d5b94c-e03f-43f7-8286-9924768bdc7e/41-pfs-blocking-volume.png)

   Click image for full size.
3. To stop foliage meshes from being spawned in the back portion of the Procedural Foliage Spawner move and scale the Procedural Foliage Blocking Volume using the following location and scale values.

   * **Location X:** 5430.0 cm
   * **Location Y:** -3900.0 cm
   * **Location Z:** 200.0 cm
   * **Scale X:** 41.75
   * **Scale Y:** 65.5
   * **Scale X:** 41.75

     [![Procedural Foliage Blocking Volume Postion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebdcb916-487a-4486-812b-62effaf3dbe1/42-t-pfbv-postion.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebdcb916-487a-4486-812b-62effaf3dbe1/42-t-pfbv-postion.png)

     Click image for full size.
4. Now select the Procedural Foliage Spawner in the level and then in the Details click on the Resimulate button. When the Resimulate is completed you should now be missing the entire back section of trees that were intersecting with the Procedural Foliage Blocking Volume.

   [![Procedural Foliage Blocking Volume Before After](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d941b57e-bce2-4300-bcca-5d0e8f8a7299/43-t-pfv-before-after.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d941b57e-bce2-4300-bcca-5d0e8f8a7299/43-t-pfv-before-after.png)

   Click image for full size.

   In the following image we can see the before and after results.

   | Image Number | Results |
   | --- | --- |
   | 1: | Before Procedural Foliage Blocking Volume is added |
   | 2: | After Procedural Foliage Blocking Volume is added |

## 6 - On Your Own!

Now that you have seen that power the Procedural Foliage tool offers, try using the tools listed below in conjunction with what you just learned about the Procedural Foliage tool to try and make a level that looks like the following image.

![On Your Own](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac596572-4efd-41d0-9bdf-8be51c901793/44-t-on-your-own.png "On Your Own")

* Try using Foliage Actors instead of Static Mesh Foliage.
* Use the [Grass Tool](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine) to make the Landscape look like it is densely covered in grass, flowers and bushes.
* Define the look and feel of the Landscape terrain using the [Landscape Sculpt](/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine) tools add things like hills, mountains and lakes.
* Give the surface of the Landscape more visual variety and detail by creating a [Landscape Material](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine) that has multiple Textures that can be painted on the Landscape terrain.
* Adjust the [Directional Light](/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine) to make the level lighting resemble lighting that happens in the early morning or late afternoon.
* Set up the level lighting to use a completely dynamic based lighting solution that will make use of dynamic shadows as well as [Ray Traced Distance Field Soft Shadows](/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine).
* Try using the [Foliage System](/documentation/en-us/unreal-engine/foliage-mode-in-unreal-engine) tools to remove or tweak the placement, rotation and scale of the Foliage meshes that are placed by the Procedural Foliage tool so that you can get the exact look you are going for.
* Show off your creation to others by using a [Camera](/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine) in conjunction with [Sequencer](/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine) to render out a video of your level for you to share with the world.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [open world](https://dev.epicgames.com/community/search?query=open%20world)
* [foliage](https://dev.epicgames.com/community/search?query=foliage)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#prerequisites)
* [1 - Creating Foliage Type Actors](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#1-creatingfoliagetypeactors)
* [2 - Telling the Spawner What to Spawn](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#2-tellingthespawnerwhattospawn)
* [3 - Tweaking Foliage Type Object Properties](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#3-tweakingfoliagetypeobjectproperties)
* [4 - Using Multiple Foliage Type Objects](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#4-usingmultiplefoliagetypeobjects)
* [5 - Implementing Procedural Foliage Blocking Volumes](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#5-implementingproceduralfoliageblockingvolumes)
* [6 - On Your Own!](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine?application_version=5.7#6-onyourown!)
