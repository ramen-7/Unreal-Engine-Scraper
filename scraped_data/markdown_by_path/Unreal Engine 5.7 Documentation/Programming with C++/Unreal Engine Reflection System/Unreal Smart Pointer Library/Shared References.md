<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/shared-references-in-unreal-engine?application_version=5.7 -->

# Shared References

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
7. [Unreal Smart Pointer Library](/documentation/en-us/unreal-engine/smart-pointers-in-unreal-engine "Unreal Smart Pointer Library")
8. Shared References

# Shared References

Smart pointer type that cannot be uninitialized or assigned null.

![Shared References](https://dev.epicgames.com/community/api/documentation/image/b74837e6-fb88-490a-9d09-5ca9f228230e?resizing_type=fill&width=1920&height=335)

 On this page

A **Shared Reference** is a strong, non-nullable **Smart Pointer** for data objects outside of the Engine's `UObject` system. This means you cannot reset a Shared Reference, assign a null object to it, or create an empty one. Because of this, Shared References always contain a valid object, and do not even have an `IsValid` method. When choosing between Shared References and **[Shared Pointers](/documentation/en-us/unreal-engine/shared-pointers-in-unreal-engine)**, Shared References are the preferred option unless you need an empty or nullable object. If you need potentially-empty or nullable references, you should use Shared Pointers instead.

Unlike a standard C++ reference, a Shared Reference can be reassigned to another object after creation.

## Declaration and Initialization

Shared References are non-nullable, so initialization requires a data object. Attempting to create a Shared Reference without a valid object will not compile, and attempting to initialize a Shared Reference to a null pointer variable.

```
	// Create a shared reference to a new node
	TSharedRef<FMyObjectType> NewReference = MakeShared<FMyObjectType>();

Copy full snippet
```

Attempting to create a Shared Reference without a valid object will not compile:

```
	// Neither of these will compile:
	TSharedRef<FMyObjectType> UnassignedReference;
	TSharedRef<FMyObjectType> NullAssignedReference = nullptr;
	// This will compile, but will assert if NullObject is actually null.
	TSharedRef<FMyObjectType> NullAssignedReference = NullObject;

Copy full snippet
```

### Converting Between Shared Pointers and Shared References

Converting between Shared Pointers and Shared References is a common practice. Shared References implicitly convert to Shared Pointers, and provide the additional guarantee that the new Shared Pointer will reference a valid object. Conversion is handled by the normal syntax:

```
	TSharedPtr<FMyObjectType> MySharedPointer = MySharedReference;

Copy full snippet
```

You can create a Shared Reference from a Shared Pointer with the `Shared Pointer` function, `ToSharedRef`, as long as the Shared Pointer references a non-null object. Attempting to create a Shared Reference from a null Shared Pointer will cause the program to assert.

```
	// Ensure your shared pointer is valid before dereferencing to avoid a potential assertion.
	If (MySharedPointer.IsValid())
	{
		MySharedReference = MySharedPointer.ToSharedRef();
	}

Copy full snippet
```

## Comparison

You can test Shared References against each other for equality. In this context, equality means referencing the same object.

```
	TSharedRef<FMyObjectType> ReferenceA, ReferenceB;
	if (ReferenceA == ReferenceB)
	{
		// ...
	}
Copy full snippet
```

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Declaration and Initialization](/documentation/en-us/unreal-engine/shared-references-in-unreal-engine?application_version=5.7#declarationandinitialization)
* [Converting Between Shared Pointers and Shared References](/documentation/en-us/unreal-engine/shared-references-in-unreal-engine?application_version=5.7#convertingbetweensharedpointersandsharedreferences)
* [Comparison](/documentation/en-us/unreal-engine/shared-references-in-unreal-engine?application_version=5.7#comparison)
