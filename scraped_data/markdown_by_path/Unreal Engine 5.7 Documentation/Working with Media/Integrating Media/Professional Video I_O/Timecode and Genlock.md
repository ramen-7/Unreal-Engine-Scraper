<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine?application_version=5.7 -->

# Timecode and Genlock

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
7. [Professional Video I/O](/documentation/en-us/unreal-engine/professional-video-io-in-unreal-engine "Professional Video I/O")
8. Timecode and Genlock

# Timecode and Genlock

Describes how to make the Unreal Engine adopt timecode from an AJA video input, and how to lock the Engine's frame rate to match the source video.

![Timecode and Genlock](https://dev.epicgames.com/community/api/documentation/image/cecfc193-454e-4b5d-95a4-cde028f0d5a9?resizing_type=fill&width=1920&height=335)

 On this page

By default, the Unreal Editor generates its own timecode, based on the current system time on your computer. This timecode is set by default to run at 30 frames per second, but the engine typically renders many more frames than 30 in any given second. So, typically multiple consecutive frames in the output will get assigned the same timecode value.

When you're working with professional video, you often have to keep timecode in sync between multiple different video feeds and signal processing devices. To do this, you may need to make the Unreal Engine's timecode match the timecode of the video feed you're working with. In some cases, you may want to go even further, and lock the engine so that it only produces one single frame for each frame of video that comes in through a reference input — we refer to this as *genlock*.

This page describes how to make the Unreal Engine adopt the timecode values from a port that you specify on your AJA card instead of generating its own, and how to genlock the Unreal Engine to that timecode signal.

Timecode and genlock management is under active development, and is likely to change in future versions.

## Visualizing Timecode in the Unreal Editor

To see the actual timecode values being used by the Unreal Engine while you're working in the Unreal Editor, use the **Timecode Provider** panel. You can find this panel in the main menu under **Window > Virtual Production > Timecode Provider**.

[![](https://dev.epicgames.com/community/api/documentation/image/7fe33b65-e66c-483f-8397-8b8365c3af03?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7fe33b65-e66c-483f-8397-8b8365c3af03?resizing_type=fit)

It displays the current timecode, the timecode provider (the source of the timecode values), and the number of timecode frames that are being generated within each second. You can dock this panel anywhere in the UI of the main Level Editor.

Alternatively, you can use the following console command:

C++

```
stat timecode
```

stat timecode

Copy full snippet(1 line long)

You'll see the values printed in the Unreal Editor viewport, in **HH:MM:SS:FF** format:

[![Timecode display in the viewport](https://dev.epicgames.com/community/api/documentation/image/32832f3c-2153-4601-917f-4b97619357d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32832f3c-2153-4601-917f-4b97619357d5?resizing_type=fit)

If you have the Unreal Engine set up to adopt timecode from an input signal, or to genlock to a video signal, you'll also see the source of the timecode and genlock. For example:

[![Genlocked and synchronized timecode in the viewport](https://dev.epicgames.com/community/api/documentation/image/d436e46c-3cfa-4aa8-a39a-c8dff349db52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d436e46c-3cfa-4aa8-a39a-c8dff349db52?resizing_type=fit)

You can use this command to confirm that the Unreal Engine is generating frames at the rate you're expecting, and that it's using the same timecode values as your input video.

## Setting up Timecode and Genlock

The following steps show how to make the Unreal Engine adopt its timecode values from an input SDI video feed coming in from an AJA or Blackmagic device, and how to make the Unreal Engine lock its frame rate to that feed so that it generates only one frame of output for each frame of input.

1. Right-click in the Content Browser, and choose **Create Basic Asset > Blueprint Class**.

   [![Create new Blueprint class](https://dev.epicgames.com/community/api/documentation/image/3a3367d3-6027-4196-aa8c-a9c93700f38d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a3367d3-6027-4196-aa8c-a9c93700f38d?resizing_type=fit)
2. In the **Pick Parent Class** window, expand the **All Classes** section (1). Search for and select the **AjaTimecodeProvider** class (pictured) or **BlackmagicTimecodeProvider** class (2), then click **Select** (3).

   [![TimecodeProvider parent classes](https://dev.epicgames.com/community/api/documentation/image/b0aa5392-8f19-4fa7-a9ef-911f37cf599a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b0aa5392-8f19-4fa7-a9ef-911f37cf599a?resizing_type=fit)

   Back in the Content Browser, give your new Asset a descriptive name, such as **AJA\_Timecode\_Port** or **Blackmagic\_Timecode\_Port**.
3. Double-click your new Asset to open it up in the Blueprint Editor, and set up the properties in the **Details** panel.

   * To read the timecode from an incoming video stream, set the **Video Configuration** or **Media Configuration** to point to the port on your AJA or Blackmagic card, and (if applicable) the type of timecode to read from the feed (LTC or VITC).
   * If you are using an AJA card, and you want to read the timecode from a reference port on the card rather than from a video stream, enable **Use Reference In** and set the **Reference Configuration** instead of the **Video Configuration**.
4. **Compile** and **Save** your Blueprint class, and close the Blueprint Editor.
5. If you want to genlock the Unreal Engine to your video source, repeat the previous instructions to create and set up another Blueprint class, but this time use **AjaCustomTimeStep** or **BlackmagicCustomTimeStep** as the parent class.

   [![Custom Time Step Provider parent classes](https://dev.epicgames.com/community/api/documentation/image/ace7a7b0-5690-4687-9217-ade5a00993ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ace7a7b0-5690-4687-9217-ade5a00993ed?resizing_type=fit)
6. This class requires similar settings to the **AjaTimecodeProvider** or **BlackmagicTimecodeProvider**:

   [![Custom Time Step Provider settings](https://dev.epicgames.com/community/api/documentation/image/946c5970-acdb-489d-8e2e-aa29643f2dca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/946c5970-acdb-489d-8e2e-aa29643f2dca?resizing_type=fit)

   AJA cards also offer additional settings; see the tooltips for details.
7. From the main menu, choose **Edit > Project Settings**.
   In the **Project Settings** window, open the **Engine > General Settings** category (1), and find the **Timecode** section (2). From the **TimecodeProvider** drop-down list, select the timecode port Asset that you created.

   [![Set the TimecodeProvider in the Project Settings](https://dev.epicgames.com/community/api/documentation/image/c9e27f3f-ef15-4904-a219-42e69c588953?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9e27f3f-ef15-4904-a219-42e69c588953?resizing_type=fit)
8. If you want to genlock the Unreal Engine to your video source, find the **Framerate** section above, and expand the advanced properties at the bottom of the section. From the **Custom TimeStep** drop-down list, select the genlock port Asset that you created.

   [![Set the Custom TimeStep in the Project Settings](https://dev.epicgames.com/community/api/documentation/image/d43b3da0-6740-425a-8a66-1a459470cf9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d43b3da0-6740-425a-8a66-1a459470cf9c?resizing_type=fit)
9. Close the Unreal Editor and restart your Project.

If you use Media Profiles to set up multiple different media configurations for your Project, you can also override these default Project-level settings for Timecode and Timestep Providers in each Media Profile. For more information, see [Supporting Multiple Media Configurations](https://dev.epicgames.com/documentation/en-us/unreal-engine/supporting-multiple-media-configurations-in-unreal-engine).

### End Result

As long as you have video input coming in to the port you set up for the timecode provider and custom timestep classes, and that video has the resolution, frame rate and timecode format that you specified, the Unreal Engine should adopt your video's timecode and lock its frame update frequency so that it generates one output frame for each input frame.

To verify that this is working, use one of the options described under [Visualizing Timecode in the Unreal Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine).

## Timecode Texel Encoding

For debugging purposes, the Media Source and Media Output Assets for AJA and Blackmagic devices can encode the timecode of each frame into the video image by illuminating pixels in white. This can be useful if you need a visual way to verify that a given frame of video actually matches the timecode signal that accompanies it.

Timecode is usually expressed in the format **HH:MM:SS:FF**, for a total of eight digits. Each of these digits is assigned a row in the texture output, starting from the top of the image. Within each of those rows, count from the left of the image to value of that timecode digit to find the pixel that represents the timecode value. The leftmost pixel is pixel number 0.

So, for example, given the timecode value 12:08:44:12:

* On the first row, the second pixel from the left is lit (pixel number 1).
* On the second row, the third pixel from the left is lit (pixel number 2).
* On the third row, the leftmost pixel from the left is lit (pixel number 0).
* On the fourth row, the ninth pixel from the left is lit (pixel number 8).
* and so on.

* [professional video](https://dev.epicgames.com/community/search?query=professional%20video)
* [guide](https://dev.epicgames.com/community/search?query=guide)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Visualizing Timecode in the Unreal Editor](/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine?application_version=5.7#visualizing-timecode-in-the-unreal-editor)
* [Setting up Timecode and Genlock](/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine?application_version=5.7#setting-up-timecode-and-genlock)
* [End Result](/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine?application_version=5.7#end-result)
* [Timecode Texel Encoding](/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine?application_version=5.7#timecode-texel-encoding)
