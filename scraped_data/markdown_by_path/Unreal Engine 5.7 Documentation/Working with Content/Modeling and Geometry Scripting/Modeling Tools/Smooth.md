<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/smooth-tool-in-unreal-engine?application_version=5.7 -->

# Smooth

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
6. [Modeling and Geometry Scripting](/documentation/en-us/unreal-engine/modeling-and-geometry-scripting-in-unreal-engine "Modeling and Geometry Scripting")
7. [Modeling Tools](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine "Modeling Tools")
8. Smooth

# Smooth

Overview of the Smooth modeling tool for softening the edges of a mesh.

![Smooth](https://dev.epicgames.com/community/api/documentation/image/3cd74aad-7bfb-429f-9522-24e3809752ee?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Smooth** tool softens the edges of surfaces by moving vertices towards the averaged location of their neighbors. This operation is helpful to use when a mesh has jagged edge artifacts.

![Jagged Cobble](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/403f8f4b-dd49-42e6-8088-fabbecc4d173/jagged-cobble.png)

![Smooth Cobble](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f59b4e4-d34e-4b2f-b38c-477f4ddc205f/smooth-cobble.png)

Jagged Cobble

Smooth Cobble

## Accessing the Tool

You can access the Smooth tool from the following:

* The **Deform** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

## Using Smooth

How you smooth your mesh is set by the **Smoothing Type** property. Each smoothing type has options to adjust the smoothing amount.

The **Fast Iterative** and **Fast Implicit** smoothing types have a vertex weight map option to adjust specific areas of your mesh. You must first create the weight map layer in the [Attribute Edit](/documentation/en-us/unreal-engine/edit-attributes-tool-in-unreal-engine) tool. The comparison images above use a weight map to create the cobblestone effect.
To learn more about creating weight maps, see [Paint Maps Tool](/documentation/en-us/unreal-engine/paint-maps-tool-in-unreal-engine).

Sometimes, your mesh can seem to have disappeared when using the Smooth tool. Your mesh has not disappeared but has significantly smoothed and shrunken in size. This change in size happens based on the resolution (number of triangles) of your mesh and values used with the **Iterative Smoothing Options**.

To avoid this issue, do one of the following:

* Increase the number of triangles the mesh has with the **Remesh** tool (you must cancel the current tool session to do this).
* Lower the **Smoothing Per Step** setting under the **Iterative Smoothing Options**.
* Lower the **Steps** settings under **Iterative Smoothing Options**.

Once you are done using the tool, accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

### Hotkeys

| **Key Command** | **Operation** |
| --- | --- |
| **F** | Zooms into the location of the mesh. |
| **ESC** | Cancels the changes and exits the tool. |
| **Enter** | Accepts the tool changes. |

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [sculpting](https://dev.epicgames.com/community/search?query=sculpting)
* [skeleton editing](https://dev.epicgames.com/community/search?query=skeleton%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/smooth-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Smooth](/documentation/en-us/unreal-engine/smooth-tool-in-unreal-engine?application_version=5.7#usingsmooth)
* [Hotkeys](/documentation/en-us/unreal-engine/smooth-tool-in-unreal-engine?application_version=5.7#hotkeys)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
