<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-customizable-states-in-mutable-with-unreal-engine?application_version=5.7 -->

# Using Customizable States

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
7. [Mutable Optimizing and Debugging](/documentation/en-us/unreal-engine/mutable-optimizing-and-debugging-in-unreal-engine "Mutable Optimizing and Debugging")
8. Using Customizable States

# Using Customizable States

An overview of using Customizable States to optimize your Mutable content.

![Using Customizable States](https://dev.epicgames.com/community/api/documentation/image/7e6d780c-f5a3-4da1-a32b-3f1b0c39097f?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

When an application uses complex Customizable Objects with many parameters, updating the instances may be a costly process that takes many milliseconds. In game, there are some usage scenarios that require these updates to be interactive (big delays are not acceptable). Mutable addresses these problems with the concept of **States**.

A State represents a specific use case of a Customizable Object in your game. For example, at some point during the character creation you may want to let the player customize the face and hair of a character. During this stage, you show a close up camera of the character head and display a user interface for the related parameters: hair color, nose size, hair style, and so on. During this stage, you will not be modifying other parameters, like t-shirt color or torso tattoos. In order for Mutable to provide maximum performance, you can create a State in your Customizable Object, with the subset of parameters that you will modify in this stage. The system will generate an optimized version of the data that updates faster while in this State.

In the **Editor Preview Instance** window, you can choose which state to use by using the **State** dropdown:

[![The Mutable States Dropdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4d25225-b94c-419c-af14-3980d987964b/mutable-states-dropdown.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4d25225-b94c-419c-af14-3980d987964b/mutable-states-dropdown.png)

The Mutable States dropdown.

You must set the state of the Customizable Object Instance before the update is issued by calling `void SetCurrentState(const FString& StateName)`.

## Runtime Parameters

The **Runtime Parameters** array defines the set of parameters that Mutable uses to optimize a given State. Each of these parameters can be of the following types:

* [Object Group](https://github.com/anticto/Mutable-Documentation/wiki/Node-Object-Group)
* [Float Parameter](https://github.com/anticto/Mutable-Documentation/wiki/Node-Float-Parameter)
* [Enum Parameter](https://github.com/anticto/Mutable-Documentation/wiki/Node-Enum-Parameter)
* [Color Parameter](https://github.com/anticto/Mutable-Documentation/wiki/Node-Color-Parameter)
* [Texture Parameter](https://github.com/anticto/Mutable-Documentation/wiki/Node-Texture-Parameter)
* [Projector Parameter](https://github.com/anticto/Mutable-Documentation/wiki/Node-Projector-Parameter)
* [Group Projector Parameter](https://github.com/anticto/Mutable-Documentation/wiki/Node-Group-Projector-Parameter)

The Runtime Parameters array can be found at the bottom of the **Base Object** and **Child Object** properties:

[![Runtime Parameters Array](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/291ec8d9-3a1c-466c-9274-ef242d2b2297/mutable-runtime-param.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/291ec8d9-3a1c-466c-9274-ef242d2b2297/mutable-runtime-param.png)

The Runtime Parameters Array

## Optimization Options

States also give you more options in order to optimize the construction time of the Customizable Object Instance. For example, the game may have more graphic resources available because, instead of being inside a level, you are in a smaller lobby scene. This means that you can afford to temporarily use more memory for your character. For each individual State, Mutable gives you these three optimization options in addition to the Runtime Parameters:

* **Do not Compress Runtime Textures**: Avoids texture compression for textures that may change in this State.
* **Build Only First LOD**: Generates only the LOD 0 of the object.
* **Forced Parameter Values**: Lists the Enumeration Parameters that are modified when the state is selected. For example, allows hiding of jackets when editing the shirt underneath. The first field represents the Enumeration Parameter name, while the second field is the forced value.

[![Mutable Optimization options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/084b59e0-3d51-4073-aa25-a3dc48177bb9/mutable-states-optimization.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/084b59e0-3d51-4073-aa25-a3dc48177bb9/mutable-states-optimization.png)

Mutable Optimization options

States are created at any Base Object Node. If no state is created, a default State with no optimized parameters and optimization options are automatically created. Also a Child Object can contain its own States. A State defined at a Child Object functions identically to a state defined at the Base Object.

Ideally, a game should have an in-game state with no optimized parameters, and several customization states to create and update objects in the different in-game customization scenarios.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Runtime Parameters](/documentation/en-us/unreal-engine/using-customizable-states-in-mutable-with-unreal-engine?application_version=5.7#runtimeparameters)
* [Optimization Options](/documentation/en-us/unreal-engine/using-customizable-states-in-mutable-with-unreal-engine?application_version=5.7#optimizationoptions)
