<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine?application_version=5.7 -->

# Motion Controller Component Setup

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Making Interactive XR Experiences](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine "Making Interactive XR Experiences")
8. Motion Controller Component Setup

# Motion Controller Component Setup

Information on how to setup Motion Controllers for VR interaction.

![Motion Controller Component Setup](https://dev.epicgames.com/community/api/documentation/image/c7d567d6-9380-4641-84b5-1137ab1b1888?resizing_type=fill&width=1920&height=335)

 On this page

No matter which Virtual Reality platform you are developing for, adding support for Motion Controllers can add a level of immersion and interaction that is just not possible to achieve with a controller or mouse and keyboard. In the following How - To we will take a look at how to add Motion Controller support to the VR Platforms that support it.

## Supported Platforms

The Motion Controller component that is found in the Components tab will work on the following VR platforms.

* Oculus VR
* Steam VR
* Gear VR
* Playstation VR
* Google VR

If you do not see the platform you are developing for listed above, make sure to check that platform's documentation for how to go about setting use of Motion Controllers.

## Motion Controller Setup

In the following section we will take a look at how to add and setup the components that are needed for Motion Controllers to work.

This How - To has been written assuming that you have setup your Pawn to work with the VR Head Mounted Display (HMD) that you are developing for. If you are not sure how to do this, check please check out the getting [started guide](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine) for the VR Head Mounted Display (HMD) you are developing for.

1. First, inside the **Content Drawer** locate and open up your **Player Pawn** Blueprint.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff575b67-bf4e-498d-94f6-30b353ba9ac0/01-select-vr-pawn_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff575b67-bf4e-498d-94f6-30b353ba9ac0/01-select-vr-pawn_ue5.png)

   Click for full image.
2. In the **Components** section click on the **Add Component** button to expose the components that can be added to this Blueprint.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26e277c3-35ac-4406-a318-fbe20000b86c/02-add-button_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26e277c3-35ac-4406-a318-fbe20000b86c/02-add-button_ue5.png)

   Click for full image.
3. Input **Motion** in the search box and then click on the **Motion Controller** component to add it to the components list, giving it a name of **MC\_Left**..

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3db95fa5-8eb3-475b-b2da-bb4e066c6d27/03-motion-controller_ue5.png)
4. Select the newly added Motion Controller component and over in the **Details** panel under the **Motion Controller** section make sure the **Motion Source** is set to **Left**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35f7aa99-89b1-4117-8a00-65a0c1eec8bc/04-motion-source-left_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35f7aa99-89b1-4117-8a00-65a0c1eec8bc/04-motion-source-left_ue5.png)

   Click for full image.
5. Next, select the **Motion Controller Component** in the **Components panel** and click the **Add Component** button and then search for and add a **Static Mesh Component**, calling it **SM\_Left**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/126572b1-2b0f-4f78-ba5b-2f2a2b4a3f5d/05-sm-left_ue5.png)


   Make sure that the Static Mesh Component is a child of the Motion Controller Component otherwise the Static Mesh will not follow along when the Motion Controller is moved.
6. Now, in the Details panel of the Static Mesh Component under the **Static Mesh** section input a Static Mesh to represent what the Motion Controllers will look like. For this example we are using a simple box, but feel free to use any Static Mesh you have available.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb49530c-9e15-4b21-bbe9-cda2fd6f8e0f/06-static-mesh-cube_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb49530c-9e15-4b21-bbe9-cda2fd6f8e0f/06-static-mesh-cube_ue5.png)

   Click for full image.
7. Now, duplicate the entire Left hand Motion Controller setup and re-place the word **Left** with **Right**. Also make sure to change the which hand this Motion Controller is used for by going to the Motion Controller component and then changing **Motion Source** from Left to **Right**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05e31a17-ec32-4f4d-8847-911d8bca7c7e/07-mc-right_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05e31a17-ec32-4f4d-8847-911d8bca7c7e/07-mc-right_ue5.png)

   Click for full image.
8. Compile and save your Pawn Blueprint, make sure it is placed in your test level and then launch your project. When you put on your HMD and pick up your Motion Controlers you should be able to now do what is shown in the following video.

## Motion Controller Component Visualization

Motion Controllers have a **Visualization** category that enables you to quickly and more easily add a display model Static Mesh to your Motion Controllers. By default, the system attempts to load a Static Mesh model matching the device driving the Motion Controller.  The visualization fields  offer the following options:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10b5a0f7-7a3b-4602-82d2-387934e590f2/08-visualization-settings_ue5.png "08-visualization-settings_ue5.png")

| Property Name | Description |
| --- | --- |
| **Display Device Model** | Used to automatically render a model associated with the set hand. |
| **Display Model Source** | Determines the source of the desired model. Ny default, the active XR system(s) will be queried and (if available) will provide a model for the associated device. Note: This may fail if there's no default model; use 'Custom' to specify your own mode. |
| **Custom Display Mesh** | A mesh override that'll be displayed attached to this Motion Controller. |
| **Display Mesh Material Overrides** | Material overrides for the specified Display mesh. |

## Training Streams

* [vr](https://dev.epicgames.com/community/search?query=vr)
* [motion controller](https://dev.epicgames.com/community/search?query=motion%20controller)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Supported Platforms](/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine?application_version=5.7#supportedplatforms)
* [Motion Controller Setup](/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine?application_version=5.7#motioncontrollersetup)
* [Motion Controller Component Visualization](/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine?application_version=5.7#motioncontrollercomponentvisualization)
* [Training Streams](/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine?application_version=5.7#trainingstreams)
