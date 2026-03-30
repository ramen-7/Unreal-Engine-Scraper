<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/python-scripting?application_version=5.7 -->

# Python Scripting

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine "Live Link")
8. [Live Link Hub](/documentation/en-us/unreal-engine/live-link-hub-in-unreal-engine "Live Link Hub")
9. [Capture Manager](/documentation/en-us/unreal-engine/capture-manager "Capture Manager")
10. Python Scripting

# Python Scripting

Use the Python API and example scripts to automate Capture Manager.

![Python Scripting](https://dev.epicgames.com/community/api/documentation/image/f57aa447-e947-47e3-a8e6-43b3b0fb61f3?resizing_type=fill&width=1920&height=335)

 On this page

The download and ingest of takes using **Capture Manager** can be automated as part of a performance capture workflow with the Python API. The Capture Manager plugin includes a number of example scripts that can be used as a reference and modified to suit your specific requirements. Python scripts should be executed using the **LiveLinkHub** executable.

Use forward slashes `/`(instead of `\`) for paths that appear in a command to avoid problems with character parsing.

## Download Takes

An example script for downloading data from a **Live Link Face** device is provided in the plugin. This can be used as a reference, and modified to suit your specific requirements. It can be found in the following location:

`\Engine\Plugins\VirtualProduction\CaptureManager\CaptureManagerApp\Content\Python\examples\live_link_face_download_only.py`

The script can be run from a Windows terminal (such as PowerShell) using the following command, with the `ip-address` parameter updated for your environment:

Command Line

```
LiveLinkHub.exe -ExecutePythonScript="<path-to-ue-installation>/Engine/Plugins/VirtualProduction/CaptureManager/CaptureManagerApp/Content/Python/examples/live_link_face_download_only.py --ip-address <ip-address>"
```

LiveLinkHub.exe -ExecutePythonScript="<path-to-ue-installation>/Engine/Plugins/VirtualProduction/CaptureManager/CaptureManagerApp/Content/Python/examples/live\_link\_face\_download\_only.py --ip-address <ip-address>"

Copy full snippet(1 line long)

## Ingest Takes

Several example scripts are provided to demonstrate ingesting data from [Mono Video](https://dev.epicgames.com/documentation/en-us/unreal-engine/mono-video-device), [Live Link Face](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-face-device), and [Take Archive](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-archive-device) devices. These can be used as a reference and modified to suit your specific requirements. They can be found in the following folder:

`\Engine\Plugins\VirtualProduction\CaptureManager\CaptureManagerApp\Content\Python\examples\`

These scripts can be run from a Windows terminal (such as PowerShell) using the following command as a template. You will need to update the `path-to-takes` parameter for your environment:

Command Line

```
LiveLinkHub.exe -ExecutePythonScript="<path-to-ue-installation>/Engine/Plugins/VirtualProduction/CaptureManager/CaptureManagerApp/Content/Python/examples/take_archive_ingest.py --archive-path <path-to-takes>"
```

LiveLinkHub.exe -ExecutePythonScript="<path-to-ue-installation>/Engine/Plugins/VirtualProduction/CaptureManager/CaptureManagerApp/Content/Python/examples/take\_archive\_ingest.py --archive-path <path-to-takes>"

Copy full snippet(1 line long)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Download Takes](/documentation/en-us/unreal-engine/python-scripting?application_version=5.7#downloadtakes)
* [Ingest Takes](/documentation/en-us/unreal-engine/python-scripting?application_version=5.7#ingesttakes)
