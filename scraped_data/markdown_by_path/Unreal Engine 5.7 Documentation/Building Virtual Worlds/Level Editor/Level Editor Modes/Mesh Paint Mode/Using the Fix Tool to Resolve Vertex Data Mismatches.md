<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vertex-color-matching-in-unreal-engine?application_version=5.7 -->

# Using the Fix Tool to Resolve Vertex Data Mismatches

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Level Editor](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine "Level Editor")
7. [Level Editor Modes](/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine "Level Editor Modes")
8. [Mesh Paint Mode](/documentation/en-us/unreal-engine/mesh-paint-mode-in-unreal-engine "Mesh Paint Mode")
9. Using the Fix Tool to Resolve Vertex Data Mismatches

# Using the Fix Tool to Resolve Vertex Data Mismatches

A tool which allows vertex colors to be repaired when a new version of a mesh is imported with a different vertex count.

When you’re working with meshes, you might sometimes update the mesh outside of the editor. This can include changing the topology of a mesh that either adds or removes vertices from it. If you’ve already spent time painting vertex colors or vertex weights to your mesh, this can lead to errors with the vertex color data when you import the mesh again after changing it. Map check errors like this one could appear:

StaticMeshActor\_73 (LOD 0) has hand-painted vertex colors that no longer match the original StaticMesh

The Mesh Paint mode’s **Fix** tool can resolve these types of errors where the vertex colors are mismatched against the original mesh’s vertices, which can make them look incorrect.

The **Fix** tool is available when using **Vertex Color**, **Vertex Weights**, and **Texture Color** painting methods.

![Mesh Paint Vertex Color Fix tool.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/384b53e6-991e-449f-bcc8-7be6a7cb7e9d/fix-tool.png)


The Fix tool is only available when there is an issue with the painted vertex data that needs to be resolved with the mesh. By default, this tool is disabled and grayed out.

This tool is designed to always match some color, even if the changes are significant. The tool is effective for fixing smaller changes to a mesh. However, substantial changes can be more challenging to fix, since there they increase the likelihood of colors not matching.

The examples below show vertex color painted on the mesh with its wireframe and the RGB vertex painted visualization for comparison. This is the original mesh with vertex colors (left) before being reimported with a lower vertex count after having the Fix tool apply fixups to the vertex colors (right).

|  |  |
| --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ef8ca45-82cd-416a-8cf3-bc3f0496212f/fix-tool-high.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b45c74d0-fd46-484a-a866-b50ff170278b/fix-tool-low.png) |
| Original vertex color painted mesh with high vertex count. | Reimported vertex color painted mesh with lower vertex count with fix up applied. |

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [mesh paint tool](https://dev.epicgames.com/community/search?query=mesh%20paint%20tool)
* [vertex color](https://dev.epicgames.com/community/search?query=vertex%20color)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
