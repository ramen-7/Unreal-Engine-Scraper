<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7 -->

# Struct Variables in Blueprints

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
7. [Blueprint Variables](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine "Blueprint Variables")
8. Struct Variables in Blueprints

# Struct Variables in Blueprints

Blueprint struct variables allow you to store different data types that contain related information together.

![Struct Variables in Blueprints](https://dev.epicgames.com/community/api/documentation/image/402584fc-d4f0-4c05-8304-566441a8b10c?resizing_type=fill&width=1920&height=335)

 On this page

A struct is a collection of different types of data that are related and held together for easy access. You've probably used simple structs in Blueprints already, as
Vectors, Rotators, and Transforms are all struct variables. For example, a Vector struct holds an X float, a Y float, and a Z float variable that are related to each other.

Structs can also nest their data. A Transform struct holds Location (a Vector struct), Rotation (a Rotator struct), and Scale (a Vector struct) data about an Actor.

## Creating Structs

You add a struct variable to your Blueprint in the same way you add any other [Blueprint variable](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine). Simple structs, like Vectors, Rotators, and Transforms, are listed in the top section of the variable type dropdown menu.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6342b9f4-9fbf-4f9b-99ce-9fe0e2d4c272/addsimplestruct.png)

There is also a **Structure** section of the dropdown menu, where you can find all struct variables currently available to your Blueprint.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad4e27ac-9ff9-4a41-bf44-8861bc2996a1/addcomplexstruct.png)

## Accessing Struct Information

Because structs work by bundling data together, you also need to work on accessing those smaller chunks of information. You can do that through a few different methods:

### Splitting Struct Pins

If you want to be able to access the individual variables in a struct on a single node, splitting struct pins can be a helpful tool.

To split a struct pin, right-click on the pin and select **Split Struct Pin**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3829488-8124-4aeb-adc4-ba00dd1a57de/splitstructpin.png)

This exposes all of the variables contained within the struct as individual pins on the node, allowing you to enter values or manipulate them independently.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68a6530a-45c1-4e2b-9c7c-9447a2770d0d/locationxyz.png)

To undo a **Split Struct Pin**, right-click on any of the new pins and select **Recombine Struct Pin**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9e4cc14-fdf4-44f0-93b4-5c0f46c02a40/recombinestructpin.png)

You can split and recombine both input and output struct pins.

### Breaking Structs

Often, taking apart a struct into its individual parts will be gameplay logic you repeat in a function or macro. Using a **Break Struct** node allows you to replicate that behavior throughout your Blueprint graph easily.
To create a **Break Struct** node, drag off of a struct output pin and select **Break [Struct Name]** from the context menu.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1fde7c7d-5c73-48ea-896a-9eb899aa3946/breakhitresult.png)

The **Break Struct** node will have a different name and different output pins depending on the struct you use, but overall will break the struct into its individual parts.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8d71896-a03f-409c-8a48-404d9f560cdd/brokenhitresult.png)

For example, if you always want to work with the **Impact Point**, **Hit Component**, and **Hit Bone Name** of a **Hit Result**, you can have a **Break Hit Result** node inside a function that means that you can just input **Hit Result**
as a function input, and always have those three data pieces separated out inside the function.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7204456-e791-4805-a79d-2dd9c53ab9d4/breakhitexample.png)

### Making Structs

Much like you can break a struct into its individual pieces of data, you can make a struct out of the right data as well.

To create a **Make Struct** node, drag off of a struct input pin and select **Make [Struct Name]** from the context menu.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c054acfa-04bf-4ca2-a7a5-6222e7149479/makelinearmenu.png)

The **Make Struct** node will have a different name and different input pins depending on the struct you use, but overall will enable you to build a struct out of all the data it contains.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e4edced-b94e-4070-878e-5edc01e71987/makelinearcolor.png)

### Setting Members in Structs

Sometimes, structs can contain a lot of data, and you only want to change a few elements out of that set. Setting members in a struct enables you to be very specific about what data you change, without having to wire up all the
data pins that are remaining constant.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eff84f25-9148-48bc-b34b-5243430a8499/setmembersinstruct.png)

To change which members are available through the **Set Members in Struct** node, select the node. In the **Details** panel, there are checkboxes for each possible member to expose as a pin on the node. Member variables that are not exposed
will not be changed by the **Set Members in Struct** node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f9c6cd8-d855-41d2-850b-dd3181e0d73e/setmembersdetails.png)

## Using Custom Structs

In addition to using the structs supplied within the Engine, you can create your own custom structs with your own variables and values.�

To create a custom struct, right-click in the�**Content Browser�**then under�**Create Advanced Asset�**and�**Blueprints,�**select�**Structure**.�

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e440d46c-06cc-4047-b3a9-b24511c583fa/structs.png "Structs.png")

Once you define the name of the struct and open it, inside the **Structure Window�**you can add variables and their default values.�

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38d930fd-a9ad-4aee-9c15-5fcbaf27419d/structwindow.png "StructWindow.png")

You can then add this struct as a variable inside any other Blueprint by creating a variable and assigning the�**Variable Type�**to the name of your struct.��

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e024e13-28e1-40a0-a96f-b670854c3991/creatingstructvar.png "CreatingStructVar.png")

After compiling, you will see all the variables you've added to the struct that can be defined.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e25cdad-a137-418a-b1f5-e14115c9a988/defaultvalues.png "DefaultValues.png")

### Breaking Custom Structs

When you add a custom struct to a graph, you can drag off it and break it a part in order to access the variables within it.�

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66a377e6-88e3-43aa-b26f-bbc2e2335924/breakstruct.png "BreakStruct.png")

You can then connect individual variables from the struct to other Blueprint nodes. Optionally, from the�**Details�**panel, you can click the�**Hide Unconnected Pins�**button to hide any pins that are not connected to other Blueprint nodes.�

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/642bc34f-9417-4b35-b67e-b97fc52c4371/hideunconnectedpins.png "HideUnconnectedPins.png")

Any pins that are not connected will be hidden on the Break Struct node.�

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a81ebda9-a423-4c46-b641-5388d9e80c63/hiddenpins.png "HiddenPins.png")

You can re-enable the showing of the pins from the�**Details�**panel by enabling the (As pin) property next to your desired variable.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [arrays and structures](https://dev.epicgames.com/community/search?query=arrays%20and%20structures)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#creatingstructs)
* [Accessing Struct Information](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#accessingstructinformation)
* [Splitting Struct Pins](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#splittingstructpins)
* [Breaking Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#breakingstructs)
* [Making Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#makingstructs)
* [Setting Members in Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#settingmembersinstructs)
* [Using Custom Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#usingcustomstructs)
* [Breaking Custom Structs](/documentation/en-us/unreal-engine/blueprint-struct-variables-in-unreal-engine?application_version=5.7#breakingcustomstructs)
