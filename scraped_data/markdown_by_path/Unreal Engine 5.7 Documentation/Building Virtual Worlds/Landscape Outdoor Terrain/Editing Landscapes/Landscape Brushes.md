<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7 -->

# Landscape Brushes

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
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. [Editing Landscapes](/documentation/en-us/unreal-engine/editing-landscapes-in-unreal-engine "Editing Landscapes")
8. Landscape Brushes

# Landscape Brushes

Guide to the brushes available for modifying Landscapes.

![Landscape Brushes](https://dev.epicgames.com/community/api/documentation/image/d66946b7-b2ed-469a-a15f-144e2cea3cfa?resizing_type=fill&width=1920&height=335)

 On this page

The **Landscape** tool's **Brush** defines the size and shape of the area of the Landscape that will be affected by either sculpting or painting. Brushes can have different shapes, sizes, and falloffs. Brushes should be a familiar concept to anyone who has experience using Photoshop or a similar image-editing application.

You can set the brush type and falloff in either the **Sculpt** or **Paint** tab of the Landscape toolbar. Settings can also be adjusted in the Landscape panel.

[![Brush Settings](https://dev.epicgames.com/community/api/documentation/image/97dda3d1-9067-474d-9a33-9d6d494ae8f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97dda3d1-9067-474d-9a33-9d6d494ae8f6?resizing_type=fit)

Brush Settings

| Property | Description |
| --- | --- |
| **Brush Size** | Determines the size of the brush in Unreal Units including the falloff. Within this area, the brush will have at least some effect. |
| **Brush Falloff** | Determines the percentage from the brush's extents where the falloff should begin. Essentially, this determines how hard the brush's edges are. A falloff of 0.0 means the brush will have full effect throughout with hard edges. A falloff of 1.0 means the brush will only have full effect at its center, and the effect will be reduced throughout its entire area to the edge. |
| **Use Clay Brush** | Clay Brush allows for an organic, additive approach to sculpting your Landscape. Similar to working with digital clay. If enabled, the editor uses a Clay Brush. |
| **Apply Without Moving** | When left-clicking, the brush continuously applies action regardless of cursor movement. Enables precise editing when mouse position needs to be stationary. |

The size and falloff of the current brush is displayed in the viewport as a pair of concentric circles.

|  |  |  |
| --- | --- | --- |
| [Falloff of 0.0](https://dev.epicgames.com/community/api/documentation/image/a671f99d-4356-4f26-be6b-828b65dd97e1?resizing_type=fit) | [Falloff of 0.5](https://dev.epicgames.com/community/api/documentation/image/e2ec9f46-22ce-4b3a-8e1f-520dacb2ce29?resizing_type=fit) | [Falloff of 1.0](https://dev.epicgames.com/community/api/documentation/image/c44ee409-d88e-4891-b78f-21e65aed01e0?resizing_type=fit) |
| Falloff: 0.0 | Falloff: 0.5 | Falloff: 1.0 |

## Circle

[![Circle Brush](https://dev.epicgames.com/community/api/documentation/image/ca1fcf0c-dbc2-48d3-9623-49e810bea9ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca1fcf0c-dbc2-48d3-9623-49e810bea9ba?resizing_type=fit)

The **Circle** brush applies the current tool in a circular area, with a falloff defined both numerically and by type.

[![Circle Brush in use](https://dev.epicgames.com/community/api/documentation/image/2765491e-35be-435f-9d84-4eaf4721130f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2765491e-35be-435f-9d84-4eaf4721130f?resizing_type=fit)

### Circle Brush Falloff Type

| Icon | Type | Description |
| --- | --- | --- |
| [Smooth Falloff](https://dev.epicgames.com/community/api/documentation/image/cf15b700-af90-4ebb-b076-faa64089ec39?resizing_type=fit) | **Smooth** | A linear falloff that has been smoothed to round off the sharp edges where the falloff begins and ends. |
| [Linear Falloff](https://dev.epicgames.com/community/api/documentation/image/8bdd095a-e8a5-494a-ba5f-f24bd44f460b?resizing_type=fit) | **Linear** | A sharp linear falloff, without rounded edges. |
| [Spherical Falloff](https://dev.epicgames.com/community/api/documentation/image/0deca5ff-e834-4d24-b951-9ad4b9e01fe9?resizing_type=fit) | **Sphere** | A half-ellipsoid-shaped falloff that begins smoothly and ends sharply. |
| [Tip Falloff](https://dev.epicgames.com/community/api/documentation/image/677ec770-f64c-4d3a-ac61-d1ab1c1a3ca8?resizing_type=fit) | **Tip** | A falloff with an abrupt start and a smooth ellipsoidal end. The opposite of the **Sphere** falloff. |

Below is an example of each of these falloff types when operating on the heightmap, with the same radius and falloff:

|  |  |  |  |
| --- | --- | --- | --- |
| [Smooth Falloff example](https://dev.epicgames.com/community/api/documentation/image/53d8fce4-3b66-48d4-84e1-5e4d205bb543?resizing_type=fit) | [Linear Falloff example](https://dev.epicgames.com/community/api/documentation/image/5309fee4-6066-4894-a4c9-c092de4762d8?resizing_type=fit) | [Spherical Falloff example](https://dev.epicgames.com/community/api/documentation/image/db2a6be4-a0cc-43d7-9148-90d01b7a4d94?resizing_type=fit) | [Tip Falloff example](https://dev.epicgames.com/community/api/documentation/image/017a4ed8-d453-4385-b2f8-5c068224acf9?resizing_type=fit) |
| **Smooth** | **Linear** | **Spherical** | **Tip** |

## Alpha

[![Alpha Brush](https://dev.epicgames.com/community/api/documentation/image/23aa6730-bebb-44dd-b9fe-989bccf03a84?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23aa6730-bebb-44dd-b9fe-989bccf03a84?resizing_type=fit)

The **Alpha** brush is similar to the Pattern brush, but instead of tiling the texture across the Landscape as you paint, it orients the brush texture in the direction of your painting and drags the shape as you move the cursor.

[![Dragging a Brush Alpha](https://dev.epicgames.com/community/api/documentation/image/2d04af58-8f19-4c6c-b37f-8c9712ee226e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d04af58-8f19-4c6c-b37f-8c9712ee226e?resizing_type=fit)

### Alpha Brush Settings

[![Alpha Brush Settings](https://dev.epicgames.com/community/api/documentation/image/ae1af14a-fd8a-4fa2-8f02-bab7b9f6f1ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae1af14a-fd8a-4fa2-8f02-bab7b9f6f1ca?resizing_type=fit)

Alpha Brush Settings.

| Setting | Description |
| --- | --- |
| **Texture** | Sets the Texture to be used, assigned from the **Content Browser**. |
| **Texture Channel** | Sets the Alpha brush's contents to the data from the corresponding channel of the texture that is currently assigned. |
| **Brush Size** | Sets the size of the brush. |
| **Use Clay Brush** | If selected, uses a clay brush. |
| **Auto-Rotate** | Rotates the brush to follow the mouse cursor. |
| **Texture Rotation** | Rotates the brush texture. When combined with Auto-Rotate, this sets the starting rotation of the texture. |

## Pattern

[![Pattern Brush](https://dev.epicgames.com/community/api/documentation/image/51f48464-499e-4f41-b445-44c6edaf8bd0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51f48464-499e-4f41-b445-44c6edaf8bd0?resizing_type=fit)

The **Pattern** brush allows you to use an arbitrary shape for the brush by sampling a single color channel from a texture to use as the alpha for the brush. The texture pattern is tiled as the brush is painted.

For example, the textures below could be used as the alpha:

|  |  |
| --- | --- |
| [Pattern-brush-of-black-dots-on-white-background](https://dev.epicgames.com/community/api/documentation/image/c793f9ad-b250-4129-85f9-c717389cbfeb?resizing_type=fit) | [Pattern-brush-checkerboard](https://dev.epicgames.com/community/api/documentation/image/afe5b8eb-e521-48b6-b25b-cfb09f46d46b?resizing_type=fit) |

Those would result in the following brushes:

| Brush Pattern | Pattern Result |
| --- | --- |
| [Pattern-brush-dot-template](https://dev.epicgames.com/community/api/documentation/image/1af5c7aa-e516-45f5-983e-8957a26a4d28?resizing_type=fit) | [Pattern-brush-template-result](https://dev.epicgames.com/community/api/documentation/image/3465ae04-7ccf-47f2-8987-c857cc580e80?resizing_type=fit) |
| [Pattern-brush-square-template](https://dev.epicgames.com/community/api/documentation/image/8997d913-444a-41d9-a40b-683097bc8e60?resizing_type=fit) | [Pattern-brush-square-result](https://dev.epicgames.com/community/api/documentation/image/4bf96c51-14f0-41a2-b795-92f9348e87e8?resizing_type=fit) |

### Pattern Brush Settings

[![Pattern Brush Settings](https://dev.epicgames.com/community/api/documentation/image/10e9198c-21c1-4f56-bb91-87e08d65c0e5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10e9198c-21c1-4f56-bb91-87e08d65c0e5?resizing_type=fit)

Pattern Brush Settings

| Setting | Description |
| --- | --- |
| **Texture** | Sets the Texture to be used, assigned from the **Content Browser**. |
| **Texture Channel** | Sets the Pattern brush's contents to the data from the corresponding channel of the texture that is currently assigned. |
| **Brush Size** | Sets the size of the brush. |
| **Brush Falloff** | Sets the brush falloff. |
| **Use Clay Brush** | Enables you to use a clay brush. |
| **Use World Space** | Tile the pattern in World-Space scale and position. |
| **Texture Scale** | Sets the size of the sampled texture in relation to the surface of the Landscape. |
| **Texture Rotation** | Sets the rotation of the sampled texture in relation to the surface of the Landscape. |
| **Texture Pan [U/V]** | Sets the offset of the sampled texture on the surface of the Landscape. |

## Component

[![Component Brush](https://dev.epicgames.com/community/api/documentation/image/43b3c67d-bb97-413e-96e9-00cf8425f420?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43b3c67d-bb97-413e-96e9-00cf8425f420?resizing_type=fit)

The **Component** brush is used for operating on individual components. The cursor becomes limited to a single component at a time:

[![Component Brush selection](https://dev.epicgames.com/community/api/documentation/image/0116514c-cdbe-4a39-a70f-db8fc9e4faab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0116514c-cdbe-4a39-a70f-db8fc9e4faab?resizing_type=fit)

The Component brush is the only brush available when you are using tools that operate on the individual component level.

### Component Brush Settings

| Setting | Description |
| --- | --- |
| **Brush Size** | The number of components in the XY axis that are affected. Size 1 means 1x1, 2 means 2x2, etc. |
| **Include Border** | When true, it affects all pixels of the component including its border. The border is shared by neighboring components and all components will be modified when enabled. |

## Gizmo

[![Gizmo Brush](https://dev.epicgames.com/community/api/documentation/image/fbb741bb-8a7a-45e0-bb05-3d8106eeadaa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fbb741bb-8a7a-45e0-bb05-3d8106eeadaa?resizing_type=fit)

The **Gizmo** brush is used for modifying your Landscape with **Landscape Gizmos**, which are tools that you use to perform actions to a specific localized area of the Landscape.

The Gizmo brush is available only when you are using the Copy/Paste tool in Sculpt mode.

For more information about Gizmos, see [Landscape Copy Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-copy-tool-in-unreal-engine).

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Circle](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#circle)
* [Circle Brush Falloff Type](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#circle-brush-falloff-type)
* [Alpha](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#alpha)
* [Alpha Brush Settings](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#alpha-brush-settings)
* [Pattern](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#pattern)
* [Pattern Brush Settings](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#pattern-brush-settings)
* [Component](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#component)
* [Component Brush Settings](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#componentbrushsettings)
* [Gizmo](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine?application_version=5.7#gizmo)
