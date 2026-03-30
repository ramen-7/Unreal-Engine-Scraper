<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/find-result-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine?application_version=5.7 -->

# Blueprint Editor Find Result Panel

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
8. Blueprint Editor Find Result Panel

# Blueprint Editor Find Result Panel

Panel that is a search tool within the Blueprint Editor that allows you to quickly track down a variety of objects.

![Blueprint Editor Find Result Panel](https://dev.epicgames.com/community/api/documentation/image/35f6ddf5-2d88-422e-8f4a-d7305a20aabf?resizing_type=fill&width=1920&height=335)

 On this page

The **Find Results** panel is a powerful search tool within the Blueprint Editor that allows you to quickly track down a variety of objects based on the following criteria:

* Node name
* Pin name
* Node Comment
* Property name
* Property value

As the **Find Results** panel tracks down search matches, it will display a list of results, each of which works like a hyperlink that will jump the graph view to the resulting node. This makes it an excellent way to track down a specific node or piece of information that may be buried somewhere within a complex network of Blueprint scripting nodes.

Much like searching in a web browser, the **Find Results** panel is available by pressing **Ctrl-F** while working in the Blueprint Editor. By default, the panel will appear along the bottom of the **Graph** Panel. If the **Compiler Results** panel is showing, then the **Find Results** panel will dock alongside it.

Unlike many search fields in Unreal Engine 4, the **Find Results** panel does not filter results actively while you type, due to the sheer volume of possible results. Once you press **Enter**, the list will populate.

## Interface

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fd96b94-3db1-4a9f-81db-aaa0d6b2b51b/findresults.png)

1. **Results list** - This lists all nodes, pins, property names, comments, and property values that match the search criteria.
2. **Search filter** - This is where you type in what you are looking for.
3. **Property values** - Explicitly set property values will appear in parentheses in the middle of the results.
4. **Comments** - Node comments, if they exist, will appear in yellow text on the right side of the panel.
5. **Find in Current Blueprint Only** - When active, the search is limited only to the current Blueprint. When deactivated, the search looks through all Blueprints in the project.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Interface](/documentation/en-us/unreal-engine/find-result-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine?application_version=5.7#interface)
