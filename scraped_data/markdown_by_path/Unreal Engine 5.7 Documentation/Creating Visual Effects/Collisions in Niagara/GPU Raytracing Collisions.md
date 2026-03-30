<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/gpu-raytracing-collisions-in-niagara-for-unreal-engine?application_version=5.7 -->

# GPU Raytracing Collisions

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Collisions in Niagara](/documentation/en-us/unreal-engine/collisions-in-niagara-for-unreal-engine "Collisions in Niagara")
7. GPU Raytracing Collisions

# GPU Raytracing Collisions

Learn how to enable GPU Raytracing Collisions in Niagara.

![GPU Raytracing Collisions](https://dev.epicgames.com/community/api/documentation/image/7c3daf87-1ce8-4c34-97c7-2e7bb54d9ade?resizing_type=fill&width=1920&height=335)

 On this page

In Unreal Engine, you can set up a particle system to collide with objects in the level using the **Collision** module.

In previous versions of Unreal Engine, when using a GPU emitter, you had several options in this module. Typically, most used the **Depth Buffer** option, which generates a simulation of the environment. This is a low-cost, but also low-accuracy solution. The shapes are not accurately portrayed, and if a particle goes off the screen it disappears immediately.

**GPU Raytracing Collisions** is an experimental option in the Collision module, so you can use hardware ray tracing on the GPU. No matter whether the emitter and its particles are on-screen or off, or hidden behind an object, the collision will use raytracing to calculate an accurate result.

![GPU Ray Tracing Collisions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6838caf7-4212-4d92-8bf8-bae1c7e6e39c/gpu-raytracing-collisions-final.gif)


The calculation is asynchronous, so the Niagara collision will be one frame behind.

### Adjust Your Project Settings

To use this feature, your project must be set to DirectX 12 and your GPU must have hardware ray tracing enabled. To turn on these options, follow these instructions:

* Open **Edit > Project Settings**.
* Search for **rhi**.
* Adjust the **Default RHI** option to **DirectX 12**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25ad6c0a-0fce-45bf-bedd-d28bbf7aca57/01-set-directx-12.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25ad6c0a-0fce-45bf-bedd-d28bbf7aca57/01-set-directx-12.png)

Click image for full size.

Next, enable ray tracing, also in your **Project Settings**.

* Search for **ray tracing**.
* Enable the options **Support Hardware Ray Tracing** and **Ray Traced Shadows**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61245416-d593-4eb2-9f50-3da9c3debaed/02-enable-raytracing.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61245416-d593-4eb2-9f50-3da9c3debaed/02-enable-raytracing.png)

Click image for full size.

### Set Up the Collision Module

In the **Collision** module, adjust the settings to use this experimental feature. Set the **GPU Collision Type** to **GPU Ray Traces (Experimental)**.

The **Trace Provider** is set to **Project Settings** by default, which picks the best from an array of options. However, you can also manually set this to **HW Ray Tracing**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49204f16-63cd-4ffd-b0b3-bd98d453fae8/03-collision-module-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49204f16-63cd-4ffd-b0b3-bd98d453fae8/03-collision-module-options.png)

### Set Up A Fallback (Optional)

You can set up a fallback in case ray tracing is not available. To do this, open **Edit > Project Settings**.

In the **Plugins > Niagara** section of the settings, there is a setting called **Async Gpu Trace DI**. It has an array set up with two options in it, **HW Ray Tracing** and **Global Signed Distance Fields**. When your options are set up like this, the system will first try to use ray tracing, but if ray tracing is not available then it will fall back to use distance fields instead. These are the default settings.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a0c1712-99c6-4a46-93ee-0826559c25c1/04-fallback-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a0c1712-99c6-4a46-93ee-0826559c25c1/04-fallback-options.png)

You can add elements to the array or rearrange as needed. However, in most cases, the default settings will be sufficient.

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adjust Your Project Settings](/documentation/en-us/unreal-engine/gpu-raytracing-collisions-in-niagara-for-unreal-engine?application_version=5.7#adjustyourprojectsettings)
* [Set Up the Collision Module](/documentation/en-us/unreal-engine/gpu-raytracing-collisions-in-niagara-for-unreal-engine?application_version=5.7#setupthecollisionmodule)
* [Set Up A Fallback (Optional)](/documentation/en-us/unreal-engine/gpu-raytracing-collisions-in-niagara-for-unreal-engine?application_version=5.7#setupafallback(optional))
