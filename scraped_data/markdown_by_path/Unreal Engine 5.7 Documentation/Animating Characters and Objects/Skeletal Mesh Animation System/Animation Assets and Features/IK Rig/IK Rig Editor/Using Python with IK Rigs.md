<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7 -->

# Using Python with IK Rigs

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
7. [Animation Assets and Features](/documentation/en-us/unreal-engine/animation-assets-and-features-in-unreal-engine "Animation Assets and Features")
8. [IK Rig](/documentation/en-us/unreal-engine/unreal-engine-ik-rig "IK Rig")
9. [IK Rig Editor](/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine "IK Rig Editor")
10. Using Python with IK Rigs

# Using Python with IK Rigs

Use Python scripting to create and edit IK Rigs to automate workflows.

![Using Python with IK Rigs](https://dev.epicgames.com/community/api/documentation/image/b5116b47-534a-45b0-843e-4b93d4912cc7?resizing_type=fill&width=1920&height=335)

 On this page

When creating and using [IK Rigs](/documentation/en-us/unreal-engine/unreal-engine-ik-rig) to animate characters and objects in **Unreal Engine**, you can use custom [Python scripting](/documentation/404) to control and automate IK Rigs asset workflows.

This document provides an overview and example python scripts you can reference and use to edit and interface with IK Rig assets.

## Overview

An IK Rig is a set of controls and solvers that can apply motion data to a skeletal mesh asset in Unreal Engine. IK Rigs consists of multiple parts:

* A Hierarchy of **bones**, **goals**, **goal settings**, and **bone settings**.
* A list of [IK Solvers](/documentation/en-us/unreal-engine/ik-rig-solvers-in-unreal-engine) that influence the Hierarchy's bones and their relationship to one another.

  + Goals are used to drive the IK Solvers, while goal settings and bone settings are used to define the Solver's behaviors.
* A **Retarget Root** and a list of **Retarget Chains** used for [IK Retargeting](/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine).
* A preview scene used exclusively for an in editor preview.

The IK Rig system is constructed using a Model > View > Controller design formula. The data model itself using the following terminology:

* **Solver**: Which contains the **Inverse Kinematic** solution to rotating and positioning bones in a chain. Multiple Solvers can also be used at the same time to further customize the effect of the IK on the final pose.
* **Goal**: Serves as the **effector point** for your IK chains. Goals are used in conjunction with Solvers to modify an incoming pose to reach the goal locations. Goals can be assigned to multiple solvers.
* **Goal Settings**: Solver specific settings that exist within the IK goal. For each solver assignment to a Goal, there is a different solver specific settings object.
* **Bone Settings**: Solver specific settings that exist within the Bone. For each solver assignment to a Bone, there is a different solver specific settings object.
* **Retarget Root**: The root of the character motion that would be used to transfer from a source to a target.
* **Retarget Chains**: A chain of bones that are defined in order to transfer the motion from a source to a target.

## Accessing the IK Rig

The first step when scripting against any IK Rig is to gain access to the main object you'll interact with, or set the `The IKRigDefinition`. There are several ways to do that depending on your situation. The following examples will illustrate how you can define the IK Rig object using Python scripts.

### Loading an existing IKR asset

To access an existing IK Rig asset (`ikr`) you can simply load the asset using the following example script:

```
import unreal

# Ensure the file path is correct for the location of your asset in your project.

ikr = unreal.load_asset(name = '/Game/Characters/Mannequins/Rigs/IK_Mannequin', outer = None)

Copy full snippet
```

## Create a new IKR asset

To create a new IK Rig asset you can use the following factory:

```
# Get the asset tools.

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Create an IK Rig in the location defined by the file path. For example: ` …/Game/IK_Mannequin`.

ikr = asset_tools.create_asset(asset_name='IK_Mannequin',

package_path='/Game/', asset_class=unreal.IKRigDefinition,

factory=unreal.IKRigDefinitionFactory())

Copy full snippet
```

## Editing an IK Rig

### Preparing for an Edit by Accessing the Controller

The controller is the central object you can use to make any change to the IK Rig. The controller has many functions that you can use to make edits. The following examples are a subset of methods you can use Python scripting to make edits to IK Rig assets:

```
# Get the IK Rig controller.

ikr_controller = unreal.IKRigController.get_controller(ikr)

Copy full snippet
```

### Assigning a Skeletal Mesh in a new IK Rig

When creating a new IK Rig, you will need to assign it a skeletal mesh. You can use the following Python scripts to load, assign, a skeletal mesh asset to an IK Rig as well as reference, or get a Skeletal Mesh asset assigned to an IK Rig.

```
# Load the Skeletal Mesh asset.

skel_mesh = unreal.load_asset(name = '/Game/Characters/Mannequins/Meshes/SKM_Manny_Simple')

# Assign Skeletal Mesh asset to the IK Rig.

ikr_controller.set_skeletal_mesh(skel_mesh)

# Get the Skeletal Mesh assigned to the IK Rig.

set_mesh = ikr_controller.get_skeletal_mesh()

Copy full snippet
```

### Auto Retarget Chains and Auto FBIK

From the controller, you can apply the commands to automatically generate Retarget Chains and a Full Body IK solver with goals. The auto generation is based on commonly known bipedal skeletons.

```
# Apply auto generated retarget chains from commonly known biped skeletons
ikr_controller.apply_auto_generated_retarget_definition()


# Apply auto generated Full Body IK solver from commonly known biped skeletons
ikr_controller.apply_auto_fbik()
Copy full snippet
```

### Adding, Editing, and Querying IK Solvers

You can easily add different IK Solvers via the controller. Adding a solver requires specifying the **IK Rig Solver** class. This is required since there can be custom IK Rig solvers that are used in a project. As long as the base class is a `IKRigSolver`, any class input will work.

```
# Add a FBIK, Body Mover, Limb, Pole, and Set Transform Solver to the IK Rig.

fbik_index = ikr_controller.add_solver(unreal.IKRigFBIKSolver)

bodymover_index = ikr_controller.add_solver(unreal.IKRig_BodyMover)

limb_index = ikr_controller.add_solver(unreal.IKRig_LimbSolver)

pole_index = ikr_controller.add_solver(unreal.IKRig_PoleSolver)

settransform_index = ikr_controller.add_solver(unreal.IKRig_SetTransform)

Copy full snippet
```

When adding a solver, the controller will output a solver index. This index determines the solver order of which the IK Rig will solve. You can use the Index to toggle the solver's operation state, move solvers in the stack, or remove a specific solver.

```
# Enable or Disable a specific solver.

ikr_controller.set_solver_enabled(bodymover_index, False)

# Move a solver.

ikr_controller.move_solver_in_stack(bodymover_index, limb_index)

# Remove a solver.

ikr_controller.remove_solver(bodymover_index)

ikr_controller.remove_solver(limb_index)

ikr_controller.remove_solver(pole_index)

ikr_controller.remove_solver(settransform_index)

Copy full snippet
```

You can also query for the solver index or for all solvers in the IK Rig using the following scripts:

```
# Get the IK Rig Controller's first solver in the Index.

fbik_solver = ikr_controller.get_solver_at_index(fbik_index)

# Getting how many solvers associated with the IK Rig Controller.

num_solvers = ikr_controller.get_num_solvers()

Copy full snippet
```

### Setting Root Bone of Solver

For a solver to work, it requires a Root Bone to start the solve. This will require the solver index to set the root bone. You can set the Root Bone for the solver using the following scripts:

```
# Set and get the Root Bone of the first solver.

ikr_controller.set_root_bone("pelvis", 0)

root_bone = ikr_controller.get_root_bone(0)

Copy full snippet
```

### Adding/Editing/Querying IK Goals

Goals are required in order to drive an IK Solver. Goals can be added with or without a goal bone and can be renamed.

```
# Add goals to the IK Rig. You can also assign a bone during creation.

ikr_controller.add_new_goal("hand_l_goal", None)

ikr_controller.add_new_goal("TEMP_hand_r_goal", "hand_r")

# Assign a bone to an existing goal.

# You can also query for the goal in a bone and vice versa.

ikr_controller.set_goal_bone("hand_l_goal", "hand_l")

ikr_controller.get_goal_name_for_bone("hand_l")

ikr_controller.get_bone_for_goal("hand_l_goal")

# Rename goals.

ikr_controller.rename_goal("TEMP_hand_r_goal", "hand_r_goal")

# Remove a goal.

ikr_controller.remove_goal("hand_r_goal")

Copy full snippet
```

You can also query for all the goals in the IK Rig.

```
# Get all goals in IK Rig.

ikr_controller.get_all_goals()

Copy full snippet
```

For editing goal properties, you can get the goal object and edit any of the editor properties.

```
# Get goal object, and set the position alpha.

goal = ikr_controller.get_goal("hand_r_goal")

goal.set_editor_property("position_alpha", 0.5)

new_alpha = goal.get_editor_property("position_alpha")

Copy full snippet
```

### Connecting Goals to a Solver

Now that goals have been added, you will need to connect them to a solver. You can check if a goal is connected to a solver before connecting it.

```
# Check if the goal is connected to any solver or a specific solver.

ikr_controller.is_goal_connected_to_any_solver("hand_r_goal")

ikr_controller.is_goal_connected_to_solver("hand_r_goal", 0)

# Connect or disconnect goals from a solver.

ikr_controller.connect_goal_to_solver("hand_r_goal", 0)

ikr_controller.disconnect_goal_from_solver("hand_r_goal", 0)

Copy full snippet
```

### Adding/Editing/Querying Goal and Bone Settings

Once you have connected the goal to a solver, you can access the goal settings to that specific goal. Each connection between a goal and a solver will have its own specific settings.

In the following example, the `hand_r_goal` is connected to a FBIK solver and a Body Mover solver, thus it would have two different goal settings that are each associated with the corresponding solver.

```
# Get the specific settings for the goal by inputting the goal name and solver.

hand_r_goal_settings = ikr_controller.get_goal_settings_for_solver("hand_r_goal", 0)

# Edit the specific effector setting's properties.

hand_r_goal_settings.pull_chain_alpha = 0

hand_r_goal_settings.strength_alpha = 1

Copy full snippet
```

Solvers can optionally support per-bone settings, however not all solvers will require this. Of the solvers that IK Rig ships with, only the FBIK solver has per-bone settings. The example setup for this is similar to what was previously covered with goal settings.

```
# Add bone settings to the arms.

ikr_controller.add_bone_setting("lowerarm_l", 0)

ikr_controller.add_bone_setting("lowerarm_r", 0)

ikr_controller.add_bone_setting("clavicle_l", 0)

ikr_controller.add_bone_setting("clavicle_r", 0)

# Get bone settings.

left_lowerarm_setting = ikr_controller.get_bone_settings("lowerarm_l", 0)

right_lowerarm_setting = ikr_controller.get_bone_settings("lowerarm_r", 0)

left_clav_setting = ikr_controller.get_bone_settings("clavicle_l", 0)

right_clav_setting = ikr_controller.get_bone_settings("clavicle_r", 0)

# Set the preferred angles and rotation stiffness.

left_lowerarm_setting.use_preferred_angles = True

left_lowerarm_setting.preferred_angles = unreal.Vector(0,0,90)

right_lowerarm_setting.use_preferred_angles = True

right_lowerarm_setting.preferred_angles = unreal.Vector(0,0,90)

left_clav_setting.rotation_stiffness = 1

right_clav_setting.rotation_stiffness = 1

Copy full snippet
```

### Checking for compatibility with other Skeletal Meshes

IK Rigs are skeleton agnostic, which means that you can share IK Rigs across similar skeleton hierarchies. With Python, you can check the mesh compatibility of an IK Rig by using a simple command.

```
# Check if this IK Rig is compatible with a defined Skeletal Mesh.

compatible_skel_mesh = unreal.load_asset(name = '/Game/Characters/Mannequins/Meshes/SKM_Quinn_Simple')

print(ikr_controller.is_skeletal_mesh_compatible(compatible_skel_mesh))

Copy full snippet
```

### Adding, Editing, and Querying Retarget Roots and Chains

For setting up an IK Rig for a Retarget, it needs to have a Retarget Root and Retarget Chains. These can be authored using the following example Python scripts.

```
# Set or Get the Retarget Root.

ikr_controller.set_retarget_root("pelvis")

retarget_root = ikr_controller.get_retarget_root()

Copy full snippet
```

For retarget chains, you can author them without inputting a start bone, end bone, or a goal. These can be added to the chain at a later time if necessary.

```
# Add a Retarget Chain with a start bone, end bone, and goal.

ikr_controller.add_retarget_chain("LeftArm", "upperarm_l", "hand_l", "hand_l_goal")

# Add a Retarget Chain

ikr_controller.add_retarget_chain("TEMP_RightArm", "", "", "")

# Rename a Retarget Chain.

ikr_controller.rename_retarget_chain("TEMP_RightArm", "RightArm")

# Set the Retarget Chain's start bone, end bone, and goal.

ikr_controller.set_retarget_chain_start_bone("RightArm", "upperarm_r")

ikr_controller.set_retarget_chain_end_bone("RightArm", "hand_r")

ikr_controller.set_retarget_chain_goal("RightArm", "hand_r_goal")

# Get the Retarget Chain's start bone, end bone, and goal.

ikr_controller.get_retarget_chain_start_bone("RightArm")

ikr_controller.get_retarget_chain_end_bone("RightArm")

ikr_controller.get_retarget_chain_goal("RightArm")

# Remove a Retarget Chain.

ikr_controller.remove_retarget_chain("RightArm")

Copy full snippet
```

You can query for all the Retarget Chains in the IK Rig.

```
# Get all Retarget Chains in IK Rig.

all_retarget_chains = ikr_controller.get_retarget_chains()

Copy full snippet
```

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [python](https://dev.epicgames.com/community/search?query=python)
* [ik rig](https://dev.epicgames.com/community/search?query=ik%20rig)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#overview)
* [Accessing the IK Rig](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#accessingtheikrig)
* [Loading an existing IKR asset](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#loadinganexistingikrasset)
* [Create a new IKR asset](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#createanewikrasset)
* [Editing an IK Rig](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#editinganikrig)
* [Preparing for an Edit by Accessing the Controller](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#preparingforaneditbyaccessingthecontroller)
* [Assigning a Skeletal Mesh in a new IK Rig](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#assigningaskeletalmeshinanewikrig)
* [Auto Retarget Chains and Auto FBIK](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#autoretargetchainsandautofbik)
* [Adding, Editing, and Querying IK Solvers](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#adding,editing,andqueryingiksolvers)
* [Setting Root Bone of Solver](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#settingrootboneofsolver)
* [Adding/Editing/Querying IK Goals](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#adding/editing/queryingikgoals)
* [Connecting Goals to a Solver](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#connectinggoalstoasolver)
* [Adding/Editing/Querying Goal and Bone Settings](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#adding/editing/queryinggoalandbonesettings)
* [Checking for compatibility with other Skeletal Meshes](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#checkingforcompatibilitywithotherskeletalmeshes)
* [Adding, Editing, and Querying Retarget Roots and Chains](/documentation/en-us/unreal-engine/using-python-to-create-and-edit-ik-rigs-in-unreal-engine?application_version=5.7#adding,editing,andqueryingretargetrootsandchains)
