<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7 -->

# Broadcast Hype Chamber Sample

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
7. Broadcast Hype Chamber Sample

# Broadcast Hype Chamber Sample

Learn how to take 3D motion design to the next level with Unreal Engine's Broadcast Hype Chamber Sample.

![Broadcast Hype Chamber Sample](https://dev.epicgames.com/community/api/documentation/image/69a2392d-6405-4805-96fe-27cee0cd0e0c?resizing_type=fill&width=1920&height=335)

 On this page

Real-time technology is becoming an increasingly important part of motion graphics and sports. Epic Games partnered with Capacity Studios to deliver a high-quality Broadcast Hype Chamber sample which demonstrates how to design, develop, and play out numerous animation elements for your esports show.

Enter the Hype Chamber and learn how to drive a sports motion graphics package with advanced blueprinting and data table workflows.

By exploring this sample and this page, you'll learn about:

* How to use motion graphics animation for live playout or pre-rendered animation. This sample includes 10 motion graphics examples.
* How to build a highly customizable graphic package where artists can switch 3D models, textures, materials, and lighting, all driven by a single blueprint controller. When you change team names, all the elements in the scene will swap accordingly.
* How to extend the workflow by adding a new team to the data table.

## Getting Started

To create a project with the Broadcast Hype Chamber sample, follow these steps:

1. Access the [Broadcast Hype Chamber sample](https://fab.com/s/0d3553fc0080) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher**, go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you install the compatible engine version.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Playing Graphics and Animation

In the Unreal Editor's **Toolbar**, click **Play** to run the level.

In the **World Outliner**, select **BP\_HypeChamber\_Controller** to open its **Details** panel. These are options that you can change during **Play in Editor** mode.

### Hypechamber Control

[![Hype Chamber controls](https://dev.epicgames.com/community/api/documentation/image/58580ccd-cd1c-4a7a-b73e-ece36b7ad747?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58580ccd-cd1c-4a7a-b73e-ece36b7ad747?resizing_type=fit)

Click **Play Graphic** to play the 3D graphics and animation.

[![Playing graphic in the Hype Chamber](https://dev.epicgames.com/community/api/documentation/image/4fdfc621-c2c7-4923-853a-1dcc8d88bdc7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fdfc621-c2c7-4923-853a-1dcc8d88bdc7?resizing_type=fit)

Click **Reset Graphic** to reset everything to its initial state.

[![Reseting graphic in the Hype Chamber](https://dev.epicgames.com/community/api/documentation/image/184c33bd-927e-498f-a453-a0c1240bb26f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/184c33bd-927e-498f-a453-a0c1240bb26f?resizing_type=fit)

Change **Team ASelect** to change the team that appears in the Level. For graphics or modes with two teams, TeamASelect appears on the left side, and **Team BSelect** appears on the right side.

[![Selecting team in the Hype Chamber](https://dev.epicgames.com/community/api/documentation/image/5d050367-7b18-4b11-b485-30de262af657?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d050367-7b18-4b11-b485-30de262af657?resizing_type=fit)

**Mode Select** changes what displays in the Level. A different motion graphic and animation is associated with each mode. You have the following options:

* INT Matchup
* INT Matchup Infinite
* INT Team Hype Chamber
* INT Player Name
* INT Text
* INT\_Logo
* FS Open
* FS Team Hype Chamber Wide
* FS Team Hype Chamber Close
* FS Backgrounds
* BUMP Team Victory

### Hypechamber Advanced

The Hype Chamber Controller has the following settings for customizing media output and post processing when playing the motion graphics and animations.

[![Advnaced controls for the Hype Chamber](https://dev.epicgames.com/community/api/documentation/image/d6557ba8-91f0-4934-a9b8-1d6d0a7897b1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6557ba8-91f0-4934-a9b8-1d6d0a7897b1?resizing_type=fit)

| Parameter | Description |
| --- | --- |
| Disable SDI | Disable active media capture output. |
| Enable SDI | Enable media capture output based on Media Output Generic. |
| Update Advanced | Update quality and ray tracing settings to values set by the Hype Chamber Controller. |
| Update Logos | Update background logos and colors featured in screenwalls. |
| Use Mode Select | When enabled, you can control which scene is used with the Hype Chamber Controller. You'll need to disable this before using Movie Render Queue. |
| Screen Mode | The type of content to fill the Hype Chamber Screens. Defaults to a render target of a motion graphics scene. |
| Master Post Process | A reference to the scene post processing volume with the highest priority. |
| Media Output Generic | Defines the media capture output of content. Defaults to use a Blackmagic SDI configuration. |
| Resolution | The output resolution size for the media capture. |
| Quality | The `sg.resolution` quality command input. |
| Max Roughness | Maximum roughness amount of the Post Process volume ray tracing. |
| Max Bounces | The maximum number of bounces of the Post Process volume ray tracing. |
| Samples Per Pixel | Number of samples per pixel of the Post Process volume ray tracing. |

### Using Remote Control to Play Graphics and Animations

In **EsportsSample/\_ArtistElements/Blueprints**, double-click the **RC\_Esports** Remote Control Preset to open it in the Remote Control Panel. The parameters in the BP\_Esports\_Controller's Details panel are the same parameters exposed in the RC\_Esports preset.

[![Hype Chamber Remote Control Preset](https://dev.epicgames.com/community/api/documentation/image/fb78ad9c-0f06-47c7-a2db-fba62e287461?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb78ad9c-0f06-47c7-a2db-fba62e287461?resizing_type=fit)

Launch the Remote Control Web Application to control the team graphics and text remotely by entering the URL **127.0.0.1:7000** on your local machine, or your computer's IP address with port 7000 on a second device. Refer to [Remote Control Web Application](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-web-application-for-unreal-engine) for more information about using the web application.

[![Hype Chamber Remote Control Web Application](https://dev.epicgames.com/community/api/documentation/image/06b7d0b8-f0b5-461a-b904-ef921c2a88d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06b7d0b8-f0b5-461a-b904-ef921c2a88d5?resizing_type=fit)

## Editing Team Themes

To edit the current team themes, in the **Content Browser**, navigate to **EsportsSample/\_ArtistElements/Blueprints/Data** and double-click **DT\_Esport\_Themes** to open it in the Data Table Asset Editor.

Each row is all the data for one team, from the team name to the team's color palette. Click a row and edit its data in the **Row Editor** to make changes to the team's theme.

[![Hype Chamber Team Data Table](https://dev.epicgames.com/community/api/documentation/image/03cac7e2-a8c3-4f32-904e-19bc08fbd7fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03cac7e2-a8c3-4f32-904e-19bc08fbd7fe?resizing_type=fit)

To change what parameters define a team's theme, navigate to **EsportsSample/\_ArtistElements/Blueprints/Structures** and double-click **ST\_RL\_Design** to open it in the Structure Asset Editor.

[![Hype Chamber Team Structure Asset](https://dev.epicgames.com/community/api/documentation/image/5a48a874-39fd-41b4-ba12-904f893d04bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5a48a874-39fd-41b4-ba12-904f893d04bf?resizing_type=fit)

In **Esports/\_ArtistElements/Blueprints**, double-click **BP\_Esport\_Controller** to open it in the Blueprint Editor. In the **UpdateData** section, the **DT\_Esport\_Themes** data table is looked up by row name to populate the team data in the Level. When you add parameters, make sure they're connected to Assets defined in the **TeamAValues** and **TeamBValues** nodes.

[![Hype Chamber Controller Data Table Assignment Blueprint](https://dev.epicgames.com/community/api/documentation/image/841abd97-9661-4b1a-bc21-124502906817?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/841abd97-9661-4b1a-bc21-124502906817?resizing_type=fit)

Click image for full size.

## Creating Your Own Team

Follow these steps to add a new team to the selection.

1. In the Content Browser, navigate to **EsportsSample/\_ArtistElements/Blueprints/Enums** and double-click **EN\_Teams** to open it in the Enum Asset Editor.

   [![Hype Chamber Team Enum](https://dev.epicgames.com/community/api/documentation/image/2c75aef7-d442-45cf-adf6-38c9ed5a0d76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c75aef7-d442-45cf-adf6-38c9ed5a0d76?resizing_type=fit)
2. Click **New** to add an entry to the Enum.
3. Set the new entry's **Display Name** to the abbreviated name of the team and **Description** to the full name of the team. In this example, the new team's Display Name is **WIP** and its Description is **Work in Progress**.
4. Navigate to **EsportsSample/\_ArtistElements/Blueprints/Data** and click **(+) Add** to add a new row.
5. Set the new row's name to the abbreviated name of the team and Team Name to the full name of the team. In this example, the row's name is **WIP** and the Team Name is **Work in Progress**.

   [![Hype Chamber Team Data Table New Entry](https://dev.epicgames.com/community/api/documentation/image/e8625c2c-572b-4f62-ba2a-b3b418eb37cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8625c2c-572b-4f62-ba2a-b3b418eb37cf?resizing_type=fit)
6. You can now change the Hypechamber Controls in the Level's BP\_HypeChamber\_Controller to select your new team.

## Batch Rendering with Movie Render Queue

In the Content Browser, navigate to **EsportsSample/\_ArtistElements/Blueprints**. Right-click the **EUW\_VersioningUtility** [Editor Utility Widget](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-widgets-in-unreal-engine) Asset and choose **Run Editor Utility Widget**.

The Editor Utility Widget opens in a new window.

[![Hype Chamber Editor Utility Widget](https://dev.epicgames.com/community/api/documentation/image/f0e42b47-77ab-4bcb-8575-1dbd3fc07660?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0e42b47-77ab-4bcb-8575-1dbd3fc07660?resizing_type=fit)

This widget provides controls for batch rendering sequences with various configurations of teams using [Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue). The following parameters affect the rendering job.

| Parameter | Description |
| --- | --- |
| Mode Select | Select which graphic animation should be configured and played when rendering. |
| Target Sequence | The Level Sequence targeted by Mode Select. Can be opened while in the editor to preview graphics. |
| Team AList | The list of teams to be rendered out with the selected graphic. In graphics or modes with two teams, this controls the team featured on the left. |
| Team BList | The secondary list of teams to be rendered out with the selected graphic. In graphics or modes with two teams, this controls the team featured on the right. |
| Text Ver | Selects which version of the text mode animations is used in the renders. The input text defaults to what is currently set as the Text Line 1 and Text Line 2 inputs. |
| Background Ver | Selects which version of the background mode animations is in the renders. |
| Hype Chamber Con | A debug reference to the BP\_Hypechamber\_Controller in the scene. |
| Render Preset | The Movie Render Queue Render Preset Asset to render jobs. |
| Output Folder | The output directory of the rendered Assets. |
| Pipeline Executor Job | A debug view to show that a valid executor job is showing. |
| Next Render Executor | A debug view to show the next executor job. |
| Queue Index | A debug status of which job is currently being rendered from the Team A and Team B list |
| Job Count | The total count of jobs listed to be rendered. This is based on the number of teams featured in the Team A List. |

Click **(+) Start Render** to start the render jobs.

[![Hype Chamber Batch Render](https://dev.epicgames.com/community/api/documentation/image/2d0f7755-029e-4096-a943-a1da4176d205?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d0f7755-029e-4096-a943-a1da4176d205?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#getting-started)
* [Playing Graphics and Animation](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#playing-graphics-and-animation)
* [Hypechamber Control](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#hypechamber-control)
* [Hypechamber Advanced](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#hypechamber-advanced)
* [Using Remote Control to Play Graphics and Animations](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#using-remote-control-to-play-graphics-and-animations)
* [Editing Team Themes](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#editing-team-themes)
* [Creating Your Own Team](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#creating-your-own-team)
* [Batch Rendering with Movie Render Queue](/documentation/en-us/unreal-engine/broadcast-esports-hype-chamber-sample-with-motion-graphics-in-unreal-engine?application_version=5.7#batch-rendering-with-movie-render-queue)
