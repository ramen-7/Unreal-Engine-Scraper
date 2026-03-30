<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7 -->

# Traces Overview

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Traces with Raycasts](/documentation/en-us/unreal-engine/traces-with-raycasts-in-unreal-engine "Traces with Raycasts")
8. Traces Overview

# Traces Overview

Overview of the Unreal Engine 5 tracing system.

![Traces Overview](https://dev.epicgames.com/community/api/documentation/image/6d8db041-3d24-4619-a336-4d9d2bf6466a?resizing_type=fill&width=1920&height=335)

 On this page

**Traces** offer a method for reaching out to your levels and getting feedback on what is present along a line segment. You use them by providing two endpoints (start and end locations) and the physics system "traces" a line segment between those points, reporting any Actors (with collision) that it hits. Traces are essentially the same as **Raycasts** or **Raytraces** in other software packages.

Whether you want to know if one **Actor** can "see" another, figure out the normal of a specific polygon, simulate high velocity weaponry, or if you need to know that an **Actor** has entered a space; Traces offer you a reliable and computationally cheap solution. This document covers the basic feature set of Traces in Unreal Engine 5 (Unreal Engine).

## Trace by Channel or Object Type

Since Traces use the physics system, you'll be able to define the category of thing you want to trace against. There are two broad categories to choose from: Channels and Object Types. Channels are used for things like visibility and the camera, and almost exclusively have to do with tracing. Object Types are the physics types of Actors with the collision in your scene, such as Pawns, Vehicles, Destructible Actors, and so on.

You can add more Channels and Object types as you need them. See [Add a Custom Object Type to Your Project](/documentation/en-us/unreal-engine/add-a-custom-object-type-to-your-project-in-unreal-engine) for more information on how to do this.

## Returning Single or Multiple Hits

When tracing, you can choose to return the first thing that matches the criteria hit by the trace, or you can return everything hit by the trace that matches the criteria.

Special consideration is given to **Multi Trace by Channel** versus **Multi Trace For Objects**. When using Muli Trace by Channel the trace will return all **Overlaps** up to and including the first **Block**. Imagine shooting a bullet through some tall grass that then impacts a wall.

Multi Trace For Objects will return everything that matches an object type the trace is looking for, assuming the component is set to return trace queries. This makes it great for counting the number of objects between the start and end of the trace.

![Single or Multiple Hits](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99b44cf1-1f0e-4eb4-a1e6-e3f8b1137e4a/single-vs-multi.png)

### Hit Results

When a Trace hits something, it returns a **Hit Result** struct. Available in Blueprints (and also in C++), this is what the struct looks like:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hit Result Struct Blueprint | | **Member** |  | **Definition** | | --- | --- | --- | | **Blocking Hit** |  | Whether or not the hit was a blocking hit. This is used when **Multi Tracing by Channel**, due to the ability to have traces simply overlap and not stop the trace. | | **Initial Overlap** |  | Whether this is the first overlap in a series of results. | | **Time** |  | This is the "Time" of impact along the trace direction ranging from [0.0 to 1.0]. If there was no hit, this will return 1.0. | | **Distance** |  | The distance from the TraceStart to the Location in world space. If there was an initial overlap, this value is 0. | | **Location** |  | The world space location of the hit that is modified based on the shape of the trace. | | **Impact Point** |  | The absolute location of the hit. Does not include the shape of the trace, only the point of the hit. | | **Normal** |  | The direction of the trace. | | **Impact Normal** |  | The normal of the hitting surface. | | **Phys Mat** |  | The **Physical Material** of the hit surface. | | **Hit Actor** |  | The hit **Actor**. | | **Hit Component** |  | The specific **Component** hit. | | **Hit Bone Name** |  | If traced against a **Skeletal Mesh**, this is the name of the bone that was hit. | | **Bone Name** |  | Name of the trace bone hit. It is valid only if we hit a skeletal mesh. | | **Hit Item** |  | Primitive-specific data, recording which item in the primitive was hit. | | **Element Index** |  | Index of the part that was hit if colliding with a primitive with multiple parts. | | **Face Index** |  | If colliding with a trimesh or landscape, this is the index of the face that was hit. | | **Trace Start** |  | The start location of the trace. | | **Trace End** |  | The end location of the trace. | |

## Using Shape Traces

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bad43cc7-fa36-4f83-bc7a-0e4e5469c735/shape-traces-example.png)

When a Line Trace is not enough, you may get the results you are after by using a Shape Trace instead. For example, maybe you are creating a "vision cone" for an enemy, and you want to detect players that enter it. A Line Trace may not be enough as players may be able to avoid detection by ducking under the Line Trace.

In this situation, you could use a Box Trace, Capsule Trace, or Sphere Trace.

![Box Trace Capsule Trace and Sphere Trace](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/976ac17a-c0c9-4469-bf94-94b478cc6f05/traces-overview-shape-traces.png)

Shape Traces function like Line Traces, where you are sweeping and checking for collision from a start point to an endpoint; however, Shape Traces have an added layer of checking because you are using a shape as a volume (of sorts) in your Raycast. You can use a Shape Trace as a Single Trace, or as a Multi Trace, and each is set up in the same manner as a Line Trace; however, you will need to provide additional details about the size (or orientation) of the shape you use.

## Getting UV Coordinates from Trace

A trace can return the UV Coordinates of the Actor it hit, assuming trace complex is used. As of 4.14 this only works on **Static Mesh Components**, **Procedural Mesh Components**, and **BSP**. It will **not** work on **Skeletal Mesh Components** because you trace against the **Physics Asset**, which doesn't have UV coordinates (even if you choose to trace complex).

Using this feature will increase CPU memory usage because Unreal Engine needs to keep an additional copy of vertex positions and UV coordinates in the main memory.

### Enabling UV Coordinates from Trace

To enable this feature, follow these steps:

1. Access your **Project Settings** from the **Edit Menu**.

   ![Access your Project Settings from the Edit Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78696b8b-5256-4410-ae6e-35f6f12cfff6/access-project.png)
2. Enable the **Support UV From Hit Results** feature in the **Physics Section** of your **Project Settings**.

   ![Enable the Support UV From Hit Results feature in the Physics Section of your Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7699bf74-fbeb-4503-bb08-0e05d92e0510/project-settings.png)
3. Restart the Editor.

   You can inspect the Blueprint **Find Collision UV** node using this feature before restarting the editor; however, the node will only return [0.0, 0.0] when you inspect it.
   If you want the node to return the correct UV data, you'll have to restart the editor.

## Other Features

Tracing also has some minor features to limit what they return, making them easier to debug. They can trace against **Complex Collision** (if a Static Mesh or Procedural Mesh has it enabled). If they are called from an **Actor**, they can be told to ignore all attached components by enabling the **Actor** to trace through itself. Finally, they have the option to show a representation of the trace as red and green lines (with larger boxes representing hits).

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [tracing](https://dev.epicgames.com/community/search?query=tracing)
* [raycast](https://dev.epicgames.com/community/search?query=raycast)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Trace by Channel or Object Type](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#tracebychannelorobjecttype)
* [Returning Single or Multiple Hits](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#returningsingleormultiplehits)
* [Hit Results](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#hitresults)
* [Using Shape Traces](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#usingshapetraces)
* [Getting UV Coordinates from Trace](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#gettinguvcoordinatesfromtrace)
* [Enabling UV Coordinates from Trace](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#enablinguvcoordinatesfromtrace)
* [Other Features](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview?application_version=5.7#otherfeatures)
