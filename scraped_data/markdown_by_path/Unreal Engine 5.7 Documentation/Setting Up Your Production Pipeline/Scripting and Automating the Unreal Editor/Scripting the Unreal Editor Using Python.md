<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7 -->

# Scripting the Unreal Editor Using Python

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
6. [Scripting and Automating the Unreal Editor](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor "Scripting and Automating the Unreal Editor")
7. Scripting the Unreal Editor Using Python

# Scripting the Unreal Editor Using Python

Describes how to use Python in the Unreal Editor to script content production tasks.

![Scripting the Unreal Editor Using Python](https://dev.epicgames.com/community/api/documentation/image/21654914-b0a3-4b97-9b1a-14b6065d00dc?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

This page describes how to get started using Python in the Unreal Editor.

## Why Python?

In recent years, Python has become the de facto language for production pipelines and interoperability between 3D applications, particularly in the media and entertainment industry. This is partially due to the wide range of applications that support it. As the complexity of production pipelines continues to soar, and the number of applications involved continues to grow, having a common scripting language makes it easier to create and maintain large-scale asset management systems.

Even without these outside considerations, or the need to work with other applications, Python is a great choice if you're looking to automate your workflows within the Unreal Editor. It's relatively easy for those new to programming to get started, it offers the ability to create complex and full-featured user interfaces through modules like PySide, and there are many other useful free modules available to the community to make your life easier.

You can use Python in the Unreal Editor to do things like:

* Construct larger-scale asset management pipelines or workflows that tie the Unreal Editor to other 3D applications that you use in your organization.
* Automate time-consuming Asset management tasks in the Unreal Editor, like generating Levels of Detail (LODs) for Static Meshes.
* Procedurally lay out content in a Level.
* Control the Unreal Editor from UIs that you create yourself in Python.

## Set Up Your Project to Use Python

Python support in the Unreal Editor is provided by the **Python Editor Script Plugin**. You'll need to enable this plugin for your current Project before you can run Python scripts in the Editor.

Currently, you must enable the plugin separately for each Project.

To enable the plugin:

1. Open your Project, and choose **Edit > Plugins** from the main menu.
2. In the **Plugins** window, go to the **Scripting** section.  
   Find the **Python Editor Script Plugin** in the right-hand panel, and check its **Enabled** box.

   [![Enable the Python Editor Script Plugin](https://dev.epicgames.com/community/api/documentation/image/794a8f66-42e3-4bbb-b9f6-1332e527cbae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/794a8f66-42e3-4bbb-b9f6-1332e527cbae?resizing_type=fit)

   You'll also want to enable the **Editor Scripting Utilities** plugin, which offers simplified APIs for many common Editor tasks. For details, see [Scripting and Automating the Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor).
3. Restart the Editor.

### Python 3.11.8

The Python Editor Script Plugin contains an embedded version of Python 3.11.8.

This means that you don't have to install Python separately on your computer.

Unreal uses Python 3.11.8 by default because it is an important part of the current [VFX Reference Platform](https://www.vfxplatform.com/).
To use a different version of Python, you can set the `UE_PYTHON_DIR` environment variable in your operating system to point to the installation you want to embed, then [rebuild the Unreal Engine from source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).

## Ways to Run Python Code in Unreal Editor

There are several different ways that you can run Python scripts in the Unreal Editor, each designed for a slightly different usage scenario. You can choose whichever fits your needs.

Unlike Blueprints, the Python environment is only available **in the Unreal Editor**, not when your Project is running in the Unreal Engine in any mode, including Play In Editor, Standalone Game, cooked executable, etc. That means that you can use Python freely for scripting and automating the Editor or building asset production pipelines, but you cannot currently use it as a gameplay scripting language.

### The Python Console in the Output Log

You can switch the Unreal Editor's console input bar to accept Python code instead of Unreal console commands.

[![The Python console](https://dev.epicgames.com/community/api/documentation/image/7f38bcfb-b04c-4095-987f-1140b65435e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7f38bcfb-b04c-4095-987f-1140b65435e1?resizing_type=fit)

You can do this in the **Output Log** panel, as shown above, or when you bring up the console input bar by pressing the `~` key.

When the console is in Python mode:

* You can enter lines of Python code into this console and have the Editor execute each one immediately, exactly as if you were using an interactive Python console in a command window. This is the only way to execute Python code line-by-line; all other approaches listed below run a script file that you specify.
* You can run multiple lines of code at a time by using **Shift+Enter** to separate each line, or by pasting in a multi-line block that you copy from a text editor.
* You can execute Python script files by simply typing the file name into the console. If your Python script requires additional command-line arguments, include them after the name of your script.

Output from the built-in Python `print` function is also redirected to the **Output Log** panel.

### The py Console Command

With the console in Cmd mode, you can use the `py` command to run the rest of the line as Python code, exactly as if you had typed it into the Python console described above.

For example, this command runs the specified script file:

Command Line

C++

```
py "C:\MyScripts\my_script.py"
```

py "C:\MyScripts\my\_script.py"

Copy full snippet(1 line long)

We don't recommend running this command in the value of the `ExecCmd` command-line parameter when you start the Editor. This can cause your script to run before the Editor environment is ready — for example, before the startup Level is fully loaded. See the sections below for better options.

### The File Menu

The **File** menu in the main window of the Unreal Editor offers new options that you can use to run Python script files.

* Use **Execute Python Script** if you want to browse to a new script file on your computer that you haven't run before.
* Use the **Recent Python scripts** list to re-run any script that you ran previously. The file is read from disk again, so you changed the script in the meantime, your new version is run.

[![Execute Python from the File menu](https://dev.epicgames.com/community/api/documentation/image/b939802f-59ac-4b68-85e1-4fe3ffe12936?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b939802f-59ac-4b68-85e1-4fe3ffe12936?resizing_type=fit)

### The Command Line

If you start the Unreal Editor from the command line or from a script, you can specify a Python script file in the command line arguments. If your Python script requires additional command-line arguments, include them after the name of your script.

There are two different ways to run a Python script from the command line. In both approaches, the Editor shuts down immediately after running your Python script.

**Option 1: Full Editor**
In this approach, the full Unreal Editor launches, opens your specified Project, loads the default startup level, then runs your Python script once everything is loaded and ready. This approach is good if you need your script to interact with content in your Project or in a Level that can take some time to load.

Add the `ExecutePythonScript` argument to the command line, and set its value to the path and filename of the Python script you want to run. For example:

Command Line

C++

```
> UnrealEditor-Cmd.exe "C:\projects\MyProject.uproject" -ExecutePythonScript="c:\my_script.py"
```

> UnrealEditor-Cmd.exe "C:\projects\MyProject.uproject" -ExecutePythonScript="c:\my\_script.py"

Copy full snippet(1 line long)

The approach above requires that you enable the Editor Scripting Utilities plugin for your Project. You must have already enabled the Python Scripting Plugin in the Unreal Engine Project that you specify on the command line.

**Option 2: Commandlet**
This approach is very fast to execute, and can even run your scripts in headless mode without opening the Editor UI.

Add the following arguments to the command line for `UnrealEditor-Cmd.exe`: `-run=pythonscript -script=<script_file_or_code>`. `<script_file_or_code>` takes either of the following values:

* The path and filename of a Python script that you want to run.
* Python statements and commands that you want to run. If needed, you can use `\n` in the string to escape line breaks.

For example:

Command Line

C++

```
> UnrealEditor-Cmd.exe "C:\projects\MyProject.uproject" -run=pythonscript -script="c:\\my_script.py"
```

> UnrealEditor-Cmd.exe "C:\projects\MyProject.uproject" -run=pythonscript -script="c:\\my\_script.py"

Copy full snippet(1 line long)

or:

Command Line

C++

```
> UnrealEditor-Cmd.exe "C:\projects\MyProject.uproject" -run=pythonscript -script="a=5 \nb=10 \nc=a+b \nf=open('D:\myfile.txt','w+') \nf.write(str(c)) \nf.close()"
```

> UnrealEditor-Cmd.exe "C:\projects\MyProject.uproject" -run=pythonscript -script="a=5 \nb=10 \nc=a+b \nf=open('D:\myfile.txt','w+') \nf.write(str(c)) \nf.close()"

Copy full snippet(1 line long)

This commandlet does not automatically load levels, so when writing your script, add the following line as the first thing it does:

Command Line

C++

```
unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).load_level("/Game/maps/UVlayoutTest.UVlayoutTest")
```

unreal.get\_editor\_subsystem(unreal.LevelEditorSubsystem).load\_level("/Game/maps/UVlayoutTest.UVlayoutTest")

Copy full snippet(1 line long)

You must have already enabled the Python Scripting Plugin in the Unreal Engine Project that you specify on the command line.

### The init\_unreal.py File

If the Editor detects a script file called `init_unreal.py` in any of the paths it is configured to use (see "Python Paths in the Unreal Editor" below), it automatically runs that script immediately.

This is a good approach for situations where you are working on a Project or a Plugin and you know that everyone working with that content needs to run the same initialization code every time the Editor starts up. You could put your initialization code inside a script with this name, and put it into the **Content/Python** folder within that Project or Plugin.

### Startup Scripts

In your Project Settings, you can specify any number of Python scripts that you want to run every time you open that Project. The Editor runs these scripts after the default startup Level is fully loaded.

Select **Edit > Project Settings...**. Under the **Plugins** list, select **Python**. Then, add your scripts to the **Startup scripts** setting:

[![Python startup scripts](https://dev.epicgames.com/community/api/documentation/image/752d670e-09d4-46d1-a8a4-b88540ad6568?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/752d670e-09d4-46d1-a8a4-b88540ad6568?resizing_type=fit)

Restart the Unreal Editor when done. The next time the Editor loads your Project, it should run your new startup scripts.

### From Editor-only Blueprints

The Python Script Plugin exposes new nodes to Blueprint Visual Scripting that you can use to run Python code snippets or files during the evaluation of a Blueprint graph.

Python execution nodes are only available in Editor-only Blueprint classes, such as Editor Utility Widgets and Editor Utility Blueprints. Refer to [Scripting the Editor using Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints). You can't use this method in any Blueprint classes that are available at runtime, such as a class that you derive directly from **Actor**.

You'll find the following nodes in the **Python > Execution** section of the Blueprint palette.

|  |  |  |
| --- | --- | --- |
| [Execute Python Script](https://dev.epicgames.com/community/api/documentation/image/2c9c959c-c253-41be-84f9-3b409820f814?resizing_type=fit) | **Execute Python Script** | Executes the literal Python code that you pass in to or type in the **Python Command** input. It is the recommended way to call Python from Blueprints, and superscedes creating a new BlueprintFunctionLibrary(BPFL) type in Python.   * The aformentioned BPFL method causes issues when an asset is saved or loaded due to Python-generated types being transient, and is no longer officially supported. * **Execute Python Script** can have can have custom input and output pins, which are available as variables within the Python script on the node and can be added by the properties of the node.  -Inputs are set prior to running the **Python script** on the node, and can be read in the script.   -Outputs are read after running the **Python script** on the node, and can be set in the script. * **Execute Python Script** can contain multiple lines of Python code, and new-lines can be entered by using the keys **Shift+Return**. * The **Success?** output is true if the Python code was executed successfully, or false otherwise. If it is false, you can find the errors in the **Output Log**.   This node cannot run files. It can only execute lines of Python code. |
| [Execute Python Command](https://dev.epicgames.com/community/api/documentation/image/8a4b148a-5117-4a5d-922f-b714a3e42c61?resizing_type=fit) | **Execute Python Command** | Executes the literal Python code or file that you pass in to or type in the **Python Script** input. The node will attempt to determine based on your input whether it is literal code or a filename.  -The **Return Value** output is true if the Python code or file was executed successfully, or false otherwise. If it is false, you can find the errors in the **Output Log**. |
| [Execute Python Command Advanced](https://dev.epicgames.com/community/api/documentation/image/9ff8392b-90eb-4b3e-9fc7-496e8bace966?resizing_type=fit) | **Execute Python Command (Advanced)** | Executes the literal Python code or file that you pass in to or type in the **Python Script** input. This node is similar to **Execute Python Command**, but offers some additional inputs and outputs that may be useful in some scenarios.   * **Execution Mode** indicates how you want to interpret the **Python Script** input.    + Select **Execute File** to force the command to treat your input as the name of a file, and to attempt to find and run that file. Any values returned by this script are printed to the log.   + Select **Execute Script** to force the command to treat your input as literal Python code, and to execute it as-is. Any values returned by this script are printed to the log.   + Select **Evaluate Script** to force the command to treat your input as literal Python code, evaluate it as-is, and return any values produced by the script in the **Command Result** output. * If you pass a filename to the **Python Script** input, the **File Execution Scope** determines whether that file is executed in the global scope (**Public**) or in a sandboxed scope (**Private**). If you want the code in your file to be able to access variables, functions, and so on that have already been defined in the Python environment, then you will need to choose **Public**. However, doing so also gives the Python file the ability to redefine variables and functions. This may accidentally cause unexpected behavior. Therefore, it may be safer to use the **Private** scope. * The **Command Result** output depends on the **Execution Mode**. When the **Python Script** input is executed or evaluated successfully, and the **Execution Mode** is **Evaluate Script**, this output returns the value produced by the script. When the **Python Script** input is executed or evaluated successfully, and the **Execution Mode** is either **Execute File** or **Execute Script**, this output returns `None`. When the **Python Script** input is *not* executed or evaluated successfully, this output contains the error information. * The **Log Output** provides access to the full list of messages written to the Python log during the execution of the input script or file. You can iterate through this array if you need to look for specific messages written by the script. * The **Return Value** output is true if the Python code was executed successfully, or false otherwise. If it is false, you can find the errors in the engine's **Output Log**, in the **Log Output** output pin, and in the **Command Result**. |

## Python Environment and Paths in the Unreal Editor

When you use a relative path to run a Python script, or to import another script module using the `import` command in one of your scripts, the script that you run or import can be in any path that is listed in the `sys.path` variable of your Python environment.

The Unreal Editor automatically adds several paths to this `sys.path` list:

* The **Content/Python** sub-folder in your Project's folder.
* The **Content/Python** sub-folder in the main Unreal Engine installation.
* The **Content/Python** sub-folder in each enabled Plugin's folder.
* The **Documents/UnrealEngine/Python** folder inside your user directory. For example, on Windows 10, this is equivalent to `C:/Users/Username/Documents/UnrealEngine/Python`

You can also add your own paths to this list using any of the following approaches:

* In your Project Settings. Select **Edit > Project Settings...**. Under the **Plugins** list, select **Python**. Then, add the paths to the **Additional Paths** setting. Restart the Unreal Editor when done.

  [![Additional Python paths](https://dev.epicgames.com/community/api/documentation/image/4f0fc187-99a8-470f-858d-ae59b327f14e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f0fc187-99a8-470f-858d-ae59b327f14e?resizing_type=fit)
* Add the paths to the value of the `UE_PYTHONPATH` (or `PYTHONPATH` if you disabled the Editor isolated interpreter environment option) environment variable in your operating system, then restart the Unreal Editor.
* Add the paths directly to the `sys.path` list within a Python script, or in the Python console.

For more information, refer to the [Python sys.path documentation](https://docs.python.org/3/library/sys.html#sys.path)

By default, Unreal Engine's embedded Python interpreter runs in isolated mode. You can disable isolated mode by selecting **Edit > Project Settings > Plugins > Python > Isolate Interpreter Environment**

For more information, refer to see the [Python command line -I option documentation](https://docs.python.org/3/using/cmdline.html)

[![Isolate Interpreter Environment](https://dev.epicgames.com/community/api/documentation/image/b9ac84ab-3fdb-4473-8922-09d1325022de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9ac84ab-3fdb-4473-8922-09d1325022de?resizing_type=fit)

The **UE\_PYTHONPATH** environment variable is always parsed by the engine and its content is added to `sys.path`, regardless of the isolation mode options you select. *UE\_PYTHONPATH* serves the same purpose as the *PYTHONPATH* variable, but it should never be modified by any third-party software.

## About the Unreal Editor Python API

The Python Editor Script Plugin exposes a wide range of classes and functions that you can use to interact with the Unreal Editor, the Assets in your Project, and the content in your Levels. This API is all contained in the `unreal` module. To access it, import this module at the beginning of any Python script you run in the Editor's Python environment:

C++

```
import unreal
```

import unreal

Copy full snippet(1 line long)

The `unreal` module exposes nearly everything that is exposed from C++ to Blueprints in your Editor environment. It's not pre-generated; it automatically reflects whatever is available in Blueprints in your Editor. As you enable new plugins in the Unreal Editor, anything those plugins expose to Blueprints also becomes available in Python as well. The same goes for any C++ code that you write in your Project and expose to Blueprints.

The Python API makes every effort to expose native Unreal APIs in a way that is as friendly as possible to Python developers. For example:

* Simple data types are transparently converted back and forth between Python and native types whenever necessary.  
  When you pass in a Python list, set or dict, it is automatically converted to an Unreal array, set, or map. When you retrieve a list, set, or dict returned by an API function, you are actually getting an instance of an Unreal class, but its API is fully consistent with the base Python list, set, or dict type.
* Python classes maintain the same inheritance hierarchy as the native types they represent. That means, for example, that you can use the built-in Python functions `isinstance()` and `type()` to test whether an object derives from or matches a given class.
* The API tries to strike a good balance between the naming conventions used in Unreal for C++ and Blueprints on one hand, and Python naming conventions on the other hand. Classes and objects in the Python API have the same names as they do in Blueprints. This is typically the same as their native types, omitting the prefix (e.g. `U` or `T`). Function and property names are automatically exposed as lower-case `snake_case`. So, for example, you typically call functions like `unreal.StaticMeshActor.get_actor_transform()`. Enumeration value names are automatically exposed as upper-case `SNAKE_CASE`.
* All exposed functions can accept either ordered parameters, or named parameters in any order. For example, the following two function calls are exactly equivalent:

  C++

  ```
  |  |  |
  | --- | --- |
  |  | unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem).join_static_mesh_actors(list_of_actors, my_options) |
  |  | unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem).join_static_mesh_actors(join_options=my_options, actors_to_join=list_of_actors) |
  ```

  unreal.get\_editor\_subsystem(unreal.StaticMeshEditorSubsystem).join\_static\_mesh\_actors(list\_of\_actors, my\_options)
  unreal.get\_editor\_subsystem(unreal.StaticMeshEditorSubsystem).join\_static\_mesh\_actors(join\_options=my\_options, actors\_to\_join=list\_of\_actors)

  Copy full snippet(2 lines long)

### API Reference

For details on all of the classes and functions exposed by the Unreal Python API, see the API Reference here:

[**Unreal Editor Python API Reference**](https://api.unrealengine.com/INT/PythonAPI/)

The API Reference is not an exhaustive list of everything that may be exposed to Python by plugins. If you've installed additional plugins that aren't included in the API Reference, and you need to see the way their scripting features are exposed to Python, you can generate your own local version of the API Reference that contains docs for the plugins you need. For instructions, see the readme file under *Engine\Plugins\Experimental\PythonScriptPlugin\SphinxDocs* in your Unreal Engine installation folder.

## Best Practices for Using the Python API

This section covers a few things that it's important to keep in mind when you use the Python API.

### Working with Assets

If you need to work with Assets in your Project, always use functions from the Unreal Python API to do it. Never use file management modules built in to Python to work directly with your Asset files on disk. For example, if you need to move an Asset to a different folder, do not use Python functions like `os.rename` or `shutil.move`. Unreal Projects and Assets contain internal content references that you can break if you do not respect this rule.

Instead, we recommend using the `unreal.EditorAssetLibrary` API that is provided by the Editor Scripting Utilities plugin, or the `unreal.AssetTools` class built in to the Unreal Python API.

### Changing Editor Properties

You can use Python to get access to Objects in your Project and set up many configuration properties on those Objects programmatically. For example, your Python script could access Static Mesh Actors in the current Level, and set properties like whether the Actors can be damaged, or whether they should be hidden in the game. Or, you could retrieve their Static Mesh Components and set up properties on those Components, like their Lightmass settings, or even the Static Mesh Asset that they are linked to.

These properties may be exposed to Python in two different ways:

* Items with the BlueprintReadOnly or BlueprintReadWrite flag are exposed as simple properties on the object.  
  You can read and modify these properties like you access any Python object property.
* Items with the ViewAnywhere or EditAnywhere flag are exposed as "editor properties".  
  You can read and write these values using a special pair of functions exposed by every object: `set_editor_property()` and `get_editor_property()`.

In the API Reference for each class, you'll find a list of **Editor Properties** immediately following the class description. These are all the values that you can set and get using these `set_editor_property()` and `get_editor_property()` functions. Whenever you need to set or get a configuration property on an object, check this list first to see if the property you want is listed there.

* When you need to read a value that is exposed both as an object property and as an editor property, the result of accessing the property directly is usually the same as by calling the `get_editor_property()` function. However, the `get_editor_property()` function often has access to properties that aren't exposed directly on the Python object.
* When you need to set a value that is exposed both as an object property and as an editor property, you should in most cases use the `set_editor_property()` function to set the value rather than set the value directly on the object. When you adjust properties in the UI, the Editor often performs additional operations behind the scenes: pre- and post-edit changes. These operations typically respond to the choices you make in some way, and keep the Editor UI in sync with the state of the object in the game world. If you modify these properties directly on the Python object, this Editor code won't be run automatically. On the other hand, when you call `set_editor_property()` to set the state of a property, you do trigger this pre- and post-edit code, exactly as if you changed the setting in the **Details** panel of the Editor UI.

For example, Media Player objects have a **Play on Open** setting:

[![Details](https://dev.epicgames.com/community/api/documentation/image/fb0d6ddf-68ae-44f7-9b34-ec9794c5ffe0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb0d6ddf-68ae-44f7-9b34-ec9794c5ffe0?resizing_type=fit)

This is exposed in the `unreal.MediaPlayer` class in the `play_on_open` class member:

C++

```
import unreal
		obj = unreal.MediaPlayer()
		# Modifying a property directly can have different results
		# than changing settings in the Editor UI.
		# Generally you'll want to avoid setting these values directly, like this:
		obj.play_on_open = True
		# This way of accessing the property will have exactly the same
		# result as changing the setting in the Editor UI:
		obj.set_editor_property("play_on_open", True)
		# Both ways of reading the value are equivalent.
```

Expand code  Copy full snippet(13 lines long)

### Use Unreal Types Whenever Possible

Whenever you need utilities that are available in the Unreal Python API, like classes for math operations or manipulating 3D coordinates, we recommend using the Unreal utilities rather than using your own implementations. The Unreal versions are optimized for best performance in the Engine environment.

For example, when you need to manipulate coordinates in 3D space, use the `unreal.Vector` class:

C++

```
|  |  |
| --- | --- |
|  | import unreal |
|  | v1 = unreal.Vector() |
|  | v1.x = 10 |
|  | v2 = unreal.Vector(10, 20, 30) |
|  | v3 = (v1 + v2) * 2 |
|  | print(v3) |
```

import unreal
v1 = unreal.Vector()
v1.x = 10
v2 = unreal.Vector(10, 20, 30)
v3 = (v1 + v2) \* 2
print(v3)

Copy full snippet(6 lines long)

### Logging and Feedback

The `unreal` object exposes functions that you can use in your code to send log, warning, and error messages through the same messaging system used by all Engine and Editor subsystems. We recommend using this standardized logging framework anytime your script needs to send a message to the user.

* Use `unreal.log()` for information messages. For your convenience, the Python `print()` function has also been implemented to pass through `unreal.log()` internally.
* Use `unreal.log_warning()` to alert users of potential problems.
* Use `unreal.log_error()` for severe problems that prevent your script from running as expected.

Your messages appear in the **Output Log** panel, along with the messages sent by other subsystems:

[![Python log messages](https://dev.epicgames.com/community/api/documentation/image/9a70d2d3-eea8-4011-9ec3-41f63ae7d686?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a70d2d3-eea8-4011-9ec3-41f63ae7d686?resizing_type=fit)

### Supporting Undo and Redo

Your scripts can take full advantage of the Undo / Redo system built in to the Unreal Editor.

Each *transaction* that you define can contain any number of Python operations. Using these transactions, you can bundle large operations, or operations on many different objects, together into a single entry in the Undo / Redo history. Typically, if your script intends to perform a certain change on multiple objects, you don't want a separate entry in the Undo / Redo history for each change; you want one entry that will undo all changes to all objects.

To define a transaction, use the `unreal.ScopedEditorTransaction` scope. For example, if you run this code:

C++

```
|  |  |
| --- | --- |
|  | import unreal |
|  | obj = unreal.MediaPlayer() |
|  | with unreal.ScopedEditorTransaction("My Transaction Test") as trans: |
|  | obj.set_editor_property("play_on_open", False) |
|  | obj.set_editor_property("vertical_field_of_view", 80) |
```

import unreal
obj = unreal.MediaPlayer()
with unreal.ScopedEditorTransaction("My Transaction Test") as trans:
obj.set\_editor\_property("play\_on\_open", False)
obj.set\_editor\_property("vertical\_field\_of\_view", 80)

Copy full snippet(5 lines long)

Your Editor's **Undo History** panel now lists that transaction by name:

[![Undo History](https://dev.epicgames.com/community/api/documentation/image/d8cad124-79c5-4b56-847c-a5cc12950909?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d8cad124-79c5-4b56-847c-a5cc12950909?resizing_type=fit)

As a general rule, your scoped transactions can contain any operations that are also undoable in the Editor UI. However, not every Editor operation is undoable. For example, you can't undo importing a model in the Editor UI, so trying to import a model inside an `unreal.ScopedEditorTransaction` will not work as you may be expecting.

### Progress Dialogs for Slow Operations

If your scripts need to work on many Assets or Actors in the same operation, they may take some time to complete. However, while the Unreal Editor is running a Python script, its UI becomes blocked to other user interactions. To give the user information about the progress of a large task, and avoid the Editor appearing to freeze or hang, you can use the `unreal.ScopedSlowTask` scope.

For example:

C++

```
import unreal
    total_frames = 100
    text_label = "Working!"
    with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
        slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already
        for i in range(total_frames):
            if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
                break
            slow_task.enter_progress_frame(1)     # Advance progress by one frame.
                                                # You can also update the dialog text in this call, if you want.
```

Expand code  Copy full snippet(11 lines long)

[![Progress bar for a Scoped Slow Task](https://dev.epicgames.com/community/api/documentation/image/8679346a-9ad2-467f-ae8f-69a1aadca711?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8679346a-9ad2-467f-ae8f-69a1aadca711?resizing_type=fit)

* [editor](https://dev.epicgames.com/community/search?query=editor)
* [python](https://dev.epicgames.com/community/search?query=python)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [overview](https://dev.epicgames.com/community/search?query=overview)
* [landing page](https://dev.epicgames.com/community/search?query=landing%20page)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [scripting](https://dev.epicgames.com/community/search?query=scripting)
* [landing](https://dev.epicgames.com/community/search?query=landing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Why Python?](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#why-python)
* [Set Up Your Project to Use Python](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#set-up-your-project-to-use-python)
* [Python 3.11.8](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#python-3-11-8)
* [Ways to Run Python Code in Unreal Editor](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#ways-to-run-python-code-in-unreal-editor)
* [The Python Console in the Output Log](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#the-python-console-in-the-output-log)
* [The py Console Command](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#the-py-console-command)
* [The File Menu](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#the-file-menu)
* [The Command Line](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#the-command-line)
* [The init\_unreal.py File](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#the-init-unreal-py-file)
* [Startup Scripts](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#startup-scripts)
* [From Editor-only Blueprints](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#from-editor-only-blueprints)
* [Python Environment and Paths in the Unreal Editor](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#python-environment-and-paths-in-the-unreal-editor)
* [About the Unreal Editor Python API](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#about-the-unreal-editor-python-api)
* [API Reference](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#api-reference)
* [Best Practices for Using the Python API](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#best-practices-for-using-the-python-api)
* [Working with Assets](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#working-with-assets)
* [Changing Editor Properties](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#changing-editor-properties)
* [Use Unreal Types Whenever Possible](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#use-unreal-types-whenever-possible)
* [Logging and Feedback](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#logging-and-feedback)
* [Supporting Undo and Redo](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#supporting-undo-and-redo)
* [Progress Dialogs for Slow Operations](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python?application_version=5.7#progress-dialogs-for-slow-operations)
