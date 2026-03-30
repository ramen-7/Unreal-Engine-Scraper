<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine?application_version=5.7 -->

# BuildGraph Script Conditions

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
10. BuildGraph Script Conditions

# BuildGraph Script Conditions

Learn syntax to write BuildGraph script conditions.

![BuildGraph Script Conditions](https://dev.epicgames.com/community/api/documentation/image/7373afda-927a-4843-8d19-4e21b8b3df6d?resizing_type=fill&width=1920&height=335)

 On this page

If you want to build logical complexity into your **BuildGraph** scripts, you need to work with **conditionals**. The following section introduces you to how BuildGraph conditions are written, including a list of conditional operators.

## Conditions

BuildGraph script conditions consist of atoms and operators that evaluate to `true` or `false`.

### Atoms

**Atoms** can be numbers, strings, or identifiers that are coerced to their appropriate type for the operator using them. Atoms may be quoted with single (') or double (") quotes. They can also be an unquoted sequence of letters, digits, and underscore characters. All atoms are considered the same type, regardless of how they are declared. Additionally, atoms are considered case-insensitive for comparisons. This means that the strings "True" and 'true' are identical to the identifier `true` (despite the presence of quotes and differences in case).

## Operators

A list of operators is specified below:

| **Operator** | **Description** | **Precedence** |
| --- | --- | --- |
| `(x)` | Subexpression used for grouping. | 1 |
| `!x` | Evaluates to `true` if `x` is `false`. | 1 |
| `Exists(x)` | Evaluates to `true` if the file `x` exists. | 1 |
| `HasTrailingSlash(x)` | Evaluates to `true` if `x` ends with a slash or backslash. | 1 |
| `x == y` | Evaluates to `true` if the two atoms are equal (case insensitive). | 2 |
| `x != y` | Evaluates to `true` if the two atoms are not equal (case insensitive). | 2 |
| `x < y` | Evaluates to `true` if the integer `x` is less than the integer `y`. | 2 |
| `x <= y` | Evaluates to `true` if the integer `x` is less than or equal to the integer `y`. | 2 |
| `x > y` | Evaluates to `true` if the integer `x` is greater than the integer `y`. | 2 |
| `x >= y` | Evaluates to `true` if the integer `x` is greater than or equal to the integer `y`. | 2 |
| `x and y` | Evaluates to `true` if both atoms are `true`. | 3 |
| `x or y` | Evaluates to `true` if either `x` is `true`, `y` is `true`, or both atoms are `true`. | 4 |

The `'<'` and `'>'` characters must be escaped as `"<"` and `">"` in XML.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [buildgraph](https://dev.epicgames.com/community/search?query=buildgraph)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Conditions](/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine?application_version=5.7#conditions)
* [Atoms](/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine?application_version=5.7#atoms)
* [Operators](/documentation/en-us/unreal-engine/buildgraph-script-conditions-reference-for-unreal-engine?application_version=5.7#operators)
