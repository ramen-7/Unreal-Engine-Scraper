<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-analyzer-tool?application_version=5.7 -->

# Material Analyzer

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. Material Analyzer

# Material Analyzer

This page describes how to locate and use the Material Analyzer tool.

![Material Analyzer](https://dev.epicgames.com/community/api/documentation/image/af4b2140-2705-4535-99a4-a730002ead52?resizing_type=fill&width=1920&height=335)

 On this page

The **Material Analyzer** is a developer tool that helps you identify and analyze all Materials, or [Material instances](/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine), in your project. This enables you to make changes that can provide savings in shader permutations and data storage. When you select a Material or Material instance to analyze, the tool will find all descendants of that Material (or all descendants of the Material instance's parent Material). The tool also identifies all of the base property overrides, static switches, and static component mask parameters.

## Opening the Material Analyzer

1. In the menu bar, click **Tools > Audit > Material Analyzer**. The **Material Analyzer** window opens.

   ![Material Analyzer menu path](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/afa17c04-951b-4e18-9c9b-a0f8bdb08058/material-analyzer-menu.png)
2. Click the dropdown menu next to **Material to Analyze**. Use the list or search bar to select the Material or Material instance you want to analyze.

   ![Select Material to analyze](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1c89aa2e-a046-4b84-8867-7c25b1362c3a/select-material-to-analyze.png)
3. The Material Analyzer tool displays a list of all instances of the Material you selected.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d33e7420-a9fd-46e3-a931-508e35a9cb54/material-analyzer-results.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d33e7420-a9fd-46e3-a931-508e35a9cb54/material-analyzer-results.png)

## Viewing the Suggestion List

Below the Material instance hierarchy is a suggestion list. The suggestion list groups all Material instances with the same set of static overrides. You can click the arrow next to each line to see the specific instances identified.  
![Suggestion list](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ab14050-6d61-4246-b26d-614fdd11c211/suggestion-list.png)

## Create a Local Collection

Each suggestion list has a **Create Local Collection** button. Click this button to place all the related instances into a local collection, so you can easily find them and update them to have more efficient parameter setups.

![Create local collection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4d2c7db-8ac2-4ecf-aff9-19210bdcd1ba/create-local-collection.png)

## Viewing the Static Switch Parameters List

To see the static switch parameters for a Material instance, click the arrow next to the Static Switch Parameters column to display the full list. The columns are resizable, so you can move them if the text is cut off.

![Static switch parameters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c135a9a-9e8d-42c0-abe6-a157b59543a6/static-switch-parameters.png)

## Reparenting Material Instances

You can reparent these Material instances to a new instance that has those same static overrides, so that the reparented Material instances only change their unique overrides. This can provide a savings in shader permutations and data storage. Make sure to remove all the static parameter overrides from the Material instances you have reparented, or else the additional data is still stored.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Opening the Material Analyzer](/documentation/en-us/unreal-engine/unreal-engine-material-analyzer-tool?application_version=5.7#openingthematerialanalyzer)
* [Viewing the Suggestion List](/documentation/en-us/unreal-engine/unreal-engine-material-analyzer-tool?application_version=5.7#viewingthesuggestionlist)
* [Create a Local Collection](/documentation/en-us/unreal-engine/unreal-engine-material-analyzer-tool?application_version=5.7#createalocalcollection)
* [Viewing the Static Switch Parameters List](/documentation/en-us/unreal-engine/unreal-engine-material-analyzer-tool?application_version=5.7#viewingthestaticswitchparameterslist)
* [Reparenting Material Instances](/documentation/en-us/unreal-engine/unreal-engine-material-analyzer-tool?application_version=5.7#reparentingmaterialinstances)
