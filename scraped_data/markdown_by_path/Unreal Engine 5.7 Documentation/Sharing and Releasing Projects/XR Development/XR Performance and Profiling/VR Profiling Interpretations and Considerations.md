<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vr-profiler-interpretations-and-considerations-in-unreal-engine?application_version=5.7 -->

# VR Profiling Interpretations and Considerations

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
7. [XR Performance and Profiling](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine "XR Performance and Profiling")
8. VR Profiling Interpretations and Considerations

# VR Profiling Interpretations and Considerations

Things to keep in mind when interpreting the data from profiling tools.

![VR Profiling Interpretations and Considerations](https://dev.epicgames.com/community/api/documentation/image/067724f6-15af-49c4-b81e-4487bf98d951?resizing_type=fill&width=1920&height=335)

While [profiling tools](/documentation/en-us/unreal-engine/vr-profiling-tools-in-unreal-engine) can provide data about how your project is performing in VR, there are some points to consider when interpreting those values.

Delays can appear in odd places in the GPU and CPU profilers, most often as occlusion or scene graph traversal time. If those numbers are abnormally high, it's possible that it's a false positive.

Often when profiling, you'll notice that you pop between 90 Hz and 45 Hz. The difference is accounted for because the Compositor acts much like a vsync. If you miss framerate, it delays you until the next frame entirely. So, you tend to go down in brackets of 90 / n, where n is a whole number. Because the fps reporting is an average, it won't always report as a whole number, unless the drop is sustained. If you're bouncing back and forth between making framerate and not, you may see some fraction of a jump.

If you'd like to remove this for testing, sometimes it's useful to run the game emulating stereo rendering, instead of running in the device itself. To do so:

* Launch the game with `-game -emulatestereo -res=2160x1200` on the commandline
* Ensure vsync is off with `r.vsync 0` in the console
* Update the screen percentage to emulate the oversampling we have to do for VR with `r.screenpercentage 137` in the console

This will emulate the GPU and CPU performance characteristics without the annoyances of the variable framerate.

It's worth explicitly noting that if you're hitting 90 frames a second most of the time, and then make a change and notice a drastic drop, you're probably falling prey to the Compositor "vsync" issue noted above. As soon as
you tip over the cliff, you'll see drastic changes in numbers.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

Related documents

[VR Performance Testing

![VR Performance Testing](https://dev.epicgames.com/community/api/documentation/image/c68a897e-bf66-4786-8475-06f41fd48eb2?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/vr-performance-testing-in-unreal-engine)
