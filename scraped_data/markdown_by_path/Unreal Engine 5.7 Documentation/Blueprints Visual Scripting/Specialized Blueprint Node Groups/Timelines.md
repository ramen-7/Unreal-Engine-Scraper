<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/timelines-in-unreal-engine?application_version=5.7 -->

# Timelines

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
7. Timelines

# Timelines

An Overview of Timelines in Unreal

![Timelines](https://dev.epicgames.com/community/api/documentation/image/8b8737f0-3cd8-467e-8fe9-3bd3c3a6eac2?resizing_type=fill&width=1920&height=335)

 On this page

Programming Language 

×C++

Select an option from the dropdown to see content relevant to it.

## Overview (C++)

**UTimelineComponent** holds a series of **events**, **floats**, **vectors** or **colors** with their associated **keyframes**. They are inherited from [UActorComponents](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Components/UActorComponent?application_version=5.5)

For further documentation, please see the overview about [Actor Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/components-in-unreal-engine)

Timelines allow for time-based animation which are played from Events that can be triggered at keyframes along the timeline. They can be used to handle simple, non-cinematic tasks such as opening doors, altering lights, or performing other time-centric manipulations to Actors within a scene. They are similar to [level sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) as they both provide values such as floats, vectors, and colors to be interpolated between keyframes along the timeline.

## Inputs and Outputs

UTimelineComponents have robust methods that can be extended in native code, refer to the [UTimelineComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Components/UTimelineComponent?application_version=5.5) API reference for further documentation. If you would like to see examples on how to utilize Timeline Components in the engine, see one of the Timeline Example links in the section below.

ExampleTimeline.h

C++

```
/** Start playback of timeline */
	UFUNCTION(BlueprintCallable, Category="Components|Timeline")
	ENGINE_API void Play();

	/** Start playback of timeline from the start */
	UFUNCTION(BlueprintCallable, Category="Components|Timeline")
	ENGINE_API void PlayFromStart();

	/** Start playback of timeline in reverse */
	UFUNCTION(BlueprintCallable, Category="Components|Timeline")
```

Expand code  Copy full snippet(37 lines long)

## Timeline Examples

* [![Keys and Curves](https://dev.epicgames.com/community/api/documentation/image/ee3c8bd8-6c0c-4e0d-b5fb-190c37db5d19?resizing_type=fit&width=640&height=640)

  Keys and Curves

  This document contains an overview of how to work with keys and curves within the Timeline editor in Blueprints.](https://dev.epicgames.com/documentation/en-us/unreal-engine/keys-and-curves-in-unreal-engine)
* [![Fading Lights](https://dev.epicgames.com/community/api/documentation/image/5260f5d3-3a8a-4031-ad44-1ce064019db2?resizing_type=fit&width=640&height=640)

  Fading Lights

  An example use of a timeline in which we set up a fading light that also changes color.](https://dev.epicgames.com/documentation/en-us/unreal-engine/fading-lights-in-unreal-engine)
* [![Opening Doors](https://dev.epicgames.com/community/api/documentation/image/9097abdf-dab7-43f7-b2db-647dc17f103f?resizing_type=fit&width=640&height=640)

  Opening Doors

  An example use of a timeline in which we set up a classic proximity-based opening door using Blueprints and C++.](https://dev.epicgames.com/documentation/en-us/unreal-engine/opening-doors-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview (C++)](/documentation/en-us/unreal-engine/timelines-in-unreal-engine?application_version=5.7#overview(c++))
* [Inputs and Outputs](/documentation/en-us/unreal-engine/timelines-in-unreal-engine?application_version=5.7#inputsandoutputs)
* [Timeline Examples](/documentation/en-us/unreal-engine/timelines-in-unreal-engine?application_version=5.7#timeline-examples)
