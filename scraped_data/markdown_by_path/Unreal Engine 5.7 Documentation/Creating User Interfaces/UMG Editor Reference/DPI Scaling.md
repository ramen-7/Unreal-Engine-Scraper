<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dpi-scaling-in-unreal-engine?application_version=5.7 -->

# DPI Scaling

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
5. [Creating User Interfaces](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine "Creating User Interfaces")
6. [UMG Editor Reference](/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine "UMG Editor Reference")
7. DPI Scaling

# DPI Scaling

This page gives an overview on adjustment of DPI Scaling Rules.

![DPI Scaling](https://dev.epicgames.com/community/api/documentation/image/11d3f2df-a034-4413-b0d1-5b22669e3530?resizing_type=fill&width=1920&height=335)

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f231af35-0f22-4ce0-9ed2-23df8a273829/dpiscaling.png)

**UMG** supports automatic scaling for resolution-independent UI. There are default DPI scaling settings applied to every project. You can configure it by the **Project Settings** menu under the **User Interface** section. You can change **Application Scale** value via the input box, choose option of **DPI Scale Rule** and adjust **DPI Curve**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/059073e8-0158-4590-bd07-d3501f5706a5/projectsettings.png)

You can set the **DPI Scale Rule** to one of four options:

* **Shortest Side**: Evaluates the scale curve based on the shortest side of the viewport (Most Common Setting).
* **Longest Side**: Evaluates the scale curve based on the longest side of the viewport.
* **Horizontal**: Evaluates the scale curve based on the X axis of the viewport.
* **Vertical**: Evaluates the scale curve based on the Y axis of the viewport.

Right-click on the DPI Curve graph allows you to add points to the curve by selecting the **Add Key** option. After that you can set the resolution and its corresponding scale value via the input boxes. Also, you can supply an external **Float Curve** or create a Float Curve based on the currently applied settings by expanding the **DPI Curve** option.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87a3c79d-90c8-4389-87a9-51bc155cbb20/externalcurve.png)

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
