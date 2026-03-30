<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/troubleshooting-common-physics-asset-errors-in-unreal-engine?application_version=5.7 -->

# Troubleshooting Common Physics Asset Errors

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
7. [Physics Asset Editor](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine "Physics Asset Editor")
8. [Physics Asset Editor Tutorials](/documentation/en-us/unreal-engine/physics-asset-editor-tutorial-directory-for-unreal-engine "Physics Asset Editor Tutorials")
9. Troubleshooting Common Physics Asset Errors

# Troubleshooting Common Physics Asset Errors

This tutorial covers how to troubleshoot the two common Physics Asset issues of Exploding and Jittering.

![Troubleshooting Common Physics Asset Errors](https://dev.epicgames.com/community/api/documentation/image/abe51903-0726-4857-bab3-f567457c94ca?resizing_type=fill&width=1920&height=335)

 On this page

While there are several things that can be out of your control during a physical simulation, there are two issues that are definitely within your power to correct: **Exploding**
(interpenetrating physics bodies that are set to collide with each other) and **Jitter** (when the **Physics Bodies** refuse to sleep due to micro-movements). Below are some steps for correcting
these issues.

## Exploding

This is caused by two Physics Bodies interpenetrating and the physics system attempting to correct it by applying a massive amount of force to expel the Physics Bodies from each other.
If a **Physics Constraint** is keeping the offending Physics Bodies together, the physics system will continually apply force to separate them, causing very erratic and extreme movement.

![Exploding vehicle physics bodies](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66718f60-2b0a-464f-8761-06f0adf85a52/broken-physics-asset.png)

This is normally fixed by disabling collision between the two offending Physics Bodies, or changing their positions and/or scale to make sure they do not interpenetrate. Additionally, welded
Physics Bodies act as one regardless of interpenetration.

## Jitter

If your **Physics Asset** is mostly "collapsed" but still shaking and twitching on the ground, but not violently bouncing around, there are a few values you can tweak to get it to stop
and sleep.

Before doing anything, try simulating with **No Gravity**, this will show you if any of your Physics Constraints are misaligned, and tryi to correct them before the Physics Asset has
even hit the ground.

![No gravity simulation option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e447baa-231b-4ba0-bef1-26718b9daa2f/no-grav-simulation.png)

Often a small amount of **Linear** and **Angular Damping** on all the Physics Asset's Physics Bodies is more than enough to stop the asset from shaking. However, using large
values in Linear Damping will cause a Physics Body to slow its movement through the world, even due to gravity. Damping, as it is implemented here, is like the drag of moving through a viscous substance.

If jitter is still an issue, perhaps you have several really small Physics Bodies, check the [Substepping](/documentation/en-us/unreal-engine/physics-sub-stepping-in-unreal-engine) documentation for information on having the
physics simulation calculates in-between solutions.

See the [Constraints Reference](/documentation/en-us/unreal-engine/physics-constraint-reference-in-unreal-engine) for more details on the properties for Physics Constraints.

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [error](https://dev.epicgames.com/community/search?query=error)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Exploding](/documentation/en-us/unreal-engine/troubleshooting-common-physics-asset-errors-in-unreal-engine?application_version=5.7#exploding)
* [Jitter](/documentation/en-us/unreal-engine/troubleshooting-common-physics-asset-errors-in-unreal-engine?application_version=5.7#jitter)
