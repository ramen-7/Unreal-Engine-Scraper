<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7 -->

# Sun and Sky Actor

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
8. Sun and Sky Actor

# Sun and Sky Actor

A tool that provides a time of day system that is geographically accurate for location, date, and time.

![Sun and Sky Actor](https://dev.epicgames.com/community/api/documentation/image/80144f52-3864-4e01-96ff-f73be34f136c?resizing_type=fill&width=1920&height=335)

 On this page

The **Sun Position Calculator** plugin includes a [Geographically Accurate Sun Positioner](/documentation/en-us/unreal-engine/geographically-accurate-sun-positioning-tool-in-unreal-engine) that gives you fine control over the Sun's position based on a geographic location and date in time. The **SunSky** Actor is part of this same plugin. It uses the same mathematical equations to govern the position of the Sun in the sky and includes a bundle of components—a **Directional Light**, **Sky Light**, and **SkyAtmosphere**—to produce true-to-life renderings that show realistic patterns of sunlight and shadow.

The **SunSky** Actor makes it simple and quick to set up your scenes no matter your aesthetic choice, with settings for Daylight Saving Time (DST), the date, and the time of day. It's designed to work well within games and other industries, like our Architectural, Engineering and Construction (AEC), or Automotive, Product Design and Manufacturing.

## Project Templates and Setup

When [creating a new project,](/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine) you can select from different industry types and templates relevant to your needs.

Depending on the template you choose, some properties are enabled/disabled by default. These properties affect the look and functionality of the SunSky Actor.

Keep the following in mind when choosing a **Template Category** and **Template**:

* The project setting for **Extend default luminance range in Auto Exposure settings** is required for this SunSky Actor to display correctly without editing its properties.
* Some templates for each template category enable the Sun Position Calculator by default. You can verify this by going to the **main menu** and selecting **Edit > Plugins** and searching for the plugin once you've opened a new project.

This page demonstrates how to use the Sun and Sky Actors within the ArchVis Unreal Engine (UE) Template. To use this template, simple create a new project, select the **Architecture, Engineering, and Construction** New Project Category, and select the ArchVis template.

## Enabling the Sun Position Calculator Plugin

1. From the main menu, choose **Edit > Plugins**.
2. Find the **Sun Position Calculator** plugin under the **Misc** category and check it's **Enabled** checkbox.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4562ebd8-ef0f-4839-b5c1-df44d2c09f39/01-sunsky-plugin-enable-plugin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4562ebd8-ef0f-4839-b5c1-df44d2c09f39/01-sunsky-plugin-enable-plugin.png)

   Click image for full size.
3. Click the **Restart Now** button to apply your changes and re-open the Unreal Editor.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c7aad208-2e49-480d-86ed-ba25f0f04658/02-sunsky-plugin-rerun-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c7aad208-2e49-480d-86ed-ba25f0f04658/02-sunsky-plugin-rerun-editor.png)

   Click image for full size.

## Using the Sun and Sky Actor

Once you've enabled the Sun Position Calculator plugin, you'll find a new Actor called **Sun and Sky** available in the Editor **Place Actors** panel in the **Lights** tab.

![New Actor called Sun and Sky available in the Place Actors panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ffedf4b-c3a8-4f9d-8b78-a8f4e146f552/03-sunsky-plugin-available-actor.png)

Drag it into the Level viewport.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f34cb2b-6102-49e8-9061-d5c15af5201d/04-sunsky-plugin-place-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f34cb2b-6102-49e8-9061-d5c15af5201d/04-sunsky-plugin-place-actor.png)

Click image for full size.

When adding a SunSky Actor to your scene, it's best to remove any Directional Light, Sky Light, or SkyAtmosphere components that are already there. Otherwise, it's best to start with a new Blank Level if you're starting from scratch.



When you drag a SunSky Actor into the Level and it appears bright white, you can do one of two things:

* Enable **Extend default luminance range in Auto Exposure settings** in the Project Settings under the Rendering category (under the Default section).

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1c115e9-ac88-45c8-b107-9dcb93f09aa5/05-sunsky-plugin-project-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1c115e9-ac88-45c8-b107-9dcb93f09aa5/05-sunsky-plugin-project-settings.png)

  Click image for full size.
* Or, if you don't want this project setting to affect the look of your project, you can select the SunSky Actor's Directional Light and use a lower Lux intensity (open the SunSky actor, select the Directional Light under Components, locate the Light section in the Details pane, lower the Intensity until you're happy).

  ![Set up an Intensity of the Directional Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c5a6a96-3f8b-4d80-a2c2-28abd960bd6f/06-sunsky-plugin-intensity.png)

The SunSky Actor contains movable Actors for Directional Light, SkyLight, and SkyAtmosphere components as part of its Blueprint. When the scene component **SunSky(Self)** is selected, the exposed Blueprint properties that can be set—such as those for date, time of day, latitude and longitude—are displayed. Selecting the individual components—like those for the Directional Light or SkyAtmosphere—displays their own properties. These properties—like mobility and intensity—can also be set.

![Components of the SunSky Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/81731c98-6e3b-406a-a064-b8107269b005/07-sunsky-plugin-sunsky-details.png)

## Properties and Settings

The following adjustable properties are found in the SunSky Actor **Details** panel.

![Set of the properties for the SunSky Actor components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f40929f0-b48d-47d1-a926-4f388816d28c/08-sunsky-plugin-sunsky-properties.png)


Since **Transformation** properties are pretty standard for all Actors, we've skipped them below.

| Property | Description |
| --- | --- |
| Location |  |
| **Latitude** | The degree north or south of the equator. |
| **Longitude** | The degree east or west of the prime meridian. |
| **Time Zone** | The specified time for a given region of the world. The time zone uses GMT as a basis. |
| **North Offset** | Sets the directional position of North for the SunSky Actor and its components. |
| Date |  |
| **Month** | Sets the current month. |
| **Day** | Sets the current day. |
| **Use Daylight Saving Time** | Enables Daylight Saving Time (DST). |
| **DST Start Month** | Sets the Month at which DST starts in the current year. |
| **DST Start Day** | Sets the Day at which DST starts in the current year. |
| **DST End Month** | Sets the Month at which DST ends in the current year. |
| **DST End Day** | Sets the Day at which DST ends in the current year. |
| **DST Switch Hour** | Sets the beginning and ending hours of DST. |
| Time |  |
| **Solar Time** | Sets the time of day.  Enter this value as a float in military time. For example, 12:30 AM would be 00.5 and 12:30 PM would be 12.5. |

## ArchVis Template Level Examples

When you create a project, the template category for **Architecture, Engineering, and Construction** includes a template called **ArchVis**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f129bc95-6219-4a85-b814-c0e2a64a334a/09-sunsky-plugin-archvis-template.png)

This template project is dedicated to architecture visualization workflows, with examples for sun studies, interior rendering, and non-photorealistic stylized renderings. It includes the following assets already set up for you to use:

* Multiple Levels that contain scenes set up to demonstrate visualization with physically accurate lighting using the SunSky Actor.
* Lighting configuration and Post Process Volume with ray-tracing features already set for those projects that have enabled ray tracing.
* Example Cameras and Sequencers used to render out the scene. These also include dynamic time-of-day transitions.

This template also enables the [Datasmith plugin](/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine), which is a collection of tools and plugins designed to import scenes and assets created in offline rendering applications, like 3ds Max and CAD software, into a real-time engine.

### Exterior

The **Exterior** Level demonstrates usage of the SunSky Actor with multiple cameras used with Sequencer to demonstrate a time-of-day sequence while moving through the scene in various locations. It can be found in the `Content/ArchVisProject` folder.

It's also a use of the SunSky Actor components [lighting the scene dynamically](/documentation/en-us/unreal-engine/movable-light-mobility-in-unreal-engine), as well as a demonstration of the various real-time [Ray Tracing](/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) when they are enabled for the project.

### Interior

The **Interior** Level demonstrates usage of the SunSky Actor components to light the scene with [precomputed static lighting](/documentation/en-us/unreal-engine/static-light-mobility-in-unreal-engine). It can be found in the `Content/ArchVisProject` folder.

This includes:

* Using [Lightmass](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine) to generate baked global illumination and lighting for the scene.
* Using [Lightmass Importance Volumes](/documentation/en-us/unreal-engine/lightmass-basics-in-unreal-engine) and [Lightmass Portals](/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine) to control and focus the area from where Lightmass emits photons in.

## Additional Notes

* [Ray Tracing](/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) features enabled by default on the SunSky Actor for the Directional Light and Sky Light to both support casting of ray-traced shadows.
* It's possible to manually change rotational values of the Directional Light in the SunSky Actor. However, when you change other settings that affect other parts of the SunSky Actor, your manually adjusted rotational values will be reset to the default position. This prevents contradicting values incorporated with the idea of a geolocated calculation.
* SkyLight Actors now come with the Real Time Capture mode enabled by default. This should help you better capture your SkyAtmosphere Component, Volumetric Clouds, Height Fog, and more. Just remember that this mode is only available when using the dynamic or stationary modes. If you'd like to disable the Real Time Capture mode, simply select the SkyLight Actor, navigate to the Details panel, and uncheck the Real Time Capture box at the top of the Light section.

## Additional Resources

* When you input a location by name at the website [LatLong.net](http://www.LatLong.net), it returns a map view, along with latitude, and longitude coordinates.
* The website [TimeAndDate.com](http://www.TimeAndDate.com) has a section of their site dedicated to the [Time Zone Map](https://www.timeanddate.com/time/map/), which can be useful when figuring out what time zone you want to set the SunSky Actor to use. By default, it uses -5 GMT.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [artist tool](https://dev.epicgames.com/community/search?query=artist%20tool)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [visualization](https://dev.epicgames.com/community/search?query=visualization)
* [environmental lighting](https://dev.epicgames.com/community/search?query=environmental%20lighting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Project Templates and Setup](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#projecttemplatesandsetup)
* [Enabling the Sun Position Calculator Plugin](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#enablingthesunpositioncalculatorplugin)
* [Using the Sun and Sky Actor](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#usingthesunandskyactor)
* [Properties and Settings](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#propertiesandsettings)
* [ArchVis Template Level Examples](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#archvistemplatelevelexamples)
* [Exterior](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#exterior)
* [Interior](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#interior)
* [Additional Notes](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#additionalnotes)
* [Additional Resources](/documentation/en-us/unreal-engine/sun-and-sky-actor-in-unreal-engine?application_version=5.7#additionalresources)

Related documents

[Sky Atmosphere Component

![Sky Atmosphere Component](https://dev.epicgames.com/community/api/documentation/image/b8387986-89fb-4810-abde-f4b04c381381?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine)
