<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-mesh-auto-instancing-on-mobile-devices-in-unreal-engine?application_version=5.7 -->

# Mesh Auto-Instancing on Mobile

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
6. [Debugging and Optimization for Mobile](/documentation/en-us/unreal-engine/debugging-and-optimization-for-mobile-in-unreal-engine "Debugging and Optimization for Mobile")
7. Mesh Auto-Instancing on Mobile

# Mesh Auto-Instancing on Mobile

How to enable mesh auto-instancing on mobile.

![Mesh Auto-Instancing on Mobile](https://dev.epicgames.com/community/api/documentation/image/0818da78-bdd7-42da-8d8e-9316799a26f9?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The Unreal Engine [**Mesh Drawing Pipeline**](/documentation/en-us/unreal-engine/mesh-drawing-pipeline-in-unreal-engine) implements a mesh auto-instancing feature that merges draw calls, which can greatly improve graphics performance. This functionality is now available for mobile devices with some additional settings configuration.

## Steps

1. Locate the **Config** folder for your project and open **DefaultEngine.ini.**
2. Add the following lines:

   ```
   |  |  |
   | --- | --- |
   |  | r.Mobile.SupportGPUScene=1 |
   |  | r.Mobile.UseGPUSceneTexture=1 |
   |  |  |

   Copy full snippet
   ```

   Save your changes and close the file.

Enabling this feature will cause shaders to be rebuilt for mobile platforms. If you have Unreal Editor set to Android Preview mode, the editor will recompile shaders accordingly. Large projects may have a long iteration time.

## Result

By enabling the above settings for your project, auto-instancing will be enabled for all devices. `r.Mobile.SupportGPUScene` enables auto-instancing on mobile devices. However, they will use the same buffer as a desktop build. Mali devices only support buffers of up to 64 kb and are unable to support this feature normally. `r.Mobile.UseGPUSceneTexture` will make the auto-instancing process use a texture instead of a buffer to store the required information, enabling Mali devices to use auto-instancing as well.

## Limitations

In addition to the limitations mentioned for draw call merging on the [Mesh-Drawing Pipeline](/documentation/en-us/unreal-engine/mesh-drawing-pipeline-in-unreal-engine) page, there are some limitations to auto-instancing that are specific to mobile devices:

* Auto-instancing on mobile mainly benefits projects that are heavily CPU-bound rather than GPU-bound. While it is unlikely that enabling auto-instancing will harm a GPU-bound project, you are less likely to see significant performance improvements from using it.
* If a game is heavily memory-bound, it may be more beneficial to turn off `r.Mobile.UseGPUSceneTexture` and use the buffer instead, with the understanding that it will not work on Mali devices.

The effectiveness of auto-instancing is highly dependent on the exact specifications of your project. Therefore, we recommend that you create a build with auto-instancing enabled and profile it in order to determine whether you will see substantial performance gains. For more information about profiling, refer to the [Performance and Profiling](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content) section.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [graphics](https://dev.epicgames.com/community/search?query=graphics)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [mesh](https://dev.epicgames.com/community/search?query=mesh)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-mesh-auto-instancing-on-mobile-devices-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/using-mesh-auto-instancing-on-mobile-devices-in-unreal-engine?application_version=5.7#result)
* [Limitations](/documentation/en-us/unreal-engine/using-mesh-auto-instancing-on-mobile-devices-in-unreal-engine?application_version=5.7#limitations)

Related documents

[Testing and Optimizing Your Content

![Testing and Optimizing Your Content](https://dev.epicgames.com/community/api/documentation/image/f42a8173-428b-43f8-b672-fb940fd81e79?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content)
