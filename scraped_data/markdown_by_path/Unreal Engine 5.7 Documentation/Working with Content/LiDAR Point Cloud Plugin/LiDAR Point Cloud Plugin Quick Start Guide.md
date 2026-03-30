<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-quick-start-guide-in-unreal-engine?application_version=5.7 -->

# LiDAR Point Cloud Plugin Quick Start Guide

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
6. [LiDAR Point Cloud Plugin](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-for-unreal-engine "LiDAR Point Cloud Plugin")
7. LiDAR Point Cloud Plugin Quick Start Guide

# LiDAR Point Cloud Plugin Quick Start Guide

Guide to enabling and using the LiDAR Point Cloud plugin.

![LiDAR Point Cloud Plugin Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/7b68517c-e047-4ebc-bed5-b6e288b6a364?resizing_type=fill&width=1920&height=335)

 On this page

This Quick Start guide covers the following steps:

1. Enabling the LiDAR Point Cloud plugin.
2. Importing a point cloud and placing it into a scene.
3. Building collision for the point cloud so you can explore it in real time.
4. Editing the point cloud.

## 1. Enabling the Plugin

The LiDAR Point Cloud plugin is included with the Unreal Engine, but you must enable it for your Project before you can use it.

1. Open the **Plugins** window (main menu: **Edit > Plugins**).
2. In the **Plugins** window, search for the **LiDAR Point Cloud Support** plugin, then click the **Enabled** option.

   ![LiDAR Point Cloud Support plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e9a2798-294a-4404-a6d2-f2ccb227600c/ue5-1_01-lidar-point-cloud-support-plugin.png "LiDAR Point Cloud Support plugin")
3. Save your project and restart Unreal Engine.

## 2. Importing the Point Cloud

1. Create a new project. Use a template that includes a character controller, such as [Third Person Template](/documentation/404).
2. Choose the point cloud file you want to import and drag it into the **Content Browser**.
3. Drag the point cloud from the **Content Browser** into the **Viewport**. This will automatically create an instance of a **LidarPointCloudActor** and assign your specified cloud to it.

## 3. Building and Testing Collision

Before you can move around the imported point cloud scan like any other Level, you need to build and enable collision for it.

1. In the **Main Toolbar**, click the **Modes** button, select **Lidar Mode**.

   [![Lidar Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2599d0d-ec26-4897-9b67-3bcd2270c655/ue5-1_02-lidar-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2599d0d-ec26-4897-9b67-3bcd2270c655/ue5-1_02-lidar-mode.png)

   Click image for full size.
2. Select **Add Collision**.

   [![Add collision for a point cloud](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1315e67-3316-43ce-bdf4-87e9fbc56682/ue5-1_03-add-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1315e67-3316-43ce-bdf4-87e9fbc56682/ue5-1_03-add-collision.png)

   Click image for full size.
3. Click **Save** to save your changes.
4. Back in the main editor window, from the **Place Actors** panel, search for a **Player Start** component and drag it into your level. Place it above the ground.
5. Click **Play** to start **Play in Editor** mode and move around the imported scan.

   [![A point cloud with Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8863360-4ed2-4382-9a24-3e2080c1117d/ue5-1_04-quickstart-result.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8863360-4ed2-4382-9a24-3e2080c1117d/ue5-1_04-quickstart-result.png)

   Click image for full size.

## 4. Editing the Point Cloud

Next, you'll be making some simple edits to the point cloud. You can select and edit individual points and point groups using a range of tools.

1. To edit points, you must select them first. Choose one of the available selection methods:

   * Box Selection
   * Polygonal Selection
   * Lasso Selection
   * Paint Selection

     [![Selection tools available in the LiDAR Point Cloud Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6efaaa4e-41dd-466e-b5e7-ba0bb9bf7a5f/ue5-1_05-selection-methods.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6efaaa4e-41dd-466e-b5e7-ba0bb9bf7a5f/ue5-1_05-selection-methods.png)

     Click image for full size.

   Selected points will be highlighted. Press the **Esc** key on your keyboard to clear your selection.

   [![Selected points in a Point Cloud](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb7b4a4d-61f5-4dfd-9d36-a6f58ec77e64/ue5-1_06-selected-points.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb7b4a4d-61f5-4dfd-9d36-a6f58ec77e64/ue5-1_06-selected-points.png)

   Click image for full size.
2. You can **Hide**, **Delete**, or **Crop** the selected points.

After you edit the point cloud, you must rebuild its collision.

## On Your Own!

Explore some of the other functionality the LiDAR Point Cloud plugin offers:

* Enable [Eye-Dome Lighting](/documentation/en-us/unreal-engine/eye-dome-lighting-mode-for-point-clouds-in-unreal-engine) to enhance depth perception.
* See the [LiDAR Point Cloud Reference](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-reference) for the full range of available options.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [lidar](https://dev.epicgames.com/community/search?query=lidar)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1. Enabling the Plugin](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-quick-start-guide-in-unreal-engine?application_version=5.7#1enablingtheplugin)
* [2. Importing the Point Cloud](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-quick-start-guide-in-unreal-engine?application_version=5.7#2importingthepointcloud)
* [3. Building and Testing Collision](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-quick-start-guide-in-unreal-engine?application_version=5.7#3buildingandtestingcollision)
* [4. Editing the Point Cloud](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-quick-start-guide-in-unreal-engine?application_version=5.7#4editingthepointcloud)
* [On Your Own!](/documentation/en-us/unreal-engine/lidar-point-cloud-plugin-quick-start-guide-in-unreal-engine?application_version=5.7#onyourown!)
