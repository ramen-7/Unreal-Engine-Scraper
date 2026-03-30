<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-geometry-cache-track-in-unreal-engine?application_version=5.7 -->

# Geometry Cache Track

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Sequencer Overview](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview "Sequencer Overview")
8. [Tracks](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine "Tracks")
9. Geometry Cache Track

# Geometry Cache Track

The Geometry Cache Track enables the scrubbing and playback of cloth and other Alembic mesh simulations on Static Meshes.

![Geometry Cache Track](https://dev.epicgames.com/community/api/documentation/image/378df45b-8763-4aa1-aa72-4c39863bdf57?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

The **Geometry Cache Track** enables you to scrub through a **Geometry Cache** and render it out with frame accuracy. Once you have imported your Alembic file into Unreal Engine and added it to a Level, you can add it to a **Level Sequence** and add the **Geometry Cache Track** to play your content.

## Steps

For this How-to guide, we are using the **Blueprint Third Person**template project. You will also need an Alembic file to import into the Engine. If you do not have your own asset, download this [Sample File](https://epicgames.box.com/s/l74nagy14ttaium5j41gu61ljz4v5rul).

1. Import your Alembic file(s) into Unreal Engine [as a Geometry Cache](working-with-content/alembic-file-importer#importasgeometrycache) and define your desired settings.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41151a36-3427-475f-bb39-745cd5202557/usinggeometrycache_importwindow.png "UsingGeometryCache_ImportWindow.png")
2. Place your **Geometry Cache** in the Level, then create a **Level Sequence** and add it to **Sequencer** with the **+ Track** button.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/319c417e-317e-4016-bad3-bf1b86e04736/geocache_02.png "GeoCache_02.png")
3. Click the **+ Track**button for the newly created Track and select **Geometry Cache**from the **Tracks**menu.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7556f603-690a-4684-b4e3-51356e105de2/geocache_03.png "GeoCache_03.png")
4. Scrub the **Timeline** to view a playback.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da337063-c36d-4cc0-ab6d-a6e3668bd28b/geometrycache_example.png "GeometryCache_Example.png")


   You can also set the **Level Sequence** to **Auto Play** before selecting Play in the Level.

## End Result

With the **Geometry Cache Track**set, you can scrub through your content or it will play back automatically when your Level Sequence plays.

You can access the properties of the Geometry Cache by right-clicking on the Track in the **Tracks Window**. From the properties menu, you can change which **Geometry Cache**asset is being used, add a **Start**or **End Offset**, or adjust the **Play Rate.** There are also options for the **Section**itself and whether to play the animation in **Reverse**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79e2a018-d5c8-4a41-8353-f720e2d818b5/geocache_04.png "GeoCache_04.png")

The following properties are available for Geometry Cache tracks from the right-click context menu, under **Properties**:

| Property | Description |
| --- | --- |
| **Geometry Cache** | Specifies the Geometry Cache asset to play. |
| **Start Offset** | Number of frames to offset into the beginning of the animation clip. |
| **End Offset** | Number of frames to offset into the end of the animation clip. |
| **Play Rate** | Defines the playback rate of the animation clip (lower to slow down, increase to speed up). |

* [landing page](https://dev.epicgames.com/community/search?query=landing%20page)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [alembic](https://dev.epicgames.com/community/search?query=alembic)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [geometry cache](https://dev.epicgames.com/community/search?query=geometry%20cache)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/cinematic-geometry-cache-track-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/cinematic-geometry-cache-track-in-unreal-engine?application_version=5.7#endresult)
