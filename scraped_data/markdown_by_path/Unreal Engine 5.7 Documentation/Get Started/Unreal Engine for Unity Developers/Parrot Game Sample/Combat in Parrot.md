<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/combat-in-parrot-for-unreal-engine?application_version=5.7 -->

# Combat in Parrot

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for Unity Developers](/documentation/en-us/unreal-engine/unreal-engine-for-unity-developers "Unreal Engine for Unity Developers")
7. [Parrot Game Sample](/documentation/en-us/unreal-engine/parrot-game-sample-for-unreal-engine "Parrot Game Sample")
8. Combat in Parrot

# Combat in Parrot

How combat works in the Parrot game.

![Combat in Parrot](https://dev.epicgames.com/community/api/documentation/image/2bab56e8-1600-4e26-bea8-474878ba31ae?resizing_type=fill&width=1920&height=335)

 On this page

## Combat

Combat is less of a discrete system and more of an abstract one - It is the complex interaction of several different systems working together, and the complexity of the implementation is heavily dependent on the complexity of the design.

In our game, the scope of the design is very simple. The player has one means of attack - jumping on top of an enemy. Enemies have two different ways to attack the player - melee and contact, depending on the enemy type.

For the player’s attack and the enemy melee attack, the fundamentals are almost exactly the same. We have one or more hitboxes placed on the skeletal mesh of the character based on how they can melee attack, along with one or more hurtboxes to approximate the area we want to be hit-testable.

For the enemy contact attack, we use the enemy’s capsule collider to check if the player has come into contact with them and perform the same hit actions we do for melee. You can see the implementation of what occurs when a character is hit in our character base class, found here: `Parrot\Source\Parrot\Public\Character\ParrotCharacterBase.h`. The functional logic is contained here and in the subclasses `ParrotPlayerCharacter.h` and `ParrotEnemyCharacterBase.h`.

#### The Player Character

The setup for the player is unique in how it functions when attacking an enemy. When the player overlaps with an enemy’s hurtbox, the enemy relays this information to the player to ask if the attack was valid. In this case, it checks if the player is above the top of the hurtbox to ensure the player is landing on top and not hitting from the sides or below. If the attack is valid, the enemy cues the player to perform a jump. If the player is still holding the jump button when they make contact with the hurtbox, they will jump higher. Releasing before making contact with the hurtbox will result in a lower jump.

#### The Enemy Character

The setup for the enemy is a bit more complicated for a few reasons. We want the melee attacks to seem realistic, so the enemy hurtboxes are placed on the edge of their weapons. The hitbox(es), hurtbox(es), and capsule collider setup can be seen in the viewport of an enemy character blueprint, such as the one found here: `Blueprints > Enemy > Skeleton > BP_EnemyCharacter_Skeleton`.

[![Parrot game enemy hitbox, hurtbox, and capsule collider.](https://dev.epicgames.com/community/api/documentation/image/7cab07cd-ef74-404a-ad7b-62582e6b3e17?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7cab07cd-ef74-404a-ad7b-62582e6b3e17?resizing_type=fit)

In this example, you can see the hurtbox on the head, the hitbox on the weapon, and the capsule collider. Each of these triggers drive their overlap events to parent functions in the character base class.

In addition, the attack animations send notify events that only enable the weapon hitbox(es) during the portion of the animation when the weapon is being swung. This way, it looks and feels like the player is actually being hit by the weapon, not just coming into contact with an enemy and taking damage at any random time. These **animation notifies** are inserted in the attack animation at specific points to trigger the hurtbox to be enabled, then disabled. You can see the animation notifies in `Blueprints > Enemy/EnemyBase > BP_AnimNotify_EnemyAttackBegin` and `Blueprints > Enemy > EnemyBase > BP_AnimNotify_EnemyAttackEnd` with the setup in the attack animation of a specific enemy character, such as `Assets> Quaternius > PirateKit > Characters > Headless_Skeleton > Animations > Characters_Skeleton_Headless_Anim_CharacterArmature_Sword`.

The enemy character is the one that checks for overlaps and triggers events - this means that the enemy triggers both its own `HitCharacter()` and the player’s `HitCharacter()` functions when appropriate overlaps are detected.

You can see the code that actions on hitbox and hurtbox overlaps here: `Parrot\Source\Parrot\Public\Character\ParrotEnemyCharacterBase.h` in the functions `HitBeginOverlap()` and `HurtBeginOverlap()`.

#### Boss Combat

For our boss fight, there is additional functionality when the boss is hit by the player in order to play a ‘rage’ sequence. You can view the blueprint code that triggers a boss response here:  `Blueprints > Enemy > BossShark > BP_EnemyCharacter_BossShark`.

The ‘rage’ sequence is a simple timed sequence that plays a telegraphed “shake head” animation before increasing the boss walk speed and enabling a green flame niagara component for VFX. During this sequence, it also disables the hurtbox so the boss is invincible.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Combat](/documentation/en-us/unreal-engine/combat-in-parrot-for-unreal-engine?application_version=5.7#combat)
* [The Player Character](/documentation/en-us/unreal-engine/combat-in-parrot-for-unreal-engine?application_version=5.7#theplayercharacter)
* [The Enemy Character](/documentation/en-us/unreal-engine/combat-in-parrot-for-unreal-engine?application_version=5.7#theenemycharacter)
* [Boss Combat](/documentation/en-us/unreal-engine/combat-in-parrot-for-unreal-engine?application_version=5.7#bosscombat)
