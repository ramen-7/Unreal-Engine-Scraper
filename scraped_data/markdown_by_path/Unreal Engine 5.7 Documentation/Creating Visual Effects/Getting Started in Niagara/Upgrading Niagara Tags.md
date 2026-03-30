<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/upgrading-niagara-tags-in-unreal-engine?application_version=5.7 -->

# Upgrading Niagara Tags

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Getting Started in Niagara](/documentation/en-us/unreal-engine/getting-started-in-niagara-effects-for-unreal-engine "Getting Started in Niagara")
7. Upgrading Niagara Tags

# Upgrading Niagara Tags

A short overview of upgrading existing Niagara systems and emitters to use the new Tagged Asset Browser Configuration assets.

[![The Tagged Asset Browser](https://dev.epicgames.com/community/api/documentation/image/ab1ed11d-63d7-45cc-b7be-7568ec3f57ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab1ed11d-63d7-45cc-b7be-7568ec3f57ff?resizing_type=fit)

[![Comparing tags in an asset to tags in the Asset Browser](https://dev.epicgames.com/community/api/documentation/image/560b9418-f8ca-42e5-b6bc-61c09573bd9b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/560b9418-f8ca-42e5-b6bc-61c09573bd9b?resizing_type=fit)

The update of the **Niagara Asset Browser** with the release of Unreal Engine 5.7 means you need to upgrade existing Niagara systems and emitters that use Niagara asset tags to use the new **Tagged Asset Browser Configuration** assets.

For projects that make use of Niagara Asset Tags, we advise resaving existing Niagara systems and emitters. Tags will automatically transfer to the new User Asset Tag system once loaded.

If you defined your own tags in a now-deprecated **Niagara Asset Tag Definition** asset, we added a new context action. This action finds all Niagara assets containing the tags defined inside, and asks you to resave them.

[![New context action to migrate tagged assets to user asset tags.](https://dev.epicgames.com/community/api/documentation/image/09f784d2-96bc-4949-9835-bf65bef77354?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/09f784d2-96bc-4949-9835-bf65bef77354?resizing_type=fit)

For internal tags defined in C++, you can navigate to the folders with the assets you want to update, and use the console command `fx.Niagara.MigrateInternalTagsToUserAssetTags`.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
