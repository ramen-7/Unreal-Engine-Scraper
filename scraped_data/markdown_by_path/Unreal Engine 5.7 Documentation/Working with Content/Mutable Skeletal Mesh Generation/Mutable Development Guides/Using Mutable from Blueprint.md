<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7 -->

# Using Mutable from Blueprint

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
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Development Guides](/documentation/en-us/unreal-engine/mutable-development-guides-in-unreal-engine "Mutable Development Guides")
8. Using Mutable from Blueprint

# Using Mutable from Blueprint

How to use Mutable Characters from Blueprints.

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

You can use the following document to learn about how to set up and use Mutable Characters in Blueprints.

## Creating a Customizable Character

You can use the following steps to create a new Mutable Character in a Blueprint.

1. Create a new \*\*Actor Blueprint. After creating the blueprint, name and open the asset.

   ![custom blueprint actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/427d77d4-4fc1-4796-a1e9-3f89d3ed4845/image_0.png)


   Alternatively, you can use a class/BP that has a skeletal mesh component.
2. In the blueprint editor, in the **Components** panel, select the **Skeletal Mesh** component and add a new **Customizable Skeletal** component as a child.

   ![add customizable skeletal mesh components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7954d3ed-5203-4324-9e8f-259dd8198f59/image_1.png)
3. Name the **Skeletal Mesh** and the **Customizable Skeletal** components `Body` and `Body_CO` respectively.

   ![name body components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a29b9e64-3ef6-417a-8edd-80b4c3bab1ad/image_2.png)
4. Select the **Skeletal Mesh** component, then navigate in the **Details** panel to the **Customizable Skeletal Mesh** section and set the instance to be used in the **Customizable Object Instance** property using the asset selection drop-down menu.

   ![select instance in details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3112c0e3-e660-4f8a-ac8d-f05604cd5f9a/image_3.png)
5. Then set the **Component Name** property of the Skeletal Mesh component to `Body`. By doing this you will already see the body of the character in the BP's viewport.

   ![character body in viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ad88598-6974-4ce9-b460-054459a6ee5d/image_4.png)
6. Next, add a new **Skeletal Mesh** component for the character’s head. It should be a child of the `Body` Skeletal Mesh component. Then name the new Skeletal Mesh component `Head`.

   ![add head body component in components panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c838ea6b-8425-4f24-93a9-e5d9f8e71a37/image_5.png)
7. Create a new **Customizable Skeletal** component as child of the `Head` Skeletal Mesh component and name it `Head_CO`.

   ![add customizable skeletal component to head component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/521665cc-0b6e-4c65-829e-f0c8d78d63a5/image_6.png)
8. Select the `Head` **Skeletal Mesh** component and add the same instance that we added to the body component, then set the **Component Name** property to `Head`.

   ![set head instance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4c91493-6b84-4577-96ae-bf73e24d3624/image_7.png)

Your mutable character is now set up in the Actor Blueprint and is visible in the blueprint viewport.

![completed setup of character](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aeee771a-2ef8-43e2-a7bc-8b3d6ce95546/image_8.png)

## Changing Parameters

Parameters are stored by instances and can be accessed or modified using the API nodes. You can reference the following examples to learn how to set parameter values based on their type.

### Boolean Parameter

![boolean parameter setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dbb8ebdd-c799-41ff-a2d1-cf085d00326d/image_9.png)

### Int Parameter

It's important to make sure that the desired option actually exists within the instance. Search existing parameters using the **FindParameter** node and then get the available option with **GetIntParameterAvailableOption** node. Both nodes must use the `CustomizableObject` reference variable as a target, which can be accessed through the `CustomizableObjectInstance` reference variable.

![integer int parameter setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad07a753-20e1-4b5d-9fe8-6985ac70e8ae/image_10.png)

### Float Parameter

![float parameter setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad91baee-2fb9-4a59-8dbf-f25ff9fa0949/image_11.png)

### Color Parameter

![color parameter setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e78b924f-835f-435f-a3da-3b3b45b24f2f/image_12.png)

### Projector Parameter

![projector parameter setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/059b4c4c-a67a-481d-870b-48f9b059350c/image_13.png)

## Update Instances

To apply recent changes in parameters, the instance needs to be updated. This can be achieved by adding an **UpdateSkeletalMeshAsync** node after one or more changes.

![update instances example blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4613c35-b44a-49bc-a0d7-dafc1a078644/image_14.png)

## Updated Delegate

Events can be registered to this delegate. The broadcasting will take place after the completion of the skeletal mesh update.

| Bind Event to Updated Delegate | Unbind Event from Updated Delegate |
| --- | --- |
| bind event to updated delegate node | unbind event to updated delegate node |

## Parameter Information

Sometimes, additional information like the amount of parameters within an instance, their type or the name of an int parameter's option might be useful. This information is kept in the source `CustomizableObject` reference variable, which is accessible through the instance, and can be retrieved using the following nodes:

| Node | Image |
| --- | --- |
| **Get Parameter Count** | get parameter count node |
| **Get Parameter Name** | get parameter name node |
| **Get Parameter Type by Name** | get parameter type by name node |
| **Find Parameter** | find parameter node |
| **Get Int Parameter Num Options** | get int parameter num options node |
| **Get Int Parameter Available Option** | get int parameter available option node |

## Changing States

States can also be queried and changed using the node API:

![get current state node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba4355ec-30f4-4db6-a6ab-a20691605bb0/image_23.png)

As when changing parameters, the instance needs to be updated with a UpdateSkeletalMeshAsync node after a State change.

![using current state variable setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1dd04e89-b8f2-4632-8bcb-2615df23d106/image_24.png)

## State Information

Information about the number and name of States a **CustomizableObject** has, as well as the number and names of parameters in a State can be useful. This information is stored per **CustomizableObject**, and is accessible through a **CustomizableObjectInstance** and can be retrieved using the following nodes:

| Node | Image |
| --- | --- |
| **Get State Count** | get state count node |
| **Get State Name** | get state name node |
| **Get State Parameter Count** | get state parameter count node |
| **Get State Parameter Name** | get state parameter name node |

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Customizable Character](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#creatingacustomizablecharacter)
* [Changing Parameters](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#changingparameters)
* [Boolean Parameter](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#booleanparameter)
* [Int Parameter](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#intparameter)
* [Float Parameter](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#floatparameter)
* [Color Parameter](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#colorparameter)
* [Projector Parameter](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#projectorparameter)
* [Update Instances](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#updateinstances)
* [Updated Delegate](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#updateddelegate)
* [Parameter Information](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#parameterinformation)
* [Changing States](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#changingstates)
* [State Information](/documentation/en-us/unreal-engine/using-mutable-from-blueprint-in-unreal-engine?application_version=5.7#stateinformation)
