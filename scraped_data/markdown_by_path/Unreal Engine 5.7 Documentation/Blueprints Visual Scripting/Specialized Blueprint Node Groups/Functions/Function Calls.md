<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/function-calls-in-unreal-engine?application_version=5.7 -->

# Function Calls

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
7. [Functions](/documentation/en-us/unreal-engine/functions-in-unreal-engine "Functions")
8. Function Calls

# Function Calls

Nodes that execute both code-defined and user-defined functions of a target Actor or Object.

![Function Calls](https://dev.epicgames.com/community/api/documentation/image/80ba5a58-05af-40c5-8a04-a43fdc08508a?resizing_type=fill&width=1920&height=335)

 On this page

**Function Calls** are actions that can be formed within Blueprints that correspond to functions belonging
to a targeted Actor or Object. In the case of Level Blueprints, the associated Actor in many cases is the
Level Blueprint itself. Function Calls are displayed as boxes with titles that show the name of the function.
Different types of function calls have different color titles.

## Self

**Self Function Calls** are functions that belong to the Blueprint itself, by way of being declared in
the class the Blueprint derives from or a parent class.

## Other

**Other Function Calls** are functions that belong to other Objects or Actors besides the Blueprint. For example,
the Blueprint might have a StaticMeshComponent that can have its mesh changed via a SetStaticMesh function call.
Since this function belongs to the StaticMeshComponent and not the Blueprint, it is an Other Function Call.

## Pure

**Pure Function Calls** are special actions that can be performed that do not directly affect the world
or the Objects in it. These are generally things like functions that output a property value, or mathematical
operations such as adding, subtracting, multiplying, dividing, etc. two values, the results of which have no impact on anything.
It is the assigning or use of the result that generates an effect on the world.

|  |  |
| --- | --- |
| Pure Function Call Node | Math Pure Function Call Node |
| Standard | Compact |

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Self](/documentation/en-us/unreal-engine/function-calls-in-unreal-engine?application_version=5.7#self)
* [Other](/documentation/en-us/unreal-engine/function-calls-in-unreal-engine?application_version=5.7#other)
* [Pure](/documentation/en-us/unreal-engine/function-calls-in-unreal-engine?application_version=5.7#pure)
