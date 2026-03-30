<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/structs-in-unreal-engine?application_version=5.7 -->

# Structs

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
6. [Unreal Engine Reflection System](/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine "Unreal Engine Reflection System")
7. Structs

# Structs

Reference to creating and implementing structs for gameplay classes.

![Structs](https://dev.epicgames.com/community/api/documentation/image/828d7347-75d2-4ff2-856b-7b81731a645e?resizing_type=fill&width=1920&height=335)

 On this page

A **struct** is a data structure that helps you organize and manipulate its member properties. Unreal Engine's reflection system recognizes structs as a `UStruct`, but they are not part of the [UObject](https://dev.epicgames.com/documentation/en-us/unreal-engine/objects-in-unreal-engine) ecosystem, and cannot be used inside of [UClasses](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/UClass?application_version=5.5).

* A `UStruct` is faster to create than a `UObject` with the same data layout.
* UStruct supports [UProperty](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties), but are not managed by the Garbage Collection system and cannot provide the functionality of a [UFunction](https://dev.epicgames.com/documentation/en-us/unreal-engine/ufunctions-in-unreal-engine).

## Implement a UStruct

To make a struct into a `UStruct`, follow the steps below:

1. Open the **header (.h)** file where you want to define your struct.
2. To define your C++ struct, put the `USTRUCT` macro above the struct's definition.
3. Include the `GENERATED_BODY()` macro as the first line of the definition.

The result should look like the following example:

C++

USTRUCT([Specifier, Specifier, ...])
struct FStructName
{
GENERATED\_BODY()
};

Copy full snippet(5 lines long)

You can tag the struct's member variables with `UPROPERTY` to make them visible to the Unreal Reflection System and Blueprint Scripting. See the list of [UProperty Specifiers](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties) to learn how the property can behave in various [Modules](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules) of the Engine and Editor.

## Struct Specifiers

**Struct Specifiers** provide metadata that controls how your structs behave with various aspects of the Engine and Editor.

| Struct Specifier | Effect |
| --- | --- |
| `Atomic` | Indicates that this struct should always be serialized as a single unit. No auto-generated code will be created for this class. The header is only provided to parse metadata from. |
| `BlueprintType` | Exposes this struct as a type that can be used for variables in Blueprints. |
| `NoExport` | No auto-generated code will be created for this class. The header is only provided for parsing metadata. |

## Best Practices & Tips

Below are some helpful tips to remember when you use `UStruct`:

1. `UStruct` can use Unreal Engine's [smart pointer](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-pointers-in-unreal-engine) and garbage collection systems to prevent garbage collection from removing`UObjects`.
2. Structs are best used for simple data types. For more complicated interactions in your project, you might want to make a `UObject` or `AActor` subclass instead.
3. `UStructs` **ARE NOT** considered for replication. However, `UProperty` variables **ARE** considered for replication.
4. Unreal Engine can automatically create Make and Break functions for Structs.

   1. Make appears for any `UStruct` with the `BlueprintType` tag.
   2. Break appears if you have at least one `BlueprintReadOnly` or `BlueprintReadWrite` property in the UStruct.
   3. The pure node that Break creates provides one output pin for each property tagged as `BlueprintReadOnly` or `BlueprintReadWrite`.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [ustruct](https://dev.epicgames.com/community/search?query=ustruct)
* [structs](https://dev.epicgames.com/community/search?query=structs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Implement a UStruct](/documentation/en-us/unreal-engine/structs-in-unreal-engine?application_version=5.7#implement-a-u-struct)
* [Struct Specifiers](/documentation/en-us/unreal-engine/structs-in-unreal-engine?application_version=5.7#struct-specifiers)
* [Best Practices & Tips](/documentation/en-us/unreal-engine/structs-in-unreal-engine?application_version=5.7#best-practices-tips)
