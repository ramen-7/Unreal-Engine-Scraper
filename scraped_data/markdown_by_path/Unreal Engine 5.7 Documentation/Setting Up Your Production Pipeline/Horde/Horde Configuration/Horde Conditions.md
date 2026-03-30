<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7 -->

# Horde Conditions

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
6. [Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine "Horde")
7. [Horde Configuration](/documentation/en-us/unreal-engine/horde-configuration-for-unreal-engine "Horde Configuration")
8. Horde Conditions

# Horde Conditions

An overview of Horde Conditions.

![Horde Conditions](https://dev.epicgames.com/community/api/documentation/image/ffb16834-c481-44ad-af7e-1351b7e83066?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

In several parts of Horde, you can specify a query condition to select particular agents for an operation. These condition strings are stored in JSON configuration flies as a string and have a C-like syntax.

Agents report many properties collected from their characteristics, which you can view from the Agents page on the Horde dashboard. Agents may report multiple values for a particular key, such as `PlatformGroup: Desktop` and `PlatformGroup: Unix`. Conditions evaluate to true if there is any value for a particular key that satisfies the expression.

## Values

Values in condition strings are dynamically typed and coerced into the correct format for the operation performed on them. For example, the integer `0`, the strings `'0'` and `'false'`, and the boolean `false` are functionally equivalent.

Integers can be given the following binary order-of-magnitude suffixes as a shorthand:

| Suffix | Size |
| --- | --- |
| Kb | 2^10 (1,024) |
| Mb | 2^20 (1,048,576) |
| Gb | 2^30 (1,073,741,824) |
| Tb | 2^40 (1,099,511,627,776) |

## Operators

Operators follow standard C rules of precedence. Sub-expressions may be enclosed in `(` parentheses `)`.

### Boolean Operators

| Operator | Description |
| --- | --- |
| `true` | Boolean literal |
| `false` | Boolean literal |
| `!A` | Negation |
| A `&&` B | Logical AND |
| A `\|\|` B | Logical OR |
| A `==` B | Equality |
| A `!=` B | Inequality |

### Integer Operators

| Operator | Description |
| --- | --- |
| `1234` | Integer literal |
| `1234kb` | Integer literal with binary size suffix (evaluates to 1,263,616). |
| A `==` B | Test for equality |
| A `!=` B | Test for inequality |
| A `<` B | Test if one value is less than another |
| A `<=` B | Test if one value is less than or equal to another |
| A `>` B | Test if one value is greater than another |
| A `>=` B | Test if one value is greater than or equal to another |
| A `==` B | Test for equality |

### String Operators

| Operator | Description |
| --- | --- |
| `'value'` | String literal |
| `"value"` | String literal |
| A `==` B | Test if two strings compare equal for equality. Comparison is case-insensitive. |
| A `!=` B | Test if two strings are different. Comparison is case-insensitive. |
| A `~=` B | Test if a string (A) matches a regex (B). The regex comparison is case-insensitive. |

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7#introduction)
* [Values](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7#values)
* [Operators](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7#operators)
* [Boolean Operators](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7#booleanoperators)
* [Integer Operators](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7#integeroperators)
* [String Operators](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine?application_version=5.7#stringoperators)
