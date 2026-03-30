<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-cpp-in-unreal-engine?application_version=5.7 -->

# Gameplay Architecture

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
6. Gameplay Architecture

# Gameplay Architecture

Reference for creating and implementing gameplay classes.

![Gameplay Architecture](https://dev.epicgames.com/community/api/documentation/image/025a61a2-0107-48bb-963f-1b84aeba67b4?resizing_type=fill&width=1920&height=335)

 On this page

When programming gameplay elements using C++ code, each module can contain many C++ classes.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7906927d-5e59-459b-8846-d7a0b69723de/projectmoduleclassorg.png)

Each class defines a template for a new Actor or Object. Within the class header file, the class and any class [functions](/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine) and [properties](/documentation/en-us/unreal-engine/unreal-engine-uproperties)
are declared. Classes can also contain [structs](/documentation/404), data structures that help with organization and manipulation of related properties. Structures can also be defined on their own.
[Interfaces](/documentation/404) allow additional gameplay behavior to be implemented by different classes.

When programming with Unreal Engine, it is possible to have standard C++ classes, functions, and variables. These can be defined using standard C++ syntax. However, `UCLASS()`, `UFUNCTION()`, and
`UPROPERTY()` macros can be used to make Unreal Engine aware of the new classes, functions, and variables. For instance, a variable with a declaration prefaced by a `UPROPERTY()` macro can
be garbage collected by the engine, and can be displayed and edited within Unreal Editor. There are also `UINTERFACE()` and `USTRUCT()` macros, and keywords for each macro that can be used
to specify the behavior of the [class](/documentation/en-us/unreal-engine/class-specifiers), [function](/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers), [property](/documentation/en-us/unreal-engine/unreal-engine-uproperties#propertyspecifiers),
interface, or struct within Unreal Engine and Unreal Editor.

In addition to the above macros, there is a UPARAM() macro that is primarily used when exposing C++ code to Blueprints. To see examples of UPARAM() being used, see the [Exposing Gameplay Elements to Blueprints](/documentation/en-us/unreal-engine/exposing-gameplay-elements-to-blueprints-visual-scripting-in-unreal-engine) documentation.

## Gameplay Programming Reference Directory

[![Gameplay Classes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0f2eea1-bd5b-4b39-b46c-0e1ca5b62eec/placeholder_topic.png)

Gameplay Classes

Reference for creating and implementing gameplay classes.](/documentation/en-us/unreal-engine/gameplay-classes-in-unreal-engine)
%programming-and-scripting/programming-language-implementation/unreal-engine-reflection-system/Functions:topic%
%programming-and-scripting/programming-language-implementation/unreal-engine-reflection-system/Properties:topic%
%programming-and-scripting/programming-language-implementation/unreal-engine-reflection-system/Structs:topic%
%programming-and-scripting/programming-language-implementation/unreal-engine-reflection-system/Interfaces:topic%

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [framework](https://dev.epicgames.com/community/search?query=framework)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Gameplay Programming Reference Directory](/documentation/en-us/unreal-engine/programming-with-cpp-in-unreal-engine?application_version=5.7#gameplayprogrammingreferencedirectory)
