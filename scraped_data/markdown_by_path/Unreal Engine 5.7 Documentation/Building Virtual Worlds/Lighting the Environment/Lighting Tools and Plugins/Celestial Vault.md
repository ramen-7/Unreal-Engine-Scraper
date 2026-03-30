<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7 -->

# Celestial Vault

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
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Lighting Tools and Plugins](/documentation/en-us/unreal-engine/lighting-tools-and-plugins-in-unreal-engine "Lighting Tools and Plugins")
8. Celestial Vault

# Celestial Vault

You can use the Celestial Vault plugin to implement a time of day system using an accurate representation of the day and night sky including the solar system.

![Celestial Vault](https://dev.epicgames.com/community/api/documentation/image/5b0d3ec1-3015-4b83-8c56-8950c24eb731?resizing_type=fill&width=1920&height=335)

 On this page

The Sun Moon Day Sequence Actor provided in the **Day Sequence** plugin is ideal for artistic skies, but it lacks the exact locations of the celestial bodies, which are required for more accurate simulation or architectural projects.

This plugin is an implementation of a Day Sequence with more scientific considerations. Ensure you are familiar with Day Sequence before using the Celestial Vault plugin.

The **Celestial Vault** plugin offers the following additional considerations for more accurate representations of the sky:

* A Celestial Vault background considering the Earth's rotation.
* A Starfield where the stars' locations and magnitude are data-driven from official catalogs, or from arbitrary fictional locations.
* Solar System Planets, accurately placed using the VSOP87 equations.
* The Moon, with its appropriate phases based on the Ephemeris. (Manual Control is still possible.)
* All lighting units are set according to the real-life physical units, with a large luminance difference between Day and Night.

The focus has been set on the Solar System as seen from the Earth, using the same Geocentric approach as Plato. A Heliocentric approach allowing travel between planets has not yet been considered.

## Enabling Celestial Vault Day Sequence in a Project

To start using the Celestial Vault Day Sequence Actor in your scene, you must first enable the Celestial Vault plugin for your project. You can find it in the Plugins browser located in the Edit menu.

[![Enable the Celestial Vault Plugin](https://dev.epicgames.com/community/api/documentation/image/7d40c83e-3669-4c17-beb5-25a5e919d449?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d40c83e-3669-4c17-beb5-25a5e919d449?resizing_type=fit)

Enable the Celestial Vault Plugin

There is no need to add the DaySequence Plugin; an automatic dependency is defined.

This plugin is not dependent on the Georeferencing plugin, but both can be used together. Just make sure you set the same georeferencing location in the GeoReferencing and CelestialVaultDaySequence Actors.

## Working with the Celestial Vault Day Sequence Actor

While the Celestial Vault Day Sequence Actor is based on the same concept as a Day Sequence Collection Asset, this sequence has limited options to ensure that the sky's behavior stays consistent with reality.

The different objects related to the sky will be driven by a **Procedural Celestial Vault Sequence** that will read the shared properties in the Celestial Vault Day Sequence Actor.

Therefore, make sure that this Celestial Vault Sequence is not assigned to another type of DaySequence actor.

This procedural sequence accounts for the following considerations:

* The Celestial Vault rotates around the Earth's rotation axis in 24 hours.
* The Stars have a fixed location relative to the Vault.
* The Planets are located at the right position. (Because of their slow motion, we make the assumption that they won’t be moving during the Day Sequence.)
* The Moon is following its sidereal motion. (Moves eastward by about 13 degrees against the background stars, and rises about 50 minutes later each day.)
* The proper Moon phase is represented. (For simplicity, it’s assumed that it’s constant over one day, which is not the case in reality.)
* The Sun is following its trajectory in the sky.

### Notes on current limitations

Some Celestial equations have been simplified for performance, and even if the accuracy is quite good (fractions of a degree), this system is not guaranteed to provide exact or ultra-accurate locations.

* The precession/nutation effect of the Earth's Axis is not simulated

  + The RA, DEC coordinates are those of the J2000 Epoch, and not those of the date.
* The DaySequence System is looping over one single day.

  + Because of its sidereal motion, the Moon will jump over its previous location when passing midnight.
* The VSOP87 equations use just a limited number of Coefficients, except for the Earth and Moon. The planets' locations are approximate.
* The Eclipse use cases (Solar / Lunar) have not been considered.
* The SkyAtmosphere component considers the Earth as a spherical object with a fixed radius. When working with accurate geospatial data using the WGS84 ellipsoid as a reference, the radii matching is not possible. The recommended workaround is to set the SkyAtmosphere radius to have the right one around the UE World origin, and when the camera is far from the origin, dynamically change this radius.
* Having a Geocentric ECEF frame (Origin at Earth’s center) is not possible yet.

These limitations may improve in future iterations of the plugin.

## Celestial Vault Day Sequence Actor

### Adding the actor to the World

The Celestial Vault Day Sequence Actor is a preconfigured complete day and night cycle that you can drag and drop into your level. It requires no additional setup to be fully functioning.

Follow these steps to get started:

1. Create a new blank level or open an existing level. If your level already has environment lighting components—directional lights, Sky Light, Sky Atmosphere, Volumetric Clouds, and Global Post-Process Volume—these should be removed.
2. From the main toolbar of the level editor, click Create and drag a Celestial Vault Day Sequence Actor into the scene from the All rollout category.

[![Create Celestial Vault Day Sequence Actor](https://dev.epicgames.com/community/api/documentation/image/d085c61f-ba18-4f21-91ab-7d41ef625e18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d085c61f-ba18-4f21-91ab-7d41ef625e18?resizing_type=fit)

Create Celestial Vault Day Sequence Actor

This system uses physically accurate units for the lights' intensities and bodies' luminances. There is a huge dynamic range between night and Day (EV100 ranging from -7 to 14).

To accommodate this, special values of the HDR Eye adaptation and Local Exposure settings are needed. The actor already includes a preconfigured Postprocess Volume Component of infinite extent.

You can use it for your project, but if you want to have your own, make sure that you disable this one. Either the actor or the various materials allows you to work with other fake units.

|  |  |
| --- | --- |
|  |  |

And because the eye adaptation will take a while to adjust, consider increasing the Speed Up and Speed Down values when working.

### Working with the actor properties

Once the Celestial Vault Day Sequence Actor has been added to the level, you’re free to change any value from its components. But some of them will be driven by the procedural sequence, so it’s normal that the edition of some of them is locked.

Likewise, the Celestial Vault Day Sequence Actor always needs to be located at the World Origin. You should not change its location.

All the properties driving that you need to control are part of the actor itself:

#### Date & Location

[![Date and Time Settings](https://dev.epicgames.com/community/api/documentation/image/afc650cc-22d0-41ca-8ff5-c6416e13a493?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afc650cc-22d0-41ca-8ff5-c6416e13a493?resizing_type=fit)

Date and Time Settings

| Property | Description |
| --- | --- |
| Use Current Date | When checked, the system will be initialized with the Year, Month, and Day of your computer. It won’t consider your Time Zone or Daylight Saving time, though. |
| Year | A Year to display the sky for |
| Month | A Month to display the sky for |
| Day | A Day to display the sky for  Note that a Time is not required, since it’s defined by the TOD Time scrubber. This is supposed to be the Local Time at the location. |
| GMT Time Zone | Manually enter your Time Zone here; it’s not automatically populated from the location. |
| Is Daylight Savings | Manually check if you’re in daylight saving (Summer). It’s not automatically computed from your local date. |
| Latitude | Latitude on Earth of the point corresponding to your World Origin. |
| Longitude | Longitude on Earth of the point corresponding to your World Origin. |
| GMST at ToD 0 [Read Only] | Gives the Greenwich Mean Sidereal Time corresponding to t=0 (beginning of the day) for the current Date. |
| Planet Center Transform [Read Only] | To simplify the animations, all components are parented to a SceneComponent with a properly configured Transform, which is located at the planet's center and oriented towards its rotation axis.  The rotation of this component will simulate the planet's rotation. |

[![Example Results](https://dev.epicgames.com/community/api/documentation/image/9fad4a6c-31e6-4354-9657-216c51df4335?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9fad4a6c-31e6-4354-9657-216c51df4335?resizing_type=fit)

The sky on April 25th, 2025 - 5:00 am - “The Smiley Face"

#### Stars

| Property | Description |
| --- | --- |
| Celestial Stars Catalog | The input data table to use for actual stars with celestial properties. |
| Fictional Stars Catalog | The input data table to use for fictional stars with basic properties. |
| Max Visible Magnitude | All stars whose magnitude is higher than this threshold will be ignored at generation time.  Low magnitudes mean bright stars. The naked eye can normally see only up to magnitude 6. A higher threshold will generate more stars, but they might not be visible, unless you artificially boost their visibility with the Stars Material. |
| Keep Stars Info | When checked, a Table will be generated and kept in memory to allow for querying the stars' data.  If you’re only interested in the visual representation, keep it unchecked. |

At generation time, both Catalogs are merged into one single ISM Component for rendering. However, because fictional stars don’t have the same details, each has a different DataTable Format:

DataTables for Celestial Stars must be of CelestialStarInputData Type

DataTables for Fictional Stars must be of StarInputData Type

If you use the wrong format, you’ll have a Warning in the Message log, and the corresponding stars won’t be generated.

Some base Data Tables are provided in the Engine/Plugins/CelestialVault/Data Folder.

[![Data Folder](https://dev.epicgames.com/community/api/documentation/image/0a38c4fb-3434-44f1-b617-6e0fbb9ce15a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a38c4fb-3434-44f1-b617-6e0fbb9ce15a?resizing_type=fit)

Data Folder

##### Celestial Stars

Celestial stars are stars coming from official catalogs. They contain lots of information that can be queried later. A Celestial Star catalog can be imported from CSV files, as long as it contains the fields of the CelestialStarInputData type:

* **ID**: Unique ID [1 to n]
* **Name**: Star Name - Can be empty
* **RA**: Right Ascension - Expressed in Hours (1 Hour = 15°)
* **DEC**: Declination - Expressed in Degrees
* **DistanceInPC**: Distance - Expressed in Parsec
* **Magnitude**: Generally [-2 to 13]
* **ColorIndex**: Also known as B-V, it represents the Star Color [-0.33 to 2.0]
* **HipparcosID**: Star ID in the Hipparcos Catalog - Can be empty
* **HenryDraperID**: Star ID in the Henry Draper Catalog - Can be empty
* **YaleBrightStarID**: Star ID in the Yale Bright Star Catalog - Can be empty

Two Data Tables are provided with the plugin

* DT\_HYGCatalog\_Full - The full HYG catalog of the Astronomy Nexus page. It contains 120000 star records.
* DT\_HYGCatalog\_10K - Same HYG catalog, but limited to the 10000 brightest stars (up to magnitude 6). Sufficient for most use cases.

[![Example Result](https://dev.epicgames.com/community/api/documentation/image/76e2bbd4-51c6-423e-9a3e-38a7eebbff65?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76e2bbd4-51c6-423e-9a3e-38a7eebbff65?resizing_type=fit)

The Full HYG Catalog over a desert landscape.

##### Fictional Stars

Fictional stars are meant to be simpler and user-crafted. They use the same concept of a Catalog, but as only the visual part is needed, the Data Table needs to contain only a simplified set of fields, of the StarInputData Type:

* **ID**: Unique ID [1 to n]
* **Name**: Star Name - Can be empty
* **RA**: Right Ascension - Expressed in Hours (1 Hour = 15°)
* **DEC**: Declination - Expressed in Degrees
* **Magnitude**: Generally [-2 to 13]
* **Color**: Linear RGB Color String formatted as “(R=0.924,G=0.114,B=1.)”

Two Data Tables are provided with the plugin

* DT\_FictionalStars - A simple example for randomly-placed stars
* DT\_FictionalEasterEgg - A more advanced example of a constellation with an easter-egg shape.

Creating your own catalog of fictional stars is outside the scope of this documentation, but some open-source computer vision software can easily extract pixel coordinates from a set of dots, and with a little bit of spreadsheet magic, CSV files can be created, allowing you to do fancy experiments.

[![](https://dev.epicgames.com/community/api/documentation/image/8fde1323-ec78-47ab-9c64-86005ee001e5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8fde1323-ec78-47ab-9c64-86005ee001e5?resizing_type=fit)

##### Importing your own CSV File

Star catalogs can be imported with CSV files like these:

[![](https://dev.epicgames.com/community/api/documentation/image/c1f2d454-07e9-4743-8ef3-5b2da9ac3287?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c1f2d454-07e9-4743-8ef3-5b2da9ac3287?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/f4b05d8e-800d-43ae-bfdf-7734d3991e82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f4b05d8e-800d-43ae-bfdf-7734d3991e82?resizing_type=fit)

You can also export one of the provided Data Tables as CSV to have a starting template.

1. Drag and drop the CSV File onto your content browser.
2. Make sure you select the appropriate CelestialStarInputData/StarInputData Row Type corresponding to the content you’re importing.
3. Check the various input options if you have other fields in your dataset.
4. Make sure you name the proper field that will be used as the primary key. (here ID)

[![](https://dev.epicgames.com/community/api/documentation/image/1b959710-3480-4c1d-a74a-49305f80812f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b959710-3480-4c1d-a74a-49305f80812f?resizing_type=fit)

#### Planets

[![](https://dev.epicgames.com/community/api/documentation/image/ee4471e6-0464-4ff3-a8a0-630bec086265?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee4471e6-0464-4ff3-a8a0-630bec086265?resizing_type=fit)

| Property | Description |
| --- | --- |
| Planets Catalog | The input data table contains the planets' properties. |
| Planets Scale | An artificial scale factor to apply to planets |
| Keep Planets info | When checked, a Table will be generated and kept in memory to allow for querying the planets’ data.  If you’re only interested in the visual representation, keep it unchecked. |

Currently, the focus is on the Solar System planets. The VSOP87 ephemeris simulates their exact trajectories. The system also allows for arbitrary planets, using Elliptical trajectories, but it has not been implemented yet.

A Data Table for Planets needs to contain the following fields:

* **ID**: Unique ID [1 to n]
* Name: Planet Name - Can be empty
* **OrbitType**: Enum for Solar Planets orbits. Elliptic is unused yet.
* **Radius**: Planet radius (km)
* **TextureColumnIndex**: Index of the planet texture in the global planets Atlas.

The planets are rendered using plane impostors, with a shader scaling them so that they always have a minimum size in pixels on screen. The Planets Scale property effect is visible only if the planet's true size is above this pixel size, depending on its radius, distance, and camera FOV.

[![Results](https://dev.epicgames.com/community/api/documentation/image/db99cc3d-840f-4769-a12f-3ecd9901a87b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db99cc3d-840f-4769-a12f-3ecd9901a87b?resizing_type=fit)

Saturn with some stars in the background

#### Moon

The system is currently limited to Earth’s moon only, so options are limited.

[![](https://dev.epicgames.com/community/api/documentation/image/7dd7df16-f654-448a-be6c-5efa13f42c94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7dd7df16-f654-448a-be6c-5efa13f42c94?resizing_type=fit)

| Property | Description |
| --- | --- |
| Moon Scale | An artificial scale factor to apply to the Moon |
| Manual Control | By default, Moon location and Phase are computed from the Date and Location Values.  By checking this box, you can enable additional options (see note below) |
| Moon Age | Correspond to the Moon’s lunar age: 0 = New Moon, 0.25 = First Quarter, 0.5 = Full Moon, 1.0 = Next New Moon. |
| Moon offset to Sun’s Right Ascension | Horizontal offset of the Moon location relative to the sun, in hours. (1 hour = 15°).  If this offset is 3h, the Moon will follow the Sun with a 45° offset, passing the horizon 3 hours after the Sun. |
| Moon offset to Sun’s Declination | Vertical offset of the Moon location relative to the sun, in Degrees. |

By default, the Moon location and phase are automatically computed, and nothing has to be done. But in some Training & Simulation use cases, it’s important to control the brightness at night, because visibility during a dark night or during a light night is very different!

Finding the exact day on a calendar that would put the Moon in the right phase and at the right position is often cumbersome, so the Manual Control option helps to cover this use case.

Having an offset to the Sun is the easiest way to do this from a user perspective. It’s intuitive, whatever your hemisphere, your latitude, the current day duration…

But note that it can have uncontrolled visual effects that you should be aware of: Let’s say you set an offset of 3h. The Moon will be on “the left side” of the Sun. In this case, the Sun light should produce a waxing crescent. So, avoid setting a Moon age value over 0.75. In the extreme case, you could have a full Moon located close to the Sun, which never happens. Take care of this if you want to have a minimum of realism.

Because of the requirement for Manual control, the Moon is rendered using a plane with a custom material rather than a 3D Sphere.

[![](https://dev.epicgames.com/community/api/documentation/image/53c888af-cdcc-49c2-b828-b69fb102db2a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/53c888af-cdcc-49c2-b828-b69fb102db2a?resizing_type=fit)

A Waning crescent over the Alps

#### Advanced

The sky is rendered as a Sphere, with a set of different layers of smaller radii for the different celestial bodies, by decreasing range: The vault background, the stars, the planets, and the moon.

They need to be far from the planet to avoid parallax effects, but far away enough together to avoid depth-fighting. The advanced properties allow tuning the various object ranges.

It also enables you to set the base values for Sun and Moon directional lights.

| Property | Description |
| --- | --- |
| Celestial Vault distance | Radius (km) of the sphere that will be mapped with the background texture (Milky Way, constellations, or celestial grid lines) |
| Stars Vault percentage | Percentage of the Vault Sphere radius where the Stars will be generated. |
| Planets Vault percentage | Percentage of the Vault Sphere radius where the Planets will be generated. |
| Moon Vault percentage | Percentage of the Vault Sphere radius where the Moon will be generated. |
| Sunlight Intensity | Physically correct Sun light intensity (default: 120000 Lux) |
| Moonlight Intensity | Physically correct Moon light intensity (default: 0.1Lux) |

Note on Lights and Eye Adaptation:

This system has been designed with physical accuracy in mind, and default values have been set automatically.

The Sun and Moon Lights have been defined as Atmosphere Lights, Index 0 for the Sun, Index 1 for the Moon.

The Sun intensity of 120000 Lux implies a white surface luminance on the ground of around 8000-12000 cd/m² at noon

The Moon's base intensity has been set to 0.1 Lux, which is the average for a full moon. The literature gives ranges between 0.05 and 0.1 Lux, up to 0.32 Lux for a Super Moon, so feel free to adjust! It implies a white surface luminance on the ground of around 0.01-0.02 cd/m².

We reduce this base intensity depending on the phase, so it can go very low when no artificial light is around.

The Moon's surface is usually very bright! (~1000-2500 cd/m²), Looking at the Moon during a full moon will be dazzling.

Because of this huge range, the default values for the Eye adaptation had to be tuned too.

The MinEV100 has been set to -0.5, so that we see a clear night with a Full Moon, but a dark environment on a New Moon.

The histogram-based eye adaptation is not enough to cope with such a brightness range, especially if the moon size on screen is small. So we set a Local Exposure Highlight Contrast Curve to accommodate the Moon's brightness.

All these specific settings are part of a Global Post Process volume associated with the actor.

The system also handles cloud coverage for lighting, shadowing, and fogging objects. Both Sun and Moon Lights are set to Cast Shadows and Cloud Shadows, which has a performance impact. Feel free to disable it if you don’t need it.

### Tuning the Sky's appearance

The system is provided with Material Instances for all components, which you’re free to replace with your own. This paragraph will describe the properties of the Material instances.

Note that changing the brightness/intensity values of Materials will probably imply changing the Eye Adaptation or Exposure settings.

If you plan to change these materials, please use copies in your project content rather than
changing the originals.

#### Celestial Vault

The MI\_CelestialVault material is a multi-texture material that also contains the sun halo.

| Property | Description |
| --- | --- |
| Global Intensity | Brightness factor of the whole Celestial Vault (Background + Constellations + Celestial Grid) |
| Background Intensity | Brightness factor of the sole Background texture (Milky Way) |
| Background Texture | Replacement texture for the Vault background. Needs to be in Celestial Coordinates. |
| Show Constellations | Enables an additional texture layer with a Constellation Map (white) |
| Constellations Color | Tint color of the constellation |
| Constellations Intensity | Brightness factor of the sole Constellations texture |
| Constellations Texture | Replacement texture for the Constellations. Needs to be in Celestial Coordinates. |
| Show Celestial Grid | Enables an additional texture layer with a Celestial Grid Map (white) |
| Grid Color | Tint color of the Celestial Grid |
| Grid Intensity | Brightness factor of the sole Celestial Grid texture |
| Grid Texture | Replacement texture for the Celestial Grid. Needs to be in Celestial Coordinates. |

Medium textures a provided with the system, but you can find higher resolutions here: https://svs.gsfc.nasa.gov/4851/

[![](https://dev.epicgames.com/community/api/documentation/image/1b821acc-7c95-45e6-a097-5230c745a07a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b821acc-7c95-45e6-a097-5230c745a07a?resizing_type=fit)

Constellation lines and Celestial Grid

#### Stars

The MI\_Stars material is used to texture the Stars' individual planes, rendering them as an Instanced Static Mesh component. It contains options for the stars' appearance and size.

##### Appearance

| Property | Description |
| --- | --- |
| Desaturation | Stars are all rendered using a per-instance color, manually set for the fictional stars, computed from the B-V value for celestial stars.  This setting allows to desaturate the Value of the color (0=untouched, 1=grayscale only) |
| Magnitude Offset | The star's brightness is computed from its Magnitude. This parameter allows for artificially increasing the star's brightness by shifting its theoretical magnitude.  Negative values lower the magnitude and therefore increase brightness. Brightness is an exponential factor of Magnitude. |
| Mask | Texture Mask used for the Stars. See T\_StarMask\_\* for more masks |
| Mask Falloff | Exponential value applied to the Mask color and alpha to increase/decrease the contrast |

##### Base Size

Stars' brightness is not sufficient to see them; they need to be of a minimal size on screen, possibly above 1 pixel, to avoid upscaling artifacts.

Whereas Brightness is an exponential factor of Magnitude, the star size on screen can be a linear function, defined by magnitude/size pairs. (Clamped over the range limits)

| Property | Description |
| --- | --- |
| Brightest Star Magnitude | Reference magnitude of the Brightest star. Stars below this magnitude will still have the maximum size. |
| Brightest Star Size (pixels) | Reference Pixel Size for Stars of Brightest magnitude. Lower magnitude stars will have an interpolated size towards the faintest Star settings. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling Celestial Vault Day Sequence in a Project](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#enablingcelestialvaultdaysequenceinaproject)
* [Working with the Celestial Vault Day Sequence Actor](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#workingwiththecelestialvaultdaysequenceactor)
* [Notes on current limitations](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#notesoncurrentlimitations)
* [Celestial Vault Day Sequence Actor](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#celestialvaultdaysequenceactor)
* [Adding the actor to the World](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#addingtheactortotheworld)
* [Working with the actor properties](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#workingwiththeactorproperties)
* [Date & Location](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#date&location)
* [Stars](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#stars)
* [Celestial Stars](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#celestialstars)
* [Fictional Stars](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#fictionalstars)
* [Importing your own CSV File](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#importingyourowncsvfile)
* [Planets](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#planets)
* [Moon](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#moon)
* [Advanced](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#advanced)
* [Tuning the Sky's appearance](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#tuningthesky'sappearance)
* [Celestial Vault](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#celestialvault)
* [Stars](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#stars-2)
* [Appearance](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#appearance)
* [Base Size](/documentation/en-us/unreal-engine/celestial-vault-plugin-for-unreal-engine?application_version=5.7#basesize)
