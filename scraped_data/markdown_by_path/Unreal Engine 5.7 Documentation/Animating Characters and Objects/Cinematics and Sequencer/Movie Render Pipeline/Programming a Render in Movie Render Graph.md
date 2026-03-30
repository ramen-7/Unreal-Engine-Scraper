<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7 -->

# Programming a Render in Movie Render Graph

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
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Movie Render Pipeline](/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine "Movie Render Pipeline")
8. Programming a Render in Movie Render Graph

# Programming a Render in Movie Render Graph

Movie render graph scripting and concept discussion.

![Programming a Render in Movie Render Graph](https://dev.epicgames.com/community/api/documentation/image/01d965bf-bac1-4ff5-a809-20023657dfba?resizing_type=fill&width=1920&height=335)

 On this page

This document focuses on Scripting with **Movie Render Graph** which is the successor of **Movie Render Queue**. Movie Render Graph (**MRG**) features a similar feature set to **MRQ** but configuration files are backed by a graph editor. The functionality in Queues and Executors is shared between both systems, but the actual Movie Config and Rendering is now split into two systems that use different Configurations and Functions.

The full runnable scripts and more examples will be available inside of `MovieGraphEditorExample.py` and `MovieGraphEditorExampleHelpers.py` which will be located in the folder `/Engine/Plugins/MovieScene/MovieRenderPipeline/ Content/Python/` and is at the moment attached at the end of the course for the time being. In this document we will be referring to code snippets from the python code and discuss the new concepts within the Movie Render Graph that we should be aware of.

#### Prerequisites

* Familiarize yourself with Movie Render Queue and Movie Render Graph documentation before continuing:

  + [Movie Render Queue](/documentation/404)
  + [Movie Render Graph](/documentation/404)
* A Level Sequence and a Level to render (Shot)

## Simple Automation Example

The simplest way to render the same shots in an automated way repeatedly is by saving render jobs with specific settings in a Movie Pipeline Queue. Queues organize render jobs, applying preset settings and job properties, which streamlines authoring and managing render jobs.

In the Movie Render Window make sure to either add jobs to render or load a queue. If not done already, in the settings column, choose "replace with graph" and choose the created Movie Graph Setting. In Movie Render Queue Window under the section “Movie Graph Variables” you should see the exposed variable “Custom Output Resolution”

### Creating the Movie Graph Config UAsset

Let's first create an example graph that will help running our code examples. Our Config is based on the default Movie Render Graph Asset which you can either create by running the following snippet which will place a graph in `/Game/MyTests/IntermediateConfig`

```
import MovieGraphCreateConfigExample

MovieGraphCreateConfigExample.CreateIntermediateConfig()
Copy full snippet
```

or you can create one manually through the Content Browser by right clicking and selecting "Cinematics > Movie Render Graph Config" and applying the following 2 changes.

* On the "Global Output Settings" Node expose the `OutputResolution` by right clicking the node and selecting the checkbox in the context menu
* Expose the Output Resolution to a variable by right mouse clicking the `OutputResolution` pin of the "Global Output Settings" Node and selecting “promote to variable”

Your graph should look similar to this.

If you use the script, visually all nodes will turn entangled, you can just move them apart.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e3d405fe-666c-43d2-bbab-a8c1c2083264/image_0.png)

## Modifying User Exposed Parameters

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/851a0fd0-912f-4dc1-a1df-45815f2ff0dc/image_1.png)

With the new Movie Render Graph we now have the ability to surface per-property overrides as user parameters which are directly overridable in the details panel of the job, similar to how it’s done in Blueprints. Previously, we could only achieve this by creating our own variant of a MoviePipelineExecutorJob in C++ which required maintaining additional code and rebuilding the Editor. Furthermore you could only have one version of an Executor Job definition, which was less ideal for bigger projects that needed different attributes exposed for different kinds of renders. The graph makes it further easy for artists to directly see in the graph what path’s are taken when properties are modified.

In the next snippet we are going to override the exposed variable `CustomOutputRes` which appears on the Movie Render Queue Panel of the job.

```
def set_user_exposed_variables(job:unreal.MoviePipelineExecutorJob):

    """Find user exposed variable CustomOutputResolution and modify"""

    graph = job.get_graph_preset()

    variables = graph.get_variables()

    if not variables:

        print("No variables are exposed on this graph, expose 'CustomOutputResolution' to test this example")

    for variable in variables:

        if variable.get_member_name() == "CustomOutputRes":

            # Get Variable Assignments on Graphs or subgraphs 

            variable_assignment = job.get_or_create_variable_overrides(graph)

            # Set new Value

            variable_assignment.set_value_serialized_string(variable, 

                unreal.MovieGraphLibrary.named_resolution_from_profile("720p (HD)").export_text())

            # Enable override toggle

            variable_assignment.set_variable_assignment_enable_state(variable, True)
Copy full snippet
```

Discussion:

We first get the graph preset and iterate through the variables until we find "CustomOutputResolution", which we exposed in our graph, to override the render resolution of the rendered images. After that we set the new CustomOutputResolution attribute to a new resolution “720p”, and finally we set the enable state of the variable so that our override is actually applied.

If you wanted to test this on the job that you have in your Queue, you can grab a reference to a job, for example the first one in your queue, and run this function.

```
#Get The queue subsystem to access the current queue

subsytem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)

pipeline_queue = subsytem.get_queue()

#Get the first job

job = pipeline_queue.get_jobs()[0]

#test our function, this should change the user exposed variable

set_user_exposed_variables(job)
Copy full snippet
```

If your code is successful, it will set the `Custom Output Resolution` To 720p (HD) - 1280x720.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/243dba15-c1e6-448e-a325-976c488e3413/image_2.png)

## Modifying Default Parameters of Graph Node Settings

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f750a05-8c00-45fb-a4ac-8a5703061890/image_3.png)

Even though the recommended way of managing overrides is to expose graph variables and hook them to the graph logic, you might have situations where you need to override settings directly on the nodes themselves. In other words, you might not have exposed user variables, but still want to modify the default values.

```
@staticmethod

def set_global_output_settings_node(job:unreal.MoviePipelineExecutorJob):

    '''

    This example demonstrates how to make a modification to the global Output Settings

    Node to edit the default values. If you are interseted in just overriding some exposed

    values, check the "set_user_exposed_variables" which is a more appropiate workflow

    for per-job overrides.

    Note: This is modifiying the actual shared graph asset and dirtying it.

    '''

    # Get the Graph Asset from the Job that we want to search for the Output Settings Node

    graph = job.get_graph_preset()

    # Get the Globals Output Node

    globals_pin_on_output = graph.get_output_node().get_input_pin("Globals")

    # Assume that the Output Settings Node is connected to the Globals Pin

    output_settings_node = globals_pin_on_output.get_connected_nodes()[0]

    

    if not isinstance(output_settings_node, unreal.MovieGraphGlobalOutputSettingNode):

        unreal.log("This example expected that the Global Output Settings node is plugged into the Globals Node")

        return

    output_settings_node.set_editor_property("override_output_resolution", True)

    # Override output resolution

    output_settings_node.set_editor_property("output_resolution", 

                unreal.MovieGraphLibrary.named_resolution_from_profile("720p (HD)"))
Copy full snippet
```

In this example we first used the input pin of the "Globals" node as our entry point, and assumed that the connected node is `MovieGraphGlobalOutputSettingNode` which we created in this example.

To focus this example on the override of settings, we assume that the Input to the Globals (Outputs Node) is the Global Output Settings Node.

To test setting the global output settings node, you can run the following snippet which should set the resolution on the "Global Output Settings" node.

```
#Get The queue subsystem to access the current queue

subsytem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)

pipeline_queue = subsytem.get_queue()

#Get the first job

job = pipeline_queue.get_jobs()[0]

#test our function, this should change the user exposed variable

set_global_output_settings_node(job)
Copy full snippet
```

## Movie Graph Traversal

This is an example of how you traverse your graph settings to visit every node using a depth first search. In the following example, we use the Globals nodes Pin as a starting point to search from right to left until we exhaust all nodes.

```
graph = unreal.load_asset("/Game/YourGraph.YourGraph")

output_node = graph.get_output_node()

visisted = set()

def dfs(node, visisted=None):

    visited.add(node.get_name())

    print(node)

    

    #Different node have different number of input nodes and names

    if isinstance(node, unreal.MovieGraphSubgraphNode) or isinstance(node, unreal.MovieGraphOutputNode):

        pins = [node.get_input_pin("Globals"), node.get_input_pin("Input")]

    elif isinstance(node, unreal.MovieGraphBranchNode):

        pins = [node.get_input_pin("True"), node.get_input_pin("False")]

    elif isinstance(node, unreal.MovieGraphSelectNode):

        pins = [node.get_input_pin("Default")]

    else:

        pins = [node.get_input_pin("")]

    #Iterate over the found pins

    for pin in pins:

        if pin:

            for neighbour in pin.get_connected_nodes():

                dfs(neighbour, visited)

dfs(output_node)
Copy full snippet
```

Having a graph as shown in the image below, we are traversing the nodes and using the "pins" to find the next nodes to process. As different node types can have named pins, we need to keep a list of these properties when encountering a specific node type such as the `MovieGraphBranchNode` which we need to search for both the "True" and "False" Pins recursively. Nodes with a single input will only have an empty string on the pin.

![ImageAltText](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b76d33a8-34f8-4c8a-864a-3fcbc3c3a3bd/image_4.png)


Graph Traversal will be one of the focus areas in the next release to make it easier to visit nodes with less code.

Additional examples on Graph operations can be found inside of `Content/Python/MovieGraphCreateConfigExample.py`.

## Additional Movie Render Graph Examples

Attached are two Python files that cover additonal functionality and usage cases with comments. You can import both and study their logic. The `MovieGraphEditorExample.py` offers a complete scripted example of how to create an automation, while reusable functions can be found in the `MovieGraphEditorExample.py` file.

```
# Copyright Epic Games, Inc. All Rights Reserved.

# These examples showcase how to use scripting with movie render graph

import unreal

import MovieGraphCreateConfigExample as graph_helper

import MovieGraphEditorExampleHelpers

# USAGE:

#   - Requires the "Python Editor Script Plugin" to be enabled in your project.

#   In the main() function, you'll find examples demonstrating how to load and 

#   modify a modify movie graphs, overwrite exposed variables and peform other 

#   operations related to the Movie Render Graph

#

#   Make sure to change the "Assets to load" section to point to your own 

#   Movie Render Queue and Movie Graph Config Assets

'''

Python Globals to keep the UObjects alive through garbage collection.

Must be deleted by hand on completion.

'''

subsystem = None

executor = None

def render_queue(queue_to_load:unreal.MoviePipelineQueue=None, 

                 graph_to_load: unreal.MovieGraphConfig=None):

    """

    This example demonstrates how to:

    - load a queue or use the current queue

    - Set a graph Config as a Preset

    - Add a simple executor finished callback 

    """

    # Get the subsystem to interact with the Movie Pipeline Queue

    subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)

    # Load the provided Queue Asset if provided, otherwise use the active Queue  

    if queue_to_load:

        if subsystem.load_queue(queue_to_load, prompt_on_replacing_dirty_queue=False):

            unreal.log("Loaded specified queue")

    

    # Get a reference to the active Queue

    pipeline_queue = subsystem.get_queue()

    

    if not pipeline_queue.get_jobs():

        unreal.log("There are no jobs in the Queue.")

        return

        

    # For each job we can start modifying the job parameters such as accessing

    # the graph preset of the job, modifying values

    for job in pipeline_queue.get_jobs():

        #Make sure we are working with a job graph config for this example

        if not job.get_graph_preset():

            unreal.log("A Graph Config needs to be specified for this example)")

            return

        

        if graph_to_load:

            job.set_graph_preset(graph_to_load)

        # A collection of job operation examples can be found in 

        MovieGraphEditorExampleHelpers.advanced_job_operations(job)

    # We are using the globals keyword to indicate that the executor belongs to the 

    # global scope to avoid it being garbage collected after the job is finished rendering

    global executor

    executor = unreal.MoviePipelinePIEExecutor(subsystem)

    

    # When the render jobs are done, execute the callback on_queue_finished_callback

    executor.on_executor_finished_delegate.add_callable_unique(

        MovieGraphEditorExampleHelpers.on_queue_finished_callback

    )

 

    # Start Rendering, similar to pressing "Render" in the UI, 

    subsystem.render_queue_with_executor_instance(executor)

def allocate_render_job(config_to_load: unreal.MovieGraphConfig=None):

    '''

    Allocates new job and populates it's parameters before kicking off a render

    '''

    # Get The current Queue

    subsytem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)

    pipeline_queue = subsytem.get_queue()

    # Delete existing jobs to clear the current Queue

    pipeline_queue.delete_all_jobs()

    job = pipeline_queue.allocate_new_job(unreal.MoviePipelineExecutorJob)

    

    # To override Job Parameters check 

    # MovieGraphEditorExampleHelpers.set_job_parameters(job)

    

    if config_to_load:

        job.set_graph_preset(config_to_load)

    subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)

    executor = unreal.MoviePipelinePIEExecutor(subsystem)

    subsystem.render_queue_with_executor_instance(executor)

def render_queue_minimal():

    '''This an MVP example on how to render a Queue which already has jobs allocated

    A more exhaustive example covering overrides can be found in the function render_queue

    '''

    subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)

    executor = unreal.MoviePipelinePIEExecutor(subsystem)

    subsystem.render_queue_with_executor_instance(executor)

def main():

    """We are showcasing how to render a queue (render_queue) and also how to create 

    a job from scratch without initially creating a queue. (allocate_render_job) 

    Run these examples independently. 

    """

    # Creates A Graph Asset called "Example" in /Game/MyTests/IntermediateConfig 

    # that exposes the output resolution as a user variable 

    created_graph = graph_helper.CreateIntermediateConfig()

    # Render a Queue with a saved Queue Asset, Add Executor Callbacks, you can pass

    # a Movie Render Queue Asset or just make sure you have jobs in a Movie Render Queue

    render_queue()

    # This function creates a job in the Queue by allocating a new MoviePipelineJob, 

    # You can also pass in config_to_load to set a graph config and finally start's the render

    allocate_render_job()

if __name__ == "__main__":

    unreal.log("Check the main() function for examples")
Copy full snippet
```

MovieGraphEditorExample.py

```
# Copyright Epic Games, Inc. All Rights Reserved.

#

#

# Helper functions for the Movie Render Graph, each function is a static method

# which helps testing individual functions in isolation. This module is used

# in the MovieGraphEditorExample.py

import unreal

@staticmethod

def on_queue_finished_callback(executor: unreal.MoviePipelineExecutorBase, success: bool):

    """Is called after the executor has finished rendering all jobs

    Args:

        success (bool): True if all jobs completed successfully, false if a job 

                        encountered an error (such as invalid output directory)

                        or user cancelled a job (by hitting escape)

        executor (unreal.MoviePipelineExecutorBase): The executor that run this queue

    """

    unreal.log("on_queue_finished_callback Render completed. Success: " + str(success))

@staticmethod

def set_global_output_settings_node(job:unreal.MoviePipelineExecutorJob):

    '''

    This example demonstrates how to make a modification to the global Output Settings

    Node to edit the default values. If you are interested in just overriding some exposed

    values, check the "set_user_exposed_variables" which is a more appropiate workflow

    for per-job overrides.

    Note: This is modifiying the actual shared graph asset and dirtying it.

    '''

    # Get the Graph Asset from the Job that we want to search for the Output Settings Node

    graph = job.get_graph_preset()

    # Get the Globals Output Node

    globals_pin_on_output = graph.get_output_node().get_input_pin("Globals")

    # Assume that the Output Settings Node is connected to the Globals Pin

    output_settings_node = globals_pin_on_output.get_connected_nodes()[0]

    

    if not isinstance(output_settings_node, unreal.MovieGraphGlobalOutputSettingNode):

        unreal.log("This example expected that the Global Output Settings node is plugged into the Globals Node")

        return

    output_settings_node.set_editor_property("override_output_resolution", True)

    # Override output resolution

    output_settings_node.set_editor_property("output_resolution", 

                unreal.MovieGraphLibrary.named_resolution_from_profile("720p (HD)"))

@staticmethod

def set_job_parameters(job:unreal.MoviePipelineExecutorJob):

    """This function showcases how job Parameters can be set or modified. By

    using the set_editor_property method, we ensure that the changes mark the Queue 

    as dirty

    Args:

        job (unreal.MoviePipelineExecutorJob): the Pipeline Job to be modified

    """

    job.set_editor_property("sequence", unreal.SoftObjectPath('/Game/Levels/shots/shot0010/shot0010.shot0010'))

    job.set_editor_property("map", unreal.SoftObjectPath('/Game/Levels/Main_LVL.Main_LVL'))

    job.set_editor_property("job_name", "shot0010")

    job.set_editor_property("author", "Automated.User")

    job.set_editor_property("comment", "This comment was created through Python")

@staticmethod

def set_user_exposed_variables(job:unreal.MoviePipelineExecutorJob):

    """Finds the user exposed variable CustomOutputResolution and modifies it

    Args:

        job (unreal.MoviePipelineExecutorJob): the Pipeline Job which we will 

                                        use to find the graph preset to modify

    """

    graph = job.get_graph_preset()

    variables = graph.get_variables()

    if not variables:

        print("No variables are exposed on this graph, expose 'CustomOutputResolution' to test this example")

    for variable in variables:

        if variable.get_member_name() == "CustomOutputRes":

            # Get Variable Assignments on Graphs or subgraphs 

            variable_assignment = job.get_or_create_variable_overrides(graph)

            # Set new Value

            variable_assignment.set_value_serialized_string(variable, 

                unreal.MovieGraphLibrary.named_resolution_from_profile("720p (HD)").export_text())

            # Enable override toggle

            variable_assignment.set_variable_assignment_enable_state(variable, True)

@staticmethod

def duplicate_queue(pipeline_queue:unreal.MoviePipelineQueue):

    """

    Duplicating a queue is desirable in an interactive session, especially when you 

    want to modify a copy of the Queue Asset instead of altering the original one.

    Args:

        queue (unreal.MoviePipelineQueue): The Queue which we want to duplicate

    """

    new_queue = unreal.MoviePipelineQueue()

    new_queue.copy_from(pipeline_queue)

    pipeline_queue = new_queue

    return pipeline_queue 

@staticmethod

def advanced_job_operations(job:unreal.MoviePipelineExecutorJob):

    """

    Wrapper function that runs the following functions on the current job

    - set_job_parameters

    - set_user_exposed_variables

    - set_global_output_settings_node

    Args:

        job (unreal.MoviePipelineJob): The current processed Queue Job

    """

    if not job.get_graph_preset():

        unreal.log("This Job doesn't have a graph type preset, add a graph preset to the job to test this function")

        return

    # Set Job parameters such as Author/Level/LevelSequence

    set_job_parameters(job)

    # Set user exposed variables on the Graph config

    set_user_exposed_variables(job)

    

    # Set attributes on the actual graph's nodes directly, this is like

    # setting the default values

    set_global_output_settings_node(job)

@staticmethod

def traverse_graph_config(graph:unreal.MovieGraphConfig):

    """Demonstrates how we can use depth first search to visit all the nodes starting

    from the "Globals" pin and navigating our way to the left until all nodes are 

    exhausted

    Args:

        graph (unreal.MovieGraphConfig): The graph to operate on

    """

    visited = set()

    def dfs(node, visisted=None):

        visited.add(node.get_name())

        

        # Nodes can have different number of input nodes and names which we need to collect

        if isinstance(node, unreal.MovieGraphSubgraphNode) or isinstance(node, unreal.MovieGraphOutputNode):

            pins = [node.get_input_pin("Globals"), node.get_input_pin("Input")]

        elif isinstance(node, unreal.MovieGraphBranchNode):

            pins = [node.get_input_pin("True"), node.get_input_pin("False")]

        elif isinstance(node, unreal.MovieGraphSelectNode):

            pins = [node.get_input_pin("Default")]

        else:

            pins = [node.get_input_pin("")]

        # Iterate over the found pins

        for pin in pins:

            if pin:

                for neighbour in pin.get_connected_nodes():

                    dfs(neighbour, visited)
Copy full snippet
```

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [movie render queue](https://dev.epicgames.com/community/search?query=movie%20render%20queue)
* [render](https://dev.epicgames.com/community/search?query=render)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#prerequisites)
* [Simple Automation Example](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#simpleautomationexample)
* [Creating the Movie Graph Config UAsset](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#creatingthemoviegraphconfiguasset)
* [Modifying User Exposed Parameters](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#modifyinguserexposedparameters)
* [Modifying Default Parameters of Graph Node Settings](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#modifyingdefaultparametersofgraphnodesettings)
* [Movie Graph Traversal](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#moviegraphtraversal)
* [Additional Movie Render Graph Examples](/documentation/en-us/unreal-engine/programming-a-render-in-mrg-in-unreal-engine?application_version=5.7#additionalmovierendergraphexamples)
