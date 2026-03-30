<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---constraints-graph?application_version=5.7 -->

# Physics Asset Editor - Constraints Graph

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
7. [Physics Asset Editor](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine "Physics Asset Editor")
8. [Physics Asset Editor Interface](/documentation/en-us/unreal-engine/physics-asset-editor-interface-in-unreal-engine "Physics Asset Editor Interface")
9. Physics Asset Editor - Constraints Graph

# Physics Asset Editor - Constraints Graph

User guide for the Constraints Graph inside the Physics Asset Editor.

![Physics Asset Editor - Constraints Graph](https://dev.epicgames.com/community/api/documentation/image/2adbd91c-7431-4c28-b645-a3a80b789002?resizing_type=fill&width=1920&height=335)

 On this page

![The Constraints Graph shows the linkages for constraints between the selected bodies in the Physics Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51e6e4f6-abbd-43f3-afb6-102d58f52e66/graph.png)

The **Constraints Graph** shows the linkages for constraints between the selected bodies in the Physics Asset. Within it, you can perform the following actions:

* Select and view bodies and constraints in the skeletal hierarchy.
* Create and edit bodies and constraints using the [right-click context menus](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---skeleton-tree#selectioncontextmenus).
* Create constraint links using pin-dragging selection.
* Assign / Unassign profiles for Physical Animation and Constraints.

## Skeletal Hierarchy Selection Displayed in the Graph

When bodies or constraints are selected in the [Skeleton Tree](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---skeleton-tree), the graph will display the currently selected ones and their connections.

![The graph will display the currently selected ones and their connections](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5356cccd-8bb6-4509-af59-09ea802b4250/graph-with-skel-selection.png)

The body "spine\_03" is selected in the Skeleton Tree, and the Graph displays the constraints and the bodies they connect to.

### Bodies

When a [Body](/documentation/en-us/unreal-engine/physics-bodies-in-unreal-engine) is selected, the Graph will display the following information:

* Bone Name
* Number of Primitive Shapes used

![The Graph will display the following information](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/542b09c5-a6f4-44ed-93a7-6640cf33afc7/body-info.png)

In this example, the Bone Name is **hand\_l** and there is a single primitive shape.

You can double-click any Body node on the far right to move through the hierarchy list to that body and its constraints.

#### Graph Pin-Dragging Connections

The node-based display in the graph enables you to drag from the output pin of the main Body (far left, **hand\_l**) and use the selection menu to select a body to create a constraint. The same
workflow can be achieved through the right-click context menus in the [Skeleton Tree](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---skeleton-tree#selectioncontextmenus) as well.

|  |  |
| --- | --- |
| The node-based display in the graph enables you to drag from the output pin of the main Body and use the selection menu to select a body to create a constraint | The resulting Constraint |
| Pull off the Body output pin and select a Body from the list. | The resulting Constraint. |

If the Graph does not update after creating or deleting a constraint, click away and then back to see the update.

### Constraints

When a [Constraint](/documentation/en-us/unreal-engine/physics-constraint-reference-in-unreal-engine) is selected, the Graph will display the following information:

* Bone Names that are linked

![The Graph will display the following information](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c83f1a4d-aebf-47c7-b81d-b45856ae3609/constraint-info.png)

Here, the Bone named **lowerarm\_l** is constrained to **hand\_l**.

## Profile Assignment

In the Graph, you'll be able to see the [Profiles](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---tools-and-profiles#currentprofileassignment) that the selected bodies and constraints are assigned to.

There are two types of profiles that can be created and assigned: **Physical Animation** which bodies can be assigned to and Constraint ones which constraints can be assigned to. Profiles contain a set of default values for properties of bodies and constraints. When the **Current Profile** is set in the **Profiles** tab, the nodes in the Graph will indicate their assignment status of a profile for the displayed bodies and constraints.

There are two states that a node can be in indicated by its color:

* Is **assigned** to a profile.
* Is **not assigned** to a profile or none is selected

When the **Current Profile** is assigned to the selected body or constraint, or if none is selected, the node's fill color (green for bodies and beige for constraints) is used. When the selected body or constraint is not assigned to the Current Profile, the node will be shaded.

![When the Current Profile is assigned to the selected body or constraint the node's fill color is used](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf97da94-8b36-4570-b6e4-8adcb5db470a/profile-assignment.png)

Here, the bodies for **lowerarm\_l** and **middle\_01\_l** have been assigned the profile **MyPhysicalAnimation\_Profile**, and the remaining body nodes have not been assigned this particular profile, as
indicated by their shaded color.

![The bodies for lowerarml and middle01l have been assigned the profile MyPhysicalAnimationProfile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7be5482c-2449-46f0-baf6-12fd37bf87d7/profile-assignment-none.png)

For the constraints, since the Current Profile is set to **None**, the fill color remains unshaded until any selected constraints are assigned a selected profile.

For additional information about using Profiles and assigning them to bodies and constraints, see the [Tools and Profiles](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---tools-and-profiles#currentprofileassignment) page.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Skeletal Hierarchy Selection Displayed in the Graph](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---constraints-graph?application_version=5.7#skeletalhierarchyselectiondisplayedinthegraph)
* [Bodies](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---constraints-graph?application_version=5.7#bodies)
* [Graph Pin-Dragging Connections](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---constraints-graph?application_version=5.7#graphpin-draggingconnections)
* [Constraints](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---constraints-graph?application_version=5.7#constraints)
* [Profile Assignment](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine---constraints-graph?application_version=5.7#profileassignment)
