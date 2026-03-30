<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/eye-dome-lighting-mode-for-point-clouds-in-unreal-engine?application_version=5.7 -->

# Eye-Dome Lighting Mode for Point Clouds

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
7. Eye-Dome Lighting Mode for Point Clouds

# Eye-Dome Lighting Mode for Point Clouds

Enable Eye Dome lighting to accentuate a point cloud's edges and enhance its depth.

![Eye-Dome Lighting Mode for Point Clouds](https://dev.epicgames.com/community/api/documentation/image/916c01a4-9d74-4d0d-ab41-d2cb56024a6a?resizing_type=fill&width=1920&height=335)

 On this page

**Eye-Dome Lighting (EDL)** is a lighting model that accentuates the shapes of objects within a point cloud by grouping objects that are close together and shading their outlines, which enhances depth perception. EDL is implemented as a post-process Material and requires a Post Process Volume to work. It does not use any engine light sources, so it can be used with the unlit rendering method.

EDL can be used with Ambient Occlusion but this may produce an excessively dark image.

## Steps

1. Add a Post Process Volume to your Level. From the **Place Actors** panel, search for **Post Process Volume** and drag it into your Level.

   [![Adding a Post Process Volume to the Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10502d0f-d7cf-4c0c-9091-0ce3d163ae79/ue5_01-post-process-volume-into-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10502d0f-d7cf-4c0c-9091-0ce3d163ae79/ue5_01-post-process-volume-into-level.png)

   Click image for full size.
2. Select the Post Process Volume and, in its **Details** panel, scroll to the **Rendering Features** category.
3. Expand **Post Process Materials** and click the **plus (+)** icon to add a new Material to the array.
4. From the drop down-menu of the new Material you added, select **Asset reference**.

   [![Select Asset reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a27de993-1ff4-44e7-a770-5c0932f55fd6/ue5_02-select-asset-reference.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a27de993-1ff4-44e7-a770-5c0932f55fd6/ue5_02-select-asset-reference.png)

   Click image for full size.
5. Click the **None** dropdown. Then enable **Engine Content** and **Plugin Content** to be visible.

   [![Enable Engine Content and Plugin Content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bbf58d9-1816-4801-bdc5-3e5aab4a35d6/ue5_03-enable-engine-content-and-plugin-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bbf58d9-1816-4801-bdc5-3e5aab4a35d6/ue5_03-enable-engine-content-and-plugin-content.png)

   Click image for full size.
6. Click the **None** dropdown menu again. Then, select one of the two following options:

   * **M\_PP\_EDL\_MainPass** - This will apply the EDL to every object in the Level, not just point clouds. If you only display point cloud elements, this is the recommended option.
   * **M\_PP\_EDL\_CustomPass** - This will apply the EDL only to objects using **Custom Depth Pass**. This option is recommended if you want to selectively apply EDL.

     Enabling Custom Depth Pass will increase the performance cost.
7. To apply the EDL to the whole Level, enable the **Infinite Extent (Unbound)** option on the post-processing volume.

   [![Enable the Infinite Extent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8727b8b0-ee3e-41c0-a77b-80b6da0b43ed/ue5_04-enable-the-infinite-extent-option.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8727b8b0-ee3e-41c0-a77b-80b6da0b43ed/ue5_04-enable-the-infinite-extent-option.png)

   Click image for full size.

## Result

EDL has been applied to the Level. Notice the change to edges of objects in the level and how this enhances depth perception.

![Before applying EDL](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b7e3932-c6ae-486b-8503-8bc58cb9e9ac/ue5_05-before-applying-edl.png)

![After applying EDL](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d99df1d6-9b32-4c75-a63e-2a723df1a3f6/ue5_06-after-applying-edl.png)

Before applying EDL

After applying EDL

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [lidar](https://dev.epicgames.com/community/search?query=lidar)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/eye-dome-lighting-mode-for-point-clouds-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/eye-dome-lighting-mode-for-point-clouds-in-unreal-engine?application_version=5.7#result)
