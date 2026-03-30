<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-a-multi-line-trace-raycast-by-object-in-unreal-engine?application_version=5.7 -->

# Using a Multi Line Trace (Raycast) by Object

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
9. Using a Multi Line Trace (Raycast) by Object

# Using a Multi Line Trace (Raycast) by Object

This tutorial covers using a Multi Line Trace by Object Blueprint node to return all World Dynamic Actors it hits, and prints their names.

![Using a Multi Line Trace (Raycast) by Object](https://dev.epicgames.com/community/api/documentation/image/326160fc-1666-49cf-adcb-6493a2932c2e?resizing_type=fill&width=1920&height=335)

 On this page

**Multi LineTrace For Objects** will perform a collision trace along a given line and return all hits encountered, returning only objects that match one of the specified Object Types. Below, you will find steps for setting up a **Multi LineTrace For Objects** Blueprint.

## Steps

1. Follow the steps used for the [Line Trace By Channel](/documentation/en-us/unreal-engine/using-a-single-line-trace-raycast-by-channel-in-unreal-engine) example to set up a trace.
2. Replace the **Line Trace By Channel** node with the **Multi Line Trace For Objects** node.
3. Drag off the **Object Types** pin and add a **Make Array** node, then use the drop-down menus to add Objects to the Array.

   ![Drag off the Object Types pin and add a Make Array node then use the drop-down menus to add Objects to the Array](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23757187-7dcf-42ad-b775-e10122da8b81/guide-how-to-2b-21.png)

   Here we assign **WorldDynamic** and **PhysicsBody** as our Object Types. You can use the **Add pin** button to add more Object Types to the Array.
4. Drag off the **Out Hits** pin of the trace node and add a **For Each Loop** node.

   ![Drag off the Out Hits pin of the trace node and add a For Each Loop node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01652725-e758-48b2-b7f3-7d967e172970/guide-how-to-2b-22.png)

   This will allow us to do something for each of the Actors hit by the trace.
5. Drag off the **Array Element** and add a **Break Hit Result** node. Then, drag off the **Hit Actor**, add a **Get Display Name (Object)** node and connect to a **Print String** node.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72076e41-d2e5-4cfd-8627-77e2b5ea4f62/guide-how-to-2b-23.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72076e41-d2e5-4cfd-8627-77e2b5ea4f62/guide-how-to-2b-23.png)

   Click image for a full view.

   This will now print to the screen each of the Actors hit by the array.

## Result

Here, we have a hanging ceiling light (World Dynamic Object Type) in front of a Physics Actor (Physics Body Object Type).

![A hanging ceiling light World Dynamic Object Type in front of a Physics Actor Physics Body Object Type](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1089d63-7b40-4e5e-a189-a311cbf5861e/guide-how-to-2b-20.png)

Multi LineTrace For Objects, unlike Multi Line Trace by Channel, does not stop at the first object it hits, which is why the trace continues through the light to the cube.

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [tracing](https://dev.epicgames.com/community/search?query=tracing)
* [raycast](https://dev.epicgames.com/community/search?query=raycast)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-a-multi-line-trace-raycast-by-object-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/using-a-multi-line-trace-raycast-by-object-in-unreal-engine?application_version=5.7#result)
