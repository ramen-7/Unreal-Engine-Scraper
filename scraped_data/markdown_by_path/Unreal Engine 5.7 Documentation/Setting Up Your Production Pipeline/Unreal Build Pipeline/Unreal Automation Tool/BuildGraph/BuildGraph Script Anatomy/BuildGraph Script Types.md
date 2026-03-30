<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-types-reference-for-unreal-engine?application_version=5.7 -->

# BuildGraph Script Types

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
8. [BuildGraph](/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine "BuildGraph")
9. [BuildGraph Script Anatomy](/documentation/en-us/unreal-engine/buildgraph-script-anatomy-for-unreal-engine "BuildGraph Script Anatomy")
10. BuildGraph Script Types

# BuildGraph Script Types

Learn about valid data types for BuildGraph attributes.

![BuildGraph Script Types](https://dev.epicgames.com/community/api/documentation/image/3870f8db-ff90-457d-80b9-74388c82b9cb?resizing_type=fill&width=1920&height=335)

The following table contains valid data types that can be contained by **BuildGraph** attributes:

| **Type** | **Description** |
| --- | --- |
| **String** | An arbitrary string. |
| **String List** | A list of arbitrary strings separated by semicolons. |
| **Boolean** | The constant `true` or `false`. |
| **Integer** | An integer constant. |
| **Regex** | A regular expression, using [C#](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference) syntax. |
| **Name** | A named entity. Any printable character, except `^ < > : " / \ \| ? * ;`. Single spaces are allowed (except at the start and end of a name). |
| **Name List** | A list of identifiers separated by semicolons. |
| **Tag** | A label given to a list of files beginning with the # character (for example, `#My Files`). |
| **Tag List** | A list of tags separated by semicolons (for example, `#My Files;#Other Files`). |
| **Target** | A node name, aggregate name, agent name, or tag name. Indicates a sequence of nodes that need to be executed. Note that this overlaps with the meaning of `Target` as it applies to [UnrealBuildTool](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine) (which refers to a single program being built). |
| **Target list** | A list of target names separated by semicolons. |
| **File Spec** | A set of file and tag names separated by semicolons. Wildcards such as `"..."`, `"_"`, and `"?"` are permitted when referencing files (for example, `Engine/.../_.bat`). Unless otherwise specified, relative paths are resolved relative to the working root directory. |
| **File Reference** | A path to a file. Unless otherwise specified, relative paths are resolved to the working root directory. |
| **Directory Reference** | A path to a directory. Unless otherwise specified, relative paths are resolved relative to the working root directory. |
| **Unreal Target Configuration** | The configuration in which to build the target. Available configurations are: `Debug`, `DebugGame`, `Development`, `Test`, or `Shipping`. |
| **Unreal Target Platform** | A platform that Unreal Engine supports. Supported platforms can be found in [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine). Please refer to your platform's documentation. |
| **Condition** | A [conditional expression](/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine). |

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [buildgraph](https://dev.epicgames.com/community/search?query=buildgraph)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
