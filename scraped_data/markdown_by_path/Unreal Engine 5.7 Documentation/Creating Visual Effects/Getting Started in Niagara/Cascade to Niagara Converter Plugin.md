<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7 -->

# Cascade to Niagara Converter Plugin

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Getting Started in Niagara](/documentation/en-us/unreal-engine/getting-started-in-niagara-effects-for-unreal-engine "Getting Started in Niagara")
7. Cascade to Niagara Converter Plugin

# Cascade to Niagara Converter Plugin

This page discusses and demonstrates the plugin to convert Cascade particle systems to Niagara particle systems.

![Cascade to Niagara Converter Plugin](https://dev.epicgames.com/community/api/documentation/image/b961e31f-5ab6-45ff-a473-624c8db3ffb8?resizing_type=fill&width=1920&height=335)

 On this page

## Cascade To Niagara Converter Plugin

The **Cascade to Niagara Converter** plugin is a utility designed to convert any of your existing **Cascade Particle Systems** assets.
The plugin includes a Blueprint function library to generate both Niagara Emitter and Niagara System assets programmatically, as well as a Python scripting layer to translate Cascade Systems into the new Niagara Systems.

This plugin is ideal for those looking to convert existing content from Cascade to Niagara. It is meant as a starting point for upgrading to the latest tools used by Unreal Engine, and will continue to be updated until Cascade is deprecated and removed in a future release of the engine.

## Enabling The Cascade To Niagara Converter Plugin

To enable the Cascade to Niagara Converter plugin for your project, perform the following steps below:

1. Navigate to **Edit >Plugins** in the main menu to open the **Plugins Browser tab**.
2. From the **Built-In** category side menu, navigate to **FX >Cascade To Niagara Converter** plugin, and enable the Plugin.

   [![Cascade To Niagara Converter plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3aa81b49-ef53-44b2-8fbf-7219961802a1/niagaraconverter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3aa81b49-ef53-44b2-8fbf-7219961802a1/niagaraconverter.png)

   Click image for full size.
3. When prompted, click **Restart Now** for your changes to take effect.

   [![Click Restart Now](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/02e799fd-3912-4aa2-8569-e8aa49e429e1/restarteditor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/02e799fd-3912-4aa2-8569-e8aa49e429e1/restarteditor.png)

   Click image for full size.

## Using The Cascade To Niagara Converter Plugin

Convert your desired **Cascade Particle Systems** to a **Niagara System** by right-clicking on a
Cascade Particle in the **Content Browser** and selecting **Convert to Niagara System** from the context menu.

[![Convert to Niagara System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48b64d27-361d-43dc-affc-da0487ca48fb/convertasset.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48b64d27-361d-43dc-affc-da0487ca48fb/convertasset.png)

Click image for full size.

In the example above, we have used the Cascade Particle System P\_Steam\_Lit"from the Starter Content Folder.

A new Niagara System is created in the same directory as the source Cascade System with the suffix `_Converted`.

[![Convert Suffix](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f69cc54-72c9-45c6-8dd9-7ca63512e04a/convertsuffix.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f69cc54-72c9-45c6-8dd9-7ca63512e04a/convertsuffix.png)

Click image for full size.

Your newly generated Niagara System creates a conversion report which can be viewed by opening the new Niagara System and observing the **Niagara Log** window.
We recommend reviewing the converted Niagara Systems by opening the asset in the editor and resolving any warnings or errors that may be contained in the conversion report.

[![Niagara Log window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/04639777-a717-481f-8ef7-4c454a970436/niagaralog.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/04639777-a717-481f-8ef7-4c454a970436/niagaralog.png)

Click image for full size.

The Niagara Log provides a warning that it has skipped converting the Boolean value bApplyGlobalSpawnRateScale.

## Types Of Errors And Warnings

Upon conversion of your Cascade System to a Niagara System asset, you may notice some errors and warnings that may be displayed on the **Niagara System Overview Window**.
Hovering your mouse cursor over any of these symbols will display a brief description of any issues that may be in conflict.

* ![Error](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/22d1a26f-da86-4ce8-826a-f63586e9e4b9/error.png "Error") – Icon to indicate a **Error**.
* ![Warning](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55412e15-e24b-44c4-b0eb-10e2750b737e/warning.png "Warning") – Icon to indicate a **Warning**.

[![Converted Errors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/351247e9-b84c-49e0-b9af-066b2f0c7966/convertederrors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/351247e9-b84c-49e0-b9af-066b2f0c7966/convertederrors.png)

Click image for full size.

The image above displays a brief description of two errors denoting that a dependency has been unmet in the Particle Update field.

Selecting any of these properties will open the Selection **details window** on the right-hand side of your screen; enabling you to observe a more detailed explanation of the issues. Depending on the type of issue, a **fix issue** prompt may be provided to resolve it automatically.

|  |  |
| --- | --- |
| Error Detail | Warning Detail |
| Errors | Warnings |
| The Selection details window displays an additional detailed description of unmet dependency errors for the `Acceleration Force`, and `Drag` modules as well as suggestions on how to remedy them. Selecting Fix issue will result in the plugin adjusting the order of the module stack group | The Selection details window displays the warning Unspecified Error to indicate that the variable `bApplyGlobalRateScale` has been skipped in the conversion process. |

## Cascade To Niagara-Supported Conversion Operations

The Cascade To Niagara Converter supports converting general representations of Cascade Particle Systems; however, there are some modules and properties which are not entirely supported. The table below lists those which are not yet supported or which are partially supported.

| Feature | Supported (Y/N/Partially) | Additional Notes |
| --- | --- | --- |
| Event Modules |  |  |
| **Event Generator** | N |  |
| **EventReceiver Kill all** | N |  |
| **EventReceiver Spawn** | N |  |
| Emitter to Emitter Modules |  |  |
| **Particle Attractor** | N |  |
| **Source Movement** | N |  |
| **Emitter Initial Location** | N |  |
| **Emitter Direct Location** | N |  |
| **Seeded Mofules** | N |  |
| **Beam and AnimTrail Renderers** | N |  |
| **Ribbon Renderers** | Partially | Ribbon UVs are not guaranteed to be equivalent for the converted Niagara System. |
| **Cascade Emitter LODs** | Partially | Conversion will only operate on all modules at LOD 0. |

If a Cascade Particle System with unsupported modules or renderers is converted,
the generated Niagara System will log the skipped module or renderer conversion in its Niagara Log Window.

[![Log Conversion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e42ef823-f20d-4768-bdab-24b64e23a833/logconversion.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e42ef823-f20d-4768-bdab-24b64e23a833/logconversion.png)

Click image for full size.

Niagara Log displays a message to indicate which cascade modules have been skipped during the conversion.

## Extending The Capabilities Of Cascade To Niagara Converter Plugin

The plugin supports extending the conversion process by modifying the python scripts located in the Cascade To Niagara Converter plugin's Python directory see:  
`Engine/Plugins/FX/CascadeToNiagaraConverter/Content/Python`.

For users who have created their own custom modules, renderers, and properties in Cascade. New converter scripts for each can be created by extending from the relative interface and adding the new script to the relevant directory, under `CascadeToNiagaraConverter/Content/Python`.
For example, to add support for converting a custom module, create a new script under the `ModuleConversionScripts` directory, and extend a new class in the script from the `ModuleConverterInterface` class. For more details or examples please refer to source code for the associated interface script.

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [plugin](https://dev.epicgames.com/community/search?query=plugin)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)
* [cascade](https://dev.epicgames.com/community/search?query=cascade)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Cascade To Niagara Converter Plugin](/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7#cascadetoniagaraconverterplugin)
* [Enabling The Cascade To Niagara Converter Plugin](/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7#enablingthecascadetoniagaraconverterplugin)
* [Using The Cascade To Niagara Converter Plugin](/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7#usingthecascadetoniagaraconverterplugin)
* [Types Of Errors And Warnings](/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7#typesoferrorsandwarnings)
* [Cascade To Niagara-Supported Conversion Operations](/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7#cascadetoniagara-supportedconversionoperations)
* [Extending The Capabilities Of Cascade To Niagara Converter Plugin](/documentation/en-us/unreal-engine/cascade-to-niagara-effects-converter-plugin-for-unreal-engine?application_version=5.7#extendingthecapabilitiesofcascadetoniagaraconverterplugin)
