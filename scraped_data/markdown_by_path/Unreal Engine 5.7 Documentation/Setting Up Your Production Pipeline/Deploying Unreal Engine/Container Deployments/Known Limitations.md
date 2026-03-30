<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/known-limitations-of-containers-in-unreal-engine?application_version=5.7 -->

# Known Limitations

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
6. [Deploying Unreal Engine](/documentation/en-us/unreal-engine/deploying-unreal-engine "Deploying Unreal Engine")
7. [Container Deployments](/documentation/en-us/unreal-engine/container-deployments-and-images-for-unreal-editor-and-unreal-engine "Container Deployments")
8. Known Limitations

# Known Limitations

Known limitations of container support in Unreal Engine.

![Known Limitations](https://dev.epicgames.com/community/api/documentation/image/4c820e8f-e3f4-43dd-9f26-298590437303?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

Official support for containers in Unreal Engine is still in Beta and is subject to a number of limitations.

## Windows Development Images

The container images that are included with Unreal Engine currently only include Linux development images and not Windows development images. This is due to both technical and legal limitations that currently prevent us from distributing Windows development images.

For a discussion on the technical issues that affect Windows development images, see the blog post [Preview the future of the ue4-docker project](https://adamrehn.com/articles/preview-the-future-of-ue4-docker/) by Adam Rehn.

## Support for AMD GPUs in Container-Based Pixel Streaming

Windows runtime images that support [Pixel Streaming](/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine) support GPU acceleration with both NVIDIA and AMD GPUs. Linux images only support NVIDIA GPUs, but support for AMD GPUs is planned for a future release.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [container](https://dev.epicgames.com/community/search?query=container)
* [containers](https://dev.epicgames.com/community/search?query=containers)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Windows Development Images](/documentation/en-us/unreal-engine/known-limitations-of-containers-in-unreal-engine?application_version=5.7#windowsdevelopmentimages)
* [Support for AMD GPUs in Container-Based Pixel Streaming](/documentation/en-us/unreal-engine/known-limitations-of-containers-in-unreal-engine?application_version=5.7#supportforamdgpusincontainer-basedpixelstreaming)
