<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dynamic-delegates-in-unreal-engine?application_version=5.7 -->

# Dynamic Delegates

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
6. [Delegates](/documentation/en-us/unreal-engine/delegates-and-lambda-functions-in-unreal-engine "Delegates")
7. Dynamic Delegates

# Dynamic Delegates

Delegates that can be serialized and support reflection.

![Dynamic Delegates](https://dev.epicgames.com/community/api/documentation/image/1be13f25-d87f-4e3c-aa33-c7ab8f9e78bf?resizing_type=fill&width=1920&height=335)

 On this page

Dynamic delegates can be serialized, their functions can be found by name, and they are slower than regular delegates.

## Declaring Dynamic Delegates

Dynamic delegates are declared in the same manner as you [declare standard delegates](/documentation/en-us/unreal-engine/delegates-and-lambda-functions-in-unreal-engine) except they use the macro variations specific to dynamic delegates.

| Declaration Macro | Description |
| --- | --- |
| `DECLARE_DYNAMIC_DELEGATE[_RetVal, ...]\( DelegateName \)` | Creates a dynamic delegate. |
| `DECLARE_DYNAMIC_MULTICAST_DELEGATE[_RetVal, ...]\( DelegateName \)` | Creates a dynamic multi-cast delegate. |

## Dynamic Delegate Binding

| Helper Macro | Description |
| --- | --- |
| `BindDynamic( UserObject, FuncName )` | Helper macro for calling BindDynamic() on dynamic delegates. Automatically generates the function name string. |
| `AddDynamic( UserObject, FuncName )` | Helper macro for calling AddDynamic() on dynamic multi-cast delegates. Automatically generates the function name string. |
| `RemoveDynamic( UserObject, FuncName )` | Helper macro for calling RemoveDynamic() on dynamic multi-cast delegates. Automatically generates the function name string. |

## Executing Dynamic Delegates

The function bound to a delegate is executed by calling the delegate's `Execute()` function. You must check if delegates are "bound" before executing them. This is to make the
code more safe as there may be cases where delegates have return values and output parameters that are uninitialized and subsequently accessed. Executing an unbound delegate
could actually scribble over memory in some instances. You can call `IsBound()` to check if the delegate is safe to execute. Also, for delegates that have no return value,
you can call `ExecuteIfBound()`, but be wary of output parameters that may be left uninitialized.

| Execution Functions | Description |
| --- | --- |
| `Execute` | Executes a delegate without checking its bindings |
| `ExecuteIfBound` | Checks that a delegate is bound, and if so, calls Execute |
| `IsBound` | Checks whether or not a delegate is bound, often before code that includes an `Execute` call |

See [Multi-cast Delegates](/documentation/en-us/unreal-engine/multicast-delegates-in-unreal-engine) for details on executing multi-cast delegates.

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Declaring Dynamic Delegates](/documentation/en-us/unreal-engine/dynamic-delegates-in-unreal-engine?application_version=5.7#declaringdynamicdelegates)
* [Dynamic Delegate Binding](/documentation/en-us/unreal-engine/dynamic-delegates-in-unreal-engine?application_version=5.7#dynamicdelegatebinding)
* [Executing Dynamic Delegates](/documentation/en-us/unreal-engine/dynamic-delegates-in-unreal-engine?application_version=5.7#executingdynamicdelegates)
