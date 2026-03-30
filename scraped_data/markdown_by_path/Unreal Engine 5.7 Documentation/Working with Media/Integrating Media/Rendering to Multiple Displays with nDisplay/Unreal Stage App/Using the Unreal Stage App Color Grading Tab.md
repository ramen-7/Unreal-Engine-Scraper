<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-unreal-stage-app-color-grading-tab-in-unreal-engine?application_version=5.7 -->

# Using the Unreal Stage App Color Grading Tab

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
9. Using the Unreal Stage App Color Grading Tab

# Using the Unreal Stage App Color Grading Tab

Color grade the nDisplay LED volume through the Unreal Stage app.

![Using the Unreal Stage App Color Grading Tab](https://dev.epicgames.com/community/api/documentation/image/fa961c6c-a5c0-42ec-8636-c5c524a5a707?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## Color Grading

The nDisplay Color Grading Tab enables you to perform color grading operations on the nDisplay cluster as a whole, just as you can in the ICVFX Editor. You can apply color grading to the entire cluster or on a per-viewport basis, as well as any ICVFX Cameras (plural) with per-node granularity if desired.

## Outliner

When on the nDisplay Color Grading Tab, a modified Outliner will appear with two panes instead of one:

* Color Grading Outliner
  + All color grade-able content in the Level will appear here, which can include Post Process Volume(s) in addition to the nDisplay Root actor.
  + ICVFX Camera components are listed underneath the corresponding nDisplay Root Actor. Select the Root to color grade the viewports vs. the cameras.
* Per-Viewport/Per-Node Color Grading
  + Per-Viewport (for the outer viewports) and Per-Node (for the inner frustums) color grading can be defined in Unreal Engine and appear as options here to color grade specific areas of the LED volume, such as the ceiling.
  + Per-Viewport and Per-Node configurations cannot yet be created and modified directly in Unreal Stage, but this is planned to be included in a future release.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1dad093-6827-4f30-926f-980f8991037e/colorgrading-1.gif)

## Preview Thumbnail

The Color Grading tab offers a preview thumbnail to provide an in-app visual while modifying properties. The preview thumbnail can be moved to any corner of the Unreal Stage UI or stowed/minimized.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/699770c8-c922-4458-9b5e-0f661ac671aa/colorgrading-2.gif)

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

* [Color Grading](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-color-grading-tab-in-unreal-engine?application_version=5.7#colorgrading)
* [Outliner](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-color-grading-tab-in-unreal-engine?application_version=5.7#outliner)
* [Preview Thumbnail](/documentation/en-us/unreal-engine/using-the-unreal-stage-app-color-grading-tab-in-unreal-engine?application_version=5.7#previewthumbnail)
