<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.7 -->

# Using CommonUI With Enhanced Input

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
5. [Creating User Interfaces](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine "Creating User Interfaces")
6. [Plugins for UI Development](/documentation/en-us/unreal-engine/plugins-for-ui-development-in-unreal-engine "Plugins for UI Development")
7. [Common UI](/documentation/en-us/unreal-engine/common-ui-plugin-for-advanced-user-interfaces-in-unreal-engine "Common UI")
8. Using CommonUI With Enhanced Input

# Using CommonUI With Enhanced Input

Learn how to incorporate Enhanced Input with CommonUI's input system.

![Using CommonUI With Enhanced Input](https://dev.epicgames.com/community/api/documentation/image/778868b5-c668-4f75-b0f7-9c6829073a92?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Common UI Overview](/documentation/en-us/unreal-engine/overview-of-advanced-multiplatform-user-interfaces-with-common-ui-for-unreal-engine)

 On this page

The **CommonUI plugin** provides limited support for [Enhanced Input](/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine) actions.

As of UE 5.2, Enhanced Input support has not been tested as thoroughly as other features in CommonUI. We do not recommend attempting to ship titles with this feature at this time.

## 1. Required Setup

This page assumes that you have performed the following setup steps for CommonUI:

* Enable both the CommonUI and Enhanced Input plugins.
* Set your Viewport class to CommonGameViewportClient.
* Set up your InputData for Accept/Back actions.

## 2. Enable Enhanced Input in CommonUI

After enabling the CommonUI and Enhanced Input plugins, open **Project Settings.** Navigate to **Game** > **Common Input Settings** and set **Enable Enhanced** **Input Support** to **true**. This enables support for these two plugins to communicate.

![Enable Enhanced Input in Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de59e142-588c-4853-a138-6a92a7d9f49a/enableenhancedinput.png)

## 3. Set Up Enhanced Input Actions for CommonUI

Enhanced Input actions can bind input events anywhere, including specialized variants such as *ongoing* and *triggered* events. However, it is undesirable and chaotic to globally bind a majority of UI action bindings such as *FaceButtonTop*, *Accept*, or *Back*, as this can cause unintended events as a result of the user's input at unexpected times. CommonUI solves this problem with *generic actions* . Generic actions are bound to UI elements, but do not trigger their Enhanced Input Events in CommonUI.

To set up Enhanced Input Actions within CommonUI, follow these steps:

1. Create a generic **Input Action** in the Content Browser. Name it `IA_UI_GenericAccept`.

   ![Select Input Action asset type](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0477b1a7-a525-4afd-b41a-37529b293c6a/selectinputaction.png)
2. Add a **PlayerMappableKeySettings** to your Input Action.
3. In the **Settings** for your **PlayerMappableKeySettings**, set the **Metadata** field to an object that implements the ICommonMappingContextMetadataInterface.

   ![Player Mappable Key Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e1c3574-4c2f-4678-88aa-db0e76a27d7c/mappingmetadata.png)


   You might need your Input Action Metadata for something other than CommonUI. Therefore, we advise using a class that implements `ICommonMappingContextMetadataInterface` to ensure flexibility.
4. Right-click in the Content Browser, then click **Miscellaneous** > **Data Asset** to create a Data Asset.
5. Select a metadata class that implements `ICommonMappingContextMetadataInterface` as your Data Asset class. Name your Metadata UI\_IA\_GenericMetadata. You can use UCommonMappingContextMetadata as a default, or you can use a custom asset class.

   ![Common Mapping Context](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05877376-d7ed-4746-85a3-d285b4ebb64a/commonmappingcontext.png)
6. Open UI\_IA\_GenericMetadata, then edit its settings as follows:

   * **Is Generic Input Action:** True
   * **Per Action Enhanced Input Metadata:** IA\_UI\_GenericAccept
   * **Nav Bar Priority:** 10![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7647fe51-1456-4a43-bd85-02de1b72664f/commoninputsettings.png)

   Check **Is Generic Input Action** to prevent CommonUI from broadcasting the input action.

   This data asset provides a metadata object where you can set CommonUI action data. If you are already familiar with CommonUI, you might recognize the Nav Bar Priority setting from CommonUI's data tables. You can also extend your input actions with additional metadata by inheriting from *UCommonInputMetadata*.

   You can use the **Per Action Enhanced Input Metadata** to handle the metadata for multiple actions in a single asset rather than creating one asset for each action.
7. Repeat steps 5-6, but this time leave Is Generic Input Action unchecked. Name this metadata `UI_IA_SpecificMetadata`. This results in a metadata class you can use on any Input Action that is not generic.
8. Open your Input Action. Set the Metadata to UI\_IA\_GenericMetadata. The Input Action now has all the information needed to function with CommonUI.

   ![Generic Input Action](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3723a60a-b014-400b-bd48-521eb4b38dfe/genericmetadata.png)
9. For Input Actions whose metadata does not have Is Generic Input Action enabled, you can bind input to events like any other Input Action.

   ![Non-generic Input Action](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56e8cdc7-3e22-4fc4-82a0-0637ab7fb8a9/specificwidgetaction.png)

## 4. Create an Input Mapping Context (IMC) for CommonUI

Input Mapping Contexts (IMCs) for CommonUI behave the same as other IMCs. To create an Input Mapping Context, right-click in the Content Browser, then click **Input** > **Input Mapping Context**. The following image is an example of what an IMC used with CommonUI might look like:

![Input Mapping Context](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c0cbe35-54ac-4554-b311-c1278981c5e0/inputmappingcontext.png)

For the sake of clarifying that your IMC is used for your UI, we recommend naming it `IMC_UI_GenericActions` or something similar.

## 5. Use Input Actions and Input Mapping Contexts in CommonUI

You can use Input Actions anywhere you previously used **DataTableRows**to specify input information. The following are typical examples:

* CommonButtonBase.

  ![Common Button Base](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0905c2db-e32e-4cab-a93b-56b85f33ae3b/specificwidgetactionobj.png)
* CommonActionWidget. This can show keys for Non-UI Input actions.

  ![Common Action Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da9eef3f-06c5-4d46-a38f-68e60313a3f7/iagrenade.png)
* Common UI Input Data. This is where default navigation actions are defined.

  ![Common UI Input Data](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8398d146-6b09-469f-bdcc-3b7ae96aeed1/genericacceptback.png)

If these settings do not appear, check that the [Enable Enhanced Input in CommonUI](/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine#enableenhanced) setting is set to true.

In Activatable Widgets, you can specify IMCs to apply and remove on activation and deactivation. For better organization, we suggest applying your generic UI IMC wherever you apply other top-level game IMCs.

![IMC specified in an Activatable Widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4d3b2fd-7621-4725-8254-542ed15e4bdb/imc_uispecific.png)

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [input](https://dev.epicgames.com/community/search?query=input)
* [commonui](https://dev.epicgames.com/community/search?query=commonui)
* [enhanced input](https://dev.epicgames.com/community/search?query=enhanced%20input)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1. Required Setup](/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.7#1requiredsetup)
* [2. Enable Enhanced Input in CommonUI](/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.7#2enableenhancedinputincommonui)
* [3. Set Up Enhanced Input Actions for CommonUI](/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.7#3setupenhancedinputactionsforcommonui)
* [4. Create an Input Mapping Context (IMC) for CommonUI](/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.7#4createaninputmappingcontext(imc)forcommonui)
* [5. Use Input Actions and Input Mapping Contexts in CommonUI](/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.7#5useinputactionsandinputmappingcontextsincommonui)

Related documents

[Common UI Overview

![Common UI Overview](https://dev.epicgames.com/community/api/documentation/image/996bbe21-6b71-4f81-961a-8a07a076833d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/overview-of-advanced-multiplatform-user-interfaces-with-common-ui-for-unreal-engine)
