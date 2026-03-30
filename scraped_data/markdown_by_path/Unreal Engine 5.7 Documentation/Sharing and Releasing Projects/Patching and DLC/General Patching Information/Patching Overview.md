<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release?application_version=5.7 -->

# Patching Overview

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [Patching and DLC](/documentation/en-us/unreal-engine/patching-content-delivery-and-dlc-in-unreal-engine "Patching and DLC")
7. [General Patching Information](/documentation/en-us/unreal-engine/general-patching-information-in-unreal-engine "General Patching Information")
8. Patching Overview

# Patching Overview

Creating updated content packages for updating your project after release.

![Patching Overview](https://dev.epicgames.com/community/api/documentation/image/1713deef-3e87-43c7-b136-a766f5a5cd00?resizing_type=fill&width=1920&height=335)

 On this page

Once you have released your project, you will probably make updates to it after the initial release. This process is known as **patching**. Patching usually includes new content that addresses known issues, or that fixes vulnerabilities in the original release.

## Different Methods for Patching

There are several methods for creating patches, but they all use one of two approaches. One approach keeps files from the original release or previous patches, but adds a pointer to new content. The other approach is to transform the content in the original build using a binary patch.

You can build patches in **Unreal Engine** (UE) for many different platforms. However, it does not support distribution of patches for your project. Each platform has their own system for uploading patch files, and for distributing those patch files to users. For information on these platform-specific distribution systems, see the documentation for that platform's **Software Development Kit (SDK)**.

## Platform-Agnostic Patching Method

There is a method for creating patches in Unreal Engine that will technically work on any platform. This method packages the entire build with new content, while the changes between the two builds are placed in a sidecar file that is added to the original file. The new **PAK** file is labeled with a `_p` suffix. For example, if the original build file is called `MyGamesStuff.pak`, your patch file would be called `MyGamesStuff_p.pak`.

### Windows Patching

Windows uses the method described in [Platform-Agnostic Patching Method](/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release#platform-agnosticpatchingmethod) .

For more information on platform-agnostic patching, see [How to Create a Patch](/documentation/en-us/unreal-engine/how-to-create-a-patch-in-unreal-engine).

* [patching](https://dev.epicgames.com/community/search?query=patching)
* [distribution](https://dev.epicgames.com/community/search?query=distribution)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Different Methods for Patching](/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release?application_version=5.7#differentmethodsforpatching)
* [Platform-Agnostic Patching Method](/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release?application_version=5.7#platform-agnosticpatchingmethod)
* [Windows Patching](/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release?application_version=5.7#windowspatching)
