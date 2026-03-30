<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7 -->

# Properties

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
7. Properties

# Properties

Reference for creating and implementing properties for gameplay classes.

![Properties](https://dev.epicgames.com/community/api/documentation/image/5454ae33-c7c5-418d-adf9-9fa79c86b851?resizing_type=fill&width=1920&height=335)

 On this page

## Property Declaration

Properties are declared using standard C++ variable syntax, preceded by the UPROPERTY macro which defines property metadata and variable specifiers.

C++

```
|  |  |
| --- | --- |
|  | UPROPERTY([specifier, specifier, ...], [meta(key=value, key=value, ...)]) |
|  | Type VariableName; |
```

UPROPERTY([specifier, specifier, ...], [meta(key=value, key=value, ...)])
Type VariableName;

Copy full snippet(2 lines long)

## Core Data Types

### Integers

The convention for integral data types is "int" or "uint" followed by the size in bits.

| Variable Type | Description |
| --- | --- |
| **uint8** | 8-bit unsigned |
| **uint16** | 16-bit unsigned |
| **uint32** | 32-bit unsigned |
| **uint64** | 64-bit unsigned |
| **int8** | 8-bit signed |
| **int16** | 16-bit signed |
| **int32** | 32-bit signed |
| **int64** | 64-bit signed |

#### As Bitmasks

Integer properties can now be exposed to the Editor as bitmasks. To mark an integer property as a bitmask, just add "bitmask" to the meta section, as follows:

C++

```
|  |  |
| --- | --- |
|  | /*~ BasicBits appears as a list of generic flags in the editor, instead of an integer field. */ |
|  | UPROPERTY(EditAnywhere, Meta = (Bitmask)) |
|  | int32 BasicBits; |
```

/\*~ BasicBits appears as a list of generic flags in the editor, instead of an integer field. \*/
UPROPERTY(EditAnywhere, Meta = (Bitmask))
int32 BasicBits;

Copy full snippet(3 lines long)

Adding this meta tag will cause the integer to be editable as a drop-down list of generically-named flags ("Flag 1", "Flag 2", "Flag 3", etc.) that can be
turned on or off individually.

[![](https://dev.epicgames.com/community/api/documentation/image/2b1e1468-04f9-41fa-88ac-89282c9fa233?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b1e1468-04f9-41fa-88ac-89282c9fa233?resizing_type=fit)

You can also make integer parameters to Blueprint-callable functions behave as bitmasks, by adding the `Bitmask` meta tag (no value necessary) to a `UPARAM` Specifier for the parameter.

C++

```
|  |  |
| --- | --- |
|  | /*~ You can set MyFunction using a generic list of flags instead of typing in an integer value. */ |
|  | UFUNCTION(BlueprintCallable) |
|  | void MyFunction(UPARAM(meta=(Bitmask)) int32 BasicBitsParam) |
```

/\*~ You can set MyFunction using a generic list of flags instead of typing in an integer value. \*/
UFUNCTION(BlueprintCallable)
void MyFunction(UPARAM(meta=(Bitmask)) int32 BasicBitsParam)

Copy full snippet(3 lines long)

In order to customize the bitflags' names, we must first create a UENUM with the "bitflags" meta tag:

C++

```
|  |  |
| --- | --- |
|  | UENUM(Meta = (Bitflags)) |
|  | enum class EColorBits |
|  | { |
|  | ECB_Red, |
|  | ECB_Green, |
|  | ECB_Blue |
|  | }; |
```

UENUM(Meta = (Bitflags))
enum class EColorBits
{
ECB\_Red,
ECB\_Green,
ECB\_Blue
};

Copy full snippet(7 lines long)

The supported value range for a bitmask enumerated type is 0 to 31, inclusive. This corresponds to the bits (starting at bit 0) of a 32-bit integer variable. In the example above, bit 0 is `ECB_Red`, bit 1 is `ECB_Green`, and bit 2 is `ECB_Blue`.

As an alternate declaration style, you can use the `ENUM_CLASS_FLAGS` to turn your enumerated type into a bitmask after defining it. In order to use the flag selector in the editor, we must also add the meta field `UseEnumValuesAsMaskValuesInEditor` and set it to `true`. The key difference is that this method uses the mask values directly, instead of the bit numbers. The equivalent enumerated type, made using this method, would look like this:

C++

```
|  |  |
| --- | --- |
|  | UENUM(Meta = (Bitflags, UseEnumValuesAsMaskValuesInEditor = "true")) |
|  | enum class EColorBits |
|  | { |
|  | ECB_Red = 0x01, |
|  | ECB_Green = 0x02, |
|  | ECB_Blue = 0x04 |
|  | }; |
|  |  |
|  | ENUM_CLASS_FLAGS(EColorBits); |
```

UENUM(Meta = (Bitflags, UseEnumValuesAsMaskValuesInEditor = "true"))
enum class EColorBits
{
ECB\_Red = 0x01,
ECB\_Green = 0x02,
ECB\_Blue = 0x04
};
ENUM\_CLASS\_FLAGS(EColorBits);

Copy full snippet(9 lines long)

After creating this UENUM, we can reference it with the "BitmaskEnum" meta tag, like this:

C++

```
|  |  |
| --- | --- |
|  | /*~ This property lists flags matching the names of values from EColorBits. */ |
|  | UPROPERTY(EditAnywhere, Meta = (Bitmask, BitmaskEnum = "EColorBits")) |
|  | int32 ColorFlags; |
```

/\*~ This property lists flags matching the names of values from EColorBits. \*/
UPROPERTY(EditAnywhere, Meta = (Bitmask, BitmaskEnum = "EColorBits"))
int32 ColorFlags;

Copy full snippet(3 lines long)

Following this change, the bitflags listed in the drop-down box will take on the names and values of the enumerated class entries. In the example above, ECB\_Red
is value 0, meaning it will activate bit 0 (adding 1 to ColorFlags) when checked. ECB\_Green corresponds to bit 1 (adding 2 to ColorFlags), and ECB\_Blue
corresponds to bit 2 (adding 4 to ColorFlags).

[![](https://dev.epicgames.com/community/api/documentation/image/e30b24de-da30-4d1d-8188-67b193b03c3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e30b24de-da30-4d1d-8188-67b193b03c3d?resizing_type=fit)

Similarly, you can add `BitmaskEnum` and the appropriate enumerated type name to the meta section of your `UPARAM` tag to customize it.

C++

```
|  |  |
| --- | --- |
|  | /*~ MyOtherFunction shows flags named after the values from EColorBits. */ |
|  | UFUNCTION(BlueprintCallable) |
|  | void MyOtherFunction(UPARAM(meta=(Bitmask, BitmaskEnum = "EColorBits")) int32 ColorFlagsParam) |
```

/\*~ MyOtherFunction shows flags named after the values from EColorBits. \*/
UFUNCTION(BlueprintCallable)
void MyOtherFunction(UPARAM(meta=(Bitmask, BitmaskEnum = "EColorBits")) int32 ColorFlagsParam)

Copy full snippet(3 lines long)

While enumerated types can contain more than 32 entries, only the first 32 values will be visible in a bitmask association in the Property Editor UI. Similarly, while explicit-value entries are accepted, entries with explicit values not between 0 and 31 will not be included in the drop-down.

### Floating Point Types

Unreal uses the standard C++ floating point types, float, and double.

### Boolean Types

Boolean types can be represented either with the C++ bool keyword or as a bitfield.

C++

```
|  |  |
| --- | --- |
|  | uint32 bIsHungry : 1; |
|  | bool bIsThirsty; |
```

uint32 bIsHungry : 1;
bool bIsThirsty;

Copy full snippet(2 lines long)

### Strings

Unreal Engine supports three core types of strings.

* FString is a classic "dynamic array of chars" string type.
* FName is a reference to an immutable case-insensitive string in a global string table. It is smaller and more efficient to pass around than an FString, but more difficult to manipulate.
* FText is a more robust string representation designed to handle localization.

For most uses, Unreal relies on the TCHAR type for characters. The TEXT() macro is available to denote TCHAR literals.

C++

```
MyDogPtr->DogName = FName(TEXT("Samson Aloysius"));
```

MyDogPtr->DogName = FName(TEXT("Samson Aloysius"));

Copy full snippet(1 line long)

For more on the three string types, when to use each one, and how to work with them, see the [String Handling documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/string-handling-in-unreal-engine).

## Property Specifiers

When declaring properties, **Property Specifiers** can be added to the declaration to control how the property behaves with various aspects of the Engine and Editor.

| Property Tag | Effect |
| --- | --- |
| `AdvancedDisplay` | The property will be placed in the advanced (dropdown) section of any panel where it appears. |
| `AssetRegistrySearchable` | The `AssetRegistrySearchable` Specifier indicates that this property and its value will be automatically added to the Asset Registry for any Asset class instances containing this as a member variable. It is not legal to use struct properties or parameters. |
| `BlueprintAssignable` | Usable with Multicast Delegates only. Exposes the property for assigning in Blueprints. |
| `BlueprintAuthorityOnly` | This property must be a Multicast Delegate. In Blueprints, it will only accept events tagged with `BlueprintAuthorityOnly`. |
| `BlueprintCallable` | Multicast Delegates only. Property should be exposed for calling in Blueprint code. |
| `BlueprintGetter=GetterFunctionName` | This property specifies a custom accessor function. If this property isn't also tagged with `BlueprintSetter` or `BlueprintReadWrite`, then it is implicitly `BlueprintReadOnly`. |
| `BlueprintReadOnly` | This property can be read by Blueprints, but not modified. This Specifier is incompatible with the `BlueprintReadWrite` Specifier. |
| `BlueprintReadWrite` | This property can be read or written from a Blueprint. This Specifier is incompatible with the `BlueprintReadOnly` Specifier. |
| `BlueprintSetter=SetterFunctionName` | This property has a custom mutator function, and is implicitly tagged with `BlueprintReadWrite`. Note that the mutator function must be named and part of the same class. |
| `Category="TopCategory\|SubCategory\|..."` | Specifies the category of the property when displayed in Blueprint editing tools. Define nested categories using the | operator. |
| `Config` | This property will be made configurable. The current value can be saved to the `.ini` file associated with the class and will be loaded when created. Cannot be given a value in default properties. Implies `BlueprintReadOnly`. |
| `DuplicateTransient` | Indicates that the property's value should be reset to the class default value during any type of duplication (copy/paste, binary duplication, etc.). |
| `EditAnywhere` | Indicates that this property can be edited by property windows, on archetypes and instances. This Specifier is incompatible with any of the "Visible" Specifiers. |
| `EditDefaultsOnly` | Indicates that this property can be edited by property windows, but only on archetypes. This Specifier is incompatible with any of the "Visible" Specifiers. |
| `EditFixedSize` | Only useful for dynamic arrays. This will prevent the user from changing the length of an array via the Unreal Editor property window. |
| `EditInstanceOnly` | Indicates that this property can be edited by property windows, but only on instances, not on archetypes. This Specifier is incompatible with any of the "Visible" Specifiers. |
| `Export` | Only useful for Object properties (or arrays of Objects). Indicates that the Object assigned to this property should be exported in its entirety as a subobject block when the Object is copied (such as for copy/paste operations), as opposed to just outputting the Object reference itself. |
| `GlobalConfig` | Works just like `Config` except that you cannot override it in a subclass. Cannot be given a value in default properties. Implies `BlueprintReadOnly`. |
| `Instanced` | Object (`UCLASS`) properties only. When an instance of this class is created, it will be given a unique copy of the Object assigned to this property in defaults. Used for instancing subobjects defined in class default properties. Implies `EditInline` and `Export`. |
| `Interp` | Indicates that the value can be driven over time by a Track in Sequencer. |
| `Localized` | The value of this property will have a localized value defined. Mostly used for strings. Implies `ReadOnly`. |
| `Native` | Property is native: C++ code is responsible for serializing it and exposing it to [Garbage Collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-object-handling-in-unreal-engine). |
| `NoClear` | Prevents this Object reference from being set to none from the editor. Hides the clear (and browse) button in the editor. |
| `NoExport` | Only useful for native classes. This property should not be included in the auto-generated class declaration. |
| `NonPIEDuplicateTransient` | The property will be reset to the default value during duplication, except if it's being duplicated for a Play In Editor (PIE) session. |
| `NonTransactional` | Indicates that changes to this property's value will not be included in the editor's undo/redo history. |
| `NotReplicated` | Skip replication. This only applies to struct members and parameters in service request functions. |
| `Replicated` | The property should be replicated over the network. |
| `ReplicatedUsing=FunctionName` | The `ReplicatedUsing` Specifier specifies a callback function which is executed when the property is updated over the network. |
| `RepRetry` | Only useful for struct properties. Retry replication of this property if it fails to be fully sent (for example, Object references not yet available to serialize over the network). For simple references, this is the default, but for structs, this is often undesirable due to the bandwidth cost, so it is disabled unless this flag is specified. |
| `SaveGame` | This Specifier is a simple way to include fields explicitly for a checkpoint/save system at the property level. The flag should be set on all fields that are intended to be part of a saved game, and then a proxy archiver can be used to read/write it. |
| `SerializeText` | Native property should be serialized as text (`ImportText`, `ExportText`). |
| `SkipSerialization` | This property will not be serialized, but can still be exported to a text format (such as for copy/paste operations). |
| `SimpleDisplay` | Visible or editable properties appear in the **Details** panel and are visible without opening the "Advanced" section. |
| `TextExportTransient` | This property will not be exported to a text format (so it cannot, for example, be used in copy/paste operations). |
| `Transient` | Property is transient, meaning it will not be saved or loaded. Properties tagged this way will be zero-filled at load time. |
| `VisibleAnywhere` | Indicates that this property is visible in all property windows, but cannot be edited. This Specifier is incompatible with the "Edit" Specifiers. |
| `VisibleDefaultsOnly` | Indicates that this property is only visible in property windows for archetypes, and cannot be edited. This Specifier is incompatible with any of the "Edit" Specifiers. |
| `VisibleInstanceOnly` | Indicates that this property is only visible in property windows for instances, not for archetypes, and cannot be edited. This Specifier is incompatible with any of the "Edit" Specifiers. |

## Metadata Specifiers

When declaring classes, interfaces, structs, enums, enum values, functions, or properties, you can add **Metadata Specifiers** to control how they interact with various aspects of the engine and editor. Each type of data structure or member has its own list of Metadata Specifiers.

Metadata only exists in the editor; do not write game logic that accesses metadata.

| Property Meta Tag | Effect |
| --- | --- |
| `AllowAbstract="true/false"` | Used for `Subclass` and `SoftClass` properties. Indicates whether abstract Class types should be shown in the Class picker. |
| `AllowedClasses="Class1, Class2, .."` | Used for `FSoftObjectPath` properties. Comma delimited list that indicates the Class type(s) of assets to be displayed in the Asset picker. |
| `AllowPreserveRatio` | Used for `FVector` properties. It causes a ratio lock to be added when displaying this property in details panels. |
| `ArrayClamp="ArrayProperty"` | Used for integer properties. Clamps the valid values that can be entered in the UI to be between 0 and the length of the array property named. |
| `AssetBundles` | Used for `SoftObjectPtr` or `SoftObjectPath` properties. List of Bundle names used inside Primary Data Assets to specify which Bundles this reference is part of. |
| `BlueprintBaseOnly` | Used for `Subclass` and `SoftClass` properties. Indicates whether only Blueprint Classes should be shown in the Class picker. |
| `BlueprintCompilerGeneratedDefaults` | Property defaults are generated by the Blueprint compiler and will not be copied when the `CopyPropertiesForUnrelatedObjects` function is called post-compile. |
| `ClampMin="N"` | Used for float and integer properties. Specifies the minimum value `N` that may be entered for the property. |
| `ClampMax="N"` | Used for float and integer properties. Specifies the maximum value `N` that may be entered for the property. |
| `ConfigHierarchyEditable` | This property is serialized to a config (`.ini`) file, and can be set anywhere in the config hierarchy. |
| `ContentDir` | Used by `FDirectoryPath` properties. Indicates that the path will be picked using the Slate-style directory picker inside the `Content` folder. |
| `DisplayAfter="PropertyName"` | This property will show up in the Blueprint Editor immediately after the property named `PropertyName`, regardless of its order in source code, as long as both properties are in the same category. If multiple properties have the same `DisplayAfter` value and the same `DisplayPriority` value, they will appear after the named property in the order in which they are declared in the header file. |
| `DisplayName="Property Name"` | The name to display for this property, instead of the code-generated name. |
| `DisplayPriority="N"` | If two properties feature the same `DisplayAfter` value, or are in the same category and do not have the `DisplayAfter` Meta Tag, this property will determine their sorting order. The highest-priority value is 1, meaning that a property with a `DisplayPriority` value of 1 will appear above a property with a `DisplayPriority` value of 2. If multiple properties have the same `DisplayAfter` value, they will appear in the order in which they are declared in the header file. |
| `DisplayThumbnail="true"` | Indicates that the property is an Asset type and it should display the thumbnail of the selected Asset. |
| `EditCondition="BooleanPropertyName"` | Names a boolean property that is used to indicate whether editing of this property is disabled. Putting "!" before the property name inverts the test.  The EditCondition meta tag is no longer limited to a single boolean property. It is now evaluated using a full-fledged expression parser, meaning you can include a full C++ expression. |
| `EditFixedOrder` | Keeps the elements of an array from being reordered by dragging. |
| `ExactClass="true"` | Used for `FSoftObjectPath` properties in conjunction with `AllowedClasses`. Indicates whether only the exact Classes specified in `AllowedClasses` can be used, or if subclasses are also valid. |
| `ExposeFunctionCategories="Category1, Category2, .."` | Specifies a list of categories whose functions should be exposed when building a function list in the Blueprint Editor. |
| `ExposeOnSpawn="true"` | Specifies whether the property should be exposed on a Spawn Actor node for this Class type. |
| `FilePathFilter="FileType"` | Used by `FFilePath` properties. Indicates the path filter to display in the file picker. Common values include "uasset" and "umap", but these are not the only possible values. |
| `GetByRef` | Makes the "Get" Blueprint Node for this property return a const reference to the property instead of a copy of its value. Only usable with Sparse Class Data, and only when `NoGetter` is not present. |
| `HideAlphaChannel` | Used for `FColor` and `FLinearColor` properties. Indicates that the `Alpha` property should be hidden when displaying the property widget in the details. |
| `HideViewOptions` | Used for `Subclass` and `SoftClass` properties. Hides the ability to change view options in the Class picker. |
| `InlineEditConditionToggle` | Signifies that the boolean property is only displayed inline as an edit condition toggle in other properties, and should not be shown on its own row. |
| `LongPackageName` | Used by `FDirectoryPath` properties. Converts the path to a long package name. |
| `MakeEditWidget` | Used for Transform or Rotator properties, or Arrays of Transforms or Rotators. Indicates that the property should be exposed in the viewport as a movable widget. |
| `NoGetter` | Causes Blueprint generation not to generate a "get" Node for this property. Only usable with Sparse Class Data. |
| `ScriptName="DisplayName"` | The name to use for this clas, property, or function when exporting it to a scripting language. You may include deprecated names as additional semi-colon-separated entries. |

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [uenum](https://dev.epicgames.com/community/search?query=uenum)
* [uproperty](https://dev.epicgames.com/community/search?query=uproperty)
* [variable](https://dev.epicgames.com/community/search?query=variable)
* [enum](https://dev.epicgames.com/community/search?query=enum)
* [bitmask](https://dev.epicgames.com/community/search?query=bitmask)
* [bitfield](https://dev.epicgames.com/community/search?query=bitfield)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Property Declaration](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#property-declaration)
* [Core Data Types](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#core-data-types)
* [Integers](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#integers)
* [As Bitmasks](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#as-bitmasks)
* [Floating Point Types](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#floating-point-types)
* [Boolean Types](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#boolean-types)
* [Strings](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#strings)
* [Property Specifiers](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#property-specifiers)
* [Metadata Specifiers](/documentation/en-us/unreal-engine/unreal-engine-uproperties?application_version=5.7#metadataspecifiers)
