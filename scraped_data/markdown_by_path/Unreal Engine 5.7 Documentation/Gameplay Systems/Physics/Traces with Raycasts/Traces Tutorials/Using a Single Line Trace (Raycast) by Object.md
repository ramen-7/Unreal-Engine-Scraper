<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-a-single-line-trace-raycast-by-object-in-unreal-engine?application_version=5.7 -->

# Using a Single Line Trace (Raycast) by Object

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
8. [Traces Tutorials](/documentation/en-us/unreal-engine/traces-tutorials-in-unreal-engine "Traces Tutorials")
9. Using a Single Line Trace (Raycast) by Object

# Using a Single Line Trace (Raycast) by Object

This how-to guide covers using a Single Line Trace by Object Blueprint node to return the first World Dynamic Actor it hits, and prints its name.

![Using a Single Line Trace (Raycast) by Object](https://dev.epicgames.com/community/api/documentation/image/206f9c2a-c211-479a-9e84-37a440b4989f?resizing_type=fill&width=1920&height=335)

 On this page

**Line Trace For Objects** will perform a collision trace along a given line and return the first Object the trace hits that matches one of the specified Object Types. To set up a **Line Trace For Objects** Blueprint, do the following:

## Steps

1. Follow the steps used for the [Line Trace By Channel](/documentation/en-us/unreal-engine/using-a-single-line-trace-raycast-by-channel-in-unreal-engine) example to set up a trace.
2. Replace the **Line Trace By Channel** node with the **Line Trace For Objects** node.
3. Drag off the **Object Types** pin and add the **Make Array** node.

   ![Drag off the Object Types pin and add the Make Array node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff8e9a25-292b-4e14-b517-8f3820c98855/guide-how-to-2b-12.png)
4. On the **Make Array** node, specify the **ObjectType** you want to trace for (via the drop-down menu).

   ![Specify the ObjectType you want to trace for via the drop-down menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0c9ca92-04b4-4914-a962-424740f589f2/guide-how-to-2b-13.png)


   Here, we are tracing for **WorldDyanmic** Objects. You can add more by clicking the **Add Pin** button.
5. You can set the rest of the trace up the same way a **Line Trace By Channel** is setup.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/929e45ee-4478-42b1-8e81-5049090780cf/guide-how-to-2b-15.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/929e45ee-4478-42b1-8e81-5049090780cf/guide-how-to-2b-15.png)

   Click image for a full view.

## Result

We have added a single WorldDynamic Object to our level.

![A single WorldDynamic Object in our level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/812ef67c-6d6f-45a0-ad2f-00b3e75c2d1b/guide-how-to-2b-16.png)

Only the added Actor is now returning as a hit; consequently, the cubes (since they are Physics Actors) do not return a hit.

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [tracing](https://dev.epicgames.com/community/search?query=tracing)
* [raycast](https://dev.epicgames.com/community/search?query=raycast)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-a-single-line-trace-raycast-by-object-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/using-a-single-line-trace-raycast-by-object-in-unreal-engine?application_version=5.7#result)
