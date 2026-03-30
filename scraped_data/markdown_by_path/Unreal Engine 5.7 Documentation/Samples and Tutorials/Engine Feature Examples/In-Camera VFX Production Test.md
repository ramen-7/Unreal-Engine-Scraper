<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7 -->

# In-Camera VFX Production Test

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Engine Feature Examples](/documentation/en-us/unreal-engine/engine-feature-examples-for-unreal-engine "Engine Feature Examples")
7. In-Camera VFX Production Test

# In-Camera VFX Production Test

How to set up the In-Camera VFX Production Test sample, and explore the features, project structure, and settings used during production.

![In-Camera VFX Production Test](https://dev.epicgames.com/community/api/documentation/image/0ea45129-ed56-4e4b-b7bc-e54151c401ec?resizing_type=fill&width=1920&height=335)

 On this page

The In-Camera VFX Production Test is a Virtual Production sample that uses Unreal Engine and an LED Volume to feature traveling vehicle shots, multi-camera setups, and multi-user setup for making quick changes between takes. This sample was created in collaboration with filmmakers' collective [Bullitt](https://bullittbranded.com/). The team produced final pixels in-camera over four days on [Nant Studios](https://www.nantstudios.com/)' LED stage in Los Angeles.

The short produced from the project.

Exploring and modifying the sample will help you learn how you can:

* Structure your Virtual Production project so multiple artists can collaborate simultaneously on scenes during production.
* Use GPU Lightmass with Multi-User to bake lighting on one computer and share to all computers in the session for faster lighting changes.
* Render the inner frustum using mGPU on a multi-screen nDisplay cluster.
* Apply color correction and OCIO profiles to your nDisplay renders to achieve the desired look for each scene.
* Build the UI of your Remote Control Web Application to meet your production's needs and make quick changes on set from a tablet.
* Apply cvars to improve performance in the project.

This guide covers how the production team used Unreal Engine's features in the project to make the final result. Use this project as an example for designing your production. For learning the basics of in-camera VFX, refer to the [In-Camera VFX Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-quick-start-for-unreal-engine). For behind the scenes footage of this production, refer to the [Unreal Engine Spotlight](https://www.unrealengine.com/en-US/spotlights/taking-unreal-engine-s-latest-in-camera-vfx-toolset-for-a-spin).

## Stage Setup and Hardware

[![The In-Camera VFX Production Test stage](https://dev.epicgames.com/community/api/documentation/image/72193e19-7044-4c0a-ab54-07b24f3ba52c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/72193e19-7044-4c0a-ab54-07b24f3ba52c?resizing_type=fit)

Click image to expand.

Four nDisplay nodes were used to render the following volume, with 2 LED panels assigned to each node:

* **Walls**: Total resolution of **15312 x 2112** over **5** LED panels.
* **Ceiling**: Total resolution of **4160 x 5280** over **3** LED panels.

This real production sample is both CPU-intensive and GPU-intensive so it can render on this large LED volume at a camera-ready resolution. The diagram below shows every device contributing to the production and the connections between devices on stage. To learn about the roles of each device in the shoot, refer to [In-Camera VFX Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-overview-in-unreal-engine) for details. To learn what hardware is recommended for an in-camera VFX shoot, refer to [In-Camera VFX Recommended Hardware](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-hardware-for-in-camera-vfx-in-unreal-engine).

[![In-Camera VFX Production Test devices diagram](https://dev.epicgames.com/community/api/documentation/image/a4d534ef-b038-4d62-8f67-c3673c9330fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a4d534ef-b038-4d62-8f67-c3673c9330fd?resizing_type=fit)

Diagram showing what devices were used and how they communicated with each other on stage. Click image to expand.

## Getting Started

In addition to the [nDisplay Config](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-configuration-file-reference-for-unreal-engine) that represents the topology of the real stage used in production, a simple nDisplay Config is included in the project so you can view the scenes on a single computer without an LED volume. This section shows how to use the simple nDisplay Config to render the scene and make changes in a multi-user session on a single computer.

Follow these steps to launch an instance of the Unreal Editor and another instance of Unreal Engine with the nDisplay renderer in a multi-user session on your computer.

1. Access the [In-Camera VFX Production Test sample](https://fab.com/s/c9a039f679f8) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

   1. To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).
4. Go to the Unreal Engine folder on your computer and run Engine\Binaries\Win64\SwitchboardListener.exe to launch **SwitchboardListener** on your computer. The listener will minimize its window automatically on start to avoid issues with nDisplay devices. You can find the application in your OS's taskbar.

   The following is an example of a full path: `C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\SwitchboardListener.exe`
5. In the Unreal Engine folder, run Engine\Plugins\VirtualProduction\Switchboard\Source\Switchboard\Switchboard.bat to launch **Switchboard** on your computer. If this is your first time running Switchboard, it will install any required dependencies before opening the application window.

   The following is an example of a full path: `C:\Program Files\Epic Games\UE_4.27\Engine\Plugins\VirtualProduction\Switchboard\Source\Switchboard\Switchboard.bat`
6. Create a new **Switchboard Configuration**.

   * If this is your first time running Switchboard, the **Add New Switchboard Configuration** window appears when Switchboard launches.
   * If you have run Switchboard before, click **Configs > New Config** in the top left corner of the window to open the **Add New Switchboard Configuration** window.

     [![Adding a new Switchboard configuration](https://dev.epicgames.com/community/api/documentation/image/23f9c8ff-92d5-4f69-a457-501cd8fa9981?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23f9c8ff-92d5-4f69-a457-501cd8fa9981?resizing_type=fit)
7. In the **Add New Switchboard Configuration** window:

   1. Set **Config Path** to the name and location where you want to store your Switchboard Configuration file.
   2. Set **uProject** to the location of the In-Camera VFX Production Test sample project file, `TheOrigin.uproject`.
   3. Make sure **Engine Dir** is pointing to the **Engine** folder for your Unreal Engine.
   4. Click **Ok** to create the Switchboard Configuration.

      [![New Switchboard configuration paths](https://dev.epicgames.com/community/api/documentation/image/edae77f8-da6a-4e10-bb08-b093b03413b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/edae77f8-da6a-4e10-bb08-b093b03413b8?resizing_type=fit)
8. Set **Level** to **CaveEntrance\_NantStudiosSimple**.

   [![Setting the Level in Switchboard](https://dev.epicgames.com/community/api/documentation/image/e2930ce1-5b6e-4780-accd-2b1f6840928e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2930ce1-5b6e-4780-accd-2b1f6840928e?resizing_type=fit)
9. Add an nDisplay device to Switchboard:

   1. Click **Add Device** and select **nDisplay** from the dropdown.

      [![Adding an nDisplay device](https://dev.epicgames.com/community/api/documentation/image/fd4c1037-6df0-4df4-8797-ba8d649a3203?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd4c1037-6df0-4df4-8797-ba8d649a3203?resizing_type=fit)
   2. In the **Add nDisplay Device window**, click **Browse** and navigate to Content\TheOrigin\Content\Stages\NantStudiosSimple\Config\NDC\_NantStudiosSimple.uasset in the sample project's folder.

      [![Browsing to the nDisplay device .uasset file](https://dev.epicgames.com/community/api/documentation/image/a6455d50-ac0f-4b1f-8984-29549a5dad91?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a6455d50-ac0f-4b1f-8984-29549a5dad91?resizing_type=fit)
   3. Click **OK** to see one nDisplay device added to Switchboard.

      [![The nDisplay device added to Switchboard](https://dev.epicgames.com/community/api/documentation/image/13061684-dc19-4d17-9dc3-dfcb6fbefc46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13061684-dc19-4d17-9dc3-dfcb6fbefc46?resizing_type=fit)
10. Add an Unreal device to Switchboard:

    1. Click **Add Device** again and select **Unreal** from the dropdown.

       [![Adding an Unreal device](https://dev.epicgames.com/community/api/documentation/image/e70b70cc-9a79-437b-abae-9ba912d96931?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e70b70cc-9a79-437b-abae-9ba912d96931?resizing_type=fit)
    2. In the **Add Unreal Device** window, set the **IP Address** to the local computer: **127.0.0.1**.

       [![Setting the Unreal device local IP address](https://dev.epicgames.com/community/api/documentation/image/86aba67d-776d-42e4-b74e-377973406e47?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86aba67d-776d-42e4-b74e-377973406e47?resizing_type=fit)
    3. Click **OK** and see one Unreal device added to Switchboard.

       [![The Unreal device added to Switchboard](https://dev.epicgames.com/community/api/documentation/image/c6ebe068-49f7-4320-96a5-650d6dfcd6b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c6ebe068-49f7-4320-96a5-650d6dfcd6b8?resizing_type=fit)
11. Click the **Connect to Listener** button for the nDisplay **Render\_2** device to connect to SwitchboardListener.

    [![Connect to Listener button for nDisplay device in Switchboard](https://dev.epicgames.com/community/api/documentation/image/09dd46f9-4ea2-4104-bafd-85bf894869cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/09dd46f9-4ea2-4104-bafd-85bf894869cd?resizing_type=fit)
12. Click the **Start Unreal** button for the nDisplay **Render\_2** device to launch Unreal with the nDisplay renderer in a multi-user session.

    [![Start Unreal button for nDisplay device in Switchboard](https://dev.epicgames.com/community/api/documentation/image/c5b0059c-5d61-4f48-876e-c3131c0676f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5b0059c-5d61-4f48-876e-c3131c0676f3?resizing_type=fit)
13. All windows automatically minimize and the full screen nDisplay render appears. The view might be dark but you will change the view in a later step.
14. Open the minimized Switchboard window, and click the **Connect to listener** button for the Unreal device to connect to SwitchboardListener.

    [![Connect to Listener button for Unreal device in Switchboard](https://dev.epicgames.com/community/api/documentation/image/58be2e79-ad4d-4a86-987f-5dd254623321?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58be2e79-ad4d-4a86-987f-5dd254623321?resizing_type=fit)
15. Click the **Start Unreal** button for the Unreal device to launch an instance of the Unreal Editor in the Multi-User Session.

    [![Start Unreal button for Unreal device in Switchboard](https://dev.epicgames.com/community/api/documentation/image/cae77a7d-3c7a-4cbc-993e-9edd5c1324b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cae77a7d-3c7a-4cbc-993e-9edd5c1324b2?resizing_type=fit)
16. In the Editor, on the toolbar click **Open Level Snapshots Editor**.

    [![Open the Level Snapshots editor](https://dev.epicgames.com/community/api/documentation/image/b1bb6ca8-e35c-403e-81cd-06f1afa44de7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1bb6ca8-e35c-403e-81cd-06f1afa44de7?resizing_type=fit)
17. In the Level Snapshots Editor, double-click the **CaveEntrance\_NantStudiosSimple\_SetupA** Level Snapshot and click **Restore Level Snapshot**.

    [![Restore the Setup A Level Snapshot](https://dev.epicgames.com/community/api/documentation/image/95187f56-0e75-464a-b5e0-b9bd49a129ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95187f56-0e75-464a-b5e0-b9bd49a129ff?resizing_type=fit)
18. In the Unreal Editor's **World Outliner panel**, select the nDisplay Root Actor **NDC\_NantStudios\_Simple** to see its updated position.

    ![Before Level Snapshot restore](https://dev.epicgames.com/community/api/documentation/image/d9330861-8b44-4cad-8224-0bde11188b3b?resizing_type=fit&width=1920&height=1080)

    ![After Level Snapshot restore](https://dev.epicgames.com/community/api/documentation/image/ecea61a4-35a3-41bb-8c90-4dad86d3cea1?resizing_type=fit&width=1920&height=1080)

    Before Level Snapshot restore

    After Level Snapshot restore
19. The nDisplay view updates with the changes you make in the Unreal Editor instance.

    [![nDisplay view updates](https://dev.epicgames.com/community/api/documentation/image/d4454d0d-c63f-458f-8e7e-7c23e21ea6c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4454d0d-c63f-458f-8e7e-7c23e21ea6c7?resizing_type=fit)
20. Select **InnerCamera\_A** under the nDisplay Root Actor and move it around the scene to see the inner frustum move in the nDisplay view.

These steps showed how to run the project on a single computer. You can use similar steps and modify the nDisplay Config that represents the real stage to test on your own LED volume.

## mGPU and Multi-Screen Cluster

[![The In-Camera VFX Production Test shoot in progress](https://dev.epicgames.com/community/api/documentation/image/128a0a52-abf0-408e-944d-650cb03c5415?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/128a0a52-abf0-408e-944d-650cb03c5415?resizing_type=fit)

The production leveraged multi-GPU to improve performance during the shoot. Rather than relying on a single GPU to render all viewports, a second GPU was dedicated to rendering only what appeared in-camera, to allow for the highest fidelity where it counted most. Refer to the [nDisplay Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-overview-for-unreal-engine) to learn how to use mGPU in a project.

Unreal Engine includes the **Stage Monitor** tool so you can receive reports associated with specific events from all the nDisplay cluster nodes in one application. You can have the tool enter a critical state while filming so you can easily notice events that could affect your shot. For more on how to use this tool, refer to [Stage Monitor](https://dev.epicgames.com/documentation/en-us/unreal-engine/stage-monitor-with-unreal-engine).

## Remote Control

With [Remote Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-for-unreal-engine), the production team, while on set, was able to control the displays and virtual environment dynamically from a web application running on a tablet. Exposed controls from the project included lighting, color grading of the displays, and modifying the position and rotation of the stage in the virtual environment.

[![Using Remote Control to control the stage](https://dev.epicgames.com/community/api/documentation/image/28a80824-373c-4cde-b7aa-5a82bc494253?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28a80824-373c-4cde-b7aa-5a82bc494253?resizing_type=fit)

### Using Remote Control

In the [Getting Started](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine) section, you used an Unreal Editor instance to make changes to the scene and see the updates immediately in the nDisplay render. This section shows how to do the same thing using the Remote Control Web Application designed for the project.

Follow these steps to view the Remote Control Web Application designed for this project, and move the nDisplay Root Actor remotely:

1. In the **Content Browser**, go to **TheOrigin > Content > Tools > RemoteControl** and double-click **RCP\_NantStudios** to open the Remote Control Preset in the **Remote Control Panel**.

   [![Open the Remote Control Preset in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/6cb644a7-854f-4fc8-85ea-3e89db047dbb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cb644a7-854f-4fc8-85ea-3e89db047dbb?resizing_type=fit)
2. The Remote Control Panel shows all the exposed parameters in the [Remote Control Preset](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-presets-and-web-application-for-unreal-engine). Launch the web application by clicking the angled arrow icon in the top right of the panel.

   [![Launch the web application from the Remote Control panel](https://dev.epicgames.com/community/api/documentation/image/f831a1b0-74e4-4d03-aaaf-4dbf827254de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f831a1b0-74e4-4d03-aaaf-4dbf827254de?resizing_type=fit)

   If there is no option to launch the web application in the Remote Control Panel, ensure the web application was built properly. You may need to modify the Remote Control section of the Project Settings to build it on your computer. Scan the Output Log in the Unreal Editor for errors.
3. You might need to rebind properties to work with the level and stage you have open.

   [![Rebinding properties in the Remote Control panel](https://dev.epicgames.com/community/api/documentation/image/baabe5e6-d502-4a37-933d-364cd2ca600d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/baabe5e6-d502-4a37-933d-364cd2ca600d?resizing_type=fit)
4. Switch to the **Stage** tab of the Remote Control Web Application.
5. Move the joysticks to change the location of the nDisplay Root Actor.

### Designing the Web Application

The [Remote Control Web Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-presets-and-web-application-for-unreal-engine) is a plugin that provides a companion web application to Remote Control. The web application includes a UI builder so you can create and customize your own web application without any code.

To switch to the UI builder of the Remote Control Web Application, toggle the **Control** button to **Design**, and modify the UI for the project. Save the **Remote Control Preset Asset** to save changes to the Remote Control Web Application's UI design.

[![Remote Control Design mode to modify UI](https://dev.epicgames.com/community/api/documentation/image/da768e9f-58fb-4ea7-9359-bb8810d1bca6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da768e9f-58fb-4ea7-9359-bb8810d1bca6?resizing_type=fit)

The following list describes the controls exposed in each tab of the Remote Control Web Application designed for this production.

* **Stage**: Combines the controls for the Stage Position and Rotation within the Level.

  [![Stage controls](https://dev.epicgames.com/community/api/documentation/image/6c7de9fb-06c7-4347-832e-7cdb256a7fa7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c7de9fb-06c7-4347-832e-7cdb256a7fa7?resizing_type=fit)
* **Viewport Settings**: Combines the controls for the global Viewport Screen Percentage and per-viewport Screen Percentage parameters.

  [![Viewport settings controls](https://dev.epicgames.com/community/api/documentation/image/796c0dae-047a-4f15-aa15-2c98ba3158ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/796c0dae-047a-4f15-aa15-2c98ba3158ca?resizing_type=fit)
* **Color Correction**: Combines the controls for global Color Correction and per-viewport Color Correction parameters.

  [![Color correction controls](https://dev.epicgames.com/community/api/documentation/image/edea4971-c08d-43eb-874d-332079193a7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/edea4971-c08d-43eb-874d-332079193a7c?resizing_type=fit)
* **LightCard**: Combines the controls for Light Cards.

  [![Light cards controls](https://dev.epicgames.com/community/api/documentation/image/4353c267-0e8b-4c57-86f7-5d48e62a364b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4353c267-0e8b-4c57-86f7-5d48e62a364b?resizing_type=fit)
* **Snapshot**: Shows all Level Snapshots in the project, and combines controls for taking and applying Level Snapshots. See [Level Snapshots](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-snapshots-in-unreal-engine) for more details.

  [![Level Snapshot controls](https://dev.epicgames.com/community/api/documentation/image/d289de31-8137-4b67-84bb-50f83a4e3168?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d289de31-8137-4b67-84bb-50f83a4e3168?resizing_type=fit)

## Color Grading and OCIO

In order to preserve accurate and consistent color across the pipeline, the art and stage teams leveraged [OpenColorIO (OCIO)](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine) to standardize color space conversions. These color space conversions accounted for display differences between monitors, LED panels, and production cameras.

A sample OCIO configuration and its look- up tables (LUTs) are included in the OCIO Plugin. This project has an example OCIO Configuration Asset that references this OCIO configuration and is assigned to both nDisplay Config Assets. You can find the OCIO Configuration Asset in **TheOrigin/Content/OCIO**.

To learn more about creating OCIO configurations and color space conversions for your displays, see [In-Camera VFX Camera Calibration](https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine).

Follow these steps to use your own OCIO configuration in the project:

1. In the **Content Browser**, right-click and select **Miscellaneous > OpenColorIOConfiguration** to create a new **OpenColorIO Configuration Asset**.

   [![Add an OCIO configuration asset](https://dev.epicgames.com/community/api/documentation/image/d728665d-2ad7-48bb-b47f-55502114b9df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d728665d-2ad7-48bb-b47f-55502114b9df?resizing_type=fit)
2. Double-click the new asset to open its editor.
3. In the Asset Editor, under the **Config** section, set the **Configuration File** field to the path of your OCIO configuration file on disk.

   [![Set the path to the OCIO configuration file](https://dev.epicgames.com/community/api/documentation/image/01c9b026-1620-4adc-8a32-e00cbf8c67a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01c9b026-1620-4adc-8a32-e00cbf8c67a5?resizing_type=fit)
4. Click **Reload and Rebuild** to load the OCIO configuration.
5. When the OCIO configuration is successfully loaded, expand the **Color Space** section.
6. Add the Source and Destination color spaces you wish to use. The options available are determined by the OCIO config you specified.

   [![Add source and destination color spaces](https://dev.epicgames.com/community/api/documentation/image/26a9c4df-6665-410c-b758-810cd3714a01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/26a9c4df-6665-410c-b758-810cd3714a01?resizing_type=fit)
7. To apply this configuration to your nDisplay viewport, open the level containing your **nDisplay Config Asset**, and search for **OCIO** in the **Details Panel** of the actor. Ensure that you have **Enable Viewport OCIO** set to true.
8. Expand **All Viewports Color Configuration:**

   1. Specify the Config asset you want to use.
   2. Set the Source and Destination color spaces.

      [![Set the Source and Destination color spaces](https://dev.epicgames.com/community/api/documentation/image/38b61529-18d0-4ff6-9e46-414082d019ef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38b61529-18d0-4ff6-9e46-414082d019ef?resizing_type=fit)

These steps demonstrate how to add your own OCIO configuration to the project. You can also set OCIO configurations per viewport and separately on the inner frustum. For more information, refer to [Color Management in nDisplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-in-ndisplay-in-unreal-engine).

## GPU Lightmass and Multi-User

The production team used the new [GPU Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/gpu-lightmass-global-illumination-in-unreal-engine) feature to bake the scenes' lighting and thus minimize how long the production had to wait for lighting changes in their multi-GPU and multi-user environment. Light baking occurred on a single multi-GPU workstation and then was distributed over the network through the multi-user session. This meant that the scene could be baked quickly and reloaded on the LED walls without needing to close and relaunch the cluster.

Follow these steps to use GPU Lightmass to bake lighting for the scene:

1. In the **Toolbar**, click the arrow next to **Build** and select **GPU Lightmass** from the dropdown.

   [![Select GPU Lightmass in the Build dropdown menu](https://dev.epicgames.com/community/api/documentation/image/56e551ce-4d18-4fc0-bb5e-b60b03d13d3e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56e551ce-4d18-4fc0-bb5e-b60b03d13d3e?resizing_type=fit)
2. In the **GPU Lightmass** window, click **Build Lighting** to begin your bake.

   [![Build Lighting using GPU Lightmass](https://dev.epicgames.com/community/api/documentation/image/1cd87bf3-c965-4c4b-8aa7-b3769749ce1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1cd87bf3-c965-4c4b-8aa7-b3769749ce1b?resizing_type=fit)
3. When the lighting finishes building, in the main menu choose **File > Save All** to transmit the changes to the other computers in the multi-user session.

   [![Save All to transmit the baked lighting](https://dev.epicgames.com/community/api/documentation/image/54e21f06-747d-482a-8e81-c8862fb9a2c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54e21f06-747d-482a-8e81-c8862fb9a2c8?resizing_type=fit)

Instead of sharing all changes with the other computers in the multi-user session, you can also choose what changes to transmit.

1. In the main menu, choose **File > Choose Files to Save…**

   [![Choose files to save](https://dev.epicgames.com/community/api/documentation/image/9c3e0532-3381-477f-b637-3cb56b6c96cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c3e0532-3381-477f-b637-3cb56b6c96cd?resizing_type=fit)
2. Select only the levels and build data you want to save and transfer.

   [![Select baked lighting files to save and transmit](https://dev.epicgames.com/community/api/documentation/image/0485df86-7f10-4d0e-814e-f5ec0e71bcc9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0485df86-7f10-4d0e-814e-f5ec0e71bcc9?resizing_type=fit)
3. Click **Save Selected** to transmit the changes to the other computers in the multi-user session.

For more on the settings you can change for your lightmass bakes, refer to [GPU Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/gpu-lightmass-global-illumination-in-unreal-engine).

Transferring GPU Lightmass bakes through the multi-user session is an experimental feature. Scenes that produce large BuildData files may experience issues with the transfer. If this happens, you can:

1. Check your updated levels and BuildData into source control.
2. Through source control, sync the changes to your render nodes to distribute the updated lightmaps.

## Level Snapshots

The production team used [Level Snapshots](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-snapshots-in-unreal-engine) to save configurations of the Actors in a Level for each scene. Once Level Snapshots were created, the team was able to restore the scene later to exactly how it was set up for a specific shot. Level Snapshots also track changes to the nDisplay Root Actor, so modifications to the inner frustum and color grading can be saved and applied to the nDisplay renders at any time.

The following sections describe how to use the filters and presets included in the project. To learn about creating your own filters and other features in the tool, refer to [Level Snapshots](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-snapshots-in-unreal-engine).

### Filtering with Level Snapshots

Included in the project is an example **Blueprint Level Snapshot Filter** that lets you filter Actors in the Level Snapshot changes by their Class. You can find the filter **LSF\_FilterByClass** in **TheOrigin/Content/Tools/LevelSnapshotFilters**. This section shows how to use this filter in the project.

[![The Blueprint Level Snapshot Filter](https://dev.epicgames.com/community/api/documentation/image/3407312c-17a7-4efb-adba-ed1fdfebacd7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3407312c-17a7-4efb-adba-ed1fdfebacd7?resizing_type=fit)

Diagram showing what devices were used and how they communicated with each other on stage. Click image to expand.

Follow these steps to filter Level Snapshot changes and apply them to your project:

1. In Unreal Editor's **Content Browser**, go to **TheOrigin > Content > StageLevels > NantStudiosSimple > StageLevels** and double-click **CaveEntrance\_NantStudiosSimple** to open the Level.
2. In the **Toolbar**, click the arrow next to the **Level Snapshots** button and select **Open Level Snapshots Editor** from the dropdown.

   [![Open Level Snapshot Editor](https://dev.epicgames.com/community/api/documentation/image/8fc556fe-7573-4787-8ea9-9f077e557dd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8fc556fe-7573-4787-8ea9-9f077e557dd3?resizing_type=fit)
3. There are two Level Snapshots already created for the Level CaveEntrance\_NantStudiosSimple. Double-click **CaveEntrance\_NantStudiosSimple\_SetupA** to see how the Actors saved in the Level Snapshot differ from the current state of the Level.

   [![The In-Camera VFX Production Test Level Snapshots](https://dev.epicgames.com/community/api/documentation/image/d409cdf9-e3bc-48ce-8e83-f1e173de65a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d409cdf9-e3bc-48ce-8e83-f1e173de65a0?resizing_type=fit)
4. Click **Filter Group**.

   [![The Setup A Level Snapshot selected](https://dev.epicgames.com/community/api/documentation/image/8c41330b-5508-428b-bc59-399bb1a1cb3c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c41330b-5508-428b-bc59-399bb1a1cb3c?resizing_type=fit)
5. Click **Add Filter** and in the dropdown choose **Blueprint Filters > LSF Filter by Class**.

   [![Add the LDF Filter by Class Blueprint filter](https://dev.epicgames.com/community/api/documentation/image/ad3f260d-0a6f-4b94-a1d6-c58f4481dbde?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad3f260d-0a6f-4b94-a1d6-c58f4481dbde?resizing_type=fit)
6. Click **LSF Filter by Class** in the Filter Group.

   [![Click the filter](https://dev.epicgames.com/community/api/documentation/image/453f0ab3-282d-431a-8565-137a54110250?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/453f0ab3-282d-431a-8565-137a54110250?resizing_type=fit)
7. In the **Default** section next to **Class**, click the dropdown and search for **Light Card**.

   [![Search for Light Card](https://dev.epicgames.com/community/api/documentation/image/67f2fe4b-fe03-4652-955a-e68268709643?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67f2fe4b-fe03-4652-955a-e68268709643?resizing_type=fit)
8. Click the **Refresh Results** button to apply the filter changes.

   [![Refresh Results to apply filter](https://dev.epicgames.com/community/api/documentation/image/6bb2ee2a-2f88-47ff-9a1d-d78617c44d21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bb2ee2a-2f88-47ff-9a1d-d78617c44d21?resizing_type=fit)
9. Now, only changes to Light Card Actors are shown. To turn off the filter, right-click the filter and select **Ignore Filter**.

   [![Only changes to Light Card Actors shown](https://dev.epicgames.com/community/api/documentation/image/96a0f1a9-7536-4db7-804f-61061ad9feea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96a0f1a9-7536-4db7-804f-61061ad9feea?resizing_type=fit)
10. Click **Refresh Results** and see the nDisplay Root Actor appear in the list again.

    [![Disabled filter means all Actors are shown](https://dev.epicgames.com/community/api/documentation/image/9315e697-815a-4c0d-bf22-fd56fd6ec1bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9315e697-815a-4c0d-bf22-fd56fd6ec1bc?resizing_type=fit)

### Using Presets with Level Snapshots

With Level Snapshot Presets, you can set up logic using Blueprint and C++ filters and save it as a preset. Later, you can load the preset to use this logic again. Included in the project is an example Level Snapshot Preset located in **TheOrigin/Content/Tools/LevelSnapshotPresets**.

This preset strings multiple instances of the **Filter by Class** Blueprint Filter together with the OR boolean so only Actors that match any of those Classes will appear. The Classes used in the preset are: LightCards, Stages, Cameras, SyncTestBall, ColorCorrectRegion, and PostProcessVolume.

Follow these steps to use the Level Snapshot Preset in the project.

1. In the **Content Browser**, go to **TheOrigin > Content > StageLevels > NantStudiosSimple > StageLevels** and double-click **CaveEntrance\_NantStudiosSimple** to open the Level.
2. In the **Toolbar**, click the arrow next to the **Level Snapshots** button and select **Open Level Snapshots Editor** from the dropdown.

   [![Open Level Snapshot Editor](https://dev.epicgames.com/community/api/documentation/image/91dbee56-7a47-425a-bcb7-9d7f6421f9ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/91dbee56-7a47-425a-bcb7-9d7f6421f9ee?resizing_type=fit)
3. There are two Level Snapshots already created for the Level CaveEntrance\_NantStudiosSimple. Click **Load/Save Filter** and choose **ExampleStagePreset**.

   [![Load the Example Stage Preset filter](https://dev.epicgames.com/community/api/documentation/image/6dfa2852-fd90-42be-a49c-bb0bfae62342?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6dfa2852-fd90-42be-a49c-bb0bfae62342?resizing_type=fit)
4. Double-click **CaveEntrance\_NantStudiosSimple\_SetupA** to see how the Actors saved in the Level Snapshot differ from the current state of the Level.

   [![The Preset Filter loaded](https://dev.epicgames.com/community/api/documentation/image/d85a3abb-8bff-47dc-a550-e8179e98a6fb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d85a3abb-8bff-47dc-a550-e8179e98a6fb?resizing_type=fit)
5. When the Level Snapshot is opened, only the Actors that fit the filter loaded from the preset are shown.

   [![The Setup A Level Snapshot filtered by the Preset](https://dev.epicgames.com/community/api/documentation/image/439d72c8-5d29-464c-b668-bf6963b18e06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/439d72c8-5d29-464c-b668-bf6963b18e06?resizing_type=fit)

## Project Structure

The In-Camera VFX Production Test is a great example to see how to structure an Unreal Project for Virtual Production. The following folders define the overall structure for the project's content and separate it into relevant categories.

* [Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine#assets)
* [Envs](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine#environments)
* [OCIO](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine#ocio)
* [StageLevels](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine)
* [Stages](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine#stages)
* [Tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine#tools)

### Assets

This folder typically contains all assets for creating Characters, Environments, and FX. Level Assets are not included here. The following list is how the assets were categorized for this sample project.

* **Atlases**
* **Decals**
* **FX**
* **IES**
* **Landscape**
* **Materials**
* **MS\_Presets**
* **Props**
* **Rocks**
* **Scatter**
* **Sky**
* **Textures**
* **Vegetation**

### Environments

Three environments from the shoot are included in the project:

* CaveEntrance

  [![The Cave Entrance environment](https://dev.epicgames.com/community/api/documentation/image/153bf112-6fcf-4e24-9921-719a030547e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/153bf112-6fcf-4e24-9921-719a030547e2?resizing_type=fit)
* CavePath

  [![The Cave Path environment](https://dev.epicgames.com/community/api/documentation/image/30af3277-1938-4846-92b0-b842a8ec8ce3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30af3277-1938-4846-92b0-b842a8ec8ce3?resizing_type=fit)
* SpaceJunkyard

  [![The Space Junkyard environment](https://dev.epicgames.com/community/api/documentation/image/45f297b0-6954-4dfb-9426-af280da77018?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/45f297b0-6954-4dfb-9426-af280da77018?resizing_type=fit)

#### Environment Structure

Since source control only lets you exclusively check out binary assets, such as `.umap` files, each artist working on an environment at the same time must work in their own level. The solution to this is to divide an environment up into multiple [sublevels](https://dev.epicgames.com/documentation/en-us/unreal-engine/managing-multiple-levels-in-unreal-engine) based on the type of Actors in each.

For example, a lighting artist would work in the lighting sublevel, and an FX artist in the FX sublevel. It is also common to have multiple GEO levels that divide the environment up into regions, each being worked on by a different artist. The number and types of sublevels used should be dependent on the needs of the production.

The following are the folders used for each environment in this project:

* **LevelSnapshots**: Level Snapshot Assets associated with the Level.
* **SubLevels**: In this project, each Level was separated into the Caustics, FX, Geo, and Lighting sublevels.
* **Level Asset**: Level Assets follow a {LevelName}\_{Descriptor} structure. The \_P suffix is given to the Persistent Level, which acts as a container for the sublevels. Open this Level Asset to view the full environment composed of all the sublevels.

### OCIO

This folder contains the OpenColorIO Configuration Assets. There is one Asset for this project: ExampleOCIO. For more details on using OCIO in this project, refer to the [Color Grading and OCIO section](https://dev.epicgames.com/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine) on this page.

[![The Example OCIO asset](https://dev.epicgames.com/community/api/documentation/image/7d3d6207-cca6-4598-a242-acb7c5a798a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d3d6207-cca6-4598-a242-acb7c5a798a1?resizing_type=fit)

### Stage Levels

The folder contains all the Level Assets that have both the environment and stage Actors. Open these assets when you want to render with nDisplay. The stage levels are categorized by the stage used in the Level Asset. This sample project uses the following structure to match the stages:

* NantStudios

  + CaveEntrance\_NantStudios
  + CavePath\_NantStudios
  + SpaceJunkyard\_NantStudios
* NantStudiosSimple

  + CaveEntrance\_NantStudiosSimple
  + CavePath\_NantStudiosSimple
  + SpaceJunkyard\_NantStudiosSimple

### Stages

This folder contains the nDisplay Configurations which describe the topology of the LED volumes. The production used one stage for all the shots: Nant Studios. A simpler version of the stage is provided as well so you can render the front walls on a single desktop.

[![The NantStudios LED stage](https://dev.epicgames.com/community/api/documentation/image/96392b43-1f00-4a49-9b9c-c612d0b6f88a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96392b43-1f00-4a49-9b9c-c612d0b6f88a?resizing_type=fit)

Click image to expand.

#### NantStudios

* **Config**: An nDisplay Config Asset for the stage that defines the topology of the LED volume and how to render on it.

  [![The NantStudios nDisplay Config asset](https://dev.epicgames.com/community/api/documentation/image/4cc82b82-d40d-4b59-bb70-7746b8484e86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4cc82b82-d40d-4b59-bb70-7746b8484e86?resizing_type=fit)
* **LEDMeshes**: Static Meshes and materials with the LED panel resolution used in the **nDisplay Config Asset**.

  [![NantStudios LED meshes](https://dev.epicgames.com/community/api/documentation/image/7d2bfcc0-6f1f-48d3-acda-92886c11cd00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d2bfcc0-6f1f-48d3-acda-92886c11cd00?resizing_type=fit)
* **LiveLinkPresets**: These are previously created configurations for Live Link that are required to load LiveLink sources on the nDisplay nodes at launch. The default preset is specified in **Project Settings > Live Link > Default Live Link Preset.** They can also be used to quickly reload different sources in an editor environment.
* **NantStudios\_Stage**: A Level Asset that contains only the Actors that represent the stage, such as the **nDisplay Root Actor**, **ICVFX Cameras**, and **Light Cards**.

#### Simple Nant Studios

* **Config**: An nDisplay Config Asset for the stage that defines the topology of the LED volume and how to render on it. The topology looks the same as the Nant Studios configuration, but only two of the front walls are set up to render.
* **NantStudiosSimple\_Stage**: A Level Asset that contains only the Actors that represent the stage, such as the **nDisplay Root Actor**, **ICVFX Cameras**, and **Light Cards**.

### Tools

This folder contains custom Blueprint controls, Level Snapshot Filters and Presets, and Remote Control Presets. The following list describes each tool.

* **CaveMaterialControl**: A blueprint controller for various Material Parameter Collections used by objects in the scene. Contains controls for things such as caustic speed, light shaft intensity, and global color shifts for the rocks.
* **HierarchicalInstanceConverter**
* **HolePunch**: A spherical actor used to create a hole in the geometry of the cave. This was used on the day of the shoot to create an additional light shaft.
* **InnerFrustumCamera**: A CineCameraActor with a LiveLinkComponent. This Blueprint simplifies the camera tracking by not requiring the user to manually add an instanced LiveLinkComponent to the scene actor.
* **LevelSnapshotFilters**: Custom Blueprint Filters for Level Snapshots.
* **LevelSnapshotPresets**: Presets of groups of filters for Level Snapshots.
* **RemoteControl**: Remote Control Presets.
* **SyncTestBall**: This tool creates a bouncing red ball used to test synchronization. Place the ball in the scene so that it appears on the seam between two walls. A visible tearing of the ball occurs at the seam if the synchronization is not functioning properly.

## Cvars

To improve performance while rendering with nDisplay on stage, the production team used the cvars in the table below to tweak settings. You can set cvars during an nDisplay session in Switchboard and have them applied to the cluster.

To set cvars in Switchboard:

1. Open Switchboard.
2. Under the **nDisplay Monitor** tab, in the **Console:** text box, enter the cvar and the desired value, if applicable.
3. Click **Exec**.

[![The nDisplay Monitor Console](https://dev.epicgames.com/community/api/documentation/image/bb3afaa3-deaa-4385-8edb-cca03408fac8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb3afaa3-deaa-4385-8edb-cca03408fac8?resizing_type=fit)

The following values are what were used for the In-Camera VFX Production Test. You might need to use different values depending on the content in your project and what look you want to achieve.

| Cvar | Value | Description |
| --- | --- | --- |
| `r.ExrReadAndProcessOnGPU` | N/A | Switches EXR playback between CPU and GPU. When enabled for the GPU, Unreal Engine 4 can load large, uncompressed EXR files directly into a Structured Buffer and process them on the GPU. |
| Ray Tracing |  |  |
| --- | --- | --- |
| `r.RayTracing.ForceAllRayTracingEffects` | 0 | Forces all ray tracing effects either on or off. Options for value include:   * -1: Do not force (default) * 0: Disable all ray tracing effects * 1: Enable all ray tracing effects   Setting this cvar to 0 turns off all the additional ray tracing features that are enabled by default. When using GPU Lightmass, which requires ray tracing, you can still use GPU-accelerated light baking. This cvar can also be useful for figuring out how much performance is required with ray tracing enabled. |
| `r.RayTracing.Reflections.MaxRoughness` | 0.2 | Sets the maximum roughness for visible ray tracing reflections (default = -1 (max roughness driven by post processing volume)). This guarantees that only Materials with roughness values lower than 0.2 will have ray-traced reflections. |
| `r.RayTracing.Reflections.MaxRayDistance` | 500 | Sets the maximum ray distance for ray traced reflection rays. When ray shortening is used, the skybox will not be sampled in the RT reflection pass and will be composited later, together with local reflection captures. Negative values turn off this optimization (default = -1 (infinite rays)). Using a value other than -1 will help reduce the amount of ray tracing that is done in a scene. |
| `r.RayTracing.Reflections.SortMaterials` | 0 | Determines whether reflected materials will be sorted before shading. Options:   * 0: Disabled * 1: Enabled, using Trace > Sort > Trace (Default) |
| `r.DiffuseIndirect.Denoiser` | 2 | Denoising options (default = 1) |
| `r.RayTracing.Reflections` | 0 | Turn OFF only ray tracing reflections in your level. This is useful in case you still want to use ray-traced shadows or other ray tracing features, and not pay the cost of ray-traced reflections. Options:   * -1: Value driven by the postprocess volume (default) * 0: Use traditional rasterized SSR. * 1: Use ray-traced reflections. |
| `r.RayTracing.Geometry.Landscape` | 0 | Include landscapes in ray tracing effects (default = 1 (landscape enabled in ray tracing)) In order to optimize the levels that needed ray-traced reflections, we disabled landscape ray-tracing as it was not adding much to the final look, and disabling it gave us some performance boost. |
| `r.RayTracing.Reflections.ScreenPercentage` | 50 | Screen percentage the reflections should be ray traced at (default = 100). If your scene doesn't have very shiny and clean reflections you can reduce this value and you will gain some performance. |
| Upscaling Resolution |  |  |
| --- | --- | --- |
| `r.ScreenPercentage` | 75 | Render in lower resolution and upscale for better performance (combined with the blendable post process setting). 75 is a good value for low aliasing and performance, verify with 'show TestImage'.  In percent, use >0 and <=100, larger numbers are possible (supersampling) but the downsampling quality is improvable. Numbers <0 are treated like 100. |
| `r.TemporalAA.Algorithm` | 1 | Algorithm to use for Temporal AA Options:   * 0: Gen 4 TAAU (default) * 1: Gen 5 TAAU (experimental)   This will turn ON our new Gen5 TAAU in case some resolution upscaling is needed . |
| `r.TemporalAA.Upsampling` | 1 | Whether to perform primary screen percentage with temporal AA or not. Options:   * 0: Perform the spatial upscale pass independently of TAA (default). * 1: TemporalAA performs the spatial and temporal upscale using the screen percentage method. |
| SSGI |  |  |
| --- | --- | --- |
| `r.SSGI.Enable` | 0 | Whether to enable or disable Screen Space GI Options:   * 0: Disable * 1: Enable   Turns OFF Screen Space GI. |
| `r.SSGI.HalfRes` | 1 | Whether to perform SSGI at half resolution. Options:   * 0: Disable (defaults) * 1: Enable |
| `r.SSGI.Quality` | 1 | Quality setting to control the number of rays shot with SSGI, between 1 and 4 (defaults to 4). |
| Volumetric Fog |  |  |
| --- | --- | --- |
| `r.VolumetricFog.GridPixelSize` | 6 | XY size of a cell in the voxel grid, in pixels. Lower values produce better Volumetric Fog Quality but it will affect performance. |
| `r.VolumetricFog.GridSizeZ` | 96 | How many Volumetric Fog cells to use in the Z axis. Higher values can help increase accuracy and reduce noise but it can impact performance. |
| `r.VolumetricFog` | 0 | Whether to enable the Volumetric Fog feature. Options   * 0: Disabled * 1: Enabled   This can be used to quickly turn OFF Volumetric Fog and determine how much performance it uses. |
| Rendering |  |  |
| --- | --- | --- |
| `ShowFlag.DirectLighting` | 0 | This cvar is useful for quickly disabling direct lighting in order to understand what is baked and what isn't, and its performance implications. Options:   * 0: Disable the showflag. * 1: Enable the showflag. * 2: Do not override this showflag (default). |
| `r.SetNearClipPlane` | 150 | Set the near clipping plane (in cm). This cvar will allow you to modify the Near Clip Plane in case you want to quickly remove any geometry that is in front of your render camera. |
| `r.TextureStreaming` | 0 | Defines whether texture streaming is enabled, which can be changed at run time. Options   * 0: Disabled * 1: Enabled (default) |
| `r.Streaming.PoolSize` | 3600 | -1: Default texture pool size, otherwise the value is the size in MB. This cvar can be used to increase the texture pool size at runtime in order to allow higher mipmaps to be loaded, if the pool size originally was set too low and your hardware allows a higher texture pool size. |
| `r.DFShadowScatterTileCulling` | 1 | Whether to use the rasterizer to scatter objects onto the tile grid for culling. Options   * 0: Disabled * 1: Enabled |
| `r.ForceLOD` | 5 | LOD level to force, -1 is disabled. This is useful for testing how much performance or quality can be gained by forcing a specific LOD on the scene. |

* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [in-camera vfx](https://dev.epicgames.com/community/search?query=in-camera%20vfx)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Stage Setup and Hardware](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#stage-setup-and-hardware)
* [Getting Started](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#getting-started)
* [mGPU and Multi-Screen Cluster](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#m-gpu-and-multi-screen-cluster)
* [Remote Control](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#remote-control)
* [Using Remote Control](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#using-remote-control)
* [Designing the Web Application](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#designing-the-web-application)
* [Color Grading and OCIO](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#color-grading-and-ocio)
* [GPU Lightmass and Multi-User](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#gpu-lightmass-and-multi-user)
* [Level Snapshots](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#level-snapshots)
* [Filtering with Level Snapshots](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#filtering-with-level-snapshots)
* [Using Presets with Level Snapshots](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#using-presets-with-level-snapshots)
* [Project Structure](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#project-structure)
* [Assets](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#assets)
* [Environments](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#environments)
* [Environment Structure](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#environment-structure)
* [OCIO](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#ocio)
* [Stage Levels](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#stage-levels)
* [Stages](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#stages)
* [NantStudios](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#nant-studios)
* [Simple Nant Studios](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#simple-nant-studios)
* [Tools](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#tools)
* [Cvars](/documentation/en-us/unreal-engine/incamera-vfx-production-test-sample-project-for-unreal-engine?application_version=5.7#cvars)

Related documents

[GPU Lightmass Global Illumination

![GPU Lightmass Global Illumination](https://dev.epicgames.com/community/api/documentation/image/4ad4f9df-e2e3-4507-92e4-7071d2e49cd8?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/gpu-lightmass-global-illumination-in-unreal-engine)
