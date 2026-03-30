<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7 -->

# Environment Light Mixer

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Environmental Light with Fog, Clouds, Sky and Atmosphere](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine "Environmental Light with Fog, Clouds, Sky and Atmosphere")
8. Environment Light Mixer

# Environment Light Mixer

An editor window that combines common atmospheric lighting components in one place where they can be created and edited for a Level.

![Environment Light Mixer](https://dev.epicgames.com/community/api/documentation/image/47706023-ee6b-4206-ac96-ca1cf6db4cd9?resizing_type=fill&width=1920&height=335)

 On this page

The **Environment Light Mixer** is an editor window where you can create and edit a Level's environment lighting components for sky, clouds, atmosphere lights, and sky lighting. For designers and artists, it's a single window that enables you to edit these components quickly and choose the amount of properties detail you want access to.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c64caa0-f8b5-426f-95a7-45eed18212ce/01-env-light-mixer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c64caa0-f8b5-426f-95a7-45eed18212ce/01-env-light-mixer.png)

Click image for full size.

## Opening the Environment Light Mixer

Open the Environment Light Mixer from the **Main Menu** by selecting **Window > Env. Light Mixer**.

![From the Main Menu, select Window, then select Env. Light Mixer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0ed64465-7304-4295-93b8-a34ad0592f1d/02-open-env-light-mixer.png)

## Environment Light Mixer Interface

The Environment Light Mixer's interface is comprised of two primary elements:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99e420f8-2b48-423f-b4fe-1e9d1df98216/03-elm-interface.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99e420f8-2b48-423f-b4fe-1e9d1df98216/03-elm-interface.png)

Click image for full size.

1. [Toolbar](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine#toolbar)
2. [Components Panels](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine#componentspanels)

### Toolbar

The **Toolbar** is where you'll add and configure the level of properties detail that is visible in the Components Panels.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/973a5330-aff5-4ff0-8f90-d5e0bf3fb034/04-elm-toolbar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/973a5330-aff5-4ff0-8f90-d5e0bf3fb034/04-elm-toolbar.png)

Click image for full size.

#### Adding Scene Components

When you open the Environment Light Mixer window, if you are starting from an empty Level, you will find the following components listed:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98780f70-ca16-465a-8a81-f4d9445ad3a8/05-elm-toolbar-adding-components.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98780f70-ca16-465a-8a81-f4d9445ad3a8/05-elm-toolbar-adding-components.png)

Click image for full size.

1. [Sky Light](/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine)
2. [Atmosphere Lights (2x Directional Lights for sun and moon, or two suns representation)](/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine)
3. [Sky Atmosphere](/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine)
4. [Volumetric Cloud](/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine)

If any of these components is added from the Place Actors panel or already exists in the scene, the list will automatically reflect what is not currently added. Likewise, when you remove a component from the scene, the create button becomes available again in the toolbar.

### Controlling the Amount of Properties Detail

When one of the available components is referenced in your Level – whether you added it through the Environment Light Mixer, or it already exists – the component's properties are added to the Components Panel where you can adjust and edit various properties for each of them.

For those that want maximum control over editing of their components, you can change the amount of properties shown using the **Property Details** dropdown:

![Using the Property Details Dropdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ae31959-7a2e-43b8-a870-4755c4d88e1c/06-elm-toolbar-properties-detail.png)

1. **Minimal** provides the bare essentials for components.
2. **Normal** provides the common properties for components.
3. **Normal+Advanced** provides common and advanced properties for components.

Below are examples of the amount of properties shown for the Directional Light using each detail amount:

|  |  |  |
| --- | --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c48b0e72-00a9-4945-975f-9cba54e28669/07-elm-toolbar-minimal.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d4331a54-d8f1-4a80-90ef-9e8ed8bc4f1d/08-elm-toolbar-normal.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3d66ae3-ab0b-4af2-b732-14ba46484a22/09-elm-toolbar-advanced.png) |
| Minimal | Normal | Normal+Advanced |

Click images for full size

### Components Panels

The **Components Panels** lists any of the components available in the Toolbar to add to your scene. It includes components for Sky Atmosphere, Volumetric Clouds, up to two Directional Lights, and a Sky Light.

By Default, the properties displayed for each component is limited to its **Minimal** set but can be extended to show more using the [Property Details](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine#controllingtheamountofpropertiesdetail) dropdown in the toolbar.

![The Components Panels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/614a547f-6c5f-43c7-ac97-89dd2165451c/10-elm-components-panel.png)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [environment lighting](https://dev.epicgames.com/community/search?query=environment%20lighting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Opening the Environment Light Mixer](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7#openingtheenvironmentlightmixer)
* [Environment Light Mixer Interface](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7#environmentlightmixerinterface)
* [Toolbar](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7#toolbar)
* [Adding Scene Components](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7#addingscenecomponents)
* [Controlling the Amount of Properties Detail](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7#controllingtheamountofpropertiesdetail)
* [Components Panels](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine?application_version=5.7#componentspanels)
