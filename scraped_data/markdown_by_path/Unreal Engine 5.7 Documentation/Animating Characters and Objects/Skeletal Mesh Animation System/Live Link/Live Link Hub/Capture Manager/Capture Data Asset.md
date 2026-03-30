<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/capture-data-asset?application_version=5.7 -->

# Capture Data Asset

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine "Live Link")
8. [Live Link Hub](/documentation/en-us/unreal-engine/live-link-hub-in-unreal-engine "Live Link Hub")
9. [Capture Manager](/documentation/en-us/unreal-engine/capture-manager "Capture Manager")
10. Capture Data Asset

# Capture Data Asset

Overview of the Capture Data asset in Unreal Engine.

![Capture Data Asset](https://dev.epicgames.com/community/api/documentation/image/3cfa9187-38f8-4cbd-a96d-c14eac3a4556?resizing_type=fill&width=1920&height=335)

 On this page

The **Capture Data** asset is created by **Capture Manager** as part of the ingest process. It tracks the assorted set of data and metadata that is required when working with performance capture data. Some of that data is optional but commonly available (such as audio).

A Capture Data asset can be input to the [MetaHuman Identity](https://dev.epicgames.com/documentation/en-us/metahuman/metahuman-identity-asset?application_version=5.6) and [MetaHuman Performance](https://dev.epicgames.com/documentation/en-us/metahuman/metahuman-performance-asset?application_version=5.6) asset.

Although the asset is typically created by an automated process, it can be created manually if required. While a Capture Data asset can be configured manually, be mindful of the fact that incompletely or incorrectly configured information will create unpredictable issues that might be difficult to troubleshoot.

[![Footage Capture Data](https://dev.epicgames.com/community/api/documentation/image/42bd6dd2-33b5-4f3a-8147-651f003a0d82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/42bd6dd2-33b5-4f3a-8147-651f003a0d82?resizing_type=fit)

A **Capture Data** asset may reference one or more of the following other assets depending on the data it represents:

* **Img Media Source** (for depth and/or RGB video)
* **Sound Wave** (for audio tracks)
* **Camera Calibration**

It is important to not confuse the difference between the **Device Class** and the **Device Model** for iOS devices. The **Device Class** inside a **Capture Data** asset is a fixed choice from limited options, and it’s the commonly known name of the model from a consumer point of view. The **Device Model** is a less visible versioning that **doesn’t necessarily line up** with the public-facing model number. This is usually ahead of the consumer branding. For example, an iPhone 12 device is likely to have a model number of iPhone 13,N.

## Timecode Information

The Timecode for the Image and Depth Sequences can be viewed and set via the **ImgMediaSource** asset editor.

[![Timecode](https://dev.epicgames.com/community/api/documentation/image/515c6634-0f6e-45e1-8f40-ca522a459e6a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/515c6634-0f6e-45e1-8f40-ca522a459e6a?resizing_type=fit)

The Timecode and Timecode Frame Rate for SoundWave assets can be viewed and set selecting **Scripted Asset Actions > Set Timecode Info**.

[![Scripted Asset Actions](https://dev.epicgames.com/community/api/documentation/image/531c8a32-e28a-4942-abd3-5b1f6245714f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/531c8a32-e28a-4942-abd3-5b1f6245714f?resizing_type=fit)

Enter the desired Timecode and Timecode Frame Rate values and click **OK** to set the values.

[![Set Timecode Info](https://dev.epicgames.com/community/api/documentation/image/c71dd437-a0a6-4964-b036-aa0cc4c54f9f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c71dd437-a0a6-4964-b036-aa0cc4c54f9f?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Timecode Information](/documentation/en-us/unreal-engine/capture-data-asset?application_version=5.7#timecodeinformation)
