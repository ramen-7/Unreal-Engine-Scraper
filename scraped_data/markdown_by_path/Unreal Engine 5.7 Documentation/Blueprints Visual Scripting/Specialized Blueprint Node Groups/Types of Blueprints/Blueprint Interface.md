<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine?application_version=5.7 -->

# Blueprint Interface

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
6. [Specialized Blueprint Node Groups](/documentation/en-us/unreal-engine/specialized-blueprint-visual-scripting-node-groups-in-unreal-engine "Specialized Blueprint Node Groups")
7. [Types of Blueprints](/documentation/en-us/unreal-engine/types-of-blueprints-in-unreal-engine "Types of Blueprints")
8. Blueprint Interface

# Blueprint Interface

Blueprints that declare functions to define an interface between Blueprints.

![Blueprint Interface](https://dev.epicgames.com/community/api/documentation/image/062695ff-f253-4a44-9c8b-dc1c979463ec?resizing_type=fill&width=1920&height=335)

 On this page

A **Blueprint Interface** is a collection of one or more functions - name only, no implementation - that can be added to
other Blueprints. Any Blueprint that has the Interface added is guaranteed to have those functions. The functions
of the Interface can be given functionality in each of the Blueprints that added it. This is essentially like the
concept of an interface in general programming, which allows multiple different types of Objects to all share and be accessed
through a common interface. Put simply, Blueprint Interfaces allow different Blueprints to share with and send data to one another.

Blueprint Interfaces can be made by content creators through the editor in a similar fashion to other Blueprints, but they
come with certain limitations in that they cannot:

* Add new variables
* Edit graphs
* Add Components

The use of Blueprint Interfaces allows for a common method of interacting with multiple disparate types of Objects that all share
some specific functionality. This means you can have completely different types of Objects, such as a car and a tree, that
share one specific thing like they can both be shot by weapon fire and take damage. By creating a Blueprint Interface that
contains an `OnTakeWeaponFire` function, and having both the car and the tree implement that Blueprint Interface, you can treat the
car and the tree as the same type and simply call the `OnTakeWeaponFire` function when either of them is shot. Read about how to implement
Blueprint Interfaces on the [Implement Interface in Blueprint](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine) page.

## Creating Blueprint Interfaces

Click the **Add** in the **Content Browser**, then select **Blueprints > Blueprint Interface**. Name your new Blueprint Interface.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f58b3f2b-2e0a-4124-b784-acdac8e7f6ce/createinterface.png)


You can also add a Blueprint Interface by right-clicking into **Content Browser**, then **Blueprints > Blueprint Interface**.

![](createdblueprintinterface.png)

Once created, you need to edit the Interface's functions.

## Editing Blueprint Interfaces

Blueprint Interfaces are edited by the **Blueprint Editor**. Since you cannot create your own variables, graphs, or components, the process of Interface editing differs greatly from the process of editing standard Blueprint Classes.

When you first open up a new Interface, the editor looks like this:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca176849-4f39-4e50-bd83-e01672bddf2d/interfaceeditor.png)

If you have just created your Interface, you will see that the Editor has created a new blank Function for you named **NewFunction\_0** and it will be highlighted for you to rename it.

### Adding Functions

Functions are the primary component of an Interface. Interface functions have no implementation. They exist simply as a definition of inputs and outputs. These can be used to send data through the interface, or can be overridden within any Blueprint that implements that Interface.

To add a new function:

1. In the **My Blueprint** tab create a new function, by clicking on the **+** icon on the functions list header.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44eda649-8b7f-4bfb-a496-2ed3b02dcb82/addmyfunction.png)
2. In the **My Blueprint** pane, enter a name for the new function.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fbca9f5-8d46-49a6-9897-5dc5f8bb6bca/renamemyfunction.png)
3. The new Graph area will appear with the new function. Note that the function has neither inputs nor outputs.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de268461-5f55-4250-8e22-ca435296cb2a/newfunctioncreated.png)

### Editing Function Signatures

Since an interface function has no implementation, all you can do as a designer is designate a series of typed inputs and outputs.

To edit a function's signature:

1. In the **Details** tab, scroll to the **Inputs** category and click the **+** icon to create a new Input Parameter.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4045afc7-59b4-4412-ba47-eaeb064fe79f/details_signature.png)
2. Set the Input Name and Type as desired. You may also expand the input using the ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc978a2d-00ea-42e9-bbcf-8dbada9bbb12/button_dropdownarrow.png) button next to the name, and thereby set a Default Value.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/578f36aa-c423-4505-812b-088750a72e69/floatinput-graph.png)
3. In the same manner, outputs can also be added. Note how the graph automatically updates to show them.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5bd5f5a-8367-4ceb-b408-9cf06f1d1d4a/outputbool-graph.png)

### Other Considerations

* On any input or output parameter, you can click the ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f5b2c0a-f239-455c-9ba6-9db8ac206adc/button_x_remove.png) button to remove that parameter.
* Input parameters can be given a default value using the small text field immediately under the parameter name field, though you must expand the property entry in the **Details** tab to see it.
* You can change the order of the input and output parameters on the node. Drag the right edge of the parameters in the **Input** and **Output** sections to adjust them to the order you need.
* You can use the Replicates checkbox for any Interfaces containing functions that need to replicate across the server. This is found within the **Details** tab by first clicking the **Class Settings** button.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Blueprint Interfaces](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine?application_version=5.7#creatingblueprintinterfaces)
* [Editing Blueprint Interfaces](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine?application_version=5.7#editingblueprintinterfaces)
* [Adding Functions](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine?application_version=5.7#addingfunctions)
* [Editing Function Signatures](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine?application_version=5.7#editingfunctionsignatures)
* [Other Considerations](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine?application_version=5.7#otherconsiderations)
