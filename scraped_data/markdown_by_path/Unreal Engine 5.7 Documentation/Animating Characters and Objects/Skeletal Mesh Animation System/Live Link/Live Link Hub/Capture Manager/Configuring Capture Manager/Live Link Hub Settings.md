<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-hub-settings?application_version=5.7 -->

# Live Link Hub Settings

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
10. [Configuring Capture Manager](/documentation/en-us/unreal-engine/configuring-capture-manager "Configuring Capture Manager")
11. Live Link Hub Settings

# Live Link Hub Settings

Configuring Capture Manager in Live Link Hub.

![Live Link Hub Settings](https://dev.epicgames.com/community/api/documentation/image/33ed7aba-7510-4d67-9d8f-4bde75cc0254?resizing_type=fill&width=1920&height=335)

 On this page

## General Settings

The **Capture Manager** settings in **Live Link Hub** can be accessed through the **Settings** menu.

|  |  |
| --- | --- |
| [Live Link Hub Settings](https://dev.epicgames.com/community/api/documentation/image/fea933d6-0e2a-4167-8261-0c5b10904b69?resizing_type=fit) | [Plugins Capture Manager](https://dev.epicgames.com/community/api/documentation/image/6dd9cd38-9141-496f-89db-7f70c8bef4b5?resizing_type=fit) |

* **Default Working Directory**: Specify the (potentially temporary) location where converted data will be stored during the ingest process.
* **Should Clean Working Directory**: Whether the downloaded and converted files should be deleted from the **Working Directory** after ingest is complete (successfully or otherwise).
* **Download Directory**: Location where data downloaded from a remote device (such as Live Link Face device) will be stored.
* **Enable Third Party Encoder**: If enabled, use a third party encoder/decoder ([FFmpeg](https://ffmpeg.org/)) for data conversion, with additional settings as provided.
* **Parallel Jobs**: The number of jobs to process in parallel when ingesting.

Naming tokens can be used to automatically populate parts of the **Working Directory** and **Download Directory** locations.

## Third Party Encoder Support

It is possible to use an external third party media encoder or decoder ([FFmpeg](https://ffmpeg.org/)) for data conversion during ingest. This may be desirable if the default workflow using Windows Media Foundation does not support the data format you wish to work with.

To configure a third party encoder or decoder:

1. Download and install FFmpeg from [ffmpeg.org](http://ffmpeg.org/).
2. Ensure E**nable Third Party Encoder** is enabled in the settings. This will cause some additional options to be available.

   [![](https://dev.epicgames.com/community/api/documentation/image/f53d0583-7982-488b-8720-e59280acb31f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f53d0583-7982-488b-8720-e59280acb31f?resizing_type=fit)
3. Provide the additional settings as needed:

   * **Third Party Encoder**: The full path to the ffmpeg executable.
   * **Custom Video Command Arguments**: To be used when executing the third party encoder with video data.
   * **Custom Audio Command Arguments**: To be used when executing the third party encoder with audio data.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [General Settings](/documentation/en-us/unreal-engine/live-link-hub-settings?application_version=5.7#generalsettings)
* [Third Party Encoder Support](/documentation/en-us/unreal-engine/live-link-hub-settings?application_version=5.7#thirdpartyencodersupport)
