<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7 -->

# Reordering and Hiding Properties

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Scripting and Automating the Unreal Editor](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor "Scripting and Automating the Unreal Editor")
7. [Slate Tools Programming](/documentation/en-us/unreal-engine/programming-tools-for-the-unreal-editor-with-slate-ui-in-cplusplus "Slate Tools Programming")
8. [Details Panel Customizations](/documentation/en-us/unreal-engine/details-panel-customizations-in-unreal-engine "Details Panel Customizations")
9. Reordering and Hiding Properties

# Reordering and Hiding Properties

Reorder properties and categories in your Details Panel customization.

![Reordering and Hiding Properties](https://dev.epicgames.com/community/api/documentation/image/cf659a44-85d0-46a9-84ab-05e97aa7962c?resizing_type=fill&width=1920&height=335)

 On this page

Details Panel Customizations can change the order in which properties appear in the Details Panel, as well as show or hide properties that wouldn't ordinarily be visible. This page provides instructions on how to show, hide, and reorder both properties and categories.

## Prerequisites

This page uses the [Details Panel Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/details-panel-quickstart-guide-for-unreal-engine) tutorial as the basis for its examples and refers to the following:

* FCustomDataProperty – A custom struct consisting of the following:

  + TSoftObjectPtr<UTexture> CustomTexture
  + FName CustomName
  + FString CustomString
  + Int32 CustomInt
* ACustomActor – A simple Actor with the following added properties:

  + TSoftObjectPtr<UStaticMesh> CustomMesh
  + float CustomFloat
  + bool CustomBool
  + FCustomDataProperty CustomData
* FCustomDataPropertyCustomization – A Property Type Customization for FCustomDataProperty.
* FCustomClassDetailsCustomization – A Detail Customization for ACustomActor.

You should also review [Refreshing the Details Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/refreshing-custom-details-panels-in-unreal-engine) if you want to show or hide details based on changes made by the user.

## Properties

### Reorder Properties

You can re-order properties by changing the order in which you make **AddProperty** calls. The Class Details customization in the [Details Panel Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/details-panel-quickstart-guide-for-unreal-engine) includes an example of re-ordering properties. The original property declarations for `ACustomActor` are as follows:

C++

CustomActorClass.h

```
UPROPERTY(EditAnywhere)
	TSoftObjectPtr<UStaticMesh> CustomMesh;

	UPROPERTY(EditAnywhere)
	float CustomFloat;

	UPROPERTY(EditAnywhere)
	bool CustomBool;

	UPROPERTY(EditAnywhere)
```

Expand code  Copy full snippet(11 lines long)

Normally, CustomMesh and CustomFloat would appear first in the Details Panel. However, the `FCustomClassDetailsCustomization::CustomizeDetails` function adds them to the details panel as follows:

C++

CustomActorClassCustomization.h

```
|  |  |
| --- | --- |
|  | CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomData)); |
|  | CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomBool)); |
|  | CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomMesh)); |
|  | CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomFloat)); |
```

CustomCategory.AddProperty(GET\_MEMBER\_NAME\_CHECKED(ACustomActor, CustomData));
CustomCategory.AddProperty(GET\_MEMBER\_NAME\_CHECKED(ACustomActor, CustomBool));
CustomCategory.AddProperty(GET\_MEMBER\_NAME\_CHECKED(ACustomActor, CustomMesh));
CustomCategory.AddProperty(GET\_MEMBER\_NAME\_CHECKED(ACustomActor, CustomFloat));

Copy full snippet(4 lines long)

This results in CustomData and CustomBool appearing first. Similarly, any other custom **Slate** elements will appear in the order that you add them.

If you do not add a property in your **Details Customization**, it uses the default order and the default category for your actor. See **Hide Properties** below for information on how to avoid displaying properties.

### Hide Properties

Use `IDetailCategoryBuilder::HideProperty` to selectively hide properties that would normally appear due to their UPROPERTY specifiers.

C++

CustomClassDetailsCustomization.cpp

```
DetailBuilder.HideProperty(FCustomDataProperty::StaticStruct()->GetFName());
```

DetailBuilder.HideProperty(FCustomDataProperty::StaticStruct()->GetFName());

Copy full snippet(1 line long)

## Categories

### Reorder Categories

Use `IDetailCategoryBuilder::SortCategories` to set the order your custom categories render in.

`IDetailCategoryBuilder::SortCategories` takes a delegate with the signature `void FunctionName (const TMap<FName, IDetailCategoryBuilder*>&)`. Any functions you use for this delegate must be static functions. The [TMap](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/Containers/TMap?application_version=5.5) is a map of all the categories added by your custom class. Once you fetch a category from it, use `IDetailCategoryBuilder::SetSortOrder` to change what order the categories appear in. `IDetailCategoryBuilder::SetSortOrder` always sorts from lowest to highest.

C++

CustomClassDetailsCustomization.h

```
static void SortCustomDetailsCategories(const TMap<FName, IDetailCategoryBuilder*>& AllCategoryMap);
```

static void SortCustomDetailsCategories(const TMap<FName, IDetailCategoryBuilder\*>& AllCategoryMap);

Copy full snippet(1 line long)

C++

CustomClassDetailsCustomization.cpp

```
//Custom details with two category names.

	void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder& DetailBuilder)
	{
		IDetailCategoryBuilder& CustomCategory = DetailBuilder.EditCategory(FName("Custom Settings"));
		IDetailCategoryBuilder& DataCategory = DetailBuilder.EditCategory(FName("Data"));
		CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomBool));
		CustomCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomMesh));
		DataCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomData));
		DataCategory.AddProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomFloat));
```

Expand code  Copy full snippet(20 lines long)

### Hide Categories

Use `IDetailCategoryBuilder::HideCategory` to hide an entire category. You can use categories you defined with UPROPERTY specifiers or one you defined as part of a detail customization. Provide the `FName` of the category.

C++

CustomClassDetailsCustomization.cpp

```
|  |  |
| --- | --- |
|  | void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder& DetailBuilder) |
|  | { |
|  | FName CustomCategoryName = FName("Custom Settings"); |
|  | IDetailCategoryBuilder& CustomCategory = DetailBuilder.EditCategory(CustomCategoryName); |
|  | DetailBuilder.HideCategory(CustomCategoryName); |
|  | } |
```

void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder& DetailBuilder)
{
FName CustomCategoryName = FName("Custom Settings");
IDetailCategoryBuilder& CustomCategory = DetailBuilder.EditCategory(CustomCategoryName);
DetailBuilder.HideCategory(CustomCategoryName);
}

Copy full snippet(6 lines long)

### Advanced Categories

Use `IDetailCategoryBuilder::SetShowAdvanced` to designate a category to show only when you expand the **Advanced** section of the **Details Panel**.

C++

CustomClassDetailsCustomization.cpp

```
|  |  |
| --- | --- |
|  | void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder& DetailBuilder) |
|  | { |
|  | FName CustomCategoryName = FName("Custom Settings"); |
|  | IDetailCategoryBuilder& CustomCategory = DetailBuilder.EditCategory(CustomCategoryName); |
|  | CustomCategory.SetShowAdvanced(true); |
|  | } |
```

void FCustomClassDetailsCustomization::CustomizeDetails(IDetailLayoutBuilder& DetailBuilder)
{
FName CustomCategoryName = FName("Custom Settings");
IDetailCategoryBuilder& CustomCategory = DetailBuilder.EditCategory(CustomCategoryName);
CustomCategory.SetShowAdvanced(true);
}

Copy full snippet(6 lines long)

* [customizations](https://dev.epicgames.com/community/search?query=customizations)
* [slate](https://dev.epicgames.com/community/search?query=slate)
* [tools programming](https://dev.epicgames.com/community/search?query=tools%20programming)
* [details panel](https://dev.epicgames.com/community/search?query=details%20panel)
* [details categories](https://dev.epicgames.com/community/search?query=details%20categories)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#prerequisites)
* [Properties](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#properties)
* [Reorder Properties](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#reorder-properties)
* [Hide Properties](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#hide-properties)
* [Categories](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#categories)
* [Reorder Categories](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#reorder-categories)
* [Hide Categories](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#hide-categories)
* [Advanced Categories](/documentation/en-us/unreal-engine/reordering-and-hiding-properties-in-details-panel-customizations-in-unreal-engine?application_version=5.7#advanced-categories)
