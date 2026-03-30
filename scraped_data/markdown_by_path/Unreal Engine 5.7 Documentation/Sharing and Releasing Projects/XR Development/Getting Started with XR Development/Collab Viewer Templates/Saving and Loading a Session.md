<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-a-session-in-unreal-engine?application_version=5.7 -->

# Saving and Loading a Session

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
7. [Getting Started with XR Development](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine "Getting Started with XR Development")
8. [Collab Viewer Templates](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine "Collab Viewer Templates")
9. Saving and Loading a Session

# Saving and Loading a Session

Describes how to save (and then later reload) a session, including Annotations, Measurements, and transparency

![Saving and Loading a Session](https://dev.epicgames.com/community/api/documentation/image/94cccf0a-4b85-492d-8855-578b2002c766?resizing_type=fill&width=1920&height=335)

 On this page

The host and other participants in a collaborative view can save annotations, measurements, **Xray** transparency state, **3D Cut** sections, and the position of items moved by **Transform**.

## Saving a Session

To save your session, select the **Save** button, type a name for the session, then press Enter.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8b1576b-5af5-4251-995f-941406de835e/01-save-button_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8b1576b-5af5-4251-995f-941406de835e/01-save-button_ue5.png)

Click for full image.

Each participant saves their session in their own local copy of the collaborative view package.
Sessions are saved in the `YourProjectName/Saved/SaveGames` sub-folder.

The current positions and rotations of you and other participants are not saved.

You cannot modify a saved session or use the name of an existing saved session.

You cannot save and restore sessions while in VR mode.

## Loading a Session

To load a saved session, select the menu next to the **Save** button, then select a session.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2aa5e20b-b81f-4198-86a6-145ed7424737/02-load-session_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2aa5e20b-b81f-4198-86a6-145ed7424737/02-load-session_ue5.png)

Click for full image.

The list of sessions includes those you have saved, as well as those saved by any other participants who are currently connected.

## Load States in the Unreal Editor

You can now reload saved states directly in the editor:

1. Copy the **.sav files** representing the states you want to reload as well as the **MainSaveGame.sav** file from your Saved / SaveGames folder from your application into the same folder in your project.
2. In the editor, open the **CollaborativeViewer > Blueprints > Tools** folder, select the **Editor\_CollabViewerUtility\_BP**. Right-click and select **Run Editor Utility Widget**.
3. A widget containing the Default state selector will appear, you can now select one of the copied states from the drop down list.
4. You might need to move the camera in the viewport to refresh the parameters.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38a1ac2d-4b12-4abb-9375-482ef985044b/03-load-states_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38a1ac2d-4b12-4abb-9375-482ef985044b/03-load-states_ue5.png)

Click for full image.

* [collaboration](https://dev.epicgames.com/community/search?query=collaboration)
* [templates](https://dev.epicgames.com/community/search?query=templates)
* [collab viewer](https://dev.epicgames.com/community/search?query=collab%20viewer)
* [design review](https://dev.epicgames.com/community/search?query=design%20review)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Saving a Session](/documentation/en-us/unreal-engine/saving-and-loading-a-session-in-unreal-engine?application_version=5.7#savingasession)
* [Loading a Session](/documentation/en-us/unreal-engine/saving-and-loading-a-session-in-unreal-engine?application_version=5.7#loadingasession)
* [Load States in the Unreal Editor](/documentation/en-us/unreal-engine/saving-and-loading-a-session-in-unreal-engine?application_version=5.7#loadstatesintheunrealeditor)
