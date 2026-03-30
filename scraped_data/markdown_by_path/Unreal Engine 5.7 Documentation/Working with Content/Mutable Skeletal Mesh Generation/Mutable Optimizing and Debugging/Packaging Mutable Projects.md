<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7 -->

# Packaging Mutable Projects

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
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Optimizing and Debugging](/documentation/en-us/unreal-engine/mutable-optimizing-and-debugging-in-unreal-engine "Mutable Optimizing and Debugging")
8. Packaging Mutable Projects

# Packaging Mutable Projects

An overview of how Mutable packages your Unreal Engine projects.

![Packaging Mutable Projects](https://dev.epicgames.com/community/api/documentation/image/366daf0c-2b20-457f-8f5d-dbe14aa347c3?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

Mutable packages data like any other asset when packaging projects.

At runtime, Mutable does not use the source graph of the Customizable Objects. Instead, it converts this graph into a more efficient representation and removes it from the asset, like Blueprints or Materials.

Most of the meshes and textures in the source graph are processed and stored in Mutable's internal format. These processed resources are packed in .pak/.ucas containers. Source assets converted to Mutable are not included in builds unless referenced externally.

Assets not processed are included in the package as standard Unreal assets. Here is a list of the assets that may be included in builds.

Pass-through meshes and textures (Mutable does not touch them)

* Materials
* Skeletons
* Skeletal meshes of reference
* Baked instances (They are no longer Mutable assets)

## Packaging Options

* Base customizable objects are compiled during the cook stage. To improve runtime performance and texture quality, Mutable overrides some of the compile options specified in the base object. The optimization level is set to **Maximum**, and texture compression is set to **High Quality**.

### Bulk data files

Processed resources are stored in bulk data files and streamed on demand when generating an instance. These files can be stored in two different formats:

* **Bulk Data** format (`.ubulk` and `.uptnl`)
* Mutable format (`.mut` and `.mut.high`)

#### BulkData format

Bulk data (`.ubulk`) is the standard file format for binary blobs. It is the default and recommended format. Bulk data provides benefits like compatibility with content on demand, allows the use of optional data, has slightly faster load times especially noticeable on big projects, and has better integration with other standard UE features.

On the other hand, it can generate a limited number of `.ubulk` files, which in some cases might produce worse patching results.

#### Mutable format

The Mutable format (`.mut` and `.mut.high`) main benefit is that there is more control over the output. It doesn’t have a restriction on the number of files to generate, so if appropriately configured, it can produce better patching results. Lowering the maximum size of the generated files will result in more files and granularity.

The maximum size of Mutable files can be set per object in the compilation options by modifying the **Packaged Data File Max Limit** value. This setting is only relevant when packaging a project.

The downside is that it has worse integration with some UE features. Content on demand and optional bulk data files are not supported.

[![Mutable Packaging Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9f9ffce-519a-4af8-8e60-9c8351bab15a/mutable-packaging.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9f9ffce-519a-4af8-8e60-9c8351bab15a/mutable-packaging.png)

The Mutable packaging options.

### Embedded Bulk Data

Some blobs of bulk data are so small that streaming them may be inefficient. It is possible to configure a size limit to decide which bulk data files will be streamed or embedded into the object. Embedded resources use additional memory but can improve performance.

The Embedded Data Limit setting in the compilation options sets the embedded data threshold. A value of `256` bytes usually provides a reasonable tradeoff.

## Customizable Object Instance Assets

Instances are also packed into the build, but their size is negligible since they only contain parameter values. These values are stored in a portable way to support adding, removing, and changing parameters in the source graph of the Customizable Object. At runtime, the parameters and values are validated and updated.

See the section on [Storage and Replication](/documentation/en-us/unreal-engine/mutable-storage-and-replication-in-unreal-engine) for details.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Packaging Options](/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7#packagingoptions)
* [Bulk data files](/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7#bulkdatafiles)
* [BulkData format](/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7#bulkdataformat)
* [Mutable format](/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7#mutableformat)
* [Embedded Bulk Data](/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7#embeddedbulkdata)
* [Customizable Object Instance Assets](/documentation/en-us/unreal-engine/packaging-mutable-projects-in-unreal-engine?application_version=5.7#customizableobjectinstanceassets)
