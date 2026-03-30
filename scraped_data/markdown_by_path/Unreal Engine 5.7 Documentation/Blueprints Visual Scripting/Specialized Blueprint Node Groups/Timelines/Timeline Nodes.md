<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7 -->

# Timeline Nodes

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Specialized Blueprint Node Groups](/documentation/en-us/unreal-engine/specialized-blueprint-visual-scripting-node-groups-in-unreal-engine "Specialized Blueprint Node Groups")
7. [Timelines](/documentation/en-us/unreal-engine/timelines-in-unreal-engine "Timelines")
8. Timeline Nodes

# Timeline Nodes

Nodes that are used to handle specific functionality of Blueprint Timelines.

![Timeline Nodes](https://dev.epicgames.com/community/api/documentation/image/4e53b1d3-f3e8-4c9c-8140-b39aa3451205?resizing_type=fill&width=1920&height=335)

 On this page

## Get Play Rate

The **Get Play Rate** node returns the current playback rate of the input Timeline. The number is returned as a float value.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52c20cd3-ad66-4865-a4be-ae86d1243a9d/get_playrate.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **Outputs** |  |  |
| **Return Value** | Float | Outputs the current playback rate for the Timeline. |

## Get Playback Position

The **Get Playback Position** node returns the current playback position, or the current moment in time along the input Timeline. The number is returned as a float value.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a69859a1-3577-42bf-ab24-b29a397028e9/get_playback_position.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **Outputs** |  |  |
| **Return Value** | Float | Outputs the current playback position for the Timeline. |

## Get Timeline Length

The **Get Timeline Length** node returns the total length of the input Timeline as a float value.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84384299-a9e9-4cf4-828e-f09b45abf3c2/get_timeline_length.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **Outputs** |  |  |
| **Return Value** | Float | Outputs the total playback length for the Timeline. |

## Is Looping

The **Is Looping** node returns a boolean value which will be true if the input Timeline is looping, false if it is not.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e638a0c-6146-4216-84c0-9d9d4deb6f23/is_looping.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **Outputs** |  |  |
| **Return Value** | Boolean | Outputs the value of the Looping property. |

## Is Playing

The **Is Playing** node returns a boolean value which will be true if the input Timeline is currently playing, false if it is not.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0505f82-28d4-46f8-bbc6-c9f447bc8725/is_playing.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **Outputs** |  |  |
| **Return Value** | Boolean | Outputs whether the Timeline is currently playing. |

## Is Reversing

The **Is Reversing** node returns a boolean value which will be true if the input Timeline is currently reversing (or playing in reverse), false if it is not.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b98fc0b6-fc27-438c-99ba-93146c8c759a/is_reversing.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **Outputs** |  |  |
| **Return Value** | Boolean | Outputs whether the Timeline is currently reversing. |

## Play

The **Play** node tells the input Timeline to begin playing from the current playback position.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73f0146a-a722-49db-b190-608608a866f5/play01.png)

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |

## Play from Start

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd9d1a34-b5e8-4487-bc65-fb835f806206/play_from_start.png)

The **Play from Start** node tells the input Timeline to begin playing from the start of the Timeline.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |

## Reverse

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cde36b9a-0500-4662-b25d-3c5abc50407e/reverse01.png)

The **Reverse** node tells the input Timeline to begin reversing (playing in reverse) from the current playback position.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |

## Reverse from End

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3cc78793-369b-45a7-a51b-87c92832d083/reverse_from_end.png)

The **Reverse from End** node tells the input Timeline to begin reversing (playing in reverse) from the end of the Timeline.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |

## Set Looping

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfe78c41-8bf9-48d3-abab-44e9f7442e89/set_looping.png)

The **Set Looping** node takes in an input Timeline and a boolean value. It sets the Timeline's Looping property to the value of the boolean.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **New Looping** | Boolean | Used to set the Timeline's looping value. |

## Set New Time

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ded53eab-615d-46e4-a572-1270c9b2af60/set_new_time.png)

The **Set New Time** node takes in an input Timeline and a float value. It sets the Timeline's New Time property to the value of the float.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **New Time** | Float | Used to set a new playback position. |

## Set Play Rate

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5931a7c5-ea38-421d-ae4f-8cda2a1b50c3/set_play_rate.png)

The **Set Play Rate** node takes in an input Timeline and a float value. It sets the Timeline's Play Rate property to the value of the float.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **New Rate** | Float | Used to set a new playback rate. |

## Set Playback Position

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bcb18a62-3068-4578-b8b0-d3bdbe2084ec/set_playback_position.png)

The **Set Playback Position** node takes in an input Timeline, a float value, and a boolean. It jumps the Timeline's Playback Position property to the value of the float. If there are any event tracks within the Timeline, the value of the Boolean is used to determine if they will fire or not.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **New Position** | Float | Used to jump to a new playback position. |
| **Fire Events** | Boolean | Used to control whether any events (from any Event Tracks) that were jumped will be fired. |

## Set Timeline Length

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b7dc1e6c-5c2e-486f-babd-63cdceea6bf7/set_timeline_length.png)

The **Set Timeline Length** node sets the length of the Timeline's total playback.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **New Length** | Float | Used to set a new playback length. |

## Set Timeline Length Mode

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11bb4fef-ffd7-4f72-a18e-8beabc5ee897/set_timeline_lengthmode.png)

The **Set Timeline Length Mode** node sets the Length Mode property of the Timeline. This allows you to switch between playing the full Timeline length and just playing to the last keyframe.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |
| **New Length Mode** | Byte | Sets the playback mode to either "Timeline Length" or "Last Keyframe." |

## Stop

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36478795-9848-405f-afaf-f41c7b8a2461/stop01.png)

The **Stop** node stops playback for the input Timeline node.

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Inputs** |  |  |
| **Target** | Timeline Component | Takes in a Timeline variable. |

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Get Play Rate](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#getplayrate)
* [Get Playback Position](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#getplaybackposition)
* [Get Timeline Length](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#gettimelinelength)
* [Is Looping](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#islooping)
* [Is Playing](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#isplaying)
* [Is Reversing](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#isreversing)
* [Play](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#play)
* [Play from Start](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#playfromstart)
* [Reverse](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#reverse)
* [Reverse from End](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#reversefromend)
* [Set Looping](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#setlooping)
* [Set New Time](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#setnewtime)
* [Set Play Rate](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#setplayrate)
* [Set Playback Position](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#setplaybackposition)
* [Set Timeline Length](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#settimelinelength)
* [Set Timeline Length Mode](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#settimelinelengthmode)
* [Stop](/documentation/en-us/unreal-engine/timelines-nodes-in-unreal-engine?application_version=5.7#stop)
