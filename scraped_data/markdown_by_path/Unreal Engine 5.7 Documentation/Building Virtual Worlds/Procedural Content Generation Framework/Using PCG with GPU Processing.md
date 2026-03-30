<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7 -->

# Using PCG with GPU Processing

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
6. [Procedural Content Generation Framework](/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine "Procedural Content Generation Framework")
7. Using PCG with GPU Processing

# Using PCG with GPU Processing

An introduction to Procedural Content Generation using GPU Execution and how to use it with your PCG workflow.

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Procedural Content Generation Framework (PCG)** is a toolset for creating your own procedural content and tools inside Unreal Engine. **PCG GPU Processing** provides technical artists and designers with the ability to send many PCG processing tasks directly to the GPU to free up resources on the CPU.

PCG GPU processing is efficient for a variety of tasks, such as point processing, [Runtime Generation](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine#using-runtime-generation), and [static mesh spawning](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.5#spawner).

GPU processing is currently available on a [small number of nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine#supported-nodes),
including the Copy Points and Static Mesh Spawner, as well as a new
Custom HLSL node has been added which can be scripted using the [HLSL language](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl). Additional nodes that support GPU Execution will be available in the future.

Nodes that are set to target the GPU are labeled with **GPU** in the PCG Graph. A subset of connected GPU nodes executes together on the GPU efficiently and is called a **Compute Graph**.

[![PCG GPU Compute Graph example](https://dev.epicgames.com/community/api/documentation/image/e1ade4e3-9f89-455e-b145-ca428efbb918?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1ade4e3-9f89-455e-b145-ca428efbb918?resizing_type=fit)

|  |  |
| --- | --- |
| Number | Description |
| 1 | Transferring data between the CPU and GPU. These points represent a performance cost. |
| 2 | GPU execution nodes that are executed together. |

Targeting the GPU may give performance increases over CPU execution when there are enough points in the data to fully utilize the GPU hardware. Additionally, a sequence of connected GPU nodes with a GPU-enabled Static Mesh Spawner node provides a fast path for [static mesh spawning](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine?application_version=5.5#spawner).

It is important to note that there is a CPU cost for transferring data between the CPU and GPU, and for preparing a compute graph for execution. Therefore the optimal way to use the GPU execution feature is to group GPU-enabled nodes together, and minimize how much data is transferred into and out of each compute graph.

## Authoring High Performance Graphs

The following guidelines are recommended for authoring efficient runtime PCG graphs.

* Use Hierarchical Generation to run nodes on large grids or the Unbounded grid level to factor out shared work and minimize the amount of work done on smaller grids.
* Prefer GPU nodes which are dispatched as compute shaders and execute efficiently on GPU hardware.
* Minimize data transfers between CPU and GPU which are computationally costly. Uploads of data from CPU to GPU are indicated via small yellow up arrow badges on nodes, and downloads of data from GPU back to CPU are indicated via small yellow down arrow badges.

## Supported Nodes

### Custom HLSL Node

The Custom HLSL node can be used for arbitrary data processing tasks to be scripted via user created HLSL source code. The source code is injected into a compute shader and executed over data elements in parallel on GPU hardware.

This node provides low level access to GPU hardware and is available for advanced users.

|  |  |
| --- | --- |
| **Option** | **Description** |
| **Kernel Type** | Selects a preset for the behavior of the node. The available options are documented in the [Custom HLSL Node Kernel Types](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine#custom-hlsl-node-kernel-types) section below. |
| **Input Pins** | Defines the data that is taken as input. Opening the rollout provides the following options:   * **Label**: Name displayed on the input pin. * **Usage**: Not relevant for the Custom HLSL node. * **Allowed Types**: Defines the data type that this input will accept. * **Allow Multiple Data**: Provides for multiple data on the same pin, if checked. Used with only certain data types. * **Allow Multiple Connections**: Currently disabled for all GPU node input pins. * **Pin Status**: Not relevant for Custom HLSL node. * **Tooltip**: Defines the tooltip displayed to users. |
| **Output Pins** | Defines the data that is output from the node. Contains the same options as the Input Pins, with additional options for setting up the output data. These are covered in the  section [Pin Setup](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine#pin-setup) below. |
| **Kernel Source Override** | Used to replace your **Shader Source** field with a UComputeSource asset. |
| **Additional Sources** | Allows referencing additional UComputeSource assets to be bundled with your Custom HLSL node. |
| **Mute Unwritten Pin Data Errors** | Mutes warnings on output pins with potentially uninitialized data. |
| **Seed** | Defines the seed value used to drive random generation. |
| **Dump Cooked HLSL** | Prints the cooked HLSL data into the log when it is generated for debugging. |
| **Dump Data Descriptions** | Prints the data descriptions of the input and output data into the log when it is generated for debugging. |
| **Print Shader Debug Values** | Provides simple debug logging from shader code. Covered in the  [Debugging Custom HLSL](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine#debugging-custom-hlsl) section below. |
| **Trigger Render Captu****r****e** | If a GPU debugger is attached and the graph is currently being debugged, then the next execution of the graph will trigger a scoped render capture of the dispatch of the kernels associated with this node. |

### HLSL Source Editor

The HLSL Source Editor provides quick authoring of Custom HLSL nodes. It can be found in the PCG Graph editor under **Window > HLSL Source Editor**, or by selecting a Custom HLSL node and clicking the **Open Source Editor** button in the node settings.

The HLSL Source Editor has three parts:

* **Declarations panel**
* **Shader Functions**
* **Shader Source**

[![PCG HLSL Source Editor](https://dev.epicgames.com/community/api/documentation/image/2b359d25-46a9-4788-b470-26e98e7942a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b359d25-46a9-4788-b470-26e98e7942a8?resizing_type=fit)

The **Declarations panel** serves as an API reference for writing your shader code. The declarations are automatically generated from the Custom HLSL node settings, such as the kernel type and input/output pin settings.

The **Shader Functions** field allows authors to create reusable functions to call in their **Shader Source**.

The **Shader Source** field is where you implement the main entry point for your kernel implementation.

### Custom HLSL Node Kernel Types

The **Kernel Type** defines a preset for the behavior of the node.

#### Point Processor

The **Point Processor** kernel type is ideal for modifying points. It requires the primary input and output pin to be of type Point, and executes the HLSL code once for each point. Data sent by the primary output pin has the same layout as the primary input pin, meaning the number of data and number of elements are identical.

All points in the primary output are automatically initialized from the primary input, so it is only necessary to set output attributes that should be changed.

You can also use the Point Processor to create additional input and output pins which you must configure manually to set the desired data type and data/element counts.

[![Custom HLSL node Point Processor](https://dev.epicgames.com/community/api/documentation/image/8fd161ee-9135-44c5-a151-557955c2f498?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8fd161ee-9135-44c5-a151-557955c2f498?resizing_type=fit)

#### Point Generator

The **Point Generator** kernel type is ideal for creating and populating a set of points. It requires the primary output pin to be of type Point, and executes the HLSL code once for each point.

This kernel type has the following additional options:

|  |  |
| --- | --- |
| **Option** | **Description** |
| **Num Elements** | Determines the number of points that are generated. The shader code is executed on each generated point. |

[![Custom HLSL node Point Generator](https://dev.epicgames.com/community/api/documentation/image/5857769b-f3e7-4bb7-b2d5-2f67cf82127d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5857769b-f3e7-4bb7-b2d5-2f67cf82127d?resizing_type=fit)

Similar to the Point Processor, you can use the Point Generator to create additional input and output pins which you must configure manually to set the desired data type and data or element counts.

#### Attribute Processor

The **Attribute Processor** kernel behaves similarly to the Point Processor kernel, forwarding attribute sets from the primary input pin to the primary output pin. The kernel will execute one thread per element in the input attribute set(s).

#### Custom

The **Custom** kernel type exposes fine-grained control over the execution for advanced use cases. Unlike the other two kernel types, there are no settings enforced on the input or output pins, as the node does not assume any specific relationship between the input and output. The output data must be configured in the output pin settings which are documented below. The number of threads that should execute the shader code must also be configured.

[![Custom HLSL node Custom](https://dev.epicgames.com/community/api/documentation/image/e5f8b729-3531-4010-afc9-a255af5b0416?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5f8b729-3531-4010-afc9-a255af5b0416?resizing_type=fit)

This kernel type has the following additional options:

|  |  |
| --- | --- |
| **Option** | **Description** |
| **Dispatch Thread Count** | Determines the number of threads the shader code uses to execute. The following modes are available:   * **From First Output Pin**: Dispatches one thread per data element (e.g. per point) on the first output pin. Can have a user-defined thread multiplier. * **Fixed Thread Count**: Defines a specific thread count. * **From Product of Input Pins**: Dispatches a thread per data element coming from one or more input pins. Can have a user-defined thread multiplier. |

### Pin Setup

Any pins not driven by the  **Kernel Type** should be configured manually.

For output pins, it is required to explicitly describe the data size and layout, which can be set under the **GPU Properties** dropdown in the output pin settings.

|  |  |
| --- | --- |
| **Option** | **Description** |
| **Initialization Mode** | Describes how the output data for this pin will be initialized. The menu contains the following modes:   * **From First Output Pin**: Dispatches one thread per element on the first output pin. Can have a user-defined thread multiplier. * **Fixed Thread Count**: Defines a specific thread count. * **From Product of Input Pins**: Dispatches a thread per data element coming from one or more input pins. Can have a user-defined thread multiplier. |
| **Pins to Initialize From** | Defines the input pins to initialize this pin's data from. |
| **Data Count Mode** | Defines the number of data objects. The menu contains the following modes:   * **From Input Data**: Acquire data counts from the **Pins to Initialize From**. * **Fixed**: Specifies a number of data to output. |
| **Data Multiplicity** | Combines data counts if there are multiple **Pins to Initialize From**.  Available modes:   * **Pairwise**: A data item is produced for each pair/tuple/etc. of input data items across the input pins. Requires all pins to have the same number of data. * **Cartesian**: If there are two input pins with N and M data items respectively, the output will have NxM data items. |
| **Element Count Mode** | Defines the number of elements. The menu contains the following modes:   * **From Input Data**: Acquire element counts from the **Pins to Initialize From**. * **Fixed**: Specify a number of elements to output. |
| **Element Multiplicity** | Combines element counts if there are multiple **Pins to Initialize From**.  Available modes:   * **Product**: Element count will be the product of the elements in each pair/tuple/etc. of input data. * **Sum**: Element count will be the sum of the elements in each pair/tuple/etc. of input data. |
| **Attribute Inheritance Mode** | Defines how to inherit attribute names, types, and values. The menu contains the following modes:   * **None:** No attributes inherited from **Pins to Initialize From**. * **Copy Attribute Setup**: Takes attribute names and types from **Pins to Initialize From**. Pins declared first will take priority during conflicts. Does not copy values. |
| **Attributes to Create** | Defines a list of new attributes to create on the output data. |

### Debugging Custom HLSL

The **Debug Display** (default hotkey ‘D’) and **Inspection** (default hotkey ‘A’) features work for GPU nodes and enable inspection of the data flowing through the GPU nodes.

It is also possible to debug custom shader code by toggling the **Print Shader Debug Values** option on the Custom HLSL node. This exposes a new function `WriteDebugValue`, which can be used to write float values to a buffer which gets logged during execution. The buffer size is controlled by the **Debug Buffer Size** property.

### Examples

#### Example 1: Height Offset Using a Sine Wave

In the example below, a **Point Processor** is used to apply a sine wave-based height offset to a set of points.

The following code is added to the **Shader Source** field of HLSL Source Editor window:

HLSL

```
// Get the position of the incoming point from input pin ‘In’.
float3 Position = In_GetPosition(In_DataIndex, ElementIndex);

// Compute a sine wave with amplitude 500cm and wavelength 400cm.
const float Wave = 500.0f * sin(Position.x / 400.0f);

// Add the wave to the Z coordinate of the point’s position.
Position.z += Wave;

// Write the offset position to the output point on pin ‘Out’.
```

Copy full snippet(11 lines long)

[![Height offset using a sine wave](https://dev.epicgames.com/community/api/documentation/image/cc577246-e92c-4c93-a663-0cd3fed7571d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc577246-e92c-4c93-a663-0cd3fed7571d?resizing_type=fit)

[![Source editor code for height offset using a sine wave](https://dev.epicgames.com/community/api/documentation/image/aca49e82-ff58-4ee1-aedf-a9764ca6b9e4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aca49e82-ff58-4ee1-aedf-a9764ca6b9e4?resizing_type=fit)

#### Example 2: Creating an Attribute

In the example below, a Point Generator is used to create a grid of points, and uses an attribute set to control the height of the grid.

The following code is added to the **Shader Source** field of **HLSL Source Editor** window:

HLSL

```
// Get PCG Component bounds.
const float3 BoundsMin = GetComponentBoundsMin();
const float3 BoundsMax = GetComponentBoundsMax();

// Get the current point position in a 2D grid, based on the 
// number of points and the component bounds.
float3 Position = CreateGrid2D(ElementIndex, NumPoints, BoundsMin, BoundsMax);
Position.z += InHeight_GetFloat(0, 0, 'GridHeight');

// Set the point's position.
```

Copy full snippet(11 lines long)

Attributes can be accessed in shader code using the provided Get and Set functions, and querying the attribute by name by wrapping it in apostrophes. For example, ‘GridHeight’.

[![Creating an attribute](https://dev.epicgames.com/community/api/documentation/image/8647ebff-ae2c-4c50-b142-97bbfd66774e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8647ebff-ae2c-4c50-b142-97bbfd66774e?resizing_type=fit)

[![Creating an attribute source editor code](https://dev.epicgames.com/community/api/documentation/image/4540be89-3895-422f-9d20-51cefbf99f86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4540be89-3895-422f-9d20-51cefbf99f86?resizing_type=fit)

#### Example 3: Spawning Random Meshes on a Landscape

The Custom HLSL node is also capable of running a sequence of operations.

In the example below, the shader code performs the following operations:

* Creates several points on a landscape.
* Applies a random position adjustment to each point.
* Sets the point position.
* Writes a random seed value to each point.
* Reads an attribute set containing a list of static meshes and assigns a random mesh to each point.

Downstream of the Custom HLSL node is a **Static Mesh Spawner** with GPU execution enabled and the mesh attribute set to `MeshPath`.

On the GPU attributes of type String, Name, Soft Object Path, Soft Class Path become `StringKeys`, which uniquely identify each string.

The following code is added to the **Shader Source** field of **HLSL Source** window:

HLSL

```
// Get generation volume bounds
const float3 BoundsMin = GetComponentBoundsMin();
const float3 BoundsMax = GetComponentBoundsMax();

// Compute a position on a 2D grid within the volume.
float3 Pos = CreateGrid2D(ElementIndex, NumPoints, BoundsMin, BoundsMax);

// Initialize the random seed from the position.
uint Seed = ComputeSeedFromPosition(Pos);
```

Copy full snippet(30 lines long)

[![Spawning random meshes on a landscape](https://dev.epicgames.com/community/api/documentation/image/1bea9066-d7e4-46ca-a309-0d79274d07de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1bea9066-d7e4-46ca-a309-0d79274d07de?resizing_type=fit)

[![Spawning random meshes on a landscape source editor code](https://dev.epicgames.com/community/api/documentation/image/e1083368-37ff-4132-a369-cb3f307b56c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1083368-37ff-4132-a369-cb3f307b56c7?resizing_type=fit)

### Static Mesh Spawner Node

You can cause the Static Mesh Spawner node to execute on the GPU by toggling the **Execute on GPU** option in the node settings.

#### Procedural Instancing

When the Static Mesh Spawner is set to run on the GPU, it sets up mesh instances entirely on the GPU, saving CPU time and memory. This uses the **Procedurally Instanced Static Mesh Component**. This can be a very efficient path for spawning meshes, but is experimental and comes with the following tradeoffs:

* Instances are not persisted or saved in any way. They exist only at runtime in GPU memory.

  + Therefore the primary use case is **Runtime Generation**.
  + Static Baked Lighting and HLOD require persisted instance information and are also not supported at this time.
* Several features currently require CPU access to instance data and are not supported:

  + Collisions / physics
  + Navigation
  + Ray tracing
  + Affecting Distance Field lighting

The GPU implementation is Experimental and not all Static Mesh Spawner features are supported.

### Mesh Selector Types

The following mesh selectors are supported when executing on the GPU, and due to how instances are allocated, there are slight differences in behavior.

* Weighted (**PCGMeshSelectorWeighted**)

  + Similar to the CPU implementation, this mode uses the input point random seeds and the configured selection weights to randomly select the mesh for each instance. These meshes must be set on the node rather than driven by attribute.
  + The system uses weights to determine how many instances should be allocated for each mesh. An over allocation is made based on a heuristic to minimize the chance of saturating the allocation for one or more primitives and losing instances.
  + This mode relies on the **Seed** attribute on points being well-initialized, for example using the provided shader function `ComputeSeedFromPosition()`. If all point seeds are set to the same value, the same selection will be made for all points and the estimated allocation may be exceeded which will result in instances missing from the result.
* By-Attribute (**PCGMeshSelectorByAttribute**)
* Other mesh selector types (for example, **PCGMeshSelectorWeightedByCategory**) are not currently supported when executing on GPU.

The final allocated instance counts can be inspected by selecting the generated **procedurally instanced static mesh components** and checking the **Num Instances** property.

### Instance Data Packing

Similar to CPU execution, attributes can be packed into instance data.

The system needs to know prior to GPU execution how many attributes will be packed, and therefore only the by-attribute packer type (**PCGInstanceDataPackerByAttribute**) is supported.

### Component-less Spawning Via FastGeo

The FastGeo spawning path is Experimental.

Rather than using actor components to spawn primitives, we have Experimental support for spawning primitives via FastGeo components. These are simpler and more compact than actor components, and require significantly less Game Thread time for setup and tear down.

To enable this path, enable the experimental PCGFastGeoInterop plugin, and enable the CVar `pcg.RuntimeGeneration.ISM.ComponentlessPrimitives`. The results should be visually identical, but spawned using a more efficient path.

### Other Nodes

The following nodes currently support GPU execution:

* Attribute Partition

  + Currently only supports partitioning on attributes of type String, Soft Object Path or Soft Class Path.
* Copy Points
* Cull Points Outside Actor Bounds
* Custom HLSL

  + CPU execution not supported.
* Data Count
* Normal to Density
* Static Mesh Spawner
* Transform Points

## Compute Sources

**Compute Source** assets make sharing source code easier and reduces code duplication between nodes.

The assets support in-line editing of HLSL source code with syntax highlighting, and PCG specific syntax like data labels and attribute names.

Compute Source assets can also reference other Compute Source assets by using the **Additional Sources** property which creates dependency hierarchies between multiple compute sources.

[![Compute source assets](https://dev.epicgames.com/community/api/documentation/image/40d5a4fe-2177-4b57-b348-59c69467b68c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40d5a4fe-2177-4b57-b348-59c69467b68c?resizing_type=fit)

## Data Labels

Data labels can be used to reference data by label rather than index in Custom HLSL source. Data labels are communicated on data through tags with the prefix PCG\_DATA\_LABEL.

Some nodes automatically label their output data, including:

* **Get Texture Data**
* **Get Virtual Texture Data**
* **Generate Grass Maps**

[![Data labels 1](https://dev.epicgames.com/community/api/documentation/image/f9cd0c8f-018f-4801-877a-6707512231aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9cd0c8f-018f-4801-877a-6707512231aa?resizing_type=fit)

[![Data labels 2](https://dev.epicgames.com/community/api/documentation/image/20f0d641-0eed-472c-b130-7e19ee28a146?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20f0d641-0eed-472c-b130-7e19ee28a146?resizing_type=fit)

## Sampling Landscape Heights

A common use case is scattering assets on a landscape, and a few paths exist for sampling landscape height information with different trade-offs:

* Default: Upload heights to GPU from Landscape Collision Components

  + Used when Get Landscape Data with default settings is connected directly to a Landscape input pin on a GPU node.
  + Robust, does not depend on virtual textures.
  + Uses some game thread time to gather and upload the height data.
* Landscape Height Runtime Virtual Texture

  + See Using Virtual Textures in PCG section below for details about setting up this path.
  + Efficient, kernels can access height data directly on the GPU without CPU involvement.
  + Relies on the Virtual Texture being sufficiently populated which can be problematic to ensure in all cases.
* Generate Landscape Textures node

  + Generates landscape height maps (and optionally grass maps) directly on the GPU using data from the landscape system.
  + Efficient, does not require CPU involvement.
  + Robust, does not depend on Runtime Virtual Textures

## Generating Grass Maps

PCG supports sampling **Landscape Grass Layers** from a specified Landscape material to support runtime procedural generation workflows.

1. Set up your Landscape material with a **Landscape Grass Output** node. For more information on setting up a Landscape material, see [Landscape Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine).

   [![Landscape material with a landscape grass output node](https://dev.epicgames.com/community/api/documentation/image/d9d96b86-9245-465b-96d7-8351c084f87b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9d96b86-9245-465b-96d7-8351c084f87b?resizing_type=fit)
2. Connect your landscape data into a **Generate Grass Maps** node. Select your desired grass types directly using override or through exclusion.
3. Sample your grass map textures. You can sample by index or by the automatically assigned data labels. The following code is added to the **Shader Source** field of **HLSL Source Editor** window:

C++

```
float3 Min = GetComponentBoundsMin();
float3 Max = GetComponentBoundsMax();

float3 Position = CreateGrid2D(ElementIndex, NumPoints, Min, Max);
uint Seed = ComputeSeedFromPosition(Position);
Position.xy += (float2(FRand(Seed), FRand(Seed)) - 0.5) * 45.0;
Position.z = LS_GetHeight(Position);

float Density = FRand(Seed);
float Thresh = GrassMaps_SampleWorldPos('GSM_PCGGrass1', Position.xy).x;
```

Expand code  Copy full snippet(21 lines long)

[![Generate grass maps node](https://dev.epicgames.com/community/api/documentation/image/167347c6-e337-4cd4-a4f9-edb9763bbee7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/167347c6-e337-4cd4-a4f9-edb9763bbee7?resizing_type=fit)

If you plan to sample your grass map textures only on the GPU, you can toggle **Skip Readback to CPU** in the PCG Graph for significant performance improvements.

[![Generate grass maps - skip Readback to CPU](https://dev.epicgames.com/community/api/documentation/image/81183c7b-0866-49f9-8a02-726a89621b84?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81183c7b-0866-49f9-8a02-726a89621b84?resizing_type=fit)

Painted landscape layers:

[![Painted landscape layers](https://dev.epicgames.com/community/api/documentation/image/c7bdb334-bce8-4ef7-bcc2-dc2aae53aca3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7bdb334-bce8-4ef7-bcc2-dc2aae53aca3?resizing_type=fit)

Resulting generation:

[![Grass map generation](https://dev.epicgames.com/community/api/documentation/image/821544bc-0f44-4c8f-aa79-19a4f089b233?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/821544bc-0f44-4c8f-aa79-19a4f089b233?resizing_type=fit)

## Using Virtual Textures in PCG

PCG supports using virtual textures as part of your procedural content generation workflow.

### Virtual texture sampling

Virtual textures can be sampled from Landscape data to improve the performance of height sampling.

#### Example 1: Landscape Height Virtual Texture

To sample Landscape data using virtual textures, make sure **Sample Virtual Textures** is toggled on in the **Get Landscape Data** node settings. This gives the ability to the **Landscape Data** node to use any virtual textures provided through the corresponding **Landscape Material**.

This only affects GPU sampling.

HLSL

```
// Get Position and Height
float3 Position = CreateGrid2D(ElementIndex, NumPoints, GetComponentBoundsMin(), GetComponentBoundsMax());
Position.z = A_GetHeight(Position);

// Get Normal and Orientation
const float3 Normal = A_GetNormal(Position);
const FQuat Orientation = QuatFromNormal(Normal);

// Get Base Color
const float3 BaseColor = A_GetBaseColor(Position);
```

Copy full snippet(15 lines long)

[![Landscape data generated using virtual textures](https://dev.epicgames.com/community/api/documentation/image/4ba4d517-fa22-4c19-b0e6-1cca9e826629?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ba4d517-fa22-4c19-b0e6-1cca9e826629?resizing_type=fit)

#### Example 2: Virtual Texture Data

To sample a virtual texture, query the world for runtime virtual texture components. Each one will produce a virtual texture data, tagged with a data label for the runtime virtual texture asset.

C++

```
float3 Position = CreateGrid2D(ElementIndex, NumPoints, GetComponentBoundsMin(), GetComponentBoundsMax());

// Sample virtual textures
bool bInsideVolume;
float3 BaseColor;
float Specular;
float Roughness;
float WorldHeight;
float3 Normal;
float Displacement;
```

Expand code  Copy full snippet(19 lines long)

[![Virtual texture data](https://dev.epicgames.com/community/api/documentation/image/8472b6a7-a12d-4c80-b5d6-cb6efec34b21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8472b6a7-a12d-4c80-b5d6-cb6efec34b21?resizing_type=fit)

### Virtual Texture Priming

It’s important to make sure the virtual textures are primed before generation, otherwise your sampling results may be inaccurate.

To request virtual texture priming, add a graph parameter of type `FPCGVirtualTexturePrimingInfo` to your PCG Graph. This exposes the following options:

|  |  |
| --- | --- |
| **Virtual Texture** | Defines the virtual texture to be primed. |
| **Grid** | Defines the largest grid on which the virtual texture is sampled in the graph. The virtual textures are primed for the generation radius dictated by this grid. |
| **World Texel Size** | Defines the desired size of a texel in the primed virtual texture. This will determine what mipmap level should be primed. |

You can control virtual texture priming using the console command `pcg.VirtualTexturePriming.Enable`. You can debug this feature using the command `pcg.VirtualTexturePriming.DebugDrawTexturePrimingBounds`.

[![VIrtual texture priming](https://dev.epicgames.com/community/api/documentation/image/ae34190b-be03-4885-b6b9-554159a42eb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae34190b-be03-4885-b6b9-554159a42eb3?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Authoring High Performance Graphs](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#authoringhighperformancegraphs)
* [Supported Nodes](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#supported-nodes)
* [Custom HLSL Node](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#customhlslnode)
* [HLSL Source Editor](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#hlslsourceeditor)
* [Custom HLSL Node Kernel Types](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#custom-hlsl-node-kernel-types)
* [Point Processor](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#pointprocessor)
* [Point Generator](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#pointgenerator)
* [Attribute Processor](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#attributeprocessor)
* [Custom](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#custom)
* [Pin Setup](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#pin-setup)
* [Debugging Custom HLSL](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#debugging-custom-hlsl)
* [Examples](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#examples)
* [Example 1: Height Offset Using a Sine Wave](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#example1:heightoffsetusingasinewave)
* [Example 2: Creating an Attribute](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#example2:creatinganattribute)
* [Example 3: Spawning Random Meshes on a Landscape](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#example3:spawningrandommeshesonalandscape)
* [Static Mesh Spawner Node](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#staticmeshspawnernode)
* [Procedural Instancing](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#proceduralinstancing)
* [Mesh Selector Types](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#meshselectortypes)
* [Instance Data Packing](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#instancedatapacking)
* [Component-less Spawning Via FastGeo](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#component-lessspawningviafastgeo)
* [Other Nodes](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#othernodes)
* [Compute Sources](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#computesources)
* [Data Labels](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#datalabels)
* [Sampling Landscape Heights](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#samplinglandscapeheights)
* [Generating Grass Maps](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#generatinggrassmaps)
* [Using Virtual Textures in PCG](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#usingvirtualtexturesinpcg)
* [Virtual texture sampling](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#virtualtexturesampling)
* [Example 1: Landscape Height Virtual Texture](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#example1:landscapeheightvirtualtexture)
* [Example 2: Virtual Texture Data](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#example2:virtualtexturedata)
* [Virtual Texture Priming](/documentation/en-us/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.7#virtualtexturepriming)
