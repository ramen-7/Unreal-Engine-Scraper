<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7 -->

# Camera Rigs

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
7. [Cameras in Sequencer](/documentation/en-us/unreal-engine/movie-and-cinematic-cameras-in-unreal-engine "Cameras in Sequencer")
8. Camera Rigs

# Camera Rigs

Film with real-world techniques in Unreal Engine by using Camera Rigs.

![Camera Rigs](https://dev.epicgames.com/community/api/documentation/image/6529016d-f952-4dca-a249-0e3c7ab7e152?resizing_type=fill&width=1920&height=335)

 On this page

One of the methods real-world filmmakers use to produce smooth, sweeping shots, is by utilizing **Camera Rigs**, which are apparatuses that the camera attaches to. In Unreal Engine, you can use **Rail** and **Crane** rigs to create realistic camera movements.

#### Prerequisites

* You have an understanding of the **[Cine Camera Actor](/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)**, and have already added one into your Level.
* You know how to **[Create Camera Animation](/documentation/en-us/unreal-engine/how-to-animate-cinematic-cameras-in-unreal-engine)** within **[Sequencer](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine)**.

## Camera Rig Rail

The Camera Rig Rail is used to emulate a **[Camera Dolly](https://en.wikipedia.org/wiki/Camera_dolly)** system, which is used to create **[Tracking Shots](https://en.wikipedia.org/wiki/Tracking_shot)**. The rail's track length and curvature can be modified to suit the needs of your shot.

![camera rig rail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45cc0745-bfcf-479b-9c38-c650f9b62295/railoverview.png)

### Creation

To add a rail rig to your Level, navigate to the **Cinematic** tab in the **[Place Actors](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)** panel and locate **Camera Rig Rail**. Drag it from the panel and into your viewport.

![create camera rig rail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f83d5c2-d20e-4bca-b2bb-5b3bbea3fd76/addrail.png)

Next, move the camera to your chosen position, relative to the dolly, and attach it to the rail by dragging the camera Actor onto the rig rail in the **[World Outliner](/documentation/en-us/unreal-engine/outliner-in-unreal-engine)**.

![attach camera rig rail](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca7230a7-1b92-4c31-8afd-60e166b55a0d/attachcamrail.gif)


After a camera is attached to the dolly, it can still be moved to fine-tune its final position.

### Track Length and Shape

The Camera Rig Rail uses Unreal Engine's **[Blueprint Splines](/documentation/en-us/unreal-engine/blueprint-splines-in-unreal-engine)** for determining its track's length and shape. By default, the rail uses linear spline points at the start and end of the track. These points can be selected and moved to adjust the length and direction of the track.

![camera rig rail length](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa011cb6-04f5-48b9-b05c-09af64e2d852/railshape1.gif)

Selecting and moving the spline tangent points will add curvature to the track based on the tangent angle.

![camera rig rail curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/152bc475-10b7-4408-bc78-a22a0c5efa09/railshape2.gif)

Additional points can be added to the track's spline to fine-tune the track's shape. Select the rig rail, right-click the spline, and select **Add Spline Point Here** to add a new point at your cursor's position.

![camera rail spline point](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2807870e-b72d-41e8-b1e5-03a58b4c5139/addsplinepoint.png)

### Rail Controls

When selecting the **Camera Rig Rail Actor**, it displays the following properties for controlling its behavior and movement.

![rail details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9beb6c55-fd49-42c6-92fb-075566c72bde/railproperties.png)

| Name | Description |
| --- | --- |
| **Current Position on Rail** | This property controls the dolly movement along the track. The value range is clamped between **0** and **1**, where **0** is the **start point** of the track, and **1** is the **end point**. current position on rail |
| **Lock Orientation to Rail** | By default, the camera's orientation is set independently from the orientation of the dolly. Enabling **Lock Orientation to Rail** will cause the camera's rotation to be set relative to the dolly's rotation. lock orientation to rail |
| **Show Rail Visualization** | Disabling **Show Rail Visualization** will hide the dolly and track mesh, leaving only the spline visible. show rail visualization |
| **Preview Mesh Scale** | This property changes the size of the track and dolly preview geometry. preview mesh scale |

## Camera Rig Crane

The **Camera Rig Crane Actor** is used to emulate a boom arm or **[Camera Jib](https://en.wikipedia.org/wiki/Jib_%28camera%29)** system, which is used to create **[Crane Shots](https://en.wikipedia.org/wiki/Crane_shot)**. The crane can be pivoted along horizontal and vertical axes, and can be extended as needed.

![camera rig crane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5936e17-ae07-4db3-ae48-08612a12d0d2/craneoverview.png)

### Creation

To add a crane rig to your Level, navigate to the **Cinematic** tab in the **[Place Actors](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)** panel and locate **Camera Rig Crane**. Drag it from the panel and into your viewport.

![create camera rig crane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32d42de3-98b9-467b-9698-0112c537646e/addcrane.png)

Next, move the camera to your chosen position, relative to the crane anchor, and attach it by dragging the camera onto the rig crane in the **[World Outliner](/documentation/en-us/unreal-engine/outliner-in-unreal-engine)**.

![attach camera crane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45c40a9d-269c-412b-8940-d526ce067808/attachcamcrane.gif)

### Crane Controls

When selecting the **Camera Rig Crane Actor**, it displays the following properties for controlling its behavior and movement.

![camera rig crane details](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ef18210e-9f8e-4261-864f-ea726deca453/cranecontrols.png)

| Name | Description |
| --- | --- |
| **Crane Pitch** | Controls the pitch movement of the crane mechanism. crane pitch |
| **Crane Yaw** | Controls the yaw movement of the crane mechanism. crane yaw |
| **Crane Arm Length** | Controls the crane arm length in centimeters. This is a type-aware field, meaning that if you were to type in other units such as **2m** will automatically convert to **200cm**. crane arm length |
| **Lock Mount Pitch / Yaw** | By default, the camera's orientation is independent from the crane's pitch and yaw movement. Enabling either **Lock Mount Pitch** or **Lock Mount Yaw** will cause the camera's rotation to be set relative to the pitch or yaw rotation of the crane. crane lock axis |

## Camera Rigs In Sequencer

The primary way you will be manipulating Camera Rigs will be by animating them in **Sequencer**. Both the Camera Rig Rail and Camera Rig Crane Actor tracks can be [**added to your sequence**](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine#addingactors)

![add camera rig sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d1366ef-068d-4e71-a332-6c45c59833d1/addtoseq.png)

You will also need to add the attached camera Actors as tracks in Sequencer in order to animate them in conjunction with the movement of your rigs.

![add camera rig sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/119197ba-a996-4c4b-9f7d-84062c9429c3/addcameraseq.png)

### Rail

Camera Rail Rig property tracks can be added to Sequencer by clicking the **+ Track** button on the track and selecting from the **Properties** category.

![camera rail tracks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/908fef4e-8cce-409a-bc53-66314b593ea6/addrailtracks.png)

Once the tracks have been added, you can **[set keyframes](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine)** on the rail and camera property tracks to create your tracking shot.

![camera rig rail example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/048ca6a2-56bf-4d6a-9699-95b307434c19/railexample.gif)

### Crane

Camera Crane Rig property tracks can be added by clicking the **+ Track** button on the track and selecting from the **Properties** category.

![camera crane tracks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96d48563-36d7-4a5c-a97c-912c07c02d0b/addcranetracks.png)

Once the tracks have been added, you can **[set keyframes](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine)** on the crane and camera property tracks to create your crane shot.

![camera rig crane example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da4b47d3-74e8-4a5a-b2a0-f54bf476e20f/craneexample.gif)

### Combining Crane and Rail

You can also attach a rail to a crane, using the same camera attachment steps detailed above, to create a camera **dolly and crane** system. Crane and rail properties can be animated together to allow for more freedom and realism in your shot creation.

![crane and rail example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/decff876-4f05-4cc8-a587-2f3d9a6c4080/combinedexample.gif)

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [camera](https://dev.epicgames.com/community/search?query=camera)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#prerequisites)
* [Camera Rig Rail](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#camerarigrail)
* [Creation](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#creation)
* [Track Length and Shape](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#tracklengthandshape)
* [Rail Controls](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#railcontrols)
* [Camera Rig Crane](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#camerarigcrane)
* [Creation](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#creation-2)
* [Crane Controls](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#cranecontrols)
* [Camera Rigs In Sequencer](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#camerarigsinsequencer)
* [Rail](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#rail)
* [Crane](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#crane)
* [Combining Crane and Rail](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine?application_version=5.7#combiningcraneandrail)
