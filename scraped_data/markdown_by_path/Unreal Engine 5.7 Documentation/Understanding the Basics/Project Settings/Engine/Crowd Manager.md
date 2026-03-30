<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/crowd-manager-settings-in-the-the-unreal-engine-project-settings?application_version=5.7 -->

# Crowd Manager

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine "Project Settings")
7. [Engine](/documentation/en-us/unreal-engine/engine-settings-in-the-unreal-engine-project-settings "Engine")
8. Crowd Manager

# Crowd Manager

Crowd Manager section of the Unreal Engine Project Settings.

On this page

## Crowd Manager

### Config

| **Section** | **Description** |
| --- | --- |
| **Avoidance Config** | Obstacle avoidance parameters. |
| **Sampling Patterns** | Obstacle avoidance parameters. |
| **Max Agents** | Maximum number of agents supported by crowd. |
| **Max Agent Radius** | Maximum radius of an agent that can be added to the crowd. |
| **Max Avoided Agents** | Maximum number of neighbor agents for velocity avoidance. |
| **Max Avoided Walls** | Maximum number of wall segments for velocity avoidance. |
| **NavMesh Check Interval** | Defines how often the agents should check their position after moving off NavMesh. |
| **Path Optimization Interval** | Defines how often agents should try to optimize their paths. |
| **Separation Dir Clamp** | Clamp the separation force to the left or right when the neighbor is behind the agent (that is, when the dot product between the agent's facing direction and the direction of the neighbor is less than this threshold value).  This can be any value between -1 (no effect) and 1 (applies all the time), but is typically set to a value of 0 or below.  The effect is that the agent will try to give a way to the agents coming from behind. To tune the behavior, change this value gradually from -1 towards 1. 0 means that to avoid neighbor agents strictly behind. |
| **Path Offset Radius Multiplier** | Agent radius multiplier for offsetting paths around corners. |
| **Resolve Collisions** | Defines whether crowd simulation should resolve collisions between agents.  If not, this will be handled by their movement components. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Crowd Manager](/documentation/en-us/unreal-engine/crowd-manager-settings-in-the-the-unreal-engine-project-settings?application_version=5.7#crowdmanager)
* [Config](/documentation/en-us/unreal-engine/crowd-manager-settings-in-the-the-unreal-engine-project-settings?application_version=5.7#config)
