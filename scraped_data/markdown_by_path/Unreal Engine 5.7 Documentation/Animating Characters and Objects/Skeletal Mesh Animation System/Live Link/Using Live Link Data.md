<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7 -->

# Using Live Link Data

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
8. Using Live Link Data

# Using Live Link Data

Provides an overview of the features available for using Live Link to stream data to Actors.

![Using Live Link Data](https://dev.epicgames.com/community/api/documentation/image/9ebd71ba-5cd6-476b-84f5-57f52e79d308?resizing_type=fill&width=1920&height=335)

 On this page

**Live Link** provides users with the ability to stream various types of data from a variety of sources and apply that data directly to Actors within their level. To improve these workflows, **Unreal Engine** uses several features designed to streamline the process of applying Live Link data to the Actors in your level.

* **Live Link Presets** save your source settings for later use.
* The **LiveLink Controller Component** enables using LiveLink controllers. These simplify applying Live Link information to your Actors and several Blueprint nodes have been added to facilitate gathering this data.
* The **LiveLink Skeletal Animation Component** exposes the **OnLiveLinkUpdated** event node which retrieves information on Subjects and Sources every time Live Link updates, and can perform a number of other functions through Blueprint.

For more information on enabling Live Link and setting up your connections, please see the [Live Link Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine) documentation.

Prior to Unreal Engine version 4.23, the **LiveLink Skeletal Animation Component** was called the **Live Link Component**.

## Live Link Presets

Unreal Engine obtains Live Link data from a variety of sources created in the [Live Link Connection](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine) window. Once created, these sources can be saved as **Presets** and accessed via Blueprints using the **Apply to Client** node.

[![Live Link apply to client node](https://dev.epicgames.com/community/api/documentation/image/645ab61f-d308-4efb-9043-77ab21e28015?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/645ab61f-d308-4efb-9043-77ab21e28015?resizing_type=fit)

Using this node, a Live Link preset can load when your application launches.

Live Link presets can also be activated via the Presets button in the Live Link panel or in the Project Settings by setting the **Default Live Link Preset** in the **Plugins - Live Link** section of the menu. A preset may also be applied via command line using 'LiveLink.Preset.Apply Preset=/Game/Folder/MyLiveLinkPreset.MyLiveLinkPreset'.

## Live Link Components

### Live Link Skeletal Animation Component

When you add a Live Link Skeletal Animation Component to an Actor Blueprint from the **Components** panel, it doesn't get parented to other Components. It sits inside your Blueprint and gives you access to the **On Live Link Updated Event**.

[![Live Link component details panel](https://dev.epicgames.com/community/api/documentation/image/d8d637b5-fb27-49c2-a384-045ea87cd84e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d8d637b5-fb27-49c2-a384-045ea87cd84e?resizing_type=fit)

The On Live Link Updated event is triggered any time the Component is updated, including inside the Editor.

[![On Live Link Updated node](https://dev.epicgames.com/community/api/documentation/image/3aa4fc55-dedf-459d-a20d-afb03dbd4345?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3aa4fc55-dedf-459d-a20d-afb03dbd4345?resizing_type=fit)

The On Live Link Updated node effectively takes the place of your **Tick Event**, but it runs inside the Editor as well. For example, if you want to drive some data live inside the Editor, this node will support that.

### Live Link Controller Component

The Live Link Controller Component is a component that sits inside of your character Blueprint and provides the ability to use Live Link Controllers. These controllers automatically fetch data from your Live Link subject and apply it to a corresponding component in your Actor via a Live Link Controller.

[![Live Link component controller](https://dev.epicgames.com/community/api/documentation/image/f4132bae-9edf-4839-b8db-ed5c2e0237b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f4132bae-9edf-4839-b8db-ed5c2e0237b3?resizing_type=fit)

## Using a Live Link Controller

Live Link controllers provide a quick method of taking Live Link data and pushing it to an Actor in your scene. Each controller consumes data from a Live Link subject and applies it automatically to the actor of your choice. Controllers come in three different varieties defined by the role:

* Transform
* Camera
* Light

See below for details on the different Live Link controllers.

### Transform

The Transform controller quickly captures and applies transform data from a Live Link subject to an Actor in your level.

[![Live Link transform controller](https://dev.epicgames.com/community/api/documentation/image/a8fb77ce-e1de-4b19-bf01-c85549a954c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8fb77ce-e1de-4b19-bf01-c85549a954c5?resizing_type=fit)

This controller provides the following options:

| Setting | Description |
| --- | --- |
| **World Transform** | Sets the transform of the component to world space. Uncheck for local space. |
| **Use Scale** | Uses scale data from Live Link. |
| **Sweep** | Sweeps the root component and checks for blocking collision, triggering overlaps along the way and stopping short of the target if blocked. |
| **Teleport** | Teleports the physics state (if physics collision is enabled).   * If checked, physics velocity remains unchanged. * If unchecked, physics velocity is updated based on the change in position. |

### Camera

The Camera controller applies camera settings and movement data directly from a Live Link subject with the camera role to a Camera Actor in your level.

[![Live Link camera controller](https://dev.epicgames.com/community/api/documentation/image/75297823-f45c-457c-945a-5b9013f7fd75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75297823-f45c-457c-945a-5b9013f7fd75?resizing_type=fit)

Camera settings that can be animated include:

* Field of View (in degrees)
* Aspect Ratio (width / height)
* Focal Length
* Aperture of the camera in terms of f-stop
* Focus distance of the camera in cm (works only with manual focus)
* Projection mode of the camera (perspective, orthographic, etc)

### Light

The Light controller applies Light settings directly from a Live Link subject with the Light role to a Light Actor in your level.

[![Live Link light controller](https://dev.epicgames.com/community/api/documentation/image/445c0f07-7cad-4829-a212-72b4439dd931?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/445c0f07-7cad-4829-a212-72b4439dd931?resizing_type=fit)

Light settings that can be animated include:

* Color temperature (in kelvin).
* Total energy (in lux).
* Filter color.
* Inner cone angle (in degrees for a spotlight).
* Outer cone angle (in degrees for a spotlight).
* Light visible influence (for pointlight and spotlight).
* Soft radius for light source shape (for pointlight and spotlight).
* Length of light source shape (for pointlight and spotlight).

Additional controllers may be added or created using external plugins. For more information on external Plugins, please see our [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine) documentation.

### Applying a Controller to an Actor

Applying a Live Link Controller begins with adding the Live Link Controller component to your Actor:

[![Applying a Live Link controller to a cube static mesh actor](https://dev.epicgames.com/community/api/documentation/image/1ef2c47c-cc58-44cc-a560-9a84003f2dd4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ef2c47c-cc58-44cc-a560-9a84003f2dd4?resizing_type=fit)

This section requires that you have connected to a Live Link source. For more information on connecting to your source, please see our [Live Link Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine) documentation.

Use the following steps to add the component through the **Details** panel:

1. Select the **Actor** in your level.
2. In the **Details** panel click the **+ Add Component** button and search for the **Live Link Controller** component.
3. Once added, select the component from the component list and open the **Subject Representation** drop down menu. Select the subject from the list that you want to use as the source of data for this Actor. Unreal will select the **Component to Control** for you based on your selection. This can be adjusted if needed.

With the controller set up, your Actor will begin receiving data from the selected Live Link subject automatically.

## Common Blueprint Nodes

Live Link data can be accessed via a variety of Blueprint nodes.

### Get Live Link Subjects

There are times when you will need to get a list of Subjects to use with the **Evaluate Live Link Frame** node. When this happens, you can use **Get Live Link Subjects**:

[![get live link subjects Blueprint node](https://dev.epicgames.com/community/api/documentation/image/6d530389-0636-4dc3-91c5-020f2bbd81ef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d530389-0636-4dc3-91c5-020f2bbd81ef?resizing_type=fit)

This returns an array of Subjects that the Evaluate Live Link Frame function will find valid.

### Evaluate Live Link Frame

Calling the Evaluate Live Link Frame function enables you to get the Live Link data associated with the provided Subject Name. This function gives you execute pins for whether the current frame is valid or not, as well as static and frame data that can be accessed from the **Data Result** output. This data is determined by the type of Role chosen to evaluate the subject.

The example below shows data being accessed directly from the data structure pin.

[![evaluate live link frame Blueprint node with connected output](https://dev.epicgames.com/community/api/documentation/image/b8156fda-142c-4d18-9041-d220919064c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8156fda-142c-4d18-9041-d220919064c0?resizing_type=fit)

### Using Data from Evaluate Live Link Frame

Evaluate Live Link Frame opens the way to using several Blueprint functions to evaluate the data that it provides. The resulting data depends on the Role being evaluated. When the Animation Role is evaluated, you see the following:

* Get Basic Data
* Get Curves
* Get Metadata
* Get Root Transform
* Get Transform by Index
* Get Transform by Name
* Number of Transforms
* Transform Names

### Get Basic Data

The **Get Basic Data** node returns the base structure of the Subject that is stored in the current Subject frame.

[![get basic data Blueprint node](https://dev.epicgames.com/community/api/documentation/image/36090a0e-4878-441e-a376-6f123d7b3d07?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36090a0e-4878-441e-a376-6f123d7b3d07?resizing_type=fit)

### Get Curves

The **Get Curves** function enables you to get all the Blend Shapes or Animated Curves and returns a Map of the Name to Value for each entry.

[![get curves node](https://dev.epicgames.com/community/api/documentation/image/af01b6bf-e08b-4a07-84d9-37055a1ffc23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af01b6bf-e08b-4a07-84d9-37055a1ffc23?resizing_type=fit)

You could use a **Find** and enter a Name to retrieve the value of a curve (or use the boolean to determine if it was found or not).

[![find map node](https://dev.epicgames.com/community/api/documentation/image/895eba09-69d5-4b9d-846c-aae1b58bc8e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/895eba09-69d5-4b9d-846c-aae1b58bc8e7?resizing_type=fit)

### Get Metadata

The **Get Metadata** function returns the Subject Metadata structure stored in the Subject Frame which you can break apart to retrieve information:

[![get metadata node](https://dev.epicgames.com/community/api/documentation/image/abc31aec-e2a6-4ef6-8abf-5cad3e74221b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abc31aec-e2a6-4ef6-8abf-5cad3e74221b?resizing_type=fit)

String Metadata is a Map to named strings on the subject, for example you may want to pass through the type of an object being streamed as a named string. Also included with the metadata is the **Scene Timecode** and **Scene Framerate**, whose structures you can break to obtain the information you need.

| Output | Description |
| --- | --- |
| **String Metadata** | A map of named strings used to provide additional information about a frame or subject, for example "Type": "Camera". |
| **Scene Timecode** | Timecode value associated with the current frame.  This is not guaranteed to be unique, for example editing a single frame in MotionBuilder will result in that frame's timecode being sent for multiple frames. |
| **Scene Framerate** | Corresponding Framerate to the Scene Timecode. |

### Get Root Transform

The **Get Root Transform** function will return the Root Transform for the Subject Frame as a Live Link Transform (or the identity if there are no transforms).

[![get root transform node](https://dev.epicgames.com/community/api/documentation/image/38381b17-1581-4f69-9974-76fd55c82fd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38381b17-1581-4f69-9974-76fd55c82fd1?resizing_type=fit)

This returns a Live Link Transform instead of a standard Transform as you can call additional functions on it (outlined below):

| Function | Description |
| --- | --- |
| **Child Count** | Returns the number of Children for a given Live Link Transform. |
| **Component Space Transform** | Returns the Transform value in Root Space for a given Live Link Transform (relative to the root of your model). |
| **Get Children** | Returns an array of Child Live Link Transforms for a given Live Link Transform. |
| **Get Parent** | Returns the Parent Live Link Transform if one exists or an Identity Transform if no Parent exists. |
| **Has Parent** | Returns whether a given Live Link Transform has a Parent Transform. |
| **Parent Bone Space Transform** | Returns the Transform value in Parent Space for a given Live Link Transform (how it's stored internally and relative to whatever the Parent bone is). |
| **Transform Name** | Returns the Name of a given Live Link Transform. |

### Get Transform By Index

The **Get Transform By Index** function returns the Live Link Transform stored in a Subject Frame at a specified index (the function returns an Identity Transform if the Transform Index is invalid).

[![](https://dev.epicgames.com/community/api/documentation/image/c917d728-e0f4-4fb4-8c6e-14c5df1b2506?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c917d728-e0f4-4fb4-8c6e-14c5df1b2506?resizing_type=fit)

### Get Transform by Name

The **Get Transform by Name** function is similar to **Get Transform by Index** but takes in Transform Name data.

[![](https://dev.epicgames.com/community/api/documentation/image/69cd7265-7e64-4c26-99da-b816233fb08c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69cd7265-7e64-4c26-99da-b816233fb08c?resizing_type=fit)

### Number of Transforms

The **Number of Transforms** function returns the number of Transforms within the Subject Frame.

[![number of transforms node](https://dev.epicgames.com/community/api/documentation/image/4727e834-7ff7-47ac-bade-394d85726ebf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4727e834-7ff7-47ac-bade-394d85726ebf?resizing_type=fit)

One use case for this would be to use it in conjunction with the **Get Transform By Index** to loop through and retrieve each of your Live Link Transforms (similar to the example below):

[![loopong through transforms Blueprint section](https://dev.epicgames.com/community/api/documentation/image/8dfc35d9-187c-4d80-a7d6-7b28baea2140?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8dfc35d9-187c-4d80-a7d6-7b28baea2140?resizing_type=fit)

Click image for full view.

### Get Transform Names

The **Get Transform Names** function returns an array of names for all the transforms in a frame.

[![get transform names node](https://dev.epicgames.com/community/api/documentation/image/adfd289e-9a6f-4e5d-be4b-30127f83598b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/adfd289e-9a6f-4e5d-be4b-30127f83598b?resizing_type=fit)

## Applying a Live Link Preset with Blueprints

A common use of Blueprints with Live Link is to use the **Apply to Client** node to assign a Live Link preset to a Skeletal Mesh at runtime:

[![Apply to client node](https://dev.epicgames.com/community/api/documentation/image/ee1a543d-65ce-4f0d-8852-a17fbf82056a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee1a543d-65ce-4f0d-8852-a17fbf82056a?resizing_type=fit)

1. Start by creating your Live Link preset in the Live Link Panel. For more information on presets, please see our [Live Link Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine) documentation.
2. In your character blueprint, create a reference to your preset by making a new variable and setting the **Variable Type** to **Live Link Preset** in the **Details** panel.
3. Compile your Blueprint and set the default value of your new variable to your saved Live Link Preset.
4. Drag your variable into your Blueprint and choose **Get** from the menu.
5. Drag off from the variable and search for the **Apply to Client** node.
6. Connect the **Event Begin Play** node to **Apply to Client**.

* [live link](https://dev.epicgames.com/community/search?query=live%20link)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Live Link Presets](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#live-link-presets)
* [Live Link Components](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#live-link-components)
* [Live Link Skeletal Animation Component](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#live-link-skeletal-animation-component)
* [Live Link Controller Component](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#live-link-controller-component)
* [Using a Live Link Controller](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#using-a-live-link-controller)
* [Transform](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#transform)
* [Camera](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#camera)
* [Light](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#light)
* [Applying a Controller to an Actor](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#applying-a-controller-to-an-actor)
* [Common Blueprint Nodes](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#common-blueprint-nodes)
* [Get Live Link Subjects](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-live-link-subjects)
* [Evaluate Live Link Frame](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#evaluate-live-link-frame)
* [Using Data from Evaluate Live Link Frame](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#using-data-from-evaluate-live-link-frame)
* [Get Basic Data](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-basic-data)
* [Get Curves](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-curves)
* [Get Metadata](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-metadata)
* [Get Root Transform](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-root-transform)
* [Get Transform By Index](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-transform-by-index)
* [Get Transform by Name](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-transform-by-name)
* [Number of Transforms](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#number-of-transforms)
* [Get Transform Names](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#get-transform-names)
* [Applying a Live Link Preset with Blueprints](/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine?application_version=5.7#applying-a-live-link-preset-with-blueprints)
