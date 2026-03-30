<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7 -->

# Recording a Live Session

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Chaos Visual Debugger](/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine "Chaos Visual Debugger")
8. [Capturing Data with Chaos Visual Debugger](/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger "Capturing Data with Chaos Visual Debugger")
9. Recording a Live Session

# Recording a Live Session

Record a live session with Chaos Visual Debugger

![Recording a Live Session](https://dev.epicgames.com/community/api/documentation/image/fc975a5f-77bd-4484-bb0b-d5f4ff1d224b?resizing_type=fill&width=1920&height=335)

 On this page

In this tutorial, you’ll learn how to record and play back an application in real time using **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**). Unlike [recording to file](https://dev.epicgames.com/documentation/en-us/unreal-engine/recording-to-file), recording a live session can be done **locally** (on your machine) or **remotely** (over a network). This is useful for live debugging on the fly but also saves the recording as a `.utrace` file for you to review and share later on.

[![Recording a Live Session](https://dev.epicgames.com/community/api/documentation/image/ae8844cb-a23d-480c-9cb5-8d6933123a5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae8844cb-a23d-480c-9cb5-8d6933123a5e?resizing_type=fit)

## Record Live Sessions

In this section you’ll learn how to record a PIE session using the Local Editor target preset, and the process to record all other target types.

### Local Editor

To record and play back a live PIE session on a local or a remote machine, follow these steps:

1. In CVD, toggle the data channels you want to record.

   [![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/d7f37ce6-fe06-4924-aacb-574b3b8917ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7f37ce6-fe06-4924-aacb-574b3b8917ac?resizing_type=fit)
2. In Unreal Editor, click the **Play** button in the main toolbar to begin a PIE session. You can start the PIE session before or after beginning a recording in CVD

   [![Play Button](https://dev.epicgames.com/community/api/documentation/image/47e06c72-8aec-4e57-891b-46dc007a8d12?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47e06c72-8aec-4e57-891b-46dc007a8d12?resizing_type=fit)
3. Since the Local Editor target is already selected by default, you can begin the recording by clicking **Record Live Session**. While recording, this button turns into a red recording icon.

   [![Record Live Session](https://dev.epicgames.com/community/api/documentation/image/0ea42f7e-95d0-41ab-a5d6-5c08bc12020c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ea42f7e-95d0-41ab-a5d6-5c08bc12020c?resizing_type=fit)
4. To stop recording, highlight the recording icon and click the red square icon. This process outputs a single `.utrace` file.

   [![Stop Recording](https://dev.epicgames.com/community/api/documentation/image/d48c70cd-0587-4d4c-9a8d-3c47edbeab78?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d48c70cd-0587-4d4c-9a8d-3c47edbeab78?resizing_type=fit)

   If you are currently recording, you can quit an existing PIE session and begin a new one — CVD automatically connects to it.

### All Other Targets

To record and playback a game client, server, or packaged build on a local or remote machine, follow these steps:

1. Verify that your target application or applications are running.
2. Toggle the data channels you want to record.

   [![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/6c39ebe0-b317-4bdd-9cb3-3acdcbf4fd58?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c39ebe0-b317-4bdd-9cb3-3acdcbf4fd58?resizing_type=fit)
3. To select a target to record, in CVD’s main toolbar, click the **Session Target** dropdown menu and choose your target.

   [![Session Target](https://dev.epicgames.com/community/api/documentation/image/38cc5554-1c75-47a9-b590-6a2960e1edcb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38cc5554-1c75-47a9-b590-6a2960e1edcb?resizing_type=fit)
4. To begin a recording, in CVD’s main toolbar, click **Record Live Session**. While recording, this button turns into a red recording icon.

   [![Record Live Session](https://dev.epicgames.com/community/api/documentation/image/f0edea29-2309-44de-8563-feddcd89175d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0edea29-2309-44de-8563-feddcd89175d?resizing_type=fit)
5. To stop recording, highlight the recording icon and click the red square icon. This process outputs one or more `.utrace` files.

   [![Stop Recording](https://dev.epicgames.com/community/api/documentation/image/96245b53-8d1a-4d82-9bba-627ab9f65758?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96245b53-8d1a-4d82-9bba-627ab9f65758?resizing_type=fit)

The game client and CVD compete for GPU resources. If the playback in CVD is struggling, you can limit the game client’s framerate or reduce the graphics quality.

## (Legacy) Record a Live Session with the Command Line Interface

We recommend using CVD’s UI to start and end recordings, however, you can use the command line to record PIE sessions, game clients and servers, and packaged builds. The session can be local (on the same workstation or even in the same PIE instance) or over the network.

### Enable a Data Channel

1. To modify data channels, open the command line in the target application. In a packaged build, press **Backtick** (`).
2. Enter the following console command, making sure to replace `[newstate]` with true or false and `[channelname]` with the desired data channel:

   `p.Chaos.VD.SetCVDDataChannelEnabled [newstate] [channelname]`

    For example:

   [![Recording Live (Console)](https://dev.epicgames.com/community/api/documentation/image/d3dd8bf8-4769-4ae8-acc8-7a521da337fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d3dd8bf8-4769-4ae8-acc8-7a521da337fc?resizing_type=fit)
3. Press **Enter** to execute the command.

### Enable Multiple Data Channels

You can enable or disable multiple channels by listing them, separated by commas. The following example enables the **PostIntegrate** and **Scene Queries** channels:

`p.Chaos.VD.SetCVDDataChannelEnabled true SceneQueries,PostIntegrate`

[![Recording Live Multiple Channels (Console)](https://dev.epicgames.com/community/api/documentation/image/ca30d14b-75c4-4112-aa9f-1765412a5e64?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca30d14b-75c4-4112-aa9f-1765412a5e64?resizing_type=fit)

### Enable Predefined Data Channels

If you want to launch a game client or server with a predefined set of enabled channels, add the following command line argument:

`CVDDataChannelsOverride=[ChannelName1,ChannelName2]`

The following example enables the Integrate and Scene Queries channels:

`CVDDataChannelsOverride=SceneQueries,PostIntegrate`

### Start a Recording Using the Command Line

1. To start a recording, open the command line.
2. If you are working on a local machine, type the following command and press **Enter** to execute it:

   `p.Chaos.StartVDRecording Server`

   [![Start Recording Server (Console)](https://dev.epicgames.com/community/api/documentation/image/b5c6027a-54dd-4282-8999-ad07469861cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5c6027a-54dd-4282-8999-ad07469861cc?resizing_type=fit)

   If you are working on a remote machine, type the following command and press **Enter** to execute it:

   `p.Chaos.StartVDRecording Server [YOURWORKSTATIONIP]`
3. In CVD’s main toolbar, click **Connect To Session**. In the **Live Session Browser**, next to **Selected Live Session**, select the available live session running on the local trace store.
4. (Optional) If you’re connecting to multiple targets, from the **Connection Mode** dropdown menu, select **Multi Source**.

   [![Multi Source Connection Mode](https://dev.epicgames.com/community/api/documentation/image/fc5ebfbc-59f0-4621-a850-b48061297719?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc5ebfbc-59f0-4621-a850-b48061297719?resizing_type=fit)
5. Click **Connect to Session** (in the **Live Session Browser** dialog). When the recording begins, the string **Chaos Visual Debugger recording in progress…** displays on screen.

   [![Recording String](https://dev.epicgames.com/community/api/documentation/image/97f55263-0aac-49c6-8130-a95cb7e9b689?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97f55263-0aac-49c6-8130-a95cb7e9b689?resizing_type=fit)
6. To stop a recording, open the command line. If you’re working on a local machine, type the following command and press **Enter**:

   `p.Chaos.StopVDRecording Server`

   [![Stop Recording Server (Console)](https://dev.epicgames.com/community/api/documentation/image/8c6a9ebb-0b1a-4be7-9eaa-86d6699c825b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c6a9ebb-0b1a-4be7-9eaa-86d6699c825b?resizing_type=fit)

   If you’re working on a remote machine, type:

   `p.Chaos.StopVDRecording Server [YOURWORKSTATIONIP]`

## Next Up

In the next tutorial, you’ll learn how to locate your `.utrace` files and play back your recordings.

* [![Playback in Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/118531b5-4316-4ac7-a933-abe744980883?resizing_type=fit&width=640&height=640)

  Playback in Chaos Visual Debugger

  Play back recordings in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/playback-in-chaos-visual-debugger)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Record Live Sessions](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#recordlivesessions)
* [Local Editor](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#localeditor)
* [All Other Targets](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#allothertargets)
* [(Legacy) Record a Live Session with the Command Line Interface](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#legacy-record-a-live-session-with-the-command-line-interface)
* [Enable a Data Channel](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#enableadatachannel)
* [Enable Multiple Data Channels](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#enablemultipledatachannels)
* [Enable Predefined Data Channels](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#enablepredefineddatachannels)
* [Start a Recording Using the Command Line](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#startarecordingusingthecommandline)
* [Next Up](/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger?application_version=5.7#nextup)
