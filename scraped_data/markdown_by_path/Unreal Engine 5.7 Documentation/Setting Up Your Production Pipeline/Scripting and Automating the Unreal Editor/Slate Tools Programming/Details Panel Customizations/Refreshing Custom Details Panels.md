<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/refreshing-custom-details-panels-in-unreal-engine?application_version=5.7 -->

# Refreshing Custom Details Panels

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
9. Refreshing Custom Details Panels

# Refreshing Custom Details Panels

Refresh the Details Panel in response to property changes.

![Refreshing Custom Details Panels](https://dev.epicgames.com/community/api/documentation/image/a84fbb0a-d771-4185-bf11-5c7adfabcfbb?resizing_type=fill&width=1920&height=335)

 On this page

Normally, the **Details Panel** rebuilds itself only when you select an object. This means that if you use edit conditions to add, hide, or skip adding a field in a Details Panel customization, the Details Panel updates even when you change the variables used in your edit condition. Instead, the Details Panel updates when you de-select and re-select the object.

To update the **Details Panel** manually, add a delegate that calls `IDetailLayoutBuilder::ForceRefreshDetails` to any properties that you want to trigger an update. This tutorial provides a on how to create this kind of delegate.

This tutorial builds on the code from the [Details Panel Quickstart](/documentation/en-us/unreal-engine/details-panel-quickstart-guide-for-unreal-engine).

## Steps

Follow these steps to create a reusable delegate for refreshing Details:

1. Set up your delegate to call `IDetailLayoutBuilder::ForceRefreshDetails`. The following is a simple lambda function delegate you can put inline in your `CustomizeDetails` function and reuse for all properties you want to cause a refresh:

   CustomClassDetailsCustomization.cpp

   ```
        const FSimpleDelegate OnValueChanged = FSimpleDelegate::CreateLambda([&DetailBuilder]()
        {
            DetailBuilder.ForceRefreshDetails();
        });
   Copy full snippet
   ```
2. Use `IDetailLayoutBuilder::GetProperty` to get a TSharedRef pointing at your property.

   CustomClassDetailsCustomization.cpp

   ```
        TSharedRef<IPropertyHandle> boolPropertyHandle = DetailBuilder.GetProperty(GET_MEMBER_NAME_CHECKED(ACustomActor, CustomBool));
   Copy full snippet
   ```
3. Use `IPropertyHandle::SetOnPropertyValueChanged` to assign your delegate and force the details panel to refresh anytime that property is changed.

   CustomClassDetailsCustomization.cpp

   ```
        boolProperty->SetOnPropertyValueChanged(OnValueChanged);
   Copy full snippet
   ```

With this change, any changes to the CustomBool field causes the Details Panel to refresh.

* [customizations](https://dev.epicgames.com/community/search?query=customizations)
* [slate](https://dev.epicgames.com/community/search?query=slate)
* [tools programming](https://dev.epicgames.com/community/search?query=tools%20programming)
* [details panel](https://dev.epicgames.com/community/search?query=details%20panel)
* [edit conditions](https://dev.epicgames.com/community/search?query=edit%20conditions)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/refreshing-custom-details-panels-in-unreal-engine?application_version=5.7#steps)
