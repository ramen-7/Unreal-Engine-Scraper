<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/python-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Python

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
7. [Plugins Settings](/documentation/en-us/unreal-engine/plugins-section-of-the-unreal-engine-project-settings "Plugins Settings")
8. Python

# Python

Reference for the Python section of the Unreal Engine Project Settings.

![Python](https://dev.epicgames.com/community/api/documentation/image/f5f6735d-11e9-4551-87dd-ac1dd2851e48?resizing_type=fill&width=1920&height=335)

 On this page

## Python

### Python

| **Setting** | **Description** |
| --- | --- |
| **Startup Scripts** | Array of Python scripts to run at startup. These run before the first Tick after the Engine initializes. |
| **Additional Paths** | Array of additional paths to add to the Python system paths. |
| **Isolate Interpreter Environment** | Defines whether the embedded interpreter should run in isolation mode.  In isolation, the standard `PYTHON*` environment variables (`PYTHONPATH`, `PYTHONHOME`, and so on), the script's directory and the user's site-packages directory are ignored by the interpreter.  Enabling this prevents the Engine from crashing because of incompatible software.  Consider disabling this option if you tightly control your Python environment and you're sure everything is compatible.  The `UE_PYTHONPATH` environment variable is added to `sys.path` whether the interpreter runs in isolation mode or not. |
| **Advanced** |  |
| **Developer Mode (all users)** | Defines whether Developer Mode should be enabled on the Python interpreter for all users of the project.  Setting Developer Mode in the Project Settings will only enable Developer Mode and Python development for this particular project. Enabling Developer Mode in the Editor Preferences will enable developer mode for Python development across all projects that are opened with the editor.  Enabling developer mode has an extra cost at boot time associated with generating the Python stub file, because this file is generated every time you restart the editor. If you don't always develop with Python, enable this setting per project.  This setting also enables extra warnings (for example, for deprecated code) and stub code generation for use with external IDEs. |

### Python Remote Execution

| **Setting** | **Description** |
| --- | --- |
| **Enable Remote Execution** | Defines whether remote Python execution should be enabled. |
| **Advanced** |  |
| **Multicast Group Endpoint** | The multicast group endpoint (in the form of `IP_ADDRESS:PORT_NUMBER` that the UDP multicast socket should join). |
| **Multicast Bind Address** | The adapter address that the UDP multicast socket should bind to, or `0.0.0.0` to bind to all adapters. |
| **Send Buffer Size** | Size of the send buffer for the remote endpoint connection. |
| **Receive Buffer Size** | Size of the receive buffer for the remote endpoint connection. |
| **Multicast Time-To-Live** | The TTL that the UDP multicast socket should use (`0` is limited to the local host, `1` is limited to the local subnet). |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Python](/documentation/en-us/unreal-engine/python-settings-in-the-unreal-engine-project-settings?application_version=5.7#python)
* [Python](/documentation/en-us/unreal-engine/python-settings-in-the-unreal-engine-project-settings?application_version=5.7#python-2)
* [Python Remote Execution](/documentation/en-us/unreal-engine/python-settings-in-the-unreal-engine-project-settings?application_version=5.7#pythonremoteexecution)
