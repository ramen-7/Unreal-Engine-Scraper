<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine?application_version=5.7 -->

# BuildGraph

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Unreal Build Pipeline](/documentation/en-us/unreal-engine/using-the-unreal-engine-build-pipeline "Unreal Build Pipeline")
7. [Unreal Automation Tool](/documentation/en-us/unreal-engine/unreal-automation-tool-for-unreal-engine "Unreal Automation Tool")
8. BuildGraph

# BuildGraph

Customize your builds with the BuildGraph scripting system.

![BuildGraph](https://dev.epicgames.com/community/api/documentation/image/276005c7-425b-4d07-9ed7-336302873473?resizing_type=fill&width=1920&height=335)

 On this page

**BuildGraph** is a script-based build automation system that features graphs of building blocks common to **Unreal Engine (UE)** projects. BuildGraph integrates with **UnrealBuildTool**, **AutomationTool**, and the **Editor**. BuildGraph can also be extended and customized for your projects.

BuildGraph scripts are written in XML, specifying a graph of user-defined nodes with dependencies between them. Each node consists of tasks executed in sequence to produce some sort of output (for example, compile this project, then cook, run this test, and so on). When asked to build a target (that is, a node or named output) BuildGraph will execute all of the nodes in the graph required to make that happen.

Unlike other build tools, BuildGraph is designed as a hybrid between a makefile-like scripting language and a build farm configuration script. It enables annotations for the type of machine that steps are supposed to be executed on, providing a list of recipients for failure notifications if a step fails, and groups nodes that should only be executed after an explicit user trigger. It also tracks the creation of output files from task execution in a way that lends to graph execution being distributed across a farm of machines (with nodes running in parallel where possible) and intermediate artifacts being transferred to and from a network share automatically.

Epic uses BuildGraph to prepare the Unreal Engine binary release, package samples for the marketplace, and implement pipelines for our own games (among other things). Several example BuildGraph scripts are provided in the `[Unreal Engine Root Directory]/Engine/Build/Graph/Examples` directory, and the script for creating a binary Unreal Engine distribution can be found at `[Unreal Engine Root Directory]/Engine/Build/InstalledEngineBuild.xml`.

Opening a script with Visual Studio will use the schema located at `[Unreal Engine Root Directory]/Engine/Build/Graph/Schema.xsd` to provide rich tooltips, validation, and Intellisense features while editing.

## Writing BuildGraph Scripts

If you want to learn how to write your own BuildGraph scripts, it helps to know the various parts that go into making a Graph. Graphs are created with the following elements:

* **Tasks**: Actions that are executed as part of a build process (compiling, cooking, and so on).
* **Nodes**: A named sequence of ordered tasks that are executed to produce outputs. Before they can be executed, nodes may depend on other nodes executing their tasks first.
* **Agents**: A group of nodes that are executed on the same machine (if running as part of a build system). Agents have no effect when building locally.
* **Triggers**: Container for groups that should only be executed after manual intervention.
* **Aggregates**: Groups of nodes and named outputs that can be referred to with a single name.

Scripts typically make frequent use of properties for reusable or conditionally defined values. Properties are declared with the `<Property>` element, and are scoped to the point of their first declaration. Properties referenced with the `$(Property Name)` notation are valid within all attribute strings, and will be expanded when the script is read. Properties that can be supplied by the user on the command-line can be declared with the `<Option>` element, and environment variables can be imported into properties using the `<EnvVar>` element.

Any element may be conditionally defined via the "If" attribute. See below for the syntax of conditional expressions.

BuildGraph is typically used for packaged games, so filtering and file manipulation are natively supported. Any attribute that accepts a list of files may consist of a Perforce style wildcard (matching any number of `...`, `*` and `?` patterns in any location), a full path name, or a reference to a tagged collection of files. Attributes are denoted by prefixing a `#` character. Files may be added to a tag set using the `<Tag>` task, which also enables the performance of union and difference style operations. Each node can declare multiple outputs in the form of a list of named tags, which other nodes can then depend on.

Graphs may be executed in parallel as part of a build system. To do so, the initial graph configuration is generated by running with the `-Export=<Filename>` argument (producing a JSON file listing the nodes and dependencies to execute). Each participating agent should be synced to the same changelist, and AutomationTool (UAT) should be re-run with the appropriate `-SingleNode=<Name>` argument. Outputs from different nodes are transferred between agents via shared storage (typically, a network share) the path to which can be specified on the command line using the `-SharedStorageDir=<Path>` argument. Note that the allocation of machines (and coordination between them) is assumed to be managed by an external system.

The syntax of elements used to define BuildGraph constructs is listed in the following sections.

## BuildGraph Scripting Reference

[![BuildGraph Script Conditions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4082243c-40bb-4aa0-9972-a5ba6ea91aee/placeholder_topic.png)

BuildGraph Script Conditions

Learn syntax to write BuildGraph script conditions.](/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine)
[![BuildGraph Script Types](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb269443-11a3-4bd1-805b-78312f0e4841/placeholder_topic.png)

BuildGraph Script Types

Learn about valid data types for BuildGraph attributes.](/documentation/en-us/unreal-engine/buildgraph-script-types-reference-for-unreal-engine)
[![BuildGraph Script Tasks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a28e256-3952-4ce3-b22a-1f4449117eb9/placeholder_topic.png)

BuildGraph Script Tasks

Learn how BuildGraph can help you create custom tasks.](/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine)
[![BuildGraph Script Elements](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27c8a703-e2ae-4a0d-90b3-7cd9c8bb02e3/placeholder_topic.png)

BuildGraph Script Elements

Learn about BuildGraph Elements.](/documentation/en-us/unreal-engine/buildgraph-script-elements-reference-for-unreal-engine)

## Using BuildGraph

[![BuildGraph Usage](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e2d72f2-2ca9-4d66-b27a-7c42ed9c39f0/placeholder_topic.png)

BuildGraph Usage

This page provides sample BuildGraph Script usage.](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine)

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [buildgraph](https://dev.epicgames.com/community/search?query=buildgraph)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Writing BuildGraph Scripts](/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine?application_version=5.7#writingbuildgraphscripts)
* [BuildGraph Scripting Reference](/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine?application_version=5.7#buildgraphscriptingreference)
* [Using BuildGraph](/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine?application_version=5.7#usingbuildgraph)

Related documents

[UnrealBuildTool

![UnrealBuildTool](https://dev.epicgames.com/community/api/documentation/image/6e2c734a-9b81-4c58-a46d-230de6ba218d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine)
