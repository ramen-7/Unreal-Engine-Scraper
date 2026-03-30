<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine?application_version=5.7 -->

# In-Camera VFX Template

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
7. [In-Camera VFX](/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine "In-Camera VFX")
8. In-Camera VFX Template

# In-Camera VFX Template

An overview of the In-Camera VFX Template

![In-Camera VFX Template](https://dev.epicgames.com/community/api/documentation/image/f6b18202-d53a-4f4d-90df-4755d2a2ffe1?resizing_type=fill&width=1920&height=335)

 On this page

The **In-Camera VFX Template** is the starting point for creating the complex configuration that goes into a live-action LED stage. It provides a basic map and a variety of features to help you get started with your in-camera VFX project.

## Creating a Project from the Template

1. Launch **Unreal Engine**.
2. Select the **Film, Television, and Live Events** template category.

   [![Film, Television and Live Events template category](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4dc3f8fe-2b45-4025-825d-5277552fb022/ue5_01-select-section.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4dc3f8fe-2b45-4025-825d-5277552fb022/ue5_01-select-section.png)

   Click image for full size.
3. Click **InCamera VFX**.

   [![InCamera VFX template selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2646e3f-0547-4fc4-bc9a-d3aea2c8a87b/ue5_02-select-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2646e3f-0547-4fc4-bc9a-d3aea2c8a87b/ue5_02-select-template.png)

   Click image for full size.
4. Choose whether to include starter content and whether to enable retracing, and select the path and name for your project.
5. Click **Create**.

## Template Features

* An nDisplay configuration and Blueprint set up for In-Camera VFX
* Configurable inner frustum and outer frustum
* Live Link
* A chroma key and tracking markers
* Color Correction Regions
* Web remote control
* OSC

Refer to the [In-Camera VFX Overview](/documentation/en-us/unreal-engine/in-camera-vfx-overview-in-unreal-engine) and [In-Camera VFX Quick Start](/documentation/en-us/unreal-engine/in-camera-vfx-quick-start-for-unreal-engine) for information on how to use these features.

In order to access the **Blueprints** and other assets described in the template, make sure to enable **Show Engine Content** and **Show Plugin Content** in the **View Options** menu in the **Content Browser**.

![View engine content and plugin content options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6507451f-f012-4133-b511-d4e930b10f00/ue5_03-enable-engin-plugin-content.png "View engine content and plugin content options")

## Maps

[![In camera VFX maps](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/21529d9f-4d7c-4ce4-93bb-35ba6b0dbb19/ue5_04-curved-stage-map.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/21529d9f-4d7c-4ce4-93bb-35ba6b0dbb19/ue5_04-curved-stage-map.png)

Click image for full size.

**LED\_CurvedStage** is the main map. It is provided for typical in-camera VFX set-ups and configurations.

### LED Curved Stage

![LED Curved Stage](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/630a5611-93b8-450b-989f-4389cc032a9f/ue5_05-curved-stage-example.png "LED Curved Stage")

This map provides an alternative set up with a curved mesh used for the LED wall. The LED wall is composed of four sub-sections, two on the left and two on the right, hence why there are four screens within **nDisplay\_InCamVFX\_Config** under the root component. You can customize these sub-sections to use this as a starting point to describe any type of curved LED displays, so that it matches your hardware configuration.

![Curved screen section in the hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3191f6ea-e58c-4bb0-a940-9e8d6e37a4f0/ue5_06-screen-components.png "Curved screen section in the hierarchy")

#### Chroma Key

In the Details for **nDisplay\_InCamVFX\_Config** in the Curved Stage map, there is a control setting to enable the chroma key, allowing control over the visibility of that layer.

[![Enable chroma key](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a825e0d-9483-4950-8e0a-c210d09ffac0/ue5_07-enable-chromakey.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a825e0d-9483-4950-8e0a-c210d09ffac0/ue5_07-enable-chromakey.png)

Click image for full size.

* [templates](https://dev.epicgames.com/community/search?query=templates)
* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [in-camera vfx](https://dev.epicgames.com/community/search?query=in-camera%20vfx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Project from the Template](/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine?application_version=5.7#creatingaprojectfromthetemplate)
* [Template Features](/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine?application_version=5.7#templatefeatures)
* [Maps](/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine?application_version=5.7#maps)
* [LED Curved Stage](/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine?application_version=5.7#ledcurvedstage)
* [Chroma Key](/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine?application_version=5.7#chromakey)
