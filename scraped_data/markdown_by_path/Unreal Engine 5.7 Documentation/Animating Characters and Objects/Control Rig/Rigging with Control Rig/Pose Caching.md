<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7 -->

# Pose Caching

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
6. [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine "Control Rig")
7. [Rigging with Control Rig](/documentation/en-us/unreal-engine/rigging-with-control-rig-in-unreal-engine "Rigging with Control Rig")
8. Pose Caching

# Pose Caching

Save bone poses and states to reference in your Control Rig graph.

![Pose Caching](https://dev.epicgames.com/community/api/documentation/image/9f82b9d6-a2b7-435c-9da7-c4cf9ec59f71?resizing_type=fill&width=1920&height=335)

 On this page

The Pose Caching feature in Control Rig is used to save and apply animation poses at different times in the control rig graph. Any **[Rig Element](/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine)** can be cached into a pose and different properties can be accessed within the rig graph, such as curve values or transforms.

This document provides an overview of the Pose Caching feature, and how to store and apply poses.

#### Prerequisites

* You have created a Control Rig Asset for a character. See the **[Control Rig Quick Start](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine)** page for information on how to do this.

## Quickstart

The following is a quick guide showing how to store and retrieve a pose.

### Storing Poses

Poses are stored as variables within Control Rig's **My Blueprint** panel. To create a new pose variable, click the **Add (+)** button on the **Variables** category and set the variable type to **Rig Pose**.

![rig pose variable](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a998441a-ac21-4034-a2b7-fd764687aae9/posevar.png)

Next, reference the variable within the Rig Graph as a **Set** operation by dragging the variable into the graph and selecting **Set**.

![rig pose reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f495ebd-acb6-423b-89e7-3fb8873b34de/store1.png)

Then, create a **Get Pose Cache** node by right-clicking in the graph and selecting **Get Pose Cache**. Connect the **Pose** and **Value** pins.

![gest pose cache](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a7fb713-0de9-4992-906c-507809601efb/store2.png)

Lastly, connect the Set node to an event. In this example, you can connect it to the **[Setup Event](/documentation/en-us/unreal-engine/control-rig-forwards-solve-and-backwards-solve-in-unreal-engine#setupevent)**, which will store the character's initial A-Pose.

![store control rig pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1f88304-358e-49b1-a343-dc80f39082d4/store3.png)

### Applying Poses

Poses are applied by using the **Apply Pose Cache** node, which reads from your Rig Pose variable.

To start, reference the Rig Pose variable in the graph as a **Get** operation by dragging the variable into the graph and selecting **Get**.

![rig pose reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4edd233-9529-4fdf-b2fc-951c0fb5d63c/apply1.png)

Then, create an **Apply Pose Cache** node by right-clicking in the graph and selecting **Apply Pose Cache**. Connect the **Pose** and **Value** pins. Also connect it to an event so you can preview its evaluation, like the **[Forwards Solve](/documentation/en-us/unreal-engine/control-rig-forwards-solve-and-backwards-solve-in-unreal-engine#forwardssolve)** event.

![apply pose cache](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efcaf91b-67f1-474f-aa3c-b36a5549c055/apply2.png)

Since you are applying the entire pose, you can preview the pose effect by editing the **Weight** value. For this example, you can also use a Preview Controller from the **[Preview Scene Settings](/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine#previewscenesettings)** in order to better see the pose application.

![apply pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d3a0584-e84b-4646-80e4-99ba57b33047/apply3.gif)

## Pose Cache Nodes

The following pose cache nodes are available for use in your Control Rig Graph:

| Name | Image | Description |
| --- | --- | --- |
| **Apply Pose Cache** | apply pose cache | Applies a saved pose. Includes properties for setting rig elements, the transform space, items to set, and weight. |
| **For Each Pose Cache Element** | for each pose cache element | This node executes iteratively across all items from a given pose. |
| **Get Pose Cache** | get pose cache | Saves a pose based on the input of **Items to Get** and rig element types. If no items are specified, then all items will be used. |
| **Get Pose Cache Curve** | get pose cache curve | Gets a single **[Animation Curve](/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine)** from a saved pose. |
| **Get Pose Cache Delta** | get pose cache delta | Compares two poses and outputs a comparison check boolean. |
| **Get Pose Cache Items** | get pose cache items | Returns rig elements in an item array. |
| **Get Pose Cache Transform** | get pose cache transform | Gets the transform or Animation Curve value from a single rig element in a pose. |
| **Get Pose Cache Transform Array** | get pose cache transform array | Gets the transforms of all items in a pose and returns them as a transform array. |
| **Is Pose Cache Empty** | is pose cache empty | Checks if a pose is empty or not. |
| **Draw Pose Cache** | draw pose cache | Draws axis debug information on the saved pose in the viewport. It will only draw the elements saved in a pose. draw pose cache |

Most nodes related to pose caching contain the following common properties:

![apply pose cache](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8411dfe-ce95-4ea8-9f04-3c89329b8544/node_apply.png)

| Name | Description |
| --- | --- |
| **Element Type** | The Rig Elements to filter for when saving poses. You can choose from the following elements:   * **Bones** * **Nulls** * **Controls** * **Curves** * **All** |
| **Space** | The transform space that the pose information should be stored and applied in. Can either be **Local** or **Global** space. |
| **Items to Set** | An array of rig elements to include when saving the pose. If nothing is set here, then all elements will be included according to the **Element Type** specified. |

## Workflow Examples

By using array building nodes, like **Get Children**, you can get just a subsection of rig elements to save into a pose. This is useful if you want to only save and apply the pose to certain elements.

![apply pose partial](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa207eaa-5d60-4366-8618-0bfb3f1bfe4c/childrenexample.gif)

Execution nodes like **Branch** can be used to save poses at specific times or states.

![branch set pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4989eacb-f827-4606-ae08-a2c60bb9cf9e/branch.png)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)
* [pose caching](https://dev.epicgames.com/community/search?query=pose%20caching)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7#prerequisites)
* [Quickstart](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7#quickstart)
* [Storing Poses](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7#storingposes)
* [Applying Poses](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7#applyingposes)
* [Pose Cache Nodes](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7#posecachenodes)
* [Workflow Examples](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine?application_version=5.7#workflowexamples)
