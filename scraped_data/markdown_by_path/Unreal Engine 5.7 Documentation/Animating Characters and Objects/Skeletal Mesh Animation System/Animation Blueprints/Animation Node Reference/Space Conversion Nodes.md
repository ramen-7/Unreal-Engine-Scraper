<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-component-space-conversion-in-unreal-engine?application_version=5.7 -->

# Space Conversion Nodes

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine "Animation Blueprints")
8. [Animation Node Reference](/documentation/en-us/unreal-engine/animation-blueprint-nodes-in-unreal-engine "Animation Node Reference")
9. Space Conversion Nodes

# Space Conversion Nodes

Animation nodes that convert poses between local and component space.

![Space Conversion Nodes](https://dev.epicgames.com/community/api/documentation/image/8ffc5f24-996f-4787-8252-eafd31a02342?resizing_type=fill&width=1920&height=335)

Animation Blueprint nodes on the **AnimGraph** calculate and generate new poses that drive animations in either the **Local Space** or a **Component Space**. Animation poses generated in **Local space** calculate bone transforms relative to the bones **parent bone**. Animation poses generated in **Component Space** calculate bone transforms relative to the [Skeletal Mesh Component](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) of your character.

![space conversion nodes overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5272723f-6dff-4128-a342-cc744055c264/overview.png)

The **Convert Spaces** nodes available in the **AnimGraph** of Animation Blueprints provides the ability to convert poses between **local** and **component** space.

When working with poses in an Animation Blueprint, most nodes will operate within Local Space, indicated with **white** pose input and output pins. However, certain [blend nodes](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine) and all [skeletal controls nodes](/documentation/en-us/unreal-engine/animation-blueprint-skeletal-controls-in-unreal-engine), operate in **Component Space**, indicated with **blue** pose input and output.

To use nodes that operate within Component Space, poses must first be converted to Component Space using the Local to Component conversion node.

![local to component space conversion node animbp animgraph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cdb488c-5e68-4338-94af-14803e6662d9/localtocomponent.png)

After an animation pose has undergone component space operations, it must be converted back to local space in order to be usable by additional nodes, or provide a final pose for the output node.

![component to local space conversion node animbp animgraph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/319913e7-8bcb-4e4b-b4c5-7495910d9c16/componenttolocal.png)

Because there is a cost associated with each conversion **to** or **from** Component Space, it is best to group any nodes that operate in Component Space, to reduce the number of conversions needed.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [animation features](https://dev.epicgames.com/community/search?query=animation%20features)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

Related documents

[Blueprints Visual Scripting

![Blueprints Visual Scripting](https://dev.epicgames.com/community/api/documentation/image/4e3f56de-8371-4c9d-aa32-4bafe6592648?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)
