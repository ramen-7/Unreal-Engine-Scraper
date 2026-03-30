<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7 -->

# Simulating Waves Using The Water Waves Asset

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Water System](/documentation/en-us/unreal-engine/water-system-in-unreal-engine "Water System")
7. Simulating Waves Using The Water Waves Asset

# Simulating Waves Using The Water Waves Asset

An overview of how to use the Water Waves Asset to drive wave simulation.

![Simulating Waves Using The Water Waves Asset](https://dev.epicgames.com/community/api/documentation/image/ba9649f9-012a-43e0-ac4f-400bb433a6d2?resizing_type=fill&width=1920&height=335)

 On this page

The Water system uses GPU-driven wave data to simulate the surface of waves on Water Body Actors. The **Water Waves** Asset provides the individual wave parameters that are governed by its simulation model.

## Creating a Water Waves Asset

Water Bodies are supplied with a wave simulation model to use with a **Water Waves Asset** assignment slot. By default, one is already supplied that uses the [Gerstner wave simulation model](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine#gerstnerwaterwavesproperties).

While you do not need to create a new Water Wave Asset every time you use a Water Body, there are times when you want different types of wave input from the simulation model to behave differently, or when you want to use a completely different wave simulation model.

You can create your own Water Waves Asset using the Content Browser to click **Add/Import** or use the **Right-Click Context Menu**. From the menu, select **Water > Water Waves**.

On a selected **Water Body**, use the **Water Waves Asset** assignment slot to apply this asset.

[![Content Browser Context Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b33a84f-2343-4881-9435-5d3f4d6b9106/01-water.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b33a84f-2343-4881-9435-5d3f4d6b9106/01-water.png)

Click image for full size.

[![Water Body](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0becaf3-64be-4b0e-9c10-6197451b6b54/02-water-waves.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0becaf3-64be-4b0e-9c10-6197451b6b54/02-water-waves.png)

Click image for full size.

[![Water Wave Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39419df4-51e4-4339-9238-dedd60ea0041/03-water-waves-asset.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39419df4-51e4-4339-9238-dedd60ea0041/03-water-waves-asset.png)

Click image for full size.

### Editing the Water Waves Asset

When creating, or opening an existing, Water Wave Asset, you select the type of wave simulation to be used, when multiple simulation models are available to choose from. Any editable properties will populate the panel to configure the simulation.

[![Water Wave Asset Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9e687dc-7696-493c-a05b-b32fa3133a1d/04-water-wave-asset-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9e687dc-7696-493c-a05b-b32fa3133a1d/04-water-wave-asset-editor.png)

Click image for full size.

Water Waves Asset Editor using Gerstner Water Waves simulation model.

The **Waves Source** specifies the wave simulation model that is to be used for generating waves on Water Bodies. When one is selected, it provides parameters that are exposed through the selected **Waves Source** file to control the wave simulation. For example, the **Gerstner Water Waves** source provides parameters under the **Gerstner Wave Generator**.

You can configure these parameters to define the look of the wave simulation on any Water Bodies placed in the Level that have this Water Wave Asset assigned to them.

Unreal Engine only provides the Gerstner wave simulation model. However, you can implement other models or your own by using Blueprint or C++ code as a function that outputs waves based on some specified input. See the [Adding Your Own Wave Simulation Model and Wave Generator](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine#addingyourownwavesimulationmodelandwavegenerator) section of this page for more details.

## Gerstner Water Waves Properties

The **Gerstner Water Waves** simulation model provides the following parameters for wave simulation.

[![Water Wave Asset Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/793338eb-ec02-4434-8a1d-72ca3e600e65/05-water-wave-asset-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/793338eb-ec02-4434-8a1d-72ca3e600e65/05-water-wave-asset-settings.png)

Click image for full size.

| Property | Description |
| --- | --- |
| Default |  |
| **Num Waves** | The number of waves to be summed up. |
| **Seed** | A deterministic starting point for generating a random value to feed the wave model. |
| **Randomness** | Adds some amount of randomness to the interpolation between the minimum and maximum wavelength and amplitude values used by the Gerstner Water Waves model.. |
| Wavelengths |  |
| **Min Wavelength** | Specifies the low-end of the wavelength range between waves that have a specified falloff. |
| **Max Wavelength** | Specifies the high-end of the wavelength range between waves that have a specified falloff. |
| **Wavelength Falloff** | Uses the minimum and maximum wavelengths to determine the distance between wave crests on a continuous wave. |
| Amplitude |  |
| **Min Amplitude** | Specifies the low-end of all generated waves' amplitude with a specified falloff. |
| **Max Amplitude** | Specifies the high-end of all generated waves' amplitude with a specified falloff. |
| **Amplitude Falloff** | Uses the minimum and maximum amplitudes to determine the height of generated waves. |
| Directions |  |
| **Dominant Wind Angle** | Set the primary direction from which the wind is blowing. |
| **Dominant Angular Spread** | Sets a random wind direction within the specified angle that the window should blow. Waves will appear to travel in this direction. |
| Steepness |  |
| **Small Wave Steepness** | Specifies the steepness of smaller waves with a specified falloff. The steepness determines how sharp the point of the wave crest becomes. This is achieved through lateral motion and controls how much the waves move side-to-side. |
| **Large Wave Steepness** | Specifies the steepness of larger waves with a specified falloff. The steepness determines how sharp the point of the wave crest becomes. This is achieved through lateral motion and controls how much the waves move side-to-side. |
| **Steepness Falloff** | Uses the small and large wave steepness values to determine the height range of wave crests that occur. |

The Water system's mesh rendering system for surface detail is ideal for defining the macro movement patterns and look of waves. The micro details are best handled using the water material with normal maps where the tessellation of the mesh is limited by the balance of quality and performance.



Material-driven details have been disabled in the demonstrations that follow to demonstrate the macro-level detail that is achievable using the Water Wave Asset alone.

### Setting the Number of Waves and Randomness

The **Default** category of parameters define the overall look of the Lake and Ocean Water Bodies.

The **Num Waves** parameter specifies the number of waves. This creates the overall look of the waves that are formed. By default 16 waves are used. Using fewer waves is more performant, but offers less variation in the randomness of waves colliding.

The **Seed** parameter creates a deterministic starting point for a random value, which is passed to the wave simulation algorithm to create variations with the waves. The **Randomness** parameter feeds random values to the minimum and maximum wavelength and amplitude values, to reduce repeating patterns in the wave simulation.

### Wavelength of the Waves Simulation

The **Wavelengths** parameters specify a minimum and maximum value range for the distance between waves when a falloff value is used. The Seed and Randomness values work together with the Wavelength minimum and maximum value ranges to further define the look of the water surface.

### Amplitude of the Waves Simulation

The **Amplitude** parameters specify a minimum and maximum value range for height displacement between waves. This controls the peaks and valleys of the wave crests. The Seed and Randomness values work together with the Amplitude minimum and maximum value ranges to further define the look of the water surface.

### Direction and Angular Spread of Wind

The **Directions** parameters specify the direction wind is traveling. With the **Dominant Wind Angle**, the wind will push the waves in the wind's general direction.The **Dominant Angular Spread** specifies a secondary angle that waves move along while traveling in the direction set by the Dominant Wind Angle.

### Steepness of the Waves Simulation

The **Steepness** parameters define how pointed or rounded the cresting waves become. The steepness of the wave crests is achieved through lateral motion, and controls how much the waves move side-to-side.

Small steepness values have softer, rounded wave crests. Large steepness values have sharper wave crests. These values provide random wave interactions that produce both softer and sharper wave crests without all wave crests being completely soft or sharp.

## Adding Your Own Wave Simulation Model and Wave Generator

Unreal Engine provides the Gerstner wave simulation model for the Water System. The Water system is capable of supporting additional wave simulation models through the Water Wave Asset with configurable parameters, which can be done either through C++ code or Blueprint.

The information in this section uses the Gerstner wave implementation as a working example for creating your own wave generator backend for evaluating surface waves.

In C++, you would start by creating a new type that derives from `UGerstnerWaterWaveGeneratorBase` and uses `GenerateGerstnerWaves_Implementation(TArray<FGerstnerWave>&OutWaves) const`.

In Blueprint, the Parent Class inherits from the **GerstnerWaterWaveGeneratorBase** class.

[![Blueprint Class Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f128bbe-d17d-427f-9675-86a90231b7bd/12-blueprint-class-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f128bbe-d17d-427f-9675-86a90231b7bd/12-blueprint-class-button.png)

Click image for full size.

[![Gerstner Wave Asset Class](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fde8cd1e-ea3b-4304-9385-9e3cab85cb6c/13-gerstner-wave-asset-pick-class.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fde8cd1e-ea3b-4304-9385-9e3cab85cb6c/13-gerstner-wave-asset-pick-class.png)

Click image for full size.

[![Gerstner Water Wave Generator Base](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/293ee1c9-5884-46de-b757-0bb7107fec63/14-gerstner-water-wave-generator-base.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/293ee1c9-5884-46de-b757-0bb7107fec63/14-gerstner-water-wave-generator-base.png)

Click image for full size.

In the Blueprint, you override and add your own Generate Gerstner Waves function that uses the **Make GerstnerWave** and **Make GerstnerWaveOctave** nodes to output to an array that stores information.

[![Gerstner Generator Wave Function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/305a11c8-9fb1-4161-bd84-7fc77befdbbc/15-gerstner-generator-waves-function.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/305a11c8-9fb1-4161-bd84-7fc77befdbbc/15-gerstner-generator-waves-function.png)

Click image for full size.

[![BP Custom Wave Simulation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a027ea63-6266-4751-9e4a-62c616f05295/16-bp-custom-wave-simulation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a027ea63-6266-4751-9e4a-62c616f05295/16-bp-custom-wave-simulation.png)

Click image for full size.

In the Water Waves Asset, the **Gerstner Wave Generator** selection dropdown lists any classes that inherit from the Gerstner Wave Source.

[![BP Custom Gerstner Wave Generator](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cbf27154-0ac4-4494-8d0d-b56d082cccbc/17-bp-custom-gerstner-wave-generator.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cbf27154-0ac4-4494-8d0d-b56d082cccbc/17-bp-custom-gerstner-wave-generator.png)

Click image for full size.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [water](https://dev.epicgames.com/community/search?query=water)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [level editing](https://dev.epicgames.com/community/search?query=level%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Water Waves Asset](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#creatingawaterwavesasset)
* [Editing the Water Waves Asset](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#editingthewaterwavesasset)
* [Gerstner Water Waves Properties](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#gerstnerwaterwavesproperties)
* [Setting the Number of Waves and Randomness](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#settingthenumberofwavesandrandomness)
* [Wavelength of the Waves Simulation](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#wavelengthofthewavessimulation)
* [Amplitude of the Waves Simulation](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#amplitudeofthewavessimulation)
* [Direction and Angular Spread of Wind](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#directionandangularspreadofwind)
* [Steepness of the Waves Simulation](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#steepnessofthewavessimulation)
* [Adding Your Own Wave Simulation Model and Wave Generator](/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine?application_version=5.7#addingyourownwavesimulationmodelandwavegenerator)
