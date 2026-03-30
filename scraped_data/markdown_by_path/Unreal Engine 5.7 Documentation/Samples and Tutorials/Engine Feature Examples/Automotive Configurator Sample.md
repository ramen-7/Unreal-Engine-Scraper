<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7 -->

# Automotive Configurator Sample

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
7. Automotive Configurator Sample

# Automotive Configurator Sample

How to setup the Automotive Configurator sample project, render a commercial with Movie Render Queue, and edit with the Variant Manager.

![Automotive Configurator Sample](https://dev.epicgames.com/community/api/documentation/image/8d9933a6-6d5b-4ad4-9e48-a9807a0d4fa4?resizing_type=fill&width=1920&height=335)

 On this page

The automotive industry is increasingly turning to real-time solutions, such as Unreal Engine (UE), to drive their visualization and commercial projects. The **Automotive Configurator** sample is built using Epic Games' best practices for the creation of a vehicle configurator, a common use case for 3D visualization artists in the automotive industry.

The Automotive Configurator sample demonstrates the use of the following features:

* [Variant Manager](https://dev.epicgames.com/documentation/en-us/unreal-engine/variant-manager-template-overview)
* [Lumen](building-virtual-worlds/lighting-and-shadows/global-illumination/lumen)
* [Path Tracer](building-virtual-worlds/lighting-and-shadows/ray-tracing-and-path-tracing/path-tracer)
* [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine)
* [Chaos Cloth Solver](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine)
* [Control Rig](animating-characters-and-objects/ControlRig)
* [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview)
* [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue)

## How To Use the Automotive Configurator

### Downloading the Sample

To create a project with the Automotive Configurator sample, follow these steps:

1. Access the [Automotive Configurator](https://fab.com/s/f54cb8fd6f65) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project in Fab in Launcher, or in the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.
4. Download the [Automotive Materials](https://fab.com/s/da380b9a6082) and [Automotive Salt Flats](https://fab.com/s/db62e7a8704a) assets from Fab.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

This project requires the following plugins (enabled by default):

* **Movie Render Queue**
* **Color Correct Regions**
* **Control Rig**
* **Variant Manager**

This may require you to restart the Editor.

### Navigating the User Interface

The Automotive Configurator is built using the [Product Configurator](https://dev.epicgames.com/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine) template as a base. Using the [Variant Manager](https://dev.epicgames.com/documentation/en-us/unreal-engine/variant-manager-template-overview), you can choose from a variety of saved Static Mesh configurations called **Variants** to customize your Audi A5.

[![Configurator user Interface](https://dev.epicgames.com/community/api/documentation/image/8ed8c9cf-60ad-40b0-aff9-35c4aeba66d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8ed8c9cf-60ad-40b0-aff9-35c4aeba66d6?resizing_type=fit)

You can control the configurator using the interface buttons located at the bottom of the screen:

| Number | Description |
| --- | --- |
| **1** | Configurator Mode |
| **2** | Commercial Mode |
| **3** | Car Paint Color |
| **4** | Wheel Style |
| **5** | Trim Color |
| **6** | Leather Color |
| **7** | Seat Upholstery Style |
| **8** | Toggle Path Tracer |
| **9** | Take Screenshot |
| **10** | Mute/Unmute |
| **11** | Camera Views |

The Automotive Configurator also includes focus points, represented by white flashing circles. These have been animated using [Control Rig](animating-characters-and-objects/ControlRig), Unreal Engine's Blueprint-based animation control system:

* **Open/Close Doors**: Open and close the car doors.
* **Open/Close Convertible Soft Top**: Open and close the convertible top by clicking on the roof control switch located by the rearview mirror in any of the interior views.
* **Open/Close Trunk**: Open and close the trunk lid.
* **Horn**: Honk the horn.
* **Start/Stop the Engine**: Click the Engine Start button to start or stop the engine. When the engine is started, the dash gauges and Audi Virtual Cockpit are powered and the front lights and tail lights are lit up.

### Rendering the Commercial View

Clicking the **Play** button in the Configurator will transport your customized vehicle to the Commercial mode.

[![Commercial user interface](https://dev.epicgames.com/community/api/documentation/image/cdeab1e1-c7fc-4e0b-ad18-eb6d2b0fae40?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cdeab1e1-c7fc-4e0b-ad18-eb6d2b0fae40?resizing_type=fit)

In Commercial mode, your vehicle becomes the star of your very own TV spot. This takes your vehicle through several camera shots often seen in car commercials. You can control the commercial using the following interface options:

| Number | Description |
| --- | --- |
| **1** | Stop |
| **2** | Play |
| **3** | Pause |
| **4** | Render Video |

Powered by [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview), the camera races across the salt flats, moving to highlight the wheels and interior. The car commercial takes advantage of [Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine) for real-time lighting and shadows, and can be saved to your computer thanks to the [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) runtime feature. Optional Path Tracer use

## Variant Manager

The Automotive Configurator is built on the Product Configurator template and uses the Variant Manager to store the various asset configurations used to customize your vehicle.

![Move the slider to see the different Trim variants](https://dev.epicgames.com/community/api/documentation/image/d4fb84e5-fe42-4231-affc-a3778f29fce9?resizing_type=fit&width=1920&height=1080)![Move the slider to see the different Trim variants](https://dev.epicgames.com/community/api/documentation/image/4502fabc-6548-4a80-8ec1-b256f35dddfd?resizing_type=fit&width=1920&height=1080)![Move the slider to see the different Trim variants](https://dev.epicgames.com/community/api/documentation/image/a778815a-c02b-4cb8-a4fd-e6816b2b8963?resizing_type=fit&width=1920&height=1080)

**Move the slider to see the different Trim variants**

Each configuration option is stored in an entry called a **Variant**. Each variant points to a property on an Actor that is changed when the variant is activated. Variants are arranged into Variant Sets and the data is used by the **BP\_Configurator** Blueprint to populate the user interface with options. In the image above, you can see that when different trim options are selected the Variant Manager applies that value to different static mesh components on the vehicle Actor.

For more information on using the Variant Manager, please see the [Variant Manager](https://dev.epicgames.com/documentation/en-us/unreal-engine/variant-manager-template-overview) documentation.

## Lumen Global Illumination and Reflections

Unreal Engine uses the [Lumen Global Illumination and Reflection](building-virtual-worlds/lighting-and-shadows/global-illumination/lumen) system to provide dynamic global illumination and shadows.

[![Audi A5 illuminated using Lumen](https://dev.epicgames.com/community/api/documentation/image/35ff0f02-0998-4e88-b5e8-917628fa3692?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35ff0f02-0998-4e88-b5e8-917628fa3692?resizing_type=fit)

The Automotive Configurator sample uses Lumen's ability to provide diffuse interreflection and indirect specular reflection to accurately reflect the salt flats environment off the tire rims and car, making the most of the Clear Coat properties of the Materials used from the Automotive Materials pack.

For more information on lighting your level with Lumen, see the [Lumen](building-virtual-worlds/lighting-and-shadows/global-illumination/lumen) documentation.

## Path Tracer

[Path Tracer](building-virtual-worlds/lighting-and-shadows/ray-tracing-and-path-tracing/path-tracer) is Unreal Engine's progressive, hardware-accelerated rendering mode. Designed to generate physically correct global illumination and reflection and refraction of materials, enabling Path Tracer can provide you with photorealistic renders with little to no additional setup.

![Audi A5 illuminated using Lumen](https://dev.epicgames.com/community/api/documentation/image/dc89cd0f-c7c7-4af4-91d1-5d00fa495304?resizing_type=fit&width=1920&height=1080)

![Audi A5 illuminated using Path Tracer](https://dev.epicgames.com/community/api/documentation/image/58a98832-04ed-4583-a651-1eae43cb9afd?resizing_type=fit&width=1920&height=1080)

Audi A5 illuminated using Lumen

Audi A5 illuminated using Path Tracer

Path Tracer features full integration with [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) and [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) making it ideal for Film and TV quality render outputs.

The Automotive Configurator sample gives you the option to toggle path tracing on from the interface to provide photorealistic output for screen captures or rendering during Commercial mode.

For information on using Path Tracer in your own projects, see the [Path Tracer](building-virtual-worlds/lighting-and-shadows/ray-tracing-and-path-tracing/path-tracer) documentation.

## Volumetric Clouds

The [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine) found in the sample use a physically-based cloud rendering system and a material-driven approach to create the sky that is seen on the salt flats.

[![Automotive Configurator sample](https://dev.epicgames.com/community/api/documentation/image/3e2c96f7-0c0a-4b56-9b6f-030905e8d4ae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e2c96f7-0c0a-4b56-9b6f-030905e8d4ae?resizing_type=fit)

The Epic Games team uses volumetric clouds to bring aesthetic touches to the salt flats, while also getting bounced light reflection on the car paint. The Volumetric Cloud component uses a Material Instance of the default cloud Material to accomplish these effects.

For more information on using the Volumetric Clouds system, please see our [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine) documentation.

## Chaos Cloth Solver

The Automotive Configurator sample uses the [Chaos Cloth Solver](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine) to simulate the physics interactions of the cloth convertible top.

Using the Cloth Painting workflow directly in the Engine, the Epic Games team is able to assign a variety of properties such as friction, constraints, drag, and stiffness to closely simulate the look and feel of the Audi A5's canvas soft top.

For more information on the Chaos Cloth Solver and in-engine Clothing Tool, please see the [Clothing Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine) documentation.

## Control Rig

The [Control Rig](animating-characters-and-objects/ControlRig/) system is a scriptable node-based rigging system that provides rigging and animation tools directly in the engine.

[![Control Rig convertable top skeleton](https://dev.epicgames.com/community/api/documentation/image/c736d98a-bfe8-4897-a522-6fee376faa63?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c736d98a-bfe8-4897-a522-6fee376faa63?resizing_type=fit)

In the Automotive Configurator, the Epic Games team uses Control Rig in two ways. The first is to create an adaptable skeletal mesh version of the car and create the animations for the wheels, doors, and trunk. The second is to create the animation for the convertible top.

The Audi A5 uses a skeleton with pivot locations for each movable element in the car. With this method, the main vehicle geometry does not need to be bound to the vehicle, and the skeletal mesh can be imported into Unreal quickly. Once imported, the mesh is added to a Blueprint, which attaches the rest of the vehicle components to the pivots and binds the skeleton to the Control Rig at runtime. This makes it easier to update the pivot locations if needed without having to go back to our DCC application.

Due to its complexity, the cloth convertible top is a separate piece with its own skeleton and Control Rig. A state machine tracks if the top is open or closed, and runs the correct transition animation when it is selected in the configurator application.

For more information on using Control Rig to animate in-engine, please see the [Control Rig](animating-characters-and-objects/ControlRig) documentation.

## Sequencer

Powering the Commercial mode, [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) is a robust keyframe animation system which you can use to create in-game cinematics.

[![Commervial view using Sequencer](https://dev.epicgames.com/community/api/documentation/image/c9ece5de-9e48-4531-8f20-02888c5ddf46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9ece5de-9e48-4531-8f20-02888c5ddf46?resizing_type=fit)

The Commercial mode uses a series of level sequences with animated cameras to showcase various configurable features on the car. The Epic Games team then uses **Movie Render Queue** to render and save the level sequences and assemble them using a non-linear editing program. This edited sequence is brought back into Unreal as a master sequence, where audio is added and the cameras, animation, and overall timing is refined. These sequences are found in the **CarConfigurator/Commercial/Sequences** folder.

For more information on using Sequencer in your projects, please see the [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) documentation.

## Movie Render Queue

Used to output the final commercial render, [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) is an engine feature that can export high-quality media. When used with Real-Time Ray Tracing, the final render can take advantage of advanced anti-aliasing, radial motion blur, and reduced noise in ray tracing:

[![Movie Render Queue at runtime](https://dev.epicgames.com/community/api/documentation/image/45649e13-6ea2-49bc-8d5c-1091ef9b371a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/45649e13-6ea2-49bc-8d5c-1091ef9b371a?resizing_type=fit)

The Epic Games team uses Blueprint to enable Movie Render Queue at runtime. With this, you can render and save a video of your commercial directly from the configurator.

For more information on using the Movie Render Queue feature, please see the [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue) documentation.

## Adding Art Assets to the Configurator

You can add new art assets to the Automotive Configurator by adding a new variant to the Level Variant Set. This process is similar for both Materials and Static Mesh assets. The example below describes how to add a new paint color to the configurator.

The Audi A5 in this sample makes use of the [Automotive Materials Pack](https://www.fab.com/listings/5dd132fe-ee32-4e8c-9cd3-7496547dfb29) for paint, leather, and trim options. To add additional colors to the interface, follow these steps:

1. Create a custom folder to hold your new Material and any texture samples that it may need. Do this by right clicking on the **CarConfigurator** folder and selecting **New Folder**. Name the new folder **Custom**.
2. If you are not adding a color that is already available within the sample, you will need to either create your paint sample using the tools available within the [Automotive Material Pack](https://dev.epicgames.com/documentation/en-us/unreal-engine/automotive-materials-pack-in-unreal-engine), or import and set up your Material. For this sample, you are duplicating an existing paint sample and editing it. For more information on importing textures and creating new Materials, see our [Material How-To](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials-tutorials) documentation.
3. Next, open the **CarConfigurator/Shared** folder and double click on the **CarVariants** Level Variant Set to open it in the Variant Manager.

   [![Opening the Level Variant](https://dev.epicgames.com/community/api/documentation/image/9214b6da-173b-4bed-90be-622a51c5f7ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9214b6da-173b-4bed-90be-622a51c5f7ea?resizing_type=fit)
4. To make sure that your new color is applied to all the required static meshes, you can duplicate an existing Variant. Open the **Paint, Trim**, or **Leather** Variant Sets and right click on the last variant in the list. From the menu, choose the **Duplicate** option.

   [![Variant duplicate](https://dev.epicgames.com/community/api/documentation/image/dbba9dd5-289b-410b-af7c-e181d57aae89?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dbba9dd5-289b-410b-af7c-e181d57aae89?resizing_type=fit)
5. Right click on your new variant and choose **Rename**. Create a new name that is appropriate for the color.

   [![Variant rename](https://dev.epicgames.com/community/api/documentation/image/20c0e77c-c186-4655-92de-8d0c192bdc19?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20c0e77c-c186-4655-92de-8d0c192bdc19?resizing_type=fit)
6. Click the **BP\_AudiA5** in the **Properties** panel to display the **Properties** and **Values** for the car. For each value in the Values column, click the drop down menu and select your new color, excluding the **SM\_trunkDetails** Material.

   [![Changing the Variant colors](https://dev.epicgames.com/community/api/documentation/image/62bd4fe0-97a9-4fcb-9f8b-3fbd67b0d50e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/62bd4fe0-97a9-4fcb-9f8b-3fbd67b0d50e?resizing_type=fit)

   Changing the Material for **SM\_trunkDetails** changes the license plate on the car.
7. Set the thumbnail image for your new variant by switching on the variant and positioning the **Viewport** camera to best display your new option.

   [![Setting the Viewport camera](https://dev.epicgames.com/community/api/documentation/image/20cb798b-6f22-47ae-b45a-ccd6dc665941?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20cb798b-6f22-47ae-b45a-ccd6dc665941?resizing_type=fit)
8. Then right click the variant in the **Variant Manager** choose the **Set from viewport** option.

   [![Variant thumbnail from viewport](https://dev.epicgames.com/community/api/documentation/image/a17dcb46-d981-41be-bc2c-65f3832606f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a17dcb46-d981-41be-bc2c-65f3832606f9?resizing_type=fit)
9. Test the sample by clicking the **Play** button in the Editor. Your new variant should appear in the user interface.

* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [ray tracing](https://dev.epicgames.com/community/search?query=ray%20tracing)
* [movie render queue](https://dev.epicgames.com/community/search?query=movie%20render%20queue)
* [variant manager](https://dev.epicgames.com/community/search?query=variant%20manager)
* [volumetric clouds](https://dev.epicgames.com/community/search?query=volumetric%20clouds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How To Use the Automotive Configurator](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#how-to-use-the-automotive-configurator)
* [Downloading the Sample](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#downloading-the-sample)
* [Navigating the User Interface](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#navigating-the-user-interface)
* [Rendering the Commercial View](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#rendering-the-commercial-view)
* [Variant Manager](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#variant-manager)
* [Lumen Global Illumination and Reflections](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#lumen-global-illumination-and-reflections)
* [Path Tracer](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#path-tracer)
* [Volumetric Clouds](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#volumetric-clouds)
* [Chaos Cloth Solver](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#chaos-cloth-solver)
* [Control Rig](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#control-rig)
* [Sequencer](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#sequencer)
* [Movie Render Queue](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#movie-render-queue)
* [Adding Art Assets to the Configurator](/documentation/en-us/unreal-engine/automotive-configurator-sample-in-unreal-engine?application_version=5.7#adding-art-assets-to-the-configurator)

Related documents

[Hardware Ray Tracing and Path Tracing Features

![Hardware Ray Tracing and Path Tracing Features](https://dev.epicgames.com/community/api/documentation/image/16584512-21dd-4348-82ee-2c6d599038c1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine)

[Volumetric Cloud Component

![Volumetric Cloud Component](https://dev.epicgames.com/community/api/documentation/image/d5d27248-8407-4e94-9ea9-9982ba198b84?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine)
