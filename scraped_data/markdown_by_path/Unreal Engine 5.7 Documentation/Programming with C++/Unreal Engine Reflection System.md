<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine?application_version=5.7 -->

# Unreal Engine Reflection System

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
5. [Programming with C++](/documentation/en-us/unreal-engine/programming-with-cplusplus-in-unreal-engine "Programming with C++")
6. Unreal Engine Reflection System

# Unreal Engine Reflection System

Information for programmers developing Objects to be used with Unreal Engine.

![Unreal Engine Reflection System](https://dev.epicgames.com/community/api/documentation/image/ef0e2911-acc2-44a4-b479-a0ef52d92f1c?resizing_type=fill&width=1920&height=335)

 On this page

The **Unreal Engine Reflection System** encapsulates your classes with various macros that provide engine and editor functionality. When programming with **Unreal Engine**(**UE**), it is possible to have standard C++ classes, functions, and variables.

* The base class for objects in Unreal is [UObject](/documentation/en-us/unreal-engine/objects-in-unreal-engine). Each class defines a template for a new [Actor](/documentation/en-us/unreal-engine/actors-in-unreal-engine) or Object.
* You can use the `UCLASS` macro to tag classes derived from `UObject` so that the [UObject handling system](/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine) is aware of them.
* [TSubclassOf](/documentation/en-us/unreal-engine/typed-object-pointer-properties-in-unreal-engine) is a template class that provides `UClass` type safety. It is useful for assigning classes that derive from a specific type. For example, you may expose this variable to Blueprint where a designer can assign which weapon class is spawned for a Player Character.
* Classes can contain [structs](/documentation/404). Structs are data structures that help with the organization and manipulation of their related member properties. Structs can be defined on their own using the `USTRUCT()` macro.
* The [Unreal Smart Pointer Library](/documentation/en-us/unreal-engine/smart-pointers-in-unreal-engine) is a custom implementation of C++11 smart pointers designed to ease the burden of memory allocation and tracking. This implementation includes the industry standard [Shared Pointers](/documentation/en-us/unreal-engine/shared-pointers-in-unreal-engine), [Weak Pointers](/documentation/en-us/unreal-engine/weak-pointers-in-unreal-engine), **Unique Pointers**, and [Shared References](/documentation/en-us/unreal-engine/shared-references-in-unreal-engine) which act like non-nullable Shared Pointers.
* [Interfaces](/documentation/404) provide functions and additional gameplay behavior you can implement in multiple or different classes. Your player character can interact with a variety of Actors in the world. Each of these interactions can cause a different reaction to an event.
* [Metadata Specifiers](/documentation/en-us/unreal-engine/metadata-specifiers-in-unreal-engine) control how classes, interfaces, structs, enums, functions, or properties interact with various aspects of the engine and editor. Each type of data structure or member has its own list of Metadata Specifiers.
* [UFUNCTION](/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine), and [UPROPERTY](/documentation/en-us/unreal-engine/unreal-engine-uproperties) macros make UE aware of new classes, functions, and variables. These macros are garbage collected by the engine. When specifying macros, you can edit and display them within the Unreal Editor.

## Section Directory

[![Objects](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d3299446-248b-43e5-b811-5ab559aba486/placeholder_topic.png)

Objects

Explanations of the basic gameplay elements, Actors and Objects.](/documentation/en-us/unreal-engine/objects-in-unreal-engine)
[![TSubclassOf](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cae8bad5-c8f9-4ae8-bd71-0c3952880511/placeholder_topic.png)

TSubclassOf

Using the TSubclassOf template class to provide type safety.](/documentation/en-us/unreal-engine/typed-object-pointer-properties-in-unreal-engine)
[![Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53db5803-08a3-4ae8-8094-54d42dae7ce4/placeholder_topic.png)

Properties

Reference for creating and implementing properties for gameplay classes.](/documentation/en-us/unreal-engine/unreal-engine-uproperties)
[![Metadata Specifiers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e2ce810-b8d3-47e7-b850-6bed2c60fd25/placeholder_topic.png)

Metadata Specifiers

Metadata keywords used when declaring UClasses, UFunctions, UProperties, UEnums, and UInterfaces to specify how they behave with various aspects of Unreal Engine and the editor](/documentation/en-us/unreal-engine/metadata-specifiers-in-unreal-engine)
[![UFunctions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e09e55b-5f50-45ff-ba43-664c3e9ef323/ufunctionherotopic.png)

UFunctions

Overview for creating and implementing functions for gameplay Classes](/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine)
[![Unreal Smart Pointer Library](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da914dc7-5353-4d7d-a948-3e03990bf8fe/placeholder_topic.png)

Unreal Smart Pointer Library

Custom implementation of shared pointers, including weak pointers and non-nullable shared references.](/documentation/en-us/unreal-engine/smart-pointers-in-unreal-engine)

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Section Directory](/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine?application_version=5.7#sectiondirectory)
