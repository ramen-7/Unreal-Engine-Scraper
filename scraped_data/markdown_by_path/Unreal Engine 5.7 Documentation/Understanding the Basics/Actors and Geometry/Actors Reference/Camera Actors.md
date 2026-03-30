<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine?application_version=5.7 -->

# Camera Actors

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
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. [Actors Reference](/documentation/en-us/unreal-engine/unreal-engine-actors-reference "Actors Reference")
8. Camera Actors

# Camera Actors

Understanding the fundamentals of Cameras in Unreal Engine.

![Camera Actors](https://dev.epicgames.com/community/api/documentation/image/7279c655-96fc-4b0a-a338-a592f84ac489?resizing_type=fill&width=1920&height=335)

 On this page

Any kind of experience you create in **Unreal Engine 5**, whether it is a game or something else, will need at least one Camera through which a user can view it. Unreal Engine contains different kinds of **Camera Actors** that you can use for this purpose.

The following types of Camera Actors are available in Unreal Engine:

* **Camera Actor**, which is a generic type of camera that can be used as a stationary or mobile viewpoint.
* **Cine Camera Actor**, which is a specialized type of camera used to create cinematics. Refer to the [Cine Camera Actor](/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine) page to learn more.

In addition to Camera Actors, you can use the following types of Actors to work with cameras in Unreal Engine:

| Actor Type | Description | Further Reading |
| --- | --- | --- |
| Camera Blocking Volume | Prevents the camera from entering a specific volume. This is useful, for example, to prevent the camera from clipping through walls or other environments. |  |
| Camera Rig Crane | Emulates a boom arm or Camera Jib system, which is used to create Crane Shots. The crane can be pivoted along horizontal and vertical axes, and can be extended as needed. | [Camera Rigs](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine) |
| Camera Rig Rail | Emulates a Camera Dolly system, which is used to create Tracking Shots. The rail's track length and curvature can be modified to suit the needs of your shot. | [Camera Rigs](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine) |
| Level Sequence Actor | Acts as a container for the Level Sequence Asset. The Level Sequence Asset is located in the Content Browser and contains Sequencer's data. This includes tracks, cameras, keyframes, and animations. This is assigned to a Level Sequence Actor in order to bind its data to a Level. | [Sequencer Overview](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) |

## Placing a Camera Actor

Camera Actors are placed from the [Place Actors panel](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine). To add a Camera to your Level, find it in the **Place Actors** panel, then drag it and drop it into the Level Viewport.

## Previewing a Camera Actor

If you select a Camera Actor (or a Blueprint that contains a Camera component), a separate preview window will open within the Level viewport. This window shows what the currently selected Camera "sees".

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdca753a-71c6-4cd7-986c-25096c5e517b/camera-actor-preview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdca753a-71c6-4cd7-986c-25096c5e517b/camera-actor-preview.png)

The Preview window of a Camera Actor. Click the image for full size.

* [camera](https://dev.epicgames.com/community/search?query=camera)
* [actor](https://dev.epicgames.com/community/search?query=actor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Placing a Camera Actor](/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine?application_version=5.7#placingacameraactor)
* [Previewing a Camera Actor](/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine?application_version=5.7#previewingacameraactor)
