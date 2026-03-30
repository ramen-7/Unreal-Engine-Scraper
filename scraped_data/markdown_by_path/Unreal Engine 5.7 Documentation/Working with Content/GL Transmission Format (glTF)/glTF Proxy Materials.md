<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/gltf-proxy-materials-in-unreal-engine?application_version=5.7 -->

# glTF Proxy Materials

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [GL Transmission Format (glTF)](/documentation/en-us/unreal-engine/the-gl-transmission-format-gltf-in-unreal-engine "GL Transmission Format (glTF)")
7. glTF Proxy Materials

# glTF Proxy Materials

How to pre-bake complex materials into runtime-friendly proxies

![glTF Proxy Materials](https://dev.epicgames.com/community/api/documentation/image/c2cae64a-fb57-41d4-82bf-632e6a08bdd1?resizing_type=fill&width=1920&height=335)

 On this page

**glTF proxy Materials** are baked versions of the Materials in your Unreal Engine Levels. They are optimized for glTF export, and most commonly used to export Materials at runtime. Because Material baking, and other techniques the glTF exporter relies on, are not possible at runtime, proxy materials are the only way to export a Material properly.

glTF proxy Materials are also useful for:

* **Previewing**: When you generate a proxy Material, you see exactly what your Unreal Engine Material looks like when you export it to glTF.
* **Performance**: Using glTF proxy materials speeds up glTF exports because the exporter no longer needs to do any Material baking, which is the most time-consuming part of the export process.

Some Unreal Engine Materials use mesh-specific data such as world position, vertex colors, and so on. The glTF exporter can bake Unreal Engine Materials with mesh-specific data, but it cannot create proxy materials with mesh-specific data. If you need to create proxies for Materials that use mesh-specific data, you must create a proxy with each mesh individually.

## Create a glTF Proxy Material

When you create a glTF proxy Material from an Unreal Engine Material, the proxy appears in a `GLTF` subfolder of the folder that contains the source Material. It has the same name as the source Material, prefixed with `MI_GLTF`.

To create a glTF proxy Material, do the following:

1. In the **Content Browser**, right-click a Material.
2. From the right-click menu, select **Create GLTF Proxy Material**.

When you create a proxy material, the glTF exporter automatically creates a reference to it in the Unreal Engine Material's **Asset User Data** array.

To see or modify the reference, do the following:

1. In the **Content Browser**, select the Asset and edit it.
2. In the **Details** panel, expand the **Asset User Data** section.
3. Locate the **Asset User Data** row, and click **Add Element (+)**. A new **Index** row appears.
4. From the dropdown list in the new Index row, select **GLTF Material Export Options**.
5. Expand the **Index > General** section.
6. In the **Proxy** settings, you can see or modify the reference to the glTF proxy Material.

* [gltf](https://dev.epicgames.com/community/search?query=gltf)
* [gl transmission format](https://dev.epicgames.com/community/search?query=gl%20transmission%20format)
* [import / export](https://dev.epicgames.com/community/search?query=import%20%2F%20export)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create a glTF Proxy Material](/documentation/en-us/unreal-engine/gltf-proxy-materials-in-unreal-engine?application_version=5.7#createagltfproxymaterial)
