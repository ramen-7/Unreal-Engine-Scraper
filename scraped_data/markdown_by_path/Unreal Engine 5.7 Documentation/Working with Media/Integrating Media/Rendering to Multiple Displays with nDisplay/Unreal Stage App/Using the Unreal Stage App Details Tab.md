<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-unreal-stage-app-details-tab-in-unreal-engine?application_version=5.7 -->

# Using the Unreal Stage App Details Tab

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. [Unreal Stage App](/documentation/en-us/unreal-engine/unreal-stage-app-for-unreal-engine "Unreal Stage App")
9. Using the Unreal Stage App Details Tab

# Using the Unreal Stage App Details Tab

The Details tab offers the full set of Actor properties available to modify within the scene via the Unreal Stage app.

![Using the Unreal Stage App Details Tab](https://dev.epicgames.com/community/api/documentation/image/65b467ef-8b50-4c40-884b-93575d26f565?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## Details Tab Properties

The available properties match the equivalent properties in the desktop Unreal Engine scene and will vary based on the type of content selected.

### Light Cards and Flags

For Light Cards and Flags, the following properties are available:

* **Color**
  + RGB or HSV values.
* **Orientation:**
* **Mask**
  + Toggle between a circle or square mask for the Light Card
* **Scale X and Scale Y**
  + Sliders can provide more precise control compared to resizing with pinch zoom
* **Latitude and Longitude**
* **Longitude**
  + Sliders can provide precise control for placement and positioning compared to touch-only
* **Spin**
  + Sliders can provide more precise control for rotation compared to touch-only
* **Appearance:**
  + **Temperature**
  + **Tint**
  + **Gain**
  + **Opacity**
  + **Feathering**
  + **Exposure**
    - Exposure controls include convenient buttons for quarter-, half-, and full-stop increments.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79ffeb9a-9eef-4e76-abd7-6815f8cceff4/details-1.gif)

### Color Correction Regions and Windows

For Color Correction Windows, the following properties are available:

* Color Grading
* RGB or HSV values
* Color Grading Modes:
  + **Global**
  + **Shadows**
  + **Midtones**
  + **Highlights**
* Color Grading Properties (each available per mode):
  + **Saturation**
  + **Contrast**
  + **Gamma**
  + **Gain**
  + **Offset**
* Orientation:
  + Mask
    - Toggle between a circle or square mask for the Color Correction Window
  + Scale X and Scale Y
    - Sliders can offer more fine-grain control over precise resizing than pinch zoom
  + Latitude and Longitude
    - Sliders can offer more fine-grain control over precise placement and positioning
  + **Spin**
    - Sliders can offer more fine-grain control over precise rotation than touch-only.
  + **Radial Offset**
    - Push/pull the Color Correction Window away from the LED volume representation along an axis with the nDisplay Root Actor's origin. This is useful to apply color grading behind some content in the scene but in front of others (as opposed to in front of everything in the scene visible to nDisplay).
* Appearance:
  + Color Temperature
  + Tint
  + Intensity
  + Inner
  + Outer
  + Falloff

**Color Correction Regions** do not offer appearance controls because there are no 3D placement tools in Unreal Stage. Only color grading and appearance properties can be modified in the app.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/761b609c-c66e-468f-9c28-dc250ee944c5/details-2.gif)

### Preview Thumbnail

The Details tab offers a preview thumbnail to provide a visual in the app while modifying properties. The preview thumbnail can be moved to any corner of the Unreal Stage UI or stowed/minimized.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0ad8f87c-1629-454c-b098-5b7f9857e590/details-3.gif)

### Set a Property to an Explicit Value

In addition to the sliders, properties can also be modified and set to an explicit value by double-tapping on it to bring up an input dialog and the keyboard.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63d6219b-5cc9-4b06-8e13-e204f3e85646/details-4.gif)

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Details Tab Properties](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-details-tab-in-unreal-engine?application_version=5.7#detailstabproperties)
* [Light Cards and Flags](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-details-tab-in-unreal-engine?application_version=5.7#lightcardsandflags)
* [Color Correction Regions and Windows](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-details-tab-in-unreal-engine?application_version=5.7#colorcorrectionregionsandwindows)
* [Preview Thumbnail](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-details-tab-in-unreal-engine?application_version=5.7#previewthumbnail)
* [Set a Property to an Explicit Value](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-details-tab-in-unreal-engine?application_version=5.7#setapropertytoanexplicitvalue)
