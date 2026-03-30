<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/walkable-slope-in-unreal-engine?application_version=5.7 -->

# Walkable Slope

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. Walkable Slope

# Walkable Slope

What the Walkable Slope Override is and the situations you may want to use it in.

![Walkable Slope](https://dev.epicgames.com/community/api/documentation/image/fae878eb-34f0-4237-b744-7704a6543464?resizing_type=fill&width=1920&height=335)

 On this page

The **Walkable Slope Override** on **Physics Bodies** enables you to tweak what surfaces **Characters** can walk up. Perhaps a staircase is too steep or maybe you want to enforce the "no walking on the grass" signs, these settings will enable you to do so.

## Usage

The **Character Movement Component** has a property called **Walkable Floor Angle**. It defaults to around 45 degrees. So, when the Character attempts to move across a surface that is angled higher than this, the Character will not be able to climb the incline or will lose their footing and slide down it.

Depending on the editor you are in, or if you are looking at an Actor in the level, you will find a property, or expandable grouping of properties, prefixed with **Override Walkable Slope**. Here you can set the **Walkable Slope Behavior** and **Walkable Slope Angle**.

![Override Walkable Slope](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b035d1c-a93f-4ee9-a86b-a49ea6bbc696/walkable-properties.png)

### Increase Walkable Slope

This setting will increase the walkable slope of a **Physics Body** up to the value listed in the **Walkable Slope Angle** property. If **Walkable Slope Angle** is set to 75, and the angle of the surface of the **Physics Body** is 65, the Character will be able to walk up to it, regardless of the Character's **Walkable Floor Angle**.

While **Walkable Slope Behavior** is set to "Increase Walkable Slope":

* A value of 0.0 in the **Walkable Slope Angle** is essentially the same as **No Change** in the **Walkable Slope Behavior** property.
* A value of 90.0 in the **Walkable Slope Angle** will allow the character to traverse any angle on the Physics Body up to (but not including) 90 degrees.

### Decrease Walkable Slope

This setting will "cap" the walkable slope of a **Physics Body** to the value listed in the **Walkable Slope Angle** property. If **Walkable Slope Angle** is set to 25, and the angle of the surface of the **Physics Body** is 35 degrees, the Character will be unable to walk up to it regardless of the Character's **Walkable Floor Angle**.

While **Walkable Slope Behavior** is set to "Decrease Walkable Slope":

* A value of 0.0 in the **Walkable Slope Angle** will result in the Character being unable to walk across the **Physics Body** surface. This can result in some odd behavior for mostly flat surfaces, as the character will skate across them but will not be able to change direction.
* A value of 90.0 in the **Walkable Slope Angle** is essentially the same as **No Change** in the **Walkable Slope Behavior** property.

## Examples

|  |  |
| --- | --- |
| The blue angle is the default Character Movement Component Walkable Floor Angle and the green represents the new Increased Walkable Slope angle | The blue angle is the default Character Movement Component Walkable Floor Angle and the red represents the new Decreased Walkable Slope angle |
| The blue angle is the default **Character Movement Component Walkable Floor Angle**, while the green represents the new **Increased Walkable Slope** angle. | The blue angle is the default **Character Movement Component Walkable Floor Angle**, while the red represents the new **Decreased Walkable Slope** angle. |

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [slope](https://dev.epicgames.com/community/search?query=slope)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Usage](/documentation/en-us/unreal-engine/walkable-slope-in-unreal-engine?application_version=5.7#usage)
* [Increase Walkable Slope](/documentation/en-us/unreal-engine/walkable-slope-in-unreal-engine?application_version=5.7#increasewalkableslope)
* [Decrease Walkable Slope](/documentation/en-us/unreal-engine/walkable-slope-in-unreal-engine?application_version=5.7#decreasewalkableslope)
* [Examples](/documentation/en-us/unreal-engine/walkable-slope-in-unreal-engine?application_version=5.7#examples)
