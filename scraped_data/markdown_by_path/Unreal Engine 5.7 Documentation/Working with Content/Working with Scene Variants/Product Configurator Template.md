<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7 -->

# Product Configurator Template

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Working with Scene Variants](/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine "Working with Scene Variants")
7. Product Configurator Template

# Product Configurator Template

How to customize and use the Product Configurator template

![Product Configurator Template](https://dev.epicgames.com/community/api/documentation/image/77156f68-bde6-481b-836d-0eb2376bc67d?resizing_type=fill&width=1920&height=335)

 On this page

![The guitar sample from the Product Configurator](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/318051a6-1241-4cba-b9b4-bf2142bbba7a/01-the-guitar-sample-from-the-product-configurator.png "Guitar sample from the Product Configurator")

The **Product Configurator** template in **Unreal Engine 5 (UE5)** presents 3D visualization artists with a starting point for the creation of a customizable product configurator and user interface. The template utilizes Level Variant Sets, custom UMG interface elements, and a purpose-built configuration Blueprint with the following features:

* Geometry variation using Actor switching.
* Material and Visibility options.
* Camera position and setting variation.
* Lighting and environment variation.
* Procedurally generated interface that presents users with options.
* Ability to add new variations without using Blueprint code.

## Overview

Using the **Variant Manager**, you can define **Actor Variants** and **Variant Sets** within a **LevelVariantSet** Actor. The information is then passed to the **BP\_Configurator** Blueprint; which uses the information to dynamically create the user interface and display all of the variant options, complete with user-defined thumbnail images:

[![Example configurator showing the upholstery options for a car seat](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6994c6d9-6618-4b4a-8a96-4fbadc970db6/02-configurator-with-the-upholstery-options-for-a-car-seat.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6994c6d9-6618-4b4a-8a96-4fbadc970db6/02-configurator-with-the-upholstery-options-for-a-car-seat.png)

Click image for full size.

### Controling the Template

| **Control** | **Description** |
| --- | --- |
| **Alt + LMB** | Rotate camera around the product. |
| **Alt + RMB** | Zoom in/out |
| **G** | Hide/Show Interface |
| **Escape** | Exit the Configurator |

## Template Features

The template uses the Variant Manager, a specialized UI panel that organizes different configurations of properties for Actors in your level and stores them in a LevelVariantSet Actor.

[![Variant Manager](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bd9ea00-d41a-4cbb-9722-ef3c5de18247/03-variant-manager.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bd9ea00-d41a-4cbb-9722-ef3c5de18247/03-variant-manager.png)

Click image for full size.

| **Number** | **Description** |
| --- | --- |
| **1** | Variants |
| **2** | Actors |
| **3** | Properties |
| **4** | Enable auto-capture properties |

The Variants column contains all of your Actor configurations, known as variants, organized into Variant Sets. Each Variant represents an option in the configurator and can contain one or more Actors with a variety of property changes. These are represented by a thumbnail image set by the user. All Variants are translated into buttons in the interface at runtime via the BP\_Configurator.

For information on using the Variant Manger, please see the [Variant Manager](/documentation/en-us/unreal-engine/variant-manager-template-overview) documentation.

### Using the BP\_Configurator

The BP\_Configurator Blueprint takes in data from a specified Level Variant Set and dynamically creates the user interface for your configurator:

1. The BP\_Configurator takes in data from the specified Level Variant Set.
2. Each Variant Set is translated into an icon on the main UI toolbar.
3. Each Variant becomes an option in that Variant Set's sub menu.
4. The Variant is visually represented by the thumbnail set in the Variant Manager.
5. Variant Sets are represented by the icon of the currently active Variant.

## How to Import Your Data

Customizing the Product Configurator template begins with importing your 3d artwork and textures. Unreal Engine 5 supports the use of [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-overview), as well as the [FBX Content Pipeline](/documentation/en-us/unreal-engine/fbx-content-pipeline) for importing from your favorite 3D applications such as Maya, 3ds Max, and Blender.

Once your 3D and 2D assets have been imported into the Content Browser, you will need to remove the sample guitar from the level and build your Variant and Variant Sets using the Variant Manager. The final step will be to connect your level variant set to the BP\_Configurator to create the custom user interface at runtime.

### Adding Your Artwork into the Main Level

When your assets have been imported into UE5 and setup in the Content Browser, the example guitar will need to be removed and the new art added to the level:

[![Project Start](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1af77a1f-9c0a-488f-be46-1aa9c94f74b0/04-project-start.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1af77a1f-9c0a-488f-be46-1aa9c94f74b0/04-project-start.png)

Click image for full size.

[![Guitar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0503db5e-acc9-4740-a70d-6ea627220c6f/05-guitar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0503db5e-acc9-4740-a70d-6ea627220c6f/05-guitar.png)

Click image for full size.

The Product Configurator uses one or more root Actors to provide standard placement for your static meshes:

[![Guitar Root](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4011f60-eb6a-463b-9f86-69453d942e60/06-guitar-root.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4011f60-eb6a-463b-9f86-69453d942e60/06-guitar-root.png)

Click image for full size.

To remove the example model, delete the GuitarRoot object and all of its child objects.

Next, place a new Empty Actor into the level to serve as your new root object. Center its location at the level origin (X=0, Y=0, Z=0):

[![Create Blueprint Class](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06f2f9de-0bde-4c90-9ef9-992c4a789453/07-create-blueprint-class.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06f2f9de-0bde-4c90-9ef9-992c4a789453/07-create-blueprint-class.png)

Click image for full size.

[![Actor Class](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fe7f35a-5572-40fe-b85a-8d0c9113cc90/08-actor-class.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fe7f35a-5572-40fe-b85a-8d0c9113cc90/08-actor-class.png)

Click image for full size.

[![Empty Scene Object](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95dee943-295d-4c1e-a332-b9591e53b2df/09-empty-scene-object.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95dee943-295d-4c1e-a332-b9591e53b2df/09-empty-scene-object.png)

Click image for full size.

This will place your product in front of the existing camera setup.

Now, place the pieces of your product in the level as children of the root object:

[![Car Seat Blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37b3b628-61d6-41cb-baaa-deb9132e04f7/10-car-seat-blueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37b3b628-61d6-41cb-baaa-deb9132e04f7/10-car-seat-blueprint.png)

Click image for full size.

### Creating Your Variants in the Variant Manager

With the artwork set up in the level, you can begin to create Variants and Variant Sets using a LevelVariantSet Actor and the Variant Manager.

For the dynamic UI created by the BP\_Configurator to work, the first and second Variant Sets **must** be the Environment and the Camera.

Create a LevelVariantSet Actor by right clicking in the content browser, navigating to the Miscellaneous sub menu and choosing the Level Variant Sets option:

[![Level Variant Set](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae34a58b-698c-45f5-807d-0cfce0793fbe/11-level-variant-set.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae34a58b-698c-45f5-807d-0cfce0793fbe/11-level-variant-set.png)

Click image for full size.

[![Level Variant Set](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1677809e-c6a0-4b8a-ac57-8f2f25d33fbe/12-level-variant-set-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1677809e-c6a0-4b8a-ac57-8f2f25d33fbe/12-level-variant-set-1.png)

Click image for full size.

[![Drag the Level Variant Set to the Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13ae3063-fb42-4e17-9482-f4ac9c8d06e3/13-drag-the-level-variant-set-to-the-viewport.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13ae3063-fb42-4e17-9482-f4ac9c8d06e3/13-drag-the-level-variant-set-to-the-viewport.png)

Click image for full size.

Give it a unique name and double click to open the Variant Manager.

Start by creating a custom Variant Set. Click the **+ Variant Set** button and name the new set:

[![Variant Set](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11bb98cd-67f0-470d-b2dd-1a2b12843018/14-variant-set.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11bb98cd-67f0-470d-b2dd-1a2b12843018/14-variant-set.png)

Click image for full size.

Once the Variant Set is created, click the **Add (+)** button next to its name to create a Variant. This represents the Actors and properties that you want to change when the user selects this preset:

[![Adding Variant](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/151117f1-fb4a-494f-ae3a-412b16c1c74e/15-adding-variant.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/151117f1-fb4a-494f-ae3a-412b16c1c74e/15-adding-variant.png)

Click image for full size.

Click on the new Variant to highlight it and then click the + button in the Actors column. This will open a new window listing all of the Actors in your scene. Select the Actor that you want to change when the user selects this Variant. Repeat the process for each Actor that will be part of this preset:

[![Adding Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98894bd2-7197-46d8-b83c-7dc2e0b0c4c1/16-adding-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98894bd2-7197-46d8-b83c-7dc2e0b0c4c1/16-adding-actors.png)

Click image for full size.

Next, highlight the Actor that you would like to work with and click the **Add (+)** button in the Properties column. This will create a new window listing all the properties of the Actor that can be changed as part of the variant. Select the checkbox for each property that will be changed when the variant is selected:

[![Adding Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47ed56e3-00e3-4330-a2ce-191a231977d8/17-adding-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47ed56e3-00e3-4330-a2ce-191a231977d8/17-adding-properties.png)

Click image for full size.

This list includes both the default and any user defined properties. In the example above, the Env Map property has been selected. Changing this property will allow you to change the environment in the product configurator during runtime.

The last step is to set the value of the property. This can be completed one of two ways. The first is to manually set the value using the Values column:

[![Setting Property](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37a4dd44-045e-4faa-89fe-64dbcae6d1dd/18-setting-property.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37a4dd44-045e-4faa-89fe-64dbcae6d1dd/18-setting-property.png)

Click image for full size.

You can also set the property using the value set in the level by right-clicking the property and selecting **Record current value** from the context menu to record the current value for your Variant.

As an alternative, pressing the **Auto Capture** button enables the auto-capture of properties. When activated, this option tells the Variant Manager to listen for changes made to Actors in the level and record them in the selected Variant. If the Actor being modified is not bound to the selected variant, it does so automatically.

Each Variant in a Variant Set also needs a thumbnail. These thumbnails are used as the button icon in the user interface and can be a texture image that is imported into the engine or captured from the viewport. Right click on a variant to open the menu:

[![Thumbnail Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90d81389-7f30-4dbf-a952-cb0d702710cf/21-thumbnail-viewport.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90d81389-7f30-4dbf-a952-cb0d702710cf/21-thumbnail-viewport.png)

Click image for full size.

Repeat this process for all Variants and Variant Sets.

## Connecting to the BP\_Configurator

To complete the process of customizing the template, your Level Variant Set needs to be connected to the BP\_Configurator. Start by deleting the existing LevelVariantSet Actor from the level and replacing it with your own. The Actor must be in the level to be seen by the BP\_Configurator:

[![Setting Up Config](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6320f5aa-6d1e-4a6f-82be-2c18fa5bb8fb/23-setting-up-config.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6320f5aa-6d1e-4a6f-82be-2c18fa5bb8fb/23-setting-up-config.png)

Click image for full size.

In the Details panel, find the LVSActor option in the Default section of the menu and change the setting to your Level Variant Set using the drop down menu.

Finally, test you configurator:

[![Car Seat Blueprint on the Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/378786d4-fcd1-43f2-a5fa-0d1df29a4eed/24-car-seat-blueprint-on-the-viewport.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/378786d4-fcd1-43f2-a5fa-0d1df29a4eed/24-car-seat-blueprint-on-the-viewport.png)

Click image for full size.

[![Press Play button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/504e2b17-4e7b-49bf-a0b8-8dbd999cb092/25-press-play-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/504e2b17-4e7b-49bf-a0b8-8dbd999cb092/25-press-play-button.png)

Click image for full size.

[![Final](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7209746e-0092-4233-b631-55c8d487126d/26-final.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7209746e-0092-4233-b631-55c8d487126d/26-final.png)

Click image for full size.

* [templates](https://dev.epicgames.com/community/search?query=templates)
* [variantmanager](https://dev.epicgames.com/community/search?query=variantmanager)
* [productconfigurator](https://dev.epicgames.com/community/search?query=productconfigurator)
* [variant manager](https://dev.epicgames.com/community/search?query=variant%20manager)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#overview)
* [Controling the Template](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#controlingthetemplate)
* [Template Features](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#templatefeatures)
* [Using the BP\_Configurator](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#usingthebp-configurator)
* [How to Import Your Data](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#howtoimportyourdata)
* [Adding Your Artwork into the Main Level](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#addingyourartworkintothemainlevel)
* [Creating Your Variants in the Variant Manager](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#creatingyourvariantsinthevariantmanager)
* [Connecting to the BP\_Configurator](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine?application_version=5.7#connectingtothebp-configurator)
