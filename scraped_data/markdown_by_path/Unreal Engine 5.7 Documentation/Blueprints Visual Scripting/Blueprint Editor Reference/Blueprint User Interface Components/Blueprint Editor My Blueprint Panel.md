<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine?application_version=5.7 -->

# Blueprint Editor My Blueprint Panel

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Blueprint Editor Reference](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine "Blueprint Editor Reference")
7. [Blueprint User Interface Components](/documentation/en-us/unreal-engine/user-interface-components-in-unreal-engine "Blueprint User Interface Components")
8. Blueprint Editor My Blueprint Panel

# Blueprint Editor My Blueprint Panel

Hierarchical breakdown of the nodes within a Blueprint.

![Blueprint Editor My Blueprint Panel](https://dev.epicgames.com/community/api/documentation/image/be3f4755-9133-4b15-823a-493c0d9d767f?resizing_type=fill&width=1920&height=335)

 On this page

The **My Blueprint** tab displays a tree list of the graphs, scripts, functions, macros, etc. contained within the Blueprint. This is essentially an outline of the Blueprint that lets you easily view existing elements of the Blueprint, as well as create new ones.



Different types of Blueprints will have different types of items shown in the **My Blueprint** tab tree list.

![My Blueprint Pane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/671e9734-93a1-4af0-9e47-fd06ffdb9cb0/myblueprintpane.png)

For example, a normal Blueprint will always have a **ConstructionScript** and an **EventGraph**. In addition, any functions created within the Blueprint will be displayed. A Level Blueprint will only have an **EventGraph** and any functions created within it. An Interface will only display the functions created within it. A Macro Blueprint will display the macro functions created within it.

## Creation Buttons

The **My Blueprint** tab has shortcut buttons (the ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41e3428e-8be3-4444-8b21-a7808b4e5760/plus_button.png) at the end of each heading) for creating new variables, functions, macros, event graphs, and event dispatchers.

| **Button** | **Name** | **Description** |
| --- | --- | --- |
| New Variable | **New Variable** | Creates a new variable when clicked. The properties of that variable immediately appear in the **Details** tab. There, you can change the name, type, and other properties. |
| New Function | **New Function** | Creates a new function, then immediately puts focus on the Name field of the **Details** tab so that it can be named. A new graph view will also be opened where you can define the node network for the function. |
| New Macro | **New Macro** | Creates a new macro, then immediately puts focus on the Name field of the **Details** tab so that it can be named. A new graph view will also be opened where you can define the node network for the macro. |
| New Event Graph | **New Event Graph** | Creates a new function, then immediately puts focus on the Name field of the **Details** tab so that it can be named. The new graph appears and is ready to have a node network defined within it. |
| New Event Dispatcher | **New Event Dispatcher** | Creates a new event dispatcher, then immediately puts focus on the Name field of the **Details** tab so that it can be named. |

These same buttons can also be accessed by **Right-clicking** in the **My Blueprint** tab. The **Right-click** menu also includes an option for creating a new enum asset.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93c1e737-7141-42a7-909c-e552f48c7b4f/myblueprint_rightclick.png)

Finally, you can use the **Add New** button at the top of the **My Blueprint** Panel

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03ce2368-df24-48d3-8ed7-12ca87e16e46/addnew.png)

## My Blueprint Sections

The **My Blueprint** tab is divided up into 6 sections: The **Add New**, Graphs, Functions, Macros, Variables, and Event Dispatchers sections.

![My Blueprint Pane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3570ecfe-1ea7-425a-8f17-e080307c1e73/myblueprintpane.png)

The 5 lower sections will organize elements of your Blueprint into their respective groups. While the top section gives you quick access to create new Graphs, Variables, etc... and search the entire **My Blueprint** panel.

## Searching in My Blueprint

The **My Blueprint** tab contains a text box used for searching the graphs belonging to the Blueprint. This works the same way as the contextual action menu that you use for adding new nodes, but is limited to searching items found within **My Blueprint**. You can search based on name, comment, and other data. So, if you know you have a node that is **SetActorHidden**, you can type that in the box, and the explorer will show you all the **SetActorHidden** nodes in your graph.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creation Buttons](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine?application_version=5.7#creationbuttons)
* [My Blueprint Sections](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine?application_version=5.7#myblueprintsections)
* [Searching in My Blueprint](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine?application_version=5.7#searchinginmyblueprint)
