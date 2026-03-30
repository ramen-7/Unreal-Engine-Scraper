<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/editing-timelines-in-unreal-engine?application_version=5.7 -->

# Editing Timelines

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
8. Editing Timelines

# Editing Timelines

This document contains an overview of how to edit Timeline nodes in Blueprints.

![Editing Timelines](https://dev.epicgames.com/community/api/documentation/image/f44ee51f-53ea-4cce-bfe2-2156d20d5a5d?resizing_type=fill&width=1920&height=335)

 On this page

**Timelines** can be edited by **Double-clicking** on the Timeline node in the **Graph** tab or on the Timeline in the **My Blueprint** tab. This opens the **Timeline Editor** in a new tab.

## Timeline Editor

[![Blueprint Timeline Editor](https://dev.epicgames.com/community/api/documentation/image/6e44536d-af86-4aae-a863-afec370143db?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e44536d-af86-4aae-a863-afec370143db?resizing_type=fit)

| Button/Checkbox | Description |
| --- | --- |
|  | Adds a new float track to the Timeline, for animating scalar float values. |
|  | Adds a new vector track to the Timeline, for animating float vector values such as rotation or translation. |
|  | This adds an event track, which provides another execution output pin that will be triggered at keyframed times on the track. |
|  | Adds a new linear color track to the Timeline, for animating colors. |
|  | Add an external curve to the Timeline. This button is only active if an external curve is selected in the **Content Browser**. |
|  | Allows you to set the playback length for this Timeline. |
|  | If this is not active, the last keyframe of a sequence is ignored. This can help prevent skipping when an animation is looping. |
|  | If active, this Timeline node does not require an execution input to begin, and will start playing as soon as the level begins. |
|  | If active, the Timeline animation will repeat indefinitely unless stopped via the Stop input pin. |
|  | If active, the Timeline animation will be replicated across clients. |

## Adding Tracks

Timelines use **Tracks** to define the animation of a single piece of data. This can be a float value, vector value, color value, or events. Tracks can be added to the Timeline by clicking one of the **Add Track** buttons. For instance, click the button and enter a name for the new track.
Press **Enter** to save the name for your new float track.

[![Blueprint Timeline - Add Float Track](https://dev.epicgames.com/community/api/documentation/image/02c05d7d-44db-4251-9485-16e852833735?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/02c05d7d-44db-4251-9485-16e852833735?resizing_type=fit)

1. **Track Name** - You can enter a new name for the track into this field at any time.
2. **External Curve group** - Allows you to choose an external curve asset from the **Content Browser** instead of creating your own curve.
3. **Track timeline** - This is the keyframe graph for this track. You will place keyframes into this and see the resulting interpolation curve.

## Adding Keys

Once you have tracks in place, you can then start adding keys to define your animation.

For more information on working with keys and curves in Timelines, please see the [Keys and Curves page](https://dev.epicgames.com/documentation/en-us/unreal-engine/keys-and-curves-in-unreal-engine).

[![](https://dev.epicgames.com/community/api/documentation/image/5fb5d0f7-cb05-4521-b3e3-130c2d62bdb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fb5d0f7-cb05-4521-b3e3-130c2d62bdb3?resizing_type=fit)

Once you have finished editing your track, the data or event execution from the track is output through a data or execution pin with the same name as the track.

[![Blueprint Timelines - Track Data Output](https://dev.epicgames.com/community/api/documentation/image/9a0884b6-e598-411d-a20e-1044d0d76bc3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a0884b6-e598-411d-a20e-1044d0d76bc3?resizing_type=fit)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Timeline Editor](/documentation/en-us/unreal-engine/editing-timelines-in-unreal-engine?application_version=5.7#timeline-editor)
* [Adding Tracks](/documentation/en-us/unreal-engine/editing-timelines-in-unreal-engine?application_version=5.7#adding-tracks)
* [Adding Keys](/documentation/en-us/unreal-engine/editing-timelines-in-unreal-engine?application_version=5.7#adding-keys)
