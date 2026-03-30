<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7 -->

# TMap

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
6. [Containers in Unreal Engine](/documentation/en-us/unreal-engine/containers-in-unreal-engine "Containers in Unreal Engine")
7. TMap

# TMap

TMaps are defined by two types, a key type and a value type, which are stored as associated pairs in the map.

![TMap](https://dev.epicgames.com/community/api/documentation/image/b5438314-fb9b-4641-bf1a-cce527ab4bfb?resizing_type=fill&width=1920&height=335)

 On this page

After [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/array-containers-in-unreal-engine), the most commonly used container in **Unreal Engine** is [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap?application_version=5.5). **TMap** is similar to [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/set-containers-in-unreal-engine) in that its structure is based on hashing keys. However, unlike [TSet](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSet?application_version=5.5), TMap stores data as key-value pairs (`TPair<KeyType, ValueType>`), using keys only for storage and retrieval.

## Types of Maps in Unreal Engine

There are two types of map in Unreal Engine:

* [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap?application_version=5.5)
* [TMultiMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMultiMap?application_version=5.5)

### Overview of TMap

* In a TMap, key-value pairs are treated as the element type of the map as if each pair were an individual object. In this document, element means a key-value pair, while individual components are referred to as the element's key or the element's value.
* The element type is a `TPair<KeyType, ElementType>`, though it should be rare to need to refer to the TPair type directly.
* TMap keys are unique.
* Similar to TArray, TMap is a homogeneous container, meaning that all of its elements are strictly the same type.
* TMap is a value type, and supports the usual copy, assignment, and destructor operations, as well as strong ownership of its elements, which are destroyed when the map is destroyed. The key and value must also be value types.
* TMap is a hashing container, which means that the key type must support the [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5) function and provide an `operator==` for comparing keys for equality

TMap and TMultimap (like many Unreal Engine containers) assume that the element type is trivially relocatable, meaning that elements can safely be moved from one location in memory to another by directly copying raw bytes.

### Overview of TMultiMap

* Supports storing multiple, identical keys.
* When adding a new key-value pair to a TMap with a key that matches an existing pair, the new pair will replace the old one.
* In a TMultiMap, the container stores both the new pair and the old.

TMap can take an optional allocator to control the memory allocation behavior. However, unlike TArray, these are set allocators rather than the standard Unreal allocators like [FHeapAllocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/FHeapAllocator?application_version=5.5) and [TInlineAllocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/TraceLog/TInlineAllocator?application_version=5.5). **Set Allocators**, ([TSetAllocator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSetAllocator?application_version=5.5)), define how many hash buckets the map should use and which standard UE allocators should be used for hash and element storage.

The final TMap template parameter is `KeyFuncs`, which tells the map how to retrieve the key from the element type, how to compare two keys for equality, and how to hash the key. These have defaults that return a reference to the key, then use `operator==` for equality, and call the non-member [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5) function for hashing. If your key type supports these functions, you can use it as a map key without supplying a custom `KeyFuncs`.

Unlike TArray, the relative order of TMap elements in memory is not reliable or stable, and iterating over the elements is likely to return them in a different order from the order in which they were added. Elements are unlikely to be laid out contiguously in memory.

The base data structure of a map is a sparse array, which is an array that efficiently supports gaps between its elements. As elements are removed from the map, gaps in the sparse array will appear. Adding new elements to the array can then fill these gaps. However, even though TMap doesn't shuffle elements to fill gaps, pointers to map elements may still be invalidated, as the entire storage can be reallocated when it is full and new elements are added.

## Create and Fill a Map

The following code creates a **TMap**:

C++

```
TMap<int32, FString> FruitMap;
```

TMap<int32, FString> FruitMap;

Copy full snippet(1 line long)

`FruitMap` is now an empty TMap of strings that are identified by integer keys. We have specified neither an allocator nor a `KeyFuncs`, so the map performs standard heap allocation and compares the key of type `int32` using `operator==` and hashes the key using [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5). No memory has been allocated at this point.

### Add

The standard way to populate a map is to call [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Add?application_version=5.5) with a key and a value:

C++

```
|  |  |
| --- | --- |
|  | FruitMap.Add(5, TEXT("Banana")); |
|  | FruitMap.Add(2, TEXT("Grapefruit")); |
|  | FruitMap.Add(7, TEXT("Pineapple")); |
|  | // FruitMap == [ |
|  | // 	{ Key: 5, Value: "Banana"     }, |
|  | // 	{ Key: 2, Value: "Grapefruit" }, |
|  | // 	{ Key: 7, Value: "Pineapple"  } |
|  | // ] |
```

FruitMap.Add(5, TEXT("Banana"));
FruitMap.Add(2, TEXT("Grapefruit"));
FruitMap.Add(7, TEXT("Pineapple"));
// FruitMap == [
// { Key: 5, Value: "Banana" },
// { Key: 2, Value: "Grapefruit" },
// { Key: 7, Value: "Pineapple" }
// ]

Copy full snippet(8 lines long)

While the elements are listed here in the order of insertion, there is no guarantee of their actual order in memory. For a new map, they are likely to be in order of insertion, but as more insertions and removals happen, it becomes increasingly unlikely that new elements will appear at the end.

This is not a `TMultiMap`; therefore, the keys are guaranteed to be unique. The following is the result of attempting to add a duplicate key:

C++

```
|  |  |
| --- | --- |
|  | FruitMap.Add(2, TEXT("Pear")); |
|  | // FruitMap == [ |
|  | // 	{ Key: 5, Value: "Banana"    }, |
|  | // 	{ Key: 2, Value: "Pear"      }, |
|  | // 	{ Key: 7, Value: "Pineapple" } |
|  | // ] |
```

FruitMap.Add(2, TEXT("Pear"));
// FruitMap == [
// { Key: 5, Value: "Banana" },
// { Key: 2, Value: "Pear" },
// { Key: 7, Value: "Pineapple" }
// ]

Copy full snippet(6 lines long)

The map still contains three elements, but the previous Grapefruit value with a key of 2 has been replaced with Pear.

The [Add](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Add?application_version=5.5) function can accept a key without a value. When this overloaded `Add` is called, the value will be default-constructed:

C++

```
|  |  |
| --- | --- |
|  | FruitMap.Add(4); |
|  | // FruitMap == [ |
|  | // 	{ Key: 5, Value: "Banana"    }, |
|  | // 	{ Key: 2, Value: "Pear"      }, |
|  | // 	{ Key: 7, Value: "Pineapple" }, |
|  | // 	{ Key: 4, Value: ""          } |
|  | // ] |
```

FruitMap.Add(4);
// FruitMap == [
// { Key: 5, Value: "Banana" },
// { Key: 2, Value: "Pear" },
// { Key: 7, Value: "Pineapple" },
// { Key: 4, Value: "" }
// ]

Copy full snippet(7 lines long)

### Emplace

Like TArray, we can use [Emplace](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Emplace?application_version=5.5) instead of `Add` to avoid the creation of temporaries when inserting into the map:

C++

```
|  |  |
| --- | --- |
|  | FruitMap.Emplace(3, TEXT("Orange")); |
|  | // FruitMap == [ |
|  | // 	{ Key: 5, Value: "Banana"    }, |
|  | // 	{ Key: 2, Value: "Pear"      }, |
|  | // 	{ Key: 7, Value: "Pineapple" }, |
|  | // 	{ Key: 4, Value: ""          }, |
|  | // 	{ Key: 3, Value: "Orange"    } |
|  | // ] |
```

FruitMap.Emplace(3, TEXT("Orange"));
// FruitMap == [
// { Key: 5, Value: "Banana" },
// { Key: 2, Value: "Pear" },
// { Key: 7, Value: "Pineapple" },
// { Key: 4, Value: "" },
// { Key: 3, Value: "Orange" }
// ]

Copy full snippet(8 lines long)

Here, the key and value are passed directly to their respective type constructors. While this isn't meaningful for the `int32` key, it does avoid the creation of a temporary `FString` for the value. Unlike TArray, it's only possible to emplace elements into a map with single-argument constructors.

### Append

You can merge two maps with the [Append](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap/Append?application_version=5.5) function, which moves all elements from the argument map into the calling object map:

C++

```
TMap<int32, FString> FruitMap2;
FruitMap2.Emplace(4, TEXT("Kiwi"));
FruitMap2.Emplace(9, TEXT("Melon"));
FruitMap2.Emplace(5, TEXT("Mango"));
FruitMap.Append(FruitMap2);
// FruitMap == [
// 	{ Key: 5, Value: "Mango"     },
// 	{ Key: 2, Value: "Pear"      },
// 	{ Key: 7, Value: "Pineapple" },
// 	{ Key: 4, Value: "Kiwi"      },
```

Expand code  Copy full snippet(14 lines long)

In the above example, the resulting map is equivalent to using `Add` or `Emplace` to add each element of `FruitMap2` individually, emptying `FruitMap2` when the process is complete. This means that any element from `FruitMap2` that shares its key with an element already in `FruitMap` replaces that element.

If you mark the TMap with the [UPROPERTY](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties) macro and one of the "editable" keywords (`EditAnywhere`, `EditDefaultsOnly`, or `EditInstanceOnly`), you can [add and edit elements in the Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine).

C++

```
|  |  |
| --- | --- |
|  | UPROPERTY(EditAnywhere, Category = MapsAndSets) |
|  | TMap<int32, FString> FruitMap; |
```

UPROPERTY(EditAnywhere, Category = MapsAndSets)
TMap<int32, FString> FruitMap;

Copy full snippet(2 lines long)

## Iterate

Iteration over TMaps is similar to TArrays. You can use the C++ ranged-for feature, remembering that the element type is a TPair:

C++

```
for (auto& Elem : FruitMap)
{
	FPlatformMisc::LocalPrint(
		*FString::Printf(
			TEXT("(%d, \"%s\")\n"),
			Elem.Key,
			*Elem.Value
		)
	);
}
```

Expand code  Copy full snippet(18 lines long)

You can create iterators with the [CreateIterator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/CreateIterator?application_version=5.5) and [CreateConstIterator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/CreateConstIterator?application_version=5.5) functions.

| Function | Description |
| --- | --- |
| `CreateIterator` | Return an iterator with read-write access. |
| `CreateConstIterator` | Returns a read-only iterator. |

In either case, you can use the `Key` and `Value` functions of these iterators to examine the elements. Printing the contents of our example `FruitMap` using iterators would look like this:

C++

```
|  |  |
| --- | --- |
|  | for (auto It = FruitMap.CreateConstIterator(); It; ++It) |
|  | { |
|  | FPlatformMisc::LocalPrint( |
|  | *FString::Printf( |
|  | TEXT("(%d, \"%s\")\n"), |
|  | It.Key(),   // same as It->Key |
|  | *It.Value() // same as *It->Value |
|  | ) |
|  | ); |
|  | } |
```

for (auto It = FruitMap.CreateConstIterator(); It; ++It)
{
FPlatformMisc::LocalPrint(
\*FString::Printf(
TEXT("(%d, \"%s\")\n"),
It.Key(), // same as It->Key
\*It.Value() // same as \*It->Value
)
);
}

Copy full snippet(10 lines long)

## Get Value

If you know that your map contains a certain key, you can look up the corresponding value with `operator[]`, using the key as the index. Doing this with a non-const map returns a non-const reference, while a const map returns a const reference.

You should always check that the map contains the key before using `operator[]`. If the map does not contain the key, it will assert.

C++

```
|  |  |
| --- | --- |
|  | FString Val7 = FruitMap[7]; |
|  | // Val7 == "Pineapple" |
|  | FString Val8 = FruitMap[8]; |
|  | // Assert! |
```

FString Val7 = FruitMap[7];
// Val7 == "Pineapple"
FString Val8 = FruitMap[8];
// Assert!

Copy full snippet(4 lines long)

## Query

To determine how many elements are currently in a TMap, call the [Num](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Num?application_version=5.5) function:

C++

```
|  |  |
| --- | --- |
|  | int32 Count = FruitMap.Num(); |
|  | // Count == 6 |
```

int32 Count = FruitMap.Num();
// Count == 6

Copy full snippet(2 lines long)

To determine whether or not a map contains a specific key, call the `Contains` function:

C++

```
|  |  |
| --- | --- |
|  | bool bHas7 = FruitMap.Contains(7); |
|  | bool bHas8 = FruitMap.Contains(8); |
|  | // bHas7 == true |
|  | // bHas8 == false |
```

bool bHas7 = FruitMap.Contains(7);
bool bHas8 = FruitMap.Contains(8);
// bHas7 == true
// bHas8 == false

Copy full snippet(4 lines long)

If you are uncertain whether or not your map contains a key, you could check using the [Contains](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Contains?application_version=5.5) function, and then use `operator[]`. However, this is suboptimal, since a successful retrieval involves two lookups on the same key.

The [Find](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Find?application_version=5.5) function combines these behaviors with a single lookup. `Find` returns a pointer to the value of the element if the map contains the key, or a null pointer if it does not. Calling `Find` on a const map returns a const pointer.

C++

```
|  |  |
| --- | --- |
|  | FString* Ptr7 = FruitMap.Find(7); |
|  | FString* Ptr8 = FruitMap.Find(8); |
|  | // *Ptr7 == "Pineapple" |
|  | //  Ptr8 == nullptr |
```

FString\* Ptr7 = FruitMap.Find(7);
FString\* Ptr8 = FruitMap.Find(8);
// \*Ptr7 == "Pineapple"
// Ptr8 == nullptr

Copy full snippet(4 lines long)

Alternatively, to ensure that you receive a valid result from your query, you can use [FindOrAdd](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/FindOrAdd?application_version=5.5) or [FindRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/FindRef?application_version=5.5):

| Function | Description |
| --- | --- |
| `FindOrAdd` | Return a reference to the value associated with the key you provide. If the key is not in the map, `FindOrAdd` returns a newly-created element, with your key and the default-constructed value, that it will add to the map.  `FindOrAdd` is only available for non-const maps. |
| `FindRef` | Despite its name, returns a copy of the value associated with your key, or a default-constructed value if your key is not found in the map. `FindRef` does not create a new element, and thus is available for use with both const and non-const maps. |

Because `FindOrAdd` and `FindRef` succeed even when the key isn't found in the map, you can safely call them without the usual safety procedures like checking `Contains` in advance, or null-checking the return value.

C++

```
FString& Ref7 = FruitMap.FindOrAdd(7);
// Ref7     == "Pineapple"
// FruitMap == [
// 	{ Key: 5, Value: "Mango"     },
// 	{ Key: 2, Value: "Pear"      },
// 	{ Key: 7, Value: "Pineapple" },
// 	{ Key: 4, Value: "Kiwi"      },
// 	{ Key: 3, Value: "Orange"    },
// 	{ Key: 9, Value: "Melon"     }
// ]
```

Expand code  Copy full snippet(36 lines long)

Because `FindOrAdd` can add new entries to the map, as it does when initializing `Ref8` in our example, previously-obtained pointers or references could become invalid. This is a result of the addition operation allocating memory and moving existing data if the map's backend storage needs to expand to contain the new element. In the example above, `Ref7` may be invalidated after `Ref8` after the call to `FindOrAdd(8)`.

The [FindKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/FindKey?application_version=5.5) function performs a reverse lookup, meaning that a supplied value is matched to a key, and returns a pointer to the first key that's paired to the provided value. Searching for a value that isn't present in the map returns a null pointer.

C++

```
|  |  |
| --- | --- |
|  | const int32* KeyMangoPtr   = FruitMap.FindKey(TEXT("Mango")); |
|  | const int32* KeyKumquatPtr = FruitMap.FindKey(TEXT("Kumquat")); |
|  | // *KeyMangoPtr   == 5 |
|  | //  KeyKumquatPtr == nullptr |
```

const int32\* KeyMangoPtr = FruitMap.FindKey(TEXT("Mango"));
const int32\* KeyKumquatPtr = FruitMap.FindKey(TEXT("Kumquat"));
// \*KeyMangoPtr == 5
// KeyKumquatPtr == nullptr

Copy full snippet(4 lines long)

Lookups by value are slower (linear time) than lookups by key. This is because the map is hashed by key, not by value. In addition, if a map has multiple keys with the same value, `FindKey` may return any of them.

The [GenerateKeyArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/GenerateKeyArray?application_version=5.5) and [GenerateValueArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/GenerateValueArray?application_version=5.5) functions populate a [TArray](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/TraceLog/TArray?application_version=5.5) with a copy of all the keys and values respectively. In both cases, the array being passed is emptied before population, so the resulting number of elements will always equal the number of elements in the map.

C++

```
|  |  |
| --- | --- |
|  | TArray<int32>   FruitKeys; |
|  | TArray<FString> FruitValues; |
|  | FruitKeys.Add(999); |
|  | FruitKeys.Add(123); |
|  | FruitMap.GenerateKeyArray  (FruitKeys); |
|  | FruitMap.GenerateValueArray(FruitValues); |
|  | // FruitKeys   == [ 5,2,7,4,3,9,8 ] |
|  | // FruitValues == [ "Mango","Pear","Pineapple","Kiwi","Orange", |
|  | //                  "Melon","" ] |
```

TArray<int32> FruitKeys;
TArray<FString> FruitValues;
FruitKeys.Add(999);
FruitKeys.Add(123);
FruitMap.GenerateKeyArray (FruitKeys);
FruitMap.GenerateValueArray(FruitValues);
// FruitKeys == [ 5,2,7,4,3,9,8 ]
// FruitValues == [ "Mango","Pear","Pineapple","Kiwi","Orange",
// "Melon","" ]

Copy full snippet(9 lines long)

## Remove

You can remove elements from a map using the [Remove](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Remove?application_version=5.5) function and providing the key of the element to remove. The return value is the number of elements that were removed, and can be zero if the map didn't contain any elements matching the key.

C++

```
|  |  |
| --- | --- |
|  | FruitMap.Remove(8); |
|  | // FruitMap == [ |
|  | // 	{ Key: 5, Value: "Mango"     }, |
|  | // 	{ Key: 2, Value: "Pear"      }, |
|  | // 	{ Key: 7, Value: "Pineapple" }, |
|  | // 	{ Key: 4, Value: "Kiwi"      }, |
|  | // 	{ Key: 3, Value: "Orange"    }, |
|  | // 	{ Key: 9, Value: "Melon"     } |
|  | // ] |
```

FruitMap.Remove(8);
// FruitMap == [
// { Key: 5, Value: "Mango" },
// { Key: 2, Value: "Pear" },
// { Key: 7, Value: "Pineapple" },
// { Key: 4, Value: "Kiwi" },
// { Key: 3, Value: "Orange" },
// { Key: 9, Value: "Melon" }
// ]

Copy full snippet(9 lines long)

Removing elements can leave holes in the data structure, which you can see when visualizing the map in Visual Studio's watch window, but they have been omitted here for clarity.

The `FindAndRemoveChecked` function can be used to remove an element from the map and return its value. The "checked" part of the name indicates that the map calls check if the key does not exist.

C++

```
FString Removed7 = FruitMap.FindAndRemoveChecked(7);
// Removed7 == "Pineapple"
// FruitMap == [
// 	{ Key: 5, Value: "Mango"  },
// 	{ Key: 2, Value: "Pear"   },
// 	{ Key: 4, Value: "Kiwi"   },
// 	{ Key: 3, Value: "Orange" },
// 	{ Key: 9, Value: "Melon"  }
// ]
```

Expand code  Copy full snippet(12 lines long)

The [RemoveAndCopyValue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap/RemoveAndCopyValue?application_version=5.5) function is similar to `Remove`, but copies the value of the removed element out to a reference parameter. If the key you specified is not present in the map, the output parameter will be unchanged and the function returns `false`.

C++

```
FString Removed;
bool bFound2 = FruitMap.RemoveAndCopyValue(2, Removed);
// bFound2  == true
// Removed  == "Pear"
// FruitMap == [
// 	{ Key: 5, Value: "Mango"  },
// 	{ Key: 4, Value: "Kiwi"   },
// 	{ Key: 3, Value: "Orange" },
// 	{ Key: 9, Value: "Melon"  }
// ]
```

Expand code  Copy full snippet(20 lines long)

Finally, you can remove all elements from the map with the [Empty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Empty?application_version=5.5) or [Reset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Reset?application_version=5.5) functions.

C++

```
|  |  |
| --- | --- |
|  | TMap<int32, FString> FruitMapCopy = FruitMap; |
|  | // FruitMapCopy == [ |
|  | // 	{ Key: 5, Value: "Mango"  }, |
|  | // 	{ Key: 4, Value: "Kiwi"   }, |
|  | // 	{ Key: 3, Value: "Orange" }, |
|  | // 	{ Key: 9, Value: "Melon"  } |
|  | // ] |
|  |  |
|  | FruitMapCopy.Empty();		// You can also use Reset() here. |
|  | // FruitMapCopy == [] |
```

TMap<int32, FString> FruitMapCopy = FruitMap;
// FruitMapCopy == [
// { Key: 5, Value: "Mango" },
// { Key: 4, Value: "Kiwi" },
// { Key: 3, Value: "Orange" },
// { Key: 9, Value: "Melon" }
// ]
FruitMapCopy.Empty(); // You can also use Reset() here.
// FruitMapCopy == []

Copy full snippet(10 lines long)

`Empty` can take a parameter to indicate how much slack to leave in the map, while `Reset` always leaves as much slack as possible.

## Sort

You can sort a TMap by key or by value. After sorting, iteration over the map presents the elements in sorted order, but this behavior is only guaranteed until the next time you modify the map. Sorting is unstable, so equivalent elements in a `TMultiMap` may appear in any order.

You can sort by key or by value using the [KeySort](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSortableMapBase/KeySort?application_version=5.5) or [ValueSort](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TSortableMapBase/ValueSort?application_version=5.5) functions, respectively. Both functions take a binary predicate which specifies the sort order.

C++

```
FruitMap.KeySort([](int32 A, int32 B) {
	return A > B; // sort keys in reverse
});
// FruitMap == [
// 	{ Key: 9, Value: "Melon"  },
// 	{ Key: 5, Value: "Mango"  },
// 	{ Key: 4, Value: "Kiwi"   },
// 	{ Key: 3, Value: "Orange" }
// ]
```

Expand code  Copy full snippet(19 lines long)

## Operators

Like TArray, TMap is a regular value type and can be copied with the standard copy constructor or assignment operator. Maps strictly own their elements, so copying a map is deep; the new map will have its own copy of the elements.

C++

```
TMap<int32, FString> NewMap = FruitMap;
NewMap[5] = "Apple";
NewMap.Remove(3);
// FruitMap == [
// 	{ Key: 4, Value: "Kiwi"   },
// 	{ Key: 5, Value: "Mango"  },
// 	{ Key: 9, Value: "Melon"  },
// 	{ Key: 3, Value: "Orange" }
// ]
// NewMap == [
```

Expand code  Copy full snippet(14 lines long)

TMap supports move semantics, which can be invoked using the `MoveTemp`function. After a move, the source map is guaranteed to be empty:

C++

```
|  |  |
| --- | --- |
|  | FruitMap = MoveTemp(NewMap); |
|  | // FruitMap == [ |
|  | // 	{ Key: 4, Value: "Kiwi"  }, |
|  | // 	{ Key: 5, Value: "Apple" }, |
|  | // 	{ Key: 9, Value: "Melon" } |
|  | // ] |
|  | // NewMap == [] |
```

FruitMap = MoveTemp(NewMap);
// FruitMap == [
// { Key: 4, Value: "Kiwi" },
// { Key: 5, Value: "Apple" },
// { Key: 9, Value: "Melon" }
// ]
// NewMap == []

Copy full snippet(7 lines long)

## Slack

Slack is allocated memory that doesn't contain an element. You can allocate memory without adding elements by calling [Reserve](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Reserve?application_version=5.5), and you can remove elements without deallocating the memory they were using by calling [Reset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Reset?application_version=5.5) or by calling [Empty](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Empty?application_version=5.5) with a non-zero slack parameter. Slack optimizes the process of adding new elements to the map by using pre-allocated memory instead of having to allocate new memory. It can also help with element removal since the system does not need to deallocate memory. This is especially efficient when you are emptying a map that you expect to repopulate immediately with the same number of elements or fewer.

TMap does not provide a way of checking how many elements are preallocated the way the `Max` function in TArray does.

In the code below, the `Reserve` function allocates space for the map to contain up to ten elements:

C++

```
FruitMap.Reserve(10);
for (int32 i = 0; i < 10; ++i)
{
	FruitMap.Add(i, FString::Printf(TEXT("Fruit%d"), i));
}
// FruitMap == [
// 	{ Key: 9, Value: "Fruit9" },
// 	{ Key: 8, Value: "Fruit8" },
// 	...
// 	{ Key: 1, Value: "Fruit1" },
```

Expand code  Copy full snippet(12 lines long)

To remove all slack from a TMap, use the `Collapse` and [Shrink](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Shrink?application_version=5.5) functions. `Shrink` removes all slack from the end of the container, but leaves any empty elements in the middle or at the start.

C++

```
for (int32 i = 0; i < 10; i += 2)
{
	FruitMap.Remove(i);
}
// FruitMap == [
// 	{ Key: 9, Value: "Fruit9" },
// 	<invalid>,
// 	{ Key: 7, Value: "Fruit7" },
// 	<invalid>,
// 	{ Key: 5, Value: "Fruit5" },
```

Expand code  Copy full snippet(29 lines long)

`Shrink` only removed one invalid element in the code above because there was only one empty element at the end. To remove all slack, use the [Compact](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Compact?application_version=5.5) function first so that the empty spaces will be grouped together in preparation for `Shrink`.

C++

```
FruitMap.Compact();
// FruitMap == [
// 	{ Key: 9, Value: "Fruit9" },
// 	{ Key: 7, Value: "Fruit7" },
// 	{ Key: 5, Value: "Fruit5" },
// 	{ Key: 3, Value: "Fruit3" },
// 	{ Key: 1, Value: "Fruit1" },
// 	<invalid>,
// 	<invalid>,
// 	<invalid>,
```

Expand code  Copy full snippet(21 lines long)

## KeyFuncs

As long as a type has an `operator==` and a non-member [GetTypeHash](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/GenericPlatform/GetTypeHash?application_version=5.5) overload, you can use it as a key type for a TMap without any changes. However, you may want to use types as keys without overloading those functions. In these cases, you can provide your own custom [KeyFuncs](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs?application_version=5.5). To create KeyFuncs for your key type, you must define two typedefs and three static functions, as follows:

| Type Definition | Description |
| --- | --- |
| `KeyInitType` | Type used to pass keys around. |
| `ElementInitType` | Type used to pass elements around. |

| Function | Description |
| --- | --- |
| `KeyInitType GetSetKey(ElementInitType Element)` | Returns the key of an element. |
| `bool Matches(KeyInitType A, KeyInitType B)` | Returns `true` if `A` and `B` are equivalent, `false` otherwise. |
| `uint32 GetKeyHash(KeyInitType Key)` | Returns the hash value of `Key`. |

`KeyInitType` and `ElementInitType` are typedefs to the normal passing convention of the key type and element type. Usually, these will be a value for trivial types and a const reference for non-trivial types. Remember that the element type of a map is a `TPair`.

The following code snippet is an example of a custom KeyFuncs:

MyCustomKeyFuncs.cpp

C++

```
struct FMyStruct
{
	// String which identifies our key
	FString UniqueID;

	// Some state which doesn't affect struct identity
	float SomeFloat;

	explicit FMyStruct(float InFloat)
		: UniqueID (FGuid::NewGuid().ToString())
```

Expand code  Copy full snippet(49 lines long)

`FMyStruct` features a unique identifier, as well as some other data that does not contribute to its identity. `GetTypeHash` and `operator==` would be inappropriate here, because `operator==` should not ignore any of the type's data for general-purpose usage, but would simultaneously need to do so in order to be consistent with the behavior of `GetTypeHash`, which only looks at the *UniqueID* field.

To create a custom `KeyFuncs` for `FMyStruct`, follow these steps:

1. Inherit from `BaseKeyFuncs`, as it defines some helpful types, including `KeyInitType` and `ElementInitType`.

   * `BaseKeyFuncs` takes two template parameters:

     1. The element type of the map.

        + As with all maps, the element type is a `TPair`, taking `FMyStruct` as its `KeyType` and the template parameter of `TMyStructMapKeyFuncs` as its `ValueType`. The replacement `KeyFuncs` is a template, so that you can specify `ValueType` on a per-map basis, rather than needing to define a new `KeyFuncs` every time you want to create a TMap keyed on `FMyStruct`.
     2. The type of our key.

        + The second `BaseKeyFuncs` argument is the type of the key, not to be confused with the `KeyType` from TPair, the Key field of the element stores. Since this map should use `UniqueID` (from `FMyStruct`) as its key, `FString` is used here.
2. Define the three required `KeyFuncs` static functions.

   * The first is [GetSetKey](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs/GetSetKey?application_version=5.5), which returns the key for a given element type. Our element type is `TPair`, and our key is `UniqueID`, so the function can simply return `UniqueID` directly.
   * The second static function is [Matches](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs/Matches?application_version=5.5), which takes the keys of two elements retrieved by `GetSetKey`, and compares them to see if they are equivalent. For `FString`, the standard equivalence test (`operator==`) is case-insensitive; to replace this with a case-sensitive search, use the `Compare()` function with the appropriate case-comparison option.
   * The third static function is `GetKeyHash`, which takes an extracted key and returns a hashed value for it. Because the `Matches` function is case-sensitive, `GetKeyHash` must also be. A case-sensitive [FCrc](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Misc/FCrc?application_version=5.5) function calculates the hash value from the key string.
3. Now that the structure supports the behaviors that TMap requires, you can create instances of it.

   C++

   ```
   TMap<
            FMyStruct,
            int32,
            FDefaultSetAllocator,
            TMyStructMapKeyFuncs<int32>
        > MyMapToInt32;
   		
        // Add some elements
        MyMapToInt32.Add(FMyStruct(3.14f), 5);
        MyMapToInt32.Add(FMyStruct(1.23f), 2);
   ```

   Expand code  Copy full snippet(26 lines long)

   In this example, the default set allocator is specified. This is because the `KeyFuncs` parameter is last, and this `TMap` type requires it.

When providing your own KeyFuncs, be aware that `TMap` assumes that two items that compare as equal with [Matches](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/DefaultKeyFuncs/Matches?application_version=5.5) also return the same value from `GetKeyHash`. In addition, modifying the key of an existing map element in a way that changes the results from either of these functions is considered an undefined behavior, as this invalidates the map's internal hash. These rules also apply to overloads of `operator==` and `GetKeyHash` when using the default `KeyFuncs`.

## Miscellaneous

The `CountBytes` and `GetAllocatedSize` functions estimate how much memory the internal array is currently utilizing. `CountBytes` takes an `FArchive` parameter, while `GetAllocatedSize` does not. These functions are typically used for stats reporting.

The [Dump](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMapBase/Dump?application_version=5.5) function takes an `FOutputDevice` and writes out some implementation information about the contents of the map. This function is usually used for debugging.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Types of Maps in Unreal Engine](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#types-of-maps-in-unreal-engine)
* [Overview of TMap](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#overview-of-t-map)
* [Overview of TMultiMap](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#overview-of-t-multi-map)
* [Create and Fill a Map](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#create-and-fill-a-map)
* [Add](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#add)
* [Emplace](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#emplace)
* [Append](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#append)
* [Iterate](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#iterate)
* [Get Value](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#get-value)
* [Query](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#query)
* [Remove](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#remove)
* [Sort](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#sort)
* [Operators](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#operators)
* [Slack](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#slack)
* [KeyFuncs](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#key-funcs)
* [Miscellaneous](/documentation/en-us/unreal-engine/map-containers-in-unreal-engine?application_version=5.7#miscellaneous)
