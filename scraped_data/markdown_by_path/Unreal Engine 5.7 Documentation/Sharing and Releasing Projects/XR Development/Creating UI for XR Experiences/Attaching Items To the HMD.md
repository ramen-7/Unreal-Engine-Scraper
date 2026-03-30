<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/attaching-items-to-the-hmd-in-unreal-engine?application_version=5.7 -->

# Attaching Items To the HMD

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
7. [Creating UI for XR Experiences](/documentation/en-us/unreal-engine/design-user-interfaces-for-xr-experiences-in-unreal-engine "Creating UI for XR Experiences")
8. Attaching Items To the HMD

# Attaching Items To the HMD

Information on attaching items to any HMD.

![Attaching Items To the HMD](https://dev.epicgames.com/community/api/documentation/image/5cc17e31-3018-46cc-8e8f-9ee871cfdc14?resizing_type=fill&width=1920&height=335)

 On this page

No matter which Head Mounted Display (HMD) you are developing for Unreal Engine 4 (UE4) offers a unified approach to attaching items to the HMD. Not only will this unified approach work with any HMD, the items that are attached will move perfectly in-sync with the HMD. In the following document, we will go over all you need to know about attaching items to the HMD.

Now if you want to get the position of the player in the world you can just get the Camera Actor's position.

## Setting Up Objects To Follow The HMD

You can setup a Static Mesh, Particle Effect, UI elements and many more items to follow the movment of the HMD by doing the following.

1. First open up your Pawn Blueprint and navigate to the **Viewport** tab.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77804a7d-b9a3-4e6c-9d95-3f130650b76e/vr_follow_hmd_setup_00.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77804a7d-b9a3-4e6c-9d95-3f130650b76e/vr_follow_hmd_setup_00.png)

   Click for full image.
2. From the **Component** tab, click on **Add Component** and then input the word **Cube** into the search box clicking on the **Cube** mesh that is displayed to add it as a component

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/885e2921-e934-4092-a977-c93e04f0c9bf/vr_follow_hmd_setup_01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/885e2921-e934-4092-a977-c93e04f0c9bf/vr_follow_hmd_setup_01.png)

   Click for full image.
3. Select the Cube Static Mesh and drag it onto the Camera so that the Cmera is now the parent of the Cube Static Mesh.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e53d993f-1c46-43b0-884e-43742d72545c/vr_follow_hmd_setup_02.png)
4. Now compile your Blueprint and then launch your project using the VR preview option from inside the UE4 editor. When you put an HMD on then move your head around the Cube you attached will now accurately follow your head movements like in the video below.

## HMD and Player World Position

You can also quickly get the exact world location player and their HMD by getting the location of the Camera Component using the following Blueprint setup.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72573fce-2bd5-4386-9c86-594153a3cf36/vr_get_player_location_00.png)

In the above image whenever a user presses the T key on the keyboard the X, Y and Z position of the Camera in the world will then be output to the screen and log window.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac33432a-a57a-47d6-b4bc-73a350cf40ff/vr_follow_hmd_setup_03.png)

* [vr](https://dev.epicgames.com/community/search?query=vr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setting Up Objects To Follow The HMD](/documentation/en-us/unreal-engine/attaching-items-to-the-hmd-in-unreal-engine?application_version=5.7#settingupobjectstofollowthehmd)
* [HMD and Player World Position](/documentation/en-us/unreal-engine/attaching-items-to-the-hmd-in-unreal-engine?application_version=5.7#hmdandplayerworldposition)
