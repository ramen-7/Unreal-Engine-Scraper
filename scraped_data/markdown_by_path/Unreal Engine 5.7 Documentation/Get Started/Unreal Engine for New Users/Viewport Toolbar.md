<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7 -->

# Viewport Toolbar

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. Viewport Toolbar

# Viewport Toolbar

An reference for the viewport toolbar and its functionality with the Unreal Editor.

On this page

When working in the Unreal Editor, there are Level Editor Modes that each have their own workflows, functionality, and toolbar that corresponds to this. This **Viewport Toolbar** is located above the editor viewport, they include quick-select tools and menu options that affect how you interact with objects, the level in general, and what you see there. These viewport toolbar options can change depending on which mode the level editor is currently using.

## Improved Viewport Toolbar versus the Legacy Viewport Toolbar

Unreal Engine 5.6 introduces the improved viewport toolbar that has a new layout that accommodates modern workflows. This viewport toolbar replaces the previous viewport toolbar entirely for the Level Viewport and any other asset editors that also have a viewport.

[![The improved level viewport toolbar in Unreal Engine 5.6 and later compared to the legacy viewport toolbar found in earlier versions of Unreal Engine.](https://dev.epicgames.com/community/api/documentation/image/9201b235-664e-4d98-93cb-67daad6ae107?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9201b235-664e-4d98-93cb-67daad6ae107?resizing_type=fit)

The improved level viewport toolbar in Unreal Engine 5.6 and later compared to the legacy viewport toolbar found in earlier versions of Unreal Engine.

This update to the viewport toolbar provides the following benefits:

* It has consistent locations for features ordered by logical categories, such as those for transforms, snapping, and viewport modes.
* Unification of related tools and options that were previously located in high-level settings dropdowns.
* Better overflow management for smaller viewports as quick-select elements and menu condense and collapse into an overflow menu.
* Unique toolbars for Level Editor Modes and asset editors with their own specific controls.
* User-customizable menus.
* Better extensibility and customization with the `ToolsMenu` system.

## Viewport Toolbar Interface

The toolbar — whether it’s in the level editor or an asset editor — is located just above the viewport window.

[![Toolbar interface](https://dev.epicgames.com/community/api/documentation/image/7f700865-8a6e-4189-9b83-41982e5993fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7f700865-8a6e-4189-9b83-41982e5993fc?resizing_type=fit)

The improved Viewport Toolbar is located at the top of any viewport as a separate toolbar above the viewport window. Its settings and tools are grouped into the following categories:

[![Toolbar settings grouped into 5 categories.](https://dev.epicgames.com/community/api/documentation/image/6ab39431-1b3d-4ee4-8f82-46f2c9d53766?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6ab39431-1b3d-4ee4-8f82-46f2c9d53766?resizing_type=fit)

1. [Transform and Snapping Tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar#viewport-toolbar-transform-amp-snapping-tools)
2. [Camera-Related Tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar#viewport-toolbar-camera-settings)
3. [View Mode and Show Flag Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar#viewport-toolbar-view-mode-and-show-flag-options)
4. [Performance and Scalability Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar#viewport-toolbar-performance-and-scalability-tools)
5. [Viewport-Related Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar#viewport-related-settings)

## Viewport Toolbar Transform & Snapping Tools

The **Transform** and **Snapping** tools make up most of the tools you’ll use to select and manipulate objects within the editor viewport. This includes tools for selection, snapping, space orientation, and quick-select options for the most common ones.

### Transform Tools

The **Transform** **tools** are a set of quick selection tools to move, rotate, and scale objects and set what space (local or world) these should operate in. These options are how you will interact with objects in the level. This part of the toolbar also includes a dropdown menu with additional transform-related options.

[![Viewport transform tools area.](https://dev.epicgames.com/community/api/documentation/image/3259772e-4069-49a7-8a76-20a9b26b441a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3259772e-4069-49a7-8a76-20a9b26b441a?resizing_type=fit)

You can use these quick-select toolbar options to manipulate objects in the viewport:

[![Viewport quick-select transform tools.](https://dev.epicgames.com/community/api/documentation/image/9d7fd7f9-f6b0-40a2-8fd8-bb2dab9485d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d7fd7f9-f6b0-40a2-8fd8-bb2dab9485d5?resizing_type=fit)

| Icon | Name | Keyboard Shortcut | Description |
| --- | --- | --- | --- |
| [Transform tool select icon](https://dev.epicgames.com/community/api/documentation/image/bbca8976-655c-416c-a612-b6825158523d?resizing_type=fit) | **Select Objects** | **Q** | Use this option to select objects within the viewport. |
| [Select and transform icon](https://dev.epicgames.com/community/api/documentation/image/70738772-d626-4c40-9cd1-b3d118969cb1?resizing_type=fit) | **Select and Translate Objects** | **W** | Use this option to select objects and move them around the world using the translate gizmo. Use the gizmo to move objects along individual axes, dual axes, or on all three axes. |
| [Select and rotate objects tool icon](https://dev.epicgames.com/community/api/documentation/image/5580838d-a0bb-4975-93a5-676f7a30aa69?resizing_type=fit) | **Select and Rotate Objects** | **E** | Use this option to select objects and rotate them using the rotate gizmo. Use the gizmos to rotate the selected object along individual axes. |
| [Select and scale objects tool icon](https://dev.epicgames.com/community/api/documentation/image/fcaa9d3e-b0f2-4dcf-885a-abf434c85194?resizing_type=fit) | **Select and Scale Objects** | **R** | Use this option to select objects and scale them using the scale gizmo. Use the gizmo to scale objects along individual axes, dual axes, or uniformly on all three axes. |

|  |  |  |
| --- | --- | --- |
| [Transform tools video of object moving.](https://dev.epicgames.com/community/api/documentation/image/90fc8bd3-c7fd-4a95-b7d9-a9f78c46e677?resizing_type=fit) | [Transform tools video of object rotating..](https://dev.epicgames.com/community/api/documentation/image/370964df-56d3-4b76-944f-381e5cdd390d?resizing_type=fit) | [Transform tools video of object rotating.](https://dev.epicgames.com/community/api/documentation/image/ad04c343-2037-49ba-b0a2-f3bf7c52a509?resizing_type=fit) |
| **Move** | **Rotate** | **Scale** |

  You can click the **Coordinate Space** icon to toggle between World and Local space that affects how objects in the viewport are translated and rotated.

[![Coordinate space tool in toolbar.](https://dev.epicgames.com/community/api/documentation/image/de95532e-13f1-45db-b126-a2c2ac2c1ceb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de95532e-13f1-45db-b126-a2c2ac2c1ceb?resizing_type=fit)

| Icon | Name | Keyboard Shortcut | Description |
| --- | --- | --- | --- |
| [World space coordinates icon](https://dev.epicgames.com/community/api/documentation/image/ed536087-8a6f-47d3-acd2-fd288e379625?resizing_type=fit) | **World Space Coordinates** | **CTRL + `** | This icon is the coordinate system used for World Space (the entire level), with its origin being the center of the scene (the world grid). This coordinate system is fixed — you cannot transform it. Objects are translated and rotated in absolute units relative to the level’s origin and scale relative to the entire level. |
| [Local space coordinates icon](https://dev.epicgames.com/community/api/documentation/image/b274eda8-0131-4e54-95fe-f2ed90445b1d?resizing_type=fit) | **Local Space Coordinates** | **CTRL + `** | This icon is the coordinate system used for Local (Object) Space with its coordinate system relative to the scene component to which the actor is attached. Every actor has a local space coordinate system within a scene relative to the actor’s pivot point. Use local space to translate or rotate an object relative to its parent. |

|  |  |
| --- | --- |
| [Video of world space view and rotate.](https://dev.epicgames.com/community/api/documentation/image/65808225-afc5-48ca-8b51-4f80a7384d78?resizing_type=fit) | [Video of local space move and rotate.](https://dev.epicgames.com/community/api/documentation/image/ef0618b6-ea57-4b87-837b-2f82768fec7e?resizing_type=fit) |
| **World Space Move and Rotate** | **Local Space Move and Rotate** |

For more in-depth explanations of Unreal Engine’s coordinate system and coordinate spaces for transforming objects within a 3D space, see [Coordinate System and Spaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinate-system-and-spaces-in-unreal-engine).

#### Viewport-Related Transform Tools Menu

The **Transform** toolbar dropdown menu contains a list of transform options, coordinate spaces, and options for how the gizmo is displayed in the level editor viewport. Some options here, such as transform tool and coordinate system are available as quick-select options in the viewport toolbar.

[![Image of transform tools menu with checkbox options.](https://dev.epicgames.com/community/api/documentation/image/c19febae-2ea7-489a-afca-f63746d125b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c19febae-2ea7-489a-afca-f63746d125b8?resizing_type=fit)

  The menu is broken down into the following categories:

| Menu Section | Name | Description |
| --- | --- | --- |
| [Transform tools menu.](https://dev.epicgames.com/community/api/documentation/image/5e1e6a98-6d1e-41fc-8a0f-c2cc7d4993c7?resizing_type=fit) | **Transform Tools** | Menu options to select the transform tool or coordinate space you want to use. These options are available as quick-select options in the viewport toolbar. |
| [Transform tools menu, gizmo options.](https://dev.epicgames.com/community/api/documentation/image/aa7f0e10-60de-44ff-b92f-520aa56d04f8?resizing_type=fit) | **Gizmo Options** | Menu options to change how you view and interact with the transform tools gizmo when objects are selected. |
| [Transform tools menu, selection options.](https://dev.epicgames.com/community/api/documentation/image/cea80378-3fad-40b9-a4a9-6726011aadfc?resizing_type=fit) | **Selection Options** | Menu options to change how you select objects in the viewport. |

### Snapping Tools & Snap Settings

The **Snapping** tools includes a set of quick selection tools for snap sizes and angles to move, rotate, and scale objects in incremental steps. The snap settings also include options for how objects should snap to other objects and surfaces.

The **Snapping Settings** dropdown displays a list of optional toggles for how objects snap within the world.

[![Snapping tools menu.](https://dev.epicgames.com/community/api/documentation/image/99d5f8fc-7f8e-44b1-83f8-4bbaccea59fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99d5f8fc-7f8e-44b1-83f8-4bbaccea59fe?resizing_type=fit)

The toolbar includes quick-select snapping toggles and size / angle increments settings.

[![Snapping tools increment settings.](https://dev.epicgames.com/community/api/documentation/image/81b7f217-7421-4eab-a956-bf8b86c11678?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81b7f217-7421-4eab-a956-bf8b86c11678?resizing_type=fit)

When clicking on the values next to any quick-select snapping icon in the toolbar, you can use its dropdown to set a value, or select from available ones to use.

|  |  |  |  |
| --- | --- | --- | --- |
| [Surface snapping setting options.](https://dev.epicgames.com/community/api/documentation/image/e4034613-7dde-4d78-9070-266520a01162?resizing_type=fit) | [Snapping menu, grid snap options.](https://dev.epicgames.com/community/api/documentation/image/817b97f9-86d4-451b-a274-3c3cfbad7e77?resizing_type=fit) | [Rotation angle snap increments.](https://dev.epicgames.com/community/api/documentation/image/aaf70367-3665-42ed-8891-f99ffa70eaa5?resizing_type=fit) | [Snapping menu scaling options.](https://dev.epicgames.com/community/api/documentation/image/a10a3765-54a6-4585-825a-ff0eed28d2a0?resizing_type=fit) |
| **Surface Snapping Settings** | **Grid Snap Sizes** | **Rotation Angle Snap Increments** | **Scaling Snap Sizes** |

#### Snap to Surfaces Settings

The **Surface Snapping** settings dropdown sets the snapping behavior of objects when you drag them around in the scene.

[![Surface snapping menu.](https://dev.epicgames.com/community/api/documentation/image/00651981-91ec-475c-9aa5-6e9324c71463?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00651981-91ec-475c-9aa5-6e9324c71463?resizing_type=fit)

The **Rotate to Normal Surface** setting toggles whether objects should align to the surface's normal direction they are being snapped to. For example, when an object, like the pillar below, is dragged along a curved surface, it aligns to the direction of the curved surface when this setting is enabled. When disabled, the pillar will always face in the direction it is oriented.

|  |  |
| --- | --- |
| [Video clip of normal rotate to surface action.](https://dev.epicgames.com/community/api/documentation/image/f17da804-2de5-4981-8a8c-1dbdae69b76c?resizing_type=fit) | [Video of Rotate to surface in off mode.](https://dev.epicgames.com/community/api/documentation/image/0a52916f-4043-417c-8b77-3ca526009a7c?resizing_type=fit) |
| **Rotate to Surface Normal: ON (default)** | **Rotate to Surface Normal: OFF** |

## Viewport Toolbar Camera Settings

The **Camera Settings** contain options that affect the camera view for the viewport and the look of the scene.

[![Toolbar camera settings.](https://dev.epicgames.com/community/api/documentation/image/9dedf700-3edf-487a-a6cc-1b92c095251e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9dedf700-3edf-487a-a6cc-1b92c095251e?resizing_type=fit)

| Icon | Name | Description |
| --- | --- | --- |
| [Camera perspective options](https://dev.epicgames.com/community/api/documentation/image/d8ef1553-42ab-4857-90d9-a7da3235f368?resizing_type=fit) | **Camera Options** | A selection of options that affect the look of the viewport, its view, and includes the access to the high resolution screenshot tool. |
| [Camera speed options icon](https://dev.epicgames.com/community/api/documentation/image/7f22b887-418e-45e6-8101-57a68fc51f01?resizing_type=fit) | **Camera Speed Options** | Options that control the speed of the camera when moving through the world. |

### Camera Options Menu

You can click on the **Camera Options** dropdown menu that includes options to change the look of the viewport, switch between camera views for perspective and orthographic, set the viewport to a cinematic view, and more. The options available in this menu change depending on cameras placed in the level and whether you are using a perspective or orthographic view.

[![Camera toolbar menu.](https://dev.epicgames.com/community/api/documentation/image/af5b150d-f75b-4189-87f1-e3892aaf6b4f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af5b150d-f75b-4189-87f1-e3892aaf6b4f?resizing_type=fit)

  This menu is broken up into the following sections:

| Menu Section | Name | Description |
| --- | --- | --- |
| [Camera perspective menu options.](https://dev.epicgames.com/community/api/documentation/image/5b8a8710-c522-4063-979d-05768aa2cae0?resizing_type=fit) | **Perspective** | This camera view simulates how the human eye perceives the world. This camera view is the default view used for all viewports. The **View** options in this menu that affect field of view, near view plane, and far view plane are specific to the perspective camera view. |
| [Camera orthographic menu options.](https://dev.epicgames.com/community/api/documentation/image/9e505886-f138-4784-8031-1d528f412805?resizing_type=fit) | **Orthographic** | This camera view uses a projection that maintains parallel lines, whereby objects appear to have the same scale regardless of their distance from the camera. This includes views for top, bottom, left, right, front, and back. |
| [Camera movement menu options.](https://dev.epicgames.com/community/api/documentation/image/59b55901-60cc-4c03-b13d-78ff48915096?resizing_type=fit) | **Movement** | Options to change how the viewport camera moves. You can pilot other actors in the scene and change the movement of the camera. |
| [Camera view menu options.](https://dev.epicgames.com/community/api/documentation/image/0ed63789-b195-496c-883f-725bca882221?resizing_type=fit) | **View** | When the **Perspective** view is used, these options change the field of view, near view plane, and far view plane for how content is shown in the viewport. |
| [Camera exposure menu options.](https://dev.epicgames.com/community/api/documentation/image/2a1bd87b-b0ec-4801-926e-f1498172b7f2?resizing_type=fit) | **Exposure** | Override settings change the exposure value in the viewport. When Game Settings is disabled, you can use the text field to override the camera exposure for the viewport. |
| [Camera viewport type menu options.](https://dev.epicgames.com/community/api/documentation/image/16b804ae-e5d3-42b2-8818-7124eae4fd4d?resizing_type=fit) | **Viewport Type** | Choose a viewport layout to use. The **Cinematic Viewport** layout is tailored for cinematic workflows and adds the **Composition Overlays** options menu to the toolbar, where you can select different overlays for framing, masking, and composition. |
| [Camera create menu options.](https://dev.epicgames.com/community/api/documentation/image/9a23614c-b413-4a5c-b9aa-67ad92ced0a5?resizing_type=fit) | **Create** | Options to create camera actors in the world and scene bookmarks for camera views in the world. |
| [Camera options menu choices.](https://dev.epicgames.com/community/api/documentation/image/ae7ac020-c440-4d69-873c-eafb922ee619?resizing_type=fit) | **Options** | Toggleable settings that affect the viewport, such as game view that disables selection highlight and gizmos tools, or **Preview Selected Cameras** sets how large the preview window for a selected camera is in the bottom-right of the viewport. |

### Camera Perspective & Orthographic Views

You can use the **Camera Options** menu to select how content is displayed in the viewport. The default viewport uses the **Perspective** view, but you can select from a list of **Orthographic** views to use as well.

[![Perspective and orthographic menu options.](https://dev.epicgames.com/community/api/documentation/image/fdd342af-5f81-45d7-94a7-1984912ff8d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fdd342af-5f81-45d7-94a7-1984912ff8d7?resizing_type=fit)

  Below is an example of different views in the viewport for both orthographic and perspective.

[![Orthographic and perspective views in 4 viewports.](https://dev.epicgames.com/community/api/documentation/image/f42680c1-eb52-4f26-a995-c25692213e6a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f42680c1-eb52-4f26-a995-c25692213e6a?resizing_type=fit)

### Movement Options

The **Movement** options section of the menu includes options for how you pilot actors using the viewport, and change camera movement in the viewport.

[![Camera movement options menu.](https://dev.epicgames.com/community/api/documentation/image/ff70792f-4e7d-45b0-a84b-b4f9c5e1da39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff70792f-4e7d-45b0-a84b-b4f9c5e1da39?resizing_type=fit)

  This section of the menu includes the following settings:

| Setting Name | Description |
| --- | --- |
| Pilot |  |
| **Pilot [Selected Actor]** | Move the selected actor around using the viewport controls, and bind the viewport to the actor’s location and orientation. |
| **Stop Piloting Actor** | When piloting is enabled for an actor, this stops piloting of an actor with the current viewport. It unlocks the viewport’s position and orientation from the actor the viewport is currently piloting. |
| **Exact Camera View** | Toggles showing the exact camera view when using the viewport to pilot a camera. |
| **Selected Piloted Actor** | Selects the currently piloted actor in the Outliner. |
| Camera Movement |  |
| --- | --- |
| **Camera Speed** | Set the camera speed for movement in the viewport. These options are available from the quick-select toolbar as well. |
| **Frame Selected** | Centers the viewport on the selected actor(s). |
| **Move Camera to Object** | Move the current camera to match the location and rotation of the selected object. |
| **Move Object to Camera** | Move the selected object to match the location and rotation of the current camera. |
| **Orbit Around Selection** | If enabled, the camera will orbit around the current selection in the viewport. |
| **Link Ortho Camera Movement** | If enabled, all orthographic viewports are linked to the same position and move together. When disabled, they move independent of one another. |
| **Ortho Zoom to Cursor** | If enabled, orthographic viewport zooming centers on the mouse cursor’s position. When disabled, the zoom is around the center of the viewport. |

### View Options

The **View** options are available when the viewport is using the **Perspective** view. These options configure the viewing angle of the viewport camera, and at what distance content should be visible from this camera.

[![Image of menu options for field of view.](https://dev.epicgames.com/community/api/documentation/image/db4da03f-8be2-47b7-8089-1d2af9781ab8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db4da03f-8be2-47b7-8089-1d2af9781ab8?resizing_type=fit)

  This section includes the following settings:

| Setting Name | Description |
| --- | --- |
| **Field of View** | Sets the viewing angle of the viewport camera. This angle defines the extent of the world that is visible to the camera at any given time. The default is a **90 degree** viewing angle. Higher angles give you wider views to see more of the world but this skews the camera view. Lower angles show less of the world, feeling zoomed in, but the view of content is limited. |
| **Near View Plane** | Sets the size of the plane used to clip through objects when the camera is close to a surface. Large values make the clip plane bigger to see through objects more easily. |
| **Far View Plane** | Sets the far distance at which objects stop being rendered on screen.    This value does not affect objects that have Nanite enabled. |

In the example below, you can see how adjusting the field of view angle affectss your view:

|  |  |  |
| --- | --- | --- |
| [Example field of view at 65 degrees.](https://dev.epicgames.com/community/api/documentation/image/2b6cb9d2-7977-40c9-8829-9c001a8572cc?resizing_type=fit) | [Example field of view at 90 degrees.](https://dev.epicgames.com/community/api/documentation/image/0e58de84-d150-41f8-868f-109e5c800d8b?resizing_type=fit) | [Example field of view at 120 degrees.](https://dev.epicgames.com/community/api/documentation/image/0f4d478a-3766-4ad2-bcb3-dae7d6e98c1d?resizing_type=fit) |
| **Field of View: 65 Degrees** | **Field of View: 90 Degrees (Default)** | **Field of View: 120 Degrees** |

### Create Options

The **Create** options provide a way to place cameras and bookmarks in the world based on the current viewport location and orientation.

[![Options in the Create camera menu.](https://dev.epicgames.com/community/api/documentation/image/03f61040-bb98-4c20-927c-0d48b4e63296?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03f61040-bb98-4c20-927c-0d48b4e63296?resizing_type=fit)

  This section includes the following options:

| Setting Name | Description |
| --- | --- |
| Create Camera |  |
| **Camera Actor** | Spawn a Camera actor in the current location and orientation of the viewport. |
| **Cine Camera Actor** | Spawn a Cine Camera actor in the current location and orientation of the viewport. |
| Bookmarks |  |
| --- | --- |
| **Set Bookmark** | Choose a bookmark from the list to set with the current viewport location and orientation. |
| **Manage Bookmarks** | * **Clear Bookmark**: Clears a specific bookmark that has been saved. * **Compact Bookmarks**: Attempts to move bookmark indices so they are continuous. For example, if you have bookmarks for 1, 2, and 4 slots bookmarked, this will attempt to move bookmark 4 to the bookmark 3 slot. * **Clear All Bookmarks**: Clears any saved bookmarks. |
| **Bookmarks List** | A list of any bookmarks that have been saved and what keyboard shortcut they are assigned to. |

### General Options

The **Options** section of the menu includes general settings you can enable for the viewport. It also includes access to the **High Resolution Screenshot** tool, to capture still images from the viewport quickly.

[![General options menu items.](https://dev.epicgames.com/community/api/documentation/image/56c74bb9-a206-4fd6-9f6e-917f46a8695a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56c74bb9-a206-4fd6-9f6e-917f46a8695a?resizing_type=fit)

  This section includes the following options:

| Setting Name | Description |
| --- | --- |
| **Allow Cinematic Control** | When enabled, this allows for cinematic (Sequencer) previews to play in this viewport. |
| **Game View** | When enabled, the viewport shows the scene as it appears in the game — without editor widgets, selection highlights, or any other element usually only visible in the editor. |
| **Allow Camera Shakes** | When enabled, it allows for the camera shake previewer panel to apply shaking to this viewport. |
| **Preview Selected Cameras** | When enabled, selecting a camera actor displays a live picture-in-picture preview from the camera’s perspective within the current editor viewport. This can be used to make adjustments to positioning, post processing, and other settings without having to possess the camera itself. The **Preview Size** value adjusts the size of this picture-in-picture preview window for the camera view. |
| **High Resolution Screenshot** | Opens the control panel dialog to take high resolution screenshots of the currently used viewport. |

#### High Resolution Screenshot Tool

The **High Resolution Screenshot** tool is a dialog window you can use to capture still images of the current viewport window or you can use the **Crop** tool to select a part of the viewport to capture. It includes additional output options you can toggle on.

[![Menu options for the high resolution screenshot tool.](https://dev.epicgames.com/community/api/documentation/image/cd118747-fbe2-43aa-a41a-fc21a93309ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd118747-fbe2-43aa-a41a-fc21a93309ec?resizing_type=fit)

  For more information on using this tool, see [High Resolution Screenshot Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/taking-screenshots-in-unreal-engine#high-resolution-screenshot-tool).

### Camera Speed Options

The **Camera Speed** dropdown menu includes options that affect the speed at which the camera can move around the world.

[![View of camera speed menu items.](https://dev.epicgames.com/community/api/documentation/image/feb6ac89-145e-487d-a419-67c3660a55b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/feb6ac89-145e-487d-a419-67c3660a55b0?resizing_type=fit)

| Setting Name | Description |
| --- | --- |
| **Camera Speed** | Sets the speed of the camera in first person mode.  Hold either mouse button (LMB or RMB) and use the scroll wheel to adjust the camera speed up or down. |
| **Speed Scalar** | Multiplies the effective value of the camera speed slider, changing how quickly the slider changes camera speed. |
| **Distance Based Camera Speed** | When enabled, this scales the perspective camera speed based on the distance between the camera and its look-at position. |

## Viewport Toolbar View Mode and Show Flag Options

The **View Mode** and **Show Flag** options for the viewport enable different visualization modes and options to enable or disable elements being rendered in the viewport.

[![View of toolbar icons for view mode and show flag.](https://dev.epicgames.com/community/api/documentation/image/df92925c-5a37-4fb8-9e95-a3c006e9d007?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df92925c-5a37-4fb8-9e95-a3c006e9d007?resizing_type=fit)

| Icon | Name | Description |
| --- | --- | --- |
| [Image of view mode button.](https://dev.epicgames.com/community/api/documentation/image/4b17f05d-8719-4868-a8fb-5d31157d99b7?resizing_type=fit) | **Viewport Modes** | A listing of visualization modes to help see specific types of data being processed in your scene, such as lighting only, reflections, or buffer visualizations. These can help you diagnose and investigate specific issues for your project. |
| [View of show flag icon.](https://dev.epicgames.com/community/api/documentation/image/d8257806-4096-4706-b5bf-0ac0ecbab95e?resizing_type=fit) | **Show Flags** | A list of engine features you can show and hide within the viewport. For example, you can disable all particle systems, individual post processing features, and more. |

### Viewport Modes

The **Viewport Modes** dropdown menu includes many visualization options to select from. When selected, they apply to the current viewport only.

[![Image of the viewport modes dropdown menu items.](https://dev.epicgames.com/community/api/documentation/image/3d29525a-52e9-4f0a-98b6-a60d314bb09b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d29525a-52e9-4f0a-98b6-a60d314bb09b?resizing_type=fit)

These are some examples of different viewport modes being applied to the viewport:

|  |  |  |
| --- | --- | --- |
| [View of a set with the walls and actors lit.](https://dev.epicgames.com/community/api/documentation/image/68116b60-e222-4703-bd8e-4dd90ffffce8?resizing_type=fit) | [View of a set with the walls and actors unlit.](https://dev.epicgames.com/community/api/documentation/image/700bce53-2264-423b-878a-4a1535d6dd76?resizing_type=fit) | [View of a set with the walls and actors in light gradient..](https://dev.epicgames.com/community/api/documentation/image/f2354e6a-acf3-4038-8293-69f77697a7fa?resizing_type=fit) |
| Viewport Mode: Lit (default) | Viewport Mode: Unlit | View Modeport: Light Complexity |

For more information on using these viewport modes in your project workflows, see [Viewport Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine).

### Show Flags

The **Show Flags** dropdown menu includes many options to toggle visibility of engine features, such as lighting, post processing, geometry types, and more.

[![Image of show flags menu items.](https://dev.epicgames.com/community/api/documentation/image/64dd26de-4693-4f31-a870-5552d3291aa1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64dd26de-4693-4f31-a870-5552d3291aa1?resizing_type=fit)

For more information on using these show flags in your project, see [Viewport Show Flags](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-show-flags-in-unreal-engine).

## Viewport Toolbar Performance and Scalability Tools

The **Performance** and **Scalability Tool** menu includes options that affect the look and performance of content in the viewport. These tools are useful for approximating what content looks like on a particular platform, setting scalability for the project (to make it easier to work with), and looking at how the game can look with different scalability options. This can help you to set up your own scalability options for your project.

[![Image of scalability menu options on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/bec1f7fa-d1a1-4baa-896f-b41b531386fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bec1f7fa-d1a1-4baa-896f-b41b531386fe?resizing_type=fit)

### Realtime Viewport

The **Realtime Viewport** toggles whether the current viewport should update every frame.

When disabled, the viewport only updates when you move around the scene. A warning icon is added to the viewport toolbar next to the performance and scalability dropdown menu. Clicking it restores realtime to the viewport.

[![Image of warning icon next to the realtime viewer.](https://dev.epicgames.com/community/api/documentation/image/5e43c4d4-f97a-411a-96ce-bffbdf3a6aab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e43c4d4-f97a-411a-96ce-bffbdf3a6aab?resizing_type=fit)

### Preview Platform

The **Preview Platform** rollout menu includes a variety of platform options to select from. Selecting platform and its target, triggers a shader recompile for the engine. Once completed, the viewport updates to display an approximation of what the scene would render like using this target.

Each platform can have multiple targets depending on what rendering paths of the engine it supports.

[![Preview platform menu dropdowns.](https://dev.epicgames.com/community/api/documentation/image/54c607c3-cf0d-42ce-8af9-ce98fdfe814a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54c607c3-cf0d-42ce-8af9-ce98fdfe814a?resizing_type=fit)

This menu rollout includes the following options:

| Setting Name | Description |
| --- | --- |
| Preview Platform |  |
| **Disable Preview** | Disables any currently selected preview platform target and sets it back to the operating system's default preview. For Windows, this would be Windows with Shader Model 6 (SM6). |
| **[Platform Preview Select]** | Choose from a list of platform targets to preview in the main editor viewport. Each platform can support multiple targets, such as Android with OpenGL and Vulkan preview options. Some platform preview options, such as console platforms, only become available when their SDKs are installed. |

The scene below shows a comparison of the default viewport preview settings on WIndows compared to previewing the scene on Android in the viewport.

|  |  |
| --- | --- |
| [Statue in a foyer, darker version image.](https://dev.epicgames.com/community/api/documentation/image/c4fbc4df-e423-4aeb-bb71-73d5b64784d8?resizing_type=fit) | [Statue in a foyer, better lighting.](https://dev.epicgames.com/community/api/documentation/image/827bf15b-6632-4588-aca2-f1961613ddd6?resizing_type=fit) |
| **Windows with SM6** | **Android with Vulkan High** |

For more information, see [Mobile Previewer](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-mobile-previewer-in-unreal-engine).

### Viewport Scalability

The **Viewport Scalability** options include a rollout menu of common settings of the engine. You can change individual feature categories to be Low, Medium, High, Epic, or Cinematic, or you can select any of these quality options to set all categories to be Low, Medium, High, Epic, or Cinematic. Optionally, you can use **Auto** to configure the scalability options based on your system specifications and its performance.

[![Image of viewport scalability groups.](https://dev.epicgames.com/community/api/documentation/image/042331db-11bc-4573-b17b-dccff46a8aef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/042331db-11bc-4573-b17b-dccff46a8aef?resizing_type=fit)

When the scalability options are set to anything other than the default, this warning icon appears in the toolbar. This is an indicator that what the game would look like running outside of the editor doesn’t reflect the options currently set in the scalability options. You can click this icon to reset the scalability options to their default settings.

[![Viewport scalability icon on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/6cd64904-3c73-462a-ad4f-eb8365b85fa4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cd64904-3c73-462a-ad4f-eb8365b85fa4?resizing_type=fit)

For more information, see [Scalability](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-in-unreal-engine).

### Material Quality Level

The **Material Quality Level** rollout menu lists quality levels for Low, Medium, High, and Epic to choose from. You can use these to check any materials that use the **Quality Switch** node in a material. You can use these menu options to inspect only materials in the viewport. The material quality switches also work with the scalability options.

[![Material quality menu options.](https://dev.epicgames.com/community/api/documentation/image/8679081e-7f87-40c1-b8d9-23ef845f4868?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8679081e-7f87-40c1-b8d9-23ef845f4868?resizing_type=fit)

### Screen Percentage

The **Screen Percentage** rollout menu includes information about the current screen percentage used in the viewport, and options to override screen percentage in the viewport. The summary in this menu provides specific information about the viewport and its current settings.

[![Image of the screen percentage menu options.](https://dev.epicgames.com/community/api/documentation/image/4c493df0-39f1-473b-b9f2-07bedf029090?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4c493df0-39f1-473b-b9f2-07bedf029090?resizing_type=fit)

## Viewport-Related Settings

The viewport **Settings** and **Overlay** menus assist with audio settings, mouse movement within the viewport, viewport layout options (for working with multiple viewports), and more.

[![Image of the settings and viewport-layout icons on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/8a159805-f927-489c-9753-e255c3841975?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a159805-f927-489c-9753-e255c3841975?resizing_type=fit)

| Icon | Name | Description |
| --- | --- | --- |
| [Viewport settings icon.](https://dev.epicgames.com/community/api/documentation/image/79a550b8-2ef7-4fbd-ab27-7fa0eac4e5ee?resizing_type=fit) | **Viewport Settings** | A list of settings to control the volume of sounds in the level editor, configurable controls for interacting and traversing the scene in the level editor viewport, and more. |
| [Viewport layout icon.](https://dev.epicgames.com/community/api/documentation/image/7fa0062e-dae0-4ef8-bfce-3e8bcc138f95?resizing_type=fit) | **Viewport Layout Options** | A list of viewport layouts to choose from when using more than one viewport. |

### Viewport Settings

The **Viewport Settings** menu includes options that affect controls and interactions with objects within the viewport, sound levels for audio playback, and quick access to the **Editor Preferences** you can configure for the viewport.

[![Viewport settings menu options.](https://dev.epicgames.com/community/api/documentation/image/b57b2916-1013-4f1d-a74a-6cb989dd5876?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b57b2916-1013-4f1d-a74a-6cb989dd5876?resizing_type=fit)

| Settings Name | Description |
| --- | --- |
| Settings |  |
| **Level Editor Volume (dB)** | Sets the preview volume (in decibels) of audio placed in the level while working in the level editor. |
| Controls |  |
| --- | --- |
| **Mouse Sensitivity** | How fast the perspective camera moves through the world when using the mouse scroll wheel. |
| **Mouse Scroll Zoom Speed** | Sets the incremental speed at which the camera should move in a forward or reverse direction when using the mouse scroll wheel. |
| **Invert Middle Mouse Pan** | When enabled, the direction of the middle mouse panning in the viewport is inverted. |
| **Invert Orbit Axis** | When enabled, the Y-axis of the mouse movement when orbiting is inverted. |
| **Invert Right Mouse Dolly** | When enabled, the direction of the right mouse dolly on the Y-axis in orbit mode is inverted. |
| **Scroll Gestures** | Set whether scroll gestures should use standard or natural scrolling when working in the **Perspective** and **Orthographic** viewports. |
| **Open Viewport Preferences** | Opens the advanced viewport settings of the **Editor Preferences**. There, you can configure settings for the look and feel, controls, grid snapping, and more. |
| Cascade |  |
| --- | --- |
| **Cascade** | These settings only apply to the deprecated particle systems created with Cascade.   * Enable Particle Systems LOD Switching: When enabled, Cascade particle systems will use distance level of detail (LOD) switching in perspective viewports. * **Toggle Particle System Helpers**: When enabled, Cascade particle systems show helper widgets in viewports. * **Freeze Particle Simulation**: When enabled, Cascade particle systems will freeze their simulation state. |

### Viewport Layouts and Sizing Settings

The **Viewport Layouts** includes a layouts window to select the type of viewport layout you prefer, and a quick-toggle to switch between a selected layout and maximized viewport screen.

[![Viewport layouts icon and ellipses on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/4fd0ef66-a187-4eb1-97bd-58020e8e8243?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fd0ef66-a187-4eb1-97bd-58020e8e8243?resizing_type=fit)

The vertical ellipses menu includes different layout configurations you can choose from, including an option to use **Immersive View** with the selected viewport.

[![Viewport panes menu options in the toolbar.](https://dev.epicgames.com/community/api/documentation/image/d49176a3-1884-46d2-9155-bb5ccbc7f985?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d49176a3-1884-46d2-9155-bb5ccbc7f985?resizing_type=fit)

The quick-toggle button switches between maximizing the currently selected viewport or switching to the selected layout configuration with multiple viewports displayed in the editor window.

[![Quick toggle menu icon on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/9decc4e3-649a-42ec-a695-07bde74ee80e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9decc4e3-649a-42ec-a695-07bde74ee80e?resizing_type=fit)

In this example, clicking the overlay toggle buttons will switch between the maximized and selected layout for the editor viewports.

Video of clicking through adjusting to multiple viewports view.

### Viewport Toolbar Warning Indicators

When the interaction within a menu alters something critical that affects the viewport, such as a change that could cause visual or performative differences, actionable warning indicators appear in the viewport toolbar alongside the category they affect. This is helpful to indicate a change has occurred that can affect what you see in the viewport in some way.

For example, when **Realtime Viewport** is disabled, the warning indicator can clue you into the fact that the viewport isn’t updating what you see, which can have unintended consequences.

When these indicators are shown, you can click them to rest the changed setting to its default state, in turn removing the warning.

[![Realtime viewport warning icon on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/029ba3a2-c6a8-4387-b664-8b0fd70b90b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/029ba3a2-c6a8-4387-b664-8b0fd70b90b2?resizing_type=fit)

### Other Editor Viewports

The **Viewport Toolbar** is adapted to different modes of the level editor and to the individual asset editors it has.

The sections below are some examples of these differences.

### Level Editor Viewport Modes

The level editor can be put into different **Modes** to enable specialized editing interfaces and workflows for editing particular types of actors and geometry within the viewport.

You can change the level editor mode using the dropdown selection menu in the main toolbar.

[![Menu of categories you can select via the selection tool.](https://dev.epicgames.com/community/api/documentation/image/f48c6934-f883-4516-b7e3-818e95323a89?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f48c6934-f883-4516-b7e3-818e95323a89?resizing_type=fit)

These modes change the primary behavior of the level editor viewport for a specialized task, such as moving and transforming assets in the world, sculpting landscapes, generating foliage, animating objects, and more.

| Level Editor Mode | Viewport Toolbar |
| --- | --- |
| **Selection (default)** | [Default toolbar for level editor modes.](https://dev.epicgames.com/community/api/documentation/image/2f322b76-90a1-41b9-bb47-18c7e6cb1cbb?resizing_type=fit) |
| **Animation** | [Animation toolbar for level editor modes.](https://dev.epicgames.com/community/api/documentation/image/44930c53-3974-42d4-948d-4837995abfd3?resizing_type=fit) |
| **Modeling** | [Modeling toolbar for level editor modes.](https://dev.epicgames.com/community/api/documentation/image/4110e3f3-5706-485f-a194-2dc04ede5de8?resizing_type=fit) |

For more information on these editor modes, see [Level Editor Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine).

### Asset Editors

Individual **Asset Editors** use a viewport toolbar adapted to their editors and functionality within.

In this example, you can see a comparison of the legacy viewport toolbar to the improved viewport toolbar.

[![Legacy editor under current toolbar for comparison.](https://dev.epicgames.com/community/api/documentation/image/88b1cfe4-2351-4550-b3ca-b12f7cd5ae3c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88b1cfe4-2351-4550-b3ca-b12f7cd5ae3c?resizing_type=fit)

Below are examples of the different viewport toolbars you’ll see in different editors:

| Viewport Toolbar Location | Viewport Toolbar Representation |
| --- | --- |
| **Level Editor Selection Mode** | [Level editor selection mode toolbar layout.](https://dev.epicgames.com/community/api/documentation/image/e6ac847d-f6d9-407a-889c-bd6c5ecb7f10?resizing_type=fit) |
| **Static Mesh Editor** | [Static mesh editor toolbar layout.](https://dev.epicgames.com/community/api/documentation/image/b3f66d0b-c004-4310-8074-87ddf5911c2a?resizing_type=fit) |
| **Material / Material Instance Editor** | [Material instance editor toolbar layout.](https://dev.epicgames.com/community/api/documentation/image/6ee70b32-d73e-4f75-9129-b7b60c608100?resizing_type=fit) |

### Asset Editor Preview Scene Settings

**Asset Editor** viewports use a preview scene to display their assets. This scene can give you an idea of how that asset will look in a lit environment. You can change properties of the scene using the **Preview Scene Settings**.

You can access a portion of these settings from the viewport toolbar by clicking its menu.

[![Asset editor preview scene menu settings.](https://dev.epicgames.com/community/api/documentation/image/f4df69e5-b16f-41c4-a0d9-c8c6abe6a2b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f4df69e5-b16f-41c4-a0d9-c8c6abe6a2b3?resizing_type=fit)

If you want to make additional changes to the scene in the viewport, select Preview Scene Settings from this menu to open the Preview Scene Settings panel, where you’ll have access to additional lighting, post process, and scene options.

[![The preview scene settings panel for more options.](https://dev.epicgames.com/community/api/documentation/image/eca9b1df-ebb6-489e-bee1-7f365c7858bd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eca9b1df-ebb6-489e-bee1-7f365c7858bd?resizing_type=fit)

### Materials and Material Instances Viewport Toolbars

The **Material** and **Material Instance** editors display a limited viewport toolbar. Since these editors are previewing a material and how it renders on an object within an environment, viewport controls found in other editors simply aren’t necessary here.

[![Materials options icons on the toolbar.](https://dev.epicgames.com/community/api/documentation/image/029b2c64-9055-487a-9fdc-6b378d0804ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/029b2c64-9055-487a-9fdc-6b378d0804ee?resizing_type=fit)

The notable difference between these editors and others is that **Preview Mesh** options are included in the viewport toolbar. You can choose one of the provided shapes, or select a custom mesh from the **Content Browser** to preview the material.

* [editor](https://dev.epicgames.com/community/search?query=editor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Improved Viewport Toolbar versus the Legacy Viewport Toolbar](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#improvedviewporttoolbarversusthelegacyviewporttoolbar)
* [Viewport Toolbar Interface](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewporttoolbarinterface)
* [Viewport Toolbar Transform & Snapping Tools](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewport-toolbar-transform-amp-snapping-tools)
* [Transform Tools](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#transformtools)
* [Viewport-Related Transform Tools Menu](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewport-relatedtransformtoolsmenu)
* [Snapping Tools & Snap Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#snappingtools&snapsettings)
* [Snap to Surfaces Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#snaptosurfacessettings)
* [Viewport Toolbar Camera Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewport-toolbar-camera-settings)
* [Camera Options Menu](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#cameraoptionsmenu)
* [Camera Perspective & Orthographic Views](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#cameraperspective&orthographicviews)
* [Movement Options](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#movementoptions)
* [View Options](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewoptions)
* [Create Options](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#createoptions)
* [General Options](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#generaloptions)
* [High Resolution Screenshot Tool](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#highresolutionscreenshottool)
* [Camera Speed Options](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#cameraspeedoptions)
* [Viewport Toolbar View Mode and Show Flag Options](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewport-toolbar-view-mode-and-show-flag-options)
* [Viewport Modes](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewportmodes)
* [Show Flags](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#showflags)
* [Viewport Toolbar Performance and Scalability Tools](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewport-toolbar-performance-and-scalability-tools)
* [Realtime Viewport](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#realtimeviewport)
* [Preview Platform](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#previewplatform)
* [Viewport Scalability](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewportscalability)
* [Material Quality Level](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#materialqualitylevel)
* [Screen Percentage](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#screenpercentage)
* [Viewport-Related Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewport-related-settings)
* [Viewport Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewportsettings)
* [Viewport Layouts and Sizing Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewportlayoutsandsizingsettings)
* [Viewport Toolbar Warning Indicators](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#viewporttoolbarwarningindicators)
* [Other Editor Viewports](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#othereditorviewports)
* [Level Editor Viewport Modes](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#leveleditorviewportmodes)
* [Asset Editors](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#asseteditors)
* [Asset Editor Preview Scene Settings](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#asseteditorpreviewscenesettings)
* [Materials and Material Instances Viewport Toolbars](/documentation/en-us/unreal-engine/viewport-toolbar?application_version=5.7#materialsandmaterialinstancesviewporttoolbars)
