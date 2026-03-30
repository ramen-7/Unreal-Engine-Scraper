<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7 -->

# Using Pix on Windows with Unreal Engine

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Optimizing and Debugging Projects for Real-Time Rendering](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine "Optimizing and Debugging Projects for Real-Time Rendering")
7. Using Pix on Windows with Unreal Engine

# Using Pix on Windows with Unreal Engine

Instructions on how to get started using Pix with Unreal Engine

![Using Pix on Windows with Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/3c79534c-da2c-4823-ac92-69d4b74950a7?resizing_type=fill&width=1920&height=335)

 On this page

Pix is a free standalone proprietary graphics debugger maintained by Microsoft, that you can use to perform single-frame captures of an application, such as Unreal Engine. The capture is loaded into Pix to inspect what is happening on the GPU through events, API calls, and more, in full detail.

## Install Pix

Pix is available to download and install from the [Pix on Windows](https://devblogs.microsoft.com/pix/) website. The list of supported operating systems and APIs below reflect what Pix currently supports, which may differ from what Unreal Engine supports. For the latest updates, see [Pix’s Download](https://devblogs.microsoft.com/pix/download/) page.

Pix supports the following Operating Systems:

1. Windows 10 and 11

Pix supports the following Graphics APIs:

1. D3D11 (Using an emulator, instructions are provided [below](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine#pixapplication).)
2. D3D12
3. Xbox GDK (Not covered in this article.)

## Enable Pix in Your Project

You need to install Windows on Pix on your system before being able to use it. As of Unreal Engine 5.5, all you need to do to enable Pix is to pass in the `-AttachPix` command line argument when launching your project.

When Pix attaches on startup, you'll see the Pix application icon in the upper-right corner of the Level Viewport.

![Pix application icon in the Level Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3760ecd0-ca8e-4cab-9ae9-2a894d69c4b3/viewport-bar.png)

For more detailed steps, please follow the instructions below.

## Enabling Pix through Shortcut Properties

1. Enable command line arguments using an editor shortcut.
2. In the Shortcut tab, add the following to the Target line: `-AttachPix`.

This method is ideal when you only want to run Pix some of the time. You can also provide this command line argument inside Visual Studio or any other IDE that supports passing in command line arguments at launch.

![Pix shortcut properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cab57a50-6869-4724-8c9f-50da1af42e3d/shortcut-settings.png)

## Performing a Frame Capture

The steps below describe at a high level how to perform a single-frame capture with your Unreal Engine project using the integrated Pix plugin or directly from the Pix application.

You can find further details on functionality and use of Pix in the [Pix Documentation](https://devblogs.microsoft.com/pix/documentation/).

## Pix Application

The following are the high-level steps required to capture a frame using Unreal Engine with the standalone Pix executable:

1. Configure Pix to launch your game or the UEEditor.exe with the appropriate command line arguments.

   1. You can either choose to launch the application through PIX or attach to a running process.
   2. Once launched, you can press the in-editor capture button or use the Pix's native capture button to capture a single frame.![Pix attach options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e67953b-fba9-48a1-9ca3-42c915e5b576/pix-attach-options.png)


   If you are using a D3D11 application, make sure to select the Force D3D11On12 option.
2. Launch the executable.

   1. The Pix capture button should automatically appear in the level viewport.
   2. Press the capture button and the capture should open automatically within Pix.

For full details on setting up Pix, launching an application and performing a frame capture, see the [Pix Take A Capture Guide](https://devblogs.microsoft.com/pix/taking-a-capture/).

## **Troubleshooting**

If you are having trouble seeing all of the events in your Pix captures, make sure to disable the **Use Less CPU in Background** editor setting.

![Disable Use Less CPU in Background editor setting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19d31267-ddad-41a0-b87f-9f40175f7ad0/editor-settings.png)

## **Additional Notes and Resources**

See [Pix Documentation](https://devblogs.microsoft.com/pix/documentation/) for further reading on Pix use and analysis of frame captures.

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Install Pix](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#installpix)
* [Enable Pix in Your Project](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#enablepixinyourproject)
* [Enabling Pix through Shortcut Properties](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#enablingpixthroughshortcutproperties)
* [Performing a Frame Capture](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#performingaframecapture)
* [Pix Application](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#pixapplication)
* [Troubleshooting](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#troubleshooting)
* [Additional Notes and Resources](/documentation/en-us/unreal-engine/using-pix-on-windows-with-unreal-engine?application_version=5.7#additionalnotesandresources)
