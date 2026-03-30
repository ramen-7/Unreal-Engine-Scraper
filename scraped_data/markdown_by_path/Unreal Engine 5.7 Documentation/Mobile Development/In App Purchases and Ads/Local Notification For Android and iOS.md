<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/local-notifications-for-android-and-ios-in-unreal-engine?application_version=5.7 -->

# Local Notification For Android and iOS

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [In App Purchases and Ads](/documentation/en-us/unreal-engine/in-app-purchases-and-ads-in-unreal-engine-projects "In App Purchases and Ads")
7. Local Notification For Android and iOS

# Local Notification For Android and iOS

Product documentation including reference and guides for Unreal Engine 4

![Local Notification For Android and iOS](https://dev.epicgames.com/community/api/documentation/image/3436d321-5bc9-4030-afbb-5d0b5c9f7816?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

Local notifications are messages that can be displayed outside of your Unreal Engine 4 (UE4) application, alerting users to changes or updates that have been made.  In the following How-To we will take a look at how to set up local notifications that will work on both Android and iOS devices.

The current implementation of Local Notifications for both Android and iOS is very simplistic in its setup and execution. This system also will only work with local notifications and not notifications that are sent via a remote server.

Choose Your mobile platform

Android
iOS

## Steps

1. First, create a new Project from the **Games > Blank** template with the following options:

   * **Blueprint** enabled
   * **Mobile** / **Tablet** enabled
   * **Scalable 3D or 2D** enabled
   * **No Starter Content** enabled
2. Once the project has opened, open the **Level Blueprint** by clicking on the **Blueprints** button that is on **Main Toolbar** and then from the displayed list, select the **Open Level Blueprint** option.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e552dd7-ad79-4f62-b6aa-3465b78c9877/android-20oslocalnotification_openlevelblueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e552dd7-ad79-4f62-b6aa-3465b78c9877/android-20oslocalnotification_openlevelblueprint.png)

   Click for full image.

   To make this How-To easy to follow along with, we are using the Level Blueprint to set up and call the required Local Notifications Blueprint nodes. While setting up Local Notifications in the Level Blueprint will work, you should consider adding this logic where it makes the most sense for your project.
3. In the **Variables** section, create the following three **text variables** so that we can display messages to the user when the local notification is shown:

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27782059-9f42-4403-a32f-741a7391ff71/localnotifications_stingvariables.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27782059-9f42-4403-a32f-741a7391ff71/localnotifications_stingvariables.png)

   Click for full image.

   | Variable Name | Value |
   | --- | --- |
   | **Title** | Title: This is the Title! |
   | **Body** | Body: This is the body! |
   | **Action** | Action: I am taking this Action! |
4. To make sure that the user can see the local notifications when they are called to be displayed, add **Event Begin Play** and **Register for Remote Notifications** nodes to the **Event Graph**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1bce213-e7da-42c6-8eb7-0bad0c4c692d/localnotifications_beginplayregisterremotenot-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1bce213-e7da-42c6-8eb7-0bad0c4c692d/localnotifications_beginplayregisterremotenot-1.png)

   Click for full image.

   When adding this to your UE4 project, make sure that the Register for Remote Notifications node is called right when your project first loads. This way you will not have to worry about calling it again when trying to display notifications.
5. To make sure that users can see the notifications when they are fired off, you will need to connect the **output** of the **Event Begin Play** to the input on the **Register for Remote Notifications**. This will make sure that the user gives the operating system (OS) the permission to display the notifications.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9dcb74a-0ca5-45a5-af5c-bbb0f8ec20b9/localnotifications_connectbeginplayregisterremotenot.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9dcb74a-0ca5-45a5-af5c-bbb0f8ec20b9/localnotifications_connectbeginplayregisterremotenot.png)

   Click for full image.
6. Now that we have given the OS permission to display the notification, next we need to set up what will happen when the user clicks on the notification. To handle this type of interaction, add **Get Launch Notification**, **Print String** and **Branch** nodes to the **Event Graph**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/33d23a96-a5be-4cba-bb3d-7f9d08461149/localnotifications_laucnbrankprintnodes.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/33d23a96-a5be-4cba-bb3d-7f9d08461149/localnotifications_laucnbrankprintnodes.png)

   Click for full image.
7. Connect the Output of the **Get Launch Notification** node to the input on the **Branch** node and then connect the **True** output of the Branch node to the input on the **Print String** node.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a43eaa91-fe36-4be2-8c6a-ae312ae96d3b/localnotifications_connectgetlaunchtoprintandbranch-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a43eaa91-fe36-4be2-8c6a-ae312ae96d3b/localnotifications_connectgetlaunchtoprintandbranch-2.png)

   Click for full image.
8. Now, connect the **Notification Launched App** to the **Condition** input on the Branch node and the **Activation Event** to the **In String** on the **Print String** node.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d618d6e-0073-4b59-8ef5-dd95c4a6359c/localnotifications_connectlaunchtobranch.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d618d6e-0073-4b59-8ef5-dd95c4a6359c/localnotifications_connectlaunchtobranch.png)

   Click for full image.

   When adding this to your project you can omit the **Print String** node. This was added to make sure that the correct Activation Event was being used.
9. Now, we need to set up what the notification will say and how much time should pass before the notification is displayed. To accomplish this, you will first need to add the following Blueprint nodes to the Event Graph.

   * **Schedule Local Notifications from Now**
   * **Delay**
   * **Title, Body, and Action Text Variables**[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74784827-917c-46f4-bf5c-df01a4cc4ec6/20oslocalnotification_delayvarsschedule.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74784827-917c-46f4-bf5c-df01a4cc4ec6/20oslocalnotification_delayvarsschedule.png)

   Click for full image.
10. With the required nodes added to the Event Graph, connect the **Completed** output of the Delay node to the input on the **Schedule Local Notifications from Now**, and then connect each of the **Text** variables to their respective inputs on the **Schedule Local Notifications from Now** node. When completed, your Event Graph should match the image below.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e4a629c-9db4-468c-a801-e479b21711a5/localnotifications_delayvarsetup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e4a629c-9db4-468c-a801-e479b21711a5/localnotifications_delayvarsetup.png)

Click for full image.

1. Set the **Duration** on the Delay node to **five (5)** seconds. This will help make sure that there is enough time to either close the app or put the app in the background before the local notification is called and displayed.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/85cd5c52-a808-4df1-b67e-4270573e129a/localnotifications_delaynodesetup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/85cd5c52-a808-4df1-b67e-4270573e129a/localnotifications_delaynodesetup.png)

Click for full image.

The **Delay** node was only added to ensure that there would be enough time to close the app or send it to the background before the notification went off. When adding this to your project you do not have to use the **Delay** node.

1. Next, set the **Seconds from Now** input on the Schedule Local Notifications from Now node to **30** seconds. This will display the notification 30 seconds after this piece of code has been run.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ac1c722-e0fe-449b-a199-60447c1cdf19/localnotifications_setschedualetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ac1c722-e0fe-449b-a199-60447c1cdf19/localnotifications_setschedualetime.png)

Click for full image.

1. Set the **Activation Event** on the Schedule Local Notifications from Now to a value of **42**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b506e908-6261-4593-8eac-f376879c11a9/localnotifications_setactivationevent.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b506e908-6261-4593-8eac-f376879c11a9/localnotifications_setactivationevent.png)

Click for full image.

The Activation Event input enables you to associate a string value that can be used to call a specific notification. This allows you to set up and use different notifications that can be displayed when certain conditions are met.

1. With all of the needed nodes for Local Notifications to work now added to the Event graph, the last thing left to do is connect the **False** output of the **Branch** node to the input on the **Delay** node. When completed your Event Graph should look like the following image.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fa823a5-3f06-4a78-991d-ff810cd3fe71/localnotifications_connectfalsetodelay.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fa823a5-3f06-4a78-991d-ff810cd3fe71/localnotifications_connectfalsetodelay.png)

Click for full image.

1. Press the Compile button to compile the level Blueprint and the Save button to your level.
2. Finally, on the **Main Toolbar** click on the **Advanced Options** drop down next to the **Launch** icon and then select the device you want to test this on.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d115aed-9f44-44c6-a3f3-6a7800e2c416/localnotifications_launchonedevice.png "LocalNotifications_LaunchOneDevice.png")



Local Notifications for iOS projects are only available using source builds at present time.

1. First, download and compile a source code build of Unreal Engine. You can find instructions on how to download the source code from GitHub on the [UE4 On GitHub](https://www.unrealengine.com/en-US/ue4-on-github) page as well as the [Downloading Unreal Engine Source Code](/documentation/404) guide.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/219af3f3-47c5-409c-ad97-6fb4a5d62556/localnotifications_githubsourceios.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/219af3f3-47c5-409c-ad97-6fb4a5d62556/localnotifications_githubsourceios.png)

   Click for full image.
2. Once you have compiled the Editor, open it and create a new Project from the **Games > Blank** template with the following options:

   * **C++** enabled
   * **Mobile** / **Tablet** enabled
   * **Scalable 3D or 2D** enabled
   * **No Starter Content** enabled
3. When the project has opened, go to the **Edit**and then select **Project Settings**.
4. From the **Project Settings** menu, click on **All Settings** and then in the search box input **Enable Remote Notifications Support**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cd6e90f1-735a-4265-99f5-02df52f907bd/localnotification_enableremotenotios-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cd6e90f1-735a-4265-99f5-02df52f907bd/localnotification_enableremotenotios-1.png)

   Click for full image.

   Enable Remote Notifications Support is only available when using a C++ based project. If you are using a Blueprint based project, this option will be grayed out.
5. Once the project has opened, open the **Level Blueprint** by clicking on the **Blueprints** button that is on **Main Toolbar** and then from the displayed list, select the **Open Level Blueprint** option.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e2345592-beff-4eef-a5aa-0f41ee4009b3/android-20oslocalnotification_openlevelblueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e2345592-beff-4eef-a5aa-0f41ee4009b3/android-20oslocalnotification_openlevelblueprint.png)

   Click for full image.

   To make this How-To easy to follow along with, we are using the Level Blueprint to set up and call the required Local Notifications Blueprint nodes. While setting up Local Notifications in the Level Blueprint will work, you should consider adding this logic where it makes the most sense for your project.
6. In the **Variables** section, create the following three **text variables** so that we can display messages to the user when the local notification is shown:

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2228a87a-0ece-4b2e-8b57-bcad1d49d7ae/localnotifications_stingvariables.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2228a87a-0ece-4b2e-8b57-bcad1d49d7ae/localnotifications_stingvariables.png)

   Click for full image.

   | Variable Name | Value |
   | --- | --- |
   | **Title** | Title: This is the Title! |
   | **Body** | Body: This is the body! |
   | **Action** | Action: I am taking this Action! |
7. To make sure that the user can see the local notifications when they are called to be displayed, add **Event Begin Play** and **Register for Remote Notifications** nodes to the **Event Graph**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e14a222a-563d-43f9-86c2-a2079822f31f/localnotifications_beginplayregisterremotenot-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e14a222a-563d-43f9-86c2-a2079822f31f/localnotifications_beginplayregisterremotenot-1.png)

   Click for full image.

   When adding this to your UE4 project, make sure that the Register for Remote Notifications node is called right when your project first loads. This way you will not have to worry about calling it again when trying to display notifications.
8. To make sure that users can see the notifications when they are fired off, you will need to connect the **output** of the **Event Begin Play** to the input on the **Register for Remote Notifications**. This will make sure that the user gives the operating system (OS) the permission to display the notifications.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98ed9b98-db8f-442a-bb87-d9ef40469c77/localnotifications_connectbeginplayregisterremotenot.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98ed9b98-db8f-442a-bb87-d9ef40469c77/localnotifications_connectbeginplayregisterremotenot.png)

   Click for full image.
9. Now that we have given the OS permission to display the notification, next we need to set up what will happen when the user clicks on the notification. To handle this type of interaction, add **Get Launch Notification**, **Print String**, and **Branch** nodes to the **Event Graph**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8067fae1-ca2b-493e-a029-dd4e3d016dae/localnotifications_laucnbrankprintnodes.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8067fae1-ca2b-493e-a029-dd4e3d016dae/localnotifications_laucnbrankprintnodes.png)

   Click for full image.
10. Connect the Output of the **Get Launch Notification** node to the input on the **Branch** node and then connect the **True** output of the Branch node to the input on the **Print String** node.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/577cf65f-36b4-44a8-aff1-c4387e622cea/localnotifications_connectgetlaunchtoprintandbranch-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/577cf65f-36b4-44a8-aff1-c4387e622cea/localnotifications_connectgetlaunchtoprintandbranch-2.png)

Click for full image.

1. Now, connect the **Notification Launched App** to the **Condition** input on the Branch node and the **Activation Event** to the **In String** on the **Print String** node.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e5d4c30-3224-4526-80b8-7ace05ce43e6/localnotifications_connectlaunchtobranch.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e5d4c30-3224-4526-80b8-7ace05ce43e6/localnotifications_connectlaunchtobranch.png)

Click for full image.

When adding this to your project you can omit the **Print String** node. This was added to make sure that the correct Activation Event was being used.

1. Now, we need to set up what the notification will say and how much time should pass before the notification is displayed. To accomplish this, you will first need to add the following Blueprint nodes to the Event Graph.

***Schedule Local Notifications from Now*** **Delay**
\* **Title, Body, and Action Text Variables**

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cd1dd97f-33bd-4771-b332-ce78f5506502/20oslocalnotification_delayvarsschedule.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cd1dd97f-33bd-4771-b332-ce78f5506502/20oslocalnotification_delayvarsschedule.png)

Click for full image.

1. With the required nodes added to the Event Graph, connect the **Completed** output of the Delay node to the input on the **Schedule Local Notifications from Now**, and then connect each of the **Text** variables to their respective inputs on the **Schedule Local Notifications from Now** node. When completed, your Event Graph should match the image below.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d238a48-e90e-4bbc-991e-13a0f47d2259/localnotifications_delayvarsetup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d238a48-e90e-4bbc-991e-13a0f47d2259/localnotifications_delayvarsetup.png)

Click for full image.

1. Set the **Duration** on the Delay node to **five (5)** seconds. This will help make sure that there is enough time to either close the app or put the app in the background before the local notification is called and displayed.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47c0f195-f0fa-4881-a823-17e178138bcd/localnotifications_delaynodesetup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47c0f195-f0fa-4881-a823-17e178138bcd/localnotifications_delaynodesetup.png)

Click for full image.

The **Delay** node was only added to ensure that there would be enough time to close the app or send it to the background before the notification went off. When adding this to your project you do not have to use the **Delay** node.

1. Next, set the **Seconds from Now** input on the Schedule Local Notifications from Now node to **30** seconds. This will display the notification 30 seconds after this piece of code has been run.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bcc1532-5d1d-4e34-8f42-d65d8aa01598/localnotifications_setschedualetime.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bcc1532-5d1d-4e34-8f42-d65d8aa01598/localnotifications_setschedualetime.png)

Click for full image.

1. Set the **Activation Event** on the Schedule Local Notifications from Now to a value of **42**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd2c6a78-3285-44dc-859d-adb7791c00b3/localnotifications_setactivationevent.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd2c6a78-3285-44dc-859d-adb7791c00b3/localnotifications_setactivationevent.png)

Click for full image.

The Activation Event input enables you to associate a string value that can be used to call a specific notification. This allows you to set up and use different notifications that can be displayed when certain conditions are met.

1. With all of the needed nodes for Local Notifications to work now added to the Event graph, the last thing left to do is connect the **False** output of the **Branch** node to the input on the **Delay** node. When completed your Event Graph should look like the following image.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6a0a342-62b2-4bbe-b530-043a4b6b29d3/localnotifications_connectfalsetodelay.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6a0a342-62b2-4bbe-b530-043a4b6b29d3/localnotifications_connectfalsetodelay.png)

Click for full image.

1. Press the Compile button to compile the level Blueprint and the Save button to your level.
2. Finally, on the **Main Toolbar** click on the **Advanced Options** drop down next to the **Launch** icon and then select the device you want to test this on.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dcd63f26-4a44-4b92-9e78-4c0c3a0a7fe2/localnotifications_launchonios.png "LocalNotifications_LaunchOnIOS.png")

## End Result

Once the project has been deployed to your mobile device, you should hear and see a notification pop up five seconds after your app has been opened like in the video below.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [services](https://dev.epicgames.com/community/search?query=services)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/local-notifications-for-android-and-ios-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/local-notifications-for-android-and-ios-in-unreal-engine?application_version=5.7#endresult)
