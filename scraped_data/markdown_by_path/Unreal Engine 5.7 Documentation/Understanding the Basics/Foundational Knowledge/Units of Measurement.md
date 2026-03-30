<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7 -->

# Units of Measurement

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Foundational Knowledge](/documentation/en-us/unreal-engine/foundational-knowledge-in--unreal-engine "Foundational Knowledge")
7. Units of Measurement

# Units of Measurement

Measure quantities of interest.

![Units of Measurement](https://dev.epicgames.com/community/api/documentation/image/4bc0cd16-c469-460c-8b99-f66d9615f25c?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine (UE) defaults to the following International System (SI) units for measurement:

| **Quantity** | **Unit** |
| --- | --- |
| Distance/Length | Centimeters (cm) |
| Mass | Kilograms (kg) |
| Time | Minutes (min), Seconds (s) |
| Angles | Degrees (deg) |
| Speed/Velocity | Meters per Second (m / s) |
| Temperature | Celsius (C) |
| Force | Newtons (N) |
| Torque | Newton Meters (N • m) |

For more information about all units available in UE, see the [Available Units](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine#availableunits) section below.

### Change Default Units

You can change the units for any of these quantities in your project in the Unreal Editor. To change these units, follow these steps:

1. From the menu bar, select **Edit > Project Settings...** This opens a new **Project Settings** window or tab.
2. Navigate to **Editor > Appearance**.
3. Expand the category under **Units > Advanced**.
4. You should now see all the quantities of measurement along with their units. To change a quantity, select a new unit from the dropdown menu located next to the quantity you wish to change.

[![Change Editor Units](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36cfbd05-918d-4087-acf3-4d9f10f1c08a/change-units.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36cfbd05-918d-4087-acf3-4d9f10f1c08a/change-units.png)

View or change units in Unreal Editor.

Distance/Length, Mass, and Time can use compound units.

### Available Units

The following sections contain lists of all units of measurement available in UE, organized by measured quantity:

#### Distance and Length

| **Unit** | **Abbreviation** |
| --- | --- |
| **SI** |  |
| Micrometers | µm |
| Millimeters | mm |
| Centimeters | cm |
| Meters | m |
| Kilometers | km |
| **Imperial** |  |
| Inches | in |
| Feet | ft |
| Yards | yd |
| Miles | mi |
| Lightyear | ly |

#### Velocity and Speed

| **Unit** | **Abbreviation** |
| --- | --- |
| **SI** |  |
| Centimeters Per Second | cm/s |
| Meters Per Second | m/s |
| Kilometers Per Second | km/s |
| **Imperial** |  |
| Miles Per Hour | mph |

#### Acceleration

| **Unit** | **Abbreviation** |
| --- | --- |
| Centimeters Per Second Squared | cm/s2 |
| Meters Per Second Squared | m/s2 |

#### Angles

| **Unit** | **Abbreviation** |
| --- | --- |
| Degrees | ° , deg |
| Radians | rad |

#### Angular Velocity

| **Unit** | **Abbreviation** |
| --- | --- |
| Degrees Per Second | deg/s |
| Radians Per Second | rad/s |

#### Temperature

| **Unit** | **Abbreviation** |
| --- | --- |
| **Temperature - SI** |  |
| Celsius | C |
| Kelvin | K |
| **Temperature - Imperial** |  |
| Farenheit | F |

#### Mass

| **Unit** | **Abbreviation** |
| --- | --- |
| **Mass - SI** |  |
| Micrograms | µg |
| Milligrams | mg |
| Grams | g |
| Kilograms | kg |
| Metric Tons | t, Mg |
| **Mass - Imperial** |  |
| Ounces | oz |
| Pounds | lb |
| Stones | st |

#### Density

| **Unit** | **Abbreviation** |
| --- | --- |
| **Density - SI** |  |
| Grams Per Cubic Centimeter | g/cm3 |
| Grams Per Cubic Meter | g/m3 |
| Kilograms Per Cubic Centimeter | kg/cm3 |
| Kilograms Per Cubic Meter | kg/m3 |

#### Force

| **Unit** | **Abbreviation** | **In Base Units** |
| --- | --- | --- |
| **Force - SI** |  |  |
| Newtons | N | 1 N = 1 kg • m / s2 |
| Kilograms Force | kgf | 1 kgf = 9.80665 kg • m / s2 |
| Kilogram Centimeters Per Second Squared | kg • cm / s2 |  |
| **Force - Imperial** |  |  |
| Pounds Force | lbf | 1 lbf = 32.174049 lb • ft / s2 |

#### Torque

| **Unit** | **Abbreviation** | **In Base Units** |
| --- | --- | --- |
| **Torque - SI** |  |  |
| Newton Meters | N·m | 1 N·m = 1 kg • m2 / s2 |
| Kilogram Centimeters Squared Per Second Squared | kg • cm2 / s2 |  |

#### Momentum

| **Unit** | **Abbreviation** | **In Base Units** |
| --- | --- | --- |
| **Momentum - SI** |  |  |
| Newton Seconds | N·s | 1 N • s = 1 kg • m / s |

#### Frequency

| **Unit** | **Abbreviation** | **In Base Units** |
| --- | --- | --- |
| **Frequency - SI** |  |  |
| Hertz | Hz | 1 Hz = 1 s-1 |
| Kilohertz | kHz |  |
| Megahertz | MHz |  |
| Gigahertz | GHz |  |
| Revolutions Per Minute | rpm | 1 rpm = 1/60 s-1 |

#### Pixel Density

| **Unit** | **Abbreviation** |
| --- | --- |
| Pixels Per Inch | PPI |

#### Digital Information

| **Unit** | **Abbreviation** |
| --- | --- |
| Byte | B |
| Kilobyte | kB |
| Megabyte | MB |
| Gigabyte | GB |
| Terabyte | TB |

#### Luminous Flux

| **Unit** | **Abbreviation** |
| --- | --- |
| Lumens | lm |

#### Luminous Intensity

| **Unit** | **Abbreviation** |
| --- | --- |
| Candela | cd |

#### Illuminance

| **Unit** | **Abbreviation** | **In Base Units** |
| --- | --- | --- |
| Lux | lx | 1 lx = 1 lm/m2 |

#### Luminance

| **Unit** | **Abbreviation** |
| --- | --- |
| Candela Per Meter 2 | cd/m2 |

#### Time

| **Unit** | **Abbreviation** |
| --- | --- |
| Nanoseconds | ns |
| Microseconds | µs |
| Milliseconds | ms |
| Seconds | s |
| Minutes | min |
| Hours | hr |
| Days | d |
| Months | mo |
| Years | yr |

#### Pressure

| **Unit** | **Abbreviation** | **In Base Units** |
| --- | --- | --- |
| Pascals | Pa | 1 Pa = 1 kg / m • s2 |
| Kilo Pascals | KPa |  |
| Mega Pascals | MPa |  |
| Giga Pascals | GPa |  |

#### Other Units

| **Unit** | **Abbreviation** | **Notes** |
| --- | --- | --- |
| Exposure Value | EV | Describes how much light is in a scene. |
| Percentage | % | Numerical value between 0 and 100. |
| Multiplier |  | Unitless quantity that represents multiples of some base quantity. |
| Unspecified |  | No specified units. |

## More Information

For more information about coordinate systems, see the following resources:

* [The International System of Units](https://www.bipm.org/en/measurement-units)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Change Default Units](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#changedefaultunits)
* [Available Units](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#availableunits)
* [Distance and Length](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#distanceandlength)
* [Velocity and Speed](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#velocityandspeed)
* [Acceleration](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#acceleration)
* [Angles](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#angles)
* [Angular Velocity](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#angularvelocity)
* [Temperature](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#temperature)
* [Mass](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#mass)
* [Density](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#density)
* [Force](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#force)
* [Torque](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#torque)
* [Momentum](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#momentum)
* [Frequency](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#frequency)
* [Pixel Density](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#pixeldensity)
* [Digital Information](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#digitalinformation)
* [Luminous Flux](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#luminousflux)
* [Luminous Intensity](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#luminousintensity)
* [Illuminance](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#illuminance)
* [Luminance](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#luminance)
* [Time](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#time)
* [Pressure](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#pressure)
* [Other Units](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#otherunits)
* [More Information](/documentation/en-us/unreal-engine/units-of-measurement-in-unreal-engine?application_version=5.7#moreinformation)
